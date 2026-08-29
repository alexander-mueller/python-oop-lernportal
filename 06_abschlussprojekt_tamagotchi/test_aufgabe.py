import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

try:
    import aufgabe
except ImportError as e:
    raise ImportError(f"Konnte 'aufgabe.py' nicht importieren: {e}")


class TestKapitel06(unittest.TestCase):

    def test_01_init(self):
        """Prüft die Standard-Startwerte eines neuen Tamagotchis."""
        t = aufgabe.Tamagotchi("Pikachu", "Maus")
        self.assertEqual(t.name, "Pikachu")
        self.assertEqual(t.tierart, "Maus")
        self.assertEqual(t.hunger, 50)
        self.assertEqual(t.muedigkeit, 20)
        self.assertEqual(t.glueck, 80)
        self.assertEqual(t.alter_tage, 0)
        self.assertTrue(t.ist_lebendig)

    def test_02_fuettern(self):
        """Prüft die Auswirkungen des Fütterns."""
        t = aufgabe.Tamagotchi("Yoshi")
        t.hunger = 50
        t.muedigkeit = 20
        t.glueck = 80

        text = t.fuettern(20)
        self.assertEqual(t.hunger, 30, "Hunger sollte um 20 sinken!")
        self.assertEqual(t.glueck, 85, "Glück sollte um 5 steigen!")
        self.assertEqual(t.muedigkeit, 25, "Müdigkeit sollte um 5 steigen!")
        self.assertIn("Yoshi", text)

        # Hunger darf nicht negativ werden
        t.fuettern(100)
        self.assertEqual(t.hunger, 0, "Hunger darf nicht unter 0 fallen!")

    def test_03_spielen(self):
        """Prüft die Auswirkungen des Spielens und die Müdigkeitsgrenze."""
        t = aufgabe.Tamagotchi("Sparky")
        t.hunger = 30
        t.muedigkeit = 20
        t.glueck = 50

        text = t.spielen(25)
        self.assertEqual(t.glueck, 75)
        self.assertEqual(t.hunger, 45)
        self.assertEqual(t.muedigkeit, 40)
        self.assertIn("Sparky", text)

        # Zu müde zum Spielen (muedigkeit > 80)
        t.muedigkeit = 85
        t.glueck = 50
        text_muede = t.spielen(20)
        self.assertIn("zu müde", text_muede.lower())
        self.assertEqual(t.glueck, 50, "Werte dürfen sich bei Müdigkeit nicht ändern!")

    def test_04_schlafen(self):
        """Prüft Schlafen und Altern."""
        t = aufgabe.Tamagotchi("Luna")
        t.muedigkeit = 70
        t.hunger = 20
        t.alter_tage = 2

        t.schlafen()
        self.assertEqual(t.muedigkeit, 0, "Müdigkeit sollte auf 0 zurückgesetzt werden!")
        self.assertEqual(t.hunger, 35, "Hunger sollte um 15 steigen!")
        self.assertEqual(t.alter_tage, 3, "Alter in Tagen sollte um 1 steigen!")

    def test_05_zeit_vergeht_und_lebenszyklus(self):
        """Prüft Verstreichen der Zeit und Ableben bei 100 Hunger oder 0 Glück."""
        t = aufgabe.Tamagotchi("Rex")
        t.hunger = 80
        t.muedigkeit = 30
        t.glueck = 20

        lebendig = t.zeit_vergeht()
        self.assertTrue(lebendig)
        self.assertEqual(t.hunger, 90)
        self.assertEqual(t.muedigkeit, 40)
        self.assertEqual(t.glueck, 10)

        # Noch ein Zeitschritt -> Hunger erreicht 100
        lebendig2 = t.zeit_vergeht()
        self.assertFalse(lebendig2)
        self.assertFalse(t.ist_lebendig)

        # Aktionen an totem Tamagotchi
        reaktion = t.fuettern()
        self.assertIn("reagiert nicht mehr", reaktion)

    def test_06_str_darstellung(self):
        """Prüft die __str__ Repräsentation."""
        t = aufgabe.Tamagotchi("Bobo", "Affe")
        str_lebendig = str(t)
        self.assertIn("Bobo", str_lebendig)
        self.assertIn("Affe", str_lebendig)
        self.assertIn("50/100", str_lebendig)

        t.ist_lebendig = False
        str_tot = str(t)
        self.assertIn("RIP", str_tot)


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