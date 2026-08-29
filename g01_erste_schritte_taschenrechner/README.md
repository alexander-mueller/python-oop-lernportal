# Grundlagen 01: Python als Taschenrechner 🧮 (Schulabgleich 02.1)

Willkommen zum ersten Kapitel des Python-Grundlagen-Lehrpfads!

In diesem Kapitel lernst du, wie Python als extrem präziser und vielseitiger Taschenrechner verwendet wird, welche Zahlenarten es gibt und wie die mathematischen Operatoren funktionieren.

---

## 💡 Das Wichtigste in Kürze

### 1. Zahlenarten in Python
Python unterscheidet grundlegend zwischen zwei Zahlenarten:
- **`int` (Integer):** Ganze Zahlen ohne Nachkommastellen (z.B. `42`, `-5`, `0`, `1000000`). Python kann mit beliebig großen ganzen Zahlen rechnen!
- **`float` (Floating Point Number):** Kommazahlen mit Nachkommastellen (z.B. `3.14`, `-0.5`, `2.0`). Beachte: In Python wird als Dezimaltrennzeichen immer ein **Punkt `.`** verwendet, kein Komma!

---

## 🧮 Die 7 Rechenoperatoren in Python

| Operator | Name | Beispiel | Ergebnis | Besonderheit / Erklärung |
| :---: | :--- | :--- | :---: | :--- |
| `+` | Addition | `12 + 8` | `20` | Addiert zwei Zahlen |
| `-` | Subtraktion | `20 - 7` | `13` | Subtrahiert den zweiten Wert vom ersten |
| `*` | Multiplikation | `6 * 7` | `42` | Multipliziert zwei Zahlen |
| `/` | Echte Division | `7 / 2` | `3.5` | **Wichtig:** Liefert in Python 3 *immer* ein `float` (Kommazahl)! `4 / 2` ergibt `2.0`. |
| `//` | Ganzzahldivision | `17 // 5` | `3` | Teilt und rundet immer zur nächsten ganzen Zahl nach unten ab (Floor Division). |
| `%` | Modulo | `17 % 5` | `2` | Berechnet den verbleibenden **Rest** einer Ganzzahldivision. |
| `**` | Potenz | `2 ** 3` | `8` | Berechnet $2^3 = 2 \times 2 \times 2 = 8$. |

---

## 🍕 Pizza-Analogie für `//` und `%`

Stell dir vor, du bestellst eine Pizza mit **17 Stücken** für **5 Personen**:
- Wie viele ganze Stücke bekommt jede Person fair aufgeteilt?  
  $$\text{Stücke pro Person} = 17 // 5 = 3$$
- Wie viele Stücke bleiben in der Schachtel übrig?  
  $$\text{Rest} = 17 \% 5 = 2$$
- Probe: $3 \times 5 + 2 = 17$!

---

## 📐 Vorrangregeln (Punkt vor Strich & Klammern)

Genau wie in der Schulmathematik beachtet Python feste Vorrangregeln:
1. **Klammern `(...)`** haben immer die höchste Priorität.
2. **Potenzen `**`** werden vor Multiplikation/Division berechnet.
3. **Punktrechnung `*`, `/`, `//`, `%`** kommt vor **Strichrechnung `+`, `-`**.

```python
# Ohne Klammer: 3 * 4 = 12, dann 2 + 12 = 14
ergebnis = 2 + 3 * 4      # 14

# Mit Klammer: (2 + 3) = 5, dann 5 * 4 = 20
ergebnis = (2 + 3) * 4    # 20
```

---

## 📢 Textausgabe mit `print()`

Mit der eingebauten Funktion `print()` gibst du Texte und Rechenergebnisse im Terminal aus:

```python
print("Hallo Welt!")
print("Ergebnis:", 40 + 2)
print(f"Die Kreisfläche beträgt: {3.14159 * 5**2}")
```

---

## 🎯 Deine Aufgaben in `aufgabe.py`

Öffne die Datei `aufgabe.py` und bearbeite die folgenden 7 TODOs:
1. **TODO 1:** `addieren(a, b)` $\rightarrow$ Summe $a + b$
2. **TODO 2:** `subtrahieren(a, b)` $\rightarrow$ Differenz $a - b$
3. **TODO 3:** `multiplizieren(a, b)` $\rightarrow$ Produkt $a \times b$
4. **TODO 4:** `dividieren(a, b)` $\rightarrow$ Quotient $a / b$ (als float)
5. **TODO 5:** `ganzzahl_rest(a, b)` $\rightarrow$ Tupel `(a // b, a % b)`
6. **TODO 6:** `potenz(basis, exponent)` $\rightarrow$ $basis^{exponent}$ (`basis ** exponent`)
7. **TODO 7:** `kreis_flaeche(radius)` $\rightarrow$ $3.14159 \times radius^2$

---

## 🧪 Lösung überprüfen

Führe im Terminal den automatischen Unittest aus:
```bash
python3 test_aufgabe.py
```

Wenn alle 7 Tests mit `OK` durchlaufen, bist du bereit für das nächste Kapitel: **G02: Variablen & Datentypen**!
