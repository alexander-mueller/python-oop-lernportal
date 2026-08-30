# SQL 13: B-Tree Indizes & Query-Optimierung ⚡🔍

Willkommen zu **Modul 13 (Lehrpfad 4: Performance, Transaktionen & Analytics Master)**!
Als Data Engineer und SQL-Architekt ist Performance deine wichtigste Währung. In diesem Modul lernst du, wie der Query Optimizer von relationalen Datenbanken arbeitet und wie du mit gezielten B-Tree Indizes Abfragezeiten von Sekunden auf Millisekunden senkst.

---

## 🎯 Lernziele

1. **B-Tree Indizes**: Erstellen von Single-, Multi-Column- und Unique-Indizes.
2. **Leftmost-Prefix Regel**: Verstehen, wie Composite Indizes (`col_a, col_b`) funktionieren und wann sie greifen.
3. **Partial Indizes**: Ressourcenschonende Indizes mit `WHERE`-Bedingung für Hot-Data.
4. **`EXPLAIN QUERY PLAN`**: Analysieren und Interpretieren von Ausführungsplänen (`SCAN TABLE` vs. `SEARCH TABLE USING INDEX`).
5. **SARGability**: Schreiben indexfreundlicher Filterbedingungen ohne Funktionsaufrufe auf indexierten Spalten.

---

## 💡 Was bedeutet SARGable?

**SARGable** steht für *Search Argument Able*.
Wenn du in der `WHERE`-Bedingung eine Funktion auf die indexierte Spalte anwendest, kann die Datenbank den B-Tree Index nicht nutzen und muss einen langsamen Table Scan durchführen:

```sql
-- ❌ NON-SARGABLE (Index auf 'bestell_datum' wird ignoriert -> SCAN TABLE):
SELECT * FROM bestellungen WHERE strftime('%Y', bestell_datum) = '2024';

-- ✅ SARGABLE (Index wird direkt genutzt -> SEARCH TABLE USING INDEX):
SELECT * FROM bestellungen WHERE bestell_datum >= '2024-01-01' AND bestell_datum < '2025-01-01';
```

---

## 🚀 Aufgabenstellung (`aufgabe.sql`)

1. **TODO 1: Unique & Composite Indizes** – Erstelle Indizes auf `kunden(email)` und `artikel(kategorie_id, preis DESC)`.
2. **TODO 2: Partieller Index** – Erstelle einen Index für aktive Kunden (`WHERE status = 'aktiv'`).
3. **TODO 3: Abfrageplan-Analyse** – Führe `EXPLAIN QUERY PLAN` für Schlüsselabfragen aus.
4. **TODO 4: SARGable Refactoring** – Optimiere eine Zeitbereichs-Abfrage zur vollen Ausnutzung des Datums-Index.

---

## 🧪 Tests ausführen

Validierung erfolgt über `test_aufgabe.sql`.
