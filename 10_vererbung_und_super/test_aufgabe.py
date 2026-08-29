import unittest
import sys
from pathlib import Path

# Sicherstellen, dass das Kapitel-Verzeichnis im Suchpfad liegt
sys.path.insert(0, str(Path(__file__).parent))

try:
    import aufgabe
except ImportError as e:
    raise ImportError(f"Konnte 'aufgabe.py' nicht importieren: {e}")


class TestKapitel10(unittest.TestCase):

    def setUp(self):
        self.Fahrzeug = getattr(aufgabe, "Fahrzeug", None)
        self.Auto = getattr(aufgabe, "Auto", None)
        self.ElektroAuto = getattr(aufgabe, "ElektroAuto", None)
        self.Lkw = getattr(aufgabe, "Lkw", None)

        self.assertIsNotNone(self.Fahrzeug, "Klasse 'Fahrzeug' nicht gefunden!")
        self.assertIsNotNone(self.Auto, "Klasse 'Auto' nicht gefunden!")
        self.assertIsNotNone(self.ElektroAuto, "Klasse 'ElektroAuto' nicht gefunden!")
        self.assertIsNotNone(self.Lkw, "Klasse 'Lkw' nicht gefunden!")

    def test_01_fahrzeug_init_und_fahren(self):
        """Prüft Basisklasse Fahrzeug: Initialisierung und Fahren."""
        f = self.Fahrzeug("VW", "Golf", 2020, 25000.0)
        self.assertEqual(f.marke, "VW")
        self.assertEqual(f.modell, "Golf")
        self.assertEqual(f.baujahr, 2020)
        self.assertEqual(f.grundpreis, 25000.0)
        self.assertEqual(f.kilometerstand, 0.0)

        f.fahren(120.5)
        self.assertAlmostEqual(f.kilometerstand, 120.5)

        # Negative km dürfen den Kilometerstand nicht verändern
        f.fahren(-50.0)
        self.assertAlmostEqual(f.kilometerstand, 120.5)

    def test_02_fahrzeug_berechne_restwert(self):
        """Prüft Restwertberechnung mit 5% jährlichem Wertverlust und 10% Mindestwert."""
        f = self.Fahrzeug("Audi", "A4", 2020, 40000.0)
        
        # Gleiches Jahr (Alter 0)
        self.assertAlmostEqual(f.berechne_restwert(2020), 40000.0)

        # Nach 4 Jahren (20% Verlust -> 80% von 40000 = 32000)
        self.assertAlmostEqual(f.berechne_restwert(2024), 32000.0)

        # Nach 30 Jahren (Mehr als 90% Verlust -> Mindestwert 10% = 4000)
        self.assertAlmostEqual(f.berechne_restwert(2050), 4000.0)

    def test_03_fahrzeug_info_und_str(self):
        """Prüft info() und __str__() der Basisklasse Fahrzeug."""
        f = self.Fahrzeug("BMW", "320d", 2020, 35000.0)
        self.assertEqual(f.info(), "BMW 320d (2020) - 0.0 km")
        
        f.fahren(5000.0)
        self.assertEqual(str(f), "BMW 320d (2020) - 5000.0 km")

    def test_04_auto_vererbung_und_super(self):
        """Prüft Vererbung von Fahrzeug an Auto und Aufruf von super().__init__()."""
        self.assertTrue(issubclass(self.Auto, self.Fahrzeug), "Auto muss von Fahrzeug erben!")
        
        a = self.Auto("VW", "Polo", 2022, 20000.0, sitzplaetze=5, anzahl_tueren=3)
        self.assertIsInstance(a, self.Fahrzeug)
        self.assertIsInstance(a, self.Auto)

        # Geerbte Attribute prüfen
        self.assertEqual(a.marke, "VW")
        self.assertEqual(a.modell, "Polo")
        self.assertEqual(a.baujahr, 2022)
        self.assertEqual(a.grundpreis, 20000.0)
        self.assertEqual(a.kilometerstand, 0.0)

        # Neue Attribute prüfen
        self.assertEqual(a.sitzplaetze, 5)
        self.assertEqual(a.anzahl_tueren, 3)

    def test_05_auto_methoden_und_hupen(self):
        """Prüft hupen() und die erweiterte info()-Methode von Auto."""
        a = self.Auto("Porsche", "911", 2023, 120000.0, sitzplaetze=2, anzahl_tueren=2)
        self.assertEqual(a.hupen(), "Hup hup! Platz da für den Porsche 911!")

        a.fahren(250.0)
        self.assertEqual(a.info(), "Porsche 911 (2023) - 250.0 km | 2 Sitze, 2 Türen")

    def test_06_elektroauto_mehrstufige_vererbung(self):
        """Prüft mehrstufige Vererbung: ElektroAuto -> Auto -> Fahrzeug."""
        self.assertTrue(issubclass(self.ElektroAuto, self.Auto), "ElektroAuto muss von Auto erben!")
        self.assertTrue(issubclass(self.ElektroAuto, self.Fahrzeug), "ElektroAuto muss auch von Fahrzeug erben!")

        e = self.ElektroAuto(
            "Tesla", "Model 3", 2023, 42000.0,
            batterie_kapazitaet_kwh=60.0,
            sitzplaetze=5,
            anzahl_tueren=5,
            verbrauch_pro_100km=15.0
        )
        self.assertIsInstance(e, self.Fahrzeug)
        self.assertIsInstance(e, self.Auto)
        self.assertIsInstance(e, self.ElektroAuto)

        self.assertEqual(e.batterie_kapazitaet_kwh, 60.0)
        self.assertEqual(e.batterie_ladestand_kwh, 60.0)
        self.assertEqual(e.verbrauch_pro_100km, 15.0)

    def test_07_elektroauto_reichweite_und_fahren(self):
        """Prüft Reichweitenberechnung, Stromverbrauch und Fahren."""
        e = self.ElektroAuto(
            "Tesla", "Model 3", 2023, 42000.0,
            batterie_kapazitaet_kwh=60.0,
            verbrauch_pro_100km=15.0
        )
        # Voller Akku: (60 / 15) * 100 = 400 km
        self.assertAlmostEqual(e.reichweite(), 400.0)

        # 100 km fahren -> verbraucht 15 kWh -> 45 kWh übrig
        erfolg = e.fahren(100.0)
        self.assertTrue(erfolg, "Fahrt von 100 km sollte bei 400 km Reichweite erfolgreich sein!")
        self.assertAlmostEqual(e.kilometerstand, 100.0)
        self.assertAlmostEqual(e.batterie_ladestand_kwh, 45.0)
        self.assertAlmostEqual(e.reichweite(), 300.0)

        # Versuch, 400 km zu fahren (braucht 60 kWh, aber nur 45 kWh vorhanden)
        erfolg_zu_weit = e.fahren(400.0)
        self.assertFalse(erfolg_zu_weit, "Fahrt sollte fehlschlagen, wenn der Akku nicht reicht!")
        # Werte dürfen sich nicht verändert haben
        self.assertAlmostEqual(e.kilometerstand, 100.0)
        self.assertAlmostEqual(e.batterie_ladestand_kwh, 45.0)

    def test_08_elektroauto_aufladen_und_info(self):
        """Prüft Akku aufladen und die erweiterte info()-Methode."""
        e = self.ElektroAuto(
            "Tesla", "Model 3", 2023, 42000.0,
            batterie_kapazitaet_kwh=60.0,
            verbrauch_pro_100km=15.0
        )
        e.fahren(200.0)  # Verbraucht 30 kWh -> 30 kWh übrig

        # 20 kWh laden
        geladen = e.aufladen(20.0)
        self.assertAlmostEqual(geladen, 20.0)
        self.assertAlmostEqual(e.batterie_ladestand_kwh, 50.0)

        # Mehr laden als reinpasst (nur noch 10 kWh frei)
        geladen_uebervoll = e.aufladen(50.0)
        self.assertAlmostEqual(geladen_uebervoll, 10.0)
        self.assertAlmostEqual(e.batterie_ladestand_kwh, 60.0)

        info_text = e.info()
        self.assertIn("Tesla Model 3", info_text)
        self.assertIn("60.0/60.0 kWh", info_text)

    def test_09_lkw_vererbung_und_ladung(self):
        """Prüft Lkw: direkte Vererbung von Fahrzeug, Beladen und Entladen."""
        self.assertTrue(issubclass(self.Lkw, self.Fahrzeug), "Lkw muss von Fahrzeug erben!")
        self.assertFalse(issubclass(self.Lkw, self.Auto), "Lkw sollte NICHT von Auto erben!")

        lkw = self.Lkw("MAN", "TGX", 2021, 130000.0, max_zuladung_kg=18000.0)
        self.assertIsInstance(lkw, self.Fahrzeug)
        self.assertEqual(lkw.aktuelle_ladung_kg, 0.0)
        self.assertEqual(lkw.max_zuladung_kg, 18000.0)

        # Erfolgreich beladen
        self.assertTrue(lkw.beladen(10000.0))
        self.assertAlmostEqual(lkw.aktuelle_ladung_kg, 10000.0)

        # Überladung ablehnen (10000 + 9000 = 19000 > 18000)
        self.assertFalse(lkw.beladen(9000.0))
        self.assertAlmostEqual(lkw.aktuelle_ladung_kg, 10000.0)

        # Teilweise entladen
        entladen = lkw.entladen(4000.0)
        self.assertAlmostEqual(entladen, 4000.0)
        self.assertAlmostEqual(lkw.aktuelle_ladung_kg, 6000.0)

        # Mehr entladen als vorhanden (nur 6000 kg übrig)
        entladen_rest = lkw.entladen(10000.0)
        self.assertAlmostEqual(entladen_rest, 6000.0)
        self.assertAlmostEqual(lkw.aktuelle_ladung_kg, 0.0)

        # Fahren erben
        lkw.fahren(300.0)
        self.assertAlmostEqual(lkw.kilometerstand, 300.0)
        self.assertIn("Ladung: 0.0/18000.0 kg", lkw.info())


if __name__ == "__main__":
    res = unittest.main(verbosity=2, exit=False)
    try:
        from pathlib import Path
        sys.path.insert(0, str(Path(__file__).parent.parent))
        from gamification import report_single_chapter_result
        report_single_chapter_result(Path(__file__).parent.name, res.result.wasSuccessful(), res.result.testsRun)
    except Exception:
        pass
    sys.exit(0 if res.result.wasSuccessful() else 1)