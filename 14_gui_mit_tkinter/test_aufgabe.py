#!/usr/bin/env python3
"""
🧪 Testsuite für Kapitel 14: Desktop-GUIs mit Tkinter & OOP
============================================================
Überprüft:
- ZaehlerLogik: Reines Datenmodell (Werte, Grenzen, Schrittweiten, Klicks)
- ZaehlerApp: Tkinter-Oberfläche, Widget-Erstellung, Event-Handling, MVC-Synchronisation
- Headless-Kompatibilität: Läuft ohne GUI-Blockade in jeder Testumgebung!
"""

import sys
import unittest
from pathlib import Path

# Pfad zum aktuellen Kapitel hinzufügen
sys.path.insert(0, str(Path(__file__).parent))

try:
    import aufgabe
except ImportError as e:
    raise ImportError(f"Konnte 'aufgabe.py' nicht importieren: {e}")


class TestKapitel14Logik(unittest.TestCase):
    """Prüft das reine Datenmodell ZaehlerLogik."""

    def setUp(self):
        ZaehlerLogik = getattr(aufgabe, "ZaehlerLogik", None)
        self.assertIsNotNone(
            ZaehlerLogik, "Klasse 'ZaehlerLogik' in aufgabe.py nicht gefunden!"
        )
        self.ZaehlerLogik = ZaehlerLogik

    def test_01_logik_initialisierung(self):
        """Prüft Default-Werte und benutzerdefinierte Parameter."""
        # Standard-Instanziierung
        z1 = self.ZaehlerLogik()
        self.assertEqual(z1.wert, 0, "Default-Startwert sollte 0 sein.")
        self.assertEqual(z1.min_wert, -100, "Default min_wert sollte -100 sein.")
        self.assertEqual(z1.max_wert, 100, "Default max_wert sollte 100 sein.")
        self.assertEqual(z1.schrittweite, 1, "Default-Schrittweite sollte 1 sein.")
        self.assertEqual(z1.klick_anzahl, 0, "Default-Klickanzahl sollte 0 sein.")

        # Custom Instanziierung
        z2 = self.ZaehlerLogik(startwert=10, min_wert=-20, max_wert=50)
        self.assertEqual(z2.wert, 10)
        self.assertEqual(z2.min_wert, -20)
        self.assertEqual(z2.max_wert, 50)

    def test_02_logik_erhoehen_und_verringern(self):
        """Prüft das Erhöhen und Verringern des Zählerstands und Zählen der Klicks."""
        z = self.ZaehlerLogik(startwert=0)

        # 1. Erhöhen
        res = z.erhoehen()
        self.assertEqual(res, 1, "erhoehen() sollte den neuen Wert (1) zurückgeben.")
        self.assertEqual(z.wert, 1)
        self.assertEqual(z.klick_anzahl, 1)

        z.erhoehen()
        self.assertEqual(z.wert, 2)
        self.assertEqual(z.klick_anzahl, 2)

        # 2. Verringern
        res_v = z.verringern()
        self.assertEqual(res_v, 1, "verringern() sollte den neuen Wert (1) zurückgeben.")
        self.assertEqual(z.wert, 1)
        self.assertEqual(z.klick_anzahl, 3)

        z.verringern()
        z.verringern()
        self.assertEqual(z.wert, -1)
        self.assertEqual(z.klick_anzahl, 5)

    def test_03_logik_grenzwerte_clamping(self):
        """Prüft, dass der Wert min_wert und max_wert nicht überschreitet."""
        z = self.ZaehlerLogik(startwert=9, min_wert=-5, max_wert=10)

        # Erhöhen bis zum Limit
        z.erhoehen()  # wert = 10
        self.assertEqual(z.wert, 10)

        # Weiteres Erhöhen darf 10 nicht überschreiten
        z.erhoehen()
        self.assertEqual(z.wert, 10, "Zählerstand darf max_wert nicht überschreiten!")

        # Verringern bis zum Minimal-Limit
        z2 = self.ZaehlerLogik(startwert=-4, min_wert=-5, max_wert=10)
        z2.verringern()  # wert = -5
        self.assertEqual(z2.wert, -5)

        z2.verringern()  # bleibt bei -5
        self.assertEqual(z2.wert, -5, "Zählerstand darf min_wert nicht unterschreiten!")

    def test_04_logik_schrittweite(self):
        """Prüft das Setzen und Anwenden der Schrittweite."""
        z = self.ZaehlerLogik(startwert=0)

        # Gültige Schrittweite
        ok = z.setze_schrittweite(5)
        self.assertTrue(ok, "setze_schrittweite(5) sollte True zurückgeben.")
        self.assertEqual(z.schrittweite, 5)

        z.erhoehen()
        self.assertEqual(z.wert, 5, "erhoehen() sollte bei Schrittweite 5 um 5 steigen.")

        z.verringern()
        self.assertEqual(z.wert, 0)

        # Ungültige Schrittweiten (0 oder negativ)
        ok_null = z.setze_schrittweite(0)
        self.assertFalse(ok_null, "setze_schrittweite(0) sollte False zurückgeben.")
        self.assertEqual(z.schrittweite, 5, "Schrittweite darf sich bei 0 nicht ändern.")

        ok_neg = z.setze_schrittweite(-3)
        self.assertFalse(ok_neg, "setze_schrittweite(-3) sollte False zurückgeben.")
        self.assertEqual(z.schrittweite, 5, "Schrittweite darf sich bei negativen Werten nicht ändern.")

    def test_05_logik_zuruecksetzen(self):
        """Prüft das Zurücksetzen auf 0."""
        z = self.ZaehlerLogik(startwert=42)
        res = z.zuruecksetzen()
        self.assertEqual(res, 0, "zuruecksetzen() sollte 0 zurückgeben.")
        self.assertEqual(z.wert, 0)
        self.assertEqual(z.klick_anzahl, 1)

    def test_06_logik_ist_gerade_und_str(self):
        """Prüft die Geradheits-Prüfung und String-Repräsentation."""
        z = self.ZaehlerLogik(startwert=0)
        self.assertTrue(z.ist_gerade(), "0 ist gerade.")

        z.erhoehen()  # 1
        self.assertFalse(z.ist_gerade(), "1 ist ungerade.")

        z.erhoehen()  # 2
        self.assertTrue(z.ist_gerade(), "2 ist gerade.")

        # __str__ Prüfung
        text = str(z)
        self.assertIn("2", text, "__str__ sollte den aktuellen Zählerstand enthalten.")


class TestKapitel14GUI(unittest.TestCase):
    """Prüft die Tkinter-Benutzeroberfläche ZaehlerApp im Headless-Modus."""

    def setUp(self):
        ZaehlerApp = getattr(aufgabe, "ZaehlerApp", None)
        self.assertIsNotNone(
            ZaehlerApp, "Klasse 'ZaehlerApp' in aufgabe.py nicht gefunden!"
        )
        self.ZaehlerApp = ZaehlerApp

        # Hauptfenster (oder MockTk) erzeugen
        tk_mod = getattr(aufgabe, "tk", None)
        self.assertIsNotNone(tk_mod, "Tkinter-Modul 'tk' in aufgabe.py nicht gefunden!")
        self.root = tk_mod.Tk()
        self.app = self.ZaehlerApp(self.root)

    def _get_widget_text(self, widget) -> str:
        """Hilfsfunktion zum Auslesen des Texts eines Widgets."""
        if widget is None:
            return ""
        if hasattr(widget, "cget"):
            try:
                return str(widget.cget("text"))
            except Exception:
                pass
        if hasattr(widget, "_text"):
            return str(widget._text)
        if isinstance(widget, dict):
            return str(widget.get("text", ""))
        return ""

    def test_07_gui_initialisierung(self):
        """Prüft, ob alle Widgets angelegt wurden und die Startwerte stimmen."""
        self.assertIsNotNone(getattr(self.app, "root", None), "app.root fehlt!")
        self.assertIsNotNone(getattr(self.app, "logik", None), "app.logik fehlt!")

        # Widgets überprüfen
        self.assertTrue(
            hasattr(self.app, "label_anzeige"), "app.label_anzeige fehlt!"
        )
        self.assertTrue(hasattr(self.app, "label_info"), "app.label_info fehlt!")
        self.assertTrue(hasattr(self.app, "btn_plus"), "app.btn_plus fehlt!")
        self.assertTrue(hasattr(self.app, "btn_minus"), "app.btn_minus fehlt!")
        self.assertTrue(hasattr(self.app, "btn_reset"), "app.btn_reset fehlt!")
        self.assertTrue(hasattr(self.app, "entry_schritt"), "app.entry_schritt fehlt!")

        # Initialer Text im Anzeige-Label sollte "0" sein
        anzeige_text = self._get_widget_text(self.app.label_anzeige)
        self.assertEqual(
            anzeige_text, "0", f"Startwert im Anzeige-Label sollte '0' sein, war aber '{anzeige_text}'"
        )

    def test_08_gui_klick_plus_und_minus(self):
        """Prüft, ob klick_plus und klick_minus die Logik und das Label aktualisieren."""
        # 1. Plus-Klick auslösen
        self.app.klick_plus()
        self.assertEqual(self.app.logik.wert, 1, "Logik-Wert sollte 1 sein.")
        self.assertEqual(
            self._get_widget_text(self.app.label_anzeige),
            "1",
            "Anzeige-Label sollte nach Plus-Klick '1' zeigen.",
        )

        # 2. Weiterer Plus-Klick
        self.app.klick_plus()
        self.assertEqual(self.app.logik.wert, 2)
        self.assertEqual(self._get_widget_text(self.app.label_anzeige), "2")

        # 3. Minus-Klick
        self.app.klick_minus()
        self.assertEqual(self.app.logik.wert, 1)
        self.assertEqual(self._get_widget_text(self.app.label_anzeige), "1")

    def test_09_gui_klick_reset(self):
        """Prüft, ob klick_reset den Zähler und das Label zurücksetzt."""
        self.app.klick_plus()
        self.app.klick_plus()
        self.assertEqual(self.app.logik.wert, 2)

        self.app.klick_reset()
        self.assertEqual(self.app.logik.wert, 0, "Logik-Wert sollte 0 nach Reset sein.")
        self.assertEqual(
            self._get_widget_text(self.app.label_anzeige),
            "0",
            "Anzeige-Label sollte nach Reset '0' zeigen.",
        )

    def test_10_gui_schrittweite_setzen(self):
        """Prüft, ob klick_schritt_setzen den Wert aus entry_schritt übernimmt."""
        # Wert im Entry-Feld anpassen
        self.app.entry_schritt.delete(0, "end")
        self.app.entry_schritt.insert(0, "10")

        # Setzen auslösen
        self.app.klick_schritt_setzen()
        self.assertEqual(
            self.app.logik.schrittweite,
            10,
            "Schrittweite in Logik sollte auf 10 gesetzt werden.",
        )

        # Plus klicken -> Sprung um 10
        self.app.klick_plus()
        self.assertEqual(self.app.logik.wert, 10)
        self.assertEqual(self._get_widget_text(self.app.label_anzeige), "10")

    def test_11_gui_ungueltige_eingabe_abfangen(self):
        """Prüft robuste Fehlerbehandlung bei ungültigen Entry-Eingaben."""
        # Text statt Zahl eingeben
        self.app.entry_schritt.delete(0, "end")
        self.app.entry_schritt.insert(0, "keine_zahl")

        # Darf keinen Absturz/Exception erzeugen
        try:
            self.app.klick_schritt_setzen()
        except Exception as e:
            self.fail(f"klick_schritt_setzen() ist bei ungültiger Eingabe abgestürzt: {e}")

        # Schrittweite sollte unverändert geblieben sein
        self.assertEqual(self.app.logik.schrittweite, 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
