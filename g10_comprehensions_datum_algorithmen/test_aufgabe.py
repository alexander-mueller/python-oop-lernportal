import unittest
import sys
from datetime import datetime, date, timedelta
from pathlib import Path

# Sicherstellen, dass das aktuelle Verzeichnis im Modulpfad ist
sys.path.insert(0, str(Path(__file__).parent))

try:
    import aufgabe
except ImportError as e:
    raise ImportError(f"Konnte 'aufgabe.py' nicht importieren: {e}")


class TestKapitelG10(unittest.TestCase):

    def test_01_quadratzahlen_gerade(self):
        """Prüft, ob quadratzahlen_gerade Quadrate der geraden Zahlen liefert."""
        self.assertTrue(
            hasattr(aufgabe, "quadratzahlen_gerade"),
            "Fehler: Funktion 'quadratzahlen_gerade' fehlt in aufgabe.py!"
        )
        eingabe = [1, 2, 3, 4, 5, 6]
        ergebnis = aufgabe.quadratzahlen_gerade(eingabe)
        erwartet = [4, 16, 36]
        self.assertIsInstance(ergebnis, list, "Fehler: Rückgabewert muss eine Liste sein!")
        self.assertEqual(
            ergebnis,
            erwartet,
            f"Fehler: Erwartet {erwartet}, aber erhalten: {ergebnis}"
        )

        # Nur ungerade Zahlen
        self.assertEqual(aufgabe.quadratzahlen_gerade([1, 3, 5, 7]), [])
        # Leere Liste
        self.assertEqual(aufgabe.quadratzahlen_gerade([]), [])

    def test_02_filtriere_lange_woerter(self):
        """Prüft, ob filtriere_lange_woerter Wörter nach Mindestlänge filtert."""
        self.assertTrue(
            hasattr(aufgabe, "filtriere_lange_woerter"),
            "Fehler: Funktion 'filtriere_lange_woerter' fehlt in aufgabe.py!"
        )
        woerter = ["Python", "ist", "eine", "tolle", "Sprache"]
        ergebnis = aufgabe.filtriere_lange_woerter(woerter, 5)
        erwartet = ["Python", "tolle", "Sprache"]
        self.assertIsInstance(ergebnis, list, "Fehler: Rückgabewert muss eine Liste sein!")
        self.assertEqual(
            ergebnis,
            erwartet,
            f"Fehler: Erwartet {erwartet}, aber erhalten: {ergebnis}"
        )

        # Hohe Mindestlänge (kein Treffer)
        self.assertEqual(aufgabe.filtriere_lange_woerter(woerter, 20), [])
        # Mindestlänge 0 (alle Wörter)
        self.assertEqual(aufgabe.filtriere_lange_woerter(woerter, 0), woerter)

    def test_03_tage_bis_datum(self):
        """Prüft die Datumsberechnung mit strptime und timedelta."""
        self.assertTrue(
            hasattr(aufgabe, "tage_bis_datum"),
            "Fehler: Funktion 'tage_bis_datum' fehlt in aufgabe.py!"
        )
        heute = date.today()

        # 1. Heute
        heute_str = heute.strftime("%Y-%m-%d")
        self.assertEqual(aufgabe.tage_bis_datum(heute_str), 0, "Fehler: Tage bis heute muss 0 sein!")

        # 2. In 14 Tagen
        zukunft = heute + timedelta(days=14)
        zukunft_str = zukunft.strftime("%Y-%m-%d")
        self.assertEqual(
            aufgabe.tage_bis_datum(zukunft_str),
            14,
            f"Fehler: Tage bis {zukunft_str} sollte 14 sein!"
        )

        # 3. Vor 5 Tagen
        vergangenheit = heute - timedelta(days=5)
        vergangenheit_str = vergangenheit.strftime("%Y-%m-%d")
        self.assertEqual(
            aufgabe.tage_bis_datum(vergangenheit_str),
            -5,
            f"Fehler: Tage bis {vergangenheit_str} sollte -5 sein!"
        )

    def test_04_formatiere_deutsches_datum(self):
        """Prüft die Formatierung mit .strftime in DD.MM.YYYY."""
        self.assertTrue(
            hasattr(aufgabe, "formatiere_deutsches_datum"),
            "Fehler: Funktion 'formatiere_deutsches_datum' fehlt in aufgabe.py!"
        )
        # Test mit date Objekt
        d1 = date(2026, 12, 24)
        self.assertEqual(
            aufgabe.formatiere_deutsches_datum(d1),
            "24.12.2026",
            "Fehler: date(2026, 12, 24) sollte als '24.12.2026' formatiert werden."
        )

        # Test mit datetime Objekt und einstelligen Ziffern (Prüfung führender Nullen)
        dt = datetime(2025, 3, 4, 15, 30)
        self.assertEqual(
            aufgabe.formatiere_deutsches_datum(dt),
            "04.03.2025",
            "Fehler: Führende Nullen beachten! datetime(2025, 3, 4) -> '04.03.2025'."
        )

    def test_05_finde_aelteste_person(self):
        """Prüft die Algorithmus-Suche nach der ältesten Person."""
        self.assertTrue(
            hasattr(aufgabe, "finde_aelteste_person"),
            "Fehler: Funktion 'finde_aelteste_person' fehlt in aufgabe.py!"
        )
        personen = [
            {"name": "Anna", "alter": 25},
            {"name": "Ben", "alter": 32},
            {"name": "Clara", "alter": 19}
        ]
        self.assertEqual(
            aufgabe.finde_aelteste_person(personen),
            "Ben",
            "Fehler: 'Ben' (32) ist die älteste Person."
        )

        # Einzelne Person
        self.assertEqual(
            aufgabe.finde_aelteste_person([{"name": "Opa Wilhelm", "alter": 88}]),
            "Opa Wilhelm"
        )

        # Leere Liste
        self.assertEqual(
            aufgabe.finde_aelteste_person([]),
            "",
            "Fehler: Bei leerer Personenliste soll ein leerer String '' zurückgegeben werden."
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
