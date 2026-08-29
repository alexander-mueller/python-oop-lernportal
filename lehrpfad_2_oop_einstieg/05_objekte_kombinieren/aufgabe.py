"""
Kapitel 05: Komposition – Song & Playlist Manager
=================================================

In dieser Aufgabe baust du eine Musikverwaltung mit zwei Klassen:
'Song' und 'Playlist'.
"""

class Song:
    # ==========================================================================
    # 🎯 TEILZIEL 1 (TODO 1): Konstruktor für Song
    # Parameter: self, titel (str), kuenstler (str), dauer_sekunden (int)
    # Speichere: self.titel, self.kuenstler, self.dauer_sekunden
    # ==========================================================================
    def __init__(self, titel, kuenstler, dauer_sekunden):
        # 🎯 TEILZIEL 1: Implementiere die Logik Schritt für Schritt:
    # 💡 Tipp: Beachte Datentypen und das abschließende return!
        pass

    # ==========================================================================
    # 🎯 TEILZIEL 2 (TODO 2): Methode "formatierte_dauer(self)"
    # Rechnet 'self.dauer_sekunden' in Minuten und Sekunden um und gibt einen
    # String im Format "MM:SS" zurück (z.B. 215 -> "03:35", 70 -> "01:10").
    #
    # Tipp:
    # minuten = self.dauer_sekunden // 60
    # sekunden = self.dauer_sekunden % 60
    # return f"{minuten:02d}:{sekunden:02d}"
    # ==========================================================================
    def formatierte_dauer(self):
        # 🎯 TEILZIEL 2: Implementiere die Logik Schritt für Schritt:
    # 💡 Tipp: Beachte Datentypen und das abschließende return!
        pass

    # ==========================================================================
    # 🎯 TEILZIEL 3 (TODO 3): Dunder-Methode "__str__(self)"
    # Gibt einen String im Format zurück:
    # '"{titel}" von {kuenstler} ({formatierte_dauer})'
    #
    # Beispiel: '"Flowers" von Miley Cyrus (03:20)'
    # ==========================================================================
    def __str__(self):
        # 🎯 TEILZIEL 3: Implementiere die Logik Schritt für Schritt:
    # 💡 Tipp: Beachte Datentypen und das abschließende return!
        pass


class Playlist:
    # ==========================================================================
    # 🎯 TEILZIEL 4 (TODO 4): Konstruktor für Playlist
    # Parameter: self, name (str)
    # Speichere: self.name, self.songs (als leere Liste [])
    # ==========================================================================
    def __init__(self, name):
        # 🎯 TEILZIEL 4: Implementiere die Logik Schritt für Schritt:
    # 💡 Tipp: Beachte Datentypen und das abschließende return!
        pass

    # ==========================================================================
    # 🎯 TEILZIEL 5 (TODO 5): Methode "song_hinzufuegen(self, song)"
    # Hängt das übergebene Song-Objekt an 'self.songs' an (.append).
    # ==========================================================================
    def song_hinzufuegen(self, song):
        # 🎯 TEILZIEL 5: Implementiere die Logik Schritt für Schritt:
    # 💡 Tipp: Beachte Datentypen und das abschließende return!
        pass

    # ==========================================================================
    # 🎯 TEILZIEL 6 (TODO 6): Methode "anzahl_songs(self)"
    # Gibt die Anzahl der Songs in der Playlist als Integer zurück (len(self.songs)).
    # ==========================================================================
    def anzahl_songs(self):
        # 🎯 TEILZIEL 6: Implementiere die Logik Schritt für Schritt:
    # 💡 Tipp: Beachte Datentypen und das abschließende return!
        pass

    # ==========================================================================
    # 🎯 TEILZIEL 7 (TODO 7): Methode "gesamtdauer_sekunden(self)"
    # Gibt die Summe der Sekunden aller Songs in der Playlist zurück.
    # Bei leerer Playlist: 0
    #
    # Tipp:
    # total = 0
    # for s in self.songs:
    #     total += s.dauer_sekunden
    # return total
    # ==========================================================================
    def gesamtdauer_sekunden(self):
        # 🎯 TEILZIEL 7: Implementiere die Logik Schritt für Schritt:
    # 💡 Tipp: Beachte Datentypen und das abschließende return!
        pass

    # ==========================================================================
    # 🎯 TEILZIEL 8 (TODO 8): Methode "finde_songs_von(self, kuenstler)"
    # Sucht alle Songs in self.songs, bei denen der Künstler übereinstimmt.
    # Wichtig: Groß- und Kleinschreibung soll ignoriert werden! (z.B. .lower())
    # Gibt eine Liste von passenden Song-Objekten zurück.
    # ==========================================================================
    def finde_songs_von(self, kuenstler):
        # 🎯 TEILZIEL 8: Implementiere die Logik Schritt für Schritt:
    # 💡 Tipp: Beachte Datentypen und das abschließende return!
        pass

    # ==========================================================================
    # 🎯 TEILZIEL 9 (TODO 9): Methode "laengster_song(self)"
    # Findet den Song mit der längsten Spieldauer in self.songs.
    # - Gibt das gefundene Song-Objekt zurück.
    # - Gibt None zurück, wenn die Playlist leer ist.
    # ==========================================================================
    def laengster_song(self):
        # 🎯 TEILZIEL 9: Implementiere die Logik Schritt für Schritt:
    # 💡 Tipp: Beachte Datentypen und das abschließende return!
        pass


# ==============================================================================
# Hauptprogramm zum Ausprobieren:
# (Ausführen mit 'python3 aufgabe.py')
# ==============================================================================
if __name__ == "__main__":
    print("🎧 --- MEINE PLAYLIST --- 🎧")
    meine_hits = Playlist("Sommer Vibes")

    s1 = Song("Flowers", "Miley Cyrus", 200)
    s2 = Song("Cruel Summer", "Taylor Swift", 178)
    s3 = Song("Anti-Hero", "Taylor Swift", 201)
    s4 = Song("As It Was", "Harry Styles", 167)

    if hasattr(meine_hits, "songs"):
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
    else:
        print("💡 Hinweis: Implementiere die TODOs, um die Playlist zu testen!")
