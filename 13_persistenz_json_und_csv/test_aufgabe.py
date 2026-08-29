import unittest
import sys
import json
import csv
import tempfile
from pathlib import Path

# Sicherstellen, dass das aktuelle Verzeichnis im Python-Pfad liegt
sys.path.insert(0, str(Path(__file__).parent))

try:
    import aufgabe
except ImportError as e:
    raise ImportError(f"Konnte 'aufgabe.py' nicht importieren: {e}")


class TestKapitel13(unittest.TestCase):

    def setUp(self):
        self.Spieler = getattr(aufgabe, "Spieler", None)
        self.Spielstand = getattr(aufgabe, "Spielstand", None)

        self.assertIsNotNone(self.Spieler, "Klasse 'Spieler' nicht gefunden!")
        self.assertIsNotNone(self.Spielstand, "Klasse 'Spielstand' nicht gefunden!")

    def test_01_spieler_init_und_serialisierung(self):
        """Prüft Spieler-Initialisierung, to_dict() und from_dict()."""
        s = self.Spieler("Geralt", 20, 8500, ["Silberschwert", "Trank"])
        self.assertEqual(s.name, "Geralt")
        self.assertEqual(s.level, 20)
        self.assertEqual(s.punkte, 8500)
        self.assertEqual(s.inventar, ["Silberschwert", "Trank"])

        # to_dict
        d = s.to_dict()
        self.assertIsInstance(d, dict, "to_dict() muss ein Dictionary zurückgeben!")
        self.assertEqual(d["name"], "Geralt")
        self.assertEqual(d["level"], 20)
        self.assertEqual(d["punkte"], 8500)
        self.assertEqual(d["inventar"], ["Silberschwert", "Trank"])

        # from_dict
        reconstructed = self.Spieler.from_dict(d)
        self.assertEqual(reconstructed.name, s.name)
        self.assertEqual(reconstructed.level, s.level)
        self.assertEqual(reconstructed.punkte, s.punkte)
        self.assertEqual(reconstructed.inventar, s.inventar)

    def test_02_spielstand_management(self):
        """Prüft Hinzufügen, Suchen und Ermittlung des besten Spielers."""
        spielstand = self.Spielstand("Turnier 2026")
        self.assertIsNone(spielstand.bester_spieler())

        s1 = self.Spieler("Alice", 5, 1200)
        s2 = self.Spieler("Bob", 8, 3400)
        s3 = self.Spieler("Charlie", 6, 2100)

        spielstand.spieler_hinzufuegen(s1)
        spielstand.spieler_hinzufuegen(s2)
        spielstand.spieler_hinzufuegen(s3)

        self.assertEqual(len(spielstand.spieler_liste), 3)
        self.assertEqual(spielstand.bester_spieler().name, "Bob")
        self.assertEqual(spielstand.spieler_suchen("Alice").level, 5)
        self.assertIsNone(spielstand.spieler_suchen("Unbekannt"))

    def test_03_json_speichern_und_laden(self):
        """Prüft Speichern und Laden eines Spielstands im JSON-Format über temporäre Dateien."""
        with tempfile.TemporaryDirectory() as tmpdir:
            json_file = Path(tmpdir) / "savegame.json"

            original_stand = self.Spielstand("Episches RPG")
            original_stand.spieler_hinzufuegen(self.Spieler("Zelda", 30, 9999, ["Bogen", "Rubin"]))
            original_stand.spieler_hinzufuegen(self.Spieler("Link", 25, 7500, ["Master-Schwert"]))

            # Speichern
            original_stand.speichern_als_json(json_file)
            self.assertTrue(json_file.exists(), "JSON-Datei wurde nicht erstellt!")

            # Rohinhalt der JSON prüfen
            with open(json_file, "r", encoding="utf-8") as f:
                rohdialog = json.load(f)
            self.assertEqual(rohdialog["titel"], "Episches RPG")
            self.assertEqual(len(rohdialog["spieler"]), 2)
            self.assertEqual(rohdialog["spieler"][0]["name"], "Zelda")

            # In neues Spielstand-Objekt laden
            geladener_stand = self.Spielstand()
            geladener_stand.laden_aus_json(json_file)

            self.assertEqual(geladener_stand.titel, "Episches RPG")
            self.assertEqual(len(geladener_stand.spieler_liste), 2)
            self.assertEqual(geladener_stand.spieler_liste[0].name, "Zelda")
            self.assertEqual(geladener_stand.spieler_liste[0].inventar, ["Bogen", "Rubin"])
            self.assertEqual(geladener_stand.spieler_liste[1].punkte, 7500)

    def test_04_csv_export(self):
        """Prüft den Export der Spieler-Tabelle als CSV-Datei."""
        with tempfile.TemporaryDirectory() as tmpdir:
            csv_file = Path(tmpdir) / "export.csv"

            stand = self.Spielstand("Liga")
            stand.spieler_hinzufuegen(self.Spieler("Mario", 10, 5000, ["Pilz", "Stern", "Blume"]))
            stand.spieler_hinzufuegen(self.Spieler("Luigi", 8, 3200, ["Pilz"]))

            stand.exportiere_als_csv(csv_file)
            self.assertTrue(csv_file.exists(), "CSV-Datei wurde nicht erstellt!")

            with open(csv_file, "r", newline="", encoding="utf-8") as f:
                reader = list(csv.DictReader(f))

            self.assertEqual(len(reader), 2)
            self.assertEqual(reader[0]["name"], "Mario")
            self.assertEqual(reader[0]["level"], "10")
            self.assertEqual(reader[0]["punkte"], "5000")
            self.assertEqual(reader[0]["inventar_anzahl"], "3")

            self.assertEqual(reader[1]["name"], "Luigi")
            self.assertEqual(reader[1]["inventar_anzahl"], "1")

    def test_05_csv_import(self):
        """Prüft den Import von Daten aus einer CSV-Datei."""
        with tempfile.TemporaryDirectory() as tmpdir:
            csv_file = Path(tmpdir) / "import_test.csv"

            # Manuell CSV-Datei vorbereiten
            with open(csv_file, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=["name", "level", "punkte", "inventar_anzahl"])
                writer.writeheader()
                writer.writerow({"name": "Peach", "level": "12", "punkte": "4400", "inventar_anzahl": "0"})
                writer.writerow({"name": "Toad", "level": "5", "punkte": "1500", "inventar_anzahl": "0"})

            stand = self.Spielstand("Neue Runde")
            anzahl = stand.importiere_aus_csv(csv_file)

            self.assertEqual(anzahl, 2)
            self.assertEqual(len(stand.spieler_liste), 2)
            self.assertEqual(stand.spieler_liste[0].name, "Peach")
            self.assertEqual(stand.spieler_liste[0].level, 12)
            self.assertEqual(stand.spieler_liste[0].punkte, 4400)


if __name__ == "__main__":
    unittest.main(verbosity=2)
