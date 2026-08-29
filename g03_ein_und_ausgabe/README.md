# Kapitel G03: Interaktive Ein- & Ausgabe (Schulabgleich 07.0) 💬⌨️

Herzlich willkommen zum Kapitel **Interaktive Ein- und Ausgabe**!

Programme werden erst dann richtig spannend, wenn sie mit Menschen interagieren können: Sie stellen Fragen, nehmen Antworten über die Tastatur entgegen, verarbeiten diese und geben schön formatierte Ergebnisse auf dem Bildschirm aus.

---

## 🎯 Lernziele

1. **Benutzereingaben erfassen:** `input("Fragetext: ")` nutzen.
2. **Die goldene `input()`-Regel verstehen:** `input()` liefert **immer** einen `str` (Text), selbst wenn die Benutzerin `42` eingibt.
3. **Datentypen umwandeln (Typkonvertierung / Casting):** Mit `int()` und `float()` Texte in Zahlen umwandeln.
4. **Moderne f-Strings einsetzen:** Variablen und Ausdrücke sauber in Texte einbetten: `f"Hallo {name}!"`.
5. **Format-Spezifizierer beherrschen:** Zahlen präzise runden und formatieren (`{preis:.2f} €`, `{bmi:.1f}`, `{zahl:04d}`).
6. **`print()` Parameter steuern:** `sep="-"` (Trennzeichen) und `end=""` (Zeilenende) anwenden.

---

## 💡 Theorie & Wichtige Konzepte

### 1. Tastatureingabe mit `input()`

Die Funktion `input()` pausiert dein Programm und wartet darauf, dass die Benutzerin etwas im Terminal eintippt und mit <kbd>Enter</kbd> bestätigt.

```python
name = input("Wie heißt du? ")
print(f"Schön, dich kennenzulernen, {name}!")
```

> ⚠️ **Achtung, Falle!** `input()` liefert IMMER einen `str`:
> ```python
> alter_text = input("Dein Alter: ")  # Wenn du 15 eingibst, ist der Wert "15" (Text)!
> # alter_text + 1  💥 TypeError: can only concatenate str (not "int") to str
> ```

### 2. Typumwandlung (Type Casting)

Um mit Eingabezahlen rechnen zu können, musst du sie in `int` (Ganzzahl) oder `float` (Kommazahl) umwandeln:

```python
# Ganze Zahl einlesen:
alter = int(input("Dein Alter in Jahren: "))
tage = alter * 365

# Kommazahl einlesen:
preis = float(input("Preis in Euro (z.B. 4.99): "))
rabatt = preis * 0.9
```

---

### 3. Moderne f-Strings (Formatierte Strings)

Seit Python 3.6 nutzt man **f-Strings** (ein vorangestelltes `f` vor den Anführungszeichen). Alles innerhalb geschweifter Klammern `{...}` wird direkt als Python-Code ausgewertet:

```python
name = "Mia"
punkte = 42
print(f"Spielerin {name} hat {punkte} Punkte (doppelt so viel: {punkte * 2})!")
```

---

### 4. Formatierungs-Cheat-Sheet in f-Strings

Hinter einem Doppelpunkt `:` in den geschweiften Klammern kannst du das Format exakt bestimmen:

| Format-Code | Bedeutung | Beispiel | Ergebnis |
| :--- | :--- | :--- | :--- |
| `{x:.2f}` | Kommazahl mit genau 2 Dezimalstellen | `{12.5:.2f} €` | `"12.50 €"` |
| `{x:.1f}` | Kommazahl mit genau 1 Dezimalstelle | `{23.148:.1f}` | `"23.1"` |
| `{x:.1%}` | Prozentangabe (multipliziert mit 100) | `{0.19:.1%}` | `"19.0%"` |
| `{n:04d}` | Ganzzahl mit führenden Nullen (4 Stellen) | `{7:04d}` | `"0007"` |
| `{s:>10}` | Text rechtsbündig (Breite 10) | `{"Python":>10}` | `"    Python"` |

---

### 5. `print()` Parameter: `sep` und `end`

Die `print()`-Funktion hat zwei sehr praktische optionale Parameter:
- `sep`: Trennzeichen zwischen mehreren Werten (Standard: ein Leerzeichen `" "`).
- `end`: Zeichen am Ende der Ausgabe (Standard: Zeilenumbruch `"\n"`).

```python
# sep: Eigenes Trennzeichen
print("2026", "08", "29", sep="-")
# Ausgabe: 2026-08-29

# end: Kein Zeilenumbruch, nächste Ausgabe bleibt in derselben Zeile
print("Lade Fortschritt", end="... ")
print("100% Fertig!")
# Ausgabe: Lade Fortschritt... 100% Fertig!
```

---

## 🎯 Deine Aufgaben in `aufgabe.py`

Öffne `g03_ein_und_ausgabe/aufgabe.py` und implementiere die 4 Funktionen:

1. **TODO 1:** `begruessungs_text(name: str, stadt: str) -> str`
   - Rückgabe: `f"Hallo {name}, herzlich willkommen in {stadt}!"`
2. **TODO 2:** `berechne_alter_in_tagen(jahre: int) -> int`
   - Multipliziere `jahre * 365`.
3. **TODO 3:** `formatiere_rechnungsposten(artikel: str, anzahl: int, einzelpreis: float) -> str`
   - Berechne Gesamtpreis und formatiere: `f"{anzahl}x {artikel} à {einzelpreis:.2f} € = {gesamt:.2f} €"`
4. **TODO 4:** `steckbrief(name: str, groesse_m: float, gewicht_kg: float) -> str`
   - Berechne BMI: `gewicht_kg / (groesse_m ** 2)`
   - Formatiere: `f"Steckbrief: {name} | Größe: {groesse_m:.2f} m | Gewicht: {gewicht_kg:.1f} kg | BMI: {bmi:.1f}"`

---

## 🧪 Tests ausführen

Überprüfe deine Lösung im Terminal mit:

```bash
python3 test_aufgabe.py
```

Wenn alle 4 Tests mit **`OK`** durchlaufen, hast du das Kapitel gemeistert! 🎉
