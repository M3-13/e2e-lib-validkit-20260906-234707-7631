"""Shared input validation helper for string-processing functions."""

MAX_TEXT_LENGTH = 1000


def _check_text(value: str, name: str) -> None:
    """Validate a string argument used by the public API functions.

    Raises:
        TypeError: if ``value`` is not a ``str``.
        ValueError: if ``value`` is longer than 1000 characters.
    """
    if not isinstance(value, str):
        raise TypeError(f"{name} must be a str, got {type(value).__name__}")
    if len(value) > MAX_TEXT_LENGTH:
        raise ValueError(f"{name} must be at most {MAX_TEXT_LENGTH} characters long")
