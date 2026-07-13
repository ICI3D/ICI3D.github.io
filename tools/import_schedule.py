#!/usr/bin/env python3
"""One-shot migration: an MMED Liquid-wall schedule (schedule/<year>/index.md) -> cohort YAML (#54).

This is a MIGRATION tool, run once per cohort, NOT the live renderer. Its contract is the one
the design rests on: it NEVER silently drops a line. Every source bullet becomes either a typed
session / day-level link / day-level note, or a `kind: todo` row carrying the original text verbatim.
A `todo` parses under the schema but HARD-FAILS Tier 1, so CI turns every line the importer could not
confidently map into a concrete, addressable error for a human to triage (vs. today's silent failures).

    python3 tools/import_schedule.py schedule/2025/index.md --year 2025 \
        --clinic mmed --status published -o _data/schedule/mmed/2025.yml

Then validate the result:
    python3 tools/validate_schedule.py _data/schedule/mmed/2025.yml
"""
from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path

import yaml

# ---- {{ token }} vocabulary (from the assign preamble) -> closed kind enum ----
KIND = {
    "lect": ("lecture", {}), "glect": ("lecture", {"guest": True}),
    "disc": ("discussion", {}),
    "prac": ("computer-session", {}), "labex": ("computer-session", {}),
    "labs": ("computer-session", {}), "rtut": ("computer-session", {}),
    "ex": ("activity", {}),
    "gw": ("group-work", {}),
    "lc": ("live-coding", {}), "pc": ("live-coding", {}),
    "sc": ("social", {}),
    "org": ("organizing", {}),
    "post": ("poster", {}),
    "catch": ("activity", {}), "proj": ("activity", {}),
}
MEAL = {"bfast": "breakfast", "ssbfast": "breakfast", "lunch": "lunch",
        "dinner": "dinner", "ssdinner": "dinner"}
LOGISTIC = {"coffee": "coffee", "tea": "tea", "break": "break"}
LOC = {"main": "main-hall", "lab": "comp-lab", "breakout": "group-breakouts",
       "lobby": "lobby", "sections": "sections"}
LOCATIONS_LABEL = {"main-hall": "Main Hall", "comp-lab": "Comp. Lab",
                   "group-breakouts": "Group Breakouts", "lobby": "Lobby",
                   "sections": "Section 1 / Section 2"}
MONTHS = {m: i for i, m in enumerate(
    ["january", "february", "march", "april", "may", "june", "july", "august",
     "september", "october", "november", "december"], 1)}

RE_SUMMARY = re.compile(r"<summary[^>]*>(.*?)</summary>", re.I)
RE_DETAILS_OPEN = re.compile(r"<details[^>]*\bopen\b", re.I)
RE_DAY = re.compile(r"^#{2,3}\s*Day\s*([0-9A-Za-z]+)\s*(?:\(([^)]*)\))?\s*$", re.I)
RE_TIME = re.compile(r"^(\d{1,2})h(\d{2})\s*[-–]\s*(\d{1,2})h(\d{2})\s*(.*)$")
RE_TOKEN = re.compile(r"\{\{\s*(\w+)\s*\}\}")
RE_SHADOW = re.compile(r"\{:\s*\.shadow\s*\}")  # kramdown faculty-only marker; tolerates inner spaces
RE_PEOPLE = re.compile(r'people\s*=\s*"([^"]+)"')
RE_LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
RE_ANYLINK = re.compile(r"\[([^\]]+)\]\(([^)]*)\)")  # also matches empty-url [text]()
RE_DATEPROSE = re.compile(r"(\d{1,2})\s+([A-Za-z]+)")


def hhmm(h, m):
    return f"{int(h):02d}:{int(m):02d}"


def split_people(meta):
    """Pull instructor strings out of a trailing meta group like
    ({% include instructors people="a, b" %}, {{ main }}) or (everyone, {{ main }})."""
    people = []
    for grp in RE_PEOPLE.findall(meta):
        # the source separates co-instructors with both "," and "|"
        people += [x.strip() for x in re.split(r"[,|]", grp) if x.strip()]
    if not people:
        # bare names before the location token: strip tokens/includes, take leading words
        bare = RE_TOKEN.sub("", meta)
        bare = re.sub(r"\{%.*?%\}", "", bare)
        bare = bare.strip().strip("()").strip()
        for chunk in re.split(r"[,|]", bare):
            c = chunk.strip()
            if c and "include" not in c and "instructors" not in c:
                people.append(c)
    return people


def parse_meta_group(rest):
    """Given the text after the time range, separate (title+links) from the trailing
    ( ...people... {{ loc }} ) meta group. Returns (body_without_meta, location, people)."""
    location = None
    people = []
    # find the LAST parenthesised group that carries a location token, people=, or an instructors include
    best = None
    for mo in re.finditer(r"\(([^()]*(?:\([^()]*\)[^()]*)*)\)", rest):
        inner = mo.group(1)
        if RE_PEOPLE.search(inner) or "instructors" in inner or RE_TOKEN.search(inner) \
                or re.search(r"\b(everyone|all)\b", inner, re.I):
            best = mo
    if best:
        inner = best.group(1)
        toks = RE_TOKEN.findall(inner)
        location = next((LOC[t] for t in toks if t in LOC), None)
        people = split_people(inner)
        rest = (rest[:best.start()] + rest[best.end():]).strip()
    return rest, location, people


def parse_session(rest, source):
    """Build a session dict from the text after a time range (kind/title/links/people/location).

    Returns (sess, title, links, location, people, extra, is_todo). An undefined macro
    (a {{token}} that is not a known kind/meal/logistic/location, e.g. {{ mlect }}) is NOT
    silently coerced to a generic activity; it becomes a loud `todo` for a human to map.
    """
    toks = RE_TOKEN.findall(rest)
    kind = subtype = None
    extra = {}
    for t in toks:
        if t in KIND:
            kind, extra = KIND[t][0], dict(KIND[t][1])
            break
        if t in MEAL:
            kind, subtype = "meal", MEAL[t]
            break
        if t in LOGISTIC:
            kind = LOGISTIC[t]
            break
    unknown = [t for t in toks if t not in KIND and t not in MEAL and t not in LOGISTIC and t not in LOC]
    if kind is None and unknown:
        return {"kind": "todo", "source": source}, None, [], None, [], {}, True

    body, location, people = parse_meta_group(rest)
    body = re.sub(r"\{%.*?%\}", "", body)
    body = RE_TOKEN.sub("", body).strip()  # drop kind/loc tokens left in the title region

    # links: keep only non-empty urls; tidy {url} when display text duplicates the url
    links = []
    for (t, u) in RE_ANYLINK.findall(body):
        if u:
            links.append({"url": u} if t == u else {"text": t, "url": u})
    # title: inline each link's display text, drop urls and any leftover empty ()
    title = RE_ANYLINK.sub(lambda m: m.group(1), body)
    title = re.sub(r"\(\s*\)", "", title)
    title = re.sub(r"\s+", " ", title).strip(" -–·,")
    title = title or None

    if kind is None:
        kind = "activity"  # timed but no recognised token -> generic (the 33 untyped 2025 rows)

    sess = {"kind": kind}
    if subtype:
        sess["meal"] = subtype
    return sess, title, links, location, people, extra, False


def infer_dates(days, year):
    """Fill day['date'] from the prose in the header parens; carry forward +1 when absent."""
    from datetime import date, timedelta
    prev = None
    for d in days:
        iso = None
        prose = d.pop("_dateprose", "") or ""
        m = RE_DATEPROSE.search(prose)
        if m and m.group(2).lower() in MONTHS:
            iso = date(year, MONTHS[m.group(2).lower()], int(m.group(1)))
        elif prev is not None:
            iso = prev + timedelta(days=1)
        if iso is not None:
            d["date"] = iso.isoformat()
            prev = iso
        else:
            d["date"] = f"{year}-01-01"  # placeholder; Tier 0 still requires a real ISO date
            d.setdefault("_needs_date", True)


def parse(path, year):
    weeks = []
    cur_week = None
    cur_day = None
    last_session = None  # most recent timed session, so indented sub-bullets attach to it
    todos = 0

    def new_week(title, is_open):
        nonlocal cur_week, cur_day
        cur_week = {"title": title, "collapsible": True, "open": bool(is_open), "days": []}
        weeks.append(cur_week)
        cur_day = None

    def ensure_week():
        if cur_week is None:
            new_week("Schedule", False)
        return cur_week

    for raw in Path(path).read_text().splitlines():
        line = raw.rstrip()
        s = line.strip()
        if not s:
            continue

        msum = RE_SUMMARY.search(s)
        if msum:
            new_week(msum.group(1).strip(), bool(RE_DETAILS_OPEN.search(s)))
            last_session = None
            continue
        mday = RE_DAY.match(s)
        if mday:
            ensure_week()
            cur_day = {"label": ("Day " + mday.group(1) + (f" ({mday.group(2).strip()})" if mday.group(2) else "")),
                       "_dateprose": (mday.group(2) or ""), "sessions": []}
            cur_week["days"].append(cur_day)
            last_session = None
            continue

        if not s.startswith("- "):
            continue
        indented = raw[:1] in (" ", "\t")
        body = s[2:].strip()
        shadow = bool(RE_SHADOW.search(body))
        body = RE_SHADOW.sub("", body).strip()

        # an indented sub-bullet is a note on the PRECEDING session, not a day item
        if indented and last_session is not None and not RE_TIME.match(body):
            if body:
                last_session.setdefault("notes", []).append(
                    {"text": body, "shadow": True} if shadow else body)
            continue

        # top-level untimed bullet under a day -> a day-scoped link or note (never dropped)
        if cur_day is not None and not RE_TIME.match(body):
            only_link = RE_LINK.fullmatch(body)
            if only_link:
                cur_day.setdefault("links", []).append(
                    {"text": only_link.group(1).strip(), "url": only_link.group(2).strip()})
                continue
            cur_day.setdefault("notes", []).append(
                {"text": body, "shadow": True} if shadow else body)
            continue

        mt = RE_TIME.match(body)
        if not mt:
            # no day context and not a time row -> a TODO the human must place
            ensure_week()
            if cur_day is None:
                cur_day = {"label": "Day ?", "_dateprose": "", "sessions": []}
                cur_week["days"].append(cur_day)
            cur_day["sessions"].append({"kind": "todo", "source": s})
            todos += 1
            continue

        start, end = hhmm(mt.group(1), mt.group(2)), hhmm(mt.group(3), mt.group(4))
        rest = mt.group(5).strip()
        sess, title, links, location, people, extra, is_todo = parse_session(rest, s)
        sess["start"], sess["end"] = start, end
        if is_todo:
            todos += 1
            ordered = {k: sess[k] for k in ["start", "end", "kind", "source"] if k in sess}
        else:
            if title:
                sess["title"] = title
            if "track" not in sess:
                sess["track"] = "main"
            if people:
                sess["instructors"] = people
            if location:
                sess["location"] = location
            if links:
                sess["links"] = links
            if shadow:
                sess["shadow"] = True
            sess.update(extra)
            ordered = {k: sess[k] for k in ["start", "end", "kind", "meal", "track", "title",
                                            "instructors", "location", "links", "notes", "shadow", "guest"]
                       if k in sess}
        ensure_week()
        if cur_day is None:
            cur_day = {"label": "Day ?", "_dateprose": "", "sessions": []}
            cur_week["days"].append(cur_day)
        cur_day["sessions"].append(ordered)
        last_session = ordered

    for w in weeks:
        infer_dates(w["days"], year)
        for d in w["days"]:
            d.pop("_needs_date", None)
            # order day keys: date, label, sessions, links, notes
            for k in ("date", "label", "sessions", "links", "notes"):
                if k in d:
                    d[k] = d.pop(k)
    return weeks, todos


class _Dumper(yaml.SafeDumper):
    pass


def _str_representer(dumper, data):
    # force-quote scalars that YAML would otherwise coerce (dates, HH:MM times)
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", data) or re.fullmatch(r"\d{2}:\d{2}", data):
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="'")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


_Dumper.add_representer(str, _str_representer)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("source", help="schedule/<year>/index.md (the Liquid wall)")
    ap.add_argument("--year", type=int, required=True)
    ap.add_argument("--clinic", default="mmed")
    ap.add_argument("--status", default="published", choices=["draft", "published", "archive"])
    ap.add_argument("-o", "--out", required=True)
    args = ap.parse_args(argv)

    weeks, todos = parse(args.source, args.year)
    n_sess = sum(len(d.get("sessions", [])) for w in weeks for d in w["days"])
    doc = {
        "clinic": args.clinic,
        "year": args.year,
        "status": args.status,
        "title": f"MMED {args.year}",
        "timezone": "Africa/Johannesburg",
        "display_timezones": ["Africa/Johannesburg"],
        "tracks": ["main", "Section 1", "Section 2"],
        "locations": LOCATIONS_LABEL,
        "meal_defaults": {"breakfast": {"start": "07:45", "end": "08:15"},
                          "dinner": {"start": "18:00", "end": "18:30"}},
        "weeks": weeks,
    }
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    with open(args.out, "w") as fh:
        yaml.dump(doc, fh, Dumper=_Dumper, sort_keys=False, default_flow_style=False,
                  allow_unicode=True, width=100)
    print(f"wrote {args.out}: {len(weeks)} weeks, "
          f"{sum(len(w['days']) for w in weeks)} days, {n_sess} sessions, {todos} TODO rows")
    return 0


if __name__ == "__main__":
    sys.exit(main())
