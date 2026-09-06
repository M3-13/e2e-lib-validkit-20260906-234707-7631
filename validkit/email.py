"""Email validation."""

import re

from validkit._validation import _check_text

_EMAIL_RE = re.compile(
    r"[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+"
    r"@[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?"
    r"(?:\.[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?)+"
)


def is_valid_email(text: str) -> bool:
    """Return True if ``text`` is a syntactically plausible email address.

    Only a syntactic check is performed: a non-empty local part, an ``@``
    sign, and a domain that contains at least one dot. Whitespace and
    forbidden characters cause a non-match. No network or MX lookup happens.
    """
    _check_text(text, "text")
    return _EMAIL_RE.fullmatch(text) is not None
