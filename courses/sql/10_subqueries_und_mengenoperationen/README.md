# SQL 10: Subqueries & Mengenoperationen 🔍🔀

Willkommen zu **Modul 10 (Lehrpfad 3: Aggregationen, CTEs & Window Functions)**!
In diesem Modul lernst du, wie du komplexe Geschäftslogik mit verschachtelten Unterabfragen (Subqueries) und mengentheoretischen Operatoren elegant und performant löst.

---

## 🎯 Lernziele

1. **Skalare Subqueries**: Nutzen von Unterabfragen in `SELECT` und `WHERE`, die genau einen Einzelwert (z.B. Durchschnitt) zurückliefern.
2. **Korrelierte Subqueries & EXISTS**: Zeilenweise Verknüpfung äußerer Tabellen mit Subqueries (`EXISTS` / `NOT EXISTS`) für performante Filterung.
3. **Mengenoperationen**: Vereinigen von Datensätzen mit `UNION` (Deduplizierung) und `UNION ALL` (maximale Performance).
4. **Schnitt- & Differenzmengen**: Finden von gemeinsamen Kunden (`INTERSECT`) und Ausschlussmengen (`EXCEPT`).

---

## 💡 Kernkonzepte

### 1. `IN` vs. `EXISTS`

- `IN`: Evaluiert die gesamte Subquery zu einer Wertemenge. Bei großen Datenmengen oder `NULL`-Werten kann `NOT IN` unerwartete Ergebnisse liefern.
- `EXISTS`: Prüft nur auf die **Existenz** mindestens einer Zeile und bricht die Suche sofort nach dem ersten Treffer ab (*Short-Circuiting*). Das ist in den meisten Fällen deutlich performanter.

```sql
-- Finde Kunden mit mindestens einer Bestellung
SELECT k.id, k.name 
FROM kunden k
WHERE EXISTS (
    SELECT 1 FROM bestellungen b 
    WHERE b.kunde_id = k.id
);
```

### 2. Die vier Mengenoperatoren im Überblick

| Operator | Duplikate | Wirkung |
| :--- | :--- | :--- |
| `UNION` | Werden entfernt | Vereinigung aller disjunkten Zeilen beider Abfragen |
| `UNION ALL` | Bleiben erhalten | Schnelles Aneinanderhängen beider Ergebnismengen |
| `INTERSECT` | Werden entfernt | Nur Zeilen, die in beiden Mengen vorkommen |
| `EXCEPT` | Werden entfernt | Zeilen aus Menge A, die NICHT in Menge B vorkommen |

---

## 🚀 Aufgabenstellung (`aufgabe.sql`)

1. **TODO 1: Skalare Subquery & Preisabweichung** – Finde Produkte über dem Durchschnittspreis und berechne die Differenz zum Mittelwert.
2. **TODO 2: Korrelierte Subquery mit NOT EXISTS** – Identifiziere loyale Kunden (Kauf online vorhanden, aber noch nie eine Retoure eingereicht).
3. **TODO 3: Multi-Channel Konsolidierung** – Vereinige Online- und Filialumsätze mit `UNION ALL`.
4. **TODO 4: Omnichannel vs. Pure-Online Analyse** – Berechne mit `INTERSECT` Kunden, die beide Kanäle nutzen, und mit `EXCEPT` reine Online-Käufer.

---

## 🧪 Tests ausführen

Validierung erfolgt über `test_aufgabe.sql` in der Web-IDE oder lokal per SQLite.
