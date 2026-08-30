# SQL 12: Window Functions (ROW_NUMBER, OVER, PARTITION BY, LAG) 🪟📊

Willkommen zu **Modul 12 (Lehrpfad 3: Aggregationen, CTEs & Window Functions)**!
Window Functions sind der Goldstandard moderner SQL-Analytik in BigQuery, Snowflake, PostgreSQL und SQLite. Sie erlauben tiefgehende Berechnungen über benachbarte Zeilen, ohne den Detailgrad der Datensätze zu vernichten.

---

## 🎯 Lernziele

1. **Die `OVER()`-Klausel**: Definieren von Analyse-Fenstern mit `PARTITION BY` und `ORDER BY`.
2. **Ranking-Funktionen**: Verstehen der Unterschiede zwischen `ROW_NUMBER()`, `RANK()` und `DENSE_RANK()`.
3. **Offset-Navigation (`LAG` & `LEAD`)**: Berechnen von Periodenvergleichen, Wachstumsraten und Deltas ohne Self-Joins.
4. **Kumulierte Summen (Running Totals)**: Fortlaufende Kontostände und Allzeit-Umsätze berechnen.
5. **Gleitende Durchschnitte (Moving Averages)**: Glätten von Zeitreihen über `ROWS BETWEEN n PRECEDING AND CURRENT ROW`.

---

## 💡 Syntax im Detail

```sql
-- Fortlaufende Summe je Kunde
SELECT 
    kunde_id,
    bestell_datum,
    betrag,
    SUM(betrag) OVER (
        PARTITION BY kunde_id
        ORDER BY bestell_datum
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS kumulierter_umsatz
FROM bestellungen;
```

---

## 🚀 Aufgabenstellung (`aufgabe.sql`)

1. **TODO 1: Ranking-Vergleich** – Berechne für Produkte innerhalb jeder Kategorie `ROW_NUMBER()`, `RANK()` und `DENSE_RANK()`.
2. **TODO 2: Time-Series Analyse mit LAG** – Berechne Vortagesumsatz, absolutes Delta und prozentuales Wachstum.
3. **TODO 3: Running Total** – Ermittle den kumulierten Allzeitumsatz je Kunde.
4. **TODO 4: Moving Average** – Berechne den 3-Tage gleitenden Durchschnitt über die täglichen Gesamtumsätze.

---

## 🧪 Tests ausführen

Validierung erfolgt über `test_aufgabe.sql`.
