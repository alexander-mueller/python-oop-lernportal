import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

try:
    import aufgabe
except ImportError as e:
    raise ImportError(f"Konnte 'aufgabe.py' nicht importieren: {e}")


class TestKapitelG08(unittest.TestCase):

    def test_01_ist_palindrom(self):
        """Prüft die Palindrom-Erkennung unter Berücksichtigung von Leerzeichen und Groß/Klein."""
        # Echte Palindrome
        self.assertTrue(aufgabe.ist_palindrom("Anna"), "'Anna' ist ein Palindrom!")
        self.assertTrue(aufgabe.ist_palindrom("Lagerregal"), "'Lagerregal' ist ein Palindrom!")
        self.assertTrue(aufgabe.ist_palindrom("Dreh mal am Herd"), "'Dreh mal am Herd' sollte True liefern!")
        self.assertTrue(aufgabe.ist_palindrom("Rentner"), "'Rentner' ist ein Palindrom!")
        self.assertTrue(aufgabe.ist_palindrom("A"), "Ein Buchstabe ist ein Palindrom!")
        self.assertTrue(aufgabe.ist_palindrom(""), "Leerer Text gilt als Palindrom!")

        # Keine Palindrome
        self.assertFalse(aufgabe.ist_palindrom("Python"), "'Python' ist kein Palindrom!")
        self.assertFalse(aufgabe.ist_palindrom("Informatik"), "'Informatik' ist kein Palindrom!")
        self.assertFalse(aufgabe.ist_palindrom("Hallo Welt"), "'Hallo Welt' ist kein Palindrom!")

    def test_02_zaehle_vokale(self):
        """Prüft das Zählen von Vokalen inklusive Umlauten und Groß/Kleinschreibung."""
        self.assertEqual(aufgabe.zaehle_vokale("Python"), 1, "In 'Python' gibt es 1 Vokal ('o')!")
        self.assertEqual(aufgabe.zaehle_vokale("Käsebrot"), 3, "In 'Käsebrot' gibt es 3 Vokale ('ä', 'e', 'o')!")
        self.assertEqual(
            aufgabe.zaehle_vokale("SCHÖNES Wetter"),
            4,
            "In 'SCHÖNES Wetter' gibt es 4 Vokale ('Ö', 'E', 'e', 'e')!"
        )
        self.assertEqual(aufgabe.zaehle_vokale("Überflieger"), 5, "In 'Überflieger' gibt es 5 Vokale ('Ü', 'e', 'i', 'e', 'e')!")
        self.assertEqual(aufgabe.zaehle_vokale("HTML"), 0, "In 'HTML' gibt es 0 Vokale!")
        self.assertEqual(aufgabe.zaehle_vokale("Fly"), 0, "In 'Fly' gibt es 0 Vokale!")
        self.assertEqual(aufgabe.zaehle_vokale(""), 0, "Leerer String hat 0 Vokale!")

    def test_03_bereinige_benutzernamen(self):
        """Prüft die Bereinigung von Benutzernamen (strip, lowercase, Leerzeichen -> '_')."""
        self.assertEqual(
            aufgabe.bereinige_benutzernamen("  Max Mustermann  "),
            "max_mustermann",
            "Fehler bei '  Max Mustermann  '!"
        )
        self.assertEqual(
            aufgabe.bereinige_benutzernamen(" Super Coder 99 "),
            "super_coder_99",
            "Fehler bei ' Super Coder 99 '!"
        )
        self.assertEqual(
            aufgabe.bereinige_benutzernamen("LUKAS"),
            "lukas",
            "Fehler bei 'LUKAS'!"
        )
        self.assertEqual(
            aufgabe.bereinige_benutzernamen("anna"),
            "anna"
        )

    def test_04_woerter_zaehlen(self):
        """Prüft das Zählen von Wörtern bei verschiedenen Leerzeichen-Kombinationen."""
        self.assertEqual(aufgabe.woerter_zaehlen("Hallo Welt"), 2)
        self.assertEqual(
            aufgabe.woerter_zaehlen("   Python   macht   Spaß!   "),
            3,
            "Mehrere Leerzeichen sollten ignoriert werden!"
        )
        self.assertEqual(aufgabe.woerter_zaehlen("EinWort"), 1)
        self.assertEqual(aufgabe.woerter_zaehlen(""), 0, "Leerer Text muss 0 Wörter liefern!")
        self.assertEqual(aufgabe.woerter_zaehlen("     "), 0, "Nur Leerzeichen müssen 0 Wörter liefern!")

    def test_05_maskiere_kreditkarte(self):
        """Prüft die Maskierung von Kartennummern / sensiblen Strings."""
        self.assertEqual(
            aufgabe.maskiere_kreditkarte("1234567812345678"),
            "************5678",
            "Fehler: 16-stellige Nummer muss 12 Sterne + letzte 4 Ziffern haben!"
        )
        self.assertEqual(
            aufgabe.maskiere_kreditkarte("987654321"),
            "*****4321",
            "Fehler: 9-stellige Nummer muss 5 Sterne + letzte 4 Ziffern haben!"
        )
        # Randfälle: <= 4 Zeichen
        self.assertEqual(aufgabe.maskiere_kreditkarte("1234"), "1234")
        self.assertEqual(aufgabe.maskiere_kreditkarte("99"), "99")
        self.assertEqual(aufgabe.maskiere_kreditkarte(""), "")


if __name__ == "__main__":
    unittest.main(verbosity=2)
