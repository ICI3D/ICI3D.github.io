"""ICI3D clinic schedule tooling (#54 "flat data -> validate -> render" loop).

Ships the schedule JSON Schema and the allowed role-token vocabulary as package
data (ici3d_schedule/data/) and exposes the validator behind the `validate-schedule`
console script, which the distributed pre-commit hook (.pre-commit-hooks.yaml) runs.
"""
