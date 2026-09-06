"""Tests for validkit.accents.strip_accents."""

import pytest

from validkit.accents import strip_accents


def test_strip_accents_cafe():
    assert strip_accents("café") == "cafe"


def test_strip_accents_no_accents_unchanged():
    assert strip_accents("plain text 123") == "plain text 123"


def test_strip_accents_mixed_accents():
    assert strip_accents("Crème Brûlée") == "Creme Brulee"


def test_strip_accents_umlauts_diaeresis_removed():
    assert strip_accents("ä ö ü Ä Ö Ü") == "a o u A O U"


def test_strip_accents_combining_only():
    assert strip_accents("\u0301") == ""


def test_strip_accents_empty_string():
    assert strip_accents("") == ""


def test_strip_accents_long_input_ok():
    assert strip_accents("a" * 999) == "a" * 999


def test_strip_accents_too_long_raises_valueerror():
    with pytest.raises(ValueError):
        strip_accents("a" * 1001)


@pytest.mark.parametrize("bad", [123, None, 3.14, ["café"], b"cafe"])
def test_strip_accents_non_str_raises_typeerror(bad):
    with pytest.raises(TypeError):
        strip_accents(bad)
