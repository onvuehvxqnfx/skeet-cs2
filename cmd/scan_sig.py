"""Signature scanner CLI — scans a dumped .bin for a byte pattern."""
from __future__ import annotations

import sys
from pathlib import Path

from skeet.utils.patterns import compile_pattern, find_in
from skeet.utils.hexfmt import hx


def main(argv: list[str]) -> int:
    if len(argv) < 3:
        print("usage: scan_sig.py <dump.bin> <signature>")
        return 2
    buf = Path(argv[1]).read_bytes()
    needle, mask = compile_pattern(argv[2])
    off = find_in(buf, needle, mask)
    if off < 0:
        print("not found")
        return 1
    print(f"found at {hx(off)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))