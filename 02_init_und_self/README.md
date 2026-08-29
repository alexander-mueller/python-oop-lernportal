# Kapitel 02: Der Konstruktor `__init__` und das geheimnisvolle `self` 💳

Im ersten Kapitel haben wir Attribute noch manuell nach dem Erstellen zugewiesen:
```python
bello = Haustier()
bello.name = "Bello"
bello.alter = 3
```
Das ist mühsam und fehleranfällig: Was passiert, wenn man vergisst, `.alter` zu setzen? Richtig: Das Programm stürzt ab, sobald jemand darauf zugreift!

Deshalb gibt es in Python den **Konstruktor**: `__init__`.

---

## 🛠️ Was ist `__init__`?

`__init__` steht für *initialisieren* (vorbereiten/startklar machen). 

Es ist eine **spezielle Methode**, die Python **automatisch aufruft**, sobald du ein neues Objekt erstellst:

```python
class Haustier:
    def __init__(self, name, tierart, alter):
        self.name = name
        self.tierart = tierart
        self.alter = alter

# Jetzt können wir die Werte direkt in die Klammern schreiben!
bello = Haustier("Bello", "Hund", 3)
mimi = Haustier("Mimi", "Katze", 5)

print(bello.name)  # Gibt sofort "Bello" aus
```
Die doppelten Unterstriche `__` nennt man in Python auch **Dunder** (Double Underscore). Sie signalisieren besondere Python-Funktionen.

---

## 🪞 Was bedeutet eigentlich `self`?

`self` verwirrt am Anfang fast jeden – ist aber ganz einfach:
- `self` bedeutet auf Deutsch **"ich selbst"** oder **"dieses Objekt hier"**.
- Wenn du `bello = Haustier("Bello", "Hund", 3)` aufrufst, übergibt Python das neu entstandene `bello`-Objekt automatisch als erstes Argument `self`.
- `self.name = name` bedeutet also: *"Speichere den übergebenen Namen in MEINEM EIGENEN Attribut `.name` ab!"*

```
          Haustier("Bello", "Hund", 3)
                    │
                    ▼
def __init__(self, name, tierart, alter):
             ▲      │       │       │
             │      ▼       ▼       ▼
           bello  "Bello" "Hund"    3
             │
             ├── bello.name = "Bello"
             ├── bello.tierart = "Hund"
             └── bello.alter = 3
```

---

## ⚙️ Standardwerte (Default Parameters)

Manchmal hat ein Attribut einen typischen Startwert (z.B. ein neues Bankkonto startet meist bei `0.0` Euro):

```python
class Bankkonto:
    def __init__(self, inhaber, kontostand=0.0):
        self.inhaber = inhaber
        self.kontostand = kontostand

# Konto mit 0.0 Euro Startguthaben:
k1 = Bankkonto("Anna")

# Konto mit speziellem Startguthaben:
k2 = Bankkonto("Ben", 50.0)
```

---

## ⚠️ Typische Fehler vermeiden

1. **`__init__` mit zwei Unterstrichen schreiben:**
   - ❌ `def _init_(self):` (wird nicht aufgerufen!)
   - ✅ `def __init__(self):` (korrekt!)
2. **`self` bei jeder Methode als ersten Parameter:**
   - ❌ `def einzahlen(betrag):` -> führt zu `TypeError: einzahlen() takes 1 positional argument but 2 were given`
   - ✅ `def einzahlen(self, betrag):`
3. **Zuweisungsrichtung beachten:**
   - ❌ `inhaber = self.inhaber` (falsch herum!)
   - ✅ `self.inhaber = inhaber` (speichert den Parameter im Attribut)

---

## 🎯 Deine Aufgabe: Das Bankkonto

Öffne `aufgabe.py`. Du programmierst eine Klasse `Bankkonto`:
1. Schreibe den Konstruktor `__init__`.
2. Ergänze Methoden zum Einzahlen (`einzahlen`) und Auszahlen (`auszahlen`), die darauf achten, dass man nicht ins Minus rutscht.
3. Ergänze eine Methode `info_text()`.

### Testen:
```bash
python3 test_aufgabe.py
```
