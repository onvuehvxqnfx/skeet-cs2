"""Serialise dump artifacts to JSON for offline analysis."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def write_artifacts(artifacts: dict[str, Any], out_dir: Path) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "skeet_dump.json"
    target.write_text(json.dumps(artifacts, indent=2, sort_keys=True), encoding="utf-8")
    return target


def load_artifacts(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))