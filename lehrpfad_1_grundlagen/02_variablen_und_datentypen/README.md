# Grundlagen 02: Variablen & Datentypen 📦🏷️ (Schulabgleich 03.0 & 03.1)

In diesem Kapitel lernst du, wie Python Daten im Arbeitsspeicher speichert, welche 4 Basisdatentypen es gibt, wie Type Hints funktionieren und wie du Typen sicher umwandelst (Type Casting).

---

## 📦 1. Was ist eine Variable? (Die Speicherbox-Analogie)

Stell dir den Arbeitsspeicher deines Computers wie ein großes Lagerregal voller **Aufbewahrungsboxen** vor:
- Der **Wert** (z.B. `18` oder `"Anna"`) liegt in der Box.
- Die **Variable** ist das **Namensschild / Etikett**, das du außen an die Box klebst.
- Über das Etikett kannst du jederzeit auf den Inhalt zugreifen oder einen neuen Wert hineinlegen!

```python
# Zuweisungs-Operator '=' klebt das Etikett 'alter' an den Wert 16:
alter = 16

# Später Geburtstag feiern – Wert in der Box aktualisieren:
alter = alter + 1   # Jetzt ist alter 17!
```

---

## 🏷️ 2. Die 4 Basisdatentypen in Python

Python besitzt 4 grundlegende Datentypen, die du blind beherrschen musst:

| Datentyp | Deutscher Begriff | Python-Typ | Beispiele | Erklärung |
| :--- | :--- | :---: | :--- | :--- |
| **Ganzzahl** | Ganze Zahl | `int` | `42`, `-7`, `0`, `1000` | Zahlen ohne Kommastelle |
| **Kommazahl** | Gleitkommazahl | `float` | `3.14`, `-0.5`, `2.0` | Zahlen mit Dezimalpunkt `.` |
| **Text** | Zeichenkette / String | `str` | `"Hallo"`, `'Python'`, `"123"` | Zeichen in einfachen `'` oder doppelten `"` Anführungszeichen |
| **Wahrheitswert** | Boolescher Wert | `bool` | `True`, `False` | Genau zwei Zustände: Wahr oder Falsch |

---

## 🔍 3. Typprüfung mit `type()` & Moderne Type Hints

### Typ abfragen:
Mit der Funktion `type(wert)` kannst du herausfinden, welcher Datentyp vorliegt:
```python
print(type(42))       # <class 'int'>
print(type(3.14))     # <class 'float'>
print(type("Hallo"))  # <class 'str'>
print(type(True))     # <class 'bool'>
```

### Type Hints (Typ-Annotationen):
In modernem Python (und in deinem Schulskriptum!) dokumentieren wir Variablen und Funktionsparameter mit Typ-Hinweisen:
```python
name: str = "Alice"
alter: int = 16
preis: float = 19.99
ist_aktiv: bool = True

def begruessen(benutzer: str, wiederholungen: int) -> str:
    return (benutzer + "! ") * wiederholungen
```

---

## 🔄 4. Typumwandlung (Type Casting)

Manchmal liegt ein Wert im falschen Format vor (z.B. `"42"` als Text statt Zahl). Mit den Typ-Funktionen kannst du Daten umwandeln:

```python
# Text zu Ganzzahl:
zahl = int("42")          # 42 (int)

# Text zu Kommazahl:
pi = float("3.14")        # 3.14 (float)

# Zahl zu Text:
text = str(100)           # "100" (str)

# Zu Wahrheitswert (bool):
b1 = bool(1)              # True (alles außer 0 ist True)
b2 = bool(0)              # False
b3 = bool("")             # False (leerer String ist False)
b4 = bool("Python")       # True
```

---

## ⚠️ 5. Die klassische Anfängerfalle: `"10" + "20"` vs. `10 + 20`

Der Plus-Operator `+` verhält sich bei Texten ganz anders als bei Zahlen!

```python
# ❌ Text-Verkettung (String-Konkatenation):
ergebnis_text = "10" + "20"
print(ergebnis_text)      # Ausgabe: "1020"

# ✅ Mathematische Addition:
ergebnis_zahl = 10 + 20
print(ergebnis_zahl)      # Ausgabe: 30

# ✅ Aus Texten echte Zahlen machen vor der Addition:
text_a = "10"
text_b = "20"
richtig = int(text_a) + int(text_b)
print(richtig)            # Ausgabe: 30
```

---

## 🎯 Deine Aufgaben in `aufgabe.py`

Öffne die Datei `aufgabe.py` und bearbeite die folgenden 4 TODOs:
1. **TODO 1: `bestimme_typ_name(wert)`** $\rightarrow$ Gibt `"Wahrheitswert"`, `"Ganzzahl"`, `"Kommazahl"`, `"Text"` oder `"Unbekannt"` zurück.
2. **TODO 2: `summe_aus_texten(text_a, text_b)`** $\rightarrow$ Wandelt zwei Zahlen-Strings in `int` um und gibt die mathematische Summe zurück.
3. **TODO 3: `formatiere_preis(preis_float)`** $\rightarrow$ Formatiert einen Preis auf 2 Nachkommastellen mit Euro-Zeichen (z.B. `19.99 €`).
4. **TODO 4: `ist_volljaehrig(alter) -> bool`** $\rightarrow$ Gibt `True` ab 18 Jahren zurück, sonst `False`.

---

## 🧪 Lösung überprüfen

Führe im Terminal den automatischen Unittest aus:
```bash
python3 test_aufgabe.py
```

Wenn alle 4 Tests mit `OK` durchlaufen, hast du die Grundlagen von Variablen und Datentypen gemeistert! 🎉
