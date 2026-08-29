# Kapitel G06: Eigene Funktionen & Module 🪄📦

Willkommen zu **Kapitel G06** unseres Python-Grundlagen-Lehrpfads!
Dieses Kapitel entspricht den Modulen **05.0 & 05.1** deines Informatik-Skriptums.

Bis jetzt hast du vorgefertigte Funktionen wie `print()`, `len()` oder `range()` genutzt. Jetzt lernst du, wie du **deine eigenen Funktionen schreibst** und mächtige **Module der Standardbibliothek** (wie `math` und `random`) einbindest.

---

## 🪄 Die Fabrik- / Zauberkisten-Analogie

Stell dir eine Funktion wie eine kleine Fabrikmaschine (oder einen Zauberkasten) vor:

```
    [ INPUT / ZUTATEN ]
  (Parameter: z.B. a=3, b=4)
             │
             ▼
┌─────────────────────────┐
│     EIGENE FUNKTION     │
│   def hypotenuse(a, b): │  <─── VERARBEITUNG (Black Box)
│   c = math.sqrt(...)    │
└────────────┬────────────┘
             │
             ▼
    [ OUTPUT / PRODUKT ]
      (return 5.0)
```

1. **Input (Parameter):** Was die Funktion braucht, um zu arbeiten (z.B. zwei Zahlen).
2. **Verarbeitung:** Der Code innerhalb der Funktion, der die Berechnung durchführt.
3. **Output (`return`):** Das fertige Ergebnis, das die Funktion an den Aufrufer zurückgibt.

---

## 1. Funktionen definieren: `def` & Standardwerte

```python
# Definition mit Parametern und Standardwert (Default Argument):
def begruesse(name: str, titel: str = "Frau/Herr") -> str:
    return f"Guten Tag, {titel} {name}!"

# Aufruf mit beiden Argumenten:
print(begruesse("Müller", "Dr."))    # "Guten Tag, Dr. Müller!"

# Aufruf ohne Standardwert (nimmt Default "Frau/Herr"):
print(begruesse("Schmidt"))          # "Guten Tag, Frau/Herr Schmidt!"
```

---

## 2. Der fundamentale Unterschied: `return` vs. `print()`

Das ist der mit Abstand häufigste Anfängerfehler:

| Eigenschaft | `print()` 🖨️ | `return` 📦 |
| :--- | :--- | :--- |
| **Was passiert?** | Schreibt nur Text auf den Bildschirm. | Übergibt das echte Ergebnis zurück an das Programm. |
| **Weiterverwendung?** | **NEIN!** Das Ergebnis ist für das Programm verloren (`None`). | **JA!** Du kannst das Ergebnis in Variablen speichern, weiterrechnen oder vergleichen. |
| **Analogie:** | Du liest den Kassenzettel im Supermarkt. | Du nimmst die gekaufte Ware mit nach Hause! |

```python
# ❌ Falsch: Mit print kann man nicht weiterrechnen!
def verdopple_falsch(x):
    print(x * 2)

ergebnis = verdopple_falsch(5)  # Gibt 10 auf dem Bildschirm aus
# print(ergebnis + 5)          # 💥 TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'!

# ✅ Richtig: Mit return kann man das Ergebnis weiterverwenden!
def verdopple_richtig(x):
    return x * 2

ergebnis = verdopple_richtig(5)  # ergebnis ist jetzt 10
print(ergebnis + 5)             # Funktioniert perfekt -> 15!
```

---

## 3. Mehrere Rückgabewerte (Tupel-Return)

In Python kann eine Funktion problemlos **mehrere Werte gleichzeitig** zurückgeben. Python packt sie automatisch in ein **Tupel**:

```python
def min_und_max(zahlen: list[float]) -> tuple[float, float]:
    kleinste = min(zahlen)
    groesste = max(zahlen)
    return kleinste, groesste  # Gibt (kleinste, groesste) zurück

# Tuple-Unpacking (Entpacken in zwei separate Variablen):
tiefst, hoechst = min_und_max([12.5, 3.2, 19.8, -1.0])
print(f"Tiefstwert: {tiefst}, Höchstwert: {hoechst}")
```

---

## 4. Lokaler vs. Globaler Gültigkeitsbereich (Scope) 🏠

Variablen, die du **innerhalb** einer Funktion erstellst, sind **lokal**. Sie existieren nur so lange, wie die Funktion ausgeführt wird:

```python
def meine_funktion():
    geheime_zahl = 42   # Lokale Variable!
    print("In der Funktion:", geheime_zahl)

meine_funktion()
# print(geheime_zahl)   # 💥 NameError: name 'geheime_zahl' is not defined!
```

> **Die Hotelzimmer-Regel:** Was im Hotelzimmer (der Funktion) liegt, sieht man von außen auf der Straße nicht.

---

## 5. Module nutzen: `math` & `random` 🧰

Python hat eine riesige "Werkzeugkiste" an eingebauten Modulen (Standard Library), die du einfach mit `import` laden kannst:

### Das `math`-Modul (Mathematische Werkzeuge):
```python
import math

print(math.sqrt(25))     # Quadratwurzel -> 5.0
print(math.pi)           # Kreiszahl Pi -> 3.141592653589793
print(math.pow(2, 3))    # Potenz 2^3 -> 8.0
print(math.floor(4.9))   # Abrunden -> 4
print(math.ceil(4.1))    # Aufrunden -> 5
```

### Das `random`-Modul (Zufallszahlen & Würfel):
```python
import random

# Zufällige ganze Zahl zwischen 1 und 6 (beide inklusive):
wuerfelwurf = random.randint(1, 6)

# Zufällige Kommazahl zwischen 0.0 und 1.0:
zufall = random.random()

# Zufälliges Element aus einer Liste wählen:
farben = ["rot", "grün", "blau", "gelb"]
gluecksfarbe = random.choice(farben)
```

---

## ⚠️ Die 3 häufigsten Anfängerfehler

1. **`return` vergessen oder durch `print()` ersetzt:**
   - Deine Funktion berechnet etwas, gibt es aber nicht an den Aufrufer zurück. Ergebnis ist `None`.
2. **Auf lokale Variablen von außen zugreifen:**
   - Variablen innerhalb von Funktionen existieren außerhalb nicht.
3. **Falsche Modul-Namen oder Funktionen:**
   - Achte auf die Schreibweise: `math.sqrt()` (nicht `math.square_root()`) und `random.randint(1, 6)` (nicht `random.random_int()`).

---

## 🎯 Deine Aufgaben in `aufgabe.py`

Öffne `aufgabe.py` und bearbeite die nummerierten TODOs:
1. **TODO 1:** `hypotenuse(a: float, b: float) -> float` – Satz des Pythagoras mit `math.sqrt`.
2. **TODO 2:** `zylinder_volumen(radius: float, hoehe: float) -> float` – Zylindervolumen mit `math.pi`.
3. **TODO 3:** `wuerfle_wuerfel(anzahl: int, seiten: int = 6) -> list[int]` – Würfelsimulator mit `random.randint` und Standardwert `seiten=6`.
4. **TODO 4:** `statistik(zahlen: list[float]) -> tuple[float, float, float]` – Berechnet `(min, max, mittelwert)` als Tupel.

### Testen:
```bash
python3 test_aufgabe.py
```
Sobald alle 7 Tests erfolgreich durchlaufen (`OK`), hast du Funktionen und Module gemeistert!
