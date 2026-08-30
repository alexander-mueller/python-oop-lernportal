-- ============================================================================
-- 🗄️ SQL 11: COMMON TABLE EXPRESSIONS (WITH CTE & RECURSIVE) 🗄️
-- ============================================================================

-- ----------------------------------------------------------------------------
-- 1. TABELLEN-SCHEMA & TESTDATEN
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS kunden (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    stadt TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS bestellungen (
    id INTEGER PRIMARY KEY,
    kunde_id INTEGER NOT NULL,
    bestell_datum TEXT NOT NULL,
    gesamtbetrag REAL NOT NULL,
    status TEXT NOT NULL,
    FOREIGN KEY (kunde_id) REFERENCES kunden(id)
);

CREATE TABLE IF NOT EXISTS monats_umsatz_raw (
    monat TEXT PRIMARY KEY,
    umsatz REAL NOT NULL,
    kosten REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS mitarbeiter (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    position TEXT NOT NULL,
    vorgesetzter_id INTEGER,
    gehalt REAL NOT NULL,
    FOREIGN KEY (vorgesetzter_id) REFERENCES mitarbeiter(id)
);

-- Testdaten
INSERT INTO kunden (id, name, stadt) VALUES
    (1, 'TechCorp GmbH', 'München'),
    (2, 'CloudNet AG', 'Frankfurt'),
    (3, 'WebSolutions', 'Berlin'),
    (4, 'DataLab KG', 'Hamburg');

INSERT INTO bestellungen (id, kunde_id, bestell_datum, gesamtbetrag, status) VALUES
    (101, 1, '2024-01-10', 1500.00, 'abgeschlossen'),
    (102, 1, '2024-02-12', 2300.00, 'abgeschlossen'),
    (103, 2, '2024-01-15', 450.00, 'abgeschlossen'),
    (104, 3, '2024-02-20', 890.00, 'abgeschlossen'),
    (105, 3, '2024-03-05', 120.00, 'abgeschlossen');

INSERT INTO monats_umsatz_raw (monat, umsatz, kosten) VALUES
    ('2024-01', 50000.00, 32000.00),
    ('2024-02', 45000.00, 31000.00),
    ('2024-03', 68000.00, 35000.00),
    ('2024-04', 72000.00, 36000.00),
    ('2024-05', 41000.00, 30000.00),
    ('2024-06', 85000.00, 40000.00);

INSERT INTO mitarbeiter (id, name, position, vorgesetzter_id, gehalt) VALUES
    (1, 'Dr. Victoria Vance', 'CEO', NULL, 150000),
    (2, 'Marcus Meyer', 'VP Engineering', 1, 110000),
    (3, 'Sabine Schultze', 'VP Marketing', 1, 105000),
    (4, 'Lukas Weber', 'Lead Backend Engineer', 2, 85000),
    (5, 'Julia Neumann', 'Senior Data Engineer', 2, 82000),
    (6, 'Tim Franke', 'Performance Marketer', 3, 60000),
    (7, 'Sophie Klein', 'Junior Data Analyst', 5, 52000);


-- ============================================================================
-- 🎯 AUFGABEN
-- ============================================================================

-- 🎯 TODO 1: Einfache CTE & Kunden-Segmentierung
-- Erstelle eine CTE `kunden_stats`, die für jeden Kunden die Anzahl der
-- abgeschlossenen Bestellungen (bestell_anzahl) und die Gesamtsumme (gesamt_umsatz) ermittelt.
-- Selektiere im Haupt-SELECT:
-- - k.name
-- - ks.bestell_anzahl
-- - ks.gesamt_umsatz
-- - segment: Einteilung via CASE WHEN:
--     * gesamt_umsatz >= 2000 THEN 'VIP'
--     * gesamt_umsatz >= 500 THEN 'Regulär'
--     * ELSE 'Basis'
-- Sortiere nach gesamt_umsatz DESC.
-- TODO: WITH kunden_stats AS (...) SELECT ...


-- 🎯 TODO 2: Gekettete Chained CTEs für Finanz-Benchmarking
-- Erstelle zwei verkettete CTEs:
-- 1. `monats_gewinn`: Berechnet monat, umsatz, kosten, gewinn (umsatz - kosten)
-- 2. `benchmark`: Berechnet avg_gewinn (AVG(gewinn) aus monats_gewinn)
-- Haupt-SELECT:
-- Selektiere monat, gewinn, avg_gewinn, (gewinn - avg_gewinn) AS uebergewinn
-- für alle Monate, deren gewinn >= avg_gewinn ist.
-- Sortiere nach monat ASC.
-- TODO: WITH monats_gewinn AS (...), benchmark AS (...) SELECT ...


-- 🎯 TODO 3: Rekursiver Datums-Generator (Kalenderreihe)
-- Erzeuge mit WITH RECURSIVE kalender(datum) eine lückenlose Reihe aller Tage
-- vom '2024-03-01' bis zum '2024-03-07'.
-- TODO: WITH RECURSIVE kalender(datum) AS (...) SELECT ...


-- 🎯 TODO 4: Rekursives Organigramm (Hierarchie-Traversierung)
-- Erstelle eine rekursive CTE `organigramm` mit Spalten:
-- - id, name, position, vorgesetzter_id, ebene, pfad
-- Anker (Wurzel): CEO (vorgesetzter_id IS NULL), ebene = 1, pfad = name
-- Rekursionsschritt: Kind-Mitarbeiter joinen, ebene = o.ebene + 1,
--                    pfad = o.pfad || ' -> ' || m.name
-- Haupt-SELECT: id, name, position, ebene, pfad sortiert nach pfad ASC.
-- TODO: WITH RECURSIVE organigramm AS (...) SELECT ...
