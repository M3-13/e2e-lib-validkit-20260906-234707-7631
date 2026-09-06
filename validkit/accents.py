"""Accent stripping."""

import unicodedata

from validkit._validation import _check_text


def strip_accents(text: str) -> str:
    """Remove accents from ``text`` via Unicode normalization (NFD).

    Combining marks are stripped, so ``'café'`` becomes ``'cafe'``. All other
    characters are left unchanged.
    """
    _check_text(text, "text")
    decomposed = unicodedata.normalize("NFD", text)
    return "".join(ch for ch in decomposed if not unicodedata.combining(ch))
