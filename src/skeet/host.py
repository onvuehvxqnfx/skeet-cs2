"""Core plugin host — owns the registry, lifecycle, and dump context."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from skeet.contracts.plugin import PluginContract, PluginMeta
from skeet.registry.signatures import CS2_BUILDS


@dataclass
class DumpContext:
    build: str
    module_base: int
    offsets: dict[str, int] = field(default_factory=dict)
    artifacts: dict[str, Any] = field(default_factory=dict)


class PluginHost:
    def __init__(self) -> None:
        self.registry: dict[str, PluginMeta] = {}
        self._instances: dict[str, PluginContract] = {}

    def register(self, plugin: PluginContract) -> None:
        meta = plugin.meta()
        if meta.name in self.registry:
            raise ValueError(f"plugin {meta.name} already registered")
        self.registry[meta.name] = meta
        self._instances[meta.name] = plugin

    def run(self, build: str) -> dict[str, Any]:
        spec = CS2_BUILDS[build]
        ctx = DumpContext(build=build, module_base=spec.client_base, offsets=dict(spec.offsets))
        for name, plugin in self._instances.items():
            plugin.on_load(ctx)
        results: dict[str, Any] = {}
        for name, plugin in self._instances.items():
            results[name] = plugin.on_dump(ctx)
        for plugin in self._instances.values():
            plugin.on_unload(ctx)
        return results