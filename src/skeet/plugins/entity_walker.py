"""Entity walker — enumerates CBaseEntity entries via dwEntityList."""
from __future__ import annotations

from typing import Any

from skeet.contracts.plugin import BasePlugin, PluginMeta
from skeet.host import DumpContext


class EntityWalker(BasePlugin):
    _META = PluginMeta(
        name="entity_walker",
        version="0.4.1",
        description="Walk CS2 entity list and emit player + world entity records",
        requires=("dwEntityList", "m_iHealth", "m_iTeamNum"),
    )

    MAX_ENTITIES = 64

    def on_dump(self, ctx: DumpContext) -> Any:
        list_addr = ctx.module_base + ctx.offsets["dwEntityList"]
        entities: list[dict[str, int]] = []
        for idx in range(self.MAX_ENTITIES):
            # stub: real read goes through mem.read_i64(list_addr + idx * 0x78)
            entities.append({"index": idx, "addr": list_addr + idx * 0x78})
        ctx.artifacts["entities"] = entities
        return {"count": len(entities)}


def build_plugin() -> EntityWalker:
    return EntityWalker()