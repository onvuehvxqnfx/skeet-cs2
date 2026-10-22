"""Byte-pattern helpers for signature scanning the skeet module."""
from __future__ import annotations

import re

_TOKEN = re.compile(r"^[0-9A-F?]{2}$", re.I)


def compile_pattern(sig: str) -> tuple[bytes, bytes]:
    """Return (needle, mask) for a 'AA BB ?? CC' style signature."""
    parts = sig.split()
    needle = bytearray()
    mask = bytearray()
    for part in parts:
        if not _TOKEN.match(part):
            raise ValueError(f"bad signature token: {part!r}")
        if part == "??":
            needle.append(0)
            mask.append(0)
        else:
            needle.append(int(part, 16))
            mask.append(0xFF)
    return bytes(needle), bytes(mask)


def find_in(buf: bytes, needle: bytes, mask: bytes) -> int:
    n = len(needle)
    for i in range(len(buf) - n + 1):
        if all((buf[i + j] & mask[j]) == needle[j] for j in range(n)):
            return i
    return -1