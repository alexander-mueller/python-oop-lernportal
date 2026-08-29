# Kapitel 01: Die erste Klasse – Was sind Klassen & Objekte? 🐶🐱

Herzlich willkommen in der Welt der objektorientierten Programmierung (kurz: **OOP**)!

Bisher hast du in Python mit Variablen, Listen, Dictionaries und Funktionen gearbeitet. Das hat super funktioniert! Doch wenn Programme größer werden, wird es schnell unübersichtlich.

Mit **Klassen** lernst du jetzt, wie du deine eigenen, maßgeschneiderten Datentypen erstellst.

---

## 🏗️ Die wichtigste Analogie: Bauplan vs. Objekt

Stell dir vor, du bist Architektin oder Bäckermeisterin:
- Eine **Klasse** ist wie ein **Bauplan** für ein Haus (oder eine **Plätzchen-Ausstechform**). Der Bauplan selbst ist noch kein Haus, in dem man wohnen kann. Er beschreibt nur: *Wie sieht ein Haus aus? Welche Eigenschaften hat es?*
- Ein **Objekt** (auch **Instanz** genannt) ist das **echte Haus**, das nach diesem Bauplan gebaut wurde (oder das gebackene Plätzchen). Aus *einem* Bauplan kannst du beliebig viele verschiedene Häuser bauen!

```
       [ KLASSE / BAUPLAN ]
         class Haustier:
               │
      ─────────┴─────────
     │                   │
[ OBJEKT 1 ]        [ OBJEKT 2 ]
Bello, Hund, 3      Mimi, Katze, 5
```

---

## 🔍 Warum nicht einfach Dictionaries?

Bisher hättest du Tiere vielleicht so gespeichert:
```python
tier1 = {"name": "Bello", "tierart": "Hund", "alter": 3}
tier2 = {"name": "Mimi", "art": "Katze", "alter": 5} # Ups! Hier heißt der Key "art" statt "tierart"!
```
Beim Dictionary kann man sich schnell bei Schlüsseln vertippen. Eine Klasse gibt uns eine feste Struktur vor.

---

## 🌟 Vollständiges Praxisbeispiel: Der Fahrrad-Verleih

Hier siehst du ein komplettes, funktionierendes Beispiel:

```python
# 1. Bauplan definieren:
class Fahrrad:
    pass

# 2. Hilfsfunktion, die mit Fahrrad-Objekten arbeitet:
def fahrrad_info(bike):
    return f"{bike.marke} ({bike.farbe}) - {bike.gaenge} Gänge - {bike.preis_pro_tag}€/Tag"

# 3. Zwei konkrete Fahrräder (Objekte) erstellen:
mountainbike = Fahrrad()
mountainbike.marke = "Cube"
mountainbike.farbe = "Schwarz/Grün"
mountainbike.gaenge = 21
mountainbike.preis_pro_tag = 25.0

citybike = Fahrrad()
citybike.marke = "Gazelle"
citybike.farbe = "Himmelblau"
citybike.gaenge = 7
citybike.preis_pro_tag = 15.0

# 4. Ausgabe:
print("Rad 1:", fahrrad_info(mountainbike))
print("Rad 2:", fahrrad_info(citybike))
```

---

## ⚠️ Häufige Stolperfallen für Einsteiger

1. **Klammern beim Erstellen nicht vergessen:**
   - `bello = Haustier()` erzeugt ein neues Objekt.
   - `bello = Haustier` (ohne Klammern) würde die Klasse selbst speichern, kein neues Objekt erzeugen!
2. **Groß- und Kleinschreibung:**
   - Klassen werden per Konvention in **CamelCase** mit großem Anfangsbuchstaben geschrieben: `class Haustier:`, `class Fahrrad:`.
   - Variablen und Funktionen schreibt man klein: `mein_tier`, `fahrrad_info()`.
3. **`return` in Funktionen nicht vergessen:**
   - Wenn deine Funktion ein neu gebautes Haustier erzeugen soll, muss am Ende `return tier` stehen, sonst gibt die Funktion `None` zurück.

---

## 🎯 Deine Aufgaben in `aufgabe.py`

Öffne die Datei `aufgabe.py` und bearbeite die nummerierten TODOs:
1. **TODO 1:** Definiere die leere Klasse `Haustier`.
2. **TODO 2:** Schreibe die Funktion `erstelle_bello()`.
3. **TODO 3:** Schreibe die Funktion `erstelle_mimi()`.
4. **TODO 4:** Schreibe die Funktion `steckbrief_text(haustier)`.
5. **TODO 5:** Schreibe die Funktion `aelteres_tier(tier1, tier2)`.

### Testen:
```bash
python3 test_aufgabe.py
```
Sobald alle Tests mit `OK` durchlaufen, bist du bereit für Kapitel 02!
