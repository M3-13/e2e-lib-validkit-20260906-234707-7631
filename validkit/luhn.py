"""Luhn checksum validation."""

from validkit._validation import _check_text


def luhn_check(digits: str) -> bool:
    """Return True if ``digits`` ends with a valid Luhn check digit.

    Spaces and hyphens are ignored. After removing them, the remaining
    characters must be digits only.

    Raises:
        TypeError: if ``digits`` is not a ``str``.
        ValueError: if ``digits`` is longer than 1000 characters, contains no
            digits, or contains characters other than digits, spaces and
            hyphens.
    """
    _check_text(digits, "digits")

    cleaned = digits.replace(" ", "").replace("-", "")
    if not cleaned.isdigit():
        raise ValueError("digits must contain only digits, spaces and hyphens")
    if len(cleaned) < 2:
        raise ValueError("digits must contain at least two digits")

    total = 0
    for index, char in enumerate(reversed(cleaned)):
        value = int(char)
        if index % 2 == 1:
            value *= 2
            if value > 9:
                value -= 9
        total += value

    return total % 10 == 0
