# Kapitel G08: Textverarbeitung & Strings in Python 🔤✨

Willkommen im Kapitel **Textverarbeitung und Strings**! Strings (Zeichenketten) gehören zu den vielseitigsten Datentypen in Python. In diesem Kapitel lernst du alle wichtigen String-Methoden zur Bereinigung, Suche, Zerlegung und Formatierung kennen.

---

## 🏛️ 1. Die Stempel-Analogie: Strings sind unveränderlich (immutable)!

Ein grundlegendes Konzept in Python: **Strings können nach ihrer Erstellung nicht mehr verändert werden!**

```python
name = "python"
# ❌ Das funktioniert NICHT und wirft einen TypeError:
# name[0] = "P"

# ✅ Stattdessen erzeugt jede String-Methode einen NEUEN String:
name = name.capitalize()  # Erzeugt "Python" und weist es neu zu
```

> 🖨️ **Die Stempel-Analogie:** Stell dir einen String wie gedruckten Text auf Papier vor. Du kannst die Buchstaben auf dem Papier nicht wegradieren. Jede String-Methode druckt stattdessen ein **frisches neues Blatt Papier** mit dem geänderten Text aus!

---

## 🧰 2. Das große String-Methoden Cheat-Sheet

Python stellt eine Fülle praktischer Methoden für Strings bereit:

### A. Groß- & Kleinschreibung
```python
text = "hallo welt"
print(text.upper())       # -> "HALLO WELT" (alles GROSS)
print(text.lower())       # -> "hallo welt" (alles klein)
print(text.capitalize())  # -> "Hallo welt" (nur erstes Zeichen groß)
print(text.title())       # -> "Hallo Welt" (jedes Wort groß)
```

### B. Leerzeichen & Whitespace entfernen
```python
eingabe = "   max_mustermann   \n"
print(eingabe.strip())    # -> "max_mustermann" (vorne & hinten bereinigt)
print(eingabe.lstrip())   # -> "max_mustermann   \n" (nur links)
print(eingabe.rstrip())   # -> "   max_mustermann" (nur rechts)
```

### C. Suchen, Zählen & Ersetzen
```python
satz = "Python ist super und Python macht Spaß"

# Ersetzen:
print(satz.replace("Python", "Coding"))
# -> "Coding ist super und Coding macht Spaß"

# Vorkommen zählen:
print(satz.count("Python"))  # -> 2

# Position finden (-1 wenn nicht gefunden):
print(satz.find("super"))    # -> 11

# Anfang & Ende prüfen (liefert True / False):
print(satz.startswith("Python"))  # -> True
print(satz.endswith("Spaß"))      # -> True
```

### D. Zerlegen (`.split`) & Zusammenfügen (`.join`)
```python
# 1. An Trennzeichen in eine Liste zerlegen:
daten = "Max;Mustermann;18;Informatik"
teile = daten.split(";")
print(teile)  # -> ["Max", "Mustermann", "18", "Informatik"]

# 2. Ohne Parameter zerlegt .split() an beliebigen Leerzeichen:
woerter = "   Python   macht   Spaß!   ".split()
print(woerter)  # -> ["Python", "macht", "Spaß!"]

# 3. Eine Liste mit einem Trennzeichen zu einem String zusammenfügen:
zutaten = ["Mehl", "Zucker", "Eier", "Milch"]
kuchen = ", ".join(zutaten)
print(kuchen)  # -> "Mehl, Zucker, Eier, Milch"
```

---

## ✂️ 3. Strings sind Sequenzen (Index & Slicing)

Genau wie Listen kannst du auch auf einzelne Zeichen in Strings über deren Index und Slicing zugreifen:

```python
wort = "Lagerregal"

print(wort[0])     # -> "L" (Erster Buchstabe)
print(wort[-1])    # -> "l" (Letzter Buchstabe)
print(wort[-4:])   # -> "egal" (Die letzten 4 Buchstaben)
print(wort[::-1])  # -> "lagerregaL" (String umkehren!)
```

---

## 🧪 4. Praxisbeispiel: CSV-Daten bereinigen & parsen

```python
csv_zeile = "  anna.meier@schule.at ; 1050 ; Wien ; 4A  "

# 1. Zeile säubern und in Spalten zerlegen:
spalten = [feld.strip() for feld in csv_zeile.split(";")]
email, plz, stadt, klasse = spalten

print(f"E-Mail: {email.lower()}")
print(f"Standort: {plz} {stadt.title()}")
print(f"Klasse: {klasse}")
```

---

## 🎯 Deine Aufgaben in `aufgabe.py`

Öffne `aufgabe.py` und implementiere die 5 Funktionen:

1. **`ist_palindrom(text)`**: Prüft, ob ein Text vorwärts wie rückwärts gleich ist (ignoriert Groß/Klein und Leerzeichen).
2. **`zaehle_vokale(text)`**: Zählt alle Vokale (a, e, i, o, u, ä, ö, ü) im Text.
3. **`bereinige_benutzernamen(name)`**: Entfernt Rand-Leerzeichen, konvertiert zu Kleinbuchstaben und ersetzt innere Leerzeichen durch `_`.
4. **`woerter_zaehlen(text)`**: Nutzt `.split()`, um die Anzahl der Wörter zu ermitteln.
5. **`maskiere_kreditkarte(nummer)`**: Ersetzt alle Zeichen außer den letzten 4 durch `*`.

### Testen deiner Lösung:
```bash
python3 test_aufgabe.py
```
