-- ============================================================================
-- 💡 SQL 11: MUSTERLÖSUNG – COMMON TABLE EXPRESSIONS (CTE) 💡
-- ============================================================================

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

INSERT OR REPLACE INTO kunden (id, name, stadt) VALUES
    (1, 'TechCorp GmbH', 'München'),
    (2, 'CloudNet AG', 'Frankfurt'),
    (3, 'WebSolutions', 'Berlin'),
    (4, 'DataLab KG', 'Hamburg');

INSERT OR REPLACE INTO bestellungen (id, kunde_id, bestell_datum, gesamtbetrag, status) VALUES
    (101, 1, '2024-01-10', 1500.00, 'abgeschlossen'),
    (102, 1, '2024-02-12', 2300.00, 'abgeschlossen'),
    (103, 2, '2024-01-15', 450.00, 'abgeschlossen'),
    (104, 3, '2024-02-20', 890.00, 'abgeschlossen'),
    (105, 3, '2024-03-05', 120.00, 'abgeschlossen');

INSERT OR REPLACE INTO monats_umsatz_raw (monat, umsatz, kosten) VALUES
    ('2024-01', 50000.00, 32000.00),
    ('2024-02', 45000.00, 31000.00),
    ('2024-03', 68000.00, 35000.00),
    ('2024-04', 72000.00, 36000.00),
    ('2024-05', 41000.00, 30000.00),
    ('2024-06', 85000.00, 40000.00);

INSERT OR REPLACE INTO mitarbeiter (id, name, position, vorgesetzter_id, gehalt) VALUES
    (1, 'Dr. Victoria Vance', 'CEO', NULL, 150000),
    (2, 'Marcus Meyer', 'VP Engineering', 1, 110000),
    (3, 'Sabine Schultze', 'VP Marketing', 1, 105000),
    (4, 'Lukas Weber', 'Lead Backend Engineer', 2, 85000),
    (5, 'Julia Neumann', 'Senior Data Engineer', 2, 82000),
    (6, 'Tim Franke', 'Performance Marketer', 3, 60000),
    (7, 'Sophie Klein', 'Junior Data Analyst', 5, 52000);

-- 🎯 TODO 1: Einfache CTE & Kunden-Segmentierung
WITH kunden_stats AS (
    SELECT 
        kunde_id,
        COUNT(id) AS bestell_anzahl,
        SUM(gesamtbetrag) AS gesamt_umsatz
    FROM bestellungen
    WHERE status = 'abgeschlossen'
    GROUP BY kunde_id
)
SELECT 
    k.name,
    COALESCE(ks.bestell_anzahl, 0) AS bestell_anzahl,
    COALESCE(ks.gesamt_umsatz, 0.0) AS gesamt_umsatz,
    CASE 
        WHEN COALESCE(ks.gesamt_umsatz, 0) >= 2000 THEN 'VIP'
        WHEN COALESCE(ks.gesamt_umsatz, 0) >= 500 THEN 'Regulär'
        ELSE 'Basis'
    END AS segment
FROM kunden k
LEFT JOIN kunden_stats ks ON k.id = ks.kunde_id
ORDER BY gesamt_umsatz DESC;

-- 🎯 TODO 2: Gekettete Chained CTEs für Finanz-Benchmarking
WITH monats_gewinn AS (
    SELECT 
        monat,
        umsatz,
        kosten,
        (umsatz - kosten) AS gewinn
    FROM monats_umsatz_raw
),
benchmark AS (
    SELECT AVG(gewinn) AS avg_gewinn FROM monats_gewinn
)
SELECT 
    mg.monat,
    mg.gewinn,
    b.avg_gewinn,
    (mg.gewinn - b.avg_gewinn) AS uebergewinn
FROM monats_gewinn mg, benchmark b
WHERE mg.gewinn >= b.avg_gewinn
ORDER BY mg.monat ASC;

-- 🎯 TODO 3: Rekursiver Datums-Generator (Kalenderreihe)
WITH RECURSIVE kalender(datum) AS (
    SELECT '2024-03-01'
    UNION ALL
    SELECT DATE(datum, '+1 day')
    FROM kalender
    WHERE datum < '2024-03-07'
)
SELECT datum FROM kalender;

-- 🎯 TODO 4: Rekursives Organigramm (Hierarchie-Traversierung)
WITH RECURSIVE organigramm AS (
    -- Anker
    SELECT 
        id,
        name,
        position,
        vorgesetzter_id,
        1 AS ebene,
        name AS pfad
    FROM mitarbeiter
    WHERE vorgesetzter_id IS NULL
    
    UNION ALL
    
    -- Rekursionsschritt
    SELECT 
        m.id,
        m.name,
        m.position,
        m.vorgesetzter_id,
        o.ebene + 1,
        o.pfad || ' -> ' || m.name
    FROM mitarbeiter m
    JOIN organigramm o ON m.vorgesetzter_id = o.id
)
SELECT 
    id,
    name,
    position,
    ebene,
    pfad
FROM organigramm
ORDER BY pfad ASC;
