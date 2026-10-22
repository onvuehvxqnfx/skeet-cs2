"""Shared plugin contract for skeet-cs2 extension modules."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Protocol

if TYPE_CHECKING:
    from skeet.host import DumpContext


@dataclass(frozen=True)
class PluginMeta:
    name: str
    version: str
    description: str
    requires: tuple[str, ...] = ()


class PluginContract(Protocol):
    def meta(self) -> PluginMeta: ...
    def on_load(self, ctx: "DumpContext") -> None: ...
    def on_dump(self, ctx: "DumpContext") -> Any: ...
    def on_unload(self, ctx: "DumpContext") -> None: ...


class BasePlugin:
    """Convenience base — subclasses override `on_dump` only."""

    _META: PluginMeta

    def meta(self) -> PluginMeta:
        return self._META

    def on_load(self, ctx: "DumpContext") -> None:
        return None

    def on_dump(self, ctx: "DumpContext") -> Any:
        raise NotImplementedError

    def on_unload(self, ctx: "DumpContext") -> None:
        return None