# SQL 05: Foreign Keys & Relationen (1:1 und 1:n) 🔗

Willkommen zu **Modul 05** und **Lehrpfad 2: Relationale Joins & Datenbank-Design**!

Das "R" in RDBMS steht für **Relational**. Tabellen stehen nicht isoliert für sich, sondern sind über logische Beziehungen (Fremdschlüssel / Foreign Keys) miteinander verknüpft.

---

## 💡 1. Das Wichtigste in Kürze

### 1. Fremdschlüssel-Prüfung aktivieren in SQLite
In SQLite ist die Prüfung von Fremdschlüsseln aus historischen Gründen standardmäßig deaktiviert. Aktiviere sie immer zu Beginn:
```sql
PRAGMA foreign_keys = ON;
```

### 2. 1:1 Beziehung (Ein Kunde hat genau ein Detailprofil)
Eine 1:1 Beziehung entsteht, indem der Fremdschlüssel zusätzlich als `UNIQUE` deklariert wird:
```sql
CREATE TABLE kunden_profile (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    kunde_id INTEGER NOT NULL UNIQUE,
    telefon TEXT,
    lieferadresse TEXT NOT NULL,
    FOREIGN KEY (kunde_id) REFERENCES kunden(id) ON DELETE CASCADE
);
```

### 3. 1:n Beziehung (Ein Kunde hat viele Bestellungen)
Ein Kunde kann 0, 1 oder 100 Bestellungen aufgeben. Jede Bestellung gehört aber zu genau einem Kunden:
```sql
CREATE TABLE bestellungen (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    kunde_id INTEGER NOT NULL,
    bestelldatum TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    gesamtbetrag REAL NOT NULL CHECK (gesamtbetrag >= 0.0),
    status TEXT NOT NULL DEFAULT 'offen' CHECK (status IN ('offen', 'bezahlt', 'versendet', 'storniert')),
    FOREIGN KEY (kunde_id) REFERENCES kunden(id) ON DELETE CASCADE
);
```

### 4. Kaskadierendes Löschen (`ON DELETE CASCADE`)
Wenn ein Datensatz in der Elterntabelle (`kunden`) gelöscht wird:
- **`ON DELETE CASCADE`**: Alle verknüpften Kinder (Profile, Bestellungen) werden automatisch mitgelöscht.
- **`ON DELETE RESTRICT`**: Das Löschen des Kunden wird mit einem Fehler blockiert, solange noch Bestellungen existieren.
- **`ON DELETE SET NULL`**: Der Fremdschlüssel `kunde_id` im Kind wird auf `NULL` gesetzt.

---

## 🎯 Aufgaben in `aufgabe.sql`

1. **TODO 1**: `PRAGMA foreign_keys = ON;` setzen und Elterntabelle `kunden` anlegen.
2. **TODO 2**: 1:1 Tabelle `kunden_profile` mit `UNIQUE` auf `kunde_id` und `ON DELETE CASCADE` erstellen.
3. **TODO 3**: 1:n Tabelle `bestellungen` mit `FOREIGN KEY` und `ON DELETE CASCADE` erstellen.
4. **TODO 4**: 3 Kunden, 3 Profile und 5 Bestellungen einfügen.
5. **TODO 5**: Den Kunden mit `id = 1` löschen (`DELETE FROM kunden WHERE id = 1;`).
6. **TODO 6**: Verifizieren, dass Profil und Bestellungen von Kunde 1 automatisch kaskadierend mitgelöscht wurden.

---

## 🚀 Ausführung
Klicke in der Web-IDE auf **Code ausführen** oder **Tests ausführen**, um die referenzielle Integrität deiner Tabellen zu testen.
