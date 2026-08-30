PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS studenten (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    matrikelnummer TEXT NOT NULL UNIQUE,
    vorname TEXT NOT NULL,
    nachname TEXT NOT NULL,
    studiengang TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS kurse (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    kurs_code TEXT NOT NULL UNIQUE,
    titel TEXT NOT NULL,
    dozent TEXT NOT NULL,
    ects INTEGER NOT NULL CHECK (ects > 0)
);

CREATE TABLE IF NOT EXISTS einschreibungen (
    student_id INTEGER NOT NULL,
    kurs_id INTEGER NOT NULL,
    semester TEXT NOT NULL,
    note REAL CHECK (note >= 1.0 AND note <= 5.0),
    status TEXT NOT NULL DEFAULT 'angemeldet' CHECK (status IN ('angemeldet', 'bestanden', 'nicht_bestanden', 'abgebrochen')),
    PRIMARY KEY (student_id, kurs_id),
    FOREIGN KEY (student_id) REFERENCES studenten(id) ON DELETE CASCADE,
    FOREIGN KEY (kurs_id) REFERENCES kurse(id) ON DELETE CASCADE
);

INSERT INTO studenten (id, matrikelnummer, vorname, nachname, studiengang) VALUES
    (1, 'INF-2024-01', 'Felix', 'Neumann', 'Informatik'),
    (2, 'INF-2024-02', 'Hannah', 'Zimmermann', 'Informatik'),
    (3, 'WINF-2024-01', 'Lukas', 'Braun', 'Wirtschaftsinformatik'),
    (4, 'DS-2024-01', 'Marie', 'Krause', 'Data Science');

INSERT INTO kurse (id, kurs_code, titel, dozent, ects) VALUES
    (1, 'DB101', 'Datenbanken 1', 'Prof. Dr. Codd', 6),
    (2, 'PROG1', 'Programmierung in Python', 'Prof. Dr. Turing', 6),
    (3, 'WEB201', 'Fullstack Web Development', 'Dr. Berners-Lee', 5);

INSERT INTO einschreibungen (student_id, kurs_id, semester, note, status) VALUES
    (1, 1, 'WS2025', 1.3, 'bestanden'),
    (1, 2, 'WS2025', 1.7, 'bestanden'),
    (2, 1, 'WS2025', 2.0, 'bestanden'),
    (2, 3, 'SS2026', NULL, 'angemeldet'),
    (3, 1, 'WS2025', 3.7, 'bestanden'),
    (3, 3, 'SS2026', NULL, 'angemeldet'),
    (4, 2, 'WS2025', 1.0, 'bestanden');

-- 1. 3-Wege-Join
SELECT 
    s.vorname,
    s.nachname,
    k.titel AS kurs_titel,
    k.ects,
    e.semester,
    e.note
FROM studenten s
JOIN einschreibungen e ON s.id = e.student_id
JOIN kurse k ON e.kurs_id = k.id
ORDER BY s.nachname, k.kurs_code;

-- 2. DB101 Bestanden mit Note <= 2.0
SELECT 
    s.vorname,
    s.nachname,
    k.titel AS kurs_titel,
    e.note
FROM studenten s
JOIN einschreibungen e ON s.id = e.student_id
JOIN kurse k ON e.kurs_id = k.id
WHERE k.kurs_code = 'DB101' AND e.note <= 2.0
ORDER BY e.note ASC;

-- 3. Kaskadierendes Löschen testen
DELETE FROM kurse WHERE kurs_code = 'WEB201';
