"""
Grundlagen 01: Python als Taschenrechner – Aufgabenblatt
=========================================================

In diesem Kapitel lernst du, wie Python als leistungsfähiger Taschenrechner
funktioniert und wie du mathematische Operationen in Funktionen kapselst.

Bearbeite die Aufgaben Schritt für Schritt von TODO 1 bis TODO 7.
Wenn du fertig bist, überprüfe deine Lösung im Terminal mit:
    python3 test_aufgabe.py
"""

# ==============================================================================
# TODO 1: Schreibe die Funktion 'addieren(a, b)'
#
# Die Funktion soll zwei Zahlen (int oder float) entgegennehmen und deren
# mathematische Summe (a + b) zurückgeben.
#
# Beispiel:
#   addieren(5, 3)  -> 8
#   addieren(2.5, 1.5) -> 4.0
# ==============================================================================

def addieren(a: float, b: float) -> float:
    # Schreibe hier deinen Code für TODO 1:
    pass


# ==============================================================================
# TODO 2: Schreibe die Funktion 'subtrahieren(a, b)'
#
# Die Funktion soll die Differenz von a und b (a - b) berechnen und zurückgeben.
#
# Beispiel:
#   subtrahieren(10, 4) -> 6
#   subtrahieren(3, 5)  -> -2
# ==============================================================================

def subtrahieren(a: float, b: float) -> float:
    # Schreibe hier deinen Code für TODO 2:
    pass


# ==============================================================================
# TODO 3: Schreibe die Funktion 'multiplizieren(a, b)'
#
# Die Funktion soll das Produkt von a und b (a * b) berechnen und zurückgeben.
#
# Beispiel:
#   multiplizieren(6, 7)  -> 42
#   multiplizieren(4, 0.5) -> 2.0
# ==============================================================================

def multiplizieren(a: float, b: float) -> float:
    # Schreibe hier deinen Code für TODO 3:
    pass


# ==============================================================================
# TODO 4: Schreibe die Funktion 'dividieren(a, b)'
#
# Die Funktion soll den Quotienten von a und b (a / b) berechnen und zurückgeben.
# Hinweis: Die Division '/' in Python liefert immer eine Kommazahl (float).
#
# Beispiel:
#   dividieren(10, 2) -> 5.0
#   dividieren(7, 2)  -> 3.5
# ==============================================================================

def dividieren(a: float, b: float) -> float:
    # Schreibe hier deinen Code für TODO 4:
    pass


# ==============================================================================
# TODO 5: Schreibe die Funktion 'ganzzahl_rest(a, b)'
#
# Die Funktion soll zwei ganze Zahlen a und b annehmen und ein Tupel mit zwei
# Werten zurückgeben: (quotient, rest)
#   1. Der ganzzahlige Quotient (mit Ganzzahldivision '//')
#   2. Der verbleibende Rest (mit Modulo-Operator '%')
#
# Beispiel:
#   ganzzahl_rest(17, 5) -> (3, 2)   # 17 // 5 ist 3, Rest 17 % 5 ist 2
#   ganzzahl_rest(20, 4) -> (5, 0)   # 20 // 4 ist 5, Rest 20 % 4 ist 0
# ==============================================================================

def ganzzahl_rest(a: int, b: int) -> tuple:
    # Schreibe hier deinen Code für TODO 5:
    pass


# ==============================================================================
# TODO 6: Schreibe die Funktion 'potenz(basis, exponent)'
#
# Die Funktion soll 'basis' hoch 'exponent' berechnen (mit dem Operator '**').
#
# Beispiel:
#   potenz(2, 3) -> 8        # 2 * 2 * 2 = 8
#   potenz(5, 2) -> 25       # 5 * 5 = 25
#   potenz(10, 0) -> 1
# ==============================================================================

def potenz(basis: float, exponent: float) -> float:
    # Schreibe hier deinen Code für TODO 6:
    pass


# ==============================================================================
# TODO 7: Schreibe die Funktion 'kreis_flaeche(radius)'
#
# Berechne die Fläche eines Kreises mit der Formel:
#   flaeche = pi * r^2
# Verwende für Pi den Näherungswert 3.14159.
# Rechne: 3.14159 * (radius ** 2)
#
# Beispiel:
#   kreis_flaeche(1) -> 3.14159
#   kreis_flaeche(2) -> 12.56636  # (3.14159 * 4)
# ==============================================================================

def kreis_flaeche(radius: float) -> float:
    # Schreibe hier deinen Code für TODO 7:
    pass


# ==============================================================================
# Hauptprogramm zum Ausprobieren:
# (Führe diese Datei direkt aus mit: python3 aufgabe.py)
# ==============================================================================
if __name__ == "__main__":
    print("=" * 50)
    print("🧮 PYTHON ALS TASCHENRECHNER – TEST-AUSGABE")
    print("=" * 50)

    print("Addition (12 + 8):", addieren(12, 8))
    print("Subtraktion (20 - 7):", subtrahieren(20, 7))
    print("Multiplikation (6 * 7):", multiplizieren(6, 7))
    print("Division (15 / 2):", dividieren(15, 2))
    print("Ganzzahl & Rest (17 durch 5):", ganzzahl_rest(17, 5))
    print("Potenz (2 hoch 8):", potenz(2, 8))
    print("Kreisfläche (Radius 5):", kreis_flaeche(5))

    print("\n💡 Führe 'python3 test_aufgabe.py' aus, um deine Lösungen zu prüfen!")
