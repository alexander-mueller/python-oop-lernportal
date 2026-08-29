import unittest
import sys
from pathlib import Path

# Sicherstellen, dass das aktuelle Verzeichnis im Python-Pfad liegt
sys.path.insert(0, str(Path(__file__).parent))

try:
    import aufgabe
except ImportError as e:
    raise ImportError(f"Konnte 'aufgabe.py' nicht importieren: {e}")


class TestKapitel12(unittest.TestCase):

    def setUp(self):
        # Klassen und Funktionen dynamisch aus aufgabe laden
        self.BankFehler = getattr(aufgabe, "BankFehler", None)
        self.UngueltigePinError = getattr(aufgabe, "UngueltigePinError", None)
        self.KontoGesperrtError = getattr(aufgabe, "KontoGesperrtError", None)
        self.NichtGenugGuthabenError = getattr(aufgabe, "NichtGenugGuthabenError", None)
        self.UngueltigerBetragError = getattr(aufgabe, "UngueltigerBetragError", None)
        self.Bankkonto = getattr(aufgabe, "Bankkonto", None)
        self.geldautomat_abheben = getattr(aufgabe, "geldautomat_abheben", None)

        self.assertIsNotNone(self.BankFehler, "Klasse 'BankFehler' nicht gefunden!")
        self.assertIsNotNone(self.UngueltigePinError, "Klasse 'UngueltigePinError' nicht gefunden!")
        self.assertIsNotNone(self.KontoGesperrtError, "Klasse 'KontoGesperrtError' nicht gefunden!")
        self.assertIsNotNone(self.NichtGenugGuthabenError, "Klasse 'NichtGenugGuthabenError' nicht gefunden!")
        self.assertIsNotNone(self.UngueltigerBetragError, "Klasse 'UngueltigerBetragError' nicht gefunden!")
        self.assertIsNotNone(self.Bankkonto, "Klasse 'Bankkonto' nicht gefunden!")

    def test_01_exception_hierarchie(self):
        """Prüft, ob die Exception-Klassen korrekt voneinander und von Exception erben."""
        self.assertTrue(issubclass(self.BankFehler, Exception), "BankFehler muss von Exception erben!")
        self.assertTrue(issubclass(self.UngueltigePinError, self.BankFehler), "UngueltigePinError muss von BankFehler erben!")
        self.assertTrue(issubclass(self.KontoGesperrtError, self.BankFehler), "KontoGesperrtError muss von BankFehler erben!")
        self.assertTrue(issubclass(self.NichtGenugGuthabenError, self.BankFehler), "NichtGenugGuthabenError muss von BankFehler erben!")
        self.assertTrue(issubclass(self.UngueltigerBetragError, self.BankFehler), "UngueltigerBetragError muss von BankFehler erben!")

    def test_02_bankkonto_init(self):
        """Prüft Initialisierung des Bankkontos und Validierung des Startguthabens."""
        k = self.Bankkonto("Max Mustermann", "4321", 100.0)
        self.assertEqual(k.inhaber, "Max Mustermann")
        self.assertEqual(k.pin, "4321")
        self.assertEqual(k.kontostand, 100.0)
        self.assertFalse(k.gesperrt)
        self.assertEqual(k.fehlversuche, 0)

        # Negatives Startguthaben muss UngueltigerBetragError werfen
        with self.assertRaises(self.UngueltigerBetragError):
            self.Bankkonto("Schuldner", "1111", -50.0)

    def test_03_pin_pruefen_und_sperre(self):
        """Prüft PIN-Validierung, Fehlversuch-Zähler und automatische Kontosperre nach 3 Versuchen."""
        k = self.Bankkonto("Lisa", "1234", 200.0)

        # Richtige PIN
        self.assertTrue(k.pin_pruefen("1234"))
        self.assertEqual(k.fehlversuche, 0)

        # 1. Fehlversuch
        with self.assertRaises(self.UngueltigePinError):
            k.pin_pruefen("0000")
        self.assertEqual(k.fehlversuche, 1)
        self.assertFalse(k.gesperrt)

        # 2. Fehlversuch
        with self.assertRaises(self.UngueltigePinError):
            k.pin_pruefen("1111")
        self.assertEqual(k.fehlversuche, 2)
        self.assertFalse(k.gesperrt)

        # 3. Fehlversuch -> muss KontoGesperrtError werfen und Konto sperren
        with self.assertRaises(self.KontoGesperrtError):
            k.pin_pruefen("2222")
        self.assertEqual(k.fehlversuche, 3)
        self.assertTrue(k.gesperrt)

        # Weiterer Versuch auf gesperrtem Konto wirft sofort KontoGesperrtError (selbst bei richtiger PIN)
        with self.assertRaises(self.KontoGesperrtError):
            k.pin_pruefen("1234")

    def test_04_einzahlen(self):
        """Prüft Einzahlungen und Validierung von Beträgen."""
        k = self.Bankkonto("Tom", "1234", 50.0)
        neuer_stand = k.einzahlen(30.0)
        self.assertEqual(neuer_stand, 80.0)
        self.assertEqual(k.kontostand, 80.0)

        # Ungültige Beträge
        with self.assertRaises(self.UngueltigerBetragError):
            k.einzahlen(0.0)
        with self.assertRaises(self.UngueltigerBetragError):
            k.einzahlen(-20.0)

        # Einzahlen auf gesperrtem Konto
        k.sperren()
        with self.assertRaises(self.KontoGesperrtError):
            k.einzahlen(50.0)

    def test_05_abheben(self):
        """Prüft Abhebungen, PIN-Prüfung, Guthaben-Checks und Betragsprüfung."""
        k = self.Bankkonto("Sarah", "9876", 150.0)

        # Erfolgreiche Abhebung
        neuer_stand = k.abheben(50.0, "9876")
        self.assertEqual(neuer_stand, 100.0)
        self.assertEqual(k.kontostand, 100.0)

        # Falsche PIN beim Abheben
        with self.assertRaises(self.UngueltigePinError):
            k.abheben(20.0, "0000")

        # Zu viel Geld abheben (Nicht genug Guthaben)
        with self.assertRaises(self.NichtGenugGuthabenError):
            k.abheben(500.0, "9876")

        # Ungültiger Abhebebetrag
        with self.assertRaises(self.UngueltigerBetragError):
            k.abheben(-10.0, "9876")
        with self.assertRaises(self.UngueltigerBetragError):
            k.abheben(0.0, "9876")

    def test_06_sperren_und_entsperren(self):
        """Prüft manuelles Sperren und Entsperren mit Admin-Code."""
        k = self.Bankkonto("Felix", "1234", 100.0)
        k.sperren()
        self.assertTrue(k.gesperrt)

        # Entsperren mit falschem Passwort
        with self.assertRaises(self.UngueltigePinError):
            k.entsperren("FALSCH")
        self.assertTrue(k.gesperrt)

        # Entsperren mit korrektem Passwort
        erfolg = k.entsperren("ADMIN123")
        self.assertTrue(erfolg)
        self.assertFalse(k.gesperrt)
        self.assertEqual(k.fehlversuche, 0)

    def test_07_geldautomat_abheben_funktion(self):
        """Prüft die Geldautomat-Funktion mit try-except-else-finally."""
        self.assertIsNotNone(self.geldautomat_abheben, "Funktion 'geldautomat_abheben' fehlt!")

        k = self.Bankkonto("Elena", "5555", 200.0)

        # 1. Erfolgreicher Vorgang (else + finally aktiv)
        msg_erfolg = self.geldautomat_abheben(k, 50.0, "5555")
        self.assertIn("Auszahlung erfolgreich", msg_erfolg)
        self.assertIn("Bitte Karte entnehmen", msg_erfolg)
        self.assertEqual(k.kontostand, 150.0)

        # 2. Falsche PIN (except UngueltigePinError + finally aktiv)
        msg_pin_err = self.geldautomat_abheben(k, 50.0, "1111")
        self.assertIn("PIN-Fehler", msg_pin_err)
        self.assertIn("Bitte Karte entnehmen", msg_pin_err)

        # 3. Nicht genug Guthaben (except NichtGenugGuthabenError + finally aktiv)
        msg_deck_err = self.geldautomat_abheben(k, 1000.0, "5555")
        self.assertIn("Deckungs-Fehler", msg_deck_err)
        self.assertIn("Bitte Karte entnehmen", msg_deck_err)


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