"""Public API contract tests: importability, callability and signatures.

The nine functions are currently stubs (they raise NotImplementedError), so
these tests assert that the public surface is WIRED — that each name can be
imported, is callable, and exposes exactly the signature the sprint contract
specifies. They deliberately do NOT invoke the stubs.
"""

import inspect

import pytest

import validkit
from validkit._validation import MAX_TEXT_LENGTH, _check_text

EXPECTED_SIGNATURES = {
    "is_valid_email": "(text: str) -> bool",
    "luhn_check": "(digits: str) -> bool",
    "is_valid_iban": "(text: str) -> bool",
    "is_valid_isbn13": "(text: str) -> bool",
    "normalize_phone": "(text: str, country_code: str) -> str",
    "strip_accents": "(text: str) -> str",
    "mask_secret": "(text: str, keep: int = 4) -> str",
    "slugify": "(text: str) -> str",
    "clamp": "(value: float, low: float, high: float) -> float",
}

PUBLIC_NAMES = [
    "is_valid_email",
    "luhn_check",
    "is_valid_iban",
    "is_valid_isbn13",
    "normalize_phone",
    "strip_accents",
    "mask_secret",
    "slugify",
    "clamp",
]


def test_public_api_exports_exactly_nine_names():
    assert set(validkit.__all__) == set(PUBLIC_NAMES)


@pytest.mark.parametrize("name", PUBLIC_NAMES)
def test_function_is_importable(name):
    assert hasattr(validkit, name)


@pytest.mark.parametrize("name", PUBLIC_NAMES)
def test_function_is_callable(name):
    assert callable(getattr(validkit, name))


@pytest.mark.parametrize("name", PUBLIC_NAMES)
def test_function_has_contract_signature(name):
    func = getattr(validkit, name)
    assert str(inspect.signature(func)) == EXPECTED_SIGNATURES[name]


def test_check_text_accepts_exactly_max_length():
    _check_text("x" * MAX_TEXT_LENGTH, "value")


def test_check_text_rejects_longer_than_max_length():
    with pytest.raises(ValueError):
        _check_text("x" * (MAX_TEXT_LENGTH + 1), "value")


def test_check_text_rejects_non_string():
    with pytest.raises(TypeError):
        _check_text(123, "value")
