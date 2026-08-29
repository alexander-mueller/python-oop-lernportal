"""
Kapitel 15: Parameter (*args, **kwargs) & Eigene Container-Klassen 🎒📦
======================================================================
Musterlösung für flexible Parameterlisten, Unpacking und magische
Container-Dunder-Methoden.
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
    """
    if not (0.0 <= rabatt_prozent <= 100.0):
        raise ValueError("Rabatt muss zwischen 0.0 und 100.0 Prozent liegen!")

    summe = sum(float(z) for z in zahlen)
    rabatt_faktor = 1.0 - (rabatt_prozent / 100.0)
    return round(summe * rabatt_faktor, 2)


def erstelle_profil(name: str, **details: Any) -> Dict[str, Any]:
    """
    Erstellt ein Profil-Dictionary mit dem Namen und beliebigen weiteren
    Schlüsselwort-Attributen (**kwargs).
    """
    profil: Dict[str, Any] = {"name": str(name)}
    profil.update(details)
    return profil


# ==============================================================================
# TEIL 2: DIE DATENKLASSE GEGENSTAND (ITEM)
# ==============================================================================

class Gegenstand:
    """
    Repräsentiert einen Gegenstand im Spielinventar.
    """

    def __init__(self, name: str, gewicht: float, wert: int = 0):
        if float(gewicht) < 0:
            raise ValueError("Gewicht darf nicht negativ sein!")
        if int(wert) < 0:
            raise ValueError("Wert darf nicht negativ sein!")

        self.name: str = str(name)
        self.gewicht: float = float(gewicht)
        self.wert: int = int(wert)

    def __repr__(self) -> str:
        return f"Gegenstand(name='{self.name}', gewicht={self.gewicht}, wert={self.wert})"

    def __str__(self) -> str:
        return f"{self.name} ({self.gewicht}kg, {self.wert}G)"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Gegenstand):
            return False
        return (
            self.name == other.name
            and math.isclose(self.gewicht, other.gewicht)
            and self.wert == other.wert
        )


# ==============================================================================
# TEIL 3: DIE EIGENE CONTAINER-KLASSE INVENTAR
# ==============================================================================

class Inventar:
    """
    Eine maßgeschneiderte Container-Klasse für ein Gaming-Rucksack-Inventar.
    Unterstützt Maximalgewicht, *args-Hinzufügen und alle Python-Container-Dunder!
    """

    def __init__(self, max_gewicht: float = 20.0, gegenstaende: Optional[List[Gegenstand]] = None):
        if float(max_gewicht) <= 0:
            raise ValueError("Maximalgewicht muss positiv sein!")

        self.max_gewicht: float = float(max_gewicht)
        self._items: List[Gegenstand] = []

        if gegenstaende:
            self.hinzufuegen(*gegenstaende)

    @property
    def gesamtgewicht(self) -> float:
        """
        Berechnet das aktuelle Gesamtgewicht aller enthaltenen Gegenstände,
        gerundet auf 2 Nachkommastellen.
        """
        return round(sum(g.gewicht for g in self._items), 2)

    @property
    def freie_kapazitaet(self) -> float:
        """
        Gibt das noch verfügbare Restgewicht bis zum Maximalgewicht zurück.
        """
        return round(self.max_gewicht - self.gesamtgewicht, 2)

    def hinzufuegen(self, *items: Gegenstand) -> None:
        """
        Fügt ein oder mehrere Gegenstände (*args) zum Inventar hinzu.
        """
        for item in items:
            if not isinstance(item, Gegenstand):
                raise TypeError(f"Erwartet 'Gegenstand', erhielt '{type(item).__name__}'")

        zusatz_gewicht = sum(item.gewicht for item in items)
        if self.gesamtgewicht + zusatz_gewicht > self.max_gewicht:
            raise ValueError(
                f"Maximalgewicht von {self.max_gewicht}kg überschritten! "
                f"(Aktuell: {self.gesamtgewicht}kg + Neu: {zusatz_gewicht:.2f}kg)"
            )

        self._items.extend(items)

    def __len__(self) -> int:
        """Ermöglicht len(inventar)."""
        return len(self._items)

    def __getitem__(self, key: Union[int, str]) -> Gegenstand:
        """
        Ermöglicht Index- und Namenszugriff:
        - inventar[0] -> Item an Position 0 (IndexError bei ungültigem Index).
        - inventar["Heiltrank"] -> Erstes Item mit diesem Namen (KeyError bei Nicht-Auffinden).
        """
        if isinstance(key, int):
            return self._items[key]
        elif isinstance(key, str):
            for g in self._items:
                if g.name.lower() == key.lower():
                    return g
            raise KeyError(f"Gegenstand '{key}' nicht im Inventar gefunden!")
        else:
            raise TypeError("Index muss int (Position) oder str (Name) sein!")

    def __setitem__(self, index: int, value: Gegenstand) -> None:
        """
        Ermöglicht Zuweisung per Index: inventar[0] = neuer_gegenstand.
        """
        if not isinstance(index, int):
            raise TypeError("Index muss int sein!")
        if not isinstance(value, Gegenstand):
            raise TypeError("Wert muss ein Gegenstand sein!")

        if index < -len(self._items) or index >= len(self._items):
            raise IndexError("Listenindex außerhalb des gültigen Bereichs!")

        altes_gewicht = self._items[index].gewicht
        neues_gesamtgewicht = self.gesamtgewicht - altes_gewicht + value.gewicht
        if neues_gesamtgewicht > self.max_gewicht:
            raise ValueError(
                f"Austausch überschreitet Maximalgewicht von {self.max_gewicht}kg!"
            )

        self._items[index] = value

    def __delitem__(self, key: Union[int, str]) -> None:
        """
        Ermöglicht das Löschen per del-Keyword:
        - del inventar[0] (per int-Index)
        - del inventar["Heiltrank"] (per str-Name)
        """
        if isinstance(key, int):
            del self._items[key]
        elif isinstance(key, str):
            for i, g in enumerate(self._items):
                if g.name.lower() == key.lower():
                    del self._items[i]
                    return
            raise KeyError(f"Gegenstand '{key}' nicht im Inventar gefunden!")
        else:
            raise TypeError("Schlüssel muss int oder str sein!")

    def __contains__(self, item: Union[Gegenstand, str]) -> bool:
        """
        Ermöglicht den in-Operator (Name oder Objekt).
        """
        if isinstance(item, str):
            return any(g.name.lower() == item.lower() for g in self._items)
        elif isinstance(item, Gegenstand):
            return item in self._items
        return False

    def __iter__(self) -> Iterator[Gegenstand]:
        """Ermöglicht for item in inventar: ..."""
        return iter(self._items)

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
    """
    inv = Inventar(max_gewicht=max_gewicht)
    inv.hinzufuegen(*gegenstaende)
    return inv


if __name__ == "__main__":
    print("🎒 Kapitel 15: Musterlösung erfolgreich ausgeführt!\n" + "=" * 55)
    preise = [19.99, 49.99, 9.99, 29.50]
    print(f"Summe mit 15% Rabatt: {berechne_gesamtsumme(*preise, rabatt_prozent=15.0)} €")
    profil = erstelle_profil("Ignis", klasse="Magier", level=12, element="Feuer")
    print(f"Profil: {profil}")
    
    schwert = Gegenstand("Eisenschwert", 4.5, 120)
    trank = Gegenstand("Heiltrank", 0.5, 20)
    inv = packe_inventar(schwert, trank, max_gewicht=10.0)
    print(f"Rucksack: {inv}")
    for item in inv:
        print(f"  - {item}")
