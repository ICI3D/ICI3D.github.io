# ici3d_schedule — schedule validation for ICI3D clinics (#54)

The **flat-data schedule loop**: a clinic edits one YAML file per cohort
(`_data/schedule/<clinic>/<year>.yml`), a validator gates it (schema + referential
checks), and a fixed Liquid include renders it. Editing data can never break the
build, because no Liquid lives in the edited file — a bad edit fails validation instead.

This package ships the **validator**, the **JSON Schema**, and the allowed **role
vocabulary**, so any clinic repo validates against the shared, versioned schema
without vendoring it.

## Two independent channels (Path A)

Rendering and validation are distributed separately, both from this repo:

| Concern | Mechanism | What the clinic adds |
|---|---|---|
| Render `schedule.html` | Jekyll `remote_theme` | `remote_theme: ICI3D/ICI3D.github.io` + `jekyll-remote-theme` plugin |
| Validate schedule data | this pre-commit hook | a `.pre-commit-config.yaml` entry (below) |

A Jekyll theme distributes `_includes`/`_layouts`/`_sass`/`assets` only — not `_data`
and not this Python validator. So schedule **data** and **people records**
(`_data/team`, which the renderer reads as `site.data.team`) are **clinic-owned**, and
the validator resolves instructors against the clinic's own `_data/team`.

## Local validation (contributors)

    pip install pre-commit
    pre-commit install

Every commit that touches `_data/schedule/**` now runs the same check CI runs.

## Consuming from a clinic repo

`.pre-commit-config.yaml`:

    repos:
      - repo: https://github.com/ICI3D/ICI3D.github.io
        rev: <tag or commit sha>
        hooks:
          - id: validate-schedule

pre-commit installs this package (schema + roles bundled) in an isolated environment
and runs it on the clinic's `_data/schedule/*.yml`. Instructor keys resolve against the
clinic's `_data/team`; point elsewhere with `args: [--people-dir, some/dir]`.

Run the identical check in CI with `pre-commit/action`, so local and CI validation are
one source of truth.
