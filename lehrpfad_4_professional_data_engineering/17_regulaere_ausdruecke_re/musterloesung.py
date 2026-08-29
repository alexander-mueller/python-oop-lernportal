"""
Kapitel 17: Reguläre Ausdrücke (re) – Musterlösung 💡
====================================================
Vollständige Referenzlösung für alle Teilaufgaben aus Kapitel 17.
"""

import re
from typing import List, Dict, Optional, Any


def ist_gueltige_email(email: str) -> bool:
    """
    Prüft, ob ein übergebener String eine gültige E-Mail-Adresse ist.
    """
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*\.[a-zA-Z]{2,}$"
    return bool(re.fullmatch(pattern, email.strip()) if email == email.strip() else False)


def finde_telefonnummern(text: str) -> List[str]:
    """
    Findet alle Telefonnummern in einem Text (Standard, Vorwahl, Ländervorwahl).
    """
    pattern = r"(?:\+\d{1,3}[ -]\d{2,5}|\(\d{2,5}\)|0\d{1,5})[- /]?\d{3,10}\b"
    return re.findall(pattern, text)


def extrahiere_hashtags(text: str) -> List[str]:
    """
    Extrahiert alle Social-Media-Hashtags aus einem Text.
    """
    pattern = r"#[a-zA-Z0-9_äöüÄÖÜß]+"
    return re.findall(pattern, text)


def maskiere_iban(text: str) -> str:
    """
    Maskiert alle IBANs im Text: Die ersten 4 Stellen bleiben sichtbar, der Rest wird mit '*' maskiert.
    """
    pattern = r"\b([A-Z]{2}\d{2})([A-Z0-9]{8,30})\b"
    
    def _mask_match(match: re.Match) -> str:
        prefix = match.group(1)
        rest = match.group(2)
        return prefix + ("*" * len(rest))

    return re.sub(pattern, _mask_match, text)


def parse_datum_iso(datum_str: str) -> Dict[str, str]:
    """
    Parst ein Datum im ISO-Format (YYYY-MM-DD) mithilfe benannter Gruppen (?P<name>...).
    """
    pattern = r"^(?P<jahr>\d{4})-(?P<monat>\d{2})-(?P<tag>\d{2})$"
    match = re.fullmatch(pattern, datum_str.strip())
    if not match:
        raise ValueError(f"Ungültiges ISO-Datumsformat: '{datum_str}' (erwartet: YYYY-MM-DD)")
    return match.groupdict()


def parse_log_zeile(log_zeile: str) -> Dict[str, str]:
    """
    Parst eine Server-Logzeile und extrahiert timestamp, level, service und message.
    """
    pattern = r"^\[(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] \[(?P<level>[A-Z]+)\] \[(?P<service>[\w-]+)\] (?P<message>.+)$"
    match = re.match(pattern, log_zeile.strip())
    if not match:
        raise ValueError(f"Ungültige Logzeile: '{log_zeile}'")
    return match.groupdict()


if __name__ == "__main__":
    print("Musterlösung Kapitel 17:")
    print("E-Mail validieren:", ist_gueltige_email("user.name@sub.example.com"))
    print("Telefonnummern:", finde_telefonnummern("Tel: 0171-1234567 und +49 171 1234567 sowie (089) 123456"))
    print("Hashtags:", extrahiere_hashtags("Lerne #python mit #code_2026! #spaß"))
    print("IBAN:", maskiere_iban("DE89370400440532013000"))
    print("Datum:", parse_datum_iso("2026-08-29"))
