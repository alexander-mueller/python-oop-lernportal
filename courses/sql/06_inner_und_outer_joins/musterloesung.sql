CREATE TABLE IF NOT EXISTS standorte (
    id INTEGER PRIMARY KEY,
    stadt TEXT NOT NULL,
    land TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS abteilungen (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    standort_id INTEGER,
    FOREIGN KEY (standort_id) REFERENCES standorte(id)
);

CREATE TABLE IF NOT EXISTS mitarbeiter (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    rolle TEXT NOT NULL,
    gehalt REAL NOT NULL,
    abteilung_id INTEGER,
    FOREIGN KEY (abteilung_id) REFERENCES abteilungen(id)
);

INSERT INTO standorte (id, stadt, land) VALUES
    (1, 'Berlin', 'Deutschland'),
    (2, 'Zürich', 'Schweiz'),
    (3, 'Wien', 'Österreich');

INSERT INTO abteilungen (id, name, standort_id) VALUES
    (1, 'Softwareentwicklung', 1),
    (2, 'Finanzen & Controlling', 2),
    (3, 'Marketing & PR', 1),
    (4, 'Forschung & KI', 3);

INSERT INTO mitarbeiter (id, name, rolle, gehalt, abteilung_id) VALUES
    (1, 'Lukas Schmidt', 'Senior Developer', 75000.0, 1),
    (2, 'Sophie Meyer', 'Cloud Architect', 82000.0, 1),
    (3, 'Jan Becker', 'Financial Analyst', 64000.0, 2),
    (4, 'Mia Wagner', 'Marketing Lead', 59000.0, 3),
    (5, 'Dr. Aris Thorne', 'Externer KI-Berater', 95000.0, NULL);

-- 1. INNER JOIN
SELECT 
    m.name AS mitarbeiter_name, 
    m.rolle, 
    a.name AS abteilung_name
FROM mitarbeiter m
INNER JOIN abteilungen a ON m.abteilung_id = a.id;

-- 2. LEFT JOIN
SELECT 
    m.name AS mitarbeiter_name, 
    m.rolle, 
    COALESCE(a.name, 'Keine Abteilung') AS abteilung_name
FROM mitarbeiter m
LEFT JOIN abteilungen a ON m.abteilung_id = a.id;

-- 3. Anti-Join (Abteilungen ohne Mitarbeiter)
SELECT 
    a.id AS abteilung_id, 
    a.name AS abteilung_name
FROM abteilungen a
LEFT JOIN mitarbeiter m ON a.id = m.abteilung_id
WHERE m.id IS NULL;

-- 4. Multi-Table JOIN
SELECT 
    m.name AS mitarbeiter_name,
    a.name AS abteilung_name,
    s.stadt,
    s.land
FROM mitarbeiter m
INNER JOIN abteilungen a ON m.abteilung_id = a.id
INNER JOIN standorte s ON a.standort_id = s.id;
