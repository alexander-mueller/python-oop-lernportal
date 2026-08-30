# SQL 03: Daten aktualisieren, löschen & Tabellen anpassen 🔄

Willkommen zu **Modul 03** des SQL & Datenbanken Kurses!

Datenbanken sind lebendige Systeme: Gehälter ändern sich, Abteilungen werden umbenannt, inaktive Datensätze müssen bereinigt werden und Tabellenschemata wachsen mit den Anforderungen. In diesem Modul meisterst du `UPDATE`, `DELETE` und `ALTER TABLE`.

---

## 💡 1. Das Wichtigste in Kürze

### Datensätze aktualisieren (`UPDATE`)
```sql
-- Einzelnes Feld aktualisieren
UPDATE mitarbeiter 
SET abteilung = 'Management' 
WHERE id = 2;

-- Mehrere Felder gleichzeitig aktualisieren
UPDATE mitarbeiter 
SET abteilung = 'DevOps', status = 'aktiv' 
WHERE id = 3;

-- Rechnen im UPDATE (z.B. 8% Gehaltserhöhung)
UPDATE mitarbeiter 
SET gehalt = gehalt * 1.08 
WHERE abteilung = 'IT' AND status = 'aktiv';
```

### Datensätze löschen (`DELETE`)
```sql
-- Gezielt Zeilen löschen
DELETE FROM mitarbeiter 
WHERE status = 'inaktiv' AND gehalt < 35000;
```

> ⚠️ **ACHTUNG:** Ein `UPDATE` oder `DELETE` **ohne** `WHERE`-Klausel betrifft **ALLE** Zeilen der gesamten Tabelle!

### Tabellenstruktur erweitern (`ALTER TABLE`)
```sql
-- 1. Neue Spalte hinzufügen
ALTER TABLE mitarbeiter ADD COLUMN bonus REAL DEFAULT 0.0;

-- 2. Spalte umbenennen
ALTER TABLE mitarbeiter RENAME COLUMN gehalt TO monatsgehalt;

-- 3. Tabelle umbenennen
ALTER TABLE mitarbeiter RENAME TO angestellte;
```

---

## 🎯 Aufgaben in `aufgabe.sql`

1. **TODO 1**: Tabelle `mitarbeiter` erstellen und 5 Testmitarbeiter einfügen.
2. **TODO 2**: Mitarbeiter mit `id = 2` in die Abteilung `'Management'` versetzen und auf `'aktiv'` setzen.
3. **TODO 3**: 10% Gehaltserhöhung (`gehalt = gehalt * 1.10`) für alle aktiven Mitarbeiter in der `'IT'`.
4. **TODO 4**: Neue Spalte `bonus REAL DEFAULT 0.0` per `ALTER TABLE` hinzufügen.
5. **TODO 5**: Allen Mitarbeitern mit `gehalt >= 60000` einen `bonus` von `1500.0` Euro zuweisen.
6. **TODO 6**: Alle Mitarbeiter löschen, die `status = 'inaktiv'` sind UND ein `gehalt < 35000` haben.

---

## 🚀 Ausführung
Klicke in der Web-IDE auf **Code ausführen** oder **Tests ausführen**, um deine Änderungen in der SQLite-Datenbank zu verifizieren.
