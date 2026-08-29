import unittest
import sys
import importlib
from pathlib import Path

# Sicherstellen, dass das Verzeichnis im Python-Suchpfad liegt
sys.path.insert(0, str(Path(__file__).parent))


class TestKapitelG02(unittest.TestCase):

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
                cls.import_error = f"SyntaxError in 'aufgabe.py': {e}. Überprüfe Doppelpunkte und Einrückungen!"
            except Exception as e:
                cls.mod = None
                cls.import_error = f"Fehler beim Import von 'aufgabe.py': {e}"

    def _get_modul(self):
        if getattr(self, "mod", None) is None:
            err = getattr(self, "import_error", "aufgabe.py konnte nicht importiert werden")
            self.fail(f"❌ {err}")
        return self.mod

    def test_01_bestimme_typ_name(self):
        """Prüft die Funktion bestimme_typ_name(wert) für alle 4 Basisdatentypen und Unbekannt."""
        mod = self._get_modul()
        self.assertTrue(hasattr(mod, "bestimme_typ_name"), "Fehler: Die Funktion 'bestimme_typ_name' fehlt noch!")

        # Ganze Zahlen (int)
        self.assertEqual(mod.bestimme_typ_name(42), "Ganzzahl", "42 muss als 'Ganzzahl' erkannt werden!")
        self.assertEqual(mod.bestimme_typ_name(0), "Ganzzahl", "0 muss als 'Ganzzahl' erkannt werden!")
        self.assertEqual(mod.bestimme_typ_name(-15), "Ganzzahl", "-15 muss als 'Ganzzahl' erkannt werden!")

        # Kommazahlen (float)
        self.assertEqual(mod.bestimme_typ_name(3.14), "Kommazahl", "3.14 muss als 'Kommazahl' erkannt werden!")
        self.assertEqual(mod.bestimme_typ_name(0.0), "Kommazahl", "0.0 muss als 'Kommazahl' erkannt werden!")
        self.assertEqual(mod.bestimme_typ_name(-2.5), "Kommazahl", "-2.5 muss als 'Kommazahl' erkannt werden!")

        # Text (str)
        self.assertEqual(mod.bestimme_typ_name("Hallo"), "Text", "'Hallo' muss als 'Text' erkannt werden!")
        self.assertEqual(mod.bestimme_typ_name(""), "Text", "Leerer String '' muss als 'Text' erkannt werden!")
        self.assertEqual(mod.bestimme_typ_name("123"), "Text", "'123' in Anführungszeichen ist 'Text'!")

        # Wahrheitswerte (bool) - Besonderer Test: Darf nicht als Ganzzahl erkannt werden!
        self.assertEqual(
            mod.bestimme_typ_name(True), "Wahrheitswert",
            "True muss als 'Wahrheitswert' erkannt werden (nicht als 'Ganzzahl'!)"
        )
        self.assertEqual(
            mod.bestimme_typ_name(False), "Wahrheitswert",
            "False muss als 'Wahrheitswert' erkannt werden (nicht als 'Ganzzahl'!)"
        )

        # Andere / Unbekannte Typen
        self.assertEqual(mod.bestimme_typ_name([1, 2, 3]), "Unbekannt", "Eine Liste sollte 'Unbekannt' liefern.")
        self.assertEqual(mod.bestimme_typ_name(None), "Unbekannt", "None sollte 'Unbekannt' liefern.")

    def test_02_summe_aus_texten(self):
        """Prüft die Typkonvertierung von Texten zu Integers und deren Addition."""
        mod = self._get_modul()
        self.assertTrue(hasattr(mod, "summe_aus_texten"), "Fehler: Die Funktion 'summe_aus_texten' fehlt noch!")

        ergebnis = mod.summe_aus_texten("10", "20")
        self.assertIsNotNone(ergebnis, "summe_aus_texten('10', '20') liefert None. Vergiss nicht das 'return'!")
        self.assertNotEqual(
            ergebnis, "1020",
            "Achtung: Du hast '1020' als Text erhalten! Wandle die Strings mit int() um, bevor du addierst!"
        )
        self.assertIsInstance(ergebnis, int, "Das Ergebnis muss vom Typ 'int' sein!")
        self.assertEqual(ergebnis, 30, "summe_aus_texten('10', '20') muss 30 ergeben!")

        self.assertEqual(mod.summe_aus_texten("5", "7"), 12, "summe_aus_texten('5', '7') muss 12 ergeben!")
        self.assertEqual(mod.summe_aus_texten("-3", "8"), 5, "summe_aus_texten('-3', '8') muss 5 ergeben!")
        self.assertEqual(mod.summe_aus_texten("0", "0"), 0, "summe_aus_texten('0', '0') muss 0 ergeben!")

    def test_03_formatiere_preis(self):
        """Prüft die Preisformatierung mit 2 Nachkommastellen und Euro-Symbol."""
        mod = self._get_modul()
        self.assertTrue(hasattr(mod, "formatiere_preis"), "Fehler: Die Funktion 'formatiere_preis' fehlt noch!")

        self.assertEqual(mod.formatiere_preis(19.99), "19.99 €", "19.99 muss zu '19.99 €' formatiert werden!")
        self.assertEqual(mod.formatiere_preis(5.0), "5.00 €", "5.0 muss zu '5.00 €' (mit 2 Nullen) formatiert werden!")
        self.assertEqual(mod.formatiere_preis(0.0), "0.00 €", "0.0 muss zu '0.00 €' formatiert werden!")
        self.assertEqual(mod.formatiere_preis(149.5), "149.50 €", "149.5 muss zu '149.50 €' formatiert werden!")
        self.assertEqual(mod.formatiere_preis(3.14159), "3.14 €", "3.14159 muss auf 2 Nachkommastellen '3.14 €' gerundet werden!")

    def test_04_ist_volljaehrig(self):
        """Prüft die Funktion ist_volljaehrig(alter) für verschiedene Altersgrenzen."""
        mod = self._get_modul()
        self.assertTrue(hasattr(mod, "ist_volljaehrig"), "Fehler: Die Funktion 'ist_volljaehrig' fehlt noch!")

        # Volljährig
        self.assertIs(mod.ist_volljaehrig(18), True, "18 Jahre muss True (volljährig) sein!")
        self.assertIs(mod.ist_volljaehrig(21), True, "21 Jahre muss True sein!")
        self.assertIs(mod.ist_volljaehrig(50), True, "50 Jahre muss True sein!")

        # Minderjährig
        self.assertIs(mod.ist_volljaehrig(17), False, "17 Jahre muss False (minderjährig) sein!")
        self.assertIs(mod.ist_volljaehrig(16), False, "16 Jahre muss False sein!")
        self.assertIs(mod.ist_volljaehrig(0), False, "0 Jahre muss False sein!")


if __name__ == "__main__":
    res = unittest.main(verbosity=2, exit=False)
    try:
        from pathlib import Path
        root_dir = Path(__file__).parent.parent.parent.resolve()
        sys.path.insert(0, str(root_dir))
        from gamification import report_single_chapter_result
        rel_pfad = f"{Path(__file__).parent.parent.name}/{Path(__file__).parent.name}"
        report_single_chapter_result(rel_pfad, res.result.wasSuccessful(), res.result.testsRun)
    except Exception:
        pass
    sys.exit(0 if res.result.wasSuccessful() else 1)