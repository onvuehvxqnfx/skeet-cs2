from __future__ import annotations


def hx(value: int, width: int = 8) -> str:
    return f"0x{value:0{width}X}"


def parse_hx(text: str) -> int:
    text = text.strip().lower()
    if text.startswith("0x"):
        text = text[2:]
    return int(text, 16)