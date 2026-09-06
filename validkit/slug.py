"""Slug generation."""

import re
import unicodedata

from validkit._validation import _check_text


def slugify(text: str) -> str:
    _check_text(text, "text")

    text = text.lower()
    text = unicodedata.normalize("NFKD", text)
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    text = re.sub(r"[^a-z0-9-]", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")
