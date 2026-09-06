"""Tests for validkit.phone.normalize_phone."""

import pytest

from validkit.phone import normalize_phone


def test_ac_example():
    assert normalize_phone("(030) 123-4567", "49") == "+49301234567"


def test_country_code_with_leading_plus():
    assert normalize_phone("0301234567", "+49") == "+49301234567"


def test_removes_spaces_and_hyphens():
    assert normalize_phone("030 123 - 45 67", "49") == "+49301234567"


def test_removes_leading_zeros():
    assert normalize_phone("00301234567", "49") == "+49301234567"


def test_plain_digits_unchanged():
    assert normalize_phone("301234567", "49") == "+49301234567"


def test_multi_digit_country_code():
    assert normalize_phone("123 456 7890", "1") == "+11234567890"


@pytest.mark.parametrize("text", ["", "   ", "()", "---", "0000"])
def test_empty_or_only_formatting_raises(text):
    with pytest.raises(ValueError):
        normalize_phone(text, "49")


def test_non_digit_text_raises():
    with pytest.raises(ValueError):
        normalize_phone("030abc4567", "49")


def test_non_digit_country_code_raises():
    with pytest.raises(ValueError):
        normalize_phone("0301234567", "4a")


def test_empty_country_code_raises():
    with pytest.raises(ValueError):
        normalize_phone("0301234567", "")


@pytest.mark.parametrize(
    ("text", "country_code"),
    [
        (1234567, "49"),
        ("0301234567", 49),
        (None, "49"),
        ("0301234567", None),
    ],
)
def test_wrong_types_raise_type_error(text, country_code):
    with pytest.raises(TypeError):
        normalize_phone(text, country_code)


def test_too_long_text_raises_value_error():
    with pytest.raises(ValueError):
        normalize_phone("1" * 1001, "49")


def test_too_long_country_code_raises_value_error():
    with pytest.raises(ValueError):
        normalize_phone("1234567", "1" * 1001)
