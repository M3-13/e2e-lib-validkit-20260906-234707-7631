"""Tests for validkit.luhn.luhn_check."""

import pytest

from validkit.luhn import luhn_check


@pytest.mark.parametrize(
    "digits",
    [
        "4111111111111111",
        "49927398716",
        "1234567812345670",
        "79927398713",
    ],
)
def test_valid_numbers(digits: str) -> None:
    assert luhn_check(digits) is True


@pytest.mark.parametrize(
    "digits",
    [
        "4111111111111112",
        "49927398717",
        "1234567812345678",
    ],
)
def test_invalid_numbers(digits: str) -> None:
    assert luhn_check(digits) is False


@pytest.mark.parametrize(
    "digits",
    [
        "4111 1111 1111 1111",
        "4111-1111-1111-1111",
        "4111 1111-1111 1111",
    ],
)
def test_separators_are_ignored(digits: str) -> None:
    assert luhn_check(digits) is True


def test_empty_input() -> None:
    with pytest.raises(ValueError):
        luhn_check("")


def test_only_separators() -> None:
    with pytest.raises(ValueError):
        luhn_check("  -  ")


def test_single_digit() -> None:
    with pytest.raises(ValueError):
        luhn_check("7")


def test_invalid_characters() -> None:
    with pytest.raises(ValueError):
        luhn_check("4111-xxxx")


def test_wrong_type() -> None:
    with pytest.raises(TypeError):
        luhn_check(4111111111111111)  # type: ignore[arg-type]


def test_too_long() -> None:
    with pytest.raises(ValueError):
        luhn_check("1" * 1001)
