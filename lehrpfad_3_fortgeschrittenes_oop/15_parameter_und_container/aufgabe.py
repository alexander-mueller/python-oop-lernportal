"""
Kapitel 15: Parameter (*args, **kwargs) & Eigene Container-Klassen 🎒📦
======================================================================
Aufgabe: Lerne flexible Funktionsparameter kennen und baue eine
vollwertige Gaming-Inventar-Containerklasse mit magischen Dunder-Methoden!

Themen:
1. *args (beliebig viele Positionsargumente als Tupel)
2. **kwargs (beliebig viele Schlüsselwortargumente als Dictionary)
3. Argument-Unpacking (*liste, **dict)
4. Eigene Container mit __len__, __getitem__, __setitem__, __delitem__, __contains__, __iter__
"""

import math
from typing import Union, List, Optional, Dict, Any, Iterator


# ==============================================================================
# TEIL 1: FUNKTIONEN MIT *ARGS UND **KWARGS
# ==============================================================================

def berechne_gesamtsumme(*zahlen: float, rabatt_prozent: float = 0.0) -> float:
    """
    Berechnet die Gesamtsumme beliebig vieler Zahlen (*args) und wendet
    einen optionalen prozentualen Rabatt an.

    Parameter:
        *zahlen (float): Beliebig viele numerische Werte (als Tupel empfangen).
        rabatt_prozent (float): Rabatt in Prozent (0.0 bis 100.0). Standard ist 0.0.

    Rückgabe:
        float: Die berechnete Gesamtsumme nach Rabatt, gerundet auf 2 Nachkommastellen.

    Exceptions:
        ValueError: Falls rabatt_prozent < 0.0 oder > 100.0 ist.

    Beispiele:
        berechne_gesamtsumme(10.0, 20.0, 30.0) -> 60.0
        berechne_gesamtsumme(100.0, 50.0, rabatt_prozent=10.0) -> 135.0
        berechne_gesamtsumme() -> 0.0
    """
    # ==========================================================================
    # TODO 1: Implementiere berechne_gesamtsumme
    # 1. Validiere rabatt_prozent: Liegt der Wert nicht zwischen 0.0 und 100.0,
    #    löse einen ValueError mit passender Nachricht aus.
    # 2. Summiere alle Werte in `zahlen` (wenn zahlen leer ist, ist die Summe 0.0).
    # 3. Ziehe den Rabatt ab: summe * (1.0 - rabatt_prozent / 100.0)
    # 4. Runde das Ergebnis mit round(..., 2) und gib es zurück.
    # ==========================================================================
    pass


def erstelle_profil(name: str, **details: Any) -> Dict[str, Any]:
    """
    Erstellt ein Profil-Dictionary mit dem Namen und beliebigen weiteren
    Schlüsselwort-Attributen (**kwargs).

    Parameter:
        name (str): Der Name der Person oder Spielfigur.
        **details (Any): Beliebige Zusatzinformationen (z.B. alter=25, klasse="Krieger").

    Rückgabe:
        Dict[str, Any]: Ein Dictionary, das {"name": name} enthält, ergänzt um
                        alle übergebenen Keyword-Argumente.

    Beispiele:
        erstelle_profil("Aragorn", klasse="Waldlaeufer", level=20)
        -> {"name": "Aragorn", "klasse": "Waldlaeufer", "level": 20}
    """
    # ==========================================================================
    # TODO 2: Implementiere erstelle_profil
    # 1. Erstelle ein Dictionary mit {"name": str(name)}.
    # 2. Füge alle Schlüssel-Wert-Paare aus `details` hinzu.
    # 3. Gib das fertige Dictionary zurück.
    # ==========================================================================
    pass


# ==============================================================================
# TEIL 2: DIE DATENKLASSE GEGENSTAND (ITEM)
# ==============================================================================

class Gegenstand:
    """
    Repräsentiert einen Gegenstand im Spielinventar.
    """

    def __init__(self, name: str, gewicht: float, wert: int = 0):
        """
        Initialisiert einen Gegenstand.

        Parameter:
            name (str): Bezeichnung des Gegenstands.
            gewicht (float): Gewicht in Kilogramm (muss >= 0 sein).
            wert (int): Verkaufswert in Goldstücken (muss >= 0 sein, Standard 0).

        Exceptions:
            ValueError: Falls gewicht < 0 oder wert < 0 ist.
        """
        # ==========================================================================
        # TODO 3: Implementiere Gegenstand.__init__, __repr__, __str__ und __eq__
        # 1. Validiere gewicht >= 0 und wert >= 0 (sonst ValueError).
        # 2. Setze self.name = str(name), self.gewicht = float(gewicht), self.wert = int(wert).
        # ==========================================================================
        pass

    def __repr__(self) -> str:
        """
        Entwickler-Darstellung, z.B. "Gegenstand(name='Heiltrank', gewicht=0.5, wert=25)"
        """
        pass

    def __str__(self) -> str:
        """
        Benutzerfreundliche Darstellung, z.B. "Heiltrank (0.5kg, 25G)"
        """
        pass

    def __eq__(self, other: object) -> bool:
        """
        Zwei Gegenstände sind gleich, wenn Name, Gewicht und Wert übereinstimmen.
        """
        pass


# ==============================================================================
# TEIL 3: DIE EIGENE CONTAINER-KLASSE INVENTAR
# ==============================================================================

class Inventar:
    """
    Eine maßgeschneiderte Container-Klasse für ein Gaming-Rucksack-Inventar.
    Unterstützt Maximalgewicht, *args-Hinzufügen und alle Python-Container-Dunder!
    """

    def __init__(self, max_gewicht: float = 20.0, gegenstaende: Optional[List[Gegenstand]] = None):
        """
        Initialisiert das Inventar mit einem Maximalgewicht und optionalen Start-Gegenständen.

        Parameter:
            max_gewicht (float): Maximal tragbares Gewicht (muss > 0 sein, Standard 20.0).
            gegenstaende (Optional[List[Gegenstand]]): Optionale Liste von Gegenständen.

        Exceptions:
            ValueError: Falls max_gewicht <= 0 oder die Start-Gegenstände das Maximalgewicht überschreiten.
        """
        # ==========================================================================
        # TODO 4: Inventar-Initialisierung
        # 1. Validiere max_gewicht > 0 (sonst ValueError).
        # 2. Speichere self.max_gewicht = float(max_gewicht).
        # 3. Initialisiere eine interne Liste self._items = [].
        # 4. Falls `gegenstaende` übergeben wurden, füge sie mit self.hinzufuegen(*gegenstaende) hinzu.
        # ==========================================================================
        pass

    @property
    def gesamtgewicht(self) -> float:
        """
        Berechnet das aktuelle Gesamtgewicht aller enthaltenen Gegenstände,
        gerundet auf 2 Nachkommastellen.
        """
        # ==========================================================================
        # TODO 5a: Berechne Gesamtgewicht (Summe aller item.gewicht)
        # ==========================================================================
        pass

    @property
    def freie_kapazitaet(self) -> float:
        """
        Gibt das noch verfügbare Restgewicht bis zum Maximalgewicht zurück.
        """
        # ==========================================================================
        # TODO 5b: Berechne freie Kapazität (max_gewicht - gesamtgewicht, gerundet auf 2 Stellen)
        # ==========================================================================
        pass

    def hinzufuegen(self, *items: Gegenstand) -> None:
        """
        Fügt ein oder mehrere Gegenstände (*args) zum Inventar hinzu.

        Parameter:
            *items (Gegenstand): Beliebig viele Gegenstand-Objekte.

        Exceptions:
            TypeError: Falls ein Argument kein `Gegenstand`-Objekt ist.
            ValueError: Falls das Hinzufügen aller übergebenen Gegenstände
                        das Maximalgewicht des Inventars überschreiten würde.
        """
        # ==========================================================================
        # TODO 6: hinzufuegen mit *args
        # 1. Prüfe für jedes item in `items`, ob es eine Instanz von Gegenstand ist (sonst TypeError).
        # 2. Berechne das Zusatzgewicht aller neuen Gegenstände.
        # 3. Wenn self.gesamtgewicht + zusatz_gewicht > self.max_gewicht:
        #    Löse einen ValueError("Maximalgewicht überschritten!") aus.
        # 4. Hänge alle items an self._items an.
        # ==========================================================================
        pass

    def __len__(self) -> int:
        """
        Ermöglicht len(inventar) -> Gibt die Anzahl der Gegenstände zurück.
        """
        # ==========================================================================
        # TODO 7: __len__
        # ==========================================================================
        pass

    def __getitem__(self, key: Union[int, str]) -> Gegenstand:
        """
        Ermöglicht Index- und Namenszugriff:
        - inventar[0] -> Gibt den Gegenstand an Position 0 zurück (int-Index).
        - inventar["Heiltrank"] -> Sucht den ersten Gegenstand mit diesem Namen (case-insensitive).

        Exceptions:
            IndexError: Bei ungültigem Integer-Index.
            KeyError: Falls kein Gegenstand mit dem übergebenen String-Namen gefunden wurde.
            TypeError: Falls key weder int noch str ist.
        """
        # ==========================================================================
        # TODO 8: __getitem__ (Multi-Type Lookup: int und str)
        # 1. Wenn isinstance(key, int): gib self._items[key] zurück.
        # 2. Wenn isinstance(key, str): suche den ersten Gegenstand mit passendem Namen
        #    (Vergleich mit g.name.lower() == key.lower()). Wenn gefunden, zurückgeben.
        #    Wurde kein Item gefunden, löse KeyError aus.
        # 3. Andernfalls löse TypeError aus.
        # ==========================================================================
        pass

    def __setitem__(self, index: int, value: Gegenstand) -> None:
        """
        Ermöglicht Zuweisung per Index: inventar[0] = neuer_gegenstand.

        Exceptions:
            TypeError: Falls index kein int oder value kein Gegenstand ist.
            IndexError: Falls index außerhalb des gültigen Bereichs liegt.
            ValueError: Falls durch den Austausch das Maximalgewicht überschritten würde.
        """
        # ==========================================================================
        # TODO 9: __setitem__
        # 1. Prüfe Typen (index muss int sein, value muss Gegenstand sein, sonst TypeError).
        # 2. Prüfe Indexgrenzen: -len(self._items) <= index < len(self._items) (sonst IndexError).
        # 3. Berechne neues Gesamtgewicht: gesamtgewicht - altes_item.gewicht + value.gewicht.
        #    Wenn neues_gesamtgewicht > max_gewicht: löse ValueError aus.
        # 4. Ersetze das Element: self._items[index] = value.
        # ==========================================================================
        pass

    def __delitem__(self, key: Union[int, str]) -> None:
        """
        Ermöglicht das Löschen per del-Keyword:
        - del inventar[0] -> Löscht per Integer-Index.
        - del inventar["Heiltrank"] -> Löscht das erste gefundene Item mit diesem Namen.

        Exceptions:
            IndexError: Bei ungültigem int-Index.
            KeyError: Wenn String-Name nicht existiert.
            TypeError: Falls key weder int noch str ist.
        """
        # ==========================================================================
        # TODO 10: __delitem__
        # 1. Wenn int: del self._items[key].
        # 2. Wenn str: suche erstes Element mit passendem Namen (case-insensitive) und entferne es.
        #    Falls nicht vorhanden -> KeyError.
        # 3. Andernfalls -> TypeError.
        # ==========================================================================
        pass

    def __contains__(self, item: Union[Gegenstand, str]) -> bool:
        """
        Ermöglicht den `in`-Operator:
        - "Heiltrank" in inventar -> True/False (Name-Suche, case-insensitive)
        - gegenstand_objekt in inventar -> True/False (Objekt-Prüfung)
        """
        # ==========================================================================
        # TODO 11: __contains__
        # 1. Wenn str: prüfe, ob ein Gegenstand mit diesem Namen existiert (case-insensitive).
        # 2. Wenn Gegenstand: prüfe `item in self._items`.
        # 3. Andernfalls gebe False zurück.
        # ==========================================================================
        pass

    def __iter__(self) -> Iterator[Gegenstand]:
        """
        Ermöglicht Iteration: for item in inventar: ...
        """
        # ==========================================================================
        # TODO 12: __iter__
        # Gib einen Iterator über self._items zurück (z.B. iter(self._items)).
        # ==========================================================================
        pass

    def __repr__(self) -> str:
        """Entwickler-Darstellung."""
        return f"Inventar(max_gewicht={self.max_gewicht}, gegenstaende={self._items!r})"

    def __str__(self) -> str:
        """Benutzerfreundliche Zusammenfassung."""
        return f"Inventar ({len(self)} Gegenstände, {self.gesamtgewicht:.1f}/{self.max_gewicht:.1f} kg)"


# ==============================================================================
# TEIL 4: UNPACKING-HELPER-FUNKTION
# ==============================================================================

def packe_inventar(*gegenstaende: Gegenstand, max_gewicht: float = 20.0) -> Inventar:
    """
    Erstellt ein neues Inventar und packt alle übergebenen Gegenstände (*args) hinein.
    Demonstriert Argument-Unpacking und flexible Parameter.
    """
    # ==========================================================================
    # TODO 13: packe_inventar
    # 1. Erstelle ein Inventar mit `max_gewicht=max_gewicht`.
    # 2. Füge alle `gegenstaende` mit inv.hinzufuegen(*gegenstaende) hinzu.
    # 3. Gib das befüllte Inventar zurück.
    # ==========================================================================
    pass


# ==============================================================================
# INTERAKTIVER TERMINAL-TEST
# (python3 aufgabe.py)
# ==============================================================================
if __name__ == "__main__":
    print("🎒 Kapitel 15: Parameter & Eigene Container-Klassen\n" + "=" * 55)

    # 1. Test *args & Rabatt
    preise = [19.99, 49.99, 9.99, 29.50]
    summe_rabatt = berechne_gesamtsumme(*preise, rabatt_prozent=15.0)
    print(f"1. *args Summe mit 15% Rabatt: {summe_rabatt} €")

    # 2. Test **kwargs Profil
    held_daten = {"klasse": "Magier", "stufe": 12, "mana": 350, "element": "Feuer"}
    profil = erstelle_profil("Ignis", **held_daten)
    print(f"2. **kwargs Profil: {profil}")

    # 3. Test Container Inventar
    schwert = Gegenstand("Eisenschwert", 4.5, 120)
    schild = Gegenstand("Holzschild", 3.0, 45)
    trank = Gegenstand("Heiltrank", 0.5, 20)

    inv = Inventar(max_gewicht=15.0)
    try:
        inv.hinzufuegen(schwert, schild, trank)
        print(f"\n3. Inventar initialisiert: {inv}")
        print(f"   Anzahl Gegenstände (len): {len(inv)}")
        print(f"   Gesamtgewicht: {inv.gesamtgewicht} / {inv.max_gewicht} kg")
        print(f"   Erster Gegenstand [0]: {inv[0]}")
        print(f"   Suche nach Name ['Heiltrank']: {inv['Heiltrank']}")
        print(f"   Ist 'Holzschild' im Rucksack? {'Holzschild' in inv}")
        
        print("\n   Alle Gegenstände im Rucksack:")
        for item in inv:
            print(f"     - {item}")

        print("\n   Lösche Heiltrank...")
        del inv["Heiltrank"]
        print(f"   Neues Gesamtgewicht: {inv.gesamtgewicht} kg (Anzahl: {len(inv)})")

    except Exception as e:
        print(f"   ⏳ Noch nicht vollständig implementiert: {e}")
