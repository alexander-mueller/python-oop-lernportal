# Kapitel G05: Schleifen & Wiederholungen 🎡🔄

Willkommen zu **Kapitel G05** unseres Python-Grundlagen-Lehrpfads!
Dieses Kapitel entspricht den Modulen **09.1 & 09.2** deines Informatik-Skriptums.

Computer sind genial darin, dieselbe Aufgabe tausende oder millionen Male in Millisekunden auszuführen – ohne müde zu werden oder Fehler zu machen. Das Werkzeug dafür sind **Schleifen (Loops)**!

---

## 🎡 Die Karussell- & Riesenrad-Analogie

Stell dir einen Jahrmarkt vor:
- **`for`-Schleife (Zählschleife):** Wie ein Karussell mit Wertmarken. Du kaufst dir 5 Runden. Der Automat zählt mit: Runde 1, 2, 3, 4, 5. Nach 5 Runden stoppt das Karussell automatisch.
- **`while`-Schleife (Bedingungsschleife):** Wie ein Riesenrad, das sich dreht, **solange** die Musik spielt. Sobald die Musik stoppt (Bedingung wird `False`), hält das Rad an.

```
[ FOR-SCHLEIFE ]                 [ WHILE-SCHLEIFE ]
"Fahre genau 5 Runden!"           "Fahre, SOLANGE Musik läuft!"
  ┌───────────┐                    ┌───────────┐
  │ Runde 1/5 │                    │ Musik da? │ ── Nein ──> Stopp
  │ Runde 2/5 │                    └─────┬─────┘
  │ Runde 3/5 │                          │ Ja
  │ Runde 4/5 │                    ┌─────▼─────┐
  │ Runde 5/5 │                    │ 1 Runde   │
  └─────┬─────┘                    └─────┬─────┘
        ▼                                │
      FERTIG                             └───────── Wiederholen!
```

---

## 1. Die Zählschleife: `for` und die `range()`-Funktion

Wenn du im Voraus weißt, **wie oft** etwas wiederholt werden soll, ist die `for`-Schleife die perfekte Wahl.

### Wie funktioniert `range()`?

Die `range()`-Funktion erzeugt eine Zahlenfolge. **Wichtigste Regel:** Das `stop`-Element ist **immer exklusiv** (wird nicht mehr erreicht)!

```
range(stop)               -> 0 bis stop - 1
range(start, stop)        -> start bis stop - 1
range(start, stop, step)  -> start bis stop - 1 mit Schrittweite step
```

#### Visualisierung:
```
range(1, 6)   ──> [ 1,  2,  3,  4,  5 ]        (6 ist NICHT dabei!)
range(0, 10, 2) ─> [ 0,  2,  4,  6,  8 ]        (nur gerade Zahlen!)
range(5, 0, -1) ─> [ 5,  4,  3,  2,  1 ]        (rückwärts zählen!)
```

```python
# Einfaches Beispiel:
for i in range(1, 6):
    print(f"Runde {i}")
```

---

## 2. Die Bedingungsschleife: `while`

Wenn du vorher **nicht genau weißt**, wie viele Durchläufe nötig sind, sondern die Wiederholung an eine **Bedingung** geknüpft ist:

```python
energie = 3
while energie > 0:
    print(f"Roboter läuft... Energie: {energie}")
    energie -= 1  # ⚠️ WICHTIG: Schleifenzähler verändern!

print("Roboter hat keine Energie mehr.")
```

### 🛑 Die Gefahr der Endlosschleife (Infinite Loop)

Wenn die Bedingung einer `while`-Schleife niemals `False` wird, läuft das Programm für immer und friert ein:

```python
# 💥 GEFÄHRLICH: Endlosschleife!
x = 1
while x > 0:
    print(x)
    # Vergessen, x zu verändern -> x bleibt immer 1 -> Bedingung immer True!
```

> **Tipp zum Abbrechen:** Falls dein Programm in einer Endlosschleife festhängt, drücke im Terminal <kbd>Strg</kbd> + <kbd>C</kbd> (Ctrl+C).

---

## 3. Schleifen steuern: `break` & `continue`

Manchmal möchtest du eine Schleife vorzeitig beenden oder eine Runde überspringen:

- **`break` (Die Notbremse):** Verlässt die Schleife **sofort**, egal wie viele Runden noch übrig wären.
- **`continue` (Nächste Runde):** Bricht nur den **aktuellen Durchlauf** ab und springt direkt zur nächsten Runde.

```python
# Beispiel break:
for zahl in range(1, 10):
    if zahl == 5:
        print("Treffer! Schleife wird abgebrochen.")
        break
    print(zahl)  # Gibt 1, 2, 3, 4 aus

# Beispiel continue:
for zahl in range(1, 6):
    if zahl == 3:
        print("Zahl 3 wird übersprungen!")
        continue
    print(zahl)  # Gibt 1, 2, 4, 5 aus
```

---

## 4. Das Schleifen-Akkumulator-Muster 🧺

Ein **Akkumulator** ist eine Hilfsvariable, die **vor** der Schleife erstellt wird und in jedem Schleifendurchlauf einen neuen Wert aufsammelt.

```python
# 1. Summen-Akkumulator (Startwert: 0)
summe = 0
for x in [10, 20, 30]:
    summe += x  # summe = summe + x
print("Summe:", summe)  # 60

# 2. Zähler-Akkumulator (Startwert: 0)
anzahl_gerade = 0
for x in range(1, 11):
    if x % 2 == 0:
        anzahl_gerade += 1
print("Gerade Zahlen:", anzahl_gerade)  # 5

# 3. Produkt-Akkumulator (Startwert: 1, NIEMALS 0!)
produkt = 1
for x in range(1, 5):
    produkt *= x  # 1 * 2 * 3 * 4
print("Produkt:", produkt)  # 24
```

---

## 5. 🌟 Praxisbeispiele

### Beispiel A: Kleines Einmaleins (Verschachtelte Schleifen)
```python
for zeile in range(1, 4):
    for spalte in range(1, 4):
        ergebnis = zeile * spalte
        print(f"{zeile}x{spalte}={ergebnis:2d}", end="  ")
    print()  # Zeilenumbruch
```

### Beispiel B: Zahlen-Ratespiel mit `while` und `break`
```python
geheime_zahl = 7
versuche = 0

while True:
    versuche += 1
    tipp = int(input("Rate eine Zahl zwischen 1 und 10: "))
    if tipp == geheime_zahl:
        print(f"🎉 Richtig erraten nach {versuche} Versuchen!")
        break
    elif tipp < geheime_zahl:
        print("Zu klein!")
    else:
        print("Zu groß!")
```

---

## ⚠️ Die 3 häufigsten Anfängerfehler

1. **Off-by-One Fehler bei `range()`:**
   - `range(1, 5)` läuft nur bis 4! Wenn du die 5 inklusive haben willst, schreibe `range(1, 6)`.
2. **Akkumulator in der Schleife zurücksetzen:**
   - Wenn du `summe = 0` **in** der Schleife schreibst, wird die Summe in jeder Runde gelöscht! Der Startwert muss **vor** der Schleife stehen.
3. **Endlosschleife bei `while`:**
   - Vergiss nicht, die Variable in der `while`-Bedingung innerhalb der Schleife anzupassen (`i += 1` oder `n //= 10`).

---

## 🎯 Deine Aufgaben in `aufgabe.py`

Öffne `aufgabe.py` und bearbeite die Aufgaben:
1. **TODO 1:** `summe_bis(n: int) -> int` – Berechnet $1 + 2 + \dots + n$.
2. **TODO 2:** `fakultaet(n: int) -> int` – Berechnet $n! = 1 \cdot 2 \cdots n$.
3. **TODO 3:** `zaehle_gerade_zahlen(start: int, ende: int) -> int` – Zählt gerade Zahlen.
4. **TODO 4:** `ist_primzahl(n: int) -> bool` – Prüft Primzahlen.
5. **TODO 5:** `quorsumme(n: int) -> int` – Berechnet die Quersumme mit einer `while`-Schleife.

### Testen:
```bash
python3 test_aufgabe.py
```
Sobald alle 5 Tests grün sind (`OK`), kannst du zu Kapitel G06 weitergehen!
