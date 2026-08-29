import unittest
import sys
import types
import inspect
from pathlib import Path

# Sicherstellen, dass das aktuelle Verzeichnis im Python-Pfad liegt
sys.path.insert(0, str(Path(__file__).parent))

try:
    import aufgabe
except ImportError as e:
    raise ImportError(f"Konnte 'aufgabe.py' nicht importieren: {e}")


class TestKapitel19(unittest.TestCase):
    """
    Testsuite für Kapitel 19: Generatoren, Iteratoren & itertools (Memory Efficiency).
    """

    def setUp(self):
        self.endlos_zaehler = getattr(aufgabe, "endlos_zaehler", None)
        self.fibonacci_generator = getattr(aufgabe, "fibonacci_generator", None)
        self.filter_grosse_zahlen = getattr(aufgabe, "filter_grosse_zahlen", None)
        self.erzeuge_quadrat_generator = getattr(aufgabe, "erzeuge_quadrat_generator", None)
        self.kette_listen = getattr(aufgabe, "kette_listen", None)
        self.erzeuge_passwort_kombinationen = getattr(aufgabe, "erzeuge_passwort_kombinationen", None)
        self.zyklische_elemente = getattr(aufgabe, "zyklische_elemente", None)

        self.assertIsNotNone(self.endlos_zaehler, "Funktion 'endlos_zaehler' nicht gefunden!")
        self.assertIsNotNone(self.fibonacci_generator, "Funktion 'fibonacci_generator' nicht gefunden!")
        self.assertIsNotNone(self.filter_grosse_zahlen, "Funktion 'filter_grosse_zahlen' nicht gefunden!")
        self.assertIsNotNone(self.erzeuge_quadrat_generator, "Funktion 'erzeuge_quadrat_generator' nicht gefunden!")
        self.assertIsNotNone(self.kette_listen, "Funktion 'kette_listen' nicht gefunden!")
        self.assertIsNotNone(self.erzeuge_passwort_kombinationen, "Funktion 'erzeuge_passwort_kombinationen' nicht gefunden!")
        self.assertIsNotNone(self.zyklische_elemente, "Funktion 'zyklische_elemente' nicht gefunden!")

    # ==========================================================================
    # 1. Endloszähler (Generator mit yield)
    # ==========================================================================
    def test_01_endlos_zaehler(self):
        """Prüft, ob endlos_zaehler ein echter Generator ist und korrekt zählt."""
        gen = self.endlos_zaehler(start=0, schritt=1)
        self.assertTrue(inspect.isgenerator(gen) or isinstance(gen, types.GeneratorType),
                        "endlos_zaehler muss ein Generator sein (yield nutzen)!")

        # Erste 5 Werte prüfen
        werte = [next(gen) for _ in range(5)]
        self.assertEqual(werte, [0, 1, 2, 3, 4])

        # Mit benutzerdefiniertem Start und Schrittweite
        gen2 = self.endlos_zaehler(start=100, schritt=5)
        werte2 = [next(gen2) for _ in range(4)]
        self.assertEqual(werte2, [100, 105, 110, 115])

        # Mit negativer Schrittweite
        gen3 = self.endlos_zaehler(start=10, schritt=-2)
        werte3 = [next(gen3) for _ in range(4)]
        self.assertEqual(werte3, [10, 8, 6, 4])

    # ==========================================================================
    # 2. Fibonacci-Generator
    # ==========================================================================
    def test_02_fibonacci_generator(self):
        """Prüft Fibonacci-Generator für verschiedene Anzahlen und Fehlerbehandlung."""
        gen = self.fibonacci_generator(7)
        self.assertTrue(inspect.isgenerator(gen) or isinstance(gen, types.GeneratorType),
                        "fibonacci_generator muss ein Generator sein!")

        ergebnis = list(gen)
        self.assertEqual(ergebnis, [0, 1, 1, 2, 3, 5, 8])

        # Grenzfälle
        self.assertEqual(list(self.fibonacci_generator(0)), [])
        self.assertEqual(list(self.fibonacci_generator(1)), [0])
        self.assertEqual(list(self.fibonacci_generator(2)), [0, 1])
        self.assertEqual(list(self.fibonacci_generator(10)), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

        # Negative Anzahl muss ValueError werfen
        with self.assertRaises(ValueError, msg="Negative Anzahl muss ValueError auslösen!"):
            list(self.fibonacci_generator(-5))

    # ==========================================================================
    # 3. Speicherschonender Filter (filter_grosse_zahlen)
    # ==========================================================================
    def test_03_filter_grosse_zahlen(self):
        """Prüft, ob der Filter Zahlen speicherschonend per Generator filtert."""
        eingabe = [10, 2.5, 50, 100, 5, 20.1]
        gen = self.filter_grosse_zahlen(eingabe, 20.0)
        self.assertTrue(inspect.isgenerator(gen) or isinstance(gen, types.GeneratorType),
                        "filter_grosse_zahlen muss ein Generator sein (yield nutzen)!")

        ergebnis = list(gen)
        self.assertEqual(ergebnis, [50, 100, 20.1])

        # Keine Treffer
        self.assertEqual(list(self.filter_grosse_zahlen([1, 2, 3], 10)), [])

        # Alle Treffer
        self.assertEqual(list(self.filter_grosse_zahlen([15, 20, 30], 10)), [15, 20, 30])

        # Funktioniert auch mit einem Generator als Eingabe (Streaming-Pipeline)
        eingabe_gen = (x * 10 for x in range(5))  # 0, 10, 20, 30, 40
        gefiltert = list(self.filter_grosse_zahlen(eingabe_gen, 15))
        self.assertEqual(gefiltert, [20, 30, 40])

    # ==========================================================================
    # 4. Generator Expression (erzeuge_quadrat_generator)
    # ==========================================================================
    def test_04_erzeuge_quadrat_generator(self):
        """Prüft die Erzeugung von Generator Expressions."""
        gen = self.erzeuge_quadrat_generator(5)
        self.assertTrue(inspect.isgenerator(gen) or isinstance(gen, types.GeneratorType),
                        "erzeuge_quadrat_generator muss eine Generator-Expression zurückgeben!")

        self.assertEqual(list(gen), [1, 4, 9, 16, 25])
        self.assertEqual(list(self.erzeuge_quadrat_generator(0)), [])

        with self.assertRaises(ValueError, msg="Negatives n muss ValueError auslösen!"):
            self.erzeuge_quadrat_generator(-3)

    # ==========================================================================
    # 5. itertools.chain (kette_listen)
    # ==========================================================================
    def test_05_kette_listen(self):
        """Prüft das Verketten beliebiger Iterables mit itertools.chain."""
        l1 = [1, 2]
        l2 = [3, 4, 5]
        l3 = [6]
        self.assertEqual(self.kette_listen(l1, l2, l3), [1, 2, 3, 4, 5, 6])

        # Leere Iterables
        self.assertEqual(self.kette_listen([], [42], []), [42])
        self.assertEqual(self.kette_listen(), [])

        # Gemischte Iterables (Tupel, Sets, Generatoren)
        t = (10, 20)
        g = (x for x in [30, 40])
        self.assertEqual(self.kette_listen(t, g), [10, 20, 30, 40])

    # ==========================================================================
    # 6. itertools.permutations (erzeuge_passwort_kombinationen)
    # ==========================================================================
    def test_06_erzeuge_passwort_kombinationen(self):
        """Prüft die Erzeugung von Permutationen mit itertools.permutations."""
        kombis = self.erzeuge_passwort_kombinationen("abc", 2)
        erwartet = ['ab', 'ac', 'ba', 'bc', 'ca', 'cb']
        self.assertEqual(sorted(kombis), sorted(erwartet))
        self.assertEqual(len(kombis), 6)

        # Einzelzeichen
        kombis1 = self.erzeuge_passwort_kombinationen("xyz", 1)
        self.assertEqual(sorted(kombis1), ['x', 'y', 'z'])

        # Gesamtlänge
        kombis_voll = self.erzeuge_passwort_kombinationen("ab", 2)
        self.assertEqual(sorted(kombis_voll), ['ab', 'ba'])

        # Länge 0
        self.assertEqual(self.erzeuge_passwort_kombinationen("abc", 0), [''])

        # Fehlerbehandlung bei ungültigen Längen
        with self.assertRaises(ValueError, msg="Negative Länge muss ValueError werfen"):
            self.erzeuge_passwort_kombinationen("abc", -1)

        with self.assertRaises(ValueError, msg="Länge > Zeichenanzahl muss ValueError werfen"):
            self.erzeuge_passwort_kombinationen("ab", 5)

    # ==========================================================================
    # 7. itertools.cycle (zyklische_elemente)
    # ==========================================================================
    def test_07_zyklische_elemente(self):
        """Prüft zyklische Entnahme mit itertools.cycle."""
        farben = ["Rot", "Gelb", "Gruen"]
        res = self.zyklische_elemente(farben, 7)
        self.assertEqual(res, ["Rot", "Gelb", "Gruen", "Rot", "Gelb", "Gruen", "Rot"])

        # Anzahl 0
        self.assertEqual(self.zyklische_elemente(farben, 0), [])

        # Fehlerbehandlung
        with self.assertRaises(ValueError, msg="Negative Anzahl muss ValueError werfen"):
            self.zyklische_elemente(farben, -2)

        with self.assertRaises(ValueError, msg="Leere Liste bei anzahl > 0 muss ValueError werfen"):
            self.zyklische_elemente([], 5)


if __name__ == "__main__":
    unittest.main(verbosity=2)
