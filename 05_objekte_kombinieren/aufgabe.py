"""
Kapitel 05: Komposition – Song & Playlist Manager
=================================================

In dieser Aufgabe baust du eine Musikverwaltung mit zwei Klassen:
'Song' und 'Playlist'.
"""

class Song:
    # ==========================================================================
    # TODO 1: Konstruktor für Song
    # Parameter: self, titel (str), kuenstler (str), dauer_sekunden (int)
    # Speichere: self.titel, self.kuenstler, self.dauer_sekunden
    # ==========================================================================
    def __init__(self, titel, kuenstler, dauer_sekunden):
        # Schreibe hier deinen Code für TODO 1:
        pass

    # ==========================================================================
    # TODO 2: Methode "formatierte_dauer(self)"
    # Rechnet 'self.dauer_sekunden' in Minuten und Sekunden um und gibt einen
    # String im Format "MM:SS" zurück (z.B. 215 -> "03:35", 70 -> "01:10").
    # Tipp: Verwende // 60 und % 60 sowie f"{minuten:02d}:{sekunden:02d}"
    # ==========================================================================
    def formatierte_dauer(self):
        # Schreibe hier deinen Code für TODO 2:
        pass

    # ==========================================================================
    # TODO 3: Dunder-Methode "__str__(self)"
    # Gibt einen String im folgenden Format zurück:
    # '"{titel}" von {kuenstler} ({dauer})'
    #
    # Beispiel: '"Flowers" von Miley Cyrus (03:20)'
    # ==========================================================================
    def __str__(self):
        # Schreibe hier deinen Code für TODO 3:
        pass


class Playlist:
    # ==========================================================================
    # TODO 4: Konstruktor für Playlist
    # Parameter: self, name (str)
    # Speichere: self.name, self.songs (als leere Liste [])
    # ==========================================================================
    def __init__(self, name):
        # Schreibe hier deinen Code für TODO 4:
        pass

    # ==========================================================================
    # TODO 5: Methode "song_hinzufuegen(self, song)"
    # Hängt das übergebene Song-Objekt an 'self.songs' an.
    # ==========================================================================
    def song_hinzufuegen(self, song):
        # Schreibe hier deinen Code für TODO 5:
        pass

    # ==========================================================================
    # TODO 6: Methode "anzahl_songs(self)"
    # Gibt die Anzahl der Songs in der Playlist als Integer zurück.
    # ==========================================================================
    def anzahl_songs(self):
        # Schreibe hier deinen Code für TODO 6:
        pass

    # ==========================================================================
    # TODO 7: Methode "gesamtdauer_sekunden(self)"
    # Gibt die Summe der Sekunden aller Songs in der Playlist zurück.
    # Bei leerer Playlist: 0
    # ==========================================================================
    def gesamtdauer_sekunden(self):
        # Schreibe hier deinen Code für TODO 7:
        pass

    # ==========================================================================
    # TODO 8: Methode "finde_songs_von(self, kuenstler)"
    # Sucht alle Songs in self.songs, bei denen der Künstler übereinstimmt.
    # Wichtig: Groß- und Kleinschreibung soll ignoriert werden! (z.B. .lower())
    # Gibt eine Liste von passenden Song-Objekten zurück.
    # ==========================================================================
    def finde_songs_von(self, kuenstler):
        # Schreibe hier deinen Code für TODO 8:
        pass

    # ==========================================================================
    # TODO 9: Methode "laengster_song(self)"
    # Findet den Song mit der längsten Spieldauer in self.songs.
    # - Gibt das gefundene Song-Objekt zurück.
    # - Gibt None zurück, wenn die Playlist leer ist.
    # ==========================================================================
    def laengster_song(self):
        # Schreibe hier deinen Code für TODO 9:
        pass


# ==============================================================================
# Hauptprogramm zum Ausprobieren:
# ==============================================================================
if __name__ == "__main__":
    print("🎧 --- MEINE PLAYLIST --- 🎧")
    meine_hits = Playlist("Sommer Vibes")

    s1 = Song("Flowers", "Miley Cyrus", 200)
    s2 = Song("Cruel Summer", "Taylor Swift", 178)
    s3 = Song("Anti-Hero", "Taylor Swift", 201)
    s4 = Song("As It Was", "Harry Styles", 167)

    meine_hits.song_hinzufuegen(s1)
    meine_hits.song_hinzufuegen(s2)
    meine_hits.song_hinzufuegen(s3)
    meine_hits.song_hinzufuegen(s4)

    print(f"Playlist: {meine_hits.name} ({meine_hits.anzahl_songs()} Songs)")
    print(f"Gesamtlaufzeit: {meine_hits.gesamtdauer_sekunden()} Sekunden")

    laengster = meine_hits.laengster_song()
    if laengster:
        print(f"Längster Song: {laengster}")

    print("\nSongs von Taylor Swift:")
    for s in meine_hits.finde_songs_von("taylor swift"):
        print(f"- {s}")
