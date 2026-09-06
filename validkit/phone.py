"""Phone number normalization to E.164 format."""

from validkit._validation import _check_text

_ALLOWED_STRIPPED = "() -"


def normalize_phone(text: str, country_code: str) -> str:
    """Normalize a phone number into E.164 format (``+<country><digits>``).

    Accepts a ``country_code`` with or without a leading ``+``. The number
    ``text`` may contain parentheses, spaces and hyphens, which are removed,
    along with leading zeros of the national number.

    Raises:
        TypeError: if ``text`` or ``country_code`` is not a ``str``.
        ValueError: if either argument is too long or not normalizable.
    """
    _check_text(text, "text")
    _check_text(country_code, "country_code")

    code = country_code.lstrip("+")
    if not code.isdigit():
        raise ValueError("country_code must consist of digits, optionally with a leading '+'")

    cleaned = text
    for char in _ALLOWED_STRIPPED:
        cleaned = cleaned.replace(char, "")
    cleaned = cleaned.lstrip("0")

    if not cleaned.isdigit():
        raise ValueError("text does not contain a normalizable phone number")

    return f"+{code}{cleaned}"
