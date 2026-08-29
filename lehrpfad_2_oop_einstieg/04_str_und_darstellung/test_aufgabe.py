import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

try:
    import aufgabe
except ImportError as e:
    raise ImportError(f"Konnte 'aufgabe.py' nicht importieren: {e}")


class TestKapitel04(unittest.TestCase):

    def test_01_artikel_init_und_gesamtpreis(self):
        """Prüft Artikel-Konstruktor und gesamtpreis."""
        a = aufgabe.Artikel("Apfel", 0.60, 4)
        self.assertEqual(a.name, "Apfel")
        self.assertEqual(a.preis, 0.60)
        self.assertEqual(a.anzahl, 4)
        self.assertAlmostEqual(a.gesamtpreis(), 2.40, places=2)

    def test_02_artikel_str(self):
        """Prüft die __str__ Implementierung von Artikel."""
        a = aufgabe.Artikel("Milch", 1.29, 2)
        erwartet = "2x Milch (je 1.29 €) = 2.58 €"
        self.assertEqual(str(a), erwartet)

    def test_03_warenkorb_init(self):
        """Prüft, ob der Warenkorb mit einer leeren Liste startet."""
        korb = aufgabe.Warenkorb()
        self.assertTrue(hasattr(korb, "artikel_liste"))
        self.assertEqual(korb.artikel_liste, [])

    def test_04_artikel_hinzufuegen_und_gesamtsumme(self):
        """Prüft das Hinzufügen von Artikeln und die Gesamtsumme."""
        korb = aufgabe.Warenkorb()
        self.assertAlmostEqual(korb.gesamtsumme(), 0.0, places=2)

        a1 = aufgabe.Artikel("Brot", 2.50, 2)    # 5.00 €
        a2 = aufgabe.Artikel("Butter", 1.80, 1)  # 1.80 €
        
        korb.artikel_hinzufuegen(a1)
        korb.artikel_hinzufuegen(a2)

        self.assertEqual(len(korb.artikel_liste), 2)
        self.assertAlmostEqual(korb.gesamtsumme(), 6.80, places=2)

    def test_05_bon_text(self):
        """Prüft den formatierten Bon-Text."""
        korb = aufgabe.Warenkorb()
        korb.artikel_hinzufuegen(aufgabe.Artikel("Kaffee", 4.50, 1))
        korb.artikel_hinzufuegen(aufgabe.Artikel("Keks", 1.20, 3))

        bon = korb.bon_text()
        erwartete_zeilen = [
            "--- KASSENZETTEL ---",
            "1x Kaffee (je 4.50 €) = 4.50 €",
            "3x Keks (je 1.20 €) = 3.60 €",
            "--------------------",
            "Gesamtsumme: 8.10 €"
        ]
        erwartet = "\n".join(erwartete_zeilen)
        self.assertEqual(bon.strip(), erwartet.strip())


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