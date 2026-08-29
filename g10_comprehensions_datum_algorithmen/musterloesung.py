"""
Kapitel G10: Comprehensions, Datum & Algorithmen – Musterlösung
================================================================
Schulabgleich: Thema 13.0 & 15.1

Hier findest du die vollständige Musterlösung zu allen Aufgaben.
"""

from datetime import datetime, date, timedelta
from typing import List, Dict, Union


# TODO 1: Quadratzahlen gerader Zahlen (List Comprehension)
def quadratzahlen_gerade(zahlen: List[int]) -> List[int]:
    """Gibt die Quadrate aller geraden Zahlen als List Comprehension zurück."""
    return [x ** 2 for x in zahlen if x % 2 == 0]


# TODO 2: Wörter nach Mindestlänge filtern
def filtriere_lange_woerter(woerter: List[str], min_laenge: int) -> List[str]:
    """Filtert alle Wörter heraus, die mindestens 'min_laenge' Zeichen lang sind."""
    return [w for w in woerter if len(w) >= min_laenge]


# TODO 3: Tage bis Zieldatum berechnen (datetime & timedelta)
def tage_bis_datum(ziel_datum_str: str) -> int:
    """Berechnet die Anzahl der Tage von heute bis zum angegebenen Zieldatum (YYYY-MM-DD)."""
    ziel_datum = datetime.strptime(ziel_datum_str, "%Y-%m-%d").date()
    heute = date.today()
    return (ziel_datum - heute).days


# TODO 4: Datum im deutschen Format darstellen (.strftime)
def formatiere_deutsches_datum(datum_obj: Union[date, datetime]) -> str:
    """Formatiert ein date- oder datetime-Objekt in das deutsche Format DD.MM.YYYY."""
    return datum_obj.strftime("%d.%m.%Y")


# TODO 5: Älteste Person finden (Algorithmus: Maximum / Key-Suche)
def finde_aelteste_person(personen: List[Dict[str, Union[str, int]]]) -> str:
    """Findet in einer Liste von Personen-Dicts die älteste Person und gibt deren Namen zurück."""
    if not personen:
        return ""
    aelteste = max(personen, key=lambda p: p["alter"])
    return str(aelteste["name"])


if __name__ == "__main__":
    print("--- 🚀 Musterlösung G10: Comprehensions, Datum & Algorithmen ---")

    # 1. Quadratzahlen
    test_zahlen = [1, 2, 3, 4, 5, 6]
    print("Gerade Quadrate:", quadratzahlen_gerade(test_zahlen))

    # 2. Wörter filtern
    woerter_liste = ["Python", "ist", "klasse", "und", "schnell"]
    print("Wörter >= 6:", filtriere_lange_woerter(woerter_liste, 6))

    # 3. Tage bis Zieldatum
    morgen = (date.today() + timedelta(days=1)).strftime("%Y-%m-%d")
    print(f"Tage bis morgen ({morgen}):", tage_bis_datum(morgen))

    # 4. Deutsches Datum
    print("Heute im deutschen Format:", formatiere_deutsches_datum(date.today()))

    # 5. Älteste Person
    leute = [
        {"name": "Anna", "alter": 25},
        {"name": "Ben", "alter": 35},
        {"name": "Clara", "alter": 28}
    ]
    print("Älteste Person:", finde_aelteste_person(leute))
