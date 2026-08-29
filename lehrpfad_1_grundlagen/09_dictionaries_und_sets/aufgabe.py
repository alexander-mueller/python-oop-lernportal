"""
Kapitel G09: Dictionaries & Sets (Mengen) – Aufgabenblatt
=========================================================
Schulabgleich: Thema 15.0 (Dictionaries und Mengen)

In diesem Kapitel lernst du zwei der wichtigsten Datenstrukturen in Python kennen:
1. Dictionaries (Schlüssel-Wert-Paare wie im Wörterbuch oder Telefonbuch)
2. Sets (Mengen von eindeutigen Elementen ohne Duplikate)

Bearbeite die Aufgaben von TODO 1 bis TODO 4.
Überprüfe deine Lösung im Terminal mit:
    python3 test_aufgabe.py
"""

from typing import List, Dict, Set


# ==============================================================================
# 🎯 TEILZIEL 1 (TODO 1): Wörter-Häufigkeitszähler
# ------------------------------------------------------------------------------
# Schreibe eine Funktion 'woerter_haeufigkeit(text: str) -> dict[str, int]'.
#
# Anforderungen:
# 1. Wandle den gesamten Text in Kleinbuchstaben um (.lower()).
# 2. Entferne gängige Satzzeichen (.,!?;:) aus dem Text oder bereinige die Wörter.
# 3. Zerlege den Text in einzelne Wörter (.split()).
# 4. Zähle mit einem Dictionary, wie oft jedes Wort vorkommt.
# 5. Gib das fertige Dictionary {wort: anzahl} zurück.
#
# Beispiel:
#   text = "Apfel Banane Apfel Birne Banane Apfel"
#   Ergebnis: {"apfel": 3, "banane": 2, "birne": 1}
# ==============================================================================

def woerter_haeufigkeit(text: str) -> Dict[str, int]:
    """Zählt die Häufigkeit aller Wörter in einem gegebenen Text (case-insensitive)."""
    # 🎯 TEILZIEL 1: Implementiere die Logik Schritt für Schritt:
    # 💡 Tipp: Beachte Datentypen und das abschließende return!
    pass


# ==============================================================================
# 🎯 TEILZIEL 2 (TODO 2): Telefonbuch-Suche mit .get()
# ------------------------------------------------------------------------------
# Schreibe eine Funktion 'telefonbuch_suche(telefonbuch: dict[str, str], name: str) -> str'.
#
# Anforderungen:
# 1. Suche im Dictionary 'telefonbuch' nach dem Schlüssel 'name'.
# 2. Verwende dafür die sichere Methode .get(key, standardwert), um einen KeyError
#    zu vermeiden!
# 3. Wenn der Name existiert, gib die zugehörige Telefonnummer zurück.
# 4. Wenn der Name NICHT existiert, gib den Text "Nicht gefunden" zurück.
#
# Beispiel:
#   buch = {"Anna": "0171-123456", "Ben": "0160-987654"}
#   telefonbuch_suche(buch, "Anna")  -> "0171-123456"
#   telefonbuch_suche(buch, "Clara") -> "Nicht gefunden"
# ==============================================================================

def telefonbuch_suche(telefonbuch: Dict[str, str], name: str) -> str:
    """Sucht eine Telefonnummer im Telefonbuch mit sicherer .get() Abfrage."""
    # 🎯 TEILZIEL 2: Implementiere die Logik Schritt für Schritt:
    # 💡 Tipp: Beachte Datentypen und das abschließende return!
    pass


# ==============================================================================
# 🎯 TEILZIEL 3 (TODO 3): Gemeinsame Interessen (Mengenoperation Schnittmenge)
# ------------------------------------------------------------------------------
# Schreibe eine Funktion 'gemeinsame_interessen(person_a_hobbys: set, person_b_hobbys: set) -> set'.
#
# Anforderungen:
# 1. Die Funktion erhält zwei Mengen (Sets) mit Hobbys von zwei Personen.
# 2. Ermittle alle Hobbys, die BEIDE Personen gemeinsam haben (Schnittmenge / Intersection).
# 3. Nutze entweder den Mengen-Operator '&' oder die Methode '.intersection()'.
# 4. Gib das resultierende Set zurück.
#
# Beispiel:
#   a = {"Gaming", "Klettern", "Musik"}
#   b = {"Kochen", "Gaming", "Musik", "Lesen"}
#   gemeinsame_interessen(a, b) -> {"Gaming", "Musik"}
# ==============================================================================

def gemeinsame_interessen(person_a_hobbys: Set[str], person_b_hobbys: Set[str]) -> Set[str]:
    """Ermittelt die Schnittmenge der Hobbys zweier Personen."""
    # 🎯 TEILZIEL 3: Implementiere die Logik Schritt für Schritt:
    # 💡 Tipp: Beachte Datentypen und das abschließende return!
    pass


# ==============================================================================
# 🎯 TEILZIEL 4 (TODO 4): Duplikate entfernen & Reihenfolge beibehalten
# ------------------------------------------------------------------------------
# Schreibe eine Funktion 'entferne_duplikate_behalte_reihenfolge(liste: list) -> list'.
#
# Problem: Ein normales 'set(liste)' entfernt Duplikate, verliert aber die Reihenfolge!
# Anforderungen:
# 1. Entferne alle doppelten Elemente aus der übergebenen Liste.
# 2. Die ursprüngliche Reihenfolge des ERSTEN Auftretens der Elemente muss erhalten bleiben.
# 3. Nutze z.B. ein 'seen = set()', um bereits gesehene Elemente blitzschnell nachzuschlagen,
#    und füge neue Elemente einer Ergebnisliste hinzu.
# 4. Gib die bereinigte Liste zurück.
#
# Beispiel:
#   eingabe = [1, 3, 2, 3, 1, 4, 2, 5]
#   Ergebnis: [1, 3, 2, 4, 5]
# ==============================================================================

def entferne_duplikate_behalte_reihenfolge(liste: list) -> list:
    """Entfernt Duplikate aus einer Liste unter Beibehaltung der Reihenfolge."""
    # 🎯 TEILZIEL 4: Implementiere die Logik Schritt für Schritt:
    # 💡 Tipp: Beachte Datentypen und das abschließende return!
    pass


# ==============================================================================
# Hauptprogramm zum Ausprobieren:
# (Du kannst diese Datei direkt mit 'python3 aufgabe.py' ausführen)
# ==============================================================================
if __name__ == "__main__":
    print("--- 📚 Testlauf: Dictionaries & Sets ---")

    # Test TODO 1
    beispiel_text = "Python ist super. Python macht Spaß! Ist Python leicht? Ja!"
    haeufigkeiten = woerter_haeufigkeit(beispiel_text)
    print("Wort-Häufigkeiten:", haeufigkeiten)

    # Test TODO 2
    tbuch = {"Alice": "0151-111111", "Bob": "0172-222222"}
    print("Suche Alice:", telefonbuch_suche(tbuch, "Alice"))
    print("Suche Charlie:", telefonbuch_suche(tbuch, "Charlie"))

    # Test TODO 3
    hobbys_1 = {"Fotografie", "Reisen", "Schwimmen", "Python"}
    hobbys_2 = {"Kochen", "Python", "Reisen", "Yoga"}
    print("Gemeinsame Hobbys:", gemeinsame_interessen(hobbys_1, hobbys_2))

    # Test TODO 4
    tiere_mit_duplikaten = ["Katze", "Hund", "Katze", "Maus", "Hund", "Hamster"]
    eindeutige_tiere = entferne_duplikate_behalte_reihenfolge(tiere_mit_duplikaten)
    print("Ohne Duplikate (Reihenfolge fix):", eindeutige_tiere)
