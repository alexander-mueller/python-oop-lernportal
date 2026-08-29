# Kapitel 05: Komposition – Objekte kombinieren & filtern 🎵

In der echten Softwareentwicklung (wie bei Spotify, Instagram oder Netflix) besteht ein System fast immer aus vielen verschiedenen Klassen, die zusammenarbeiten.

Wenn eine Klasse andere Objekte besitzt oder verwaltet, nennt man das **Komposition** (oder *"hat-ein"-Beziehung*):
- Eine **Playlist** *hat viele* **Songs**.
- Ein **Kino** *hat viele* **Säle** und **Filme**.
- Eine **Schule** *hat viele* **Klassen** und **Schüler**.

---

## 🎶 Das Zusammenspiel: Song & Playlist

Schauen wir uns an, wie eine Playlist mit Songs arbeiten kann:

```python
class Song:
    def __init__(self, titel, dauer_sekunden):
        self.titel = titel
        self.dauer_sekunden = dauer_sekunden

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []  # Hier landen die Song-Objekte

    def hinzufuegen(self, song):
        self.songs.append(song)

    def finde_lange_songs(self, min_sekunden):
        gefundene = []
        for song in self.songs:
            if song.dauer_sekunden >= min_sekunden:
                gefundene.append(song)
        return gefundene
```

---

## ⏱️ Zeit-Formatierung: Aus Sekunden werden Minuten & Sekunden

Um z.B. `215` Sekunden als `"03:35"` darzustellen, teilt man mit Ganzzahldivision `//` und Modulo `%`:
```python
sekunden_gesamt = 215
minuten = sekunden_gesamt // 60  # 3
sekunden = sekunden_gesamt % 60  # 35

# Mit :02d wird immer zweistellig mit führender Null formatiert:
print(f"{minuten:02d}:{sekunden:02d}")  # "03:35"
```

---

## 🎯 Deine Aufgabe: Der Spotify-Playlist-Manager

In `aufgabe.py` baust du deine eigene Musikverwaltung:
1. **Klasse `Song`**:
   - Attribute: `titel`, `kuenstler`, `dauer_sekunden`
   - Methode: `formatierte_dauer()` -> `"MM:SS"`
   - `__str__()` -> `"{titel}" von {kuenstler} ({MM:SS})`
2. **Klasse `Playlist`**:
   - `song_hinzufuegen(song)`
   - `anzahl_songs()`
   - `gesamtdauer_sekunden()`
   - `finde_songs_von(kuenstler)` (Groß-/Kleinschreibung ignorieren!)
   - `laengster_song()` (liefert das Song-Objekt mit der längsten Dauer)

### Testen:
```bash
python3 test_aufgabe.py
```
