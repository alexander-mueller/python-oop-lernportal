"""
Testsuite für Kapitel G05: Schleifen & Wiederholungen
=====================================================
Schulabgleich: 09.1 & 09.2
"""

import sys
import unittest
from pathlib import Path

# Sicherstellen, dass das aktuelle Verzeichnis im Modulpfad ist
sys.path.insert(0, str(Path(__file__).parent))

try:
    import aufgabe
except ImportError as e:
    raise ImportError(f"Konnte 'aufgabe.py' nicht importieren: {e}")


class TestKapitelG05(unittest.TestCase):

    def test_01_summe_bis(self):
        """Prüft die Funktion summe_bis(n)."""
        self.assertTrue(
            hasattr(aufgabe, "summe_bis"),
            "Fehler: Die Funktion 'summe_bis' fehlt in aufgabe.py!"
        )
        self.assertEqual(
            aufgabe.summe_bis(1), 1,
            "Fehler: summe_bis(1) sollte 1 ergeben!"
        )
        self.assertEqual(
            aufgabe.summe_bis(5), 15,
            "Fehler: summe_bis(5) sollte 15 (1+2+3+4+5) ergeben!"
        )
        self.assertEqual(
            aufgabe.summe_bis(10), 55,
            "Fehler: summe_bis(10) sollte 55 ergeben!"
        )
        self.assertEqual(
            aufgabe.summe_bis(100), 5050,
            "Fehler: summe_bis(100) sollte 5050 (Gaußsche Summenformel) ergeben!"
        )
        self.assertEqual(
            aufgabe.summe_bis(0), 0,
            "Fehler: summe_bis(0) sollte 0 zurückgeben!"
        )
        self.assertEqual(
            aufgabe.summe_bis(-10), 0,
            "Fehler: summe_bis für negative Zahlen sollte 0 zurückgeben!"
        )

    def test_02_fakultaet(self):
        """Prüft die Funktion fakultaet(n)."""
        self.assertTrue(
            hasattr(aufgabe, "fakultaet"),
            "Fehler: Die Funktion 'fakultaet' fehlt in aufgabe.py!"
        )
        self.assertEqual(
            aufgabe.fakultaet(0), 1,
            "Fehler: fakultaet(0) ist mathematisch 1 (0! = 1)!"
        )
        self.assertEqual(
            aufgabe.fakultaet(1), 1,
            "Fehler: fakultaet(1) sollte 1 ergeben!"
        )
        self.assertEqual(
            aufgabe.fakultaet(4), 24,
            "Fehler: fakultaet(4) sollte 24 (1*2*3*4) ergeben!"
        )
        self.assertEqual(
            aufgabe.fakultaet(5), 120,
            "Fehler: fakultaet(5) sollte 120 ergeben!"
        )
        self.assertEqual(
            aufgabe.fakultaet(7), 5040,
            "Fehler: fakultaet(7) sollte 5040 ergeben!"
        )
        # Fehlerbehandlung bei negativen Zahlen
        with self.assertRaises(ValueError, msg="Fehler: fakultaet(-1) muss einen ValueError auslösen!"):
            aufgabe.fakultaet(-1)
        with self.assertRaises(ValueError, msg="Fehler: fakultaet(-5) muss einen ValueError auslösen!"):
            aufgabe.fakultaet(-5)

    def test_03_zaehle_gerade_zahlen(self):
        """Prüft die Funktion zaehle_gerade_zahlen(start, ende)."""
        self.assertTrue(
            hasattr(aufgabe, "zaehle_gerade_zahlen"),
            "Fehler: Die Funktion 'zaehle_gerade_zahlen' fehlt in aufgabe.py!"
        )
        self.assertEqual(
            aufgabe.zaehle_gerade_zahlen(1, 6), 3,
            "Fehler: Im Bereich von 1 bis 6 gibt es 3 gerade Zahlen (2, 4, 6)!"
        )
        self.assertEqual(
            aufgabe.zaehle_gerade_zahlen(1, 10), 5,
            "Fehler: Im Bereich von 1 bis 10 gibt es 5 gerade Zahlen (2, 4, 6, 8, 10)!"
        )
        self.assertEqual(
            aufgabe.zaehle_gerade_zahlen(2, 4), 2,
            "Fehler: Im Bereich von 2 bis 4 gibt es 2 gerade Zahlen (2, 4)!"
        )
        self.assertEqual(
            aufgabe.zaehle_gerade_zahlen(3, 3), 0,
            "Fehler: 3 ist ungerade, also sollte 0 zurückgegeben werden!"
        )
        self.assertEqual(
            aufgabe.zaehle_gerade_zahlen(4, 4), 1,
            "Fehler: Im Bereich [4, 4] gibt es genau eine gerade Zahl (4)!"
        )
        self.assertEqual(
            aufgabe.zaehle_gerade_zahlen(10, 5), 0,
            "Fehler: Wenn start > ende ist, sollte 0 zurückgegeben werden!"
        )
        self.assertEqual(
            aufgabe.zaehle_gerade_zahlen(-4, 2), 4,
            "Fehler: Im Bereich [-4, 2] liegen -4, -2, 0, 2 (4 gerade Zahlen)!"
        )

    def test_04_ist_primzahl(self):
        """Prüft die Funktion ist_primzahl(n)."""
        self.assertTrue(
            hasattr(aufgabe, "ist_primzahl"),
            "Fehler: Die Funktion 'ist_primzahl' fehlt in aufgabe.py!"
        )
        # Echte Primzahlen
        for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 97]:
            self.assertTrue(
                aufgabe.ist_primzahl(p),
                f"Fehler: {p} ist eine Primzahl, wurde aber als False bewertet!"
            )

        # Keine Primzahlen
        for non_p in [0, 1, -1, -7, 4, 6, 8, 9, 15, 21, 25, 100]:
            self.assertFalse(
                aufgabe.ist_primzahl(non_p),
                f"Fehler: {non_p} ist KEINE Primzahl, wurde aber als True bewertet!"
            )

    def test_05_quorsumme(self):
        """Prüft die Funktion quorsumme(n)."""
        fn = getattr(aufgabe, "quorsumme", getattr(aufgabe, "quersumme", None))
        self.assertIsNotNone(
            fn,
            "Fehler: Die Funktion 'quorsumme' (oder 'quersumme') fehlt in aufgabe.py!"
        )
        self.assertEqual(
            fn(0), 0,
            "Fehler: Quersumme von 0 sollte 0 sein!"
        )
        self.assertEqual(
            fn(5), 5,
            "Fehler: Quersumme von 5 sollte 5 sein!"
        )
        self.assertEqual(
            fn(123), 6,
            "Fehler: Quersumme von 123 (1+2+3) sollte 6 sein!"
        )
        self.assertEqual(
            fn(482), 14,
            "Fehler: Quersumme von 482 (4+8+2) sollte 14 sein!"
        )
        self.assertEqual(
            fn(9999), 36,
            "Fehler: Quersumme von 9999 (9+9+9+9) sollte 36 sein!"
        )
        self.assertEqual(
            fn(1000), 1,
            "Fehler: Quersumme von 1000 sollte 1 sein!"
        )
        self.assertEqual(
            fn(-482), 14,
            "Fehler: Quersumme von -482 sollte 14 sein (Vorzeichen wird ignoriert)!"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
