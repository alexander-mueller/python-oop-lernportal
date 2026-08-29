"""
Kapitel 18: Funktionale Programmierung & Pythonic Code – Musterlösung 💡
========================================================================
Vollständige Referenzlösung für alle Teilaufgaben aus Kapitel 18.
"""

from typing import List, Dict, Any, Optional


def nummerierte_liste(elemente: List[str], start: int = 1) -> List[str]:
    """
    Erstellt eine nummerierte Liste von Strings mit enumerate().
    """
    return [f"{i}. {item}" for i, item in enumerate(elemente, start=start)]


def kombiniere_katalog(artikel: List[str], preise: List[float]) -> Dict[str, float]:
    """
    Verknüpft Artikelnamen und Preise mittels zip() zu einem Dictionary.
    """
    return dict(zip(artikel, preise))


def quadriere_und_filtere(zahlen: List[int]) -> List[int]:
    """
    Filtert ungerade Zahlen und quadriert sie funktional mit map() und filter().
    """
    return list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, zahlen)))


def sortiere_personen_nach_alter(personen: List[Dict[str, Any]], absteigend: bool = False) -> List[Dict[str, Any]]:
    """
    Sortiert eine Liste von Personen-Dictionaries anhand von 'alter' mit sorted() und key=lambda.
    """
    return sorted(personen, key=lambda p: p["alter"], reverse=absteigend)


def alle_volljaehrig(alter_liste: List[int], mindestalter: int = 18) -> bool:
    """
    Prüft mit all(), ob alle Personen in der Liste mindestens mindestalter Jahre alt sind.
    """
    return all(alter >= mindestalter for alter in alter_liste)


def mindestens_ein_treffer(ergebnisse: List[bool]) -> bool:
    """
    Prüft mit any(), ob mindestens ein Element True ist.
    """
    return any(ergebnisse)


def finde_extrem_produkt(produkte: List[Dict[str, Any]], modus: str = "teuerstes") -> Dict[str, Any]:
    """
    Findet das teuerste oder günstigste Produkt mit max() / min() und key=lambda.
    """
    if not produkte:
        raise ValueError("Produktliste darf nicht leer sein!")
    if modus == "teuerstes":
        return max(produkte, key=lambda p: p["preis"])
    elif modus == "billigstes":
        return min(produkte, key=lambda p: p["preis"])
    else:
        raise ValueError(f"Ungültiger Modus '{modus}'. Erlaubt sind 'teuerstes' und 'billigstes'.")


if __name__ == "__main__":
    print("Musterlösung Kapitel 18:")
    print("1. Enumerate:", nummerierte_liste(["Python", "Rust", "Go"]))
    print("2. Zip:", kombiniere_katalog(["Kaffee", "Kuchen"], [3.5, 4.2]))
    print("3. Map/Filter:", quadriere_und_filtere([1, 2, 3, 4, 5]))
    team = [{"name": "A", "alter": 30}, {"name": "B", "alter": 20}]
    print("4. Custom Sort:", sortiere_personen_nach_alter(team))
    print("5. all():", alle_volljaehrig([20, 21, 18]))
    print("6. any():", mindestens_ein_treffer([False, True]))
    items = [{"titel": "A", "preis": 10}, {"titel": "B", "preis": 50}]
    print("7. Extremwert:", finde_extrem_produkt(items, "teuerstes"))
