import unittest
import sys
from pathlib import Path

# Sicherstellen, dass das aktuelle Verzeichnis im Modulpfad ist
sys.path.insert(0, str(Path(__file__).parent))

try:
    import aufgabe
except ImportError as e:
    raise ImportError(f"Konnte 'aufgabe.py' nicht importieren: {e}")


class TestKapitel01(unittest.TestCase):

    def test_01_klasse_existiert(self):
        """Prüft, ob die Klasse Haustier definiert wurde."""
        self.assertTrue(
            hasattr(aufgabe, "Haustier"),
            "Fehler: Die Klasse 'Haustier' existiert noch nicht. Nutze: class Haustier:"
        )
        self.assertTrue(
            isinstance(aufgabe.Haustier, type),
            "Fehler: 'Haustier' sollte eine Klasse sein!"
        )

    def test_02_erstelle_bello(self):
        """Prüft, ob erstelle_bello() ein korrektes Haustier-Objekt liefert."""
        self.assertTrue(hasattr(aufgabe, "erstelle_bello"), "Fehler: Funktion 'erstelle_bello' fehlt!")
        bello = aufgabe.erstelle_bello()
        self.assertIsNotNone(bello, "Fehler: 'erstelle_bello()' gibt None zurück. Vergiss nicht das 'return'!")
        self.assertIsInstance(bello, aufgabe.Haustier, "Fehler: 'bello' muss eine Instanz der Klasse 'Haustier' sein!")
        self.assertEqual(getattr(bello, "name", None), "Bello", "Fehler: 'bello.name' muss 'Bello' sein!")
        self.assertEqual(getattr(bello, "tierart", None), "Hund", "Fehler: 'bello.tierart' muss 'Hund' sein!")
        self.assertEqual(getattr(bello, "alter", None), 3, "Fehler: 'bello.alter' muss 3 sein!")

    def test_03_erstelle_mimi(self):
        """Prüft, ob erstelle_mimi() ein korrektes Haustier-Objekt liefert."""
        self.assertTrue(hasattr(aufgabe, "erstelle_mimi"), "Fehler: Funktion 'erstelle_mimi' fehlt!")
        mimi = aufgabe.erstelle_mimi()
        self.assertIsNotNone(mimi, "Fehler: 'erstelle_mimi()' gibt None zurück. Vergiss nicht das 'return'!")
        self.assertIsInstance(mimi, aufgabe.Haustier, "Fehler: 'mimi' muss eine Instanz der Klasse 'Haustier' sein!")
        self.assertEqual(getattr(mimi, "name", None), "Mimi", "Fehler: 'mimi.name' muss 'Mimi' sein!")
        self.assertEqual(getattr(mimi, "tierart", None), "Katze", "Fehler: 'mimi.tierart' muss 'Katze' sein!")
        self.assertEqual(getattr(mimi, "alter", None), 5, "Fehler: 'mimi.alter' muss 5 sein!")

    def test_04_steckbrief_text(self):
        """Prüft, ob steckbrief_text() den richtigen String formatiert."""
        self.assertTrue(hasattr(aufgabe, "steckbrief_text"), "Fehler: Funktion 'steckbrief_text' fehlt!")
        tier = aufgabe.Haustier()
        tier.name = "Rocky"
        tier.tierart = "Papagei"
        tier.alter = 2

        ergebnis = aufgabe.steckbrief_text(tier)
        erwartet = "Rocky ist ein(e) Papagei und ist 2 Jahre alt."
        self.assertEqual(
            ergebnis,
            erwartet,
            f"Fehler: Textausgabe weicht ab!\nErwartet: '{erwartet}'\nErhalten: '{ergebnis}'"
        )

    def test_05_aelteres_tier(self):
        """Prüft die Altersvergleich-Funktion."""
        self.assertTrue(hasattr(aufgabe, "aelteres_tier"), "Fehler: Funktion 'aelteres_tier' fehlt!")
        t1 = aufgabe.Haustier()
        t1.name = "Tier A"
        t1.alter = 4

        t2 = aufgabe.Haustier()
        t2.name = "Tier B"
        t2.alter = 7

        t3 = aufgabe.Haustier()
        t3.name = "Tier C"
        t3.alter = 4

        self.assertIs(aufgabe.aelteres_tier(t1, t2), t2, "Fehler: Tier B (7) ist älter als Tier A (4)!")
        self.assertIs(aufgabe.aelteres_tier(t2, t1), t2, "Fehler: Tier B (7) ist älter als Tier A (4)!")
        self.assertIs(aufgabe.aelteres_tier(t1, t3), t1, "Fehler: Bei gleichem Alter soll tier1 zurückgegeben werden!")


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