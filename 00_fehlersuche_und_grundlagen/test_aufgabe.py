import unittest
import sys
import importlib
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))


class TestKapitel00(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Wenn ein Test-Runner vorher 'aufgabe' durch ein anderes Modul ersetzt hat (z.B. musterloesung):
        if hasattr(cls, "modul_name"):
            cls.mod = importlib.import_module(cls.modul_name)
        else:
            try:
                cls.mod = importlib.import_module("aufgabe")
            except SyntaxError as e:
                cls.mod = None
                cls.import_error = f"SyntaxError in 'aufgabe.py': {e}. Überprüfe Doppelpunkte und Einrückungen!"
            except Exception as e:
                cls.mod = None
                cls.import_error = f"Fehler beim Import von 'aufgabe.py': {e}"

    def _get_modul(self):
        if getattr(self, "mod", None) is None:
            err = getattr(self, "import_error", "aufgabe.py konnte nicht importiert werden")
            self.fail(f"❌ {err}")
        return self.mod

    def test_01_berechne_endstand(self):
        """Prüft berechne_endstand (Syntax & Einrückung behoben)."""
        mod = self._get_modul()
        self.assertTrue(hasattr(mod, "berechne_endstand"), "Funktion 'berechne_endstand' fehlt!")
        self.assertEqual(mod.berechne_endstand(20, 15), 40, "berechne_endstand(20, 15) sollte 40 sein (inkl. Bonus)!")
        self.assertEqual(mod.berechne_endstand(20, 5), 25, "berechne_endstand(20, 5) sollte 25 sein!")

    def test_02_punkte_multiplizieren(self):
        """Prüft punkte_multiplizieren (Tippfehler NameError behoben)."""
        mod = self._get_modul()
        self.assertTrue(hasattr(mod, "punkte_multiplizieren"), "Funktion 'punkte_multiplizieren' fehlt!")
        self.assertEqual(mod.punkte_multiplizieren(10, 3), 30)
        self.assertEqual(mod.punkte_multiplizieren(7, 2), 14)

    def test_03_formatierte_ausgabe(self):
        """Prüft formatierte_ausgabe (TypeError behoben)."""
        mod = self._get_modul()
        self.assertTrue(hasattr(mod, "formatierte_ausgabe"), "Funktion 'formatierte_ausgabe' fehlt!")
        ergebnis = mod.formatierte_ausgabe("Mia", 50)
        self.assertEqual(ergebnis, "Spieler Mia hat 50 Punkte!")

    def test_04_ist_sieger_grenzwert(self):
        """Prüft Logik von ist_sieger (>= 50 Punkte)."""
        mod = self._get_modul()
        self.assertTrue(hasattr(mod, "ist_sieger"), "Funktion 'ist_sieger' fehlt!")
        self.assertTrue(mod.ist_sieger(50), "Fehler: Genau 50 Punkte müssen True (Sieg) ergeben (>= 50)!")
        self.assertTrue(mod.ist_sieger(100), "100 Punkte müssen True ergeben!")
        self.assertFalse(mod.ist_sieger(49), "49 Punkte dürfen noch kein Sieg sein (False)!")


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