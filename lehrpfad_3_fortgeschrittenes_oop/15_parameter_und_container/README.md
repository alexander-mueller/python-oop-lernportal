# Kapitel 15: Parameter (*args, **kwargs) & Eigene Container 🎒📦

Willkommen zu **Kapitel 15**! In diesem Modul meisterst du zwei der mächtigsten und flexibelsten Sprachfeatures von Python:
1. **Variable Parameterlisten** (`*args` und `**kwargs`) sowie **Argument-Unpacking** (`*liste`, `**dict`).
2. **Eigene Container-Klassen**, die sich dank magischer **Dunder-Methoden** genau wie Pythons eingebaute Listen und Dictionaries verhalten (`len()`, `[]`, `del`, `in`, `for`).

---

## 🧭 Didaktischer Hintergrund (Schulabgleich 29.0 & 30.0)

In der professionellen Softwareentwicklung und im Lehrplan sind flexible Schnittstellen und eigene Datenstrukturen essenziell:
- **Schulabgleich 29.0:** Variable Parameterlisten (`*args`, `**kwargs`) und Argument-Unpacking.
- **Schulabgleich 30.0:** Eigene Sequenzen und Container-Klassen mit dem Python-Container-Protokoll (`__len__`, `__getitem__`, `__setitem__`, `__delitem__`, `__contains__`, `__iter__`).

---

## 🧰 1. Variable Parameterlisten: `*args` und `**kwargs`

Normalerweise hat eine Python-Funktion eine feste Anzahl von Parametern:
```python
def addiere_zwei(a: float, b: float) -> float:
    return a + b
```
Was aber, wenn du eine Funktion schreiben möchtest, die **2, 5 oder 100 Zahlen** zusammenrechnet? Oder eine Funktion, die beliebige Spieler-Attribute entgegennimmt?

---

### A) `*args` (Beliebig viele Positionsargumente als Tupel)
Das Sternchen `*` vor einem Parameternamen signalisiert Python: *„Sammle alle überschüssigen Positionsargumente in einem unveränderlichen **Tupel**!“*

```python
def berechne_summe(*zahlen: float) -> float:
    print(type(zahlen))  # <class 'tuple'>
    return sum(zahlen)

print(berechne_summe(10, 20))            # -> 30 (zahlen ist (10, 20))
print(berechne_summe(1, 2, 3, 4, 5))     # -> 15 (zahlen ist (1, 2, 3, 4, 5))
print(berechne_summe())                  # -> 0  (zahlen ist ())
```

> 💡 **Analogie:** `*args` ist wie ein **unendlicher Werkzeuggürtel**. Egal ob du 1 Schraubendreher oder 10 Hämmer hineinsteckst – alle werden gebündelt in ein Tupel gelegt.

---

### B) `**kwargs` (Beliebig viele Schlüsselwortargumente als Dict)
Zwei Sternchen `**` signalisieren Python: *„Sammle alle benannten Argumente (`schluessel=wert`) in einem **Dictionary**!“*

```python
def erstelle_held(name: str, **attribute) -> dict:
    print(type(attribute))  # <class 'dict'>
    return {"name": name, **attribute}

held = erstelle_held("Legolas", klasse="Waldlaeufer", level=15, waffe="Elbenbogen")
# -> {'name': 'Legolas', 'klasse': 'Waldlaeufer', 'level': 15, 'waffe': 'Elbenbogen'}
```

> 💡 **Analogie:** `**kwargs` ist wie ein **ausfüllbares Formular**. Der Aufrufer kann beliebig viele zusätzliche Zeilen mit Label und Wert ergänzen.

---

### C) Die goldene Reihenfolge bei Parametern
Wenn du normale Parameter, `*args`, Default-Werte und `**kwargs` kombinierst, gilt stets diese feste Reihenfolge:

```python
def super_funktion(pos1, pos2, *args, standard_wert=10, **kwargs):
    pass
```

1. **Positionsargumente** (`pos1`, `pos2`)
2. **`*args`** (Restliche Positionsargumente)
3. **Keyword-Only / Default-Parameter** (`standard_wert=10`)
4. **`**kwargs`** (Restliche Keyword-Argumente)

---

## 🎁 2. Argument-Unpacking: `*liste` und `**dict`

Der Stern-Operator funktioniert nicht nur bei der **Definition** von Funktionen (Packen), sondern auch beim **Aufruf** (Entpacken / Unpacking):

```python
# 1. Listen-Unpacking mit *
preise = [19.99, 49.99, 9.99]
# Statt berechne_summe(preise[0], preise[1], preise[2]):
gesamt = berechne_summe(*preise)

# 2. Dictionary-Unpacking mit **
config = {"klasse": "Magier", "level": 20, "element": "Feuer"}
# Statt erstelle_held("Merlin", klasse="Magier", level=20, element="Feuer"):
magier = erstelle_held("Merlin", **config)
```

---

## 🎒 3. Eigene Container-Klassen mit Dunder-Methoden

Warum fühlt sich Python so elegant an? Weil eingebaute Typen (`list`, `dict`) und eigene Klassen **exakt dieselben Operatoren** nutzen können!

Wenn du eine Klasse `Inventar` erstellst, möchtest du:
- `len(inventar)` statt `inventar.get_anzahl()`
- `inventar[0]` oder `inventar["Schwert"]` statt `inventar.get_element(0)`
- `inventar[0] = trank` statt `inventar.set_element(0, trank)`
- `del inventar["Schwert"]` statt `inventar.remove_element("Schwert")`
- `'Heiltrank' in inventar` statt `inventar.enthaelt("Heiltrank")`
- `for item in inventar:` statt umständlicher Index-Schleifen

### Die magischen Container-Dunder im Überblick:

| Dunder-Methode | Ausgelöst durch | Zweck |
| :--- | :--- | :--- |
| `__len__(self)` | `len(container)` | Gibt die Anzahl der Elemente als `int` zurück. |
| `__getitem__(self, key)` | `container[key]` | Liest Element an Index `key` (z.B. int `0` oder str `"Schwert"`). |
| `__setitem__(self, key, val)` | `container[key] = val` | Setzt/Ersetzt Element an Index `key`. |
| `__delitem__(self, key)` | `del container[key]` | Löscht das Element an Index `key`. |
| `__contains__(self, item)` | `item in container` | Gibt `True` zurück, wenn `item` enthalten ist, sonst `False`. |
| `__iter__(self)` | `for x in container:` | Gibt einen Iterator zurück (`iter(self._items)`). |

---

## 🎮 4. Praxisbeispiel: Das Gaming-Inventar

In `aufgabe.py` baust du das RPG-Inventar eines Helden:

```
┌────────────────────────────────────────────────────────┐
│   🎒 Inventar (Maximalgewicht: 20.0 kg)               │
│   ├── [0] Eisenschwert (3.5 kg, 120 G)                │
│   ├── [1] Holzschild (2.0 kg, 45 G)                   │
│   └── [2] Heiltrank (0.5 kg, 20 G)                    │
│   ─────────────────────────────────────────────────   │
│   Gesamtgewicht: 6.0 / 20.0 kg (Frei: 14.0 kg)        │
│   len(inv) -> 3                                       │
│   "Eisenschwert" in inv -> True                       │
│   inv["Heiltrank"] -> Gegenstand('Heiltrank', ...)    │
└────────────────────────────────────────────────────────┘
```

---

## 📁 Die Dateien in diesem Ordner

- **`index.html`**: Interaktive Web-Lernseite mit visuellen Tabellen, Rucksack-Analogie, Cheat-Sheets und Checkliste.
- **`aufgabe.py`**: Dein Arbeitsblatt mit Type Hints und TODOs für `*args`, `**kwargs` und die Klasse `Inventar`.
- **`test_aufgabe.py`**: Automatische Unittest-Suite zur Überprüfung aller Anforderungen.
- **`musterloesung.py`**: Vollständig ausprogrammierte Referenzlösung.

---

## 🚀 Schnellstart

```bash
# 1. Bearbeite aufgabe.py
# 2. Führe die automatischen Tests aus:
python3 test_aufgabe.py

# 3. Oder starte aufgabe.py direkt:
python3 aufgabe.py
```
