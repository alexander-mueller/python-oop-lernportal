# SQL 07: Datenbank-Normalisierung (1NF bis 3NF) 📐

Willkommen zu **Modul 07** des SQL & Datenbanken Kurses!

Ein schlechtes Datenbank-Design führt unweigerlich zu massiver Datenredundanz und gefährlichen **Anomalien** (Einfüge-, Änderungs- und Löschanomalien). Die relationale Normalisierung nach Edgar F. Codd ist die bewährte Methode, um robuste Datenmodelle zu erstellen.

---

## 💡 1. Die drei Normalformen im Detail

```
Unnormalisiert (Excel-Chaos) 
       ⬇️  1. Regel: Jeder Wert atomar, keine Listen
1. Normalform (1NF)
       ⬇️  2. Regel: Keine Teilabhängigkeiten vom Primärschlüssel
2. Normalform (2NF)
       ⬇️  3. Regel: Keine transitiven Abhängigkeiten (A -> B -> C)
3. Normalform (3NF) ✅ "Clean Database Architecture"
```

### 1. Die 1. Normalform (1NF) – Atomare Werte
- **Regel:** Jedes Feld darf nur **einen einzigen atomaren Wert** enthalten (keine Kommalisten wie `'Maus, Tastatur, Kabel'`).
- Jede Zeile muss über einen eindeutigen Primärschlüssel identifizierbar sein.

### 2. Die 2. Normalform (2NF) – Volle funktionale Abhängigkeit
- **Regel:** 1NF ist erfüllt **UND** jedes Nicht-Schlüssel-Attribut muss voll vom gesamten Primärschlüssel abhängen (nicht nur von einem Teil bei zusammengesetzten Primärschlüsseln).
- Beispiel: In einer Bestelltabelle `(bestell_id, artikel_id, artikel_name)` hängt `artikel_name` nur von `artikel_id` ab, nicht von `bestell_id` -> `artikel` muss in eine eigene Tabelle!

### 3. Die 3. Normalform (3NF) – Keine transitiven Abhängigkeiten
- **Regel:** 2NF ist erfüllt **UND** kein Nicht-Schlüssel-Attribut hängt von einem anderen Nicht-Schlüssel-Attribut ab.
- **Berühmtes Beispiel:** `kunde_id -> plz -> stadt`. Die Stadt hängt von der PLZ ab, nicht direkt vom Kunden. Wird der Ort in eine eigene Tabelle `orte (plz, stadt)` ausgelagert, ist 3NF erreicht!

---

## 🏗️ Das Ziel-Schema in 3NF

1. **`orte`** (`plz TEXT PRIMARY KEY`, `stadt TEXT NOT NULL`)
2. **`kunden`** (`id INTEGER PRIMARY KEY`, `name TEXT NOT NULL`, `email TEXT NOT NULL UNIQUE`, `plz TEXT NOT NULL REFERENCES orte(plz)`)
3. **`artikel`** (`id INTEGER PRIMARY KEY`, `bezeichnung TEXT NOT NULL`, `einzelpreis REAL NOT NULL`)
4. **`auftraege`** (`id INTEGER PRIMARY KEY`, `kunde_id INTEGER NOT NULL REFERENCES kunden(id)`, `auftragsdatum TEXT NOT NULL`)
5. **`auftragspositionen`** (`auftrag_id INTEGER REFERENCES auftraege(id)`, `artikel_id INTEGER REFERENCES artikel(id)`, `menge INTEGER NOT NULL`, `PRIMARY KEY (auftrag_id, artikel_id)`)

---

## 🎯 Aufgaben in `aufgabe.sql`

1. **TODO 1**: Stammdatentabellen `orte` und `artikel` anlegen.
2. **TODO 2**: Tabelle `kunden` mit Fremdschlüssel auf `orte(plz)` erstellen.
3. **TODO 3**: Kopf- und Positionstabellen `auftraege` und `auftragspositionen` (mit zusammengesetztem Primärschlüssel) erstellen.
4. **TODO 4**: 3NF-konforme Testdaten einfügen.
5. **TODO 5**: Vollständige Reporting-Abfrage schreiben (Verbindung aller 5 Tabellen mit berechnetem Positions-Gesamtpreis `menge * einzelpreis`).

---

## 🚀 Ausführung
Klicke in der Web-IDE auf **Code ausführen** oder **Tests ausführen**, um das normalisierte Schema zu testen.
