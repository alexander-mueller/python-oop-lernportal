-- ============================================================================
-- 🧪 TESTSUITE FÜR SQL 12: WINDOW FUNCTIONS 🧪
-- ============================================================================

-- Test 1: Ranking-Funktionen (TODO 1)
SELECT 
    'TEST 1 (Ranking Window Functions)' AS test_fall,
    kategorie_id,
    name,
    preis,
    ROW_NUMBER() OVER (PARTITION BY kategorie_id ORDER BY preis DESC, id ASC) AS rn,
    RANK() OVER (PARTITION BY kategorie_id ORDER BY preis DESC) AS rk,
    DENSE_RANK() OVER (PARTITION BY kategorie_id ORDER BY preis DESC) AS dr
FROM artikel
ORDER BY kategorie_id ASC, rn ASC;

-- Test 2: LAG Zeitreihenanalyse (TODO 2)
SELECT 
    'TEST 2 (LAG Offset Analysis)' AS test_fall,
    datum,
    umsatz,
    LAG(umsatz, 1, 0) OVER (ORDER BY datum) AS lag_val,
    umsatz - LAG(umsatz, 1, umsatz) OVER (ORDER BY datum) AS delta
FROM tages_umsatz
ORDER BY datum ASC;

-- Test 3: Running Total (TODO 3)
SELECT 
    'TEST 3 (Cumulative Running Total)' AS test_fall,
    kunde_id,
    datum,
    betrag,
    SUM(betrag) OVER (
        PARTITION BY kunde_id 
        ORDER BY datum ASC, id ASC
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_sum
FROM transaktionen
ORDER BY kunde_id ASC, datum ASC;

-- Test 4: Gleitender Durchschnitt (TODO 4)
SELECT 
    'TEST 4 (Moving Average 3-Days)' AS test_fall,
    datum,
    umsatz,
    ROUND(
        AVG(umsatz) OVER (
            ORDER BY datum ASC 
            ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
        ),
        2
    ) AS mov_avg
FROM tages_umsatz
ORDER BY datum ASC;
