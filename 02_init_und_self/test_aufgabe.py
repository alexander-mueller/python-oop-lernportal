import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

try:
    import aufgabe
except ImportError as e:
    raise ImportError(f"Konnte 'aufgabe.py' nicht importieren: {e}")


class TestKapitel02(unittest.TestCase):

    def test_01_init_standardwert(self):
        """Prüft __init__ mit Standardwert für kontostand."""
        konto = aufgabe.Bankkonto("Lukas")
        self.assertEqual(konto.inhaber, "Lukas", "Fehler: self.inhaber wurde nicht korrekt gesetzt!")
        self.assertEqual(konto.kontostand, 0.0, "Fehler: Standardwert für kontostand sollte 0.0 sein!")

    def test_02_init_mit_startguthaben(self):
        """Prüft __init__ mit übergebenem Startguthaben."""
        konto = aufgabe.Bankkonto("Sarah", 100.50)
        self.assertEqual(konto.inhaber, "Sarah")
        self.assertEqual(konto.kontostand, 100.50)

    def test_03_einzahlen_gueltig(self):
        """Prüft erfolgreiches Einzahlen."""
        konto = aufgabe.Bankkonto("Tim", 50.0)
        erfolg = konto.einzahlen(25.0)
        self.assertTrue(erfolg, "Fehler: einzahlen(25.0) sollte True zurückgeben!")
        self.assertEqual(konto.kontostand, 75.0, "Fehler: Kontostand sollte nach 25€ Einzahlung auf 50€ bei 75.0€ liegen!")

    def test_04_einzahlen_ungueltig(self):
        """Prüft Einzahlen von negativen Beträgen oder 0."""
        konto = aufgabe.Bankkonto("Tim", 50.0)
        
        erfolg_null = konto.einzahlen(0)
        self.assertFalse(erfolg_null, "Fehler: Einzahlen von 0 sollte False zurückgeben!")
        self.assertEqual(konto.kontostand, 50.0, "Fehler: Kontostand darf sich bei 0€ nicht ändern!")

        erfolg_neg = konto.einzahlen(-10.0)
        self.assertFalse(erfolg_neg, "Fehler: Einzahlen von negativen Beträgen sollte False zurückgeben!")
        self.assertEqual(konto.kontostand, 50.0, "Fehler: Kontostand darf sich bei negativem Betrag nicht ändern!")

    def test_05_auszahlen_erfolgreich(self):
        """Prüft erfolgreiches Auszahlen."""
        konto = aufgabe.Bankkonto("Emma", 80.0)
        erfolg = konto.auszahlen(30.0)
        self.assertTrue(erfolg, "Fehler: auszahlen(30.0) bei 80€ Guthaben sollte True zurückgeben!")
        self.assertEqual(konto.kontostand, 50.0, "Fehler: Kontostand sollte nach Auszahlung 50.0€ sein!")

        # Gesamtes Guthaben abheben
        erfolg_alles = konto.auszahlen(50.0)
        self.assertTrue(erfolg_alles, "Fehler: Gesamtes Guthaben abheben sollte möglich sein!")
        self.assertEqual(konto.kontostand, 0.0)

    def test_06_auszahlen_zu_viel_oder_ungueltig(self):
        """Prüft Auszahlen bei unzureichendem Guthaben oder negativem Betrag."""
        konto = aufgabe.Bankkonto("Emma", 20.0)
        
        # Zu viel abheben
        erfolg = konto.auszahlen(50.0)
        self.assertFalse(erfolg, "Fehler: Auszahlen von mehr Geld als vorhanden ist muss False liefern!")
        self.assertEqual(konto.kontostand, 20.0, "Fehler: Kontostand darf sich nicht ändern, wenn Auszahlung fehlschlägt!")

        # Negativer Betrag
        erfolg_neg = konto.auszahlen(-5.0)
        self.assertFalse(erfolg_neg, "Fehler: Auszahlen von negativen Beträgen muss False liefern!")
        self.assertEqual(konto.kontostand, 20.0)

    def test_07_info_text(self):
        """Prüft die Formatierung der info_text-Methode."""
        konto = aufgabe.Bankkonto("Mia", 25.5)
        text = konto.info_text()
        erwartet = "Konto von Mia: 25.50 Euro"
        self.assertEqual(
            text,
            erwartet,
            f"Fehler: Text weicht ab!\nErwartet: '{erwartet}'\nErhalten: '{text}'"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
