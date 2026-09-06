"""Tests for validkit.email.is_valid_email."""

import pytest

from validkit.email import is_valid_email


@pytest.mark.parametrize(
    "value",
    [
        "user@example.com",
        "first.last@example.com",
        "user+tag@example.co.uk",
        "name@sub.domain.example.org",
        "a@b.co",
    ],
)
def test_valid_emails(value):
    assert is_valid_email(value) is True


@pytest.mark.parametrize(
    "value",
    [
        "not-an-email",
        "user@",
        "@example.com",
        "user@example",
        "user name@example.com",
        "user@exa mple.com",
        "user@@example.com",
        "user@.com",
        "user@example..com",
        "user@example.",
    ],
)
def test_invalid_emails(value):
    assert is_valid_email(value) is False


def test_empty_string_is_invalid():
    assert is_valid_email("") is False


def test_exactly_1000_characters_does_not_raise():
    assert is_valid_email("a" * 1000) is False


def test_over_1000_characters_raises_value_error():
    with pytest.raises(ValueError):
        is_valid_email("a" * 1001)


@pytest.mark.parametrize("value", [123, None, 1.5, ["user@example.com"], b"user@example.com"])
def test_non_string_raises_type_error(value):
    with pytest.raises(TypeError):
        is_valid_email(value)
