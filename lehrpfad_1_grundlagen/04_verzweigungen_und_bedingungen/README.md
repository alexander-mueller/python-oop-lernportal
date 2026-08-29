# Kapitel G04: Verzweigungen & Bedingungen (Schulabgleich 08.0) 🛤️🔀

Herzlich willkommen zum Kapitel **Bedingungen und Verzweigungen**!

Programme müssen oft Entscheidungen treffen: *Darf die Person schon Auto fahren?*, *Bekommt sie einen Rabatt?*, *Ist heute ein Schaltjahr?*. In Python steuern wir solche Entscheidungen mit `if`, `elif` und `else`.

---

## 🎯 Lernziele

1. **Entscheidungsstrukturen verstehen:** `if`, `elif` und `else` für logische Programmabläufe einsetzen.
2. **Die Eisenbahn-Weichen-Analogie begreifen:** Sobald die erste Bedingung zutrifft, werden alle nachfolgenden `elif`/`else`-Zweige übersprungen.
3. **Vergleichsoperatoren beherrschen:** `==`, `!=`, `<`, `>`, `<=`, `>=`.
4. **Logische Operatoren kombinieren:** `and` (und), `or` (oder), `not` (nicht / Verneinung).
5. **Klammern & Rangfolge anwenden:** Komplexe Bedingungen mit `()` sicher strukturieren.
6. **Flache vs. tief verschachtelte Bedingungen:** Sauberen, lesbaren Code nach dem KISS-Prinzip schreiben.

---

## 💡 Theorie & Wichtige Konzepte

### 1. Die Weichen-Analogie (Eisenbahn-Gleis) 🛤️

Stell dir dein Programm wie einen Zug auf den Schienen vor. An einer Weiche entscheidet das Signal (`Bedingung`), auf welches Gleis der Zug abbiegt:

```python
if alter < 12:
    preis = 6.0    # Gleis 1 (Kind)
elif alter >= 65:
    preis = 8.5    # Gleis 2 (Senior)
elif ist_student:
    preis = 9.5    # Gleis 3 (Student)
else:
    preis = 12.0   # Ausweichgleis (Standard-Erwachsener)
```

> 🔑 **Wichtig:** Python prüft die Bedingungen von oben nach unten. Der **erste** Block, dessen Bedingung `True` ergibt, wird ausgeführt. Danach verlässt Python die gesamte Weiche!

---

### 2. Die Vergleichsoperatoren

| Operator | Bedeutung | Beispiel | Ergebnis |
| :---: | :--- | :--- | :--- |
| `==` | Ist gleich? *(Vorsicht: Nicht mit Zuweisung `=` verwechseln!)* | `5 == 5` | `True` |
| `!=` | Ist ungleich? | `5 != 3` | `True` |
| `<` | Kleiner als | `10 < 20` | `True` |
| `>` | Größer als | `10 > 20` | `False` |
| `<=` | Kleiner oder gleich (Grenzwert inkludiert) | `10 <= 10` | `True` |
| `>=` | Größer oder gleich (Grenzwert inkludiert) | `18 >= 18` | `True` |

---

### 3. Logische Operatoren & Wahrheitstabellen

Oft reicht eine einzelne Bedingung nicht aus. Mit logischen Operatoren verknüpfst du mehrere Bedingungen:

#### `and` (Logisches UND – Beide müssen wahr sein):
| Bedingung A | Bedingung B | `A and B` |
| :---: | :---: | :---: |
| `True` | `True` | **`True`** |
| `True` | `False` | `False` |
| `False` | `True` | `False` |
| `False` | `False` | `False` |

#### `or` (Logisches ODER – Mindestens eins muss wahr sein):
| Bedingung A | Bedingung B | `A or B` |
| :---: | :---: | :---: |
| `True` | `True` | **`True`** |
| `True` | `False` | **`True`** |
| `False` | `True` | **`True`** |
| `False` | `False` | `False` |

#### `not` (Logisches NICHT – Dreht den Wahrheitswert um):
- `not True` ergibt `False`
- `not False` ergibt `True`

---

### 4. Das Schaltjahr-Rätsel 📅

Ein schönes Praxisbeispiel für logische Verknüpfungen ist die gregorianische Schaltjahr-Regel:
1. Ein Jahr ist ein Schaltjahr, wenn es durch 4 teilbar ist (`jahr % 4 == 0`).
2. Säkularjahre (Jahrhunderte wie 1900, 2100) sind **keine** Schaltjahre (`jahr % 100 != 0`),
3. **außer** sie sind durch 400 teilbar (wie 2000, 2400: `jahr % 400 == 0`).

In Python formuliert:
```python
ist_schalt = (jahr % 4 == 0 and jahr % 100 != 0) or (jahr % 400 == 0)
```

---

## 🎯 Deine Aufgaben in `aufgabe.py`

Öffne `g04_verzweigungen_und_bedingungen/aufgabe.py` und implementiere die 4 Funktionen:

1. **TODO 1: Kinokarten-Preisrechner**
   - `ticket_preis(alter: int, ist_student: bool) -> float`
   - Alter < 12: `6.0` €
   - Alter >= 65: `8.5` €
   - 12 bis 64 Jahre: Wenn `ist_student` -> `9.5` €, sonst -> `12.0` €

2. **TODO 2: Schulnoten-Ermittlung**
   - `schulnote_text(punkte: int) -> str`
   - `< 0` oder `> 100`: `"Ungültige Punktezahl"`
   - `>= 90`: `"Sehr gut"`, `>= 75`: `"Gut"`, `>= 60`: `"Befriedigend"`, `>= 50`: `"Genügend"`, `< 50`: `"Nicht genügend"`

3. **TODO 3: Schaltjahr-Erkennung**
   - `ist_schaltjahr(jahr: int) -> bool`
   - `(jahr % 4 == 0 and jahr % 100 != 0) or (jahr % 400 == 0)`

4. **TODO 4: Achterbahn-Zulassung**
   - `kann_achterbahn_fahren(groesse_cm: int, begleitung_erwachsen: bool) -> bool`
   - Ab 140 cm: immer `True`
   - Ab 120 cm bis 139 cm: `True`, wenn `begleitung_erwachsen == True`, sonst `False`
   - Unter 120 cm: immer `False`

---

## 🧪 Tests ausführen

Überprüfe deine Lösung im Terminal mit:

```bash
python3 test_aufgabe.py
```

Wenn alle 4 Tests mit **`OK`** durchlaufen, hast du das Kapitel gemeistert! 🎉
