import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

try:
    import aufgabe
except ImportError as e:
    raise ImportError(f"Konnte 'aufgabe.py' nicht importieren: {e}")


class TestKapitelG07(unittest.TestCase):

    def test_01_liste_umdrehen(self):
        """Prüft, ob eine Liste umgedreht wird, ohne das Original zu verändern."""
        original = [1, 2, 3, 4, 5]
        kopie_check = list(original)
        ergebnis = aufgabe.liste_umdrehen(original)

        self.assertEqual(
            ergebnis,
            [5, 4, 3, 2, 1],
            "Fehler: liste_umdrehen([1, 2, 3, 4, 5]) sollte [5, 4, 3, 2, 1] liefern!"
        )
        self.assertEqual(
            original,
            kopie_check,
            "Fehler: Die Original-Liste darf durch liste_umdrehen nicht verändert werden!"
        )

        # Leere Liste & Einzelelement
        self.assertEqual(aufgabe.liste_umdrehen([]), [], "Fehler bei leerer Liste!")
        self.assertEqual(aufgabe.liste_umdrehen(["A"]), ["A"], "Fehler bei einelementiger Liste!")

    def test_02_filtere_positive_zahlen(self):
        """Prüft das Filtern positiver Zahlen (Zahlen > 0)."""
        eingabe = [-10, 5.5, 0, -1, 42, 0.0, 7]
        ergebnis = aufgabe.filtere_positive_zahlen(eingabe)
        erwartet = [5.5, 42, 7]
        self.assertEqual(
            ergebnis,
            erwartet,
            f"Fehler: filtere_positive_zahlen({eingabe}) sollte {erwartet} liefern, war aber {ergebnis}!"
        )

        # Nur negative / Nullen
        self.assertEqual(
            aufgabe.filtere_positive_zahlen([-5, -1, 0]),
            [],
            "Fehler: Bei nur negativen Zahlen und 0 muss das Ergebnis [] sein!"
        )

        # Leere Liste
        self.assertEqual(aufgabe.filtere_positive_zahlen([]), [])

    def test_03_entferne_element(self):
        """Prüft das sichere Entfernen eines Elements aus einer Liste."""
        farben = ["Rot", "Grün", "Blau", "Gelb"]
        
        # Vorhandenes Element entfernen
        erfolg = aufgabe.entferne_element(farben, "Grün")
        self.assertTrue(erfolg, "Fehler: entferne_element sollte True zurückgeben, wenn Element existiert!")
        self.assertEqual(farben, ["Rot", "Blau", "Gelb"], "Fehler: 'Grün' wurde nicht aus der Liste entfernt!")

        # Nicht vorhandenes Element
        erfolg_fehlt = aufgabe.entferne_element(farben, "Schwarz")
        self.assertFalse(erfolg_fehlt, "Fehler: entferne_element sollte False zurückgeben, wenn Element nicht existiert!")
        self.assertEqual(farben, ["Rot", "Blau", "Gelb"], "Fehler: Liste darf sich bei fehlendem Element nicht ändern!")

        # Mehrfache Vorkommen: nur das erste soll entfernt werden
        zahlen = [1, 2, 2, 3]
        aufgabe.entferne_element(zahlen, 2)
        self.assertEqual(zahlen, [1, 2, 3], "Fehler: Bei Duplikaten sollte nur das erste Vorkommen entfernt werden!")

    def test_04_mittlere_elemente(self):
        """Prüft das Extrahieren der mittleren Elemente (ohne erstes und letztes)."""
        self.assertEqual(
            aufgabe.mittlere_elemente([10, 20, 30, 40, 50]),
            [20, 30, 40],
            "Fehler bei [10, 20, 30, 40, 50]!"
        )
        self.assertEqual(
            aufgabe.mittlere_elemente(["A", "B", "C"]),
            ["B"],
            "Fehler bei 3 Elementen!"
        )

        # Randfälle: <= 2 Elemente
        self.assertEqual(aufgabe.mittlere_elemente([1, 2]), [], "Fehler: Liste mit 2 Elementen muss [] liefern!")
        self.assertEqual(aufgabe.mittlere_elemente([1]), [], "Fehler: Liste mit 1 Element muss [] liefern!")
        self.assertEqual(aufgabe.mittlere_elemente([]), [], "Fehler: Leere Liste muss [] liefern!")

    def test_05_noten_durchschnitt_ohne_ausreisser(self):
        """Prüft die Durchschnittsberechnung ohne Best- und Schlechtnote."""
        noten = [1.0, 2.0, 3.0, 4.0, 5.0]
        original_noten = list(noten)
        schnitt = aufgabe.noten_durchschnitt_ohne_ausreisser(noten)

        self.assertAlmostEqual(
            schnitt,
            3.0,
            places=4,
            msg="Fehler: Notenschnitt für [1.0, 2.0, 3.0, 4.0, 5.0] ohne 1.0 und 5.0 sollte 3.0 sein!"
        )
        self.assertEqual(
            noten,
            original_noten,
            "Fehler: Die übergebene Liste 'noten' darf nicht mutiert werden!"
        )

        # Weiteres Notenbeispiel
        noten2 = [5.0, 1.0, 2.0, 3.0]  # min=1.0, max=5.0 -> rest=[2.0, 3.0] -> avg=2.5
        self.assertAlmostEqual(aufgabe.noten_durchschnitt_ohne_ausreisser(noten2), 2.5, places=4)

        # Randfälle: weniger als 3 Noten
        self.assertEqual(aufgabe.noten_durchschnitt_ohne_ausreisser([1.0, 2.0]), 0.0)
        self.assertEqual(aufgabe.noten_durchschnitt_ohne_ausreisser([3.0]), 0.0)
        self.assertEqual(aufgabe.noten_durchschnitt_ohne_ausreisser([]), 0.0)


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