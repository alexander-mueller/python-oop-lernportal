import unittest
import math
import sys
from pathlib import Path

# Sicherstellen, dass das Kapitel-Verzeichnis im Suchpfad liegt
sys.path.insert(0, str(Path(__file__).parent))

try:
    import aufgabe
except ImportError as e:
    raise ImportError(f"Konnte 'aufgabe.py' nicht importieren: {e}")


class TestKapitel11(unittest.TestCase):

    def setUp(self):
        self.Form = getattr(aufgabe, "Form", None)
        self.Rechteck = getattr(aufgabe, "Rechteck", None)
        self.Kreis = getattr(aufgabe, "Kreis", None)
        self.Dreieck = getattr(aufgabe, "Dreieck", None)
        self.Zeichenflaeche = getattr(aufgabe, "Zeichenflaeche", None)

        self.assertIsNotNone(self.Form, "Klasse 'Form' nicht gefunden!")
        self.assertIsNotNone(self.Rechteck, "Klasse 'Rechteck' nicht gefunden!")
        self.assertIsNotNone(self.Kreis, "Klasse 'Kreis' nicht gefunden!")
        self.assertIsNotNone(self.Dreieck, "Klasse 'Dreieck' nicht gefunden!")
        self.assertIsNotNone(self.Zeichenflaeche, "Klasse 'Zeichenflaeche' nicht gefunden!")

    def test_01_form_ist_abstrakt(self):
        """Prüft, ob Form eine echte abstrakte Klasse ist (kann nicht direkt instanziiert werden)."""
        with self.assertRaises(TypeError, msg="Abstrakte Klasse 'Form' darf nicht direkt instanziiert werden können!"):
            self.Form("gelb")

    def test_02_rechteck_berechnungen_und_vererbung(self):
        """Prüft Rechteck: Vererbung von Form, Flächen- und Umfangsberechnung."""
        self.assertTrue(issubclass(self.Rechteck, self.Form), "Rechteck muss von Form erben!")
        
        r = self.Rechteck(5.0, 3.0, farbe="rot")
        self.assertIsInstance(r, self.Form)
        self.assertEqual(r.farbe, "rot")
        self.assertEqual(r.breite, 5.0)
        self.assertEqual(r.hoehe, 3.0)

        self.assertAlmostEqual(r.flaeche(), 15.0)
        self.assertAlmostEqual(r.umfang(), 16.0)

        info = r.info()
        self.assertIn("Rechteck", info)
        self.assertIn("rot", info)
        self.assertIn("15.00", info)
        self.assertIn("16.00", info)

    def test_03_kreis_berechnungen_und_vererbung(self):
        """Prüft Kreis: Vererbung von Form, Flächen- und Umfangsberechnung mit math.pi."""
        self.assertTrue(issubclass(self.Kreis, self.Form), "Kreis muss von Form erben!")

        k = self.Kreis(2.0, farbe="blau")
        self.assertIsInstance(k, self.Form)
        self.assertEqual(k.farbe, "blau")
        self.assertEqual(k.radius, 2.0)

        erwartete_flaeche = math.pi * (2.0 ** 2)
        erwarteter_umfang = 2.0 * math.pi * 2.0
        self.assertAlmostEqual(k.flaeche(), erwartete_flaeche)
        self.assertAlmostEqual(k.umfang(), erwarteter_umfang)

        info = k.info()
        self.assertIn("Kreis", info)
        self.assertIn("blau", info)
        self.assertIn("r=2.0", info)

    def test_04_dreieck_berechnungen_und_pythagoras(self):
        """Prüft rechtwinkliges Dreieck: Hypotenuse, Fläche und Umfang."""
        self.assertTrue(issubclass(self.Dreieck, self.Form), "Dreieck muss von Form erben!")

        d = self.Dreieck(3.0, 4.0, farbe="gruen")
        self.assertIsInstance(d, self.Form)
        self.assertEqual(d.farbe, "gruen")
        self.assertEqual(d.seite_a, 3.0)
        self.assertEqual(d.seite_b, 4.0)

        # Hypotenuse: sqrt(3^2 + 4^2) = sqrt(9 + 16) = 5.0
        self.assertAlmostEqual(d.hypotenuse(), 5.0)
        # Fläche: 0.5 * 3 * 4 = 6.0
        self.assertAlmostEqual(d.flaeche(), 6.0)
        # Umfang: 3 + 4 + 5 = 12.0
        self.assertAlmostEqual(d.umfang(), 12.0)

        info = d.info()
        self.assertIn("Dreieck", info)
        self.assertIn("gruen", info)
        self.assertIn("c=5.0", info)

    def test_05_polymorphismus_in_schleife(self):
        """Prüft, ob eine heterogene Liste von Formen einheitlich polymorph durchlaufen werden kann."""
        formen = [
            self.Rechteck(4.0, 2.0),
            self.Kreis(1.0),
            self.Dreieck(3.0, 4.0),
        ]

        # Polymorpher Aufruf von flaeche() auf jedem Element
        flaechen = [f.flaeche() for f in formen]
        self.assertAlmostEqual(flaechen[0], 8.0)
        self.assertAlmostEqual(flaechen[1], math.pi)
        self.assertAlmostEqual(flaechen[2], 6.0)

    def test_06_zeichenflaeche_grundlagen(self):
        """Prüft Zeichenflaeche Initialisierung und leeren Zustand."""
        zf = self.Zeichenflaeche("Mein Bild")
        self.assertEqual(zf.name, "Mein Bild")
        self.assertEqual(zf.anzahl_formen(), 0)
        self.assertAlmostEqual(zf.gesamte_flaeche(), 0.0)
        self.assertAlmostEqual(zf.gesamter_umfang(), 0.0)
        self.assertIsNone(zf.groesste_form())
        self.assertEqual(zf.report(), [])

    def test_07_zeichenflaeche_summen_berechnung(self):
        """Prüft polymorphe Summenberechnung von gesamte_flaeche() und gesamter_umfang()."""
        zf = self.Zeichenflaeche()
        r = self.Rechteck(4.0, 5.0)  # Fläche: 20, Umfang: 18
        d = self.Dreieck(3.0, 4.0)   # Fläche: 6,  Umfang: 12
        k = self.Kreis(2.0)          # Fläche: 4*pi, Umfang: 4*pi

        zf.hinzufuegen(r)
        zf.hinzufuegen(d)
        zf.hinzufuegen(k)

        self.assertEqual(zf.anzahl_formen(), 3)
        self.assertAlmostEqual(zf.gesamte_flaeche(), 20.0 + 6.0 + (math.pi * 4.0))
        self.assertAlmostEqual(zf.gesamter_umfang(), 18.0 + 12.0 + (2.0 * math.pi * 2.0))

    def test_08_zeichenflaeche_filtern_und_groesste(self):
        """Prüft Filtern nach Farbe (case-insensitive) und Ermittlung der größten Form."""
        zf = self.Zeichenflaeche()
        r1 = self.Rechteck(2.0, 2.0, farbe="Rot")   # Fläche 4
        r2 = self.Rechteck(10.0, 5.0, farbe="rot")  # Fläche 50 (Größte)
        k = self.Kreis(2.0, farbe="Blau")           # Fläche ~12.57
        d = self.Dreieck(3.0, 4.0, farbe="ROT")     # Fläche 6

        zf.hinzufuegen(r1)
        zf.hinzufuegen(r2)
        zf.hinzufuegen(k)
        zf.hinzufuegen(d)

        # Farbfilterung (case-insensitive: Rot, rot, ROT)
        rote = zf.formen_nach_farbe("rot")
        self.assertEqual(len(rote), 3)
        self.assertIn(r1, rote)
        self.assertIn(r2, rote)
        self.assertIn(d, rote)

        blaue = zf.formen_nach_farbe("BLAU")
        self.assertEqual(len(blaue), 1)
        self.assertIn(k, blaue)

        gelbe = zf.formen_nach_farbe("gelb")
        self.assertEqual(len(gelbe), 0)

        # Größte Form finden
        groesste = zf.groesste_form()
        self.assertIs(groesste, r2)

    def test_09_zeichenflaeche_report(self):
        """Prüft report() Ausgabe."""
        zf = self.Zeichenflaeche()
        zf.hinzufuegen(self.Rechteck(2.0, 3.0, farbe="gelb"))
        zf.hinzufuegen(self.Kreis(1.0, farbe="pink"))

        berichte = zf.report()
        self.assertEqual(len(berichte), 2)
        self.assertIn("Rechteck", berichte[0])
        self.assertIn("Kreis", berichte[1])


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