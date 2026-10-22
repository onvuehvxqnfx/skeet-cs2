"""CS2 build registry — offsets for the Gamesense.pub (Skeet) module layout.

Values here are synthetic placeholders used by the parser and tests. Update
this table when a new CS2 build lands and the skeet module's netvar layout
shifts. Do not commit live dump data.
"""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class BuildSpec:
    build: str
    client_base: int
    engine_base: int
    offsets: dict[str, int] = field(default_factory=dict)


CS2_BUILDS: dict[str, BuildSpec] = {
    "2401": BuildSpec(
        build="2401",
        client_base=0x7FF6_0000_0000,
        engine_base=0x7FF6_1000_0000,
        offsets={
            "dwLocalPlayer": 0x17E2F10,
            "dwEntityList": 0x1A2B3C0,
            "dwViewMatrix": 0x1A9F2A0,
            "dwGlobalVars": 0x17C1A80,
            "m_iHealth": 0x344,
            "m_iTeamNum": 0x3C8,
            "m_vecOrigin": 0x1388,
        },
    ),
    "2402": BuildSpec(
        build="2402",
        client_base=0x7FF6_0000_0000,
        engine_base=0x7FF6_1000_0000,
        offsets={
            "dwLocalPlayer": 0x17E4A90,
            "dwEntityList": 0x1A2D0A0,
            "dwViewMatrix": 0x1AA0C20,
            "dwGlobalVars": 0x17C3B00,
            "m_iHealth": 0x344,
            "m_iTeamNum": 0x3C8,
            "m_vecOrigin": 0x1388,
        },
    ),
}


def resolve(build: str, key: str) -> int:
    spec = CS2_BUILDS.get(build)
    if spec is None:
        raise KeyError(f"unknown CS2 build: {build}")
    if key not in spec.offsets:
        raise KeyError(f"offset {key} not present for build {build}")
    return spec.offsets[key]