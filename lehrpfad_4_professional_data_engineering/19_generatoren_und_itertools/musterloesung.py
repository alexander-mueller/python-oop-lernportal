"""
Kapitel 19: Generatoren, Iteratoren & itertools (Memory Efficiency & Streaming) 🌊⚡
==================================================================================
Musterlösung für speichereffiziente Datenverarbeitung, Generatoren und itertools.
"""

import sys
import itertools
from typing import Iterator, Iterable, Any, Union, List, Tuple


# ==============================================================================
# TEIL 1: GRUNDLAGEN VON ITERATOREN & GENERATOREN MIT YIELD
# ==============================================================================

def endlos_zaehler(start: int = 0, schritt: int = 1) -> Iterator[int]:
    """
    Ein unendlicher Generator, der Zahlen beginnend bei 'start' mit der
    Schrittweite 'schritt' generiert.
    """
    aktuell = int(start)
    schritt_wert = int(schritt)
    while True:
        yield aktuell
        aktuell += schritt_wert


def fibonacci_generator(anzahl: int) -> Iterator[int]:
    """
    Ein Generator, der die ersten 'anzahl' Fibonacci-Zahlen on-demand erzeugt.
    """
    if anzahl < 0:
        raise ValueError("Anzahl darf nicht negativ sein!")

    a, b = 0, 1
    for _ in range(anzahl):
        yield a
        a, b = b, a + b


# ==============================================================================
# TEIL 2: SPEICHERSCHONENDE FILTER & GENERATOR-EXPRESSIONS
# ==============================================================================

def filter_grosse_zahlen(zahlen_iterable: Iterable[Union[int, float]], schwellenwert: float) -> Iterator[Union[int, float]]:
    """
    Ein Generator-Filter, der nur Zahlen liefert, die strikt größer als
    der angegebene 'schwellenwert' sind (x > schwellenwert).
    """
    for x in zahlen_iterable:
        if x > schwellenwert:
            yield x


def erzeuge_quadrat_generator(n: int) -> Iterator[int]:
    """
    Erzeugt eine Generator-Expression für Quadratzahlen von 1 bis n (inklusive).
    """
    if n < 0:
        raise ValueError("n darf nicht negativ sein!")
    return (x ** 2 for x in range(1, n + 1))


# ==============================================================================
# TEIL 3: DAS ITERTOOLS-MODUL (CHAIN, PERMUTATIONS & CYCLE)
# ==============================================================================

def kette_listen(*listen: Iterable[Any]) -> List[Any]:
    """
    Verbindet beliebig viele Iterables (*args) mit 'itertools.chain' zu einer
    einzigen flachen Liste.
    """
    return list(itertools.chain(*listen))


def erzeuge_passwort_kombinationen(zeichen: str, laenge: int) -> List[str]:
    """
    Erzeugt alle möglichen Permutationen der angegebenen Zeichenkette mit der
    exakten Länge 'laenge' unter Verwendung von 'itertools.permutations'.
    """
    if laenge < 0 or laenge > len(zeichen):
        raise ValueError(f"Ungültige Länge {laenge} für Zeichenkette der Länge {len(zeichen)}!")

    return ["".join(p) for p in itertools.permutations(zeichen, laenge)]


def zyklische_elemente(elemente: List[Any], anzahl: int) -> List[Any]:
    """
    Nimmt eine Liste von Elementen und liefert die ersten 'anzahl' Elemente
    in zyklischer Reihenfolge mit 'itertools.cycle'.
    """
    if anzahl < 0:
        raise ValueError("Anzahl darf nicht negativ sein!")
    if anzahl == 0:
        return []
    if not elemente:
        raise ValueError("Elemente-Liste darf nicht leer sein bei anzahl > 0!")

    zyk = itertools.cycle(elemente)
    return [next(zyk) for _ in range(anzahl)]


# ==============================================================================
# DEMONSTRATION & SPEICHER-BENCHMARK
# ==============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("🌊 KAPITEL 19: MUSTERLÖSUNG – GENERATOREN & ITERTOOLS")
    print("=" * 70)

    # 1. Speichervergleich: Liste vs. Generator
    elemente_anzahl = 1_000_000
    print(f"\n📊 SPEICHERVERGLEICH FÜR {elemente_anzahl:,} ZAHLEN:")

    liste = [x for x in range(elemente_anzahl)]
    gen = (x for x in range(elemente_anzahl))

    speicher_liste = sys.getsizeof(liste) / (1024 * 1024)
    speicher_gen = sys.getsizeof(gen)

    print(f"  🔴 Liste (Badewanne):      {speicher_liste:.2f} MB RAM im Hauptspeicher!")
    print(f"  🟢 Generator (Wasserhahn): {speicher_gen} Bytes RAM (Faktor {int(speicher_liste * 1024 * 1024 / speicher_gen):,}x sparsamer!)")

    # 2. Endloszähler Test
    print("\n⏱️ Endloszähler (erste 5 Werte ab 100 in 10er Schritten):")
    zaehler = endlos_zaehler(100, 10)
    for _ in range(5):
        print(f"   -> {next(zaehler)}")

    # 3. Fibonacci Test
    print("\n🐰 Die ersten 10 Fibonacci-Zahlen:")
    print(f"   -> {list(fibonacci_generator(10))}")

    # 4. Passwort-Permutationen Test
    print("\n🔐 Passwort-Permutationen für 'abc' (Länge 2):")
    print(f"   -> {erzeuge_passwort_kombinationen('abc', 2)}")

    # 5. Zyklischer Taktgeber
    print("\n🚦 Ampel-Zyklus (7 Schritte):")
    print(f"   -> {zyklische_elemente(['Rot', 'Gelb', 'Gruen'], 7)}")

    print("\n" + "=" * 70)
    print("✅ Musterlösung erfolgreich ausgeführt!")
    print("=" * 70)
