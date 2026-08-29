import unittest
import sys
from pathlib import Path

# Sicherstellen, dass das aktuelle Verzeichnis im Python-Pfad liegt
sys.path.insert(0, str(Path(__file__).parent))

try:
    import aufgabe
except ImportError as e:
    raise ImportError(f"Konnte 'aufgabe.py' nicht importieren: {e}")


class TestKapitel18(unittest.TestCase):
    """
    Testsuite für Kapitel 18: Funktionale Programmierung & Pythonic Code.
    """

    def setUp(self):
        self.nummerierte_liste = getattr(aufgabe, "nummerierte_liste", None)
        self.kombiniere_katalog = getattr(aufgabe, "kombiniere_katalog", None)
        self.quadriere_und_filtere = getattr(aufgabe, "quadriere_und_filtere", None)
        self.sortiere_personen_nach_alter = getattr(aufgabe, "sortiere_personen_nach_alter", None)
        self.alle_volljaehrig = getattr(aufgabe, "alle_volljaehrig", None)
        self.mindestens_ein_treffer = getattr(aufgabe, "mindestens_ein_treffer", None)
        self.finde_extrem_produkt = getattr(aufgabe, "finde_extrem_produkt", None)

        self.assertIsNotNone(self.nummerierte_liste, "Funktion 'nummerierte_liste' nicht gefunden!")
        self.assertIsNotNone(self.kombiniere_katalog, "Funktion 'kombiniere_katalog' nicht gefunden!")
        self.assertIsNotNone(self.quadriere_und_filtere, "Funktion 'quadriere_und_filtere' nicht gefunden!")
        self.assertIsNotNone(self.sortiere_personen_nach_alter, "Funktion 'sortiere_personen_nach_alter' nicht gefunden!")
        self.assertIsNotNone(self.alle_volljaehrig, "Funktion 'alle_volljaehrig' nicht gefunden!")
        self.assertIsNotNone(self.mindestens_ein_treffer, "Funktion 'mindestens_ein_treffer' nicht gefunden!")

    # ==========================================================================
    # 1. Enumerate – Nummerierte Listen
    # ==========================================================================
    def test_01_nummerierte_liste(self):
        """Prüft enumerate() mit Standardstartwert 1 und benutzerdefiniertem Start."""
        sprachen = ["Python", "Java", "Rust"]
        ergebnis = self.nummerierte_liste(sprachen)
        self.assertEqual(ergebnis, ["1. Python", "2. Java", "3. Rust"])

        # Startwert 0
        ergebnis_0 = self.nummerierte_liste(["A", "B", "C"], start=0)
        self.assertEqual(ergebnis_0, ["0. A", "1. B", "2. C"])

        # Startwert 10
        ergebnis_10 = self.nummerierte_liste(["Erster", "Zweiter"], start=10)
        self.assertEqual(ergebnis_10, ["10. Erster", "11. Zweiter"])

        # Leere Liste
        self.assertEqual(self.nummerierte_liste([]), [])

    # ==========================================================================
    # 2. Zip – Katalog-Kombination
    # ==========================================================================
    def test_02_kombiniere_katalog(self):
        """Prüft zip() zur Kombination von Artikeln und Preisen."""
        artikel = ["Apfel", "Banane", "Orange"]
        preise = [0.99, 1.49, 1.99]
        katalog = self.kombiniere_katalog(artikel, preise)
        self.assertEqual(katalog, {"Apfel": 0.99, "Banane": 1.49, "Orange": 1.99})

        # Unterschiedliche Längen (zip schneidet ab)
        katalog_kurz = self.kombiniere_katalog(["Kaffee", "Tee"], [3.50, 2.80, 9.99])
        self.assertEqual(katalog_kurz, {"Kaffee": 3.50, "Tee": 2.80})

        # Leere Listen
        self.assertEqual(self.kombiniere_katalog([], []), {})

    # ==========================================================================
    # 3. Map & Filter & Lambda – Pipeline
    # ==========================================================================
    def test_03_quadriere_und_filtere(self):
        """Prüft Filterung ungerader Zahlen und deren Quadrierung."""
        # Gemischte Zahlen
        zahlen = [1, 2, 3, 4, 5, 6, 7]
        ergebnis = self.quadriere_und_filtere(zahlen)
        self.assertEqual(ergebnis, [1, 9, 25, 49])

        # Nur gerade Zahlen -> Leeres Ergebnis
        self.assertEqual(self.quadriere_und_filtere([2, 4, 6, 8]), [])

        # Negative ungerade Zahlen: (-3)^2 = 9
        self.assertEqual(self.quadriere_und_filtere([-3, -2, -1, 0, 1]), [9, 1, 1])

        # Leere Liste
        self.assertEqual(self.quadriere_und_filtere([]), [])

    # ==========================================================================
    # 4. Custom Sorting mit Key=Lambda
    # ==========================================================================
    def test_04_sortiere_personen_nach_alter(self):
        """Prüft benutzerdefiniertes Sortieren nach Alter (aufsteigend & absteigend)."""
        personen = [
            {"name": "Charlie", "alter": 45},
            {"name": "Alice", "alter": 30},
            {"name": "Bob", "alter": 22},
            {"name": "Dora", "alter": 18}
        ]

        # Aufsteigend
        sortiert_auf = self.sortiere_personen_nach_alter(personen, absteigend=False)
        namen_auf = [p["name"] for p in sortiert_auf]
        self.assertEqual(namen_auf, ["Dora", "Bob", "Alice", "Charlie"])

        # Absteigend
        sortiert_ab = self.sortiere_personen_nach_alter(personen, absteigend=True)
        namen_ab = [p["name"] for p in sortiert_ab]
        self.assertEqual(namen_ab, ["Charlie", "Alice", "Bob", "Dora"])

        # Original-Liste darf nicht verändert werden (neue Liste zurückgeben)
        self.assertIsNot(sortiert_auf, personen)

    # ==========================================================================
    # 5. all() – Volljährigkeit
    # ==========================================================================
    def test_05_alle_volljaehrig(self):
        """Prüft all() mit Standardmindestalter 18 und dynamischem Mindestalter."""
        # Alle >= 18
        self.assertTrue(self.alle_volljaehrig([18, 19, 25, 50]))

        # Mindestens einer < 18
        self.assertFalse(self.alle_volljaehrig([18, 17, 25, 50]))
        self.assertFalse(self.alle_volljaehrig([0]))

        # Anderes Mindestalter (z.B. 21)
        self.assertTrue(self.alle_volljaehrig([21, 25, 30], mindestalter=21))
        self.assertFalse(self.alle_volljaehrig([20, 25, 30], mindestalter=21))

        # Leere Liste ist trivial True in Python
        self.assertTrue(self.alle_volljaehrig([]))

    # ==========================================================================
    # 6. any() – Mindestens ein Treffer
    # ==========================================================================
    def test_06_mindestens_ein_treffer(self):
        """Prüft any() auf Wahrheitswerte."""
        self.assertTrue(self.mindestens_ein_treffer([False, False, True, False]))
        self.assertTrue(self.mindestens_ein_treffer([True, True, True]))
        self.assertFalse(self.mindestens_ein_treffer([False, False, False]))
        self.assertFalse(self.mindestens_ein_treffer([]))

    # ==========================================================================
    # 7. Bonus: Extremwert-Finder
    # ==========================================================================
    def test_07_finde_extrem_produkt(self):
        """Prüft das Finden von Extremwerten mit max/min und key=lambda."""
        if self.finde_extrem_produkt is None:
            return

        produkte = [
            {"titel": "Kugelschreiber", "preis": 2.50},
            {"titel": "Laptop", "preis": 1299.00},
            {"titel": "Kaffeetasse", "preis": 8.90},
            {"titel": "Monitor", "preis": 349.00}
        ]

        try:
            teuerstes = self.finde_extrem_produkt(produkte, modus="teuerstes")
            if teuerstes is not None:
                self.assertEqual(teuerstes["titel"], "Laptop")
                self.assertEqual(teuerstes["preis"], 1299.00)

            billigstes = self.finde_extrem_produkt(produkte, modus="billigstes")
            if billigstes is not None:
                self.assertEqual(billigstes["titel"], "Kugelschreiber")
                self.assertEqual(billigstes["preis"], 2.50)

            # Fehlerfälle
            with self.assertRaises(ValueError):
                self.finde_extrem_produkt([], modus="teuerstes")

            with self.assertRaises(ValueError):
                self.finde_extrem_produkt(produkte, modus="ungueltig")
        except NotImplementedError:
            pass


if __name__ == "__main__":
    unittest.main(verbosity=2)
