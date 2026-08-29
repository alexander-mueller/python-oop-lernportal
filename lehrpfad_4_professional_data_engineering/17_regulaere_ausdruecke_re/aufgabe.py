r"""
Kapitel 17: Reguläre Ausdrücke (re) – Text-Mining & Validierung 🔍🕵️
===================================================================
Aufgabe: Werde zum Muster-Detektiv! Nutze Pythons eingebautes `re`-Modul,
um strukturierte Daten aus unstrukturiertem Text zu filtern, Formate zu
validieren und vertrauliche Informationen zu maskieren.

Themen:
1. Metazeichen: \d (Ziffer), \w (Wortzeichen), \s (Whitespace), . (Beliebig), ^, $
2. Quantifizierer: +, *, ?, {min,max}
3. Gruppen & Benannte Gruppen: (group) und (?P<name>...)
4. Methoden: re.search(), re.match(), re.findall(), re.sub(), re.fullmatch()
"""

import re
from typing import List, Dict, Optional, Any


# ==============================================================================
# TEIL 1: VALIDIERUNG VON E-MAIL-ADRESSEN
# ==============================================================================

def ist_gueltige_email(email: str) -> bool:
    r"""
    TODO 1: Prüft, ob ein übergebener String eine gültige E-Mail-Adresse ist.

    Regeln für eine gültige E-Mail:
    - Benutzername: Mindestens 1 Zeichen aus Buchstaben (a-z, A-Z), Ziffern (0-9),
      Punkten (.), Unterstrichen (_), Plus (+) oder Bindestrichen (-).
    - Ein einzelnes '@'-Trennzeichen.
    - Domain-Name: Mindestens 1 Zeichen aus Buchstaben, Ziffern oder Bindestrichen.
    - Domain-Endung (TLD): Ein Punkt gefolgt von mindestens 2 Buchstaben (z.B. .de, .com, .at).
    - Es dürfen keine führenden/nachfolgenden Leerzeichen oder Leerzeichen innerhalb sein.

    Beispiele:
        ist_gueltige_email("max.mustermann@schule.at") -> True
        ist_gueltige_email("dev_123+tag@gmail.com")     -> True
        ist_gueltige_email("kein_at_zeichen.de")         -> False
        ist_gueltige_email("@domain.com")               -> False
        ist_gueltige_email("user@domain")               -> False
        ist_gueltige_email("user@domain.c")             -> False

    Tipp:
        Verwende ein Regex-Muster wie: r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*\.[a-zA-Z]{2,}$"
        und teste mit re.fullmatch(pattern, email) is not None.
    """
    # 🎯 TEILZIEL 1: Implementiere die E-Mail-Validierung
    pass


# ==============================================================================
# TEIL 2: EXTRAKTION VON TELEFONNUMMERN
# ==============================================================================

def finde_telefonnummern(text: str) -> List[str]:
    r"""
    TODO 2: Findet alle Telefonnummern in einem Text und gibt sie als Liste zurück.

    Unterstützte Formate:
    - Deutsche/Österreichische Standardnummern: "0171-1234567", "0171 1234567"
    - Mit Ländervorwahl: "+49 171 1234567", "+49-171-1234567", "+43 664 1234567"
    - Mit Vorwahlklammern: "(089) 123456", "(030) 98765432"
    - Mit Schrägstrich: "089/123456", "030/98765432"

    Beispiele:
        text = "Ruf mich an unter 0171-1234567 oder im Büro unter +49 171 1234567. Notfall: (089) 123456."
        finde_telefonnummern(text)
        -> ["0171-1234567", "+49 171 1234567", "(089) 123456"]

    Tipp:
        Nutze re.findall(). Ein typisches Suchmuster berücksichtigt:
        - Ländervorwahl oder Vorwahl mit Klammern/Null: (?:\+\d{1,3}[ -]\d{2,5}|\(\d{2,5}\)|0\d{1,5})
        - Optionales Trennzeichen [- /]?
        - Anschlussnummer: \d{3,10}\b
    """
    # 🎯 TEILZIEL 2: Extrahiere alle Telefonnummern
    pass


# ==============================================================================
# TEIL 3: SOCIAL MEDIA HASHTAGS EXTRAHIEREN
# ==============================================================================

def extrahiere_hashtags(text: str) -> List[str]:
    r"""
    TODO 3: Extrahiere alle Social-Media-Hashtags aus einem Text.

    Regeln:
    - Ein Hashtag beginnt mit dem Raute-Zeichen '#'.
    - Darauf folgen 1 oder mehr Wortzeichen (Buchstaben, Ziffern, Unterstriche).
    - Deutsche Umlaute (ä, ö, ü, ß) sollen ebenfalls unterstützt werden.
    - Ein einzelnes '#' ohne nachfolgende Wortzeichen ist KEIN Hashtag.

    Beispiele:
        extrahiere_hashtags("Lerne #python und #data_engineering! #2026 #süß")
        -> ["#python", "#data_engineering", "#2026", "#süß"]
        extrahiere_hashtags("Nur ein normales Zeichen # und Text")
        -> []

    Tipp:
        Nutze re.findall() mit dem Muster r"#[a-zA-Z0-9_äöüÄÖÜß]+" oder r"#\w+".
    """
    # 🎯 TEILZIEL 3: Extrahiere Hashtags
    pass


# ==============================================================================
# TEIL 4: DATENSCHUTZ & MASKIERUNG (IBAN)
# ==============================================================================

def maskiere_iban(text: str) -> str:
    r"""
    TODO 4: Maskiert alle IBANs in einem Text aus Datenschutzgründen.

    Regeln:
    - Eine IBAN besteht aus einem 2-stelligen Ländercode (z.B. DE, AT, CH),
      gefolgt von 2 Prüfziffern und weiteren 8 bis 30 alphanumerischen Zeichen.
    - Die ersten 4 Zeichen (z.B. 'DE89') bleiben sichtbar.
    - Alle darauffolgenden Zeichen der IBAN werden durch '*' ersetzt (exakt selbe Anzahl an Sternchen!).
    - Der restliche Text um die IBAN herum bleibt unverändert.

    Beispiele:
        maskiere_iban("Bitte überweisen auf DE89370400440532013000 danke!")
        -> "Bitte überweisen auf DE89****************** danke!"

        maskiere_iban("AT611904300234573201 und DE1234567890")
        -> "AT61**************** und DE12********"

    Tipp:
        Nutze re.sub() mit einer Ersetzungsfunktion:
        pattern = r"\b([A-Z]{2}\d{2})([A-Z0-9]{8,30})\b"
        re.sub(pattern, lambda m: m.group(1) + ("*" * len(m.group(2))), text)
    """
    # 🎯 TEILZIEL 4: Maskiere gefundene IBANs mit re.sub()
    pass


# ==============================================================================
# TEIL 5: BENANNTE GRUPPEN (ISO-DATUM PARSEN)
# ==============================================================================

def parse_datum_iso(datum_str: str) -> Dict[str, str]:
    r"""
    TODO 5: Parst ein Datum im ISO-Format (YYYY-MM-DD) mithilfe benannter Gruppen
    (?P<name>...) und gibt ein Dictionary zurück.

    Format:
    - jahr: 4 Ziffern (z.B. '2026')
    - monat: 2 Ziffern (z.B. '08')
    - tag: 2 Ziffern (z.B. '29')

    Rückgabe:
        Dict[str, str]: {'jahr': '2026', 'monat': '08', 'tag': '29'}

    Exceptions:
        ValueError: Falls das Format nicht exakt dem ISO-Muster entspricht.

    Beispiele:
        parse_datum_iso("2026-08-29") -> {'jahr': '2026', 'monat': '08', 'tag': '29'}
        parse_datum_iso("29.08.2026") -> löst ValueError aus!
        parse_datum_iso("2026/08/29") -> löst ValueError aus!

    Tipp:
        Verwende das Muster r"^(?P<jahr>\d{4})-(?P<monat>\d{2})-(?P<tag>\d{2})$".
        Rufe match = re.fullmatch(pattern, datum_str.strip()) auf.
        Mit match.groupdict() erhältst du direkt das fertige Dictionary!
    """
    # 🎯 TEILZIEL 5: Parse ISO-Datum mit benannten Gruppen
    pass


# ==============================================================================
# TEIL 6: BONUS: LOGFILE-PARSER
# ==============================================================================

def parse_log_zeile(log_zeile: str) -> Dict[str, str]:
    r"""
    TODO 6 (Bonus): Parst eine Server-Logzeile und extrahiert Metadaten.

    Format einer Logzeile:
    "[YYYY-MM-DD HH:MM:SS] [LEVEL] [SERVICE] NACHRICHT"
    Beispiel:
    "[2026-08-29 14:32:00] [ERROR] [auth_service] Login fehlgeschlagen für user 'admin'"

    Rückgabe:
        Dict mit den Schlüsseln:
        - "timestamp": z.B. "2026-08-29 14:32:00"
        - "level": z.B. "ERROR"
        - "service": z.B. "auth_service"
        - "message": z.B. "Login fehlgeschlagen für user 'admin'"

    Exceptions:
        ValueError: Wenn die Logzeile nicht dem erwarteten Format entspricht.
    """
    # 🎯 TEILZIEL 6: Parse Server-Logzeile mit Gruppen
    pass


if __name__ == "__main__":
    print("=" * 60)
    print("🔍 KAPITEL 17: REGEX-DETEKTIV TESTLAUF")
    print("=" * 60)

    # 1. E-Mail Test
    test_mail = "tutor@antigravity-academy.de"
    print(f"E-Mail '{test_mail}' gültig?:", ist_gueltige_email(test_mail))

    # 2. Telefonnummern
    text = "Zentrale: +49 89 1234567, Mobil: 0171-9876543, Büro: (030) 555444"
    print("Gefundene Telefonnummern:", finde_telefonnummern(text))

    # 3. Hashtags
    tweet = "Python 3.12 ist genial! #python #data_science #AI2026 #süß"
    print("Gefundene Hashtags:", extrahiere_hashtags(tweet))

    # 4. IBAN-Maskierung
    vertraulich = "Konto A: DE89370400440532013000, Konto B: AT611904300234573201"
    print("Maskierter Text:", maskiere_iban(vertraulich))

    # 5. ISO-Datum
    datum = "2026-08-29"
    print("Geparstes Datum:", parse_datum_iso(datum))
