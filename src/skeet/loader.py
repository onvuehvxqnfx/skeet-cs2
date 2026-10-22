"""Discovers and loads built-in plugins into the host."""
from __future__ import annotations

import importlib
import pkgutil

from skeet.host import PluginHost

BUILTIN_PACKAGE = "skeet.plugins"


def load_builtin_plugins(host: PluginHost) -> None:
    pkg = importlib.import_module(BUILTIN_PACKAGE)
    for info in pkgutil.iter_modules(pkg.__path__):
        if info.name.startswith("_"):
            continue
        mod = importlib.import_module(f"{BUILTIN_PACKAGE}.{info.name}")
        factory = getattr(mod, "build_plugin", None)
        if factory is None:
            continue
        host.register(factory())