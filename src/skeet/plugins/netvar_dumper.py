"""Dumps the skeet module's netvar table into a flat offset map."""
from __future__ import annotations

from typing import Any

from skeet.contracts.plugin import BasePlugin, PluginMeta
from skeet.host import DumpContext


class NetvarDumper(BasePlugin):
    _META = PluginMeta(
        name="netvar_dumper",
        version="0.3.0",
        description="Enumerate skeet module netvar tables and emit name→offset map",
    )

    def on_load(self, ctx: DumpContext) -> None:
        ctx.artifacts.setdefault("netvars", {})

    def on_dump(self, ctx: DumpContext) -> Any:
        table = ctx.artifacts.setdefault("netvars", {})
        # stub: real implementation walks RecvTable linked list from client_base
        for name, off in ctx.offsets.items():
            table[name] = off
        return {"netvars": len(table)}


def build_plugin() -> NetvarDumper:
    return NetvarDumper()