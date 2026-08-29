# Vorkapitel 00: Python Fehlersuche & Grundlagen 🔍🕵️‍♀️

Herzlich willkommen zum Warm-up!

Bevor wir mit Klassen und objektorientierter Programmierung starten, lernen wir das wichtigste Handwerkszeug jeder guten Entwicklerin: **Wie man Fehler im Code schnell findet und behebt.**

---

## 💡 Fehlermeldungen richtig lesen: Die Unten-nach-Oben-Regel

Wenn Python stoppt und einen roten Text anzeigt, nennt man das einen **Traceback**.
Lies immer ganz unten:

```text
Traceback (most recent call last):
  File "aufgabe.py", line 15, in <module>
    summe = punkte + bonus
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```
1. **Ganz unten:** Was ist das Problem? (`TypeError: ... 'int' and 'str'`)
2. **Zeile darüber:** Wo ist es passiert? (`line 15`)

---

## 🚫 Die 4 häufigsten Python-Fehler

1. **`IndentationError`:**
   In Python müssen Codeblöcke in Funktionen, Bedingungen und Schleifen **genau 4 Leerzeichen** eingerückt sein.
2. **`SyntaxError`:**
   Doppelpunkte am Ende von `def`, `if`, `else`, `for` vergessen oder ungeschlossene Klammern `)`.
3. **`NameError`:**
   Tippfehler beim Namen einer Variable oder Funktion (z.B. `spielr_name` statt `spieler_name`).
4. **`TypeError`:**
   Falsche Datentypen gemischt (z.B. `"Ergebnis: " + 10` statt `f"Ergebnis: {10}"`).

---

## 🎯 Deine Detektiv-Aufgabe in `aufgabe.py`

In `aufgabe.py` hat sich ein fehlerhaftes Quiz-Programm eingeschlichen. Deine Aufgabe ist es, die 5 versteckten Fehler zu finden und zu reparieren.

### Vorgehen:
1. Führe die Datei im Terminal aus:
   ```bash
   python3 aufgabe.py
   ```
2. Lies die Fehlermeldung von unten nach oben.
3. Behebe den ersten angezeigten Fehler.
4. Wiederhole die Schritte, bis das Skript ohne Fehler durchläuft!
5. Führe den Test zur Bestätigung aus:
   ```bash
   python3 test_aufgabe.py
   ```
