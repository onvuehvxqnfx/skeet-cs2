"""One-shot dump helper — useful for CI smoke tests."""
from __future__ import annotations

import sys
from pathlib import Path

from skeet.host import PluginHost
from skeet.loader import load_builtin_plugins
from skeet.services.serializer import write_artifacts


def main(argv: list[str]) -> int:
    build = argv[1] if len(argv) > 1 else "2401"
    out = Path(argv[2]) if len(argv) > 2 else Path("out")
    host = PluginHost()
    load_builtin_plugins(host)
    host.run(build=build)
    path = write_artifacts({"build": build, "host": list(host.registry)}, out)
    print(f"wrote {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))