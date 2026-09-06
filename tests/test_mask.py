"""Tests for validkit.mask.mask_secret."""

import pytest

from validkit.mask import mask_secret


def test_mask_secret_ac_example():
    assert mask_secret("geheim123", 4) == "*****m123"


def test_mask_secret_default_keep():
    assert mask_secret("abcdefghij") == "******ghij"


def test_mask_secret_keep_equals_length():
    assert mask_secret("secret", keep=6) == "secret"


def test_mask_secret_keep_greater_than_length():
    assert mask_secret("abc", keep=10) == "abc"


def test_mask_secret_long_input():
    text = "x" * 100
    assert mask_secret(text, 4) == "*" * 96 + "xxxx"


def test_mask_secret_output_same_length_as_input():
    text = "abcdefgh"
    result = mask_secret(text, 3)
    assert len(result) == len(text)
    assert result == "*****fgh"


def test_mask_secret_single_char_keep_one():
    assert mask_secret("a", keep=1) == "a"


def test_mask_secret_two_chars_keep_one():
    assert mask_secret("ab", keep=1) == "*b"


def test_mask_secret_keep_zero_raises_value_error():
    with pytest.raises(ValueError):
        mask_secret("abc", keep=0)


def test_mask_secret_keep_negative_raises_value_error():
    with pytest.raises(ValueError):
        mask_secret("abc", keep=-1)


def test_mask_secret_empty_input_raises_value_error():
    with pytest.raises(ValueError):
        mask_secret("")


def test_mask_secret_non_string_raises_type_error():
    with pytest.raises(TypeError):
        mask_secret(123)


def test_mask_secret_too_long_input_raises_value_error():
    with pytest.raises(ValueError):
        mask_secret("x" * 1001)
