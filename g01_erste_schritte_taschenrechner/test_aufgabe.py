import unittest
import sys
import importlib
from pathlib import Path

# Sicherstellen, dass das Verzeichnis im Python-Suchpfad liegt
sys.path.insert(0, str(Path(__file__).parent))


class TestKapitelG01(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Ermöglicht das Testen alternativer Module (z.B. musterloesung)
        if hasattr(cls, "modul_name"):
            cls.mod = importlib.import_module(cls.modul_name)
        else:
            try:
                cls.mod = importlib.import_module("aufgabe")
            except SyntaxError as e:
                cls.mod = None
                cls.import_error = f"SyntaxError in 'aufgabe.py': {e}. Überprüfe Doppelpunkte und Klammern!"
            except Exception as e:
                cls.mod = None
                cls.import_error = f"Fehler beim Import von 'aufgabe.py': {e}"

    def _get_modul(self):
        if getattr(self, "mod", None) is None:
            err = getattr(self, "import_error", "aufgabe.py konnte nicht importiert werden")
            self.fail(f"❌ {err}")
        return self.mod

    def test_01_addieren(self):
        """Prüft die Funktion addieren(a, b)."""
        mod = self._get_modul()
        self.assertTrue(hasattr(mod, "addieren"), "Fehler: Die Funktion 'addieren' fehlt noch!")
        self.assertEqual(mod.addieren(5, 3), 8, "addieren(5, 3) muss 8 ergeben!")
        self.assertEqual(mod.addieren(-4, 9), 5, "addieren(-4, 9) muss 5 ergeben!")
        self.assertEqual(mod.addieren(0, 0), 0, "addieren(0, 0) muss 0 ergeben!")
        self.assertAlmostEqual(mod.addieren(2.5, 1.5), 4.0, places=4, msg="addieren(2.5, 1.5) muss 4.0 ergeben!")

    def test_02_subtrahieren(self):
        """Prüft die Funktion subtrahieren(a, b)."""
        mod = self._get_modul()
        self.assertTrue(hasattr(mod, "subtrahieren"), "Fehler: Die Funktion 'subtrahieren' fehlt noch!")
        self.assertEqual(mod.subtrahieren(10, 4), 6, "subtrahieren(10, 4) muss 6 ergeben!")
        self.assertEqual(mod.subtrahieren(3, 5), -2, "subtrahieren(3, 5) muss -2 ergeben!")
        self.assertEqual(mod.subtrahieren(7, 7), 0, "subtrahieren(7, 7) muss 0 ergeben!")
        self.assertAlmostEqual(mod.subtrahieren(5.5, 2.3), 3.2, places=4, msg="subtrahieren(5.5, 2.3) muss 3.2 ergeben!")

    def test_03_multiplizieren(self):
        """Prüft die Funktion multiplizieren(a, b)."""
        mod = self._get_modul()
        self.assertTrue(hasattr(mod, "multiplizieren"), "Fehler: Die Funktion 'multiplizieren' fehlt noch!")
        self.assertEqual(mod.multiplizieren(6, 7), 42, "multiplizieren(6, 7) muss 42 ergeben!")
        self.assertEqual(mod.multiplizieren(-3, 4), -12, "multiplizieren(-3, 4) muss -12 ergeben!")
        self.assertEqual(mod.multiplizieren(99, 0), 0, "multiplizieren(99, 0) muss 0 ergeben!")
        self.assertAlmostEqual(mod.multiplizieren(4, 0.5), 2.0, places=4, msg="multiplizieren(4, 0.5) muss 2.0 ergeben!")

    def test_04_dividieren(self):
        """Prüft die Funktion dividieren(a, b)."""
        mod = self._get_modul()
        self.assertTrue(hasattr(mod, "dividieren"), "Fehler: Die Funktion 'dividieren' fehlt noch!")
        self.assertEqual(mod.dividieren(10, 2), 5.0, "dividieren(10, 2) muss 5.0 ergeben!")
        self.assertEqual(mod.dividieren(7, 2), 3.5, "dividieren(7, 2) muss 3.5 ergeben!")
        self.assertEqual(mod.dividieren(-9, 3), -3.0, "dividieren(-9, 3) muss -3.0 ergeben!")
        self.assertAlmostEqual(mod.dividieren(1, 3), 0.333333, places=4, msg="dividieren(1, 3) sollte ca. 0.3333 ergeben!")

    def test_05_ganzzahl_rest(self):
        """Prüft die Funktion ganzzahl_rest(a, b) für Ganzzahldivision // und Modulo %."""
        mod = self._get_modul()
        self.assertTrue(hasattr(mod, "ganzzahl_rest"), "Fehler: Die Funktion 'ganzzahl_rest' fehlt noch!")
        
        ergebnis1 = mod.ganzzahl_rest(17, 5)
        self.assertIsInstance(ergebnis1, tuple, "ganzzahl_rest muss ein Tupel (quotient, rest) zurückgeben!")
        self.assertEqual(len(ergebnis1), 2, "Das zurückgegebene Tupel muss genau 2 Elemente haben: (quotient, rest)")
        self.assertEqual(ergebnis1[0], 3, "17 // 5 ergibt den Quotienten 3!")
        self.assertEqual(ergebnis1[1], 2, "17 % 5 ergibt den Rest 2!")

        ergebnis2 = mod.ganzzahl_rest(20, 4)
        self.assertEqual(ergebnis2, (5, 0), "ganzzahl_rest(20, 4) muss (5, 0) ergeben!")

        ergebnis3 = mod.ganzzahl_rest(7, 3)
        self.assertEqual(ergebnis3, (2, 1), "ganzzahl_rest(7, 3) muss (2, 1) ergeben!")

        ergebnis4 = mod.ganzzahl_rest(4, 9)
        self.assertEqual(ergebnis4, (0, 4), "ganzzahl_rest(4, 9) muss (0, 4) ergeben!")

    def test_06_potenz(self):
        """Prüft die Funktion potenz(basis, exponent)."""
        mod = self._get_modul()
        self.assertTrue(hasattr(mod, "potenz"), "Fehler: Die Funktion 'potenz' fehlt noch!")
        self.assertEqual(mod.potenz(2, 3), 8, "potenz(2, 3) muss 8 ergeben (2 ** 3 = 8)!")
        self.assertEqual(mod.potenz(5, 2), 25, "potenz(5, 2) muss 25 ergeben (5 ** 2 = 25)!")
        self.assertEqual(mod.potenz(10, 0), 1, "potenz(10, 0) muss 1 ergeben (jede Zahl hoch 0 ist 1)!")
        self.assertEqual(mod.potenz(3, 4), 81, "potenz(3, 4) muss 81 ergeben!")
        self.assertAlmostEqual(mod.potenz(4, 0.5), 2.0, places=4, msg="potenz(4, 0.5) muss 2.0 (Quadratwurzel) ergeben!")

    def test_07_kreis_flaeche(self):
        """Prüft die Funktion kreis_flaeche(radius) mit pi = 3.14159."""
        mod = self._get_modul()
        self.assertTrue(hasattr(mod, "kreis_flaeche"), "Fehler: Die Funktion 'kreis_flaeche' fehlt noch!")
        
        erg1 = mod.kreis_flaeche(1)
        self.assertIsNotNone(erg1, "kreis_flaeche(1) gibt None zurück. Vergiss nicht das 'return'!")
        self.assertAlmostEqual(
            erg1, 3.14159, places=4,
            msg="kreis_flaeche(1) muss 3.14159 ergeben!"
        )
        
        erg2 = mod.kreis_flaeche(2)
        self.assertIsNotNone(erg2, "kreis_flaeche(2) gibt None zurück. Vergiss nicht das 'return'!")
        self.assertAlmostEqual(
            erg2, 12.56636, places=4,
            msg="kreis_flaeche(2) muss 12.56636 ergeben!"
        )

        erg0 = mod.kreis_flaeche(0)
        self.assertIsNotNone(erg0, "kreis_flaeche(0) gibt None zurück. Vergiss nicht das 'return'!")
        self.assertAlmostEqual(
            erg0, 0.0, places=4,
            msg="kreis_flaeche(0) muss 0.0 ergeben!"
        )


if __name__ == "__main__":
    res = unittest.main(verbosity=2, exit=False)
    try:
        from pathlib import Path
        sys.path.insert(0, str(Path(__file__).parent.parent))
        from gamification import report_single_chapter_result
        report_single_chapter_result(Path(__file__).parent.name, res.result.wasSuccessful(), res.result.testsRun)
    except Exception:
        pass
    sys.exit(0 if res.result.wasSuccessful() else 1)