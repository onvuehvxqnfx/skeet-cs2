# Contributing to skeet-cs2

Thanks for helping out with the Gamesense.pub (Skeet) CS2 Dump project.

## Ground rules

- This repo is for **educational reverse-engineering research** on the CS2 binary
  and the Gamesense.pub (Skeet) cheat's CS2 module. Do not submit anything that
  targets live VAC-secured matchmaking sessions.
- Keep PRs focused. One feature or dump-offset update per PR.
- New plugin modules go under `src/skeet/plugins/` and must implement the
  `PluginContract` in `src/skeet/contracts/plugin.py`.
- Offsets and signatures live in `src/skeet/registry/` — never hardcode them
  in plugin code.

## Dev setup

```bash
python -m venv .venv
. .venv/Scripts/activate
pip install -r requirements.txt
python -m skeet dump --dry-run
```

## Tests

```bash
pytest -q tests/
```

Offsets in fixtures are synthetic; do not paste live dump data into tests.