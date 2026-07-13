#!/usr/bin/env python3
"""Validate ICI3D clinic schedule data files (#54 "flat data -> validate -> render" loop).

Two gating tiers run here; Tier 2 (link-liveness) is a separate advisory job and is NOT run here.

  Tier 0 - schema:    JSON Schema (schemas/schedule-cohort.schema.json). Required-fields-per-kind,
                      the closed `kind` enum, quoted "HH:MM" / "YYYY-MM-DD" strings (an unquoted
                      date becomes a YAML date object and fails the `type: string` assert here),
                      declared-track membership of the shape, etc.
  Tier 1 - semantic:  (a) every instructor/faculty key resolves to a person record or a role token;
                      (b) sessions do not overlap within a track (scoped: shadow + logistics/social
                          + same-`choice` alternatives + untimed rows are exempt);
                      (c) end >= start; (d) every session.track is a declared track;
                      (e) timezone + display_timezones are real IANA zones;
                      (f) no `kind: todo` survives in a non-archive cohort (the importer's loud TODO).

Usage:
    python3 tools/validate_schedule.py _data/schedule/mmed/2025.yml [more.yml ...] \
        [--schema schemas/schedule-cohort.schema.json] \
        [--people-dir _data/team] \
        [--roles _data/schedule/roles.yml] [--github]

Exit status is non-zero if any GATING finding (error) is present. Warnings never gate.
"""
from __future__ import annotations
import argparse
import json
import sys
from collections import defaultdict
from datetime import date as _date
from difflib import get_close_matches
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

try:
    from zoneinfo import available_timezones
    _IANA = available_timezones()
except Exception:  # pragma: no cover - zoneinfo always present on 3.9+
    _IANA = None

# Kinds exempt from the within-track non-overlap check. The real schedules deliberately
# nest a shadow faculty meeting inside lunch, run a coffee break inside a long lab, etc.
NONOVERLAP_EXEMPT_KINDS = {"meal", "coffee", "tea", "break", "note", "social", "raw", "todo"}
_ALL_LANE = "\x00ALL\x00"  # sentinel lane for untracked sessions


class Finding:
    __slots__ = ("level", "where", "msg", "line")

    def __init__(self, level: str, where: str, msg: str, line: int | None = None):
        self.level = level  # "error" (gates) or "warning" (advisory)
        self.where = where
        self.msg = msg
        self.line = line


def _hhmm_to_min(s):
    try:
        h, m = str(s).split(":")
        return int(h) * 60 + int(m)
    except Exception:
        return None


def _iter_sessions(doc):
    """Yield (session, locator) for every session in the document."""
    for wi, week in enumerate(doc.get("weeks") or []):
        wt = (week or {}).get("title") or f"Week #{wi}"
        for di, day in enumerate(week.get("days") or []):
            dd = (day or {}).get("date") or (day or {}).get("label") or f"Day #{di}"
            for si, sess in enumerate(day.get("sessions") or []):
                if not isinstance(sess, dict):
                    continue
                title = sess.get("title") or sess.get("meal") or sess.get("kind") or "?"
                start = sess.get("start") or "--:--"
                loc = f"{wt} / {dd} / {start} {sess.get('kind','?')} \"{title}\""
                yield sess, loc, day


def _collect_instructor_strings(sess):
    """All string (key/role) instructor entries on a session; externals/dicts skipped."""
    out = []
    for item in (sess.get("instructors") or []):
        if isinstance(item, str):
            out.append(item)
    for vals in (sess.get("instructors_by_track") or {}).values():
        for item in (vals or []):
            if isinstance(item, str):
                out.append(item)
    return out


def validate_doc(path: Path, schema, people_keys, role_tokens) -> list[Finding]:
    findings: list[Finding] = []
    raw = path.read_text()
    try:
        doc = yaml.safe_load(raw)
    except yaml.YAMLError as e:
        return [Finding("error", str(path), f"YAML did not parse: {e}")]
    if not isinstance(doc, dict):
        return [Finding("error", str(path), "top-level YAML is not a mapping")]

    status = doc.get("status", "published")

    # ---- Tier 0: schema ----
    for err in sorted(Draft202012Validator(schema).iter_errors(doc), key=lambda e: list(e.path)):
        loc = "/".join(str(p) for p in err.path) or "<root>"
        findings.append(Finding("error", f"T0 {loc}", err.message))

    # If the shape is badly broken, semantic checks would just add noise.
    if any(f.level == "error" for f in findings):
        # Still run the cheap top-level checks that don't depend on shape integrity.
        pass

    declared_tracks = set(doc.get("tracks") or [])

    # ---- Tier 1e: timezone validity ----
    if _IANA is not None:
        for tz in [doc.get("timezone")] + list(doc.get("display_timezones") or []):
            if tz and tz not in _IANA:
                findings.append(Finding("error", "T1e timezone", f"'{tz}' is not a known IANA timezone"))

    # ---- Tier 1a: top-level faculty roster resolution ----
    for key in (doc.get("faculty") or []):
        if isinstance(key, str):
            _resolve_person(key, "T1a faculty", people_keys, role_tokens, findings)

    # ---- per-session checks (+ gather per-day lanes for the non-overlap check) ----
    # Overlap only matters WITHIN a calendar day, so lanes are keyed per day, then per track.
    day_lanes: dict = defaultdict(lambda: defaultdict(list))  # id(day) -> lane -> [(smin,emin,loc,choice)]
    for sess, loc, day in _iter_sessions(doc):
        kind = sess.get("kind")
        smin, emin = _hhmm_to_min(sess.get("start")), _hhmm_to_min(sess.get("end"))

        # 1c: end >= start
        if smin is not None and emin is not None and emin < smin:
            findings.append(Finding("error", "T1c " + loc, f"end {sess.get('end')} is before start {sess.get('start')}"))

        # 1a: instructor resolution
        for key in _collect_instructor_strings(sess):
            _resolve_person(key, "T1a " + loc, people_keys, role_tokens, findings)

        # 1d: declared-track closure
        sess_tracks = []
        if sess.get("track"):
            sess_tracks.append(sess["track"])
        sess_tracks += list(sess.get("tracks") or [])
        for t in sess_tracks:
            if declared_tracks and t not in declared_tracks:
                findings.append(Finding("error", "T1d " + loc, f"track '{t}' is not in the declared tracks {sorted(declared_tracks)}"))

        # 1f: TODO closure
        if kind == "todo":
            lvl = "error" if status != "archive" else "warning"
            findings.append(Finding(lvl, "T1f " + loc, "unresolved importer TODO row: " + (sess.get("source") or "")[:160]))

        # 1b: gather lanes for non-overlap (skip exempt / shadow / untimed)
        if kind in NONOVERLAP_EXEMPT_KINDS or sess.get("shadow") or smin is None or emin is None:
            continue
        for lk in (sess_tracks or [_ALL_LANE]):
            day_lanes[id(day)][lk].append((smin, emin, loc, sess.get("choice")))

    # ---- Tier 1b: non-overlap within each (day, track) lane ----
    # An _ALL_LANE (untracked) session conflicts with everything that day; fold it into every real lane.
    for lanes in day_lanes.values():
        real_lanes = [lk for lk in lanes if lk != _ALL_LANE]
        for lk in (real_lanes or [_ALL_LANE]):
            items = list(lanes.get(lk, []))
            if lk != _ALL_LANE:
                items += lanes.get(_ALL_LANE, [])
            items.sort(key=lambda x: x[0])
            for i in range(len(items)):
                for j in range(i + 1, len(items)):
                    a, b = items[i], items[j]
                    if b[0] >= a[1]:  # sorted: no later item can overlap a
                        break
                    if a[3] is not None and a[3] == b[3]:  # same choice => alternatives, not overlap
                        continue
                    lane_name = "all tracks" if lk == _ALL_LANE else f"track '{lk}'"
                    findings.append(Finding("error", "T1b " + a[2], f"overlaps ({lane_name}) with -> {b[2]}"))

    # dedupe identical findings (an _ALL_LANE pair can surface once per real lane)
    seen, deduped = set(), []
    for f in findings:
        sig = (f.level, f.where, f.msg)
        if sig not in seen:
            seen.add(sig)
            deduped.append(f)
    return deduped


def _resolve_person(key, where, people_keys, role_tokens, findings):
    if key in people_keys:
        return
    low = key.lower()
    if low in role_tokens:
        if low == "tbd":
            findings.append(Finding("warning", where, "instructor 'tbd' is a placeholder still to be filled"))
        return
    sugg = get_close_matches(low, people_keys, n=1)
    hint = f" (did you mean '{sugg[0]}'?)" if sugg else ""
    findings.append(Finding("error", where, f"instructor '{key}' resolves to neither a person (_data/team/{key}.yml) nor a role{hint}"))


def main(argv=None):
    ap = argparse.ArgumentParser(description="Validate ICI3D clinic schedule data files (Tier 0 + Tier 1).")
    ap.add_argument("files", nargs="+", help="schedule YAML file(s)")
    here = Path(__file__).resolve().parent.parent
    ap.add_argument("--schema", default=str(here / "schemas/schedule-cohort.schema.json"))
    ap.add_argument("--people-dir", default=str(here / "_data/team"))
    ap.add_argument("--roles", default=str(here / "_data/schedule/roles.yml"))
    ap.add_argument("--github", action="store_true", help="also emit ::error/::warning GitHub annotations")
    args = ap.parse_args(argv)

    schema = json.loads(Path(args.schema).read_text())
    people_keys = {p.stem for p in Path(args.people_dir).glob("*.yml") if p.stem != "template"}
    roles_doc = yaml.safe_load(Path(args.roles).read_text()) or {}
    role_tokens = {r.lower() for r in (roles_doc.get("roles") or [])}

    n_err = n_warn = 0
    for f in args.files:
        p = Path(f)
        findings = validate_doc(p, schema, people_keys, role_tokens)
        errs = [x for x in findings if x.level == "error"]
        warns = [x for x in findings if x.level == "warning"]
        n_err += len(errs)
        n_warn += len(warns)
        status = "OK" if not errs else f"{len(errs)} ERROR(S)"
        print(f"\n=== {f}: {status}{' + ' + str(len(warns)) + ' warning(s)' if warns else ''} ===")
        for x in findings:
            print(f"  [{x.level.upper()}] {x.where}\n         {x.msg}")
            if args.github:
                tag = "error" if x.level == "error" else "warning"
                print(f"::{tag} file={f}::{x.where}: {x.msg}")
    print(f"\nTOTAL: {n_err} error(s), {n_warn} warning(s) across {len(args.files)} file(s)")
    return 1 if n_err else 0


if __name__ == "__main__":
    sys.exit(main())
