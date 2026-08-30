# SQL 11: Common Table Expressions (WITH CTE) 🧱⛓️

Willkommen zu **Modul 11 (Lehrpfad 3: Aggregationen, CTEs & Window Functions)**!
Common Table Expressions (CTEs) sind das Schweizer Taschenmesser für professionelle Data Engineers. Sie transformieren kryptische, tief verschachtelte SQL-Abfragen in saubere, lesbare und wartbare Datenpipelines.

---

## 🎯 Lernziele

1. **`WITH`-Klausel**: Strukturierung von Abfragen in logische Teilabfragen.
2. **Gekettete (Chained) CTEs**: Schrittweise Verarbeitung von Rohdaten über mehrere Zwischenstationen.
3. **Rekursive CTEs (`WITH RECURSIVE`)**: Iterative Traversierung hierarchischer Daten (Bäume, Organigramme, Stücklisten).
4. **Kalender-Generierung**: Erzeugung lückenloser Datumsreihen ohne Hilfstabellen zur Vermeidung von Lücken im Reporting.

---

## 💡 Syntax & Struktur rekursiver CTEs

Eine rekursive CTE besteht immer aus drei Komponenten:
1. **Anker-Abfrage**: Basisdatensatz (z.B. Wurzelknoten oder Startdatum).
2. **`UNION ALL`**: Verbindet die Rekursionsrunden.
3. **Rekursive Abfrage**: Verweist auf den Namen der CTE selbst und definiert die Abbruchbedingung (`WHERE`).

```sql
WITH RECURSIVE kalender(tag) AS (
    -- 1. Anker: Startdatum
    SELECT '2024-01-01'
    UNION ALL
    -- 2. Rekursion: +1 Tag bis zum Enddatum
    SELECT DATE(tag, '+1 day')
    FROM kalender
    WHERE tag < '2024-01-10'
)
SELECT tag FROM kalender;
```

---

## 🚀 Aufgabenstellung (`aufgabe.sql`)

1. **TODO 1: Einfache CTE & Kunden-Segmentierung** – Berechne Vor-Aggregate in `kunden_stats` und klassifiziere Kunden via `CASE WHEN` im Haupt-SELECT.
2. **TODO 2: Multi-Step Finanzpipeline mit Chained CTEs** – Baue eine Kette aus Monatsdaten und Benchmark-Werten.
3. **TODO 3: Rekursiver Datums-Generator** – Generiere lückenlos alle Tage vom 01.03.2024 bis zum 07.03.2024.
4. **TODO 4: Rekursive Organisations-Hierarchie** – Traverisiere das Mitarbeiter-Organigramm mit Berechnung von `ebene` und `pfad`.

---

## 🧪 Tests ausführen

Führe `test_aufgabe.sql` in der Web-IDE oder lokal per SQLite aus.
