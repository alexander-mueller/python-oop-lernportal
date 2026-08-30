# SQL 08: n:m Beziehungen & Junction Tables 🌐

Willkommen zu **Modul 08** und dem Finale von **Lehrpfad 2: Relationale Joins & Datenbank-Design**!

Viele reale Beziehungen sind n:m-Beziehungen (Viele-zu-Viele): Ein Student belegt viele Kurse, und ein Kurs hat viele Studenten. Relationale Datenbanken können n:m nicht direkt in einer einzigen Fremdschlüsselspalte speichern – sie nutzen eine **Junction Table** (Verknüpfungstabelle).

---

## 💡 1. Das Wichtigste in Kürze

### Die Anatomie einer Junction Table (n:m Brücke)

```
┌──────────────────┐               ┌─────────────────────────┐               ┌──────────────────┐
│    studenten     │  1         n  │     einschreibungen     │  n         1  │      kurse       │
├──────────────────┤ ───────────── │    (Junction Table)     │ ───────────── ├──────────────────┤
│ PK id            │               ├─────────────────────────┤               │ PK id            │
│    name          │               │ PK,FK student_id        │               │    titel         │
└──────────────────┘               │ PK,FK kurs_id           │               │    ects          │
                                   │       semester          │               └──────────────────┘
                                   │       note              │
                                   └─────────────────────────┘
```

### Definition mit zusammengesetztem Primärschlüssel
```sql
CREATE TABLE einschreibungen (
    student_id INTEGER NOT NULL,
    kurs_id INTEGER NOT NULL,
    semester TEXT NOT NULL,
    note REAL CHECK (note >= 1.0 AND note <= 5.0),
    status TEXT NOT NULL DEFAULT 'angemeldet',
    -- Zusammengesetzter Primärschlüssel verhindert Doppel-Einschreibungen:
    PRIMARY KEY (student_id, kurs_id),
    FOREIGN KEY (student_id) REFERENCES studenten(id) ON DELETE CASCADE,
    FOREIGN KEY (kurs_id) REFERENCES kurse(id) ON DELETE CASCADE
);
```

### Abfrage über zwei JOINs (3-Wege-Join)
```sql
SELECT 
    s.matrikelnummer,
    s.vorname || ' ' || s.nachname AS student,
    k.titel AS kurs,
    k.ects,
    e.semester,
    e.note
FROM studenten s
JOIN einschreibungen e ON s.id = e.student_id
JOIN kurse k ON e.kurs_id = k.id
ORDER BY s.nachname, k.kurs_code;
```

---

## 🎯 Aufgaben in `aufgabe.sql`

1. **TODO 1**: `PRAGMA foreign_keys = ON;` setzen und Tabellen `studenten` und `kurse` anlegen.
2. **TODO 2**: Junction Table `einschreibungen` mit `PRIMARY KEY (student_id, kurs_id)` und `ON DELETE CASCADE` erstellen.
3. **TODO 3**: 4 Studenten, 3 Kurse und 7 Einschreibungen einfügen.
4. **TODO 4**: 3-Wege-Join-Abfrage schreiben (Studentenname, Kurs-Titel, ECTS, Semester, Note).
5. **TODO 5**: Alle Studenten finden, die den Kurs mit Code `'DB101'` mit Note <= 2.0 bestanden haben.
6. **TODO 6**: Kaskadierendes Löschen testen: Lösche den Kurs `'WEB201'` (`DELETE FROM kurse WHERE kurs_code = 'WEB201';`) und prüfe, dass alle Verknüpfungen in `einschreibungen` automatisch gelöscht wurden.

---

## 🚀 Ausführung
Klicke in der Web-IDE auf **Code ausführen** oder **Tests ausführen**, um deine n:m-Modellierung zu überprüfen.
