import unittest
import sys
from pathlib import Path

# Sicherstellen, dass das aktuelle Verzeichnis im Python-Pfad liegt
sys.path.insert(0, str(Path(__file__).parent))

try:
    import aufgabe
except ImportError as e:
    raise ImportError(f"Konnte 'aufgabe.py' nicht importieren: {e}")


class TestKapitel15(unittest.TestCase):
    """
    Testsuite für Kapitel 15: Parameter (*args, **kwargs) & Eigene Container.
    """

    def setUp(self):
        self.berechne_gesamtsumme = getattr(aufgabe, "berechne_gesamtsumme", None)
        self.erstelle_profil = getattr(aufgabe, "erstelle_profil", None)
        self.packe_inventar = getattr(aufgabe, "packe_inventar", None)
        self.Gegenstand = getattr(aufgabe, "Gegenstand", None)
        self.Inventar = getattr(aufgabe, "Inventar", None)

        self.assertIsNotNone(self.berechne_gesamtsumme, "Funktion 'berechne_gesamtsumme' nicht gefunden!")
        self.assertIsNotNone(self.erstelle_profil, "Funktion 'erstelle_profil' nicht gefunden!")
        self.assertIsNotNone(self.packe_inventar, "Funktion 'packe_inventar' nicht gefunden!")
        self.assertIsNotNone(self.Gegenstand, "Klasse 'Gegenstand' nicht gefunden!")
        self.assertIsNotNone(self.Inventar, "Klasse 'Inventar' nicht gefunden!")

    # ==========================================================================
    # 1. *args & Rabatt-Funktion
    # ==========================================================================
    def test_01_berechne_gesamtsumme_args(self):
        """Prüft *args, leere Parameterliste, Rabattberechnung und Validierung."""
        # Keine Argumente
        self.assertEqual(self.berechne_gesamtsumme(), 0.0)

        # Einzelne und mehrere Zahlen
        self.assertEqual(self.berechne_gesamtsumme(42.5), 42.5)
        self.assertEqual(self.berechne_gesamtsumme(10.0, 20.0, 30.0), 60.0)
        self.assertEqual(self.berechne_gesamtsumme(5, 15, 25, 35, 20), 100.0)

        # Unpacking mit *liste
        zahlen_liste = [12.50, 7.50, 30.00]
        self.assertEqual(self.berechne_gesamtsumme(*zahlen_liste), 50.0)

        # Rabatt-Berechnungen
        self.assertEqual(self.berechne_gesamtsumme(100.0, 50.0, rabatt_prozent=10.0), 135.0)
        self.assertEqual(self.berechne_gesamtsumme(200.0, rabatt_prozent=50.0), 100.0)
        self.assertEqual(self.berechne_gesamtsumme(80.0, rabatt_prozent=100.0), 0.0)
        self.assertEqual(self.berechne_gesamtsumme(80.0, rabatt_prozent=0.0), 80.0)
        self.assertEqual(self.berechne_gesamtsumme(19.99, 29.99, rabatt_prozent=15.0), 42.48)

        # Ungültige Rabatte müssen ValueError werfen
        with self.assertRaises(ValueError, msg="Negativer Rabatt muss ValueError auslösen!"):
            self.berechne_gesamtsumme(100.0, rabatt_prozent=-5.0)

        with self.assertRaises(ValueError, msg="Rabatt > 100% muss ValueError auslösen!"):
            self.berechne_gesamtsumme(100.0, rabatt_prozent=105.0)

    # ==========================================================================
    # 2. **kwargs & Profil-Erstellung
    # ==========================================================================
    def test_02_erstelle_profil_kwargs(self):
        """Prüft **kwargs und Dictionary-Unpacking bei der Profil-Erstellung."""
        # Minimales Profil (nur Name)
        p1 = self.erstelle_profil("Arthur")
        self.assertEqual(p1, {"name": "Arthur"})

        # Profil mit verschiedenen Schlüsselwortargumenten
        p2 = self.erstelle_profil("Gandalf", klasse="Zauberer", stufe=99, mana=5000, aktiv=True)
        self.assertEqual(p2["name"], "Gandalf")
        self.assertEqual(p2["klasse"], "Zauberer")
        self.assertEqual(p2["stufe"], 99)
        self.assertEqual(p2["mana"], 5000)
        self.assertTrue(p2["aktiv"])

        # Unpacking mit **dict
        zusatz = {"leben": 100, "ruestung": 45, "gilde": "Gefaehrten"}
        p3 = self.erstelle_profil("Gimli", **zusatz)
        self.assertEqual(p3, {"name": "Gimli", "leben": 100, "ruestung": 45, "gilde": "Gefaehrten"})

    # ==========================================================================
    # 3. Klasse Gegenstand
    # ==========================================================================
    def test_03_gegenstand_klasse(self):
        """Prüft Gegenstand-Attribute, Validierung, __repr__, __str__ und __eq__."""
        schwert = self.Gegenstand("Eisenschwert", 3.5, 150)
        self.assertEqual(schwert.name, "Eisenschwert")
        self.assertEqual(schwert.gewicht, 3.5)
        self.assertEqual(schwert.wert, 150)

        # Standardwert
        kiesel = self.Gegenstand("Kieselstein", 0.1)
        self.assertEqual(kiesel.wert, 0)

        # Validierung negative Werte
        with self.assertRaises(ValueError, msg="Negatives Gewicht muss ValueError werfen"):
            self.Gegenstand("FehlerItem", -1.0, 10)

        with self.assertRaises(ValueError, msg="Negativer Wert muss ValueError werfen"):
            self.Gegenstand("FehlerItem", 1.0, -10)

        # Strings & Repräsentation
        self.assertIn("Eisenschwert", repr(schwert))
        self.assertIn("3.5", repr(schwert))
        self.assertIn("Eisenschwert", str(schwert))

        # Gleichheit __eq__
        gleiches_schwert = self.Gegenstand("Eisenschwert", 3.5, 150)
        anderes_schwert = self.Gegenstand("Eisenschwert", 4.0, 150)
        self.assertEqual(schwert, gleiches_schwert)
        self.assertNotEqual(schwert, anderes_schwert)
        self.assertNotEqual(schwert, "Kein Gegenstand")

    # ==========================================================================
    # 4. Klasse Inventar - Initialisierung & Gewichtsberechnung
    # ==========================================================================
    def test_04_inventar_init_und_gewicht(self):
        """Prüft Konstruktor, Maximalgewicht, Start-Items und Kapazitätsberechnung."""
        inv = self.Inventar(max_gewicht=15.0)
        self.assertEqual(inv.max_gewicht, 15.0)
        self.assertEqual(inv.gesamtgewicht, 0.0)
        self.assertEqual(inv.freie_kapazitaet, 15.0)

        # Ungültiges Maximalgewicht
        with self.assertRaises(ValueError):
            self.Inventar(max_gewicht=0.0)

        with self.assertRaises(ValueError):
            self.Inventar(max_gewicht=-10.0)

        # Init mit Start-Gegenständen
        g1 = self.Gegenstand("Buch", 1.2, 30)
        g2 = self.Gegenstand("Fackel", 0.8, 5)
        inv2 = self.Inventar(max_gewicht=10.0, gegenstaende=[g1, g2])
        self.assertEqual(inv2.gesamtgewicht, 2.0)
        self.assertEqual(inv2.freie_kapazitaet, 8.0)
        self.assertEqual(len(inv2), 2)

        # Start-Gegenstände zu schwer
        schwer = self.Gegenstand("Amboss", 50.0, 500)
        with self.assertRaises(ValueError, msg="Überladenes Startinventar muss ValueError werfen"):
            self.Inventar(max_gewicht=20.0, gegenstaende=[schwer])

    # ==========================================================================
    # 5. Inventar - hinzufuegen mit *args
    # ==========================================================================
    def test_05_inventar_hinzufuegen_args(self):
        """Prüft hinzufuegen mit variablen Argumenten (*args), Unpacking und Überladung."""
        inv = self.Inventar(max_gewicht=10.0)
        g1 = self.Gegenstand("Trank", 0.5, 20)
        g2 = self.Gegenstand("Brot", 0.3, 5)
        g3 = self.Gegenstand("Dolch", 1.2, 80)

        # Einzeln und mehrere mit *args
        inv.hinzufuegen(g1)
        self.assertEqual(inv.gesamtgewicht, 0.5)

        inv.hinzufuegen(g2, g3)
        self.assertEqual(inv.gesamtgewicht, 2.0)
        self.assertEqual(len(inv), 3)

        # Unpacking beim Aufruf von hinzufuegen
        nachschub = [self.Gegenstand("Pfeil", 0.1, 1), self.Gegenstand("Bogen", 2.0, 100)]
        inv.hinzufuegen(*nachschub)
        self.assertEqual(inv.gesamtgewicht, 4.1)
        self.assertEqual(len(inv), 5)

        # Überladung prüfen
        riesenstein = self.Gegenstand("Felsbrocken", 10.0, 0)
        with self.assertRaises(ValueError, msg="Überschreiten des Maximalgewichts muss ValueError werfen"):
            inv.hinzufuegen(riesenstein)

        # Ungültiger Typ
        with self.assertRaises(TypeError, msg="Nicht-Gegenstand muss TypeError werfen"):
            inv.hinzufuegen("Kein Gegenstand")

    # ==========================================================================
    # 6. Container-Dunder: __len__ und __iter__
    # ==========================================================================
    def test_06_container_len_und_iter(self):
        """Prüft len() und Iterierbarkeit (for item in inventar:)."""
        inv = self.Inventar(max_gewicht=20.0)
        self.assertEqual(len(inv), 0)

        items = [
            self.Gegenstand("Item 1", 1.0, 10),
            self.Gegenstand("Item 2", 2.0, 20),
            self.Gegenstand("Item 3", 3.0, 30),
        ]
        inv.hinzufuegen(*items)

        self.assertEqual(len(inv), 3)

        # Iteration mit for-Schleife & List Comprehension
        namen = [item.name for item in inv]
        self.assertEqual(namen, ["Item 1", "Item 2", "Item 3"])

        # Konvertierung zu list(inv)
        self.assertEqual(list(inv), items)

    # ==========================================================================
    # 7. Container-Dunder: __getitem__ (int Index & str Name-Suche)
    # ==========================================================================
    def test_07_container_getitem(self):
        """Prüft Index-Zugriff [i] und Namenssuche ['Name']."""
        g1 = self.Gegenstand("Heiltrank", 0.5, 25)
        g2 = self.Gegenstand("Langschwert", 4.0, 200)
        g3 = self.Gegenstand("Manatrank", 0.5, 30)

        inv = self.Inventar(max_gewicht=20.0, gegenstaende=[g1, g2, g3])

        # Integer-Index
        self.assertEqual(inv[0], g1)
        self.assertEqual(inv[1], g2)
        self.assertEqual(inv[-1], g3)

        with self.assertRaises(IndexError):
            _ = inv[10]

        # String-Namenssuche (case-insensitive)
        self.assertEqual(inv["Heiltrank"], g1)
        self.assertEqual(inv["heiltrank"], g1)
        self.assertEqual(inv["LANGSCHWERT"], g2)

        with self.assertRaises(KeyError, msg="Unbekannter Name muss KeyError werfen"):
            _ = inv["NichtImInventar"]

        # Ungültiger Key-Typ
        with self.assertRaises(TypeError):
            _ = inv[3.14]

    # ==========================================================================
    # 8. Container-Dunder: __setitem__
    # ==========================================================================
    def test_08_container_setitem(self):
        """Prüft Ersetzen per Index [i] = item und Gewichtsvalidierung."""
        g1 = self.Gegenstand("Heiltrank", 1.0, 25)
        g2 = self.Gegenstand("Holzschild", 3.0, 40)
        inv = self.Inventar(max_gewicht=10.0, gegenstaende=[g1, g2])
        self.assertEqual(inv.gesamtgewicht, 4.0)

        # Gültiger Austausch
        superschild = self.Gegenstand("Stahlschild", 5.0, 150)
        inv[1] = superschild
        self.assertEqual(inv[1], superschild)
        self.assertEqual(inv.gesamtgewicht, 6.0)

        # Austausch, der Maximalgewicht sprengt (6 - 1 + 8 = 13 > 10)
        riesenhammer = self.Gegenstand("Riesenhammer", 8.0, 300)
        with self.assertRaises(ValueError, msg="Austausch über Maximalgewicht muss ValueError werfen"):
            inv[0] = riesenhammer

        # Typ- & Index-Prüfung
        with self.assertRaises(TypeError):
            inv["kein_int"] = superschild

        with self.assertRaises(TypeError):
            inv[0] = "Kein Gegenstand"

        with self.assertRaises(IndexError):
            inv[10] = superschild

    # ==========================================================================
    # 9. Container-Dunder: __delitem__
    # ==========================================================================
    def test_09_container_delitem(self):
        """Prüft Löschen per del inv[i] und del inv['Name']."""
        g1 = self.Gegenstand("Heiltrank", 0.5, 20)
        g2 = self.Gegenstand("Schwert", 3.5, 120)
        g3 = self.Gegenstand("Fackel", 0.5, 5)
        inv = self.Inventar(max_gewicht=20.0, gegenstaende=[g1, g2, g3])
        self.assertEqual(len(inv), 3)
        self.assertEqual(inv.gesamtgewicht, 4.5)

        # Löschen per Integer-Index
        del inv[0]
        self.assertEqual(len(inv), 2)
        self.assertEqual(inv[0], g2)
        self.assertEqual(inv.gesamtgewicht, 4.0)

        # Löschen per Name (case-insensitive)
        del inv["fackel"]
        self.assertEqual(len(inv), 1)
        self.assertEqual(inv.gesamtgewicht, 3.5)

        # Fehler beim Löschen
        with self.assertRaises(KeyError):
            del inv["Unbekannt"]

        with self.assertRaises(IndexError):
            del inv[99]

    # ==========================================================================
    # 10. Container-Dunder: __contains__ (in Operator)
    # ==========================================================================
    def test_10_container_contains(self):
        """Prüft Mitgliedschaftsprüfung ('Item' in inv und obj in inv)."""
        schwert = self.Gegenstand("Eisenschwert", 3.0, 100)
        trank = self.Gegenstand("Heiltrank", 0.5, 25)
        fremdes_item = self.Gegenstand("Diamant", 0.1, 1000)

        inv = self.Inventar(max_gewicht=20.0, gegenstaende=[schwert, trank])

        # Suche nach String-Name
        self.assertTrue("Eisenschwert" in inv)
        self.assertTrue("eisenschwert" in inv)
        self.assertTrue("HEILTRANK" in inv)
        self.assertFalse("Diamant" in inv)
        self.assertFalse("Drachenei" in inv)

        # Suche nach Objekt-Referenz
        self.assertTrue(schwert in inv)
        self.assertTrue(trank in inv)
        self.assertFalse(fremdes_item in inv)

        # Suche nach Fremdtyp
        self.assertFalse(12345 in inv)

    # ==========================================================================
    # 11. Helper-Funktion packe_inventar
    # ==========================================================================
    def test_11_packe_inventar_helper(self):
        """Prüft packe_inventar mit *args und max_gewicht."""
        g1 = self.Gegenstand("Seil", 1.5, 15)
        g2 = self.Gegenstand("Proviant", 2.0, 10)
        
        rucksack = self.packe_inventar(g1, g2, max_gewicht=25.0)
        self.assertIsInstance(rucksack, self.Inventar)
        self.assertEqual(rucksack.max_gewicht, 25.0)
        self.assertEqual(len(rucksack), 2)
        self.assertEqual(rucksack.gesamtgewicht, 3.5)
        self.assertTrue("Seil" in rucksack)
        self.assertTrue("Proviant" in rucksack)


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