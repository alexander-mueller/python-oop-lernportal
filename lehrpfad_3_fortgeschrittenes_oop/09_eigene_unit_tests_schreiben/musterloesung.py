"""
Kapitel 09: Eigene Unit Tests schreiben & TDD 🧪
================================================
Musterlösung: Vollständige Test-Suite für Taschenrechner und Bankkonto.
"""

import math
import unittest
from typing import List


# ==============================================================================
# Vorgegebene Klassen: Taschenrechner & Bankkonto
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
# Musterlösung: Die Unit-Test-Klassen
# ==============================================================================

class TestTaschenrechner(unittest.TestCase):

    def setUp(self):
        """Wird vor JEDEM einzelnen Test ausgeführt."""
        self.calc = Taschenrechner()

    def test_01_grundrechenarten(self):
        """Testet Addition, Subtraktion und Multiplikation."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.sub(10, 4), 6)
        self.assertEqual(self.calc.mul(3, 7), 21)

    def test_02_division_und_kommazahlen(self):
        """Testet normale Division und periodische Kommazahlen mit assertAlmostEqual."""
        self.assertEqual(self.calc.div(10, 2), 5.0)
        self.assertAlmostEqual(self.calc.div(10, 3), 3.3333, places=2)

    def test_03_division_durch_null_exception(self):
        """Testet, dass bei Division durch 0 ein ZeroDivisionError geworfen wird."""
        with self.assertRaises(ZeroDivisionError):
            self.calc.div(10, 0)

    def test_04_wurzel_negativ_exception(self):
        """Testet normale Wurzel und Exception bei negativen Zahlen."""
        self.assertAlmostEqual(self.calc.wurzel(16), 4.0)
        with self.assertRaises(ValueError):
            self.calc.wurzel(-9)

    def test_05_speicher_funktionen(self):
        """Testet speicher_plus und speicher_loeschen."""
        self.assertEqual(self.calc.speicher, 0.0)
        self.calc.speicher_plus(15.5)
        self.calc.speicher_plus(4.5)
        self.assertEqual(self.calc.speicher, 20.0)
        self.calc.speicher_loeschen()
        self.assertEqual(self.calc.speicher, 0.0)


class TestBankkonto(unittest.TestCase):

    def setUp(self):
        """Erstellt zwei frische Konten vor jedem Test."""
        self.k1 = Bankkonto("Alice", 100.0)
        self.k2 = Bankkonto("Bob", 50.0)

    def test_06_einzahlen_und_abheben(self):
        """Testet Ein- und Auszahlung sowie Transaktionshistorie."""
        self.k1.einzahlen(50.0)
        self.assertEqual(self.k1.kontostand, 150.0)
        self.assertIn(50.0, self.k1.transaktionen)

        self.k1.abheben(30.0)
        self.assertEqual(self.k1.kontostand, 120.0)
        self.assertIn(-30.0, self.k1.transaktionen)

    def test_07_abheben_ueber_limit_exception(self):
        """Testet, dass Abheben von mehr als Kontostand einen ValueError auslöst."""
        with self.assertRaises(ValueError):
            self.k1.abheben(200.0)

    def test_08_ueberweisung(self):
        """Testet erfolgreiche Überweisung zwischen zwei Konten."""
        self.k1.ueberweisen(self.k2, 40.0)
        self.assertEqual(self.k1.kontostand, 60.0)
        self.assertEqual(self.k2.kontostand, 90.0)
        self.assertIn(-40.0, self.k1.transaktionen)
        self.assertIn(40.0, self.k2.transaktionen)


if __name__ == "__main__":
    unittest.main(verbosity=2)
