import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

try:
    import aufgabe
except ImportError as e:
    raise ImportError(f"Konnte 'aufgabe.py' nicht importieren: {e}")


class TestKapitel08(unittest.TestCase):

    def setUp(self):
        Vektor2D = getattr(aufgabe, "Vektor2D", None)
        Wegstrecke = getattr(aufgabe, "Wegstrecke", None)
        self.assertIsNotNone(Vektor2D, "Klasse 'Vektor2D' nicht in aufgabe.py gefunden!")
        self.assertIsNotNone(Wegstrecke, "Klasse 'Wegstrecke' nicht in aufgabe.py gefunden!")
        self.Vektor2D = Vektor2D
        self.Wegstrecke = Wegstrecke

    def test_01_init_und_darstellung(self):
        """Prüft __init__, __repr__ und __str__ von Vektor2D."""
        v = self.Vektor2D(3, 4)
        self.assertEqual(float(v.x), 3.0)
        self.assertEqual(float(v.y), 4.0)

        # __repr__ soll Entwickler-Syntax liefern
        self.assertEqual(repr(v), "Vektor2D(3.0, 4.0)")

        # __str__ soll lesbare Klammer-Syntax liefern
        self.assertEqual(str(v), "(3.0, 4.0)")

    def test_02_laenge_und_abs(self):
        """Prüft laenge() und die Dunder-Methode __abs__."""
        v = self.Vektor2D(3, 4)
        self.assertAlmostEqual(v.laenge(), 5.0, places=4)
        self.assertAlmostEqual(abs(v), 5.0, places=4)

        v_null = self.Vektor2D(0, 0)
        self.assertAlmostEqual(abs(v_null), 0.0, places=4)

        v_neg = self.Vektor2D(-6, -8)
        self.assertAlmostEqual(abs(v_neg), 10.0, places=4)

    def test_03_addition_und_subtraktion(self):
        """Prüft __add__ und __sub__ zweier Vektoren."""
        v1 = self.Vektor2D(3, 4)
        v2 = self.Vektor2D(1, -2)

        v_sum = v1 + v2
        self.assertIsInstance(v_sum, self.Vektor2D, "Das Ergebnis von v1 + v2 muss ein Vektor2D sein!")
        self.assertAlmostEqual(v_sum.x, 4.0)
        self.assertAlmostEqual(v_sum.y, 2.0)

        v_diff = v1 - v2
        self.assertIsInstance(v_diff, self.Vektor2D, "Das Ergebnis von v1 - v2 muss ein Vektor2D sein!")
        self.assertAlmostEqual(v_diff.x, 2.0)
        self.assertAlmostEqual(v_diff.y, 6.0)

    def test_04_skalarmultiplikation_und_skalarprodukt(self):
        """Prüft Multiplikation mit Zahlen (__mul__, __rmul__) und Skalarprodukt (__mul__)."""
        v = self.Vektor2D(2.5, -4.0)

        # Skalarmultiplikation Zahl von rechts
        v_mal_2 = v * 2
        self.assertIsInstance(v_mal_2, self.Vektor2D)
        self.assertAlmostEqual(v_mal_2.x, 5.0)
        self.assertAlmostEqual(v_mal_2.y, -8.0)

        # Skalarmultiplikation Zahl von links (__rmul__)
        v_links = 3 * v
        self.assertIsInstance(v_links, self.Vektor2D)
        self.assertAlmostEqual(v_links.x, 7.5)
        self.assertAlmostEqual(v_links.y, -12.0)

        # Skalarprodukt zweier Vektoren: v1 * v2 -> x1*x2 + y1*y2
        v1 = self.Vektor2D(2, 3)
        v2 = self.Vektor2D(4, -1)
        skalarprodukt = v1 * v2
        self.assertTrue(isinstance(skalarprodukt, (int, float)), "Skalarprodukt muss eine Zahl sein!")
        self.assertAlmostEqual(skalarprodukt, 2 * 4 + 3 * (-1))  # 8 - 3 = 5

    def test_05_vergleiche(self):
        """Prüft __eq__, __lt__ und __le__."""
        v1 = self.Vektor2D(3, 4)       # Länge 5.0
        v2 = self.Vektor2D(3.0, 4.0)   # Länge 5.0 (gleiche Werte)
        v3 = self.Vektor2D(0, 5)       # Länge 5.0 (andere Werte)
        v4 = self.Vektor2D(1, 1)       # Länge sqrt(2) ≈ 1.414
        v5 = self.Vektor2D(6, 8)       # Länge 10.0

        # Gleichheit
        self.assertEqual(v1, v2)
        self.assertNotEqual(v1, v3)
        self.assertNotEqual(v1, "kein vektor")

        # Kleiner (<)
        self.assertTrue(v4 < v1)
        self.assertFalse(v1 < v4)
        self.assertFalse(v1 < v3)  # gleiche Länge

        # Kleiner-Gleich (<=)
        self.assertTrue(v4 <= v1)
        self.assertTrue(v1 <= v3)  # gleiche Länge -> True
        self.assertTrue(v1 <= v5)
        self.assertFalse(v5 <= v1)

    def test_06_wegstrecke_container(self):
        """Prüft Wegstrecke Initialisierung, __len__ und __getitem__."""
        p1 = self.Vektor2D(0, 0)
        p2 = self.Vektor2D(2, 3)
        p3 = self.Vektor2D(5, 7)

        strecke = self.Wegstrecke([p1, p2])
        self.assertEqual(len(strecke), 2, "len(strecke) muss 2 zurückgeben!")
        self.assertEqual(strecke[0], p1, "strecke[0] muss p1 sein!")
        self.assertEqual(strecke[1], p2, "strecke[1] muss p2 sein!")

        strecke.punkt_hinzufuegen(p3)
        self.assertEqual(len(strecke), 3)
        self.assertEqual(strecke[2], p3)

    def test_07_wegstrecke_gesamtlaenge(self):
        """Prüft Wegstrecke.gesamtlaenge() mit 0, 1 und 3 Wegpunkten."""
        strecke_leer = self.Wegstrecke()
        self.assertAlmostEqual(strecke_leer.gesamtlaenge(), 0.0)

        strecke_einzeln = self.Wegstrecke([self.Vektor2D(10, 20)])
        self.assertAlmostEqual(strecke_einzeln.gesamtlaenge(), 0.0)

        # Route (0,0) -> (3,0) Distanz = 3; (3,0) -> (3,4) Distanz = 4; Summe = 7
        route = self.Wegstrecke([
            self.Vektor2D(0, 0),
            self.Vektor2D(3, 0),
            self.Vektor2D(3, 4)
        ])
        self.assertAlmostEqual(route.gesamtlaenge(), 7.0, places=4)


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