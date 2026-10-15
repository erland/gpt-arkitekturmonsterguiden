#!/usr/bin/env python3
"""Validate the active runtime registry, built packages and canonical core behavior."""
from pathlib import Path
import json
import zipfile
import yaml

root = Path(__file__).resolve().parents[1]
cfg = yaml.safe_load((root / "gpt-project.yaml").read_text(encoding="utf-8"))
expected = {"chatgpt_chat", "claude_project", "openai_plugin", "opencode"}
registered = set(cfg["runtime_parity"]["registered_runtimes"])
candidates = {c["runtime_id"]: c for c in cfg["analysis"]["runtime"]["candidates"]}
errors = []
def check(test, message):
    if not test:
        errors.append(message)

check(registered == expected, "runtime registry differs from active four runtime families")
check(set(candidates) == expected, "runtime candidates differ from registry")
check(not cfg["runtime"]["custom_gpt"]["enabled"], "Custom GPT must be disabled")
for runtime_id in expected:
    check(candidates.get(runtime_id, {}).get("suitability") in ("ready", "reduced"), runtime_id + " missing suitability")
targets = cfg["build_system"]["targets"]
check(set(targets) == {"project", "chat", "claude_project", "claude_skills", "opencode", "plugin"}, "Unexpected build targets")
markers = cfg["instructions"]["core_contract"]["required_markers"]
for name, builddir, entry in [
    ("chat", "chat", "assistant/instructions.md"),
    ("claude_project", "claude", "project/instructions.md"),
    ("claude_skills", "claude-skills", None),
    ("opencode", "opencode", "AGENTS.md"),
    ("plugin", "plugin", None),
]:
    folder = root / "build" / builddir
    check(folder.is_dir(), name + " build folder missing")
    if entry and (folder / entry).is_file():
        content = (folder / entry).read_text(encoding="utf-8")
        for marker in markers:
            check(marker in content, name + " missing core marker: " + marker)
    elif entry:
        errors.append(name + " missing " + entry)
    check(any(folder.rglob("SKILL.md")) if name in ("claude_skills", "opencode", "plugin") else True, name + " missing skill")
print(json.dumps({"result": "PASS" if not errors else "FAIL", "errors": errors}, ensure_ascii=False, indent=2))
raise SystemExit(bool(errors))
