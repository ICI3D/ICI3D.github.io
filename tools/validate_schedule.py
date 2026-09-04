#!/usr/bin/env python3
"""Backward-compatible shim: the validator now lives in the ici3d_schedule package.

Kept so `python3 tools/validate_schedule.py ...` keeps working for this repo's own
pre-commit hook, CI, and the (transitional) composite action, while clinic repos run
the same logic via the pip-installed `validate-schedule` console script. Schema and
role tokens are bundled in the package, so both invocation paths share one source.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from ici3d_schedule.validate import main  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(main())
