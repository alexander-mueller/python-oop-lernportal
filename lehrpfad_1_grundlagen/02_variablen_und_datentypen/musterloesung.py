"""
Grundlagen 02: Variablen & Datentypen – Musterlösung
=====================================================

Vollständige Referenzlösung für alle Aufgaben.
"""

def bestimme_typ_name(wert) -> str:
    """Gibt den deutschen Namen des Datentyps als String zurück."""
    # Wichtig: bool zuerst prüfen, da bool von int erbt!
    if isinstance(wert, bool):
        return "Wahrheitswert"
    elif isinstance(wert, int):
        return "Ganzzahl"
    elif isinstance(wert, float):
        return "Kommazahl"
    elif isinstance(wert, str):
        return "Text"
    else:
        return "Unbekannt"


def summe_aus_texten(text_a: str, text_b: str) -> int:
    """Wandelt zwei Zahlen-Strings in echte Integers um und berechnet deren Summe."""
    return int(text_a) + int(text_b)


def formatiere_preis(preis_float: float) -> str:
    """Formatiert einen Preis mit genau 2 Nachkommastellen und Euro-Zeichen."""
    return f"{preis_float:.2f} €"


def ist_volljaehrig(alter: int) -> bool:
    """Prüft, ob ein Alter >= 18 ist und gibt True/False zurück."""
    return alter >= 18


if __name__ == "__main__":
    print("=" * 55)
    print("📦 MUSTERLÖSUNG: G02 VARIABLEN & DATENTYPEN")
    print("=" * 55)
    print("bestimme_typ_name(42)       =", bestimme_typ_name(42))
    print("bestimme_typ_name(3.14)     =", bestimme_typ_name(3.14))
    print("bestimme_typ_name('Python') =", bestimme_typ_name("Python"))
    print("bestimme_typ_name(True)     =", bestimme_typ_name(True))
    print("summe_aus_texten('10', '20')=", summe_aus_texten("10", "20"))
    print("formatiere_preis(19.99)     =", formatiere_preis(19.99))
    print("ist_volljaehrig(17)         =", ist_volljaehrig(17))
    print("ist_volljaehrig(18)         =", ist_volljaehrig(18))
