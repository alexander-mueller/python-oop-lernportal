"""
Testsuite für Kapitel G06: Eigene Funktionen & Module
=====================================================
Schulabgleich: 05.0 & 05.1
"""

import math
import sys
import unittest
from pathlib import Path

# Sicherstellen, dass das aktuelle Verzeichnis im Modulpfad ist
sys.path.insert(0, str(Path(__file__).parent))

try:
    import aufgabe
except ImportError as e:
    raise ImportError(f"Konnte 'aufgabe.py' nicht importieren: {e}")


class TestKapitelG06(unittest.TestCase):

    def test_01_hypotenuse(self):
        """Prüft die Funktion hypotenuse(a, b)."""
        self.assertTrue(
            hasattr(aufgabe, "hypotenuse"),
            "Fehler: Die Funktion 'hypotenuse' fehlt in aufgabe.py!"
        )
        res = aufgabe.hypotenuse(3.0, 4.0)
        self.assertIsNotNone(
            res,
            "Fehler: hypotenuse(3.0, 4.0) gibt None zurück. Vergiss nicht das 'return'!"
        )
        # Standard rechtwinklige Dreiecke
        self.assertAlmostEqual(
            res, 5.0, places=4,
            msg="Fehler: hypotenuse(3.0, 4.0) sollte 5.0 sein (3-4-5 Dreieck)!"
        )
        self.assertAlmostEqual(
            aufgabe.hypotenuse(5.0, 12.0), 13.0, places=4,
            msg="Fehler: hypotenuse(5.0, 12.0) sollte 13.0 sein (5-12-13 Dreieck)!"
        )
        self.assertAlmostEqual(
            aufgabe.hypotenuse(6.0, 8.0), 10.0, places=4,
            msg="Fehler: hypotenuse(6.0, 8.0) sollte 10.0 sein!"
        )
        # Fehlerbehandlung für negative Längen
        with self.assertRaises(ValueError, msg="Fehler: hypotenuse(-3.0, 4.0) muss einen ValueError auslösen!"):
            aufgabe.hypotenuse(-3.0, 4.0)
        with self.assertRaises(ValueError, msg="Fehler: hypotenuse(3.0, -4.0) muss einen ValueError auslösen!"):
            aufgabe.hypotenuse(3.0, -4.0)

    def test_02_zylinder_volumen(self):
        """Prüft die Funktion zylinder_volumen(radius, hoehe)."""
        self.assertTrue(
            hasattr(aufgabe, "zylinder_volumen"),
            "Fehler: Die Funktion 'zylinder_volumen' fehlt in aufgabe.py!"
        )
        res = aufgabe.zylinder_volumen(3.0, 5.0)
        self.assertIsNotNone(
            res,
            "Fehler: zylinder_volumen(3.0, 5.0) gibt None zurück. Vergiss nicht das 'return'!"
        )
        # V = pi * r^2 * h
        # Für r=3, h=5 -> pi * 9 * 5 = 45 * pi ≈ 141.3716694
        erwartet = math.pi * 9 * 5
        self.assertAlmostEqual(
            res, erwartet, places=4,
            msg=f"Fehler: zylinder_volumen(3.0, 5.0) sollte {erwartet:.4f} sein!"
        )
        # Für r=1, h=1 -> pi
        self.assertAlmostEqual(
            aufgabe.zylinder_volumen(1.0, 1.0), math.pi, places=4,
            msg="Fehler: zylinder_volumen(1.0, 1.0) sollte math.pi entsprechen!"
        )
        # Für r=0, h=10 -> 0.0
        self.assertAlmostEqual(
            aufgabe.zylinder_volumen(0.0, 10.0), 0.0, places=4,
            msg="Fehler: zylinder_volumen(0.0, 10.0) sollte 0.0 sein!"
        )
        # Fehlerbehandlung für negative Werte
        with self.assertRaises(ValueError, msg="Fehler: zylinder_volumen(-1.0, 5.0) muss einen ValueError auslösen!"):
            aufgabe.zylinder_volumen(-1.0, 5.0)
        with self.assertRaises(ValueError, msg="Fehler: zylinder_volumen(2.0, -3.0) muss einen ValueError auslösen!"):
            aufgabe.zylinder_volumen(2.0, -3.0)

    def test_03_wuerfle_wuerfel_standard(self):
        """Prüft wuerfle_wuerfel mit Standardwert seiten=6."""
        self.assertTrue(
            hasattr(aufgabe, "wuerfle_wuerfel"),
            "Fehler: Die Funktion 'wuerfle_wuerfel' fehlt in aufgabe.py!"
        )
        wuerfe = aufgabe.wuerfle_wuerfel(20)
        self.assertIsInstance(
            wuerfe, list,
            "Fehler: wuerfle_wuerfel muss eine Liste zurückgeben!"
        )
        self.assertEqual(len(wuerfe), 20, "Fehler: Bei anzahl=20 müssen 20 Würfelergebnisse geliefert werden!")
        for w in wuerfe:
            self.assertIsInstance(w, int, "Fehler: Jedes Würfelergebnis muss eine ganze Zahl (int) sein!")
            self.assertTrue(1 <= w <= 6, f"Fehler: Würfelergebnis {w} liegt nicht zwischen 1 und 6!")

        # 0 Würfel
        leer = aufgabe.wuerfle_wuerfel(0)
        self.assertEqual(leer, [], "Fehler: wuerfle_wuerfel(0) sollte eine leere Liste [] zurückgeben!")

    def test_04_wuerfle_wuerfel_custom_seiten(self):
        """Prüft wuerfle_wuerfel mit benutzerdefinierter Seitenzahl (z.B. W20)."""
        wuerfe_w20 = aufgabe.wuerfle_wuerfel(25, seiten=20)
        self.assertIsInstance(
            wuerfe_w20, list,
            "Fehler: wuerfle_wuerfel(25, seiten=20) muss eine Liste zurückgeben!"
        )
        self.assertEqual(len(wuerfe_w20), 25)
        for w in wuerfe_w20:
            self.assertTrue(1 <= w <= 20, f"Fehler: W20-Ergebnis {w} liegt nicht im Bereich [1, 20]!")

        # W2 (Münzwurf)
        wuerfe_w2 = aufgabe.wuerfle_wuerfel(10, seiten=2)
        self.assertIsInstance(wuerfe_w2, list)
        for w in wuerfe_w2:
            self.assertIn(w, [1, 2], f"Fehler: W2-Ergebnis {w} darf nur 1 oder 2 sein!")

    def test_05_wuerfle_wuerfel_ungueltig(self):
        """Prüft ungültige Argumente bei wuerfle_wuerfel."""
        with self.assertRaises(ValueError, msg="Fehler: wuerfle_wuerfel(-1) muss ValueError auslösen!"):
            aufgabe.wuerfle_wuerfel(-1)
        with self.assertRaises(ValueError, msg="Fehler: wuerfle_wuerfel(5, seiten=0) muss ValueError auslösen!"):
            aufgabe.wuerfle_wuerfel(5, seiten=0)
        with self.assertRaises(ValueError, msg="Fehler: wuerfle_wuerfel(5, seiten=-4) muss ValueError auslösen!"):
            aufgabe.wuerfle_wuerfel(5, seiten=-4)

    def test_06_statistik(self):
        """Prüft die Funktion statistik(zahlen)."""
        self.assertTrue(
            hasattr(aufgabe, "statistik"),
            "Fehler: Die Funktion 'statistik' fehlt in aufgabe.py!"
        )
        zahlen = [10.0, 20.0, 30.0, 40.0, 50.0]
        ergebnis = aufgabe.statistik(zahlen)
        self.assertIsInstance(
            ergebnis, tuple,
            "Fehler: statistik(...) muss ein Tupel (min_wert, max_wert, mittelwert) zurückgeben!"
        )
        self.assertEqual(len(ergebnis), 3, "Fehler: Das Ergebnis-Tupel muss genau 3 Elemente haben!")

        min_w, max_w, mittel = ergebnis
        self.assertEqual(min_w, 10.0, "Fehler: Minimum von [10, 20, 30, 40, 50] sollte 10.0 sein!")
        self.assertEqual(max_w, 50.0, "Fehler: Maximum von [10, 20, 30, 40, 50] sollte 50.0 sein!")
        self.assertEqual(mittel, 30.0, "Fehler: Mittelwert von [10, 20, 30, 40, 50] sollte 30.0 sein!")

        # Einzelelement
        einz = aufgabe.statistik([7.5])
        self.assertIsInstance(einz, tuple)
        einz_min, einz_max, einz_mit = einz
        self.assertEqual(einz_min, 7.5)
        self.assertEqual(einz_max, 7.5)
        self.assertEqual(einz_mit, 7.5)

    def test_07_statistik_leere_liste(self):
        """Prüft Fehlerbehandlung bei leerer Liste in statistik()."""
        with self.assertRaises(ValueError, msg="Fehler: statistik([]) für eine leere Liste muss einen ValueError auslösen!"):
            aufgabe.statistik([])


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