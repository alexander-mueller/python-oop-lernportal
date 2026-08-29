# Kapitel 17: Reguläre Ausdrücke (re) – Text-Mining & Validierung 🔍🕵️

Willkommen zu **Kapitel 17** und dem Start von **Lehrpfad 4 (Professional Data Engineering)**!
In diesem Modul lernst du das Schweizer Taschenmesser der Textverarbeitung kennen: **Reguläre Ausdrücke (Regular Expressions / Regex)** mit Pythons eingebautem `re`-Modul.

---

## 🧭 Didaktischer Hintergrund & Die Detektiv-Analogie

In der Datenanalyse und beim Data Engineering sind 80% aller Rohdaten unstrukturiert: Logdateien, E-Mails, Rechnungs-PDFs, Social-Media-Feeds oder Kundeneingaben. Einfache String-Methoden (`.find()`, `.split()`) stoßen hier schnell an ihre Grenzen.

> 🕵️ **Die Detektiv-Analogie:**
> Ein regulärer Ausdruck ist wie ein **Phantombild für den Muster-Detektiv**.
> Anstatt nach einem festen Text zu suchen (*"Finde exakt 'Peter'"*), suchst du nach einer **Struktur**:
> *„Suche nach 2 Buchstaben, gefolgt von 2 Ziffern, gefolgt von vielen Zahlen – das ist eine IBAN!“*

---

## 🧰 1. Metazeichen: Die Bausteine von Regex

| Metazeichen | Bedeutung | Beispiel | Treffer |
| :--- | :--- | :--- | :--- |
| `\d` | **Digit**: Beliebige Ziffer (0-9) | `\d{3}` | `123`, `999` |
| `\D` | **Keine Ziffer**: Alles außer 0-9 | `\D+` | `abc`, `Hallo` |
| `\w` | **Word character**: Buchstabe, Ziffer, Unterstrich | `\w+` | `user_42`, `Python` |
| `\W` | **Kein Word character**: Leerzeichen, Satzzeichen | `\W` | `!`, `@`, ` ` |
| `\s` | **Whitespace**: Leerzeichen, Tab, Zeilenumbruch | `\s+` | ` `, `\t`, `\n` |
| `.` | **Beliebiges Zeichen** (außer Newline) | `a.c` | `abc`, `a-c`, `a9c` |
| `^` | **Zeilenanfang / Textanfang** | `^Start` | `Starten...` |
| `$` | **Zeilenende / Textende** | `Ende$` | `...am Ende` |
| `\b` | **Wortgrenze**: Übergang von `\w` zu `\W` | `\bTag\b` | `Tag` (nicht `Tagebuch`) |

> ⚠️ **Wichtig – Immer Raw-Strings `r"..."` nutzen:**
> Verwende für Regex-Muster in Python immer das Präfix `r"..."` (z.B. `r"\d+\s\w+"`), damit Python Backslashes nicht als Escape-Sequenzen wie `\n` oder `\t` interpretiert.

---

## 🔢 2. Quantifizierer: Wie oft kommt ein Zeichen vor?

| Quantifizierer | Häufigkeit | Bedeutung | Beispiel |
| :--- | :--- | :--- | :--- |
| `+` | $\ge 1$ | Mindestens einmal (1 bis unendlich) | `\d+` $\rightarrow$ `5`, `12345` |
| `*` | $\ge 0$ | Null oder mehrmals (optional beliebig oft) | `ab*c` $\rightarrow$ `ac`, `abc`, `abbc` |
| `?` | $0$ oder $1$ | Optional (höchstens einmal) | `https?` $\rightarrow$ `http`, `https` |
| `{n}` | Exakt $n$ | Genau $n$ Wiederholungen | `\d{4}` $\rightarrow$ `2026` |
| `{min,max}` | $min$ bis $max$ | Bereich von Wiederholungen | `\d{2,4}` $\rightarrow$ `12`, `123`, `1234` |

---

## 🎯 3. Zeichenklassen & Gruppen

### A) Benutzerdefinierte Zeichenklassen `[...]`
- `[aeiou]` $\rightarrow$ Findet einen Vokal
- `[a-zA-Z0-9]` $\rightarrow$ Alphanumerische Zeichen
- `[^0-9]` $\rightarrow$ Negation: Alles **außer** Ziffern

### B) Gruppen `(...)` & Benannte Gruppen `(?P<name>...)`
Mit runden Klammern schneidest du Teiltreffer gezielt heraus:
```python
import re

muster = r"^(?P<jahr>\d{4})-(?P<monat>\d{2})-(?P<tag>\d{2})$"
match = re.match(muster, "2026-08-29")

if match:
    print(match.group("jahr"))   # -> '2026'
    print(match.groupdict())     # -> {'jahr': '2026', 'monat': '08', 'tag': '29'}
```

---

## ⚙️ 4. Die wichtigsten Methoden des `re`-Moduls

| Methode | Wann verwenden? | Rückgabetyp |
| :--- | :--- | :--- |
| `re.search(pattern, text)` | Erstes Vorkommen irgendwo im Text suchen | `re.Match` oder `None` |
| `re.fullmatch(pattern, text)` | Ganzen String von Anfang bis Ende prüfen (Validierung) | `re.Match` oder `None` |
| `re.findall(pattern, text)` | Alle Treffer im Text als Liste sammeln | `list[str]` oder `list[tuple]` |
| `re.finditer(pattern, text)` | Alle Treffer als Iterator mit Positionen durchlaufen | `Iterator[re.Match]` |
| `re.sub(pattern, repl, text)` | Suchen & Ersetzen (z.B. Maskierung vertraulicher Daten) | `str` |

### Praxisbeispiel: Datenbereinigung mit `re.sub`
```python
# IBANs maskieren
text = "Konto: DE89370400440532013000"
maskiert = re.sub(
    r"\b([A-Z]{2}\d{2})([A-Z0-9]{8,30})\b",
    lambda m: m.group(1) + ("*" * len(m.group(2))),
    text
)
print(maskiert) # -> Konto: DE89******************
```

---

## 📁 Die Dateien in diesem Modul

- **`index.html`**: Interaktive Lernseite mit Cheat-Sheet, Live-Beispielen, Checkliste und Lösungstipps.
- **`aufgabe.py`**: Dein Arbeitsblatt mit Type Hints und TODOs für E-Mail-Check, Telefon-Finder, Hashtags, IBAN-Maskierung und ISO-Datum-Parsing.
- **`test_aufgabe.py`**: Automatische Unittest-Suite mit Grenzfall-Tests.
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
