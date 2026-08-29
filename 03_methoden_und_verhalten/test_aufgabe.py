import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

try:
    import aufgabe
except ImportError as e:
    raise ImportError(f"Konnte 'aufgabe.py' nicht importieren: {e}")


class TestKapitel03(unittest.TestCase):

    def test_01_init(self):
        """Prüft die Initialisierung des Helden."""
        h = aufgabe.Held("Galahad", 90, 18)
        self.assertEqual(h.name, "Galahad")
        self.assertEqual(h.leben, 90)
        self.assertEqual(h.max_leben, 90)
        self.assertEqual(h.angriffskraft, 18)
        self.assertTrue(h.ist_am_leben)

    def test_02_schaden_erleiden(self):
        """Prüft Schadensberechnung und K.O.-Logik."""
        h = aufgabe.Held("Krieger", 50, 10)
        
        # Normaler Schaden
        schaden = h.schaden_erleiden(20)
        self.assertEqual(schaden, 20)
        self.assertEqual(h.leben, 30)
        self.assertTrue(h.ist_am_leben)

        # Schaden, der das Leben auf 0 oder darunter bringt
        h.schaden_erleiden(40)
        self.assertEqual(h.leben, 0, "Leben darf nach Über-Schaden nicht negativ werden, sondern muss 0 sein!")
        self.assertFalse(h.ist_am_leben, "Held muss nach 0 HP als besiegt (ist_am_leben=False) markiert werden!")

        # Schaden an bereits besiegtem Helden
        schaden_tot = h.schaden_erleiden(10)
        self.assertEqual(schaden_tot, 0)
        self.assertEqual(h.leben, 0)

    def test_03_heilen(self):
        """Prüft die Heilungsfunktion und max_leben Begrenzung."""
        h = aufgabe.Held("Priester", 100, 5)
        h.leben = 70

        # Teilweise Heilung
        geheilt = h.heilen(15)
        self.assertEqual(geheilt, 15)
        self.assertEqual(h.leben, 85)

        # Heilung über max_leben hinaus
        geheilt_cap = h.heilen(30)
        self.assertEqual(geheilt_cap, 15, "Es sollten nur 15 HP geheilt werden, da max_leben=100!")
        self.assertEqual(h.leben, 100)

        # Heilung eines toten Helden
        h.leben = 0
        h.ist_am_leben = False
        geheilt_tot = h.heilen(50)
        self.assertEqual(geheilt_tot, 0, "Ein besiegter Held kann nicht geheilt werden!")
        self.assertEqual(h.leben, 0)

    def test_04_angreifen(self):
        """Prüft die Interaktion beim Angriff."""
        held1 = aufgabe.Held("Held", 50, 20)
        held2 = aufgabe.Held("Monster", 30, 10)

        erfolg = held1.angreifen(held2)
        self.assertTrue(erfolg)
        self.assertEqual(held2.leben, 10)
        self.assertTrue(held2.ist_am_leben)

        # Zweiter Angriff besiegt Monster
        erfolg2 = held1.angreifen(held2)
        self.assertTrue(erfolg2)
        self.assertEqual(held2.leben, 0)
        self.assertFalse(held2.ist_am_leben)

        # Weiterer Angriff auf besiegtes Monster schlägt fehl
        erfolg3 = held1.angreifen(held2)
        self.assertFalse(erfolg3, "Ein Angriff auf ein besiegtes Ziel sollte False zurückgeben!")

    def test_05_status_text(self):
        """Prüft die Statusanzeige."""
        h = aufgabe.Held("Arthur", 100, 20)
        self.assertEqual(
            h.status_text(),
            "[Arthur] HP: 100/100 | Kraft: 20 | Status: Lebendig"
        )
        h.schaden_erleiden(100)
        self.assertEqual(
            h.status_text(),
            "[Arthur] HP: 0/100 | Kraft: 20 | Status: Besiegt"
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