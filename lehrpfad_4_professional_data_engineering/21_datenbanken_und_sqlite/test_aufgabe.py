import unittest
import sys
import sqlite3
from pathlib import Path

# Sicherstellen, dass das aktuelle Verzeichnis im Python-Pfad liegt
sys.path.insert(0, str(Path(__file__).parent))

try:
    import aufgabe
except ImportError as e:
    raise ImportError(f"Konnte 'aufgabe.py' nicht importieren: {e}")


class TestKapitel21(unittest.TestCase):
    """
    Umfassende Testsuite für Modul 21 (SQLite Datenbanken & Persistenz).
    Nutzt isolierte In-Memory-Datenbanken (:memory:) für maximale Geschwindigkeit.
    """

    def setUp(self):
        self.KundenDatenbank = getattr(aufgabe, "KundenDatenbank", None)
        self.assertIsNotNone(self.KundenDatenbank, "Klasse 'KundenDatenbank' nicht in aufgabe.py gefunden!")
        # Jede Testmethode erhält eine frische, isolierte In-Memory-Datenbank
        self.db = self.KundenDatenbank(":memory:")

    def tearDown(self):
        if hasattr(self, "db") and self.db:
            self.db.schliessen()

    def test_01_tabelle_und_initialisierung(self):
        """Prüft, ob die Tabelle 'kunden' mit den korrekten Spalten angelegt wurde."""
        cursor = self.db.conn.cursor()
        cursor.execute("PRAGMA table_info(kunden)")
        spalten = {row[1]: row[2].upper() for row in cursor.fetchall()}

        self.assertIn("id", spalten, "Spalte 'id' fehlt in Tabelle 'kunden'!")
        self.assertIn("name", spalten, "Spalte 'name' fehlt in Tabelle 'kunden'!")
        self.assertIn("email", spalten, "Spalte 'email' fehlt in Tabelle 'kunden'!")
        self.assertIn("guthaben", spalten, "Spalte 'guthaben' fehlt in Tabelle 'kunden'!")

    def test_02_kunde_hinzufuegen(self):
        """Prüft das Einfügen von Kunden und die Rückgabe der neuen ID."""
        id1 = self.db.kunde_hinzufuegen("Alice Schmidt", "alice@example.com", 150.0)
        self.assertIsInstance(id1, int, "kunde_hinzufuegen muss die int-ID zurückgeben!")
        self.assertEqual(id1, 1, "Der erste Kunde sollte ID 1 erhalten!")

        id2 = self.db.kunde_hinzufuegen("Bob Müller", "bob@example.com", 75.50)
        self.assertEqual(id2, 2, "Der zweite Kunde sollte ID 2 erhalten!")

        # Prüfen, ob Datensätze direkt in der DB liegen
        c = self.db.conn.cursor()
        c.execute("SELECT COUNT(*) FROM kunden")
        anzahl = c.fetchone()[0]
        self.assertEqual(anzahl, 2, "Es sollten genau 2 Kunden in der Datenbank vorhanden sein!")

    def test_03_kunde_suchen_nach_id(self):
        """Prüft die Suche nach existierenden und nicht-existierenden Kunden."""
        id_neu = self.db.kunde_hinzufuegen("Clara Oswald", "clara@tardis.org", 250.0)

        # Existierender Kunde
        kunde = self.db.kunde_suchen_nach_id(id_neu)
        self.assertIsInstance(kunde, dict, "kunde_suchen_nach_id muss ein Dict zurückgeben!")
        self.assertEqual(kunde["id"], id_neu)
        self.assertEqual(kunde["name"], "Clara Oswald")
        self.assertEqual(kunde["email"], "clara@tardis.org")
        self.assertAlmostEqual(kunde["guthaben"], 250.0, places=2)

        # Nicht existierender Kunde
        unbekannt = self.db.kunde_suchen_nach_id(9999)
        self.assertIsNone(unbekannt, "kunde_suchen_nach_id muss None zurückgeben, wenn ID nicht existiert!")

    def test_04_guthaben_aufladen(self):
        """Prüft das Aufladen von Guthaben und Validierung von Beträgen."""
        kid = self.db.kunde_hinzufuegen("David Miller", "david@web.de", 100.0)

        # Gültiges Aufladen
        erfolg = self.db.guthaben_aufladen(kid, 50.0)
        self.assertTrue(erfolg, "guthaben_aufladen sollte True zurückgeben bei erfolgreicher Aktualisierung!")

        kunde = self.db.kunde_suchen_nach_id(kid)
        self.assertAlmostEqual(kunde["guthaben"], 150.0, places=2)

        # Ungültiger Betrag (<= 0)
        erfolg_negativ = self.db.guthaben_aufladen(kid, -20.0)
        self.assertFalse(erfolg_negativ, "guthaben_aufladen darf bei Beträgen <= 0 keine Buchung durchführen (False)!")

        erfolg_null = self.db.guthaben_aufladen(kid, 0.0)
        self.assertFalse(erfolg_null, "guthaben_aufladen darf bei Betrag 0.0 nicht erfolgreich sein!")

        # Nicht-existierende Kunden-ID
        erfolg_fremd = self.db.guthaben_aufladen(8888, 50.0)
        self.assertFalse(erfolg_fremd, "guthaben_aufladen sollte False zurückgeben, wenn Kunden-ID nicht existiert!")

    def test_05_kunden_mit_mindestguthaben(self):
        """Prüft die Abfrage und Sortierung von Kunden nach Mindestguthaben."""
        self.db.kunde_hinzufuegen("Sparfuchs", "sparfuchs@bank.de", 10.0)
        self.db.kunde_hinzufuegen("Mittelstand", "mittel@bank.de", 500.0)
        self.db.kunde_hinzufuegen("Vip Kunde", "vip@bank.de", 1200.0)
        self.db.kunde_hinzufuegen("Grossanleger", "investor@bank.de", 2500.0)

        # Filter ab 500.0
        ergebnis = self.db.kunden_mit_mindestguthaben(500.0)
        self.assertIsInstance(ergebnis, list, "kunden_mit_mindestguthaben muss eine Liste zurückgeben!")
        self.assertEqual(len(ergebnis), 3, "Es sollten genau 3 Kunden >= 500€ Guthaben haben!")

        # Prüfung der absteigenden Sortierung (Grossanleger > Vip Kunde > Mittelstand)
        self.assertEqual(ergebnis[0]["name"], "Grossanleger")
        self.assertEqual(ergebnis[1]["name"], "Vip Kunde")
        self.assertEqual(ergebnis[2]["name"], "Mittelstand")

        # Zu hohe Schwelle -> leere Liste
        keine = self.db.kunden_mit_mindestguthaben(10000.0)
        self.assertEqual(keine, [], "Sollte leere Liste zurückgeben, wenn kein Kunde die Schwelle erreicht!")

    def test_06_kunde_loeschen(self):
        """Prüft das Löschen von Kunden aus der Datenbank."""
        kid = self.db.kunde_hinzufuegen("Ex-Kunde", "ex@alt.de", 0.0)

        loesch_erfolg = self.db.kunde_loeschen(kid)
        self.assertTrue(loesch_erfolg, "kunde_loeschen sollte True zurückgeben, wenn Kunde existierte!")

        # Erneute Suche muss None liefern
        kunde = self.db.kunde_suchen_nach_id(kid)
        self.assertIsNone(kunde, "Gelöschter Kunde darf über kunde_suchen_nach_id nicht mehr gefunden werden!")

        # Zweites Löschen derselben ID muss False liefern
        loesch_nochmal = self.db.kunde_loeschen(kid)
        self.assertFalse(loesch_nochmal, "kunde_loeschen sollte False liefern, wenn ID nicht existiert!")

    def test_07_sql_injection_schutz(self):
        """Prüft, ob parametrisierte Queries vor böswilligen SQL-Injections schützen."""
        boeser_name = "Robert'); DROP TABLE kunden;--"
        kid = self.db.kunde_hinzufuegen(boeser_name, "bobby@tables.com", 100.0)

        kunde = self.db.kunde_suchen_nach_id(kid)
        self.assertIsNotNone(kunde, "Kunde mit SQL-Injection-String im Namen sollte als regulärer Text gespeichert werden!")
        self.assertEqual(kunde["name"], boeser_name)

        # Tabelle 'kunden' muss intakt sein!
        c = self.db.conn.cursor()
        c.execute("SELECT COUNT(*) FROM kunden")
        self.assertEqual(c.fetchone()[0], 1, "Tabelle 'kunden' wurde trotz SQL-Injection-Versuch nicht zerstört!")


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
