"""Thin wrapper around pymem for CS2 process access."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class MemoryReader:
    pid: int
    _handle: object | None = None

    def attach(self) -> None:
        try:
            import pymem  # type: ignore
        except ImportError as exc:  # pragma: no cover
            raise RuntimeError("pymem not installed") from exc
        self._handle = pymem.Pymem("cs2.exe")

    def read_i32(self, addr: int) -> int:
        if self._handle is None:
            raise RuntimeError("not attached")
        return int(self._handle.read_int(addr))

    def read_i64(self, addr: int) -> int:
        if self._handle is None:
            raise RuntimeError("not attached")
        return int(self._handle.read_longlong(addr))

    def read_bytes(self, addr: int, size: int) -> bytes:
        if self._handle is None:
            raise RuntimeError("not attached")
        return bytes(self._handle.read_bytes(addr, size))