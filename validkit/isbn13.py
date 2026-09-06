"""ISBN-13 validation."""

from validkit._validation import _check_text


def is_valid_isbn13(text: str) -> bool:
    """Return True if ``text`` is a valid ISBN-13.

    Hyphens and spaces are ignored before the check. The remaining text must
    consist of exactly 13 digits, and the weighted check digit (alternating
    factors 1 and 3) must verify.
    """
    _check_text(text, "text")

    digits = text.replace("-", "").replace(" ", "")
    if len(digits) != 13 or not digits.isdigit():
        return False

    total = sum(int(d) * (1 if i % 2 == 0 else 3) for i, d in enumerate(digits))
    return total % 10 == 0
