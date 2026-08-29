"""
Kapitel 07: Referenzen, Speicher & Stammbäume 🧠🌳
=================================================
Aufgabe: Erstelle eine Stammbaum-Klasse 'Person'.
Jede Person kann Verweise (Referenzen) auf Mutter, Vater und Kinder enthalten.
"""

from typing import Optional, List


class Person:
    # ==========================================================================
    # 🎯 TEILZIEL 1 (TODO 1): Konstruktor __init__
    # Parameter: name (str), geburtsjahr (int)
    # Attribute:
    #   - self.name: str
    #   - self.geburtsjahr: int
    #   - self.mutter: Person | None  (Startwert: None)
    #   - self.vater: Person | None   (Startwert: None)
    #   - self.kinder: list[Person]   (Startwert: leere Liste [])
    # ==========================================================================
    def __init__(self, name: str, geburtsjahr: int):
        pass

    # ==========================================================================
    # 🎯 TEILZIEL 2 (TODO 2): Methode mutter_setzen(self, mutter: 'Person') -> None
    # 1. Setze self.mutter = mutter
    # 2. Füge self zur Liste mutter.kinder hinzu (falls self noch nicht drin ist)
    # ==========================================================================
    def mutter_setzen(self, mutter: "Person") -> None:
        pass

    # ==========================================================================
    # 🎯 TEILZIEL 3 (TODO 3): Methode vater_setzen(self, vater: 'Person') -> None
    # 1. Setze self.vater = vater
    # 2. Füge self zur Liste vater.kinder hinzu (falls self noch nicht drin ist)
    # ==========================================================================
    def vater_setzen(self, vater: "Person") -> None:
        pass

    # ==========================================================================
    # 🎯 TEILZIEL 4 (TODO 4): Methode geschwister(self) -> list['Person']
    # Gibt eine Liste aller Personen zurück, die dieselbe Mutter ODER denselben
    # Vater haben wie self.
    # WICHTIG:
    #   - self darf NICHT in der eigenen Geschwisterliste sein!
    #   - Keine Person darf doppelt in der Rückgabeliste sein.
    # ==========================================================================
    def geschwister(self) -> List["Person"]:
        pass

    # ==========================================================================
    # 🎯 TEILZIEL 5 (TODO 5): Methode grosseltern(self) -> list['Person']
    # Gibt eine Liste aller bekannten Großeltern zurück:
    # (Mutter der Mutter, Vater der Mutter, Mutter des Vaters, Vater des Vaters)
    # Nur Großeltern hinzufügen, die nicht None sind!
    # ==========================================================================
    def grosseltern(self) -> List["Person"]:
        pass

    # ==========================================================================
    # 🎯 TEILZIEL 6 (TODO 6): Dunder-Methode __str__(self) -> str
    # Gibt einen String im Format: "Name (*Geburtsjahr)" zurück.
    # Beispiel: "Mia (*2008)"
    # ==========================================================================
    def __str__(self) -> str:
        pass


# ==============================================================================
# Kleiner Test zum Ausprobieren im Terminal:
# (python3 aufgabe.py)
# ==============================================================================
if __name__ == "__main__":
    oma_anna = Person("Anna", 1955)
    opa_karl = Person("Karl", 1952)
    mama_susi = Person("Susi", 1980)
    papa_tom = Person("Tom", 1978)
    kind_mia = Person("Mia", 2008)
    kind_leo = Person("Leo", 2011)

    # Verknüpfungen herstellen
    mama_susi.mutter_setzen(oma_anna)
    mama_susi.vater_setzen(opa_karl)
    kind_mia.mutter_setzen(mama_susi)
    kind_mia.vater_setzen(papa_tom)
    kind_leo.mutter_setzen(mama_susi)
    kind_leo.vater_setzen(papa_tom)

    print("Kind:", kind_mia)
    print("Mamas Kinder:", [str(k) for k in mama_susi.kinder])
    print("Mias Geschwister:", [str(g) for g in kind_mia.geschwister()])
    print("Mias Großeltern:", [str(ge) for ge in kind_mia.grosseltern()])
