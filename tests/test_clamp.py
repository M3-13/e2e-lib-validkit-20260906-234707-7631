"""Tests for validkit.clamp.clamp."""

import pytest

from validkit.clamp import clamp


def test_value_inside_interval_is_unchanged():
    assert clamp(5, 0, 10) == 5


def test_value_below_interval_is_clamped_to_low():
    assert clamp(-1, 0, 10) == 0


def test_value_above_interval_is_clamped_to_high():
    assert clamp(99, 0, 10) == 10


def test_value_exactly_at_low_boundary():
    assert clamp(0, 0, 10) == 0


def test_value_exactly_at_high_boundary():
    assert clamp(10, 0, 10) == 10


def test_float_values():
    assert clamp(3.14, 0.0, 10.0) == 3.14
    assert clamp(-0.5, 0.0, 10.0) == 0.0


def test_degenerate_interval_with_equal_bounds():
    assert clamp(7, 5, 5) == 5


def test_low_greater_than_high_raises_value_error():
    with pytest.raises(ValueError):
        clamp(1, 10, 0)


@pytest.mark.parametrize("bad", ["5", None, [1], (1,), {"a": 1}, b"5"])
def test_non_numeric_value_raises_type_error(bad):
    with pytest.raises(TypeError):
        clamp(bad, 0, 10)


@pytest.mark.parametrize("bad", ["0", None, [0]])
def test_non_numeric_low_raises_type_error(bad):
    with pytest.raises(TypeError):
        clamp(5, bad, 10)


@pytest.mark.parametrize("bad", ["10", None, [10]])
def test_non_numeric_high_raises_type_error(bad):
    with pytest.raises(TypeError):
        clamp(5, 0, bad)


@pytest.mark.parametrize("bad", [True, False])
def test_boolean_is_not_numeric(bad):
    with pytest.raises(TypeError):
        clamp(bad, 0, 10)
