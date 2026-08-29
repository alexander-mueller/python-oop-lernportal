import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

try:
    import aufgabe
except ImportError as e:
    raise ImportError(f"Konnte 'aufgabe.py' nicht importieren: {e}")


class TestKapitel05(unittest.TestCase):

    def test_01_song_init_und_dauer(self):
        """Prüft Song Attribute und Formatierung der Dauer."""
        s = aufgabe.Song("Vampire", "Olivia Rodrigo", 219)
        self.assertEqual(s.titel, "Vampire")
        self.assertEqual(s.kuenstler, "Olivia Rodrigo")
        self.assertEqual(s.dauer_sekunden, 219)
        self.assertEqual(s.formatierte_dauer(), "03:39")

        s_kurz = aufgabe.Song("Intro", "Kuenstler", 5)
        self.assertEqual(s_kurz.formatierte_dauer(), "00:05")

    def test_02_song_str(self):
        """Prüft die __str__ Methode von Song."""
        s = aufgabe.Song("Espresso", "Sabrina Carpenter", 175)
        erwartet = '"Espresso" von Sabrina Carpenter (02:55)'
        self.assertEqual(str(s), erwartet)

    def test_03_playlist_hinzufuegen_und_dauer(self):
        """Prüft Playlist Erstellung, Hinzufügen, Anzahl und Gesamtlaufzeit."""
        p = aufgabe.Playlist("Party")
        self.assertEqual(p.anzahl_songs(), 0)
        self.assertEqual(p.gesamtdauer_sekunden(), 0)
        self.assertIsNone(p.laengster_song())

        s1 = aufgabe.Song("Song A", "Artist 1", 100)
        s2 = aufgabe.Song("Song B", "Artist 2", 150)
        p.song_hinzufuegen(s1)
        p.song_hinzufuegen(s2)

        self.assertEqual(p.anzahl_songs(), 2)
        self.assertEqual(p.gesamtdauer_sekunden(), 250)

    def test_04_finde_songs_von(self):
        """Prüft die Filtersuche nach Künstlern (auch case-insensitive)."""
        p = aufgabe.Playlist("Mix")
        s1 = aufgabe.Song("Anti-Hero", "Taylor Swift", 200)
        s2 = aufgabe.Song("Cruel Summer", "Taylor Swift", 180)
        s3 = aufgabe.Song("Flowers", "Miley Cyrus", 210)

        p.song_hinzufuegen(s1)
        p.song_hinzufuegen(s2)
        p.song_hinzufuegen(s3)

        # Exakte Schreibweise
        ergebnis = p.finde_songs_von("Taylor Swift")
        self.assertEqual(len(ergebnis), 2)
        self.assertIn(s1, ergebnis)
        self.assertIn(s2, ergebnis)

        # Kleinschreibung testen
        ergebnis_lower = p.finde_songs_von("taylor swift")
        self.assertEqual(len(ergebnis_lower), 2)

        # Nicht vorhandener Künstler
        ergebnis_leer = p.finde_songs_von("Ed Sheeran")
        self.assertEqual(len(ergebnis_leer), 0)

    def test_05_laengster_song(self):
        """Prüft das Ermitteln des längsten Songs."""
        p = aufgabe.Playlist("Mix")
        s1 = aufgabe.Song("Kurz", "A", 120)
        s2 = aufgabe.Song("Lang", "B", 300)
        s3 = aufgabe.Song("Mittel", "C", 200)

        p.song_hinzufuegen(s1)
        p.song_hinzufuegen(s2)
        p.song_hinzufuegen(s3)

        self.assertIs(p.laengster_song(), s2)


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