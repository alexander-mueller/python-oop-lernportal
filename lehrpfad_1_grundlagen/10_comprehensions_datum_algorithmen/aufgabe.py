"""
Kapitel G10: Comprehensions, Datum & Algorithmen – Aufgabenblatt
================================================================
Schulabgleich: Thema 13.0 & 15.1

In diesem Kapitel meisterst du drei fortgeschrittene Kernkompetenzen:
1. List & Dict Comprehensions (kompakter, eleganter Python-Code)
2. Datum & Uhrzeit mit dem 'datetime'-Modul (Rechnen mit Tagen & Zeitspannen)
3. Grundlegende Algorithmen (Filtern, Suchen und Min/Max-Ermittlung)

Bearbeite die Aufgaben von TODO 1 bis TODO 5.
Überprüfe deine Lösung im Terminal mit:
    python3 test_aufgabe.py
"""

from datetime import datetime, date, timedelta
from typing import List, Dict, Union


# ==============================================================================
# 🎯 TEILZIEL 1 (TODO 1): Quadratzahlen gerader Zahlen (List Comprehension)
# ------------------------------------------------------------------------------
# Schreibe eine Funktion 'quadratzahlen_gerade(zahlen: list[int]) -> list[int]'.
#
# Anforderungen:
# 1. Verwende eine elegante List Comprehension: [ausdruck for x in ... if ...]
# 2. Filtere alle geraden Zahlen (x % 2 == 0) heraus.
# 3. Berechne für jede gefilterte Zahl das Quadrat (x ** 2).
# 4. Gib die neue Liste zurück.
#
# Beispiel:
#   eingabe = [1, 2, 3, 4, 5, 6]
#   Ergebnis: [4, 16, 36] (denn 2²=4, 4²=16, 6²=36)
# ==============================================================================

def quadratzahlen_gerade(zahlen: List[int]) -> List[int]:
    """Gibt die Quadrate aller geraden Zahlen als List Comprehension zurück."""
    # 🎯 TEILZIEL 1: Implementiere die Logik Schritt für Schritt:
    # 💡 Tipp: Beachte Datentypen und das abschließende return!
    pass


# ==============================================================================
# 🎯 TEILZIEL 2 (TODO 2): Wörter nach Mindestlänge filtern
# ------------------------------------------------------------------------------
# Schreibe eine Funktion 'filtriere_lange_woerter(woerter: list[str], min_laenge: int) -> list[str]'.
#
# Anforderungen:
# 1. Verwende vorzugsweise eine List Comprehension.
# 2. Behalte nur Wörter, deren Zeichenlänge größer oder gleich 'min_laenge' ist (len(w) >= min_laenge).
# 3. Gib die gefilterte Liste zurück.
#
# Beispiel:
#   liste = ["Python", "ist", "eine", "tolle", "Sprache"]
#   filtriere_lange_woerter(liste, 5) -> ["Python", "tolle", "Sprache"]
# ==============================================================================

def filtriere_lange_woerter(woerter: List[str], min_laenge: int) -> List[str]:
    """Filtert alle Wörter heraus, die mindestens 'min_laenge' Zeichen lang sind."""
    # 🎯 TEILZIEL 2: Implementiere die Logik Schritt für Schritt:
    # 💡 Tipp: Beachte Datentypen und das abschließende return!
    pass


# ==============================================================================
# 🎯 TEILZIEL 3 (TODO 3): Tage bis Zieldatum berechnen (datetime & timedelta)
# ------------------------------------------------------------------------------
# Schreibe eine Funktion 'tage_bis_datum(ziel_datum_str: str) -> int'.
#
# Anforderungen:
# 1. Der Parameter 'ziel_datum_str' ist ein Datum im Format "YYYY-MM-DD" (z.B. "2026-12-24").
# 2. Lies den Text mit 'datetime.strptime(ziel_datum_str, "%Y-%m-%d").date()' ein.
# 3. Ermittle das heutige Datum mit 'date.today()'.
# 4. Berechne die Differenz: (ziel_datum - heute).days.
# 5. Gib die Anzahl der verbleibenden Tage als Ganzzahl (int) zurück.
#    (Positiv = in der Zukunft, Negativ = in der Vergangenheit, 0 = heute).
# ==============================================================================

def tage_bis_datum(ziel_datum_str: str) -> int:
    """Berechnet die Anzahl der Tage von heute bis zum angegebenen Zieldatum (YYYY-MM-DD)."""
    # 🎯 TEILZIEL 3: Implementiere die Logik Schritt für Schritt:
    # 💡 Tipp: Beachte Datentypen und das abschließende return!
    pass


# ==============================================================================
# 🎯 TEILZIEL 4 (TODO 4): Datum im deutschen Format darstellen (.strftime)
# ------------------------------------------------------------------------------
# Schreibe eine Funktion 'formatiere_deutsches_datum(datum_obj: Union[date, datetime]) -> str'.
#
# Anforderungen:
# 1. Die Funktion erhält ein 'date'- oder 'datetime'-Objekt.
# 2. Formatiere das Datum mit '.strftime()' im deutschen Standard-Format "DD.MM.YYYY" (z.B. "24.12.2026").
#    Tipp: %d = Tag (zweistellig), %m = Monat (zweistellig), %Y = Jahr (vierstellig).
# 3. Gib den formatierten String zurück.
# ==============================================================================

def formatiere_deutsches_datum(datum_obj: Union[date, datetime]) -> str:
    """Formatiert ein date- oder datetime-Objekt in das deutsche Format DD.MM.YYYY."""
    # 🎯 TEILZIEL 4: Implementiere die Logik Schritt für Schritt:
    # 💡 Tipp: Beachte Datentypen und das abschließende return!
    pass


# ==============================================================================
# 🎯 TEILZIEL 5 (TODO 5): Älteste Person finden (Algorithmus: Maximum / Key-Suche)
# ------------------------------------------------------------------------------
# Schreibe eine Funktion 'finde_aelteste_person(personen: list[dict]) -> str'.
#
# Anforderungen:
# 1. 'personen' ist eine Liste von Dictionaries, z.B.:
#    [{"name": "Anna", "alter": 25}, {"name": "Ben", "alter": 32}, {"name": "Clara", "alter": 19}]
# 2. Wenn die Liste leer ist, gib einen leeren String "" zurück.
# 3. Finde die Person mit dem höchsten 'alter' (z.B. mit Schleife oder max(..., key=...)).
# 4. Gib den 'name' dieser ältesten Person zurück (im Beispiel: "Ben").
# ==============================================================================

def finde_aelteste_person(personen: List[Dict[str, Union[str, int]]]) -> str:
    """Findet in einer Liste von Personen-Dicts die älteste Person und gibt deren Namen zurück."""
    # 🎯 TEILZIEL 5: Implementiere die Logik Schritt für Schritt:
    # 💡 Tipp: Beachte Datentypen und das abschließende return!
    pass


# ==============================================================================
# Hauptprogramm zum Ausprobieren:
# (Du kannst diese Datei direkt mit 'python3 aufgabe.py' ausführen)
# ==============================================================================
if __name__ == "__main__":
    print("--- 🚀 Testlauf: Comprehensions, Datum & Algorithmen ---")

    # Test TODO 1
    zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Quadrate gerader Zahlen:", quadratzahlen_gerade(zahlen))

    # Test TODO 2
    woerter = ["Code", "Python", "KI", "Entwicklung", "Funktion", "Loop"]
    print("Wörter >= 6 Zeichen:", filtriere_lange_woerter(woerter, 6))

    # Test TODO 3 & 4
    heute = date.today()
    print("Heutiges deutsches Datum:", formatiere_deutsches_datum(heute))
    
    silvester = f"{heute.year}-12-31"
    print(f"Tage bis zum Jahresende ({silvester}):", tage_bis_datum(silvester))

    # Test TODO 5
    gruppe = [
        {"name": "Lisa", "alter": 21},
        {"name": "Markus", "alter": 29},
        {"name": "Sarah", "alter": 24}
    ]
    print("Älteste Person in der Gruppe:", finde_aelteste_person(gruppe))
