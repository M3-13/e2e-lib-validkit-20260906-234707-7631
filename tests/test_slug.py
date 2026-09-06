"""Tests for validkit.slug.slugify."""

import pytest

from validkit.slug import slugify


def test_slugify_ac_example():
    assert slugify("Héllo Wörld!") == "hello-world"


def test_slugify_lowercases_and_replaces_spaces():
    assert slugify("Hello World") == "hello-world"


def test_slugify_removes_accents():
    assert slugify("Über Café déjà-vu") == "uber-cafe-deja-vu"


def test_slugify_collapses_multiple_hyphens():
    assert slugify("a---b__c  d") == "a-b-c-d"


def test_slugify_strips_leading_and_trailing_hyphens():
    assert slugify("---hello-world---") == "hello-world"


def test_slugify_strips_punctuation():
    assert slugify("Hello, World! (again)") == "hello-world-again"


def test_slugify_empty_string_returns_empty():
    assert slugify("") == ""


def test_slugify_only_punctuation_returns_empty():
    assert slugify("!!!  ???") == ""


def test_slugify_digits_and_hyphens_preserved():
    assert slugify("Version 2.0") == "version-2-0"


def test_slugify_wrong_type_raises_type_error():
    with pytest.raises(TypeError):
        slugify(123)  # type: ignore[arg-type]


def test_slugify_long_input_raises_value_error():
    with pytest.raises(ValueError):
        slugify("a" * 1001)
