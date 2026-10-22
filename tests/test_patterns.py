from skeet.utils.patterns import compile_pattern, find_in


def test_compile_and_find():
    needle, mask = compile_pattern("48 8B ?? 05")
    buf = b"\x00\x00\x48\x8B\x11\x05\x00"
    assert find_in(buf, needle, mask) == 2


def test_bad_token():
    import pytest
    with pytest.raises(ValueError):
        compile_pattern("48 ZZ 05")