"""
Kapitel 07: Referenzen, Speicher & Stammbäume – Musterlösung
============================================================
"""

from typing import Optional, List


class Person:
    def __init__(self, name: str, geburtsjahr: int):
        self.name: str = name
        self.geburtsjahr: int = geburtsjahr
        self.mutter: Optional["Person"] = None
        self.vater: Optional["Person"] = None
        self.kinder: List["Person"] = []

    def mutter_setzen(self, mutter: "Person") -> None:
        self.mutter = mutter
        if self not in mutter.kinder:
            mutter.kinder.append(self)

    def vater_setzen(self, vater: "Person") -> None:
        self.vater = vater
        if self not in vater.kinder:
            vater.kinder.append(self)

    def geschwister(self) -> List["Person"]:
        ergebnis = []
        
        # Kinder der Mutter durchgehen
        if self.mutter:
            for kind in self.mutter.kinder:
                if kind is not self and kind not in ergebnis:
                    ergebnis.append(kind)
                    
        # Kinder des Vaters durchgehen
        if self.vater:
            for kind in self.vater.kinder:
                if kind is not self and kind not in ergebnis:
                    ergebnis.append(kind)
                    
        return ergebnis

    def grosseltern(self) -> List["Person"]:
        ergebnis = []
        
        # Großeltern mütterlicherseits
        if self.mutter:
            if self.mutter.mutter and self.mutter.mutter not in ergebnis:
                ergebnis.append(self.mutter.mutter)
            if self.mutter.vater and self.mutter.vater not in ergebnis:
                ergebnis.append(self.mutter.vater)
                
        # Großeltern väterlicherseits
        if self.vater:
            if self.vater.mutter and self.vater.mutter not in ergebnis:
                ergebnis.append(self.vater.mutter)
            if self.vater.vater and self.vater.vater not in ergebnis:
                ergebnis.append(self.vater.vater)
                
        return ergebnis

    def __str__(self) -> str:
        return f"{self.name} (*{self.geburtsjahr})"


if __name__ == "__main__":
    oma_anna = Person("Anna", 1955)
    opa_karl = Person("Karl", 1952)
    mama_susi = Person("Susi", 1980)
    papa_tom = Person("Tom", 1978)
    kind_mia = Person("Mia", 2008)
    kind_leo = Person("Leo", 2011)

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
