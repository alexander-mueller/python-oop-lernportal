import unittest
import sys
from pathlib import Path

# Sicherstellen, dass das aktuelle Verzeichnis im Modulpfad ist
sys.path.insert(0, str(Path(__file__).parent))

try:
    import aufgabe
except ImportError as e:
    raise ImportError(f"Konnte 'aufgabe.py' nicht importieren: {e}")


class TestKapitelG09(unittest.TestCase):

    def test_01_woerter_haeufigkeit_grundlagen(self):
        """Prüft woerter_haeufigkeit mit einfachen Wörtern."""
        self.assertTrue(
            hasattr(aufgabe, "woerter_haeufigkeit"),
            "Fehler: Funktion 'woerter_haeufigkeit' fehlt in aufgabe.py!"
        )
        text = "Apfel Banane Apfel Birne Banane Apfel"
        ergebnis = aufgabe.woerter_haeufigkeit(text)
        erwartet = {"apfel": 3, "banane": 2, "birne": 1}
        self.assertIsInstance(ergebnis, dict, "Fehler: Rückgabewert muss ein Dictionary (dict) sein!")
        self.assertEqual(
            ergebnis,
            erwartet,
            f"Fehler bei woerter_haeufigkeit: Erwartet {erwartet}, aber erhalten: {ergebnis}"
        )

    def test_02_woerter_haeufigkeit_satzzeichen_und_grossklein(self):
        """Prüft woerter_haeufigkeit bei Groß-/Kleinschreibung und Satzzeichen."""
        text = "Hallo, hallo! HALLO... ist da wer? Ja, wer da ist."
        ergebnis = aufgabe.woerter_haeufigkeit(text)
        erwartet = {"hallo": 3, "ist": 2, "da": 2, "wer": 2, "ja": 1}
        self.assertEqual(
            ergebnis,
            erwartet,
            f"Fehler: Satzzeichen oder Groß-/Kleinschreibung nicht korrekt behandelt!\nErwartet: {erwartet}\nErhalten: {ergebnis}"
        )

    def test_03_woerter_haeufigkeit_leerer_text(self):
        """Prüft woerter_haeufigkeit bei leerem String."""
        ergebnis = aufgabe.woerter_haeufigkeit("")
        self.assertEqual(ergebnis, {}, "Fehler: Ein leerer Text sollte ein leeres Dictionary {} liefern.")

    def test_04_telefonbuch_suche_gefunden(self):
        """Prüft telefonbuch_suche, wenn der Name existiert."""
        self.assertTrue(
            hasattr(aufgabe, "telefonbuch_suche"),
            "Fehler: Funktion 'telefonbuch_suche' fehlt in aufgabe.py!"
        )
        buch = {
            "Anna": "0171-123456",
            "Ben": "0160-987654",
            "Clara": "0151-555666"
        }
        self.assertEqual(
            aufgabe.telefonbuch_suche(buch, "Anna"),
            "0171-123456",
            "Fehler: Telefonnummer für 'Anna' wurde nicht korrekt zurückgegeben."
        )
        self.assertEqual(
            aufgabe.telefonbuch_suche(buch, "Clara"),
            "0151-555666",
            "Fehler: Telefonnummer für 'Clara' wurde nicht korrekt zurückgegeben."
        )

    def test_05_telefonbuch_suche_nicht_gefunden(self):
        """Prüft telefonbuch_suche mit .get() Fallback bei unbekanntem Namen."""
        buch = {"Anna": "0171-123456"}
        ergebnis = aufgabe.telefonbuch_suche(buch, "Daniel")
        self.assertEqual(
            ergebnis,
            "Nicht gefunden",
            f"Fehler: Unbekannter Name muss 'Nicht gefunden' liefern, ergab aber: {ergebnis}"
        )
        # Auch bei leerem Buch
        self.assertEqual(
            aufgabe.telefonbuch_suche({}, "Niemand"),
            "Nicht gefunden",
            "Fehler: Suche in leerem Telefonbuch muss 'Nicht gefunden' liefern."
        )

    def test_06_gemeinsame_interessen(self):
        """Prüft die Mengenoperation Schnittmenge (intersection / &)."""
        self.assertTrue(
            hasattr(aufgabe, "gemeinsame_interessen"),
            "Fehler: Funktion 'gemeinsame_interessen' fehlt in aufgabe.py!"
        )
        a = {"Gaming", "Klettern", "Musik"}
        b = {"Kochen", "Gaming", "Musik", "Lesen"}
        ergebnis = aufgabe.gemeinsame_interessen(a, b)
        erwartet = {"Gaming", "Musik"}
        self.assertIsInstance(ergebnis, set, "Fehler: Rückgabewert muss ein Set (Menge) sein!")
        self.assertEqual(
            ergebnis,
            erwartet,
            f"Fehler bei gemeinsame_interessen: Erwartet {erwartet}, erhalten: {ergebnis}"
        )

    def test_07_gemeinsame_interessen_disjunkt(self):
        """Prüft gemeinsame_interessen ohne Überschneidung."""
        a = {"Tennis", "Schwimmen"}
        b = {"Schach", "Malen"}
        ergebnis = aufgabe.gemeinsame_interessen(a, b)
        self.assertEqual(
            ergebnis,
            set(),
            "Fehler: Bei disjunkten Mengen muss ein leeres Set() zurückgegeben werden."
        )

    def test_08_entferne_duplikate_behalte_reihenfolge(self):
        """Prüft, ob Duplikate entfernt und die ursprüngliche Reihenfolge erhalten wird."""
        self.assertTrue(
            hasattr(aufgabe, "entferne_duplikate_behalte_reihenfolge"),
            "Fehler: Funktion 'entferne_duplikate_behalte_reihenfolge' fehlt in aufgabe.py!"
        )
        eingabe = [1, 3, 2, 3, 1, 4, 2, 5]
        ergebnis = aufgabe.entferne_duplikate_behalte_reihenfolge(eingabe)
        erwartet = [1, 3, 2, 4, 5]
        self.assertIsInstance(ergebnis, list, "Fehler: Rückgabewert muss eine Liste sein!")
        self.assertEqual(
            ergebnis,
            erwartet,
            f"Fehler: Reihenfolge oder Duplikat-Filterung weicht ab!\nErwartet: {erwartet}\nErhalten: {ergebnis}"
        )

    def test_09_entferne_duplikate_strings_und_randfaelle(self):
        """Prüft Duplikatentfernung mit Strings und leerer Liste."""
        eingabe = ["Apfel", "Banane", "Apfel", "Birne", "Banane", "Orange"]
        ergebnis = aufgabe.entferne_duplikate_behalte_reihenfolge(eingabe)
        erwartet = ["Apfel", "Banane", "Birne", "Orange"]
        self.assertEqual(ergebnis, erwartet)

        # Leere Liste
        self.assertEqual(aufgabe.entferne_duplikate_behalte_reihenfolge([]), [])


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