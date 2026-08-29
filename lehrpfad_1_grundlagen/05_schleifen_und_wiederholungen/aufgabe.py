"""
Kapitel G05: Schleifen & Wiederholungen – Aufgabenblatt
======================================================
Schulabgleich: 09.1 & 09.2

In diesem Kapitel lernst du, wie Wiederholungen in Python funktionieren:
- for-Schleifen mit range()
- while-Schleifen mit Bedingungen
- Schleifen-Akkumulatoren (Summen, Zähler, Produkte)
- Vorzeitiger Abbruch mit break und Weiterspringen mit continue

Bearbeite die Aufgaben von TODO 1 bis TODO 5.
Teste deine Lösungen jederzeit im Terminal mit:
    python3 test_aufgabe.py
"""


# ==============================================================================
# 🎯 TEILZIEL 1 (TODO 1): Schreibe die Funktion "summe_bis(n: int) -> int".
#
# Beschreibung:
# Berechnet die Summe aller ganzen Zahlen von 1 bis n (inklusive).
# Beispiel: summe_bis(5) = 1 + 2 + 3 + 4 + 5 = 15.
#
# Regeln:
# - Wenn n <= 0 ist, soll 0 zurückgegeben werden.
# - Nutze eine for-Schleife mit range(1, n + 1) und einen Akkumulator (summe = 0).
# ==============================================================================

def summe_bis(n: int) -> int:
    """Berechnet 1 + 2 + ... + n."""
    # 🎯 TEILZIEL 1: Implementiere die Logik Schritt für Schritt:
    # 💡 Tipp: Beachte Datentypen und das abschließende return!
    pass


# ==============================================================================
# 🎯 TEILZIEL 2 (TODO 2): Schreibe die Funktion "fakultaet(n: int) -> int".
#
# Beschreibung:
# Die Fakultät n! ist das Produkt aller ganzen Zahlen von 1 bis n.
# Beispiel: fakultaet(5) = 1 * 2 * 3 * 4 * 5 = 120.
#
# Sonderregeln:
# - Für n = 0 ist die Fakultät mathematisch definiert als 1 (fakultaet(0) == 1).
# - Für negative Zahlen (n < 0) ist die Fakultät nicht definiert.
#   Löse in diesem Fall einen ValueError aus:
#   raise ValueError("Fakultät ist für negative Zahlen nicht definiert")
# - Nutze eine for-Schleife mit range(1, n + 1) und einen Akkumulator (produkt = 1).
# ==============================================================================

def fakultaet(n: int) -> int:
    """Berechnet n! (Fakultät von n)."""
    # 🎯 TEILZIEL 2: Implementiere die Logik Schritt für Schritt:
    # 💡 Tipp: Beachte Datentypen und das abschließende return!
    pass


# ==============================================================================
# 🎯 TEILZIEL 3 (TODO 3): Schreibe die Funktion "zaehle_gerade_zahlen(start: int, ende: int) -> int".
#
# Beschreibung:
# Zählt, wie viele gerade Zahlen im Intervall von start bis ende (beide inklusive!)
# liegen.
#
# Beispiele:
# - zaehle_gerade_zahlen(1, 6) -> 3 (nämlich 2, 4, 6)
# - zaehle_gerade_zahlen(2, 4) -> 2 (nämlich 2, 4)
# - zaehle_gerade_zahlen(5, 5) -> 0
# - zaehle_gerade_zahlen(10, 2) -> 0 (wenn start > ende)
#
# Tipp:
# Eine Zahl x ist gerade, wenn x % 2 == 0 gilt.
# Nutze eine for-Schleife über range(start, ende + 1) und zähle mit zaehler += 1.
# ==============================================================================

def zaehle_gerade_zahlen(start: int, ende: int) -> int:
    """Zählt alle geraden Zahlen im Bereich [start, ende]."""
    # 🎯 TEILZIEL 3: Implementiere die Logik Schritt für Schritt:
    # 💡 Tipp: Beachte Datentypen und das abschließende return!
    pass


# ==============================================================================
# 🎯 TEILZIEL 4 (TODO 4): Schreibe die Funktion "ist_primzahl(n: int) -> bool".
#
# Beschreibung:
# Eine Primzahl ist eine ganze Zahl größer als 1, die nur durch 1 und sich selbst
# ohne Rest teilbar ist (z.B. 2, 3, 5, 7, 11, 13, ...).
#
# Regeln:
# - Zahlen kleiner oder gleich 1 (n <= 1) sind KEINE Primzahlen -> False.
# - Die Zahl 2 ist die kleinste Primzahl -> True.
# - Prüfe mit einer for-Schleife alle möglichen Teiler i von 2 bis n - 1
#   (oder bis int(n**0.5) + 1):
#   Wenn n durch i ohne Rest teilbar ist (n % i == 0), dann ist n KEINE Primzahl
#   -> brich sofort ab und gib False zurück!
# - Wird kein Teiler gefunden, gib am Ende True zurück.
# ==============================================================================

def ist_primzahl(n: int) -> bool:
    """Prüft, ob n eine Primzahl ist."""
    # 🎯 TEILZIEL 4: Implementiere die Logik Schritt für Schritt:
    # 💡 Tipp: Beachte Datentypen und das abschließende return!
    pass


# ==============================================================================
# 🎯 TEILZIEL 5 (TODO 5): Schreibe die Funktion "quorsumme(n: int) -> int".
#
# Beschreibung:
# Berechnet die Quersumme einer Zahl n mittels einer WHILE-Schleife.
# Die Quersumme ist die Summe aller einzelnen Ziffern der Zahl.
#
# Beispiele:
# - quorsumme(482) = 4 + 8 + 2 = 14
# - quorsumme(1234) = 1 + 2 + 3 + 4 = 10
# - quorsumme(0) = 0
# - quorsumme(-482) = 14 (behandle negative Zahlen mit abs(n))
#
# Wie holt man Ziffern mit while heraus? (Klassischer Algorithmus):
# 1. Zahl positiv machen: rest = abs(n), summe = 0
# 2. while rest > 0:
#        letzte_ziffer = rest % 10   # Modulo 10 liefert die letzte Ziffer
#        summe += letzte_ziffer
#        rest = rest // 10          # Ganzzahldivision schneidet letzte Ziffer ab
# 3. summe zurückgeben!
# ==============================================================================

def quorsumme(n: int) -> int:
    """Berechnet die Quersumme von n mittels einer while-Schleife."""
    # 🎯 TEILZIEL 5: Implementiere die Logik Schritt für Schritt:
    # 💡 Tipp: Beachte Datentypen und das abschließende return!
    pass


# Alias für deutsche Schreibweise
quersumme = quorsumme


# ==============================================================================
# Hauptprogramm zum manuellen Ausprobieren:
# (Führe diese Datei aus mit: python3 aufgabe.py)
# ==============================================================================
if __name__ == "__main__":
    print("=" * 50)
    print("🎡 KAPITEL G05: SCHLEIFEN & WIEDERHOLUNGEN")
    print("=" * 50)

    # 1. Summe
    s5 = summe_bis(5)
    print(f"Summe von 1 bis 5: {s5} (Erwartet: 15)")

    # 2. Fakultät
    f5 = fakultaet(5)
    print(f"Fakultät von 5 (5!): {f5} (Erwartet: 120)")

    # 3. Gerade Zahlen zählen
    g = zaehle_gerade_zahlen(1, 10)
    print(f"Gerade Zahlen von 1 bis 10: {g} (Erwartet: 5)")

    # 4. Primzahlprüfung
    p7 = ist_primzahl(7)
    p9 = ist_primzahl(9)
    print(f"Ist 7 eine Primzahl? {p7} (Erwartet: True)")
    print(f"Ist 9 eine Primzahl? {p9} (Erwartet: False)")

    # 5. Quersumme
    q = quorsumme(482)
    print(f"Quersumme von 482: {q} (Erwartet: 14)")
    print("=" * 50)
    print("💡 Führe 'python3 test_aufgabe.py' aus, um deine Lösungen zu prüfen!")
