# Kapitel G07: Listen & Sequenzen in Python 🚂📋

Willkommen im Kapitel **Listen und Sequenzen**! Listen gehören zu den wichtigsten und am häufigsten verwendeten Datenstrukturen in Python. Mit ihnen kannst du mehrere Daten geordnet in einer einzigen Variable speichern.

---

## 🚂 1. Die Zugwaggon-Analogie: Was ist eine Liste?

Stell dir eine Liste wie einen **Zug mit durchnummerierten Waggons** vor:

```text
               ┌───────────┬───────────┬───────────┬───────────┬───────────┐
Werte:         │  "Apfel"  │  "Banane" │  "Kirsche"│  "Dattel" │  "Erdbeere"
               └───────────┴───────────┴───────────┴───────────┴───────────┘
Positiver Index:     0           1           2           3           4
Negativer Index:    -5          -4          -3          -2          -1
```

- **Eckige Klammern `[]`:** Definieren eine Liste (`fruechte = ["Apfel", "Banane", "Kirsche"]`).
- **Indexierung ab 0:** Der erste Waggon ist immer Index `0`!
- **Negativer Index:** `-1` ist immer das letzte Element, `-2` das vorletzte.
- **Veränderbarkeit (mutable):** Du kannst Waggons austauschen, neue anhängen oder abkoppeln!

---

## ✂️ 2. Slicing: Teile einer Liste herausschneiden

Mit dem **Slice-Operator `[start:stop:step]`** kannst du beliebige Abschnitte aus einer Sequenz herausschneiden:

```python
zahlen = [10, 20, 30, 40, 50, 60]

# 1. Bereich von Index 1 bis vor Index 4:
print(zahlen[1:4])   # -> [20, 30, 40]

# 2. Vom Anfang bis vor Index 3:
print(zahlen[:3])    # -> [10, 20, 30]

# 3. Ab Index 3 bis zum Ende:
print(zahlen[3:])    # -> [40, 50, 60]

# 4. Jedes 2. Element (Schrittweite 2):
print(zahlen[::2])   # -> [10, 30, 50]

# 5. Ganze Liste umkehren (Rückwärts-Schritt):
print(zahlen[::-1])  # -> [60, 50, 40, 30, 20, 10]
```

> 💡 **Merke:** Der `stop`-Index ist immer **exklusiv** (wird nicht mehr mitgenommen). `zahlen[1:4]` nimmt also die Indizes 1, 2 und 3.

---

## 🛠️ 3. Die wichtigsten Listen-Methoden

Listen bringen viele eingebaute Methoden mit, um Elemente hinzuzufügen, zu löschen oder zu sortieren:

| Methode | Beschreibung | Beispiel |
| :--- | :--- | :--- |
| `.append(x)` | Fügt `x` ans Ende der Liste an | `tiere.append("Hund")` |
| `.insert(i, x)` | Fügt `x` an Position `i` ein | `tiere.insert(0, "Katze")` |
| `.remove(x)` | Entfernt das erste Vorkommen von `x` | `tiere.remove("Hund")` *(wirft Fehler, wenn `x` fehlt!)* |
| `.pop()` | Entfernt und liefert das letzte Element | `letztes = tiere.pop()` |
| `.pop(i)` | Entfernt und liefert Element an Index `i` | `erstes = tiere.pop(0)` |
| `.sort()` | Sortiert die Liste aufsteigend in-place | `zahlen.sort()` |
| `.reverse()` | Dreht die Liste an Ort und Stelle um | `zahlen.reverse()` |

---

## 🧮 4. Nützliche eingebaute Funktionen & `in`-Operator

Python bietet praktische globale Funktionen für Sequenzen:

```python
noten = [1.5, 2.0, 3.7, 1.0, 2.3]

# Länge (Anzahl der Elemente):
print(len(noten))   # -> 5

# Kleinster und größter Wert:
print(min(noten))   # -> 1.0 (beste Note)
print(max(noten))   # -> 3.7 (schlechteste Note)

# Summe aller Zahlen:
print(sum(noten))   # -> 10.5

# Notendurchschnitt:
schnitt = sum(noten) / len(noten)
print(f"Durchschnitt: {schnitt:.2f}")  # -> 2.10

# Prüfen, ob ein Element enthalten ist:
if 1.0 in noten:
    print("Glückwunsch zur Bestnote!")
```

---

## 🛒 5. Praxisbeispiel: Einkaufsliste verwalten

```python
# ==============================================================================
# Einkaufslisten-Manager
# ==============================================================================
einkauf = ["Milch", "Brot", "Käse"]

# 1. Etwas hinzufügen:
einkauf.append("Äpfel")

# 2. Prüfen und sicher entfernen:
artikel = "Brot"
if artikel in einkauf:
    einkauf.remove(artikel)
    print(f"✅ '{artikel}' wurde eingekauft und abgehakt.")
else:
    print(f"❌ '{artikel}' stand nicht auf der Liste.")

# 3. Sortiert ausgeben:
einkauf.sort()
print("Verbleibende Einkäufe:", einkauf)
```

---

## 🎯 Deine Aufgaben in `aufgabe.py`

Öffne `aufgabe.py` und implementiere die 5 Funktionen:

1. **`liste_umdrehen(liste)`**: Gibt eine neue, umgedrehte Liste zurück, ohne das Original zu verändern.
2. **`filtere_positive_zahlen(zahlen)`**: Filtert nur Zahlen `> 0` heraus.
3. **`entferne_element(liste, element)`**: Entfernt das Element sicher (ohne `ValueError` Absturz) und gibt `True` zurück, wenn es gefunden wurde, sonst `False`.
4. **`mittlere_elemente(liste)`**: Schneidet mit Slicing das erste und letzte Element ab. Bei `<= 2` Elementen wird `[]` zurückgegeben.
5. **`noten_durchschnitt_ohne_ausreisser(noten)`**: Entfernt Minimum und Maximum aus einer Kopie der Liste und berechnet den bereinigten Schnitt.

### Testen deiner Lösung:
```bash
python3 test_aufgabe.py
```
