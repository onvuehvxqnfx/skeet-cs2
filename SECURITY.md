# Security Policy

## Scope

`skeet-cs2` is a research tool that parses CS2 process memory and Gamesense.pub
(Skeet) module dumps for educational purposes. It is **not** designed to be used
against live anti-cheat protected sessions.

## Reporting

If you find a vulnerability in the loader, the plugin host, or the dump parser
(specifically anything that could cause arbitrary code execution from a
malformed `.dmp` file), please email `security@skeet-cs2.invalid` with:

- A minimal reproducer
- The affected module (`loader`, `host`, `parser`, `plugin`)
- Your Python version and OS build

Do **not** open a public issue for loader/parser RCEs.

## Out of scope

- Detection by VAC / VAC Live / Trusted Mode — expected, not a bug.
- Crashes caused by running the tool against a build that isn't in the
  `registry/signatures.py` table.