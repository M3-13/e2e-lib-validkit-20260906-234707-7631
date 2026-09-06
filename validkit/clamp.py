"""Value clamping."""

from numbers import Real


def clamp(value: float, low: float, high: float) -> float:
    if isinstance(value, bool) or not isinstance(value, Real):
        raise TypeError(f"value must be a number, got {type(value).__name__}")
    if isinstance(low, bool) or not isinstance(low, Real):
        raise TypeError(f"low must be a number, got {type(low).__name__}")
    if isinstance(high, bool) or not isinstance(high, Real):
        raise TypeError(f"high must be a number, got {type(high).__name__}")
    if low > high:
        raise ValueError(f"low ({low}) must not be greater than high ({high})")
    return max(low, min(value, high))
