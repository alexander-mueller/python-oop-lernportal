# Kapitel G10: Comprehensions, Datum & Algorithmen 🚀📅

Schulabgleich: **Thema 13.0 (Algorithmen & Datumsverarbeitung) & 15.1 (Comprehensions)**

Herzlich willkommen zum krönenden Abschluss des Grundlagen-Lehrpfads! In diesem Kapitel lernst du drei essenzielle Werkzeuge kennen, die dich von einer Programmieranfängerin zu einer echten Python-Entwicklerin machen:
1. **List & Dict Comprehensions** (Eleganter, kompakter Code in einer Zeile)
2. **Datum & Uhrzeit** mit dem `datetime`-Modul (Rechnen mit Zeitspannen & Kalendern)
3. **Praktische Algorithmen** (Suchen, Filtern, Sortieren mit `key=` und Min/Max-Findung)

---

## ⚡ 1. List Comprehensions: Das Schnellschienen-Fließband

Bisher hast du neue Listen oft mit einer leeren Liste und einer `for`-Schleife befüllt:

```python
# 🐢 Der traditionelle Weg (4 Zeilen):
quadrate = []
for x in range(1, 6):
    if x % 2 == 0:
        quadrate.append(x ** 2)
```

Mit einer **List Comprehension** schreibst du das in **einer einzigen, glasklaren Zeile**:

```python
# 🚀 Der Pythonic Weg mit List Comprehension:
quadrate = [x ** 2 for x in range(1, 6) if x % 2 == 0]
# Ergebnis: [4, 16]
```

### Die Anatomie einer List Comprehension:
```
[  WAS_REIN_SOLL   for   VARIABLE   in   QUELLE   if   BEDINGUNG  ]
   (Ausdruck / Map)        (x)            (Liste)        (Filter)
```

### Auch für Dictionaries: Dict Comprehensions
Genauso kannst du blitzschnell Dictionaries erzeugen:
```python
woerter = ["Apfel", "Banane", "Erdbeere"]
wort_laengen = {w: len(w) for w in woerter}
# Ergebnis: {'Apfel': 5, 'Banane': 6, 'Erdbeere': 8}
```

---

## 📅 2. Datum & Uhrzeit mit dem `datetime`-Modul

In der echten Softwareentwicklung (z.B. bei Buchungs-Systemen, Online-Shops oder Kalendern) musst du ständig mit Zeitangaben rechnen. Python bringt dafür das mächtige Modul `datetime` mit.

```python
from datetime import datetime, date, timedelta

# 1. Aktuelles Datum & Uhrzeit:
heute = date.today()          # z.B. 2026-08-29
jetzt = datetime.now()        # z.B. 2026-08-29 14:30:00

# 2. Rechnen mit Zeitspannen (timedelta):
in_einer_woche = heute + timedelta(days=7)
gestern = heute - timedelta(days=1)

# 3. Differenz zwischen zwei Daten berechnen:
silvester = date(2026, 12, 31)
tage_rest = (silvester - heute).days
print(f"Noch {tage_rest} Tage bis Silvester!")
```

### Formatieren (`strftime`) & Einlesen (`strptime`)

- **`strftime` (String Format Time):** Wandelt ein Datumsobjekt in einen formatierten Text um.
- **`strptime` (String Parse Time):** Liest einen Text ein und baut daraus ein Datumsobjekt.

```python
# Objekt -> Formatierter String:
datum = date(2026, 8, 29)
deutsch = datum.strftime("%d.%m.%Y")  # "29.08.2026"

# String -> Datumsobjekt:
text = "2026-12-24"
weihnachten = datetime.strptime(text, "%Y-%m-%d").date()
```

| Platzhalter | Bedeutung | Beispiel |
| :--- | :--- | :--- |
| `%d` | Tag des Monats (01 - 31) | `29` |
| `%m` | Monat als Zahl (01 - 12) | `08` |
| `%Y` | Jahr vierstellig | `2026` |
| `%H` | Stunde (00 - 23) | `14` |
| `%M` | Minute (00 - 59) | `35` |
| `%S` | Sekunde (00 - 59) | `09` |

---

## 🧠 3. Grundlegende Algorithmen: Suchen, Finden & Sortieren

### A. Lineare Suche
Wenn du ein Element in einer Liste suchst, durchläufst du die Liste von vorne nach hinten:

```python
def finde_person(personen, gesuchter_name):
    for person in personen:
        if person["name"] == gesuchter_name:
            return person
    return None
```

### B. Maximum & Minimum mit Schlüssel (`key=`)
Wie findet man die älteste Person oder das teuerste Produkt?

```python
gruppe = [
    {"name": "Anna", "alter": 25},
    {"name": "Ben", "alter": 32},
    {"name": "Clara", "alter": 19}
]

# Die Person mit dem höchsten Alter:
aelteste = max(gruppe, key=lambda person: person["alter"])
print("Älteste Person:", aelteste["name"])  # "Ben"

# Sortieren nach Alter aufsteigend:
sortiert = sorted(gruppe, key=lambda p: p["alter"])
```

---

## 🎯 Deine Aufgaben in `aufgabe.py`

Öffne die Datei `g10_comprehensions_datum_algorithmen/aufgabe.py` und löse die 5 TODOs:

1. **TODO 1 (`quadratzahlen_gerade`):** Berechne die Quadrate aller geraden Zahlen mit einer List Comprehension.
2. **TODO 2 (`filtriere_lange_woerter`):** Filtere Wörter heraus, deren Länge `>= min_laenge` ist.
3. **TODO 3 (`tage_bis_datum`):** Berechne die Anzahl der Tage von heute bis zu einem Zieldatum (`YYYY-MM-DD`).
4. **TODO 4 (`formatiere_deutsches_datum`):** Formatiere ein Datumsobjekt in das Format `DD.MM.YYYY`.
5. **TODO 5 (`finde_aelteste_person`):** Finde in einer Liste von Personen-Dictionaries den Namen der ältesten Person.

### Testen:
```bash
python3 test_aufgabe.py
```
Sobald alle Tests `OK` sind, hast du den gesamten Grundlagen-Pfad erfolgreich abgeschlossen! 🏆🎉
