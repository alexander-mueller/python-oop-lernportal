-- 🗄️ SQL 03: UPDATE, DELETE & ALTER TABLE 🗄️
-- ===========================================

-- 🎯 TEILZIEL 1 (TODO 1): Erstelle die Tabelle `mitarbeiter` und füge die 5 Testdatensätze ein.
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


-- 🎯 TEILZIEL 2 (TODO 2): Aktualisiere Mitarbeiter ID = 2:
-- Setze `abteilung = 'Management'` und `status = 'aktiv'`.
-- UPDATE ...;
UPDATE mitarbeiter 
SET abteilung = 'Management', status = 'aktiv' 
WHERE id = 2;


-- 🎯 TEILZIEL 3 (TODO 3): 10% Gehaltserhöhung (gehalt = gehalt * 1.10)
-- für alle Mitarbeiter der Abteilung 'IT', die den status 'aktiv' haben.
-- UPDATE ...;
UPDATE mitarbeiter 
SET gehalt = gehalt * 1.10 
WHERE abteilung = 'IT' AND status = 'aktiv';


-- 🎯 TEILZIEL 4 (TODO 4): Erweitere die Tabelle um eine neue Spalte:
-- `bonus REAL DEFAULT 0.0` mittels ALTER TABLE.
-- ALTER TABLE ...;
ALTER TABLE mitarbeiter ADD COLUMN bonus REAL DEFAULT 0.0;


-- 🎯 TEILZIEL 5 (TODO 5): Weise allen Mitarbeitern mit einem Gehalt von mindestens 60000.0
-- einen Bonus von 1500.0 Euro zu.
-- UPDATE ...;
UPDATE mitarbeiter 
SET bonus = 1500.0 
WHERE gehalt >= 60000.0;


-- 🎯 TEILZIEL 6 (TODO 6): Lösche alle Datensätze, die inaktiv sind (status = 'inaktiv')
-- UND deren Gehalt unter 35000.0 liegt.
-- DELETE FROM ...;
DELETE FROM mitarbeiter 
WHERE status = 'inaktiv' AND gehalt < 35000.0;
