# Kapitel G09: Dictionaries & Sets (Mengen) 📖🎯

Schulabgleich: **Thema 15.0 (Dictionaries und Mengen)**

Herzlich willkommen zu Kapitel G09! In diesem Kapitel lernst du zwei unverzichtbare Datenstrukturen kennen, die in modernen Python-Programmen tagtäglich eingesetzt werden: **Dictionaries** (Schlüssel-Wert-Zuordnungen) und **Sets** (Mengen ohne Duplikate).

---

## 🗃️ 1. Dictionaries: Die Karteikasten-Analogie

Ein **Dictionary** (abgekürzt `dict`) speichert Daten als **Schlüssel-Wert-Paare** (`key: value`).

Stell dir einen klassischen **Karteikasten** oder ein **Wörterbuch** vor:
- Wenn du nach dem Wort *"Schmetterling"* suchst (der **Key / Schlüssel**), findest du die englische Übersetzung *"Butterfly"* (der **Value / Wert**).
- Während eine Python-Liste Elemente über einen numerischen Index (`liste[0]`, `liste[1]`) abruft, greift ein Dictionary über beliebige eindeutige Schlüssel (meist Texte oder Zahlen) zu!

```
         [ DICTIONARY: telefonbuch ]
┌────────────────────────┬────────────────────────┐
│  SCHLÜSSEL (Key)       │  WERT (Value)          │
├────────────────────────┼────────────────────────┤
│  "Anna"                │  "0171-123456"         │
│  "Ben"                 │  "0160-987654"         │
│  "Clara"               │  "0151-555666"         │
└────────────────────────┴────────────────────────┘
```

### Grundlegende Syntax:
```python
# Dictionary erstellen:
kontakt = {
    "name": "Anna",
    "alter": 23,
    "ort": "Berlin"
}

# Zugriff über Schlüssel:
print(kontakt["name"])  # "Anna"

# Neuen Eintrag hinzufügen oder bestehenden ändern:
kontakt["email"] = "anna@example.com"
kontakt["alter"] = 24

# Eintrag entfernen:
del kontakt["ort"]
# oder mit Rückgabewert:
entfernter_wert = kontakt.pop("email")
```

---

## 🛡️ 2. Sicherer Datenzugriff: `dict[key]` vs. `dict.get(key, default)`

Ein häufiger Absturzgrund in Python ist der direkte Zugriff auf einen nicht existierenden Schlüssel:

```python
benutzer = {"name": "Max"}

# 💥 ABSTURZ:
print(benutzer["telefon"])  # KeyError: 'telefon'

# ✅ SICHER:
telefon = benutzer.get("telefon", "Keine Nummer hinterlegt")
print(telefon)  # Gibt "Keine Nummer hinterlegt" aus, OHNE Absturz!
```

> **Goldene Regel:** Wenn du nicht zu 100% sicher bist, ob ein Schlüssel im Dictionary vorkommt, nutze immer `.get()` mit einem sinnvollen Standardwert!

---

## 🔄 3. Über Dictionaries iterieren: `.keys()`, `.values()`, `.items()`

Python bietet drei praktische Methoden für Schleifen:

```python
preise = {"Apfel": 0.80, "Banane": 1.20, "Mango": 2.50}

# 1. Nur Schlüssel durchlaufen:
for frucht in preise.keys(): # oder einfach: for frucht in preise:
    print(frucht)

# 2. Nur Werte durchlaufen:
for preis in preise.values():
    print(f"{preis:.2f} €")

# 3. Schlüssel UND Werte gleichzeitig (sehr nützlich!):
for frucht, preis in preise.items():
    print(f"{frucht}: {preis:.2f} €")
```

---

## 🎟️ 4. Sets (Mengen): Die Club-Türsteher-Analogie

Ein **Set** (`set`) ist eine ungeordnete Sammlung von **eindeutigen Elementen**.

Stell dir einen strengen **Club-Türsteher** vor:
- Jeder Gast darf nur **ein einziges Mal** auf die Gästeliste.
- Wenn jemand versucht, sich ein zweites Mal anzustellen, winkt der Türsteher ab: *"Du bist schon drin!"*
- Im Club gibt es **keine feste Reihenfolge** (Sets haben keinen Index `set[0]`).

```python
# Set mit geschweiften Klammern erstellen:
farben = {"rot", "grün", "blau", "rot", "grün"}
print(farben)  # Ausgabe: {'rot', 'blau', 'grün'} (Duplikate automatisch entfernt!)

# Schnelle Zugehörigkeitsprüfung mit 'in' (extrem schnell in O(1)):
if "rot" in farben:
    print("Rot ist dabei!")
```

---

## 🧮 5. Mathematische Mengenoperationen mit Sets

Sets glänzen bei mathematischen Mengen-Vergleichen:

| Operation | Operator | Methode | Beschreibung |
| :--- | :--- | :--- | :--- |
| **Schnittmenge** | `A & B` | `A.intersection(B)` | Elemente, die in **beiden** Mengen vorkommen |
| **Vereinigung** | `A \| B` | `A.union(B)` | Alle Elemente aus **beiden** Mengen (ohne Duplikate) |
| **Differenz** | `A - B` | `A.difference(B)` | Elemente, die in A, aber **nicht** in B sind |
| **Symmetrische Differenz** | `A ^ B` | `A.symmetric_difference(B)` | Elemente in A oder B, aber **nicht in beiden** |

```python
schueler_kurs_a = {"Anna", "Ben", "Clara"}
schueler_kurs_b = {"Ben", "Daniel", "Clara", "Emma"}

# Wer ist in beiden Kursen? (Schnittmenge)
beide = schueler_kurs_a & schueler_kurs_b
print("In beiden Kursen:", beide)  # {'Ben', 'Clara'}

# Alle Schüler insgesamt? (Vereinigung)
alle = schueler_kurs_a | schueler_kurs_b
print("Alle Schüler:", alle)  # {'Anna', 'Ben', 'Clara', 'Daniel', 'Emma'}

# Wer ist nur in Kurs A? (Differenz)
nur_a = schueler_kurs_a - schueler_kurs_b
print("Nur in Kurs A:", nur_a)  # {'Anna'}
```

---

## ⚠️ Häufige Stolperfallen

1. **Leeres Set vs. Leeres Dictionary:**
   - `{}` erzeugt ein **leeres Dictionary**, KEIN Set!
   - Um ein leeres Set zu erstellen, schreibe immer: `mein_set = set()`.
2. **Keine veränderlichen Typen (Lists) als Keys oder Set-Elemente:**
   - Dictionaries-Schlüssel und Set-Elemente müssen **hashbar** (unveränderlich) sein (Strings, Zahlen, Tuples). Listen `[1, 2]` sind verboten (`TypeError: unhashable type: 'list'`).
3. **Reihenfolge bei Sets:**
   - Sets garantieren **keine** feste Reihenfolge. Wenn du Duplikate aus einer Liste entfernen und dabei die Reihenfolge beibehalten willst, musst du dir mit einer Hilfsmenge (`seen = set()`) und einer Ergebnisliste behelfen.

---

## 🎯 Deine Aufgaben in `aufgabe.py`

Öffne `g09_dictionaries_und_sets/aufgabe.py` und implementiere:

1. **TODO 1 (`woerter_haeufigkeit`):** Zähle die Häufigkeit jedes Wortes in einem Text (in Kleinbuchstaben, ohne Satzzeichen).
2. **TODO 2 (`telefonbuch_suche`):** Suche sicher mit `.get()` eine Nummer im Telefonbuch (Rückgabe: Nummer oder `"Nicht gefunden"`).
3. **TODO 3 (`gemeinsame_interessen`):** Finde die Hobbys, die zwei Personen gemeinsam haben (Schnittmenge `&`).
4. **TODO 4 (`entferne_duplikate_behalte_reihenfolge`):** Filtere Duplikate aus einer Liste, behalte die Reihenfolge des ersten Auftretens bei.

### Testen:
```bash
python3 test_aufgabe.py
```
Sobald alle 9 Tests mit `OK` durchlaufen, bist du bereit für Kapitel G10!
