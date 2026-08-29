"""
Kapitel 19: Generatoren, Iteratoren & itertools (Memory Efficiency & Streaming) 🌊⚡
==================================================================================
Lerne speichereffiziente Datenverarbeitung in Python:
1. Iterables vs. Iterators (iter(), next(), StopIteration)
2. Eigene Generatoren mit 'yield' (Werte on-demand generieren, 0 RAM-Verschwendung)
3. Generator-Expressions (x**2 for x in riesige_daten)
4. Das itertools-Modul (chain, cycle, count, combinations, permutations)

Didaktische Analogie:
- "Gefüllte Badewanne" (Listen): Alle Daten liegen gleichzeitig im RAM.
- "Wasserhahn" (Generatoren): Daten fließen Tropfen für Tropfen, genau dann wenn sie gebraucht werden.
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

    Parameter:
        start (int): Die Startzahl (Standard: 0).
        schritt (int): Die Schrittweite (Standard: 1).

    Erzeugt (yield):
        int: Die nächste Zahl in der unendlichen Sequenz.

    Beispiele:
        z = endlos_zaehler(10, 2)
        next(z) -> 10
        next(z) -> 12
        next(z) -> 14
    """
    # ==========================================================================
    # 🎯 TEILZIEL 1 (TODO 1): Implementiere endlos_zaehler
    # 1. Initialisiere eine Variable 'aktuell' mit dem Wert 'start'.
    # 2. Nutze eine unendliche Schleife (while True:).
    # 3. Gib 'aktuell' mit 'yield' an den Aufrufer zurück.
    # 4. Erhöhe 'aktuell' um 'schritt'.
    # ==========================================================================
    pass


def fibonacci_generator(anzahl: int) -> Iterator[int]:
    """
    Ein Generator, der die ersten 'anzahl' Fibonacci-Zahlen on-demand erzeugt.
    Die Fibonacci-Folge beginnt mit: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

    Parameter:
        anzahl (int): Wie viele Fibonacci-Zahlen erzeugt werden sollen (>= 0).

    Erzeugt (yield):
        int: Die jeweils nächste Fibonacci-Zahl.

    Exceptions:
        ValueError: Falls 'anzahl' negativ (< 0) ist.

    Beispiele:
        list(fibonacci_generator(5)) -> [0, 1, 1, 2, 3]
        list(fibonacci_generator(0)) -> []
    """
    # ==========================================================================
    # 🎯 TEILZIEL 2 (TODO 2): Implementiere fibonacci_generator
    # 1. Validiere 'anzahl': Wenn anzahl < 0, löse ValueError aus.
    # 2. Setze die Startwerte a = 0, b = 1.
    # 3. Wiederhole in einer Schleife 'anzahl'-mal:
    #    - Gib 'a' mit 'yield' zurück.
    #    - Aktualisiere die Werte mit Tupel-Zuweisung: a, b = b, a + b
    # ==========================================================================
    pass


# ==============================================================================
# TEIL 2: SPEICHERSCHONENDE FILTER & GENERATOR-EXPRESSIONS
# ==============================================================================

def filter_grosse_zahlen(zahlen_iterable: Iterable[Union[int, float]], schwellenwert: float) -> Iterator[Union[int, float]]:
    """
    Ein Generator-Filter, der nur Zahlen liefert, die strikt größer als
    der angegebene 'schwellenwert' sind (x > schwellenwert).
    
    Wichtig: Es darf KEINE Zwischenliste im Speicher aufgebaut werden!
    Die Werte müssen einzeln gestreamt werden.

    Parameter:
        zahlen_iterable (Iterable): Eine beliebige Sequenz oder ein Generator von Zahlen.
        schwellenwert (float): Der Grenzwert.

    Erzeugt (yield):
        Union[int, float]: Jede Zahl aus zahlen_iterable, die > schwellenwert ist.

    Beispiele:
        daten = [10, 5, 20, 3, 50]
        list(filter_grosse_zahlen(daten, 15)) -> [20, 50]
    """
    # ==========================================================================
    # 🎯 TEILZIEL 3 (TODO 3): Implementiere filter_grosse_zahlen
    # 1. Iteriere mit einer for-Schleife über jedes Element in 'zahlen_iterable'.
    # 2. Prüfe, ob das Element > schwellenwert ist.
    # 3. Wenn ja, gib es mit 'yield' weiter.
    # ==========================================================================
    pass


def erzeuge_quadrat_generator(n: int) -> Iterator[int]:
    """
    Erzeugt eine Generator-Expression für Quadratzahlen von 1 bis n (inklusive).
    
    Parameter:
        n (int): Die Obergrenze (>= 0).

    Rückgabe:
        Iterator[int]: Ein Generator-Objekt (x**2 for x in ...), keine Liste!

    Exceptions:
        ValueError: Falls n < 0 ist.

    Beispiele:
        gen = erzeuge_quadrat_generator(4)
        list(gen) -> [1, 4, 9, 16]
    """
    # ==========================================================================
    # 🎯 TEILZIEL 4 (TODO 4): Implementiere erzeuge_quadrat_generator
    # 1. Wenn n < 0, löse einen ValueError aus.
    # 2. Gib direkt eine Generator-Expression zurück: (x**2 for x in range(1, n + 1))
    # ==========================================================================
    pass


# ==============================================================================
# TEIL 3: DAS ITERTOOLS-MODUL (CHAIN, PERMUTATIONS & CYCLE)
# ==============================================================================

def kette_listen(*listen: Iterable[Any]) -> List[Any]:
    """
    Verbindet beliebig viele Iterables (*args) mit 'itertools.chain' zu einer
    einzigen flachen Liste.

    Parameter:
        *listen (Iterable[Any]): Beliebig viele Iterables (Listen, Tupel, Generatoren).

    Rückgabe:
        List[Any]: Eine zusammenhängende Liste aller Elemente.

    Beispiele:
        kette_listen([1, 2], [3, 4], [5]) -> [1, 2, 3, 4, 5]
        kette_listen([], [10]) -> [10]
    """
    # ==========================================================================
    # 🎯 TEILZIEL 5 (TODO 5): Implementiere kette_listen mit itertools.chain
    # 1. Nutze itertools.chain(*listen) oder itertools.chain.from_iterable(listen).
    # 2. Wandle das Ergebnis in eine normale Python-Liste um (list(...)) und gib sie zurück.
    # ==========================================================================
    pass


def erzeuge_passwort_kombinationen(zeichen: str, laenge: int) -> List[str]:
    """
    Erzeugt alle möglichen Permutationen der angegebenen Zeichenkette mit der
    exakten Länge 'laenge' unter Verwendung von 'itertools.permutations'.

    Parameter:
        zeichen (str): Die verfügbaren Zeichen als String (z.B. "abc").
        laenge (int): Die Länge der gesuchten Kombinationen.

    Rückgabe:
        List[str]: Eine Liste von Strings mit allen Permutationen.

    Exceptions:
        ValueError: Falls laenge < 0 oder laenge > len(zeichen) ist.

    Beispiele:
        erzeuge_passwort_kombinationen("abc", 2) -> ['ab', 'ac', 'ba', 'bc', 'ca', 'cb']
        erzeuge_passwort_kombinationen("ab", 1)  -> ['a', 'b']
    """
    # ==========================================================================
    # 🎯 TEILZIEL 6 (TODO 6): Implementiere erzeuge_passwort_kombinationen
    # 1. Validiere: Wenn laenge < 0 oder laenge > len(zeichen), löse ValueError aus.
    # 2. Verwende itertools.permutations(zeichen, laenge).
    # 3. Führe jedes generierte Tupel von Zeichen mit "".join(...) zu einem String zusammen.
    # 4. Gib alle kombinierten Strings als Liste zurück.
    # ==========================================================================
    pass


def zyklische_elemente(elemente: List[Any], anzahl: int) -> List[Any]:
    """
    Nimmt eine Liste von Elementen und liefert die ersten 'anzahl' Elemente
    in zyklischer Reihenfolge mit 'itertools.cycle'.

    Parameter:
        elemente (List[Any]): Die Ausgangsliste (darf nicht leer sein, falls anzahl > 0).
        anzahl (int): Wie viele Elemente zyklisch entnommen werden sollen.

    Rückgabe:
        List[Any]: Liste mit 'anzahl' Elementen.

    Exceptions:
        ValueError: Falls anzahl < 0 ist oder falls elemente leer ist bei anzahl > 0.

    Beispiele:
        zyklische_elemente(["Rot", "Gruen", "Blau"], 7)
        -> ["Rot", "Gruen", "Blau", "Rot", "Gruen", "Blau", "Rot"]
    """
    # ==========================================================================
    # 🎯 TEILZIEL 7 (TODO 7): Implementiere zyklische_elemente
    # 1. Validiere anzahl >= 0 (sonst ValueError).
    # 2. Wenn anzahl == 0, gib eine leere Liste [] zurück.
    # 3. Wenn elemente leer ist (und anzahl > 0), löse ValueError aus.
    # 4. Erstelle einen zyklischen Iterator mit zyk = itertools.cycle(elemente).
    # 5. Hole mit next(zyk) genau 'anzahl' Elemente ab und sammle sie in einer Liste.
    # ==========================================================================
    pass


# ==============================================================================
# DEMONSTRATION & SPEICHER-BENCHMARK
# ==============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("🌊 KAPITEL 19: GENERATOREN & ITERTOOLS (MEMORY EFFICIENCY)")
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
    if zaehler:
        for _ in range(5):
            print(f"   -> {next(zaehler)}")

    # 3. Fibonacci Test
    print("\n🐰 Die ersten 10 Fibonacci-Zahlen:")
    fibs = fibonacci_generator(10)
    if fibs:
        print(f"   -> {list(fibs)}")

    # 4. Passwort-Permutationen Test
    print("\n🔐 Passwort-Permutationen für 'abc' (Länge 2):")
    perms = erzeuge_passwort_kombinationen("abc", 2)
    print(f"   -> {perms}")

    # 5. Zyklischer Taktgeber
    print("\n🚦 Ampel-Zyklus (7 Schritte):")
    ampel = zyklische_elemente(["Rot", "Gelb", "Gruen"], 7)
    print(f"   -> {ampel}")

    print("\n" + "=" * 70)
    print("💡 Starte die Tests mit: python3 test_aufgabe.py")
    print("=" * 70)
