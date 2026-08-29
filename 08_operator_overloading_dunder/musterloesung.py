"""
Kapitel 08: Operator Overloading & Dunder-Methoden ➕
===================================================
Musterlösung: Vollständige Implementierung von Vektor2D und Wegstrecke.
"""

import math
from typing import Union, List, Optional


class Vektor2D:
    """
    Repräsentiert einen zweidimensionalen Vektor (x, y) in der Ebene.
    Unterstützt mathematische Operatoren (+, -, *), Vergleiche (==, <, <=),
    sowie __str__, __repr__ und __abs__.
    """

    def __init__(self, x: float, y: float):
        self.x: float = float(x)
        self.y: float = float(y)

    def __repr__(self) -> str:
        """Entwickler-Darstellung: Vektor2D(3.0, 4.0)"""
        return f"Vektor2D({self.x}, {self.y})"

    def __str__(self) -> str:
        """Benutzerfreundliche Darstellung: (3.0, 4.0)"""
        return f"({self.x}, {self.y})"

    def laenge(self) -> float:
        """Berechnet den Betrag (die euklidische Länge) des Vektors: sqrt(x² + y²)"""
        return math.sqrt(self.x**2 + self.y**2)

    def __abs__(self) -> float:
        """Ermöglicht abs(v) zur Berechnung der Vektorlänge."""
        return self.laenge()

    def __add__(self, other: "Vektor2D") -> "Vektor2D":
        """Vektoraddition: (x1 + x2, y1 + y2)"""
        if isinstance(other, Vektor2D):
            return Vektor2D(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other: "Vektor2D") -> "Vektor2D":
        """Vektorsubtraktion: (x1 - x2, y1 - y2)"""
        if isinstance(other, Vektor2D):
            return Vektor2D(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, other: Union[int, float, "Vektor2D"]) -> Union["Vektor2D", float]:
        """
        Multiplikation:
        - Mit einer Zahl (int/float): Skalarmultiplikation -> neuer Vektor2D(x*k, y*k)
        - Mit einem Vektor2D: Skalarprodukt (Dot Product) -> x1*x2 + y1*y2 (Zahl)
        """
        if isinstance(other, (int, float)):
            return Vektor2D(self.x * other, self.y * other)
        elif isinstance(other, Vektor2D):
            return self.x * other.x + self.y * other.y
        return NotImplemented

    def __rmul__(self, other: Union[int, float]) -> "Vektor2D":
        """Ermöglicht Zahl * Vektor (z.B. 3 * v), indem __mul__ aufgerufen wird."""
        if isinstance(other, (int, float)):
            return self.__mul__(other)
        return NotImplemented

    def __eq__(self, other: object) -> bool:
        """Prüft zwei Vektoren auf Gleichheit ihrer Komponenten."""
        if not isinstance(other, Vektor2D):
            return False
        return math.isclose(self.x, other.x, abs_tol=1e-9) and math.isclose(self.y, other.y, abs_tol=1e-9)

    def __lt__(self, other: "Vektor2D") -> bool:
        """Vergleicht zwei Vektoren anhand ihrer Länge (<)."""
        if isinstance(other, Vektor2D):
            return self.laenge() < other.laenge()
        return NotImplemented

    def __le__(self, other: "Vektor2D") -> bool:
        """Vergleicht zwei Vektoren anhand ihrer Länge (<=)."""
        if isinstance(other, Vektor2D):
            return self.laenge() <= other.laenge()
        return NotImplemented


class Wegstrecke:
    """
    Eine Sequenz von 2D-Wegpunkten, die Container-Dunder (__len__, __getitem__)
    nutzt und die Gesamtlänge der Strecke berechnet.
    """

    def __init__(self, punkte: Optional[List[Vektor2D]] = None):
        self.punkte: List[Vektor2D] = list(punkte) if punkte else []

    def punkt_hinzufuegen(self, punkt: Vektor2D) -> None:
        """Fügt einen neuen Wegpunkt hinzu."""
        self.punkte.append(punkt)

    def __len__(self) -> int:
        """Gibt die Anzahl der Wegpunkte zurück: len(strecke)"""
        return len(self.punkte)

    def __getitem__(self, index: int) -> Vektor2D:
        """Ermöglicht Indexzugriff per strecke[i]"""
        return self.punkte[index]

    def gesamtlaenge(self) -> float:
        """
        Berechnet die Gesamtdistanz entlang aller Wegpunkte.
        Nutzt Vektorsubtraktion und abs(), um Distanzen zwischen
        aufeinanderfolgenden Punkten zu summieren.
        """
        if len(self.punkte) < 2:
            return 0.0

        distanz = 0.0
        for i in range(len(self.punkte) - 1):
            segment = self.punkte[i + 1] - self.punkte[i]
            distanz += abs(segment)
        return distanz


# ==============================================================================
# Terminal-Demo zum direkten Ausführen
# ==============================================================================
if __name__ == "__main__":
    v1 = Vektor2D(3, 4)
    v2 = Vektor2D(1, 2)

    print(f"v1: {v1}")                       # (3.0, 4.0)
    print(f"repr(v1): {repr(v1)}")           # Vektor2D(3.0, 4.0)
    print(f"Länge |v1|: {abs(v1)}")          # 5.0
    print(f"v1 + v2 = {v1 + v2}")            # (4.0, 6.0)
    print(f"v1 - v2 = {v1 - v2}")            # (2.0, 2.0)
    print(f"v1 * 3 = {v1 * 3}")              # (9.0, 12.0)
    print(f"3 * v1 = {3 * v1}")              # (9.0, 12.0)
    print(f"Skalarprodukt v1 * v2: {v1 * v2}") # 3*1 + 4*2 = 11.0
    print(f"v1 == Vektor2D(3, 4): {v1 == Vektor2D(3, 4)}") # True
    print(f"v2 < v1: {v2 < v1}")             # True (Länge sqrt(5) < 5.0)

    # Wegstrecken-Test
    route = Wegstrecke([Vektor2D(0, 0), Vektor2D(3, 0), Vektor2D(3, 4)])
    print(f"Anzahl Punkte: {len(route)}")    # 3
    print(f"Erster Punkt: {route[0]}")       # (0.0, 0.0)
    print(f"Gesamtlänge Route: {route.gesamtlaenge()}") # 3 + 4 = 7.0
