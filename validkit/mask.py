"""Secret masking."""

from validkit._validation import _check_text


def mask_secret(text: str, keep: int = 4) -> str:
    _check_text(text, "text")
    if not text:
        raise ValueError("text must not be empty")
    if keep <= 0:
        raise ValueError("keep must be greater than 0")
    if keep >= len(text):
        return text
    return "*" * (len(text) - keep) + text[-keep:]
