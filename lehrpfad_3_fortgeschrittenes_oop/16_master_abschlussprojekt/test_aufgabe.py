#!/usr/bin/env python3
"""
🧪 Umfassende Unittest-Suite für Kapitel 16 (Master-Abschlussprojekt)
=====================================================================
Prüft:
- Teil 1: Exception-Hierarchie & Vererbung
- Teil 2: Datenmodelle (Basisklasse Tier & Kindklassen Hund, Katze, Vogel)
- Teil 3: Polymorphie & Factory-Muster (Tier.from_dict)
- Teil 4: Geschäftslogik (Tierheim, Kapazität, Filter, Massenoperationen, Statistik)
- Teil 5: Persistenz (JSON Savegame-Roundtrip & CSV-Export)
- Teil 6: GUI-Controller (TierheimApp im Headless-Modus)
"""

import csv
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

# Aktuellen Ordner in sys.path einfügen
sys.path.insert(0, str(Path(__file__).parent))

try:
    import aufgabe
except ImportError as e:
    raise ImportError(f"Konnte 'aufgabe.py' nicht importieren: {e}")


class Test01Exceptions(unittest.TestCase):
    """Prüft die Exception-Klassen und deren Vererbungshierarchie."""

    def test_01_exceptions_existieren_und_erben(self):
        self.assertTrue(hasattr(aufgabe, "TierheimFehler"), "TierheimFehler fehlt!")
        self.assertTrue(hasattr(aufgabe, "ValidierungsFehler"), "ValidierungsFehler fehlt!")
        self.assertTrue(hasattr(aufgabe, "TierNichtGefundenFehler"), "TierNichtGefundenFehler fehlt!")
        self.assertTrue(hasattr(aufgabe, "KapazitaetUeberschrittenFehler"), "KapazitaetUeberschrittenFehler fehlt!")

        self.assertTrue(issubclass(aufgabe.TierheimFehler, Exception))
        self.assertTrue(issubclass(aufgabe.ValidierungsFehler, aufgabe.TierheimFehler))
        self.assertTrue(issubclass(aufgabe.TierNichtGefundenFehler, aufgabe.TierheimFehler))
        self.assertTrue(issubclass(aufgabe.KapazitaetUeberschrittenFehler, aufgabe.TierheimFehler))


class Test02TierBasisklasse(unittest.TestCase):
    """Prüft die Basisklasse Tier inkl. Validierung und Basis-Methoden."""

    def test_02_tier_initialisierung_und_attribute(self):
        t = aufgabe.Tier("Sammy", alter=4, gewicht=12.5, geimpft=False, hunger=40)
        self.assertEqual(t.name, "Sammy")
        self.assertEqual(t.alter, 4)
        self.assertAlmostEqual(t.gewicht, 12.5)
        self.assertFalse(t.geimpft)
        self.assertEqual(t.hunger, 40)

    def test_03_tier_validierung_leerer_name(self):
        with self.assertRaises(aufgabe.ValidierungsFehler):
            aufgabe.Tier("", alter=3, gewicht=5.0)
        with self.assertRaises(aufgabe.ValidierungsFehler):
            aufgabe.Tier("   ", alter=3, gewicht=5.0)

    def test_04_tier_validierung_negatives_alter(self):
        with self.assertRaises(aufgabe.ValidierungsFehler):
            aufgabe.Tier("Sammy", alter=-1, gewicht=5.0)

    def test_05_tier_validierung_ungueltiges_gewicht(self):
        with self.assertRaises(aufgabe.ValidierungsFehler):
            aufgabe.Tier("Sammy", alter=2, gewicht=0.0)
        with self.assertRaises(aufgabe.ValidierungsFehler):
            aufgabe.Tier("Sammy", alter=2, gewicht=-4.5)

    def test_06_tier_fuettern_und_clamping(self):
        t = aufgabe.Tier("Sammy", alter=2, gewicht=5.0, hunger=60)
        msg = t.fuettern(100)  # -20 Hunger
        self.assertEqual(t.hunger, 40)
        self.assertIn("Sammy", msg)

        # Überfüttern darf nicht unter 0 fallen
        t.fuettern(500)
        self.assertEqual(t.hunger, 0)

    def test_07_tier_impfen(self):
        t = aufgabe.Tier("Sammy", alter=2, gewicht=5.0, geimpft=False)
        erstes_mal = t.impfen()
        self.assertTrue(erstes_mal, "Erstmaliges Impfen sollte True zurückgeben.")
        self.assertTrue(t.geimpft)

        zweites_mal = t.impfen()
        self.assertFalse(zweites_mal, "Erneutes Impfen sollte False zurückgeben.")

    def test_08_tier_to_dict_und_str(self):
        t = aufgabe.Tier("Sammy", alter=2, gewicht=5.0, geimpft=True, hunger=30)
        d = t.to_dict()
        self.assertEqual(d.get("name"), "Sammy")
        self.assertEqual(d.get("alter"), 2)
        self.assertEqual(d.get("gewicht"), 5.0)
        self.assertEqual(d.get("geimpft"), True)
        self.assertEqual(d.get("hunger"), 30)
        self.assertIn("Sammy", str(t))


class Test03Kindklassen(unittest.TestCase):
    """Prüft Vererbung und Spezialisierungen für Hund, Katze und Vogel."""

    def test_09_hund_spezifisch(self):
        h = aufgabe.Hund("Bello", alter=3, gewicht=15.0, rasse="Labrador", geimpft=False, hunger=40)
        self.assertTrue(isinstance(h, aufgabe.Tier), "Hund muss von Tier erben!")
        self.assertEqual(h.rasse, "Labrador")
        self.assertFalse(h.gassigegangen)

        # Gassigehen
        msg = h.gassi_gehen(20)  # +4 Hunger
        self.assertTrue(h.gassigegangen)
        self.assertEqual(h.hunger, 44)
        self.assertIn("Bello", msg)

        # Laut
        laut = h.mache_laut()
        self.assertIn("Wuff", laut)

        # to_dict
        d = h.to_dict()
        self.assertEqual(d.get("art"), "Hund")
        self.assertEqual(d.get("rasse"), "Labrador")
        self.assertTrue(d.get("gassigegangen"))

    def test_10_katze_spezifisch(self):
        k = aufgabe.Katze("Luna", alter=2, gewicht=4.0, stubenrein=True, hunger=30)
        self.assertTrue(isinstance(k, aufgabe.Tier), "Katze muss von Tier erben!")
        self.assertTrue(k.stubenrein)
        self.assertFalse(k.kratzbaum_benutzt)

        # Kratzen
        k.kratzen()
        self.assertTrue(k.kratzbaum_benutzt)

        # Laut
        laut = k.mache_laut()
        self.assertIn("Miau", laut)

        # to_dict
        d = k.to_dict()
        self.assertEqual(d.get("art"), "Katze")
        self.assertTrue(d.get("stubenrein"))
        self.assertTrue(d.get("kratzbaum_benutzt"))

    def test_11_vogel_spezifisch(self):
        v = aufgabe.Vogel("Tweety", alter=1, gewicht=0.3, spannweite_cm=18.0, kann_sprechen=True, hunger=20)
        self.assertTrue(isinstance(v, aufgabe.Tier), "Vogel muss von Tier erben!")
        self.assertEqual(v.spannweite_cm, 18.0)
        self.assertTrue(v.kann_sprechen)

        # Fliegen
        v.fliegen(5)  # +10 Hunger
        self.assertEqual(v.hunger, 30)

        # Laut mit Sprechen
        laut = v.mache_laut()
        self.assertIn("Hallo Mensch", laut)

        # Vogel ohne Sprechen
        v2 = aufgabe.Vogel("Charly", alter=2, gewicht=0.4, kann_sprechen=False)
        laut2 = v2.mache_laut()
        self.assertIn("Tschilp", laut2)


class Test04PolymorphieUndFactory(unittest.TestCase):
    """Prüft das Factory-Pattern Tier.from_dict für alle Subklassen."""

    def test_12_factory_hund_wiederherstellen(self):
        data = {
            "art": "Hund",
            "name": "Rex",
            "alter": 5,
            "gewicht": 20.0,
            "rasse": "Schäferhund",
            "geimpft": True,
            "hunger": 35,
            "gassigegangen": True,
        }
        obj = aufgabe.Tier.from_dict(data)
        self.assertIsInstance(obj, aufgabe.Hund)
        self.assertEqual(obj.name, "Rex")
        self.assertEqual(obj.rasse, "Schäferhund")
        self.assertTrue(obj.geimpft)
        self.assertTrue(obj.gassigegangen)

    def test_13_factory_katze_wiederherstellen(self):
        data = {
            "art": "Katze",
            "name": "Minka",
            "alter": 3,
            "gewicht": 3.8,
            "stubenrein": True,
            "geimpft": False,
            "hunger": 50,
            "kratzbaum_benutzt": False,
        }
        obj = aufgabe.Tier.from_dict(data)
        self.assertIsInstance(obj, aufgabe.Katze)
        self.assertEqual(obj.name, "Minka")
        self.assertTrue(obj.stubenrein)

    def test_14_factory_vogel_wiederherstellen(self):
        data = {
            "art": "Vogel",
            "name": "Kiki",
            "alter": 2,
            "gewicht": 0.2,
            "spannweite_cm": 15.5,
            "kann_sprechen": True,
            "geimpft": True,
            "hunger": 10,
        }
        obj = aufgabe.Tier.from_dict(data)
        self.assertIsInstance(obj, aufgabe.Vogel)
        self.assertEqual(obj.name, "Kiki")
        self.assertEqual(obj.spannweite_cm, 15.5)
        self.assertTrue(obj.kann_sprechen)


class Test05TierheimGeschaeftslogik(unittest.TestCase):
    """Prüft die Model-Klasse Tierheim (Aufnahme, Entlassen, Filter, Statistik)."""

    def setUp(self):
        self.heim = aufgabe.Tierheim("Tierheim Test", max_kapazitaet=4)
        self.bello = aufgabe.Hund("Bello", alter=4, gewicht=15.0, geimpft=True, hunger=20)
        self.luna = aufgabe.Katze("Luna", alter=2, gewicht=4.0, geimpft=False, hunger=60)
        self.tweety = aufgabe.Vogel("Tweety", alter=1, gewicht=0.3, geimpft=False, hunger=70)

    def test_15_aufnahme_und_kapazitaet(self):
        self.heim.tier_aufnehmen(self.bello)
        self.heim.tier_aufnehmen(self.luna)
        self.heim.tier_aufnehmen(self.tweety)
        self.assertEqual(len(self.heim), 3)

        # 4. Tier aufnehmen (Max erreicht)
        h2 = aufgabe.Hund("Rocky", alter=1, gewicht=10.0)
        self.heim.tier_aufnehmen(h2)
        self.assertEqual(len(self.heim), 4)

        # 5. Tier aufnehmen -> KapazitaetUeberschrittenFehler
        h3 = aufgabe.Hund("Pluto", alter=2, gewicht=8.0)
        with self.assertRaises(aufgabe.KapazitaetUeberschrittenFehler):
            self.heim.tier_aufnehmen(h3)

    def test_16_tier_entlassen_und_suche(self):
        self.heim.tier_aufnehmen(self.bello)
        self.heim.tier_aufnehmen(self.luna)

        # Suchen
        gefunden = self.heim.finde_tier("bello")
        self.assertIsNotNone(gefunden)
        self.assertEqual(gefunden.name, "Bello")

        # Entlassen
        entlassen = self.heim.tier_entlassen("Bello")
        self.assertEqual(entlassen.name, "Bello")
        self.assertEqual(len(self.heim), 1)

        # Erneutes Entlassen -> TierNichtGefundenFehler
        with self.assertRaises(aufgabe.TierNichtGefundenFehler):
            self.heim.tier_entlassen("Bello")

    def test_17_filter_nach_art(self):
        self.heim.tier_aufnehmen(self.bello)
        self.heim.tier_aufnehmen(self.luna)
        self.heim.tier_aufnehmen(self.tweety)

        hunde = self.heim.filtriere_nach_art("Hund")
        self.assertEqual(len(hunde), 1)
        self.assertEqual(hunde[0].name, "Bello")

        katzen = self.heim.filtriere_nach_art("Katze")
        self.assertEqual(len(katzen), 1)
        self.assertEqual(katzen[0].name, "Luna")

        alle = self.heim.filtriere_nach_art("Alle")
        self.assertEqual(len(alle), 3)

    def test_18_filter_ungeimpft_und_hungrig(self):
        self.heim.tier_aufnehmen(self.bello)   # Geimpft, Hunger 20
        self.heim.tier_aufnehmen(self.luna)    # Ungeimpft, Hunger 60
        self.heim.tier_aufnehmen(self.tweety)  # Ungeimpft, Hunger 70

        ungeimpft = self.heim.ungeimpfte_tiere()
        self.assertEqual(len(ungeimpft), 2)

        hungrig = self.heim.hungrige_tiere(schwellenwert=50)
        self.assertEqual(len(hungrig), 2)

    def test_19_statistik_berechnungen(self):
        self.heim.tier_aufnehmen(self.bello)   # 4 J., 15.0 kg
        self.heim.tier_aufnehmen(self.luna)    # 2 J., 4.0 kg
        self.heim.tier_aufnehmen(self.tweety)  # 1 J., 0.3 kg

        # Alter: (4 + 2 + 1) / 3 = 2.333
        self.assertAlmostEqual(self.heim.durchschnittsalter(), 7.0 / 3.0, places=2)
        # Gewicht: 15.0 + 4.0 + 0.3 = 19.3
        self.assertAlmostEqual(self.heim.gesamtgewicht(), 19.3, places=2)

    def test_20_massenaktionen_fuettern_und_impfen(self):
        self.heim.tier_aufnehmen(self.bello)   # Geimpft, Hunger 20
        self.heim.tier_aufnehmen(self.luna)    # Ungeimpft, Hunger 60
        self.heim.tier_aufnehmen(self.tweety)  # Ungeimpft, Hunger 70

        # Alle impfen -> 2 neu geimpft
        frisch = self.heim.alle_impfen()
        self.assertEqual(frisch, 2)
        self.assertEqual(len(self.heim.ungeimpfte_tiere()), 0)

        # Alle füttern (100g -> -20 Hunger)
        ergebnisse = self.heim.alle_fuettern(100)
        self.assertEqual(len(ergebnisse), 3)
        self.assertEqual(self.bello.hunger, 0)
        self.assertEqual(self.luna.hunger, 40)
        self.assertEqual(self.tweety.hunger, 50)


class Test06Persistenz(unittest.TestCase):
    """Prüft JSON Savegame und CSV Export."""

    def test_21_json_speichern_und_laden(self):
        heim = aufgabe.Tierheim("Savegame Heim", max_kapazitaet=10)
        heim.tier_aufnehmen(aufgabe.Hund("Bello", 3, 14.5, rasse="Husky", geimpft=True))
        heim.tier_aufnehmen(aufgabe.Katze("Luna", 2, 4.2, stubenrein=True, geimpft=False))
        heim.tier_aufnehmen(aufgabe.Vogel("Tweety", 1, 0.3, spannweite_cm=19.0, kann_sprechen=True))

        with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as tf:
            pfad = tf.name

        try:
            heim.speichern_json(pfad)
            self.assertTrue(os.path.exists(pfad))

            # Neues leeres Heim lädt den Stand
            neues_heim = aufgabe.Tierheim("Leer", max_kapazitaet=5)
            neues_heim.laden_json(pfad)

            self.assertEqual(neues_heim.name, "Savegame Heim")
            self.assertEqual(len(neues_heim), 3)

            # Prüfen ob Typen erhalten blieben (Polymorphie)
            self.assertIsInstance(neues_heim.tiere[0], aufgabe.Hund)
            self.assertEqual(neues_heim.tiere[0].rasse, "Husky")
            self.assertIsInstance(neues_heim.tiere[1], aufgabe.Katze)
            self.assertIsInstance(neues_heim.tiere[2], aufgabe.Vogel)
            self.assertTrue(neues_heim.tiere[2].kann_sprechen)
        finally:
            if os.path.exists(pfad):
                os.remove(pfad)

    def test_22_csv_export(self):
        heim = aufgabe.Tierheim("CSV Heim", max_kapazitaet=10)
        heim.tier_aufnehmen(aufgabe.Hund("Bello", 3, 14.5, rasse="Husky", geimpft=True))
        heim.tier_aufnehmen(aufgabe.Katze("Luna", 2, 4.2, stubenrein=True, geimpft=False))

        with tempfile.NamedTemporaryFile(suffix=".csv", delete=False) as tf:
            pfad = tf.name

        try:
            heim.exportiere_csv(pfad)
            self.assertTrue(os.path.exists(pfad))

            with open(pfad, "r", encoding="utf-8") as f:
                reader = list(csv.reader(f))

            # Header prüfen
            self.assertGreaterEqual(len(reader), 3)
            self.assertEqual(reader[0], ["Art", "Name", "Alter", "Gewicht", "Geimpft", "Hunger", "Details"])

            # Erste Zeile (Bello)
            self.assertEqual(reader[1][0], "Hund")
            self.assertEqual(reader[1][1], "Bello")
        finally:
            if os.path.exists(pfad):
                os.remove(pfad)


class Test07GUIHeadless(unittest.TestCase):
    """Prüft die Benutzeroberfläche TierheimApp im Headless-Modus."""

    def setUp(self):
        tk_mod = getattr(aufgabe, "tk", None)
        self.assertIsNotNone(tk_mod, "tk Modul in aufgabe.py fehlt!")
        self.root = tk_mod.Tk()
        self.heim = aufgabe.Tierheim("GUI Test Heim", max_kapazitaet=10)
        self.heim.tier_aufnehmen(aufgabe.Hund("Bello", 3, 14.5, rasse="Beagle", geimpft=True))
        self.app = aufgabe.TierheimApp(self.root, self.heim)

    def test_23_gui_initialisierung_und_widgets(self):
        self.assertTrue(hasattr(self.app, "listbox_tiere"))
        self.assertTrue(hasattr(self.app, "label_status"))
        self.assertTrue(hasattr(self.app, "label_kapazitaet"))
        self.assertEqual(self.app.listbox_tiere.size(), 1)

    def test_24_gui_tier_aufnehmen_formular(self):
        # Formular mit neuem Hund befüllen
        self.app.var_art.set("Katze")
        self.app.var_name.set("Mimi")
        self.app.var_alter.set("1")
        self.app.var_gewicht.set("3.5")
        self.app.var_extra.set("ja")
        self.app.var_geimpft.set(False)

        # Aufnahmeklick auslösen
        self.app.tier_aufnehmen_klick()

        self.assertEqual(len(self.heim), 2)
        mimi = self.heim.finde_tier("Mimi")
        self.assertIsNotNone(mimi)
        self.assertIsInstance(mimi, aufgabe.Katze)

    def test_25_gui_validierungsfehler_abfangen(self):
        # Leerer Name -> Darf nicht abstürzen
        self.app.var_name.set("")
        try:
            self.app.tier_aufnehmen_klick()
        except Exception as e:
            self.fail(f"tier_aufnehmen_klick hat bei leerem Namen Exception nicht abgefangen: {e}")

        self.assertEqual(len(self.heim), 1, "Bestand darf sich bei Fehleingabe nicht verändern.")


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