from skeet.registry.signatures import CS2_BUILDS, resolve


def test_builds_present():
    assert "2401" in CS2_BUILDS
    assert "2402" in CS2_BUILDS


def test_resolve_known_offset():
    assert resolve("2401", "dwLocalPlayer") == 0x17E2F10


def test_unknown_build_raises():
    import pytest
    with pytest.raises(KeyError):
        resolve("9999", "dwLocalPlayer")