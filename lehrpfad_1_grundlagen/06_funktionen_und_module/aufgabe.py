"""
Kapitel G06: Eigene Funktionen & Module – Aufgabenblatt
======================================================
Schulabgleich: 05.0 & 05.1

In diesem Kapitel lernst du:
- Eigene Funktionen mit Parametern und Standardwerten definieren (def)
- Rückgabewerte mit 'return' (und warum 'return' nicht 'print' ist!)
- Mehrere Rückgabewerte als Tupel zurückgeben (Tuple-Return)
- Lokale vs. Globale Gültigkeit von Variablen (Scope)
- Standardbibliotheks-Module importieren und nutzen (math, random)

Bearbeite die Aufgaben von TODO 1 bis TODO 4.
Teste deine Lösungen jederzeit im Terminal mit:
    python3 test_aufgabe.py
"""

# ==============================================================================
# Modul-Importe:
# Importiere hier die benötigten Standard-Module (math und random):
# ==============================================================================
import math
import random


# ==============================================================================
# TODO 1: Schreibe die Funktion "hypotenuse(a: float, b: float) -> float".
#
# Beschreibung:
# Berechnet die Länge der Hypotenuse c eines rechtwinkligen Dreiecks nach dem
# Satz des Pythagoras: c = sqrt(a² + b²).
#
# Regeln:
# - Verwende math.sqrt(...) für die Quadratwurzel und a**2 bzw. b**2 zum Quadrieren.
# - Wenn a < 0 oder b < 0 ist, soll ein ValueError ausgelöst werden:
#   raise ValueError("Seitenlängen dürfen nicht negativ sein")
# - Gib das Ergebnis mit 'return' als float zurück.
# ==============================================================================

def hypotenuse(a: float, b: float) -> float:
    """Berechnet die Hypotenuse c = sqrt(a^2 + b^2)."""
    # Schreibe hier deinen Code für TODO 1:
    pass


# ==============================================================================
# TODO 2: Schreibe die Funktion "zylinder_volumen(radius: float, hoehe: float) -> float".
#
# Beschreibung:
# Berechnet das Volumen eines Zylinders: V = pi * r² * h.
#
# Regeln:
# - Verwende die Kreiszahl Pi aus dem math-Modul: math.pi.
# - Wenn radius < 0 oder hoehe < 0 ist, soll ein ValueError ausgelöst werden:
#   raise ValueError("Radius und Höhe dürfen nicht negativ sein")
# - Gib das berechnete Volumen mit 'return' zurück.
# ==============================================================================

def zylinder_volumen(radius: float, hoehe: float) -> float:
    """Berechnet das Volumen eines Zylinders: V = pi * r^2 * h."""
    # Schreibe hier deinen Code für TODO 2:
    pass


# ==============================================================================
# TODO 3: Schreibe die Funktion "wuerfle_wuerfel(anzahl: int, seiten: int = 6) -> list[int]".
#
# Beschreibung:
# Simuliert das Würfeln von 'anzahl' Würfeln mit jeweils 'seiten' Seiten.
#
# Regeln:
# - Der Parameter 'seiten' hat den Standardwert 6 (Standard-Spielwürfel).
# - Verwende random.randint(1, seiten), um eine Zufallszahl zwischen 1 und 'seiten'
#   (inklusive) zu erzeugen.
# - Bei anzahl < 0 oder seiten < 1 soll ein ValueError ausgelöst werden:
#   raise ValueError("Ungültige Würfel-Parameter")
# - Bei anzahl == 0 soll eine leere Liste [] zurückgegeben werden.
# - Gib eine Liste mit allen gewürfelten Augenzahlen zurück.
# ==============================================================================

def wuerfle_wuerfel(anzahl: int, seiten: int = 6) -> list[int]:
    """Würfelt 'anzahl' Würfel mit je 'seiten' Seiten (Standard: 6-seitig)."""
    # Schreibe hier deinen Code für TODO 3:
    pass


# ==============================================================================
# TODO 4: Schreibe die Funktion "statistik(zahlen: list[float]) -> tuple[float, float, float]".
#
# Beschreibung:
# Berechnet das Minimum, das Maximum und den arithmetischen Mittelwert (Durchschnitt)
# einer Liste von Zahlen.
#
# Regeln:
# - Wenn die Liste leer ist (len(zahlen) == 0), soll ein ValueError ausgelöst werden:
#   raise ValueError("Die Liste darf nicht leer sein")
# - Berechne:
#   * min_wert = min(zahlen)
#   * max_wert = max(zahlen)
#   * mittelwert = sum(zahlen) / len(zahlen)
# - Gib alle drei Werte als Tupel zurück:
#   return (min_wert, max_wert, mittelwert)
# ==============================================================================

def statistik(zahlen: list[float]) -> tuple[float, float, float]:
    """Gibt (min_wert, max_wert, mittelwert) einer Zahlenliste zurück."""
    # Schreibe hier deinen Code für TODO 4:
    pass


# ==============================================================================
# Hauptprogramm zum manuellen Ausprobieren:
# (Führe diese Datei aus mit: python3 aufgabe.py)
# ==============================================================================
if __name__ == "__main__":
    print("=" * 55)
    print("🪄 KAPITEL G06: EIGENE FUNKTIONEN & MODULE")
    print("=" * 55)

    # 1. Pythagoras
    c = hypotenuse(3.0, 4.0)
    print(f"Hypotenuse für a=3, b=4: {c} (Erwartet: 5.0)")

    # 2. Zylindervolumen
    v = zylinder_volumen(3.0, 5.0)
    v_str = f"{v:.2f}" if v is not None else "None"
    print(f"Zylindervolumen (r=3, h=5): {v_str} (Erwartet: ~141.37)")

    # 3. Würfel werfen
    wuerfe_w6 = wuerfle_wuerfel(5)
    print(f"5x W6 gewürfelt: {wuerfe_w6}")
    wuerfe_w20 = wuerfle_wuerfel(3, seiten=20)
    print(f"3x W20 (D20) gewürfelt: {wuerfe_w20}")

    # 4. Statistik mit Tuple-Unpacking
    noten = [1.0, 2.3, 1.7, 3.0, 1.3]
    stats = statistik(noten)
    if stats is not None:
        bester, schlechtester, schnitt = stats
        print(f"Notenstatistik: Beste={bester}, Schlechteste={schlechtester}, Schnitt={schnitt:.2f}")
    else:
        print(f"Notenstatistik: None (Erwartet: (1.0, 3.0, 1.86))")

    print("=" * 55)
    print("💡 Führe 'python3 test_aufgabe.py' aus, um deine Lösungen zu prüfen!")
