-- ============================================================================
-- 🧪 TESTSUITE FÜR SQL 13: INDIZES & QUERY-OPTIMIERUNG 🧪
-- ============================================================================

-- Test 1: Überprüfe, ob alle geforderten Indizes im sqlite_master existieren
SELECT 
    'TEST 1 (Index Existenz)' AS test_fall,
    name AS index_name,
    tbl_name AS tabelle,
    sql
FROM sqlite_master 
WHERE type = 'index' AND name IN (
    'idx_kunden_email_unique',
    'idx_artikel_kat_preis',
    'idx_aktive_kunden_stadt',
    'idx_server_logs_zeitstempel'
)
ORDER BY name ASC;

-- Test 2: SARGable Log-Query Ausführung (TODO 3)
SELECT 
    'TEST 2 (SARGable Logs)' AS test_fall,
    COUNT(*) AS treffer_count,
    MIN(zeitstempel) AS erstes_log,
    MAX(zeitstempel) AS letztes_log
FROM server_logs
WHERE zeitstempel >= '2024-01-01 00:00:00' AND zeitstempel < '2025-01-01 00:00:00';

-- Test 3: EXPLAIN QUERY PLAN Verifikation (TODO 4)
EXPLAIN QUERY PLAN SELECT * FROM kunden WHERE email = 'sarah@example.com';
EXPLAIN QUERY PLAN SELECT * FROM artikel WHERE kategorie_id = 1 AND preis > 500;
