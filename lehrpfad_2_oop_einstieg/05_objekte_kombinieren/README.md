# Kapitel 05: Komposition – Objekte kombinieren & filtern 🎵

In der echten Softwareentwicklung (wie bei Spotify, Instagram oder Netflix) besteht ein System fast immer aus vielen verschiedenen Klassen, die zusammenarbeiten.

Wenn eine Klasse andere Objekte besitzt oder verwaltet, nennt man das **Komposition** (oder *"hat-ein"-Beziehung*):
- Eine **Playlist** *hat viele* **Songs**.
- Eine **Schulklasse** *hat viele* **Schüler**.
- Ein **Kino** *hat viele* **Säle** und **Filme**.

---

## 🎒 Vollständiges Praxisbeispiel: Der Schüler- & Notenmanager

```python
# 1. Klasse Schueler
class Schueler:
    def __init__(self, name, note):
        self.name = name
        self.note = float(note)

    def __str__(self):
        return f"{self.name} (Note: {self.note:.1f})"

# 2. Klasse Schulklasse verwaltet viele Schüler-Objekte:
class Schulklasse:
    def __init__(self, klassen_name):
        self.klassen_name = klassen_name
        self.schueler_liste = []

    def hinzufuegen(self, schueler):
        self.schueler_liste.append(schueler)

    def notendurchschnitt(self):
        if not self.schueler_liste:
            return 0.0
        summe = sum(s.note for s in self.schueler_liste)
        return summe / len(self.schueler_liste)

# Testen:
klasse_9a = Schulklasse("Klasse 9a")
klasse_9a.hinzufuegen(Schueler("Emma", 1.0))
klasse_9a.hinzufuegen(Schueler("Lukas", 2.3))
klasse_9a.hinzufuegen(Schueler("Mia", 1.3))

print("Durchschnitt:", klasse_9a.notendurchschnitt())
```

---

## ⏱️ Zeit-Formatierung: Aus Sekunden werden Minuten & Sekunden

```python
minuten = self.dauer_sekunden // 60
sekunden = self.dauer_sekunden % 60
return f"{minuten:02d}:{sekunden:02d}"  # "03:35"
```

---

## 🎯 Deine Aufgabe: Der Spotify-Playlist-Manager

In `aufgabe.py` baust du deine eigene Musikverwaltung mit `Song` und `Playlist`.

### Testen:
```bash
python3 test_aufgabe.py
```
