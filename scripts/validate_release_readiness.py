#!/usr/bin/env python3
"""Inspect the current delivery manifest, ZIP integrity and checksums."""
import hashlib
import json
import zipfile
from pathlib import Path
import yaml

root = Path(__file__).resolve().parents[1]
cfg = yaml.safe_load((root / "gpt-project.yaml").read_text(encoding="utf-8"))
dist = root / "dist"
errors = []
def check(test, msg):
    if not test:
        errors.append(msg)
manifest_path = dist / "DELIVERY-MANIFEST.json"
sums_path = dist / "SHA256SUMS.txt"
check(manifest_path.is_file(), "Delivery manifest missing")
check(sums_path.is_file(), "SHA256SUMS missing")
if manifest_path.is_file():
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    types = {entry.get("type") for entry in manifest.get("artifacts", [])}
    expected = {"project_zip", "checksums"} | {v["artifact_type"] for v in cfg["build_system"]["runtime_targets"].values()}
    check(expected <= types, "Missing artifact types: " + repr(sorted(expected-types)))
if sums_path.is_file():
    checksums = {}
    for line in sums_path.read_text(encoding="utf-8").splitlines():
        parts = line.split(None, 1)
        if len(parts) == 2:
            checksums[parts[1].strip()] = parts[0]
    packages = list(dist.glob("*.zip"))
    check(len(packages) == 6, "Expected 6 packages, got " + str(len(packages)))
    for path in packages:
        check(checksums.get(path.name) == hashlib.sha256(path.read_bytes()).hexdigest(), "Bad checksum: " + path.name)
        try:
            with zipfile.ZipFile(path) as archive:
                check(archive.testzip() is None, "Bad ZIP CRC: " + path.name)
        except zipfile.BadZipFile:
            errors.append("Invalid ZIP: " + path.name)
print(json.dumps({"result":"PASS" if not errors else "FAIL","errors":errors}, ensure_ascii=False, indent=2))
raise SystemExit(bool(errors))
