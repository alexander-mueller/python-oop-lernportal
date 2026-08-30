# SQL 04: Datentypen & Constraints (CHECK, UNIQUE, NOT NULL) 🛡️

Willkommen zu **Modul 04** des SQL & Datenbanken Kurses!

Eine Datenbank ist nur so gut wie die Qualität der gespeicherten Daten. **Constraints** (Integritätsbedingungen) stellen sicher, dass ungültige, unvollständige oder fehlerhafte Daten erst gar nicht in der Datenbank landen ("Garbage In, Garbage Out"-Schutz).

---

## 💡 1. Das Wichtigste in Kürze

### Die 5 SQLite-Datentypen
1. **`INTEGER`**: Ganzzahlen (1, 42, -500).
2. **`REAL`**: Fließkommazahlen (3.1415, 99.95).
3. **`TEXT`**: Zeichenketten und Texte UTF-8 ('Max', 'Berlin').
4. **`BLOB`**: Rohdaten / Binärdaten (z.B. Bilder, Dokumente).
5. **`NULL`**: Fehlender / leerer Wert.

### Wichtige Constraints im Überblick
- **`PRIMARY KEY`**: Eindeutige Kennung jeder Zeile.
- **`NOT NULL`**: Spalte darf nicht leer bleiben.
- **`UNIQUE`**: Keine Duplikate erlaubt (z.B. E-Mail, IBAN, Benutzername).
- **`DEFAULT <wert>`**: Standardwert, falls kein Wert beim `INSERT` übergeben wird.
- **`CHECK (<bedingung>)`**: Benutzerdefinierte Validierungslogik.

```sql
CREATE TABLE bank_kunden (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    kunden_nr TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    kunden_alter INTEGER NOT NULL CHECK (kunden_alter >= 18),
    bonitaets_score INTEGER NOT NULL DEFAULT 500 CHECK (bonitaets_score BETWEEN 100 AND 1000),
    status TEXT NOT NULL DEFAULT 'aktiv' CHECK (status IN ('aktiv', 'verifiziert', 'gesperrt')),
    registriert_am TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

### Tabellen mit Kontobedingungen
```sql
CREATE TABLE bank_konten (
    iban TEXT PRIMARY KEY,
    kunden_id INTEGER NOT NULL,
    kontotyp TEXT NOT NULL CHECK (kontotyp IN ('Girokonto', 'Sparkonto', 'Tagesgeld')),
    saldo REAL NOT NULL DEFAULT 0.0 CHECK (saldo >= -500.0),
    waehrung TEXT NOT NULL DEFAULT 'EUR' CHECK (waehrung IN ('EUR', 'USD', 'CHF'))
);
```

---

## 🎯 Aufgaben in `aufgabe.sql`

1. **TODO 1**: Tabelle `bank_kunden` mit `NOT NULL`, `UNIQUE`, `CHECK(kunden_alter >= 18)`, `CHECK(bonitaets_score BETWEEN 100 AND 1000)` und `DEFAULT` anlegen.
2. **TODO 2**: Tabelle `bank_konten` mit `PRIMARY KEY(iban)`, `CHECK(saldo >= -500.0)` und `CHECK(kontotyp IN (...))` anlegen.
3. **TODO 3**: 4 valide Testkunden einfügen.
4. **TODO 4**: 4 passende Bankkonten mit unterschiedlichen Kontotypen und Salden einfügen.
5. **TODO 5**: Alle verifizierten Kunden mit Bonitäts-Score >= 600 abfragen.
6. **TODO 6**: Alle Konten mit Dispo-Nutzung (`saldo < 0.0`) abfragen.

---

## 🚀 Ausführung
Klicke in der Web-IDE auf **Code ausführen** oder **Tests ausführen**, um deine Schema-Constraints gegen die Test-Suite zu validieren.
