"""Tests for validkit.iban.is_valid_iban."""

import pytest

from validkit.iban import is_valid_iban


def test_valid_iban_with_spaces():
    assert is_valid_iban("DE89 3704 0044 0532 0130 00") is True


def test_valid_iban_without_spaces():
    assert is_valid_iban("DE89370400440532013000") is True


def test_valid_iban_lowercase():
    assert is_valid_iban("de89 3704 0044 0532 0130 00") is True


def test_valid_iban_mixed_case():
    assert is_valid_iban("dE89 3704 0044 0532 0130 00") is True


def test_invalid_check_digit():
    assert is_valid_iban("DE88 3704 0044 0532 0130 00") is False


def test_unknown_country_code():
    assert is_valid_iban("XX89 3704 0044 0532 0130 00") is False


def test_wrong_length():
    assert is_valid_iban("DE89 3704 0044 0532 0130") is False


def test_country_code_not_alpha():
    assert is_valid_iban("1289 3704 0044 0532 0130 00") is False


def test_non_alnum_payload():
    assert is_valid_iban("DE89 3704 0044 0532 0130 !0") is False


def test_too_short():
    assert is_valid_iban("DE89") is False


def test_empty_string():
    assert is_valid_iban("") is False


def test_non_string_raises_type_error():
    with pytest.raises(TypeError):
        is_valid_iban(123)  # type: ignore[arg-type]


def test_long_input_raises_value_error():
    with pytest.raises(ValueError):
        is_valid_iban("D" * 1001)
