"""
Kapitel 09: Eigene Unit Tests schreiben & TDD 🧪
================================================
Aufgabe: Schreibe deine eigenen Unit Tests mit dem 'unittest'-Modul!

Die Klassen 'Taschenrechner' und 'Bankkonto' sind bereits fertig programmiert.
Deine Aufgabe ist es, die Testklassen 'TestTaschenrechner' und 'TestBankkonto'
zu vervollständigen, sodass alle Funktionalitäten und Randfälle gründlich geprüft werden.
"""

import math
import unittest
from typing import List


# ==============================================================================
# Vorgegebene Klassen (nicht verändern, sondern testen!)
# ==============================================================================

class Taschenrechner:
    """Einfacher Taschenrechner für mathematische Grundoperationen."""

    def __init__(self):
        self.speicher: float = 0.0

    def add(self, a: float, b: float) -> float:
        return a + b

    def sub(self, a: float, b: float) -> float:
        return a - b

    def mul(self, a: float, b: float) -> float:
        return a * b

    def div(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Division durch Null ist nicht erlaubt!")
        return a / b

    def wurzel(self, a: float) -> float:
        if a < 0:
            raise ValueError("Wurzel aus negativen Zahlen ist im Reellen nicht definiert!")
        return math.sqrt(a)

    def speicher_plus(self, wert: float) -> None:
        self.speicher += wert

    def speicher_loeschen(self) -> None:
        self.speicher = 0.0


class Bankkonto:
    """Modelliert ein Bankkonto mit Ein-, Auszahlungen und Überweisungen."""

    def __init__(self, inhaber: str, kontostand: float = 0.0):
        self.inhaber: str = inhaber
        self.kontostand: float = float(kontostand)
        self.transaktionen: List[float] = [float(kontostand)]

    def einzahlen(self, betrag: float) -> None:
        if betrag <= 0:
            raise ValueError("Einzahlungsbetrag muss größer als 0 sein!")
        self.kontostand += betrag
        self.transaktionen.append(betrag)

    def abheben(self, betrag: float) -> None:
        if betrag <= 0:
            raise ValueError("Auszahlungsbetrag muss größer als 0 sein!")
        if betrag > self.kontostand:
            raise ValueError("Nicht genügend Guthaben auf dem Konto!")
        self.kontostand -= betrag
        self.transaktionen.append(-betrag)

    def ueberweisen(self, ziel_konto: "Bankkonto", betrag: float) -> None:
        self.abheben(betrag)
        ziel_konto.einzahlen(betrag)


# ==============================================================================
# HIER BEGINNT DEINE AUFGABE: Eigene Unit Tests schreiben!
# ==============================================================================

class TestTaschenrechner(unittest.TestCase):

    # ==========================================================================
    # TODO 1: setUp(self)
    # Erstelle vor jedem Test eine frische Rechner-Instanz: self.calc = Taschenrechner()
    # ==========================================================================
    def setUp(self):
        pass

    # ==========================================================================
    # TODO 2: test_01_grundrechenarten(self)
    # Teste mit self.assertEqual:
    # - self.calc.add(2, 3) soll 5 sein
    # - self.calc.sub(10, 4) soll 6 sein
    # - self.calc.mul(3, 7) soll 21 sein
    # ==========================================================================
    def test_01_grundrechenarten(self):
        pass

    # ==========================================================================
    # TODO 3: test_02_division_und_kommazahlen(self)
    # - Teste self.calc.div(10, 2) mit self.assertEqual (soll 5.0 sein)
    # - Teste self.calc.div(10, 3) mit self.assertAlmostEqual(..., places=2) (ca. 3.33)
    # ==========================================================================
    def test_02_division_und_kommazahlen(self):
        pass

    # ==========================================================================
    # TODO 4: test_03_division_durch_null_exception(self)
    # Teste mit 'with self.assertRaises(ZeroDivisionError):'
    # dass self.calc.div(10, 0) den Fehler auslöst!
    # ==========================================================================
    def test_03_division_durch_null_exception(self):
        pass

    # ==========================================================================
    # TODO 5: test_04_wurzel_negativ_exception(self)
    # - Teste self.calc.wurzel(16) soll 4.0 sein (assertEqual oder assertAlmostEqual)
    # - Teste mit 'with self.assertRaises(ValueError):' dass self.calc.wurzel(-9)
    #   einen ValueError auslöst!
    # ==========================================================================
    def test_04_wurzel_negativ_exception(self):
        pass

    # ==========================================================================
    # TODO 6: test_05_speicher_funktionen(self)
    # - Prüfe, dass self.calc.speicher zu Beginn 0.0 ist
    # - Rufe self.calc.speicher_plus(15.5) und self.calc.speicher_plus(4.5) auf
    # - Prüfe, dass self.calc.speicher jetzt 20.0 ist
    # - Rufe self.calc.speicher_loeschen() auf und prüfe, dass speicher wieder 0.0 ist
    # ==========================================================================
    def test_05_speicher_funktionen(self):
        pass


class TestBankkonto(unittest.TestCase):

    # ==========================================================================
    # TODO 7: setUp(self)
    # Erstelle zwei Testkonten:
    # - self.k1 = Bankkonto("Alice", 100.0)
    # - self.k2 = Bankkonto("Bob", 50.0)
    # ==========================================================================
    def setUp(self):
        pass

    # ==========================================================================
    # TODO 8: test_06_einzahlen_und_abheben(self)
    # - Zahle 50.0 auf self.k1 ein und prüfe kontostand == 150.0
    # - Prüfe mit self.assertIn(50.0, self.k1.transaktionen), dass die Einzahlung gelistet ist
    # - Hebe 30.0 von self.k1 ab und prüfe kontostand == 120.0
    # - Prüfe mit self.assertIn(-30.0, self.k1.transaktionen), dass die Auszahlung gelistet ist
    # ==========================================================================
    def test_06_einzahlen_und_abheben(self):
        pass

    # ==========================================================================
    # TODO 9: test_07_abheben_ueber_limit_exception(self)
    # Teste mit 'with self.assertRaises(ValueError):'
    # dass das Abheben von 200.0 (bei 100.0 Guthaben) einen ValueError auslöst!
    # ==========================================================================
    def test_07_abheben_ueber_limit_exception(self):
        pass

    # ==========================================================================
    # TODO 10: test_08_ueberweisung(self)
    # - Überweise 40.0 von self.k1 an self.k2
    # - Prüfe self.k1.kontostand == 60.0
    # - Prüfe self.k2.kontostand == 90.0
    # - Prüfe Transaktionen: -40.0 in self.k1.transaktionen und 40.0 in self.k2.transaktionen
    # ==========================================================================
    def test_08_ueberweisung(self):
        pass


# ==============================================================================
# Führe deine eigenen Tests direkt im Terminal aus:
#     python3 aufgabe.py
# ==============================================================================
if __name__ == "__main__":
    unittest.main(verbosity=2)
