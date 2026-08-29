"""
Kapitel G05: Schleifen & Wiederholungen – Musterlösung
=====================================================
Schulabgleich: 09.1 & 09.2
"""


def summe_bis(n: int) -> int:
    """Berechnet 1 + 2 + ... + n."""
    if n <= 0:
        return 0
    summe = 0
    for i in range(1, n + 1):
        summe += i
    return summe


def fakultaet(n: int) -> int:
    """Berechnet n! (Fakultät von n)."""
    if n < 0:
        raise ValueError("Fakultät ist für negative Zahlen nicht definiert")
    if n == 0:
        return 1
    produkt = 1
    for i in range(1, n + 1):
        produkt *= i
    return produkt


def zaehle_gerade_zahlen(start: int, ende: int) -> int:
    """Zählt alle geraden Zahlen im Bereich [start, ende]."""
    if start > ende:
        return 0
    zaehler = 0
    for zahl in range(start, ende + 1):
        if zahl % 2 == 0:
            zaehler += 1
    return zaehler


def ist_primzahl(n: int) -> bool:
    """Prüft, ob n eine Primzahl ist."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    # Prüfe ungerade Teiler bis zur Wurzel von n
    for teiler in range(3, int(n**0.5) + 1, 2):
        if n % teiler == 0:
            return False
    return True


def quorsumme(n: int) -> int:
    """Berechnet die Quersumme von n mittels einer while-Schleife."""
    rest = abs(n)
    summe = 0
    while rest > 0:
        letzte_ziffer = rest % 10
        summe += letzte_ziffer
        rest = rest // 10
    return summe


# Alias für alternative Schreibweise
quersumme = quorsumme


if __name__ == "__main__":
    print("Musterlösung G05 Demonstrationen:")
    print("summe_bis(5) =", summe_bis(5))
    print("fakultaet(5) =", fakultaet(5))
    print("zaehle_gerade_zahlen(1, 10) =", zaehle_gerade_zahlen(1, 10))
    print("ist_primzahl(17) =", ist_primzahl(17))
    print("quorsumme(482) =", quorsumme(482))
