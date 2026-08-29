# Kapitel 18: Funktionale Programmierung & Pythonic Code ⚡🔄

Willkommen zu **Kapitel 18** in **Lehrpfad 4 (Professional Data Engineering)**!
In diesem Modul lernst du, wie du mithilfe funktionaler Konzepte sauberen, ausdrucksstarken und hocheffizienten Python-Code schreibst (*Pythonic Code*).

---

## 🧭 Didaktischer Hintergrund: Die Fließband-Analogie

In der traditionellen (imperativen) Programmierung schreibst du oft lange Schleifen mit Hilfsvariablen, Indizes und Zwischenlisten:
```python
# ❌ Umständlich / Imperativ
ergebnis = []
i = 0
for element in elemente:
    if element % 2 != 0:
        ergebnis.append(element ** 2)
    i += 1
```

> 🏭 **Die Fließband-Analogie:**
> In der funktionalen Programmierung baust du ein **automatisiertes Fließband** auf:
> - **`filter()` (Die Prüfstation):** Lässt nur Elemente durch, die eine Bedingung erfüllen.
> - **`map()` (Die Bearbeitungsstation):** Transformiert jedes durchlaufende Teil.
> - **`zip()` (Die Montagestation):** Führt zwei parallele Bänder paarweise zusammen.
> - **`enumerate()` (Die Etikettierstation):** Versieht jedes Teil mit einer laufenden Nummer.

---

## 🧰 1. Die funktionalen Werkzeuge im Überblick

### A) `enumerate(iterable, start=0)` – Zähler ohne Hilfsvariable
```python
sprachen = ["Python", "Java", "Rust"]

# Mit Startwert 1 nummerieren
for index, sprache in enumerate(sprachen, start=1):
    print(f"{index}. {sprache}")

# Als nummerierte Liste erzeugen:
nummeriert = [f"{i}. {s}" for i, s in enumerate(sprachen, start=1)]
# -> ['1. Python', '2. Java', '3. Rust']
```

---

### B) `zip(*iterables)` – Paralleles Durchlaufen
```python
artikel = ["Apfel", "Banane", "Orange"]
preise = [0.99, 1.49, 1.99]

katalog = dict(zip(artikel, preise))
# -> {'Apfel': 0.99, 'Banane': 1.49, 'Orange': 1.99}
```

---

### C) Anonyme Lambda-Funktionen (`lambda`)
Ein `lambda` ist eine kleine, namenlose Funktion für den Einmalgebrauch:
$$\text{lambda } x: \text{ausdruck}$$

```python
# Normale Funktion:
def verdopple(x):
    return x * 2

# Als Lambda-Einzeiler:
verdopple_lambda = lambda x: x * 2
```

---

### D) `map()` & `filter()` – Die Transformations-Pipeline
```python
zahlen = [1, 2, 3, 4, 5, 6]

# 1. Nur ungerade Zahlen herausfiltern (1, 3, 5)
ungerade = filter(lambda x: x % 2 != 0, zahlen)

# 2. Alle verbliebenen Zahlen quadrieren (1, 9, 25)
quadriert = map(lambda x: x ** 2, ungerade)

ergebnis = list(quadriert)  # -> [1, 9, 25]
```

---

### E) Custom Sorting mit `key=lambda`
Sortiere komplexe Datenstrukturen nach beliebigen Kriterien:
```python
team = [
    {"name": "Alice", "alter": 30, "gehalt": 65000},
    {"name": "Bob", "alter": 22, "gehalt": 48000},
    {"name": "Charlie", "alter": 45, "gehalt": 80000}
]

# Nach Alter aufsteigend sortieren
nach_alter = sorted(team, key=lambda p: p["alter"])

# Nach Gehalt absteigend sortieren
nach_gehalt = sorted(team, key=lambda p: p["gehalt"], reverse=True)

# Höchstverdiener finden
chef = max(team, key=lambda p: p["gehalt"])
```

---

### F) Kontrollfunktionen: `all()` und `any()`
```python
alter_gruppe = [20, 25, 18, 30]

# Sind ALLE Personen mindestens 18?
print(all(alter >= 18 for alter in alter_gruppe)) # -> True

# Gibt es MINDESTENS EINE Person unter 18?
print(any(alter < 18 for alter in alter_gruppe))  # -> False
```

---

## 📑 Vergleich: Imperativ vs. Funktional (Pythonic)

| Anwendungsfall | Imperativ (Klassisch) | Funktional & Pythonic |
| :--- | :--- | :--- |
| **Nummerierung** | `i = 1; for x in l: print(i, x); i += 1` | `for i, x in enumerate(l, 1): print(i, x)` |
| **Paarung** | `for i in range(len(a)): dict[a[i]] = b[i]` | `dict(zip(a, b))` |
| **Transformation** | `res = []; for x in l: res.append(x*2)` | `list(map(lambda x: x*2, l))` |
| **Filterung** | `res = []; for x in l: if x>0: res.append(x)` | `list(filter(lambda x: x>0, l))` |
| **Validierung** | `ok = True; for x in l: if not cond(x): ok=False` | `all(cond(x) for x in l)` |

---

## 📁 Die Dateien in diesem Modul

- **`index.html`**: Interaktive Lernseite mit Cheat-Sheet, Code-Pipelines, Checkliste und aufklappbaren Tipps.
- **`aufgabe.py`**: Dein Arbeitsblatt mit Type Hints und TODOs für `enumerate`, `zip`, `map`/`filter`, `sorted` und `all`/`any`.
- **`test_aufgabe.py`**: Automatische Unittest-Suite zur Validierung deiner Lösungen.
- **`musterloesung.py`**: Vollständig ausprogrammierte Referenzlösung.

---

## 🚀 Schnellstart

```bash
# 1. Bearbeite aufgabe.py
# 2. Führe die automatischen Unittests aus:
python3 test_aufgabe.py

# 3. Oder starte aufgabe.py direkt im Terminal:
python3 aufgabe.py
```
