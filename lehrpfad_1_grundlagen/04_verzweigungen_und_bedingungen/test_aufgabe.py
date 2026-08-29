import unittest
import sys
from pathlib import Path
import importlib.util

# Pfad zum aktuellen Kapitelverzeichnis
CHAPTER_DIR = Path(__file__).parent


def lade_modul(modul_name="aufgabe"):
    """Lädt das Modul (aufgabe oder musterloesung) isoliert aus dem Kapitelverzeichnis."""
    dateipfad = CHAPTER_DIR / f"{modul_name}.py"
    if not dateipfad.exists():
        raise FileNotFoundError(f"Datei '{dateipfad}' wurde nicht gefunden.")
    spec = importlib.util.spec_from_file_location(f"g04_{modul_name}", dateipfad)
    modul = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modul)
    return modul


class TestKapitelG04(unittest.TestCase):
    """
    Testsuite für Kapitel G04: Verzweigungen & Bedingungen
    Überprüft if/elif/else-Verzweigungen, Grenzwerte und logische Operatoren.
    """

    @classmethod
    def setUpClass(cls):
        cls.target_modul = getattr(cls, "modul_name", "aufgabe")
        try:
            cls.mod = lade_modul(cls.target_modul)
        except SyntaxError as e:
            cls.mod = None
            cls.import_error = f"SyntaxError in '{cls.target_modul}.py': {e}"
        except Exception as e:
            cls.mod = None
            cls.import_error = f"Fehler beim Laden von '{cls.target_modul}.py': {e}"

    def _get_modul(self):
        if getattr(self, "mod", None) is None:
            err = getattr(self, "import_error", f"{self.target_modul}.py konnte nicht geladen werden")
            self.fail(f"❌ {err}")
        return self.mod

    def test_01_ticket_preis_alle_tarife(self):
        """Prüft TODO 1: ticket_preis(alter, ist_student) für alle Altersgruppen."""
        mod = self._get_modul()
        self.assertTrue(
            hasattr(mod, "ticket_preis"),
            "Fehler: Funktion 'ticket_preis' fehlt in aufgabe.py!"
        )

        # Kindertarif (< 12 Jahre): 6.00 €
        self.assertEqual(mod.ticket_preis(5, False), 6.0, "Alter 5 sollte 6.00 € kosten (Kindertarif)!")
        self.assertEqual(mod.ticket_preis(11, False), 6.0, "Alter 11 sollte 6.00 € kosten (Kindertarif)!")
        self.assertEqual(mod.ticket_preis(11, True), 6.0, "Kinder zahlen immer 6.00 €!")

        # Seniorentarif (>= 65 Jahre): 8.50 €
        self.assertEqual(mod.ticket_preis(65, False), 8.5, "Alter 65 sollte 8.50 € kosten (Seniorentarif)!")
        self.assertEqual(mod.ticket_preis(80, False), 8.5, "Alter 80 sollte 8.50 € kosten (Seniorentarif)!")
        self.assertEqual(mod.ticket_preis(70, True), 8.5, "Senioren ab 65 zahlen 8.50 €!")

        # Studenten- / Ermäßigungstarif (12 <= alter < 65 und ist_student == True): 9.50 €
        self.assertEqual(mod.ticket_preis(12, True), 9.5, "Schüler/Student mit 12 Jahren sollte 9.50 € kosten!")
        self.assertEqual(mod.ticket_preis(22, True), 9.5, "Student mit 22 Jahren sollte 9.50 € kosten!")
        self.assertEqual(mod.ticket_preis(64, True), 9.5, "Student mit 64 Jahren sollte 9.50 € kosten!")

        # Regulärer Erwachsenentarif (12 <= alter < 65 und ist_student == False): 12.00 €
        self.assertEqual(mod.ticket_preis(12, False), 12.0, "Regulärer Preis ab 12 Jahren ohne Ermäßigung ist 12.00 €!")
        self.assertEqual(mod.ticket_preis(35, False), 12.0, "Erwachsener (35) ohne Ermäßigung sollte 12.00 € zahlen!")
        self.assertEqual(mod.ticket_preis(64, False), 12.0, "Erwachsener (64) ohne Ermäßigung sollte 12.00 € zahlen!")

    def test_02_schulnote_text_grenzwerte(self):
        """Prüft TODO 2: schulnote_text(punkte) inklusive aller Grenzwerte."""
        mod = self._get_modul()
        self.assertTrue(
            hasattr(mod, "schulnote_text"),
            "Fehler: Funktion 'schulnote_text' fehlt in aufgabe.py!"
        )

        # 90..100: "Sehr gut"
        self.assertEqual(mod.schulnote_text(100), "Sehr gut", "100 Punkte müssen 'Sehr gut' ergeben!")
        self.assertEqual(mod.schulnote_text(90), "Sehr gut", "Genau 90 Punkte müssen 'Sehr gut' ergeben (Grenzwert)!")

        # 75..89: "Gut"
        self.assertEqual(mod.schulnote_text(89), "Gut", "89 Punkte müssen 'Gut' ergeben!")
        self.assertEqual(mod.schulnote_text(75), "Gut", "Genau 75 Punkte müssen 'Gut' ergeben (Grenzwert)!")

        # 60..74: "Befriedigend"
        self.assertEqual(mod.schulnote_text(74), "Befriedigend", "74 Punkte müssen 'Befriedigend' ergeben!")
        self.assertEqual(mod.schulnote_text(60), "Befriedigend", "Genau 60 Punkte müssen 'Befriedigend' ergeben (Grenzwert)!")

        # 50..59: "Genügend"
        self.assertEqual(mod.schulnote_text(59), "Genügend", "59 Punkte müssen 'Genügend' ergeben!")
        self.assertEqual(mod.schulnote_text(50), "Genügend", "Genau 50 Punkte müssen 'Genügend' ergeben (Grenzwert)!")

        # 0..49: "Nicht genügend"
        self.assertEqual(mod.schulnote_text(49), "Nicht genügend", "49 Punkte müssen 'Nicht genügend' ergeben!")
        self.assertEqual(mod.schulnote_text(0), "Nicht genügend", "0 Punkte müssen 'Nicht genügend' ergeben!")

        # Ungültig (< 0 oder > 100)
        self.assertEqual(mod.schulnote_text(-1), "Ungültige Punktezahl", "-1 Punkt muss 'Ungültige Punktezahl' ergeben!")
        self.assertEqual(mod.schulnote_text(101), "Ungültige Punktezahl", "101 Punkte müssen 'Ungültige Punktezahl' ergeben!")

    def test_03_ist_schaltjahr_regeln(self):
        """Prüft TODO 3: ist_schaltjahr(jahr) mit allen Gregorianischen Ausnahmen."""
        mod = self._get_modul()
        self.assertTrue(
            hasattr(mod, "ist_schaltjahr"),
            "Fehler: Funktion 'ist_schaltjahr' fehlt in aufgabe.py!"
        )

        # Normale Schaltjahre (durch 4 teilbar, nicht durch 100):
        self.assertTrue(mod.ist_schaltjahr(2024), "2024 ist ein Schaltjahr (durch 4 teilbar)!")
        self.assertTrue(mod.ist_schaltjahr(2020), "2020 ist ein Schaltjahr!")
        self.assertTrue(mod.ist_schaltjahr(2016), "2016 ist ein Schaltjahr!")

        # Normale Nicht-Schaltjahre (nicht durch 4 teilbar):
        self.assertFalse(mod.ist_schaltjahr(2023), "2023 ist kein Schaltjahr!")
        self.assertFalse(mod.ist_schaltjahr(2025), "2025 ist kein Schaltjahr!")

        # Säkularjahre / Jahrhundert-Regel:
        # Durch 100 teilbar, aber NICHT durch 400 -> KEIN Schaltjahr!
        self.assertFalse(mod.ist_schaltjahr(1900), "1900 ist KEIN Schaltjahr (durch 100 teilbar, aber nicht durch 400)!")
        self.assertFalse(mod.ist_schaltjahr(2100), "2100 ist KEIN Schaltjahr (durch 100 teilbar, aber nicht durch 400)!")
        self.assertFalse(mod.ist_schaltjahr(1800), "1800 ist KEIN Schaltjahr!")

        # 400er-Regel:
        # Durch 400 teilbar -> IST ein Schaltjahr!
        self.assertTrue(mod.ist_schaltjahr(2000), "2000 IST ein Schaltjahr (durch 400 teilbar)!")
        self.assertTrue(mod.ist_schaltjahr(2400), "2400 IST ein Schaltjahr (durch 400 teilbar)!")
        self.assertTrue(mod.ist_schaltjahr(1600), "1600 IST ein Schaltjahr (durch 400 teilbar)!")

    def test_04_kann_achterbahn_fahren(self):
        """Prüft TODO 4: kann_achterbahn_fahren(groesse_cm, begleitung_erwachsen)."""
        mod = self._get_modul()
        self.assertTrue(
            hasattr(mod, "kann_achterbahn_fahren"),
            "Fehler: Funktion 'kann_achterbahn_fahren' fehlt in aufgabe.py!"
        )

        # Ab 140 cm: Immer erlaubt (auch ohne Begleitung)
        self.assertTrue(mod.kann_achterbahn_fahren(140, False), "Genau 140 cm darf alleine fahren!")
        self.assertTrue(mod.kann_achterbahn_fahren(155, False), "155 cm darf alleine fahren!")
        self.assertTrue(mod.kann_achterbahn_fahren(140, True), "140 cm mit Begleitung darf natürlich auch fahren!")

        # 120 bis 139 cm: NUR mit erwachsener Begleitung
        self.assertTrue(mod.kann_achterbahn_fahren(120, True), "120 cm mit Begleitung ist erlaubt!")
        self.assertTrue(mod.kann_achterbahn_fahren(135, True), "135 cm mit Begleitung ist erlaubt!")
        self.assertFalse(mod.kann_achterbahn_fahren(120, False), "120 cm OHNE Begleitung ist verboten!")
        self.assertFalse(mod.kann_achterbahn_fahren(139, False), "139 cm OHNE Begleitung ist verboten!")

        # Unter 120 cm: Grundsätzlich verboten (auch mit Begleitung)
        self.assertFalse(mod.kann_achterbahn_fahren(119, True), "119 cm ist zu klein, auch mit Begleitung!")
        self.assertFalse(mod.kann_achterbahn_fahren(119, False), "119 cm ohne Begleitung ist verboten!")
        self.assertFalse(mod.kann_achterbahn_fahren(95, True), "95 cm ist zu klein!")


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