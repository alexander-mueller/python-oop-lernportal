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
    spec = importlib.util.spec_from_file_location(f"g03_{modul_name}", dateipfad)
    modul = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modul)
    return modul


class TestKapitelG03(unittest.TestCase):
    """
    Testsuite für Kapitel G03: Interaktive Ein- & Ausgabe
    Überprüft f-String-Formatierungen, Berechnungen und Typkonvertierungen.
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

    def test_01_begruessungs_text(self):
        """Prüft TODO 1: begruessungs_text(name, stadt)."""
        mod = self._get_modul()
        self.assertTrue(
            hasattr(mod, "begruessungs_text"),
            "Fehler: Funktion 'begruessungs_text' fehlt in aufgabe.py!"
        )

        ergebnis1 = mod.begruessungs_text("Anna", "Wien")
        erwartet1 = "Hallo Anna, herzlich willkommen in Wien!"
        self.assertEqual(
            ergebnis1,
            erwartet1,
            f"\n❌ Falsche Begrüßung!\nErwartet: '{erwartet1}'\nErhalten: '{ergebnis1}'"
        )

        ergebnis2 = mod.begruessungs_text("Maximilian", "München")
        erwartet2 = "Hallo Maximilian, herzlich willkommen in München!"
        self.assertEqual(
            ergebnis2,
            erwartet2,
            f"\n❌ Falsche Begrüßung!\nErwartet: '{erwartet2}'\nErhalten: '{ergebnis2}'"
        )

    def test_02_berechne_alter_in_tagen(self):
        """Prüft TODO 2: berechne_alter_in_tagen(jahre)."""
        mod = self._get_modul()
        self.assertTrue(
            hasattr(mod, "berechne_alter_in_tagen"),
            "Fehler: Funktion 'berechne_alter_in_tagen' fehlt in aufgabe.py!"
        )

        self.assertEqual(mod.berechne_alter_in_tagen(18), 6570, "18 Jahre * 365 sollte 6570 Tage ergeben!")
        self.assertEqual(mod.berechne_alter_in_tagen(1), 365, "1 Jahr * 365 sollte 365 Tage ergeben!")
        self.assertEqual(mod.berechne_alter_in_tagen(0), 0, "0 Jahre * 365 sollte 0 Tage ergeben!")
        self.assertEqual(mod.berechne_alter_in_tagen(25), 9125, "25 Jahre * 365 sollte 9125 Tage ergeben!")

    def test_03_formatiere_rechnungsposten(self):
        """Prüft TODO 3: formatiere_rechnungsposten(artikel, anzahl, einzelpreis)."""
        mod = self._get_modul()
        self.assertTrue(
            hasattr(mod, "formatiere_rechnungsposten"),
            "Fehler: Funktion 'formatiere_rechnungsposten' fehlt in aufgabe.py!"
        )

        # Test 1: Kaffee
        erg1 = mod.formatiere_rechnungsposten("Kaffee", 3, 2.5)
        erw1 = "3x Kaffee à 2.50 € = 7.50 €"
        self.assertEqual(
            erg1,
            erw1,
            f"\n❌ Formatierungsfehler bei Rechnungsposten!\nErwartet: '{erw1}'\nErhalten: '{erg1}'\n💡 Tipp: Achte auf ':.2f' für zwei Nachkommastellen bei beiden Preisen!"
        )

        # Test 2: Buch
        erg2 = mod.formatiere_rechnungsposten("Buch", 1, 19.99)
        erw2 = "1x Buch à 19.99 € = 19.99 €"
        self.assertEqual(
            erg2,
            erw2,
            f"\n❌ Formatierungsfehler bei Rechnungsposten!\nErwartet: '{erw2}'\nErhalten: '{erg2}'"
        )

        # Test 3: Semmel (Rundung / Nullen am Ende z.B. 0.40 € und 2.00 €)
        erg3 = mod.formatiere_rechnungsposten("Semmel", 5, 0.4)
        erw3 = "5x Semmel à 0.40 € = 2.00 €"
        self.assertEqual(
            erg3,
            erw3,
            f"\n❌ Formatierungsfehler bei Rechnungsposten!\nErwartet: '{erw3}'\nErhalten: '{erg3}'"
        )

    def test_04_steckbrief_und_bmi(self):
        """Prüft TODO 4: steckbrief(name, groesse_m, gewicht_kg)."""
        mod = self._get_modul()
        self.assertTrue(
            hasattr(mod, "steckbrief"),
            "Fehler: Funktion 'steckbrief' fehlt in aufgabe.py!"
        )

        # Test 1: Alex (75 kg / (1.80^2) = 23.1481... -> 23.1)
        erg1 = mod.steckbrief("Alex", 1.80, 75.0)
        erw1 = "Steckbrief: Alex | Größe: 1.80 m | Gewicht: 75.0 kg | BMI: 23.1"
        self.assertEqual(
            erg1,
            erw1,
            f"\n❌ Formatierungsfehler im Steckbrief!\nErwartet: '{erw1}'\nErhalten: '{erg1}'\n💡 Formel: BMI = gewicht / (groesse ** 2) mit ':.1f'"
        )

        # Test 2: Mia (58.5 kg / (1.65^2) = 21.4876... -> 21.5)
        erg2 = mod.steckbrief("Mia", 1.65, 58.5)
        erw2 = "Steckbrief: Mia | Größe: 1.65 m | Gewicht: 58.5 kg | BMI: 21.5"
        self.assertEqual(
            erg2,
            erw2,
            f"\n❌ Formatierungsfehler im Steckbrief!\nErwartet: '{erw2}'\nErhalten: '{erg2}'"
        )


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