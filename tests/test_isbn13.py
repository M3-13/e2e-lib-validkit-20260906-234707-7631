"""Tests for validkit.isbn13.is_valid_isbn13."""

import pytest

from validkit.isbn13 import is_valid_isbn13


def test_valid_isbn13():
    assert is_valid_isbn13("9780306406157") is True


def test_valid_isbn13_with_hyphens_and_spaces():
    assert is_valid_isbn13("978-0-306-40615-7") is True
    assert is_valid_isbn13("978 0 306 40615 7") is True


def test_invalid_check_digit():
    assert is_valid_isbn13("9780306406158") is False


def test_too_short():
    assert is_valid_isbn13("978030640615") is False


def test_too_long():
    assert is_valid_isbn13("97803064061577") is False


def test_empty_string():
    assert is_valid_isbn13("") is False


def test_non_digit_characters():
    assert is_valid_isbn13("97803064061x7") is False


def test_only_hyphens_and_spaces():
    assert is_valid_isbn13("---   ") is False


def test_non_string_raises_typeerror():
    with pytest.raises(TypeError):
        is_valid_isbn13(9780306406157)


def test_none_raises_typeerror():
    with pytest.raises(TypeError):
        is_valid_isbn13(None)


def test_too_long_raises_valueerror():
    with pytest.raises(ValueError):
        is_valid_isbn13("x" * 1001)
