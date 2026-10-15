#!/usr/bin/env python3
"""Ensure CI and release share the same migration quality gates."""
from pathlib import Path
import yaml

root = Path(__file__).resolve().parents[1]
cfg = yaml.safe_load((root / "gpt-project.yaml").read_text(encoding="utf-8"))
ci = (root / ".github/workflows/ci.yml").read_text(encoding="utf-8")
release = (root / ".github/workflows/release.yml").read_text(encoding="utf-8")
errors = []
common = [
    "lint_gpt_project.py", "run_tests.py", "validate_instruction_adherence.py",
    "build_distributions.py", "validate_distributions.py", "validate_runtime_parity.py",
    "validate_release_readiness.py", "project_hygiene.py --project-root . --mode final",
    "validate_workflow_parity.py"
]
for marker in common:
    for name, body in (("CI", ci), ("release", release)):
        if marker not in body:
            errors.append(name + " missing " + marker)
target = "--targets " + ",".join(cfg["build_system"]["targets"])
for name, body in (("CI", ci), ("release", release)):
    if target not in body:
        errors.append(name + " wrong build target set")
if "github.event.release.tag_name" not in release:
    errors.append("Release version must use GitHub tag")
print("WORKFLOW PARITY: " + ("FAIL" if errors else "PASS"))
for error in errors:
    print("- " + error)
raise SystemExit(bool(errors))
