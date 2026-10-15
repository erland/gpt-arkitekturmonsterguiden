#!/usr/bin/env python3
"""Verify modular Skill projection reproduces the legacy canonical instruction exactly."""
import json
from pathlib import Path
import yaml
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from lib.canonical_skill_sources import projected_instruction
ROOT=Path(__file__).resolve().parents[1]
cfg=yaml.safe_load((ROOT/"gpt-project.yaml").read_text(encoding="utf-8"))
assert cfg["instructions"]["mode"]=="modular_skills"
assert len(cfg["skills"]["definitions"])==5
assembled=projected_instruction(ROOT,cfg,cfg["skills"]["definitions"])
assert assembled==(ROOT/cfg["instructions"]["canonical"]).read_text(encoding="utf-8"),"Canonical instruction drift"
print("MODULAR PARITY PASS: five Skills, byte-identical instructions")
