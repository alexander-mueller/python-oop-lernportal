"""
Kapitel 05: Komposition – Song & Playlist Manager – Musterlösung
================================================================
"""

class Song:
    def __init__(self, titel, kuenstler, dauer_sekunden):
        self.titel = titel
        self.kuenstler = kuenstler
        self.dauer_sekunden = int(dauer_sekunden)

    def formatierte_dauer(self):
        minuten = self.dauer_sekunden // 60
        sekunden = self.dauer_sekunden % 60
        return f"{minuten:02d}:{sekunden:02d}"

    def __str__(self):
        return f'"{self.titel}" von {self.kuenstler} ({self.formatierte_dauer()})'


class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def song_hinzufuegen(self, song):
        self.songs.append(song)

    def anzahl_songs(self):
        return len(self.songs)

    def gesamtdauer_sekunden(self):
        return sum(s.dauer_sekunden for s in self.songs)

    def finde_songs_von(self, kuenstler):
        kuenstler_lower = kuenstler.lower()
        return [s for s in self.songs if s.kuenstler.lower() == kuenstler_lower]

    def laengster_song(self):
        if not self.songs:
            return None
        return max(self.songs, key=lambda s: s.dauer_sekunden)


if __name__ == "__main__":
    meine_hits = Playlist("Sommer Vibes")
    meine_hits.song_hinzufuegen(Song("Flowers", "Miley Cyrus", 200))
    meine_hits.song_hinzufuegen(Song("Cruel Summer", "Taylor Swift", 178))
    meine_hits.song_hinzufuegen(Song("Anti-Hero", "Taylor Swift", 201))

    print(f"Playlist: {meine_hits.name} ({meine_hits.anzahl_songs()} Songs)")
    print(f"Längster Song: {meine_hits.laengster_song()}")
