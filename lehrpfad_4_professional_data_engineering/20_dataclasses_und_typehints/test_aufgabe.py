import unittest
import sys
import time
from pathlib import Path
from dataclasses import is_dataclass

# Sicherstellen, dass das aktuelle Verzeichnis im Python-Pfad liegt
sys.path.insert(0, str(Path(__file__).parent))

try:
    import aufgabe
except ImportError as e:
    raise ImportError(f"Konnte 'aufgabe.py' nicht importieren: {e}")


class TestKapitel20(unittest.TestCase):
    """
    Testsuite für Kapitel 20: Dataclasses, Type Hints & Decorators.
    """

    def setUp(self):
        self.Artikel = getattr(aufgabe, "Artikel", None)
        self.Warenkorb = getattr(aufgabe, "Warenkorb", None)
        self.aufruf_zaehler = getattr(aufgabe, "aufruf_zaehler", None)
        self.zeitmessung = getattr(aufgabe, "zeitmessung", None)
        self.formatiere_benutzer = getattr(aufgabe, "formatiere_benutzer", None)

        self.assertIsNotNone(self.Artikel, "Klasse 'Artikel' nicht gefunden!")
        self.assertIsNotNone(self.Warenkorb, "Klasse 'Warenkorb' nicht gefunden!")
        self.assertIsNotNone(self.aufruf_zaehler, "Decorator 'aufruf_zaehler' nicht gefunden!")
        self.assertIsNotNone(self.zeitmessung, "Decorator 'zeitmessung' nicht gefunden!")
        self.assertIsNotNone(self.formatiere_benutzer, "Funktion 'formatiere_benutzer' nicht gefunden!")

    # ==========================================================================
    # 1. Dataclass Artikel
    # ==========================================================================
    def test_01_artikel_dataclass_basis(self):
        """Prüft, ob Artikel eine echte Dataclass ist und Standardwerte setzt."""
        self.assertTrue(is_dataclass(self.Artikel), "Artikel muss mit @dataclass dekoriert sein!")

        a = self.Artikel("Buch", 19.99)
        self.assertEqual(a.name, "Buch")
        self.assertEqual(a.preis, 19.99)
        self.assertEqual(a.kategorie, "Allgemein")

        # Gleichheit und Repräsentation (Dataclass-Features)
        a2 = self.Artikel("Buch", 19.99)
        self.assertEqual(a, a2, "Zwei Artikel mit identischen Werten müssen gleich (==) sein!")
        self.assertIn("Buch", repr(a))

    def test_02_artikel_validierung(self):
        """Prüft die Validierung in __post_init__."""
        with self.assertRaises(ValueError, msg="Negativer Preis muss ValueError auslösen!"):
            self.Artikel("Test", -5.0)

        with self.assertRaises(ValueError, msg="Leerer Name muss ValueError auslösen!"):
            self.Artikel("", 10.0)

        with self.assertRaises(ValueError, msg="Nur-Leerzeichen-Name muss ValueError auslösen!"):
            self.Artikel("   ", 10.0)

    def test_03_artikel_berechne_bruttopreis(self):
        """Prüft die Bruttoberechnung mit verschiedenen Steuersätzen."""
        buch = self.Artikel("Buch", 10.0)
        self.assertEqual(buch.berechne_bruttopreis(0.07), 10.70)
        self.assertEqual(buch.berechne_bruttopreis(0.19), 11.90)
        self.assertEqual(buch.berechne_bruttopreis(0.0), 10.0)

        with self.assertRaises(ValueError, msg="Negativer Steuersatz muss ValueError werfen"):
            buch.berechne_bruttopreis(-0.1)

    def test_04_artikel_classmethod_und_staticmethod(self):
        """Prüft @classmethod aus_csv_zeile und @staticmethod ist_gueltiger_preis."""
        # Classmethod
        a = self.Artikel.aus_csv_zeile("Monitor;249.99;Hardware")
        self.assertEqual(a.name, "Monitor")
        self.assertEqual(a.preis, 249.99)
        self.assertEqual(a.kategorie, "Hardware")

        # Staticmethod
        self.assertTrue(self.Artikel.ist_gueltiger_preis(100))
        self.assertTrue(self.Artikel.ist_gueltiger_preis(0.0))
        self.assertFalse(self.Artikel.ist_gueltiger_preis(-10))
        self.assertFalse(self.Artikel.ist_gueltiger_preis("100"))

    # ==========================================================================
    # 2. Dataclass Warenkorb
    # ==========================================================================
    def test_05_warenkorb_basis_und_default_factory(self):
        """Prüft Warenkorb, default_factory und Unabhängigkeit von Instanzen."""
        self.assertTrue(is_dataclass(self.Warenkorb), "Warenkorb muss mit @dataclass dekoriert sein!")

        k1 = self.Warenkorb(kunde="Alice")
        k2 = self.Warenkorb(kunde="Bob")

        self.assertEqual(len(k1), 0)
        self.assertEqual(k1.gesamtsumme(), 0.0)

        # Sicherstellen, dass default_factory=list genutzt wurde (keine geteilte Referenz)
        k1.artikel_hinzufuegen(self.Artikel("Tee", 3.50))
        self.assertEqual(len(k1), 1)
        self.assertEqual(len(k2), 0, "artikel_liste darf nicht zwischen Warenkörben geteilt werden!")

    def test_06_warenkorb_artikel_hinzufuegen_und_entfernen(self):
        """Prüft Hinzufügen (*args), Typprüfung und Entfernen von Artikeln."""
        korb = self.Warenkorb(kunde="Charlie")
        a1 = self.Artikel("Kaffee", 6.00)
        a2 = self.Artikel("Keks", 2.00)

        korb.artikel_hinzufuegen(a1, a2)
        self.assertEqual(len(korb), 2)
        self.assertEqual(korb.gesamtsumme(), 8.00)
        self.assertEqual(korb.gesamtsumme(brutto=True, mwst_satz=0.10), 8.80)

        # Typprüfung
        with self.assertRaises(TypeError, msg="Ungültige Objekte müssen TypeError auslösen!"):
            korb.artikel_hinzufuegen("Kein Artikel")

        # Artikel entfernen
        entfernt = korb.artikel_entfernen("kaffee")  # Case-insensitive
        self.assertTrue(entfernt)
        self.assertEqual(len(korb), 1)
        self.assertEqual(korb.gesamtsumme(), 2.00)

        # Nicht vorhandener Artikel
        self.assertFalse(korb.artikel_entfernen("NichtDa"))

    # ==========================================================================
    # 3. Decorator aufruf_zaehler
    # ==========================================================================
    def test_07_aufruf_zaehler_decorator(self):
        """Prüft, ob der Decorator Aufrufe zählt und functools.wraps verwendet."""
        @self.aufruf_zaehler
        def addiere(a: int, b: int) -> int:
            """Addiert zwei Zahlen."""
            return a + b

        self.assertEqual(addiere.__name__, "addiere", "functools.wraps muss den Funktionsnamen bewahren!")
        self.assertEqual(addiere.__doc__, "Addiert zwei Zahlen.", "functools.wraps muss den Docstring bewahren!")
        self.assertEqual(addiere.aufrufe, 0)

        res1 = addiere(5, 10)
        self.assertEqual(res1, 15)
        self.assertEqual(addiere.aufrufe, 1)

        res2 = addiere(20, 30)
        self.assertEqual(res2, 50)
        self.assertEqual(addiere.aufrufe, 2)

    # ==========================================================================
    # 4. Decorator zeitmessung
    # ==========================================================================
    def test_08_zeitmessung_decorator(self):
        """Prüft, ob zeitmessung die Dauer erfasst und das Ergebnis zurückgibt."""
        @self.zeitmessung
        def schlafe_kurz():
            time.sleep(0.01)
            return "Aufgewacht"

        ergebnis = schlafe_kurz()
        self.assertEqual(ergebnis, "Aufgewacht")
        self.assertTrue(hasattr(schlafe_kurz, "letzte_dauer"))
        self.assertGreaterEqual(schlafe_kurz.letzte_dauer, 0.005)

    # ==========================================================================
    # 5. Type Hints formatiere_benutzer
    # ==========================================================================
    def test_09_formatiere_benutzer(self):
        """Prüft die Formatierung typisierter Benutzer-Dictionaries und Fehler."""
        u1 = {"username": "Alice", "alter": 30, "ist_admin": True}
        res1 = self.formatiere_benutzer(u1)
        self.assertIn("Alice", res1)
        self.assertIn("30", res1)
        self.assertIn("Administrator", res1)

        u2 = {"username": "Bob", "ist_admin": False}
        res2 = self.formatiere_benutzer(u2)
        self.assertIn("Bob", res2)
        self.assertIn("Unbekannt", res2)
        self.assertIn("Standardbenutzer", res2)

        # Fehler bei fehlendem Username
        with self.assertRaises(KeyError):
            self.formatiere_benutzer({"alter": 20})

        with self.assertRaises(ValueError):
            self.formatiere_benutzer({"username": "   "})


if __name__ == "__main__":
    unittest.main(verbosity=2)
