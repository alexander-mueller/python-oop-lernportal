import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

try:
    import aufgabe
except ImportError as e:
    raise ImportError(f"Konnte 'aufgabe.py' nicht importieren: {e}")


class TestKapitel07(unittest.TestCase):

    def setUp(self):
        Person = getattr(aufgabe, "Person", None)
        self.assertIsNotNone(Person, "Klasse 'Person' nicht gefunden!")
        self.Person = Person

    def test_01_init(self):
        """Prüft Initialisierung und Default-Werte für Referenzen."""
        p = self.Person("Mia", 2008)
        self.assertEqual(p.name, "Mia")
        self.assertEqual(p.geburtsjahr, 2008)
        self.assertIsNone(p.mutter)
        self.assertIsNone(p.vater)
        self.assertEqual(p.kinder, [])

    def test_02_mutter_vater_setzen(self):
        """Prüft gegenseitige Referenzverknüpfung."""
        kind = self.Person("Mia", 2008)
        mama = self.Person("Susi", 1980)
        papa = self.Person("Tom", 1978)

        kind.mutter_setzen(mama)
        kind.vater_setzen(papa)

        # Referenzprüfung
        self.assertIs(kind.mutter, mama)
        self.assertIs(kind.vater, papa)
        self.assertIn(kind, mama.kinder)
        self.assertIn(kind, papa.kinder)

        # Kein doppeltes Hinzufügen
        kind.mutter_setzen(mama)
        self.assertEqual(len(mama.kinder), 1)

    def test_03_geschwister(self):
        """Prüft Finden aller Geschwister (ohne self und ohne Duplikate)."""
        mama = self.Person("Susi", 1980)
        papa = self.Person("Tom", 1978)
        kind1 = self.Person("Mia", 2008)
        kind2 = self.Person("Leo", 2011)
        halbbruder = self.Person("Max", 2005)

        kind1.mutter_setzen(mama)
        kind1.vater_setzen(papa)
        kind2.mutter_setzen(mama)
        kind2.vater_setzen(papa)
        halbbruder.vater_setzen(papa)  # Nur gleicher Vater

        geschwister_mia = kind1.geschwister()
        self.assertNotIn(kind1, geschwister_mia, "self darf nicht in den eigenen Geschwistern sein!")
        self.assertIn(kind2, geschwister_mia)
        self.assertIn(halbbruder, geschwister_mia)
        self.assertEqual(len(geschwister_mia), 2)

    def test_04_grosseltern(self):
        """Prüft Ermittlung der Großeltern über Referenzketten."""
        oma1 = self.Person("Anna", 1955)
        opa1 = self.Person("Karl", 1952)
        oma2 = self.Person("Monika", 1956)
        
        mama = self.Person("Susi", 1980)
        mama.mutter_setzen(oma1)
        mama.vater_setzen(opa1)

        papa = self.Person("Tom", 1978)
        papa.mutter_setzen(oma2)

        kind = self.Person("Mia", 2008)
        kind.mutter_setzen(mama)
        kind.vater_setzen(papa)

        grosseltern = kind.grosseltern()
        self.assertIn(oma1, grosseltern)
        self.assertIn(opa1, grosseltern)
        self.assertIn(oma2, grosseltern)
        self.assertEqual(len(grosseltern), 3)

    def test_05_str(self):
        """Prüft __str__ Formatierung."""
        p = self.Person("Mia", 2008)
        self.assertEqual(str(p), "Mia (*2008)")


if __name__ == "__main__":
    unittest.main(verbosity=2)
