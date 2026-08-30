CREATE TABLE IF NOT EXISTS mitarbeiter (
    id INTEGER PRIMARY KEY,
    vorname TEXT NOT NULL,
    nachname TEXT NOT NULL,
    abteilung TEXT NOT NULL,
    gehalt REAL NOT NULL,
    status TEXT NOT NULL DEFAULT 'aktiv'
);

INSERT INTO mitarbeiter (id, vorname, nachname, abteilung, gehalt, status) VALUES
    (1, 'Sarah', 'König', 'IT', 58000.0, 'aktiv'),
    (2, 'Markus', 'Bauer', 'Vertrieb', 45000.0, 'probezeit'),
    (3, 'Elena', 'Vogel', 'IT', 62000.0, 'aktiv'),
    (4, 'Florian', 'Richter', 'Marketing', 32000.0, 'inaktiv'),
    (5, 'Julia', 'Sommer', 'IT', 71000.0, 'aktiv');

-- 1. Beförderung Markus Bauer
UPDATE mitarbeiter 
SET abteilung = 'Management', status = 'aktiv' 
WHERE id = 2;

-- 2. 10% Gehaltserhöhung IT
UPDATE mitarbeiter 
SET gehalt = gehalt * 1.10 
WHERE abteilung = 'IT' AND status = 'aktiv';

-- 3. Schema erweitern
ALTER TABLE mitarbeiter ADD COLUMN bonus REAL DEFAULT 0.0;

-- 4. Bonus für Gehalt >= 60000
UPDATE mitarbeiter 
SET bonus = 1500.0 
WHERE gehalt >= 60000.0;

-- 5. Inaktive Geringverdiener löschen
DELETE FROM mitarbeiter 
WHERE status = 'inaktiv' AND gehalt < 35000.0;
