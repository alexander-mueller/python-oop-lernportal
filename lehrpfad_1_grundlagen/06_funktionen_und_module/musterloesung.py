"""
Kapitel G06: Eigene Funktionen & Module – Musterlösung
=====================================================
Schulabgleich: 05.0 & 05.1
"""

import math
import random


def hypotenuse(a: float, b: float) -> float:
    """Berechnet die Hypotenuse c = sqrt(a^2 + b^2)."""
    if a < 0 or b < 0:
        raise ValueError("Seitenlängen dürfen nicht negativ sein")
    return math.sqrt(a**2 + b**2)


def zylinder_volumen(radius: float, hoehe: float) -> float:
    """Berechnet das Volumen eines Zylinders: V = pi * r^2 * h."""
    if radius < 0 or hoehe < 0:
        raise ValueError("Radius und Höhe dürfen nicht negativ sein")
    return math.pi * (radius**2) * hoehe


def wuerfle_wuerfel(anzahl: int, seiten: int = 6) -> list[int]:
    """Würfelt 'anzahl' Würfel mit je 'seiten' Seiten (Standard: 6-seitig)."""
    if anzahl < 0 or seiten < 1:
        raise ValueError("Ungültige Würfel-Parameter")
    ergebnisse = []
    for _ in range(anzahl):
        augen = random.randint(1, seiten)
        ergebnisse.append(augen)
    return ergebnisse


def statistik(zahlen: list[float]) -> tuple[float, float, float]:
    """Gibt (min_wert, max_wert, mittelwert) einer Zahlenliste zurück."""
    if not zahlen:
        raise ValueError("Die Liste darf nicht leer sein")
    min_wert = min(zahlen)
    max_wert = max(zahlen)
    mittelwert = sum(zahlen) / len(zahlen)
    return min_wert, max_wert, mittelwert


if __name__ == "__main__":
    print("Musterlösung G06 Demonstrationen:")
    print("hypotenuse(3, 4) =", hypotenuse(3.0, 4.0))
    print("zylinder_volumen(3, 5) =", zylinder_volumen(3.0, 5.0))
    print("wuerfle_wuerfel(5) =", wuerfle_wuerfel(5))
    print("statistik([10, 20, 30]) =", statistik([10.0, 20.0, 30.0]))
