r"""
Kapitel 18: Funktionale Programmierung & Pythonic Code ⚡🔄
=========================================================
Aufgabe: Schreibe eleganten, expressiven und hocheffizienten Python-Code!
Nutze funktionale Werkzeuge wie lambda, enumerate, zip, map, filter,
sorted(..., key=...) sowie any und all zur Datenverarbeitung.

Themen:
1. enumerate(iterable, start=0) – Index und Wert elegant durchlaufen
2. zip(iter_a, iter_b) – Sequenzen parallel verknüpfen
3. Lambda-Funktionen – Anonyme Einzeiler (lambda x: ...)
4. map() & filter() – Transformation & Filterung auf Datenströmen
5. Custom Sorting – sorted() & max()/min() mit key=lambda ...
6. Kontrollfunktionen – any() und all() für Datenvalidierung
"""

from typing import List, Dict, Any, Optional


# ==============================================================================
# TEIL 1: ENUMERATE – NUMMERIERTE LISTEN
# ==============================================================================

def nummerierte_liste(elemente: List[str], start: int = 1) -> List[str]:
    """
    TODO 1: Erstellt eine nummerierte Liste von Strings mit `enumerate()`.

    Parameter:
        elemente (List[str]): Eine Liste von Zeichenketten (z.B. ["Python", "Java", "Rust"]).
        start (int): Die Startnummer für die Aufzählung (Standard: 1).

    Rückgabe:
        List[str]: Eine formatierte Liste wie ["1. Python", "2. Java", "3. Rust"].
                   Falls `elemente` leer ist, soll eine leere Liste [] zurückgegeben werden.

    Beispiele:
        nummerierte_liste(["Python", "Java", "Rust"])
        -> ["1. Python", "2. Java", "3. Rust"]

        nummerierte_liste(["A", "B"], start=0)
        -> ["0. A", "1. B"]

    Tipp:
        Nutze eine List Comprehension mit enumerate:
        [f"{i}. {item}" for i, item in enumerate(elemente, start=start)]
    """
    # 🎯 TEILZIEL 1: Implementiere nummerierte_liste mit enumerate()
    pass


# ==============================================================================
# TEIL 2: ZIP – SEQUENZEN VERKNÜPFEN (KATALOG ERSTELLEN)
# ==============================================================================

def kombiniere_katalog(artikel: List[str], preise: List[float]) -> Dict[str, float]:
    """
    TODO 2: Verknüpft zwei getrennte Listen (Artikelnamen und Preise) mithilfe
    von `zip()` zu einem Produktkatalog-Dictionary.

    Parameter:
        artikel (List[str]): Liste der Artikelbezeichnungen.
        preise (List[float]): Liste der entsprechenden Preise.

    Rückgabe:
        Dict[str, float]: Ein Dictionary mit {artikel: preis}.
                          Falls eine Liste kürzer ist, schneidet `zip()` automatisch ab.

    Beispiele:
        kombiniere_katalog(["Apfel", "Banane", "Orange"], [0.99, 1.49, 1.99])
        -> {"Apfel": 0.99, "Banane": 1.49, "Orange": 1.99}

    Tipp:
        dict(zip(artikel, preise)) erzeugt direkt das fertige Dictionary!
    """
    # 🎯 TEILZIEL 2: Kombiniere Listen mit zip()
    pass


# ==============================================================================
# TEIL 3: MAP, FILTER & LAMBDA – DATEN PIPELINE
# ==============================================================================

def quadriere_und_filtere(zahlen: List[int]) -> List[int]:
    """
    TODO 3: Filtert alle ungeraden Zahlen aus der Eingabeliste und quadriert diese.
    Nutze dafür funktionale Methoden (`filter`, `map` mit `lambda`) oder Comprehensions.

    Regeln:
    - 1. Schritt (Filter): Behalte nur ungerade Zahlen (z.B. x % 2 != 0).
    - 2. Schritt (Map): Berechne das Quadrat jeder ungeraden Zahl (x ** 2).

    Beispiele:
        quadriere_und_filtere([1, 2, 3, 4, 5])
        -> Ungerade: [1, 3, 5] -> Quadriert: [1, 9, 25]

        quadriere_und_filtere([2, 4, 6])
        -> []

        quadriere_und_filtere([-3, -2, 0, 3])
        -> [9, 9]

    Tipp mit funktionaler Pipeline:
        ungerade = filter(lambda x: x % 2 != 0, zahlen)
        quadriert = map(lambda x: x ** 2, ungerade)
        return list(quadriert)
    """
    # 🎯 TEILZIEL 3: Implementiere die funktionale Transformation
    pass


# ==============================================================================
# TEIL 4: CUSTOM SORTING – SORTIEREN MIT KEY=LAMBDA
# ==============================================================================

def sortiere_personen_nach_alter(personen: List[Dict[str, Any]], absteigend: bool = False) -> List[Dict[str, Any]]:
    """
    TODO 4: Sortiert eine Liste von Personen-Dictionaries anhand des Schlüssels 'alter'.

    Parameter:
        personen (List[Dict[str, Any]]): z.B. [{'name': 'Alice', 'alter': 30}, {'name': 'Bob', 'alter': 22}]
        absteigend (bool): False = aufsteigend (Standard), True = absteigend (älteste zuerst).

    Rückgabe:
        List[Dict[str, Any]]: Eine neue, sortierte Liste von Dictionaries.

    Beispiele:
        team = [{'name': 'Alice', 'alter': 30}, {'name': 'Bob', 'alter': 22}, {'name': 'Charlie', 'alter': 45}]
        sortiere_personen_nach_alter(team)
        -> [{'name': 'Bob', 'alter': 22}, {'name': 'Alice', 'alter': 30}, {'name': 'Charlie', 'alter': 45}]

    Tipp:
        sorted(personen, key=lambda p: p["alter"], reverse=absteigend)
    """
    # 🎯 TEILZIEL 4: Sortiere mit sorted() und Lambda-Key
    pass


# ==============================================================================
# TEIL 5: KONTROLLFUNKTIONEN ALL & ANY
# ==============================================================================

def alle_volljaehrig(alter_liste: List[int], mindestalter: int = 18) -> bool:
    """
    TODO 5: Prüft mit `all()`, ob ausnahmslos ALLE Personen in der Liste
    mindestens das `mindestalter` erreicht haben.

    Parameter:
        alter_liste (List[int]): Liste mit Altersangaben in Jahren.
        mindestalter (int): Das geforderte Mindestalter (Standard: 18).

    Rückgabe:
        bool: True wenn alle >= mindestalter (oder Liste leer ist), sonst False.

    Beispiele:
        alle_volljaehrig([19, 25, 42, 18]) -> True
        alle_volljaehrig([19, 17, 25, 30]) -> False (17 ist unter 18)
        alle_volljaehrig([])               -> True (leere Menge erfüllt Kriterium trivial)

    Tipp:
        all(alter >= mindestalter for alter in alter_liste)
    """
    # 🎯 TEILZIEL 5: Prüfe Volljährigkeit mit all()
    pass


def mindestens_ein_treffer(ergebnisse: List[bool]) -> bool:
    """
    TODO 6: Prüft mit `any()`, ob mindestens ein Element in der Liste True ist.

    Parameter:
        ergebnisse (List[bool]): Liste von Wahrheitswerten.

    Rückgabe:
        bool: True wenn mindestens ein Element True ist, sonst False (bei leerer Liste False).

    Beispiele:
        mindestens_ein_treffer([False, False, True, False]) -> True
        mindestens_ein_treffer([False, False, False])       -> False
        mindestens_ein_treffer([])                          -> False

    Tipp:
        return any(ergebnisse)
    """
    # 🎯 TEILZIEL 6: Prüfe Treffer mit any()
    pass


# ==============================================================================
# TEIL 7: BONUS: EXTREMWERTE FINDEN MIT MAX / MIN UND KEY=LAMBDA
# ==============================================================================

def finde_extrem_produkt(produkte: List[Dict[str, Any]], modus: str = "teuerstes") -> Dict[str, Any]:
    """
    TODO 7 (Bonus): Findet das teuerste oder günstigste Produkt in einer Liste.

    Parameter:
        produkte (List[Dict[str, Any]]): z.B. [{'titel': 'Laptop', 'preis': 999.0}, ...]
        modus (str): "teuerstes" (nutzt max()) oder "billigstes" (nutzt min()).

    Rückgabe:
        Dict[str, Any]: Das Produkt-Dictionary mit dem maximalen/minimalen Preis.

    Exceptions:
        ValueError: Wenn `produkte` leer ist oder `modus` weder "teuerstes" noch "billigstes" ist.

    Tipp:
        max(produkte, key=lambda p: p["preis"]) bzw. min(produkte, key=lambda p: p["preis"])
    """
    # 🎯 TEILZIEL 7: Finde Extremprodukt mit max/min(..., key=lambda)
    pass


if __name__ == "__main__":
    print("=" * 60)
    print("⚡ KAPITEL 18: FUNKTIONALE PROGRAMMIERUNG TESTLAUF")
    print("=" * 60)

    # 1. Enumerate
    sprachen = ["Python", "TypeScript", "Rust", "Go"]
    print("Nummerierte Sprachen:", nummerierte_liste(sprachen))

    # 2. Zip
    artikel = ["Kaffee", "Tee", "Kuchen"]
    preise = [3.50, 2.80, 4.20]
    print("Katalog:", kombiniere_katalog(artikel, preise))

    # 3. Map & Filter
    zahlen = [1, 2, 3, 4, 5, 6, 7]
    print("Ungerade quadriert:", quadriere_und_filtere(zahlen))

    # 4. Custom Sorting
    team = [
        {"name": "Alice", "alter": 28},
        {"name": "Bob", "alter": 22},
        {"name": "Charlie", "alter": 35}
    ]
    print("Team sortiert (jung -> alt):", sortiere_personen_nach_alter(team))

    # 5. All & Any
    altersgruppe = [20, 22, 19, 18]
    print("Alle volljährig?:", alle_volljaehrig(altersgruppe))
    print("Mindestens ein Treffer?:", mindestens_ein_treffer([False, False, True]))
