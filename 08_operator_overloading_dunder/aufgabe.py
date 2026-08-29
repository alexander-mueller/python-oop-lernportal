"""
Kapitel 08: Operator Overloading & Dunder-Methoden ➕
===================================================
Aufgabe: Mache 2D-Vektoren rechen- und vergleichbar mit magischen Dunder-Methoden!

Implementiere die Klasse 'Vektor2D' und die Container-Klasse 'Wegstrecke'.
"""

import math
from typing import Union, List, Optional


class Vektor2D:
    """
    Repräsentiert einen 2D-Vektor (x, y).
    """

    # ==========================================================================
    # TODO 1: Konstruktor __init__(self, x: float, y: float)
    # Speichere self.x = float(x) und self.y = float(y).
    # ==========================================================================
    def __init__(self, x: float, y: float):
        pass

    # ==========================================================================
    # TODO 2: Darstellungsmethoden __repr__ und __str__
    # - __repr__(self) -> str: Gibt Entwickler-String "Vektor2D(x, y)" zurück (z.B. "Vektor2D(3.0, 4.0)")
    # - __str__(self) -> str:  Gibt benutzerfreundlichen String "(x, y)" zurück (z.B. "(3.0, 4.0)")
    # ==========================================================================
    def __repr__(self) -> str:
        pass

    def __str__(self) -> str:
        pass

    # ==========================================================================
    # TODO 3: Länge und Absolutbetrag
    # - laenge(self) -> float: Berechnet sqrt(x² + y²)
    # - __abs__(self) -> float: Gibt self.laenge() zurück, damit abs(v) funktioniert!
    # ==========================================================================
    def laenge(self) -> float:
        pass

    def __abs__(self) -> float:
        pass

    # ==========================================================================
    # TODO 4: Addition (__add__) und Subtraktion (__sub__)
    # - __add__(self, other: 'Vektor2D') -> 'Vektor2D':
    #   Addiert zwei Vektoren komponentenweise: (self.x + other.x, self.y + other.y)
    # - __sub__(self, other: 'Vektor2D') -> 'Vektor2D':
    #   Subtrahiert zwei Vektoren komponentenweise: (self.x - other.x, self.y - other.y)
    # Hinweis: Falls other kein Vektor2D ist, gebe 'NotImplemented' zurück.
    # ==========================================================================
    def __add__(self, other: "Vektor2D") -> "Vektor2D":
        pass

    def __sub__(self, other: "Vektor2D") -> "Vektor2D":
        pass

    # ==========================================================================
    # TODO 5: Multiplikation (__mul__) und Rechts-Multiplikation (__rmul__)
    # - __mul__(self, other):
    #   * Wenn other eine Zahl ist (int oder float):
    #     Skalarmultiplikation -> neuer Vektor2D(self.x * other, self.y * other)
    #   * Wenn other ein Vektor2D ist:
    #     Skalarprodukt (Dot Product) -> self.x * other.x + self.y * other.y (eine Zahl!)
    #   * Andernfalls -> NotImplemented
    # - __rmul__(self, other):
    #   * Ermöglicht Zahl * Vektor (z.B. 3 * v), indem self.__mul__(other) aufgerufen wird.
    # ==========================================================================
    def __mul__(self, other: Union[int, float, "Vektor2D"]) -> Union["Vektor2D", float]:
        pass

    def __rmul__(self, other: Union[int, float]) -> "Vektor2D":
        pass

    # ==========================================================================
    # TODO 6: Vergleiche (__eq__, __lt__, __le__)
    # - __eq__(self, other: object) -> bool:
    #   True, wenn other ein Vektor2D ist und self.x == other.x und self.y == other.y (Tipp: math.isclose)
    # - __lt__(self, other: 'Vektor2D') -> bool:
    #   Vergleicht anhand der Vektorlänge: self.laenge() < other.laenge()
    # - __le__(self, other: 'Vektor2D') -> bool:
    #   Vergleicht anhand der Vektorlänge: self.laenge() <= other.laenge()
    # ==========================================================================
    def __eq__(self, other: object) -> bool:
        pass

    def __lt__(self, other: "Vektor2D") -> bool:
        pass

    def __le__(self, other: "Vektor2D") -> bool:
        pass


class Wegstrecke:
    """
    Eine Sequenz von 2D-Wegpunkten (Vektor2D-Objekte).
    """

    # ==========================================================================
    # TODO 7: Wegstrecke __init__ und punkt_hinzufuegen
    # - __init__(self, punkte: list[Vektor2D] | None = None):
    #   Speichert self.punkte = list(punkte) if punkte else []
    # - punkt_hinzufuegen(self, punkt: Vektor2D) -> None:
    #   Fügt den Punkt zur internen Liste hinzu.
    # ==========================================================================
    def __init__(self, punkte: Optional[List[Vektor2D]] = None):
        pass

    def punkt_hinzufuegen(self, punkt: Vektor2D) -> None:
        pass

    # ==========================================================================
    # TODO 8: Container-Dunder (__len__ und __getitem__)
    # - __len__(self) -> int:
    #   Gibt die Anzahl der Wegpunkte zurück (len(self.punkte)).
    # - __getitem__(self, index: int) -> Vektor2D:
    #   Gibt den Punkt an Index 'index' zurück (self.punkte[index]).
    # ==========================================================================
    def __len__(self) -> int:
        pass

    def __getitem__(self, index: int) -> Vektor2D:
        pass

    # ==========================================================================
    # TODO 9: gesamtlaenge(self) -> float
    # Berechnet die Summe aller Teilstrecken zwischen aufeinanderfolgenden Punkten:
    # Distanz zwischen Punkt i und Punkt i+1 ist: abs(punkte[i+1] - punkte[i])
    # Wenn weniger als 2 Punkte vorhanden sind: gebe 0.0 zurück.
    # ==========================================================================
    def gesamtlaenge(self) -> float:
        pass


# ==============================================================================
# Kleiner Test zum Ausprobieren im Terminal:
# (python3 aufgabe.py)
# ==============================================================================
if __name__ == "__main__":
    v1 = Vektor2D(3, 4)
    v2 = Vektor2D(1, 2)

    print("--- Vektor Test ---")
    print(f"v1: {v1}")
    print(f"repr(v1): {repr(v1)}")
    if v1.laenge() is not None:
        print(f"Länge |v1|: {abs(v1)}")
    if (v1 + v2) is not None:
        print(f"v1 + v2 = {v1 + v2}")
        print(f"v1 - v2 = {v1 - v2}")
        print(f"v1 * 3 = {v1 * 3}")
        print(f"3 * v1 = {3 * v1}")
        print(f"Skalarprodukt v1 * v2 = {v1 * v2}")
        print(f"v1 == Vektor2D(3, 4): {v1 == Vektor2D(3, 4)}")
        print(f"v2 < v1: {v2 < v1}")

    print("\n--- Wegstrecke Test ---")
    route = Wegstrecke([Vektor2D(0, 0), Vektor2D(3, 0), Vektor2D(3, 4)])
    print(f"Anzahl Wegpunkte: {len(route) if len(route) is not None else 'noch nicht implementiert'}")
    try:
        print(f"Gesamtlänge Route: {route.gesamtlaenge()}")
    except Exception as e:
        print(f"Gesamtlänge Fehler: {e}")
