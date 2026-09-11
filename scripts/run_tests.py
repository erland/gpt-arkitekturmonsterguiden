#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import inspect
import sys
import traceback
from pathlib import Path

sys.dont_write_bytecode = True


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    failures = []
    count = 0
    for path in sorted((root / "tests").glob("test_*.py")):
        spec = importlib.util.spec_from_file_location(path.stem, path)
        module = importlib.util.module_from_spec(spec)
        assert spec.loader is not None
        spec.loader.exec_module(module)
        for name, func in sorted(inspect.getmembers(module, inspect.isfunction)):
            if not name.startswith("test_"):
                continue
            count += 1
            try:
                func()
                print(f"PASS {path.name}::{name}")
            except Exception:
                failures.append(f"{path.name}::{name}")
                traceback.print_exc()
    print(f"Tests: {count - len(failures)} passed, {len(failures)} failed")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
