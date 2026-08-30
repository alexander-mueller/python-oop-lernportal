-- ============================================================================
-- 🗄️ SQL 12: WINDOW FUNCTIONS (OVER, PARTITION BY, RANK, LAG) 🗄️
-- ============================================================================

-- ----------------------------------------------------------------------------
-- 1. TABELLEN-SCHEMA & TESTDATEN
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS artikel (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    kategorie_id INTEGER NOT NULL,
    preis REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS tages_umsatz (
    datum TEXT PRIMARY KEY,
    umsatz REAL NOT NULL,
    bestellungen INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS transaktionen (
    id INTEGER PRIMARY KEY,
    kunde_id INTEGER NOT NULL,
    datum TEXT NOT NULL,
    betrag REAL NOT NULL
);

-- Testdaten
INSERT INTO artikel (id, name, kategorie_id, preis) VALUES
    (1, 'Laptop Gaming X', 1, 1499.00),
    (2, 'Laptop Business Ultrabook', 1, 1499.00),
    (3, 'Laptop Student Basic', 1, 699.00),
    (4, 'Tastatur Mechanisch', 2, 129.00),
    (5, 'Tastatur Membran', 2, 39.00),
    (6, 'Maus RGB Gaming', 2, 69.00),
    (7, 'Maus Ergonomisch', 2, 69.00),
    (8, 'Maus Standard Office', 2, 19.00);

INSERT INTO tages_umsatz (datum, umsatz, bestellungen) VALUES
    ('2024-03-01', 1200.00, 15),
    ('2024-03-02', 1800.00, 22),
    ('2024-03-03', 1500.00, 19),
    ('2024-03-04', 2100.00, 26),
    ('2024-03-05', 2400.00, 30),
    ('2024-03-06', 1900.00, 24),
    ('2024-03-07', 2800.00, 35);

INSERT INTO transaktionen (id, kunde_id, datum, betrag) VALUES
    (1, 101, '2024-01-05', 150.00),
    (2, 101, '2024-01-20', 300.00),
    (3, 101, '2024-02-10', 450.00),
    (4, 102, '2024-01-08', 500.00),
    (5, 102, '2024-02-14', 250.00),
    (6, 103, '2024-01-12', 120.00),
    (7, 103, '2024-01-19', 80.00),
    (8, 103, '2024-02-25', 400.00);


-- ============================================================================
-- 🎯 AUFGABEN
-- ============================================================================

-- 🎯 TODO 1: Ranking-Vergleich (ROW_NUMBER vs. RANK vs. DENSE_RANK)
-- Berechne für alle Artikel eine Rangliste innerhalb ihrer kategorie_id,
-- sortiert nach dem Preis absteigend (teuerstes Produkt zuerst).
-- Gib folgende Spalten aus:
-- - id, name, kategorie_id, preis
-- - row_num:    ROW_NUMBER() OVER (PARTITION BY kategorie_id ORDER BY preis DESC)
-- - preis_rank: RANK() OVER (PARTITION BY kategorie_id ORDER BY preis DESC)
-- - dense_rank: DENSE_RANK() OVER (PARTITION BY kategorie_id ORDER BY preis DESC)
-- Sortiere das Gesamtergebnis nach kategorie_id ASC, row_num ASC.
SELECT 
    id,
    name,
    kategorie_id,
    preis
    -- TODO: Window-Funktionen ergänzen
FROM artikel;


-- 🎯 TODO 2: Time-Series Analyse mit LAG (Wachstumsraten & Delta)
-- Analysiere die täglichen Umsätze in tages_umsatz:
-- - datum, umsatz
-- - vortag_umsatz: Umsatz des Vortages mit LAG(umsatz, 1, 0) OVER (ORDER BY datum)
-- - delta_umsatz: Differenz zum Vortag (umsatz - LAG(umsatz, 1, umsatz) OVER (ORDER BY datum))
-- - wachstum_prozent: Prozentuales Wachstum zum Vortag gerundet auf 2 Stellen:
--   ROUND((umsatz - LAG(umsatz, 1, umsatz) OVER (ORDER BY datum)) * 100.0 / LAG(umsatz, 1, umsatz) OVER (ORDER BY datum), 2)
-- Sortiere chronologisch nach datum ASC.
SELECT 
    datum,
    umsatz
    -- TODO: LAG Berechnungen ergänzen
FROM tages_umsatz;


-- 🎯 TODO 3: Running Total (Kumulierter Kunden-Umsatz)
-- Berechne für jede Transaktion den fortlaufenden Gesamtumsatz des jeweiligen Kunden.
-- Spalten:
-- - id, kunde_id, datum, betrag
-- - laufender_umsatz: SUM(betrag) OVER (PARTITION BY kunde_id ORDER BY datum ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
-- Sortiere nach kunde_id ASC, datum ASC.
SELECT 
    id,
    kunde_id,
    datum,
    betrag
    -- TODO: Running Total Window Function ergänzen
FROM transaktionen;


-- 🎯 TODO 4: Gleitender 3-Tage Durchschnitt (Moving Average)
-- Berechne über die Tabelle tages_umsatz einen 3-Tage-Durchschnitt:
-- - datum, umsatz
-- - ma_3_tage: ROUND(AVG(umsatz) OVER (ORDER BY datum ROWS BETWEEN 2 PRECEDING AND CURRENT ROW), 2)
-- Sortiere nach datum ASC.
SELECT 
    datum,
    umsatz
    -- TODO: Moving Average Window Function ergänzen
FROM tages_umsatz;
