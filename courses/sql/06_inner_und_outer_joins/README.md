# SQL 06: Relationale Joins (INNER, LEFT & Multi-Table) 🔀

Willkommen zu **Modul 06** des SQL & Datenbanken Kurses!

In relationalen Datenbanken sind Daten über mehrere spezialisierte Tabellen verteilt. Mit **JOINs** führst du diese Daten zur Abfragezeit wieder zusammen.

---

## 💡 1. Das Wichtigste in Kürze

### Die wichtigsten Join-Typen

1. **`INNER JOIN`**: Liefert nur Datensätze zurück, bei denen in **beiden** Tabellen eine Übereinstimmung vorliegt (Schnittmenge).
2. **`LEFT JOIN` (LEFT OUTER JOIN)**: Liefert **alle** Zeilen der linken Tabelle, ergänzt um die passenden Daten der rechten Tabelle. Gibt es rechts keinen Treffer, werden die Spalten mit `NULL` aufgefüllt.
3. **Anti-Join**: Ein `LEFT JOIN` kombiniert mit `WHERE rechte_tabelle.id IS NULL`, um Datensätze zu finden, die **keine** Zuordnung haben.

### Syntax mit Tabellen-Aliasen
```sql
-- 1. INNER JOIN (Nur Mitarbeiter mit zugewiesener Abteilung)
SELECT m.name, m.rolle, a.name AS abteilungs_name
FROM mitarbeiter m
INNER JOIN abteilungen a ON m.abteilung_id = a.id;

-- 2. LEFT JOIN (Alle Mitarbeiter, auch jene ohne Abteilung wie externe Berater)
SELECT m.name, m.rolle, a.name AS abteilungs_name
FROM mitarbeiter m
LEFT JOIN abteilungen a ON m.abteilung_id = a.id;

-- 3. Anti-Join (Finde alle Abteilungen OHNE Mitarbeiter)
SELECT a.id, a.name
FROM abteilungen a
LEFT JOIN mitarbeiter m ON a.id = m.abteilung_id
WHERE m.id IS NULL;

-- 4. Multi-Table JOIN (3 Tabellen verknüpfen)
SELECT m.name AS mitarbeiter, a.name AS abteilung, s.stadt, s.land
FROM mitarbeiter m
INNER JOIN abteilungen a ON m.abteilung_id = a.id
INNER JOIN standorte s ON a.standort_id = s.id;
```

---

## 🎯 Aufgaben in `aufgabe.sql`

1. **TODO 1**: Tabellen `standorte`, `abteilungen` und `mitarbeiter` mit Testdaten anlegen.
2. **TODO 2**: `INNER JOIN`: Mitarbeiter mit Abteilungsnamen abfragen.
3. **TODO 3**: `LEFT JOIN`: Alle Mitarbeiter (inklusive externe Berater ohne Abteilung) abfragen.
4. **TODO 4**: Anti-Join: Alle Abteilungen finden, denen noch kein Mitarbeiter zugewiesen ist.
5. **TODO 5**: Multi-Table JOIN: Verbinde `mitarbeiter`, `abteilungen` und `standorte`.

---

## 🚀 Ausführung
Klicke in der Web-IDE auf **Code ausführen** oder **Tests ausführen**, um deine Join-Abfragen auszuführen.
