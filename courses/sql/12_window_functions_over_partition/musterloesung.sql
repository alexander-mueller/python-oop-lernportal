-- ============================================================================
-- 💡 SQL 12: MUSTERLÖSUNG – WINDOW FUNCTIONS 💡
-- ============================================================================

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

INSERT OR REPLACE INTO artikel (id, name, kategorie_id, preis) VALUES
    (1, 'Laptop Gaming X', 1, 1499.00),
    (2, 'Laptop Business Ultrabook', 1, 1499.00),
    (3, 'Laptop Student Basic', 1, 699.00),
    (4, 'Tastatur Mechanisch', 2, 129.00),
    (5, 'Tastatur Membran', 2, 39.00),
    (6, 'Maus RGB Gaming', 2, 69.00),
    (7, 'Maus Ergonomisch', 2, 69.00),
    (8, 'Maus Standard Office', 2, 19.00);

INSERT OR REPLACE INTO tages_umsatz (datum, umsatz, bestellungen) VALUES
    ('2024-03-01', 1200.00, 15),
    ('2024-03-02', 1800.00, 22),
    ('2024-03-03', 1500.00, 19),
    ('2024-03-04', 2100.00, 26),
    ('2024-03-05', 2400.00, 30),
    ('2024-03-06', 1900.00, 24),
    ('2024-03-07', 2800.00, 35);

INSERT OR REPLACE INTO transaktionen (id, kunde_id, datum, betrag) VALUES
    (1, 101, '2024-01-05', 150.00),
    (2, 101, '2024-01-20', 300.00),
    (3, 101, '2024-02-10', 450.00),
    (4, 102, '2024-01-08', 500.00),
    (5, 102, '2024-02-14', 250.00),
    (6, 103, '2024-01-12', 120.00),
    (7, 103, '2024-01-19', 80.00),
    (8, 103, '2024-02-25', 400.00);

-- 🎯 TODO 1: Ranking-Vergleich
SELECT 
    id,
    name,
    kategorie_id,
    preis,
    ROW_NUMBER() OVER (PARTITION BY kategorie_id ORDER BY preis DESC, id ASC) AS row_num,
    RANK() OVER (PARTITION BY kategorie_id ORDER BY preis DESC) AS preis_rank,
    DENSE_RANK() OVER (PARTITION BY kategorie_id ORDER BY preis DESC) AS dense_rank
FROM artikel
ORDER BY kategorie_id ASC, row_num ASC;

-- 🎯 TODO 2: Time-Series Analyse mit LAG
SELECT 
    datum,
    umsatz,
    LAG(umsatz, 1, 0) OVER (ORDER BY datum ASC) AS vortag_umsatz,
    umsatz - LAG(umsatz, 1, umsatz) OVER (ORDER BY datum ASC) AS delta_umsatz,
    ROUND(
        (umsatz - LAG(umsatz, 1, umsatz) OVER (ORDER BY datum ASC)) * 100.0 / 
        LAG(umsatz, 1, umsatz) OVER (ORDER BY datum ASC),
        2
    ) AS wachstum_prozent
FROM tages_umsatz
ORDER BY datum ASC;

-- 🎯 TODO 3: Running Total (Kumulierter Kunden-Umsatz)
SELECT 
    id,
    kunde_id,
    datum,
    betrag,
    SUM(betrag) OVER (
        PARTITION BY kunde_id 
        ORDER BY datum ASC, id ASC
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS laufender_umsatz
FROM transaktionen
ORDER BY kunde_id ASC, datum ASC;

-- 🎯 TODO 4: Gleitender 3-Tage Durchschnitt (Moving Average)
SELECT 
    datum,
    umsatz,
    ROUND(
        AVG(umsatz) OVER (
            ORDER BY datum ASC 
            ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
        ),
        2
    ) AS ma_3_tage
FROM tages_umsatz
ORDER BY datum ASC;
