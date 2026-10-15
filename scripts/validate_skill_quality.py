#!/usr/bin/env python3
"""Check five Skills have distinct methods and domain-appropriate references."""
from pathlib import Path
import yaml

root = Path(__file__).resolve().parents[1]
cfg = yaml.safe_load((root / "gpt-project.yaml").read_text(encoding="utf-8"))
skills = cfg["skills"]["definitions"]
ids = {"monsterval", "monsterjamforelse", "arkitekturgranskning", "adr", "monsterkombinationer"}
assert {s["id"] for s in skills} == ids
refsets = []
for skill in skills:
    ident = skill["id"]
    refs = skill["references"]
    assert f"knowledge/skill-methods/{ident}.md" in refs, ident
    assert len(refs) >= 2, ident
    assert all((root / item).is_file() for item in refs), ident
    assert (root / f"knowledge/skill-methods/{ident}.md").stat().st_size > 200
    refsets.append(tuple(refs))
assert len(set(refsets)) == 5, "All Skills should have distinct reference selections"
print("SKILL QUALITY: PASS (5 distinct methods and reference sets)")
