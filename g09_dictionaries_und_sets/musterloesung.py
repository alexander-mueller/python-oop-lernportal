"""
Kapitel G09: Dictionaries & Sets (Mengen) – Musterlösung
=========================================================
Schulabgleich: Thema 15.0 (Dictionaries und Mengen)

Hier findest du die vollständige Musterlösung zu allen Aufgaben.
"""

from typing import List, Dict, Set


# TODO 1: Wörter-Häufigkeitszähler
def woerter_haeufigkeit(text: str) -> Dict[str, int]:
    """Zählt die Häufigkeit aller Wörter in einem gegebenen Text (case-insensitive)."""
    # 1. Satzzeichen entfernen und Text in Kleinbuchstaben umwandeln
    satzzeichen = ".,!?;:()\"'[]{}<>"
    bereinigter_text = text.lower()
    for z in satzzeichen:
        bereinigter_text = bereinigter_text.replace(z, " ")
    
    # 2. In Wörter zerlegen
    woerter = bereinigter_text.split()
    
    # 3. Häufigkeiten zählen
    haeufigkeit: Dict[str, int] = {}
    for wort in woerter:
        haeufigkeit[wort] = haeufigkeit.get(wort, 0) + 1
        
    return haeufigkeit


# TODO 2: Telefonbuch-Suche mit .get()
def telefonbuch_suche(telefonbuch: Dict[str, str], name: str) -> str:
    """Sucht eine Telefonnummer im Telefonbuch mit sicherer .get() Abfrage."""
    return telefonbuch.get(name, "Nicht gefunden")


# TODO 3: Gemeinsame Interessen (Mengenoperation Schnittmenge)
def gemeinsame_interessen(person_a_hobbys: Set[str], person_b_hobbys: Set[str]) -> Set[str]:
    """Ermittelt die Schnittmenge der Hobbys zweier Personen."""
    return person_a_hobbys & person_b_hobbys


# TODO 4: Duplikate entfernen & Reihenfolge beibehalten
def entferne_duplikate_behalte_reihenfolge(liste: list) -> list:
    """Entfernt Duplikate aus einer Liste unter Beibehaltung der Reihenfolge."""
    seen = set()
    ergebnis = []
    for element in liste:
        if element not in seen:
            seen.add(element)
            ergebnis.append(element)
    return ergebnis


if __name__ == "__main__":
    print("--- 📚 Musterlösung G09: Dictionaries & Sets ---")
    
    # 1. Wörter-Häufigkeit
    text = "Python ist super. Python macht Spaß! Ist Python leicht? Ja!"
    print("Häufigkeiten:", woerter_haeufigkeit(text))
    
    # 2. Telefonbuch
    buch = {"Anna": "0171-123456", "Ben": "0160-987654"}
    print("Suche Anna:", telefonbuch_suche(buch, "Anna"))
    print("Suche Clara:", telefonbuch_suche(buch, "Clara"))
    
    # 3. Gemeinsame Interessen
    a = {"Gaming", "Klettern", "Musik"}
    b = {"Kochen", "Gaming", "Musik", "Lesen"}
    print("Gemeinsame Hobbys:", gemeinsame_interessen(a, b))
    
    # 4. Duplikate entfernen
    zahlen = [1, 3, 2, 3, 1, 4, 2, 5]
    print("Bereinigte Zahlenliste:", entferne_duplikate_behalte_reihenfolge(zahlen))
