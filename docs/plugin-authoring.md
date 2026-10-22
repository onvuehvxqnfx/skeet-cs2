# Writing a skeet-cs2 plugin

A plugin is any module under `src/skeet/plugins/` that exposes a
`build_plugin()` factory returning a `PluginContract` implementation.

## Minimal example

```python
from skeet.contracts.plugin import BasePlugin, PluginMeta
from skeet.host import DumpContext

class MyPlugin(BasePlugin):
    _META = PluginMeta(name="my_plugin", version="0.1.0", description="demo")

    def on_dump(self, ctx: DumpContext):
        return {"ok": True}

def build_plugin():
    return MyPlugin()
```

## Rules

- Offsets come from `ctx.offsets` — never hardcode.
- Write results into `ctx.artifacts` if downstream plugins need them.
- `on_load` runs before any `on_dump`; `on_unload` runs after all dumps.
- Keep `on_dump` side-effect free with respect to the CS2 process.