# validkit

Eine kleine, eigenständige Python-Bibliothek mit neun unabhängigen, reinen Prüf-
und Normalisierungsfunktionen. Sie validiert und normalisiert E-Mail-Adressen,
Kartennummern (Luhn), IBANs, ISBN-13, Telefonnummern, entfernt Akzente, maskiert
Geheimnisse, erzeugt Slugs und begrenzt Zahlenwerte. Die Bibliothek kommt
vollständig ohne externe Abhängigkeiten aus (nur Python-Standardbibliothek),
bietet keine CLI, keine UI und keinen Netzwerkzugriff.

## Tech-Stack

- **Sprache**: Python
- **Runtime**: Python 3.9+
- **Abhängigkeiten (Laufzeit)**: nur Standardbibliothek
- **Tests**: pytest
- **Projektlayout**: Python-Paket `validkit/` mit `__init__.py` und Modulen, `tests/` mit Unit-Tests

## Installation

```bash
pip install -e .
```

## Tests ausführen

```bash
pytest
```

## Verwendung

Alle neun Funktionen werden über das Paket exportiert:

```python
from validkit import (
    is_valid_email,
    luhn_check,
    is_valid_iban,
    is_valid_isbn13,
    normalize_phone,
    strip_accents,
    mask_secret,
    slugify,
    clamp,
)
```

### Beispiele mit erwarteter Ausgabe

```python
>>> from validkit import is_valid_email
>>> is_valid_email("user@example.com")
True
>>> is_valid_email("not-an-email")
False
```

```python
>>> from validkit import luhn_check
>>> luhn_check("4111111111111111")
True
>>> luhn_check("4111111111111112")
False
```

```python
>>> from validkit import is_valid_iban
>>> is_valid_iban("DE89 3704 0044 0532 0130 00")
True
>>> is_valid_iban("DE89 3704 0044 0532 0130 01")
False
```

```python
>>> from validkit import is_valid_isbn13
>>> is_valid_isbn13("9780306406157")
True
>>> is_valid_isbn13("9780306406158")
False
```

```python
>>> from validkit import normalize_phone
>>> normalize_phone("(030) 123-4567", "49")
'+49301234567'
```

```python
>>> from validkit import strip_accents
>>> strip_accents("café")
'cafe'
```

```python
>>> from validkit import mask_secret
>>> mask_secret("geheim123", 4)
'******123'
```

```python
>>> from validkit import slugify
>>> slugify("Héllo Wörld!")
'hello-world'
```

```python
>>> from validkit import clamp
>>> clamp(5, 0, 10)
5
>>> clamp(-1, 0, 10)
0
>>> clamp(99, 0, 10)
10
```

## Feature-Liste

- `is_valid_email(text: str) -> bool` – prüft eine E-Mail-Adresse.
- `luhn_check(digits: str) -> bool` – prüft eine Ziffernfolge per Luhn-Algorithmus.
- `is_valid_iban(text: str) -> bool` – prüft eine IBAN (Groß-/Kleinschreibung und Leerzeichen egal).
- `is_valid_isbn13(text: str) -> bool` – prüft eine ISBN-13.
- `normalize_phone(text: str, country_code: str) -> str` – normalisiert eine Telefonnummer.
- `strip_accents(text: str) -> str` – entfernt diakritische Zeichen.
- `mask_secret(text: str, keep: int = 4) -> str` – maskiert ein Geheimnis bis auf die letzten `keep` Zeichen.
- `slugify(text: str) -> str` – erzeugt einen URL-freundlichen Slug.
- `clamp(value: float, low: float, high: float) -> float` – begrenzt einen Wert auf `[low, high]`.

## Fehlerkonvention

- `TypeError` bei falschem Eingabetyp.
- `ValueError` bei inhaltlich ungültigem Wert oder bei Zeichenketten länger als 1000 Zeichen.
