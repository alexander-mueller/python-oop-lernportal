"""
Grundlagen 01: Python als Taschenrechner – Musterlösung
========================================================

Vollständige Referenzlösung für alle Rechenoperationen.
"""

def addieren(a: float, b: float) -> float:
    """Berechnet die Summe von a und b."""
    return a + b


def subtrahieren(a: float, b: float) -> float:
    """Berechnet die Differenz a - b."""
    return a - b


def multiplizieren(a: float, b: float) -> float:
    """Berechnet das Produkt von a und b."""
    return a * b


def dividieren(a: float, b: float) -> float:
    """Berechnet den Quotienten a / b als float."""
    return a / b


def ganzzahl_rest(a: int, b: int) -> tuple:
    """Gibt ein Tupel (ganzzahliger_quotient, rest) zurück."""
    return (a // b, a % b)


def potenz(basis: float, exponent: float) -> float:
    """Berechnet basis hoch exponent."""
    return basis ** exponent


def kreis_flaeche(radius: float) -> float:
    """Berechnet die Kreisfläche für den gegebenen Radius (pi = 3.14159)."""
    return 3.14159 * (radius ** 2)


if __name__ == "__main__":
    print("=" * 50)
    print("🧮 MUSTERLÖSUNG: G01 TASCHENRECHNER")
    print("=" * 50)
    print("addieren(12, 8)          =", addieren(12, 8))
    print("subtrahieren(20, 7)      =", subtrahieren(20, 7))
    print("multiplizieren(6, 7)     =", multiplizieren(6, 7))
    print("dividieren(15, 2)        =", dividieren(15, 2))
    print("ganzzahl_rest(17, 5)     =", ganzzahl_rest(17, 5))
    print("potenz(2, 8)             =", potenz(2, 8))
    print("kreis_flaeche(5)         =", kreis_flaeche(5))
