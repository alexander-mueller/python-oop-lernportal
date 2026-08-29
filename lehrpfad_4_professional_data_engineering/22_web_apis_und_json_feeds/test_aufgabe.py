import unittest
import sys
import json
from pathlib import Path

# Sicherstellen, dass das aktuelle Verzeichnis im Python-Pfad liegt
sys.path.insert(0, str(Path(__file__).parent))

try:
    import aufgabe
except ImportError as e:
    raise ImportError(f"Konnte 'aufgabe.py' nicht importieren: {e}")


class TestKapitel22(unittest.TestCase):
    """
    Umfassende Offline-Testsuite für Modul 22 (REST-APIs, JSON-Feeds & Fehlerbehandlung).
    Nutzt realistische Mock-JSON-Datensätze (100% Pyodide- und Offline-kompatibel).
    """

    def setUp(self):
        self.parse_wetter_antwort = getattr(aufgabe, "parse_wetter_antwort", None)
        self.filtriere_aktien_kurse = getattr(aufgabe, "filtriere_aktien_kurse", None)
        self.formatiere_nachrichten_ticker = getattr(aufgabe, "formatiere_nachrichten_ticker", None)
        self.validiere_api_antwort = getattr(aufgabe, "validiere_api_antwort", None)
        self.WetterApiParser = getattr(aufgabe, "WetterApiParser", None)

        self.assertIsNotNone(self.parse_wetter_antwort, "Funktion 'parse_wetter_antwort' fehlt!")
        self.assertIsNotNone(self.filtriere_aktien_kurse, "Funktion 'filtriere_aktien_kurse' fehlt!")
        self.assertIsNotNone(self.formatiere_nachrichten_ticker, "Funktion 'formatiere_nachrichten_ticker' fehlt!")
        self.assertIsNotNone(self.validiere_api_antwort, "Funktion 'validiere_api_antwort' fehlt!")
        self.assertIsNotNone(self.WetterApiParser, "Klasse 'WetterApiParser' fehlt!")

    def test_01_parse_wetter_antwort_erfolg(self):
        """Prüft die Extraktion von Stadt, Temperatur, Luftfeuchtigkeit und Wetterlage."""
        mock_payload = json.dumps({
            "name": "Berlin",
            "coord": {"lon": 13.41, "lat": 52.52},
            "main": {
                "temp": 19.4,
                "feels_like": 18.9,
                "humidity": 68
            },
            "weather": [
                {
                    "id": 500,
                    "main": "Rain",
                    "description": "Mäßiger Regen",
                    "icon": "10d"
                }
            ]
        })

        ergebnis = self.parse_wetter_antwort(mock_payload)
        self.assertIsInstance(ergebnis, dict, "parse_wetter_antwort muss ein Dictionary zurückgeben!")
        self.assertEqual(ergebnis["stadt"], "Berlin")
        self.assertAlmostEqual(ergebnis["temperatur"], 19.4, places=1)
        self.assertEqual(ergebnis["luftfeuchtigkeit"], 68)
        self.assertEqual(ergebnis["wetterlage"], "Mäßiger Regen")

    def test_02_parse_wetter_antwort_fehlerbehandlung(self):
        """Prüft, dass bei ungültigem JSON oder fehlenden Feldern ein ValueError ausgelöst wird."""
        # 1. Korrupter JSON-String
        with self.assertRaises(ValueError, msg="Ungültiger JSON-String muss einen ValueError werfen!"):
            self.parse_wetter_antwort("{ungueltiges json: 42")

        # 2. Fehlendes 'main' Objekt
        unvollstaendig = json.dumps({"name": "Hamburg", "weather": [{"description": "Sonne"}]})
        with self.assertRaises(ValueError, msg="Fehlende Pflichtfelder müssen einen ValueError werfen!"):
            self.parse_wetter_antwort(unvollstaendig)

    def test_03_filtriere_aktien_kurse(self):
        """Prüft das Filtern von Aktienkursen über dem Schwellenwert."""
        feed = json.dumps({
            "timestamp": "2026-08-29T12:00:00Z",
            "aktien": [
                {"symbol": "NVDA", "kurs": 125.40, "waehrung": "USD"},
                {"symbol": "AAPL", "kurs": 220.10, "waehrung": "USD"},
                {"symbol": "PENNY", "kurs": 1.20, "waehrung": "EUR"},
                {"symbol": "MSFT", "kurs": 445.00, "waehrung": "USD"}
            ]
        })

        gefiltert = self.filtriere_aktien_kurse(feed, 200.0)
        self.assertIsInstance(gefiltert, list)
        self.assertEqual(len(gefiltert), 2, "Es sollten genau 2 Aktien >= 200.0 $ gefunden werden!")

        symbole = [a["symbol"] for a in gefiltert]
        self.assertIn("AAPL", symbole)
        self.assertIn("MSFT", symbole)
        self.assertNotIn("NVDA", symbole)
        self.assertNotIn("PENNY", symbole)

        # Ungültiges JSON liefert leere Liste
        self.assertEqual(self.filtriere_aktien_kurse("defektes json", 100.0), [])

    def test_04_formatiere_nachrichten_ticker(self):
        """Prüft die Formatierung der Schlagzeilen als durchgehender Ticker."""
        feed = json.dumps({
            "nachrichten": [
                {"titel": "Python 3.13 veröffentlicht", "ressort": "Tech"},
                {"titel": "DAX schließt im Plus", "ressort": "Wirtschaft"}
            ]
        })

        ticker = self.formatiere_nachrichten_ticker(feed)
        self.assertIsInstance(ticker, str)
        self.assertIn("[Tech] Python 3.13 veröffentlicht", ticker)
        self.assertIn("[Wirtschaft] DAX schließt im Plus", ticker)
        self.assertTrue(ticker.endswith("+++"))

        # Leere Liste
        leerer_feed = json.dumps({"nachrichten": []})
        self.assertEqual(self.formatiere_nachrichten_ticker(leerer_feed), "+++ Keine aktuellen Eilmeldungen +++")

        # Defektes JSON
        self.assertEqual(self.formatiere_nachrichten_ticker("###"), "+++ Fehler beim Laden des Nachrichten-Feeds +++")

    def test_05_validiere_api_antwort_200_ok(self):
        """Prüft erfolgreiche API-Antworten (Status 200)."""
        payload = json.dumps({"status": "success", "user_id": 42, "role": "admin"})
        status, daten = self.validiere_api_antwort(200, payload)

        self.assertTrue(status, "Statuscode 200 mit gültigem JSON muss True liefern!")
        self.assertIsInstance(daten, dict)
        self.assertEqual(daten["user_id"], 42)

    def test_06_validiere_api_antwort_200_bad_json(self):
        """Prüft Status 200 mit defektem JSON Payload (z.B. Verbindungsabbruch)."""
        status, msg = self.validiere_api_antwort(200, "<html>502 Bad Gateway</html>")
        self.assertFalse(status)
        self.assertEqual(msg, "Ungültiges JSON-Format")

    def test_07_validiere_api_antwort_fehler_status(self):
        """Prüft HTTP-Fehlercodes (404, 500) und das Extrahieren von Fehlermeldungen."""
        # 404 mit Fehler-JSON
        payload_404 = json.dumps({"error": "Benutzerprofil nicht gefunden", "code": 404})
        status_404, msg_404 = self.validiere_api_antwort(404, payload_404)
        self.assertFalse(status_404)
        self.assertIn("404", msg_404)
        self.assertIn("Benutzerprofil nicht gefunden", msg_404)

        # 500 ohne JSON
        status_500, msg_500 = self.validiere_api_antwort(500, "Internal Server Error")
        self.assertFalse(status_500)
        self.assertIn("500", msg_500)

    def test_08_wetter_api_parser_klasse(self):
        """Prüft die objektorientierte Klasse WetterApiParser."""
        gueltiges_json = json.dumps({
            "name": "Innsbruck",
            "main": {"temp": -3.5, "humidity": 80},
            "weather": [{"main": "Snow", "description": "Schneefall"}]
        })

        parser = self.WetterApiParser(gueltiges_json)
        self.assertTrue(parser.ist_gueltig())
        self.assertEqual(parser.get_stadt(), "Innsbruck")
        self.assertAlmostEqual(parser.get_temperatur(), -3.5, places=1)
        self.assertTrue(parser.ist_frostig(), "-3.5 °C muss als frostig erkannt werden!")

        # Ungültige Daten laden
        parser.lade_daten("kaputtes json")
        self.assertFalse(parser.ist_gueltig())
        self.assertIsNone(parser.get_temperatur())
        self.assertIsNone(parser.get_stadt())
        self.assertFalse(parser.ist_frostig())


if __name__ == "__main__":
    res = unittest.main(verbosity=2, exit=False)
    try:
        root_dir = Path(__file__).parent.parent.parent.resolve()
        sys.path.insert(0, str(root_dir))
        from gamification import report_single_chapter_result
        rel_pfad = f"{Path(__file__).parent.parent.name}/{Path(__file__).parent.name}"
        report_single_chapter_result(rel_pfad, res.result.wasSuccessful(), res.result.testsRun)
    except Exception:
        pass
    sys.exit(0 if res.result.wasSuccessful() else 1)
