-- ============================================================================
-- 🧪 TESTSUITE FÜR SQL 11: COMMON TABLE EXPRESSIONS (CTE) 🧪
-- ============================================================================

-- Test 1: Kunden-Segmentierung mit CTE (TODO 1)
WITH kunden_stats AS (
    SELECT kunde_id, COUNT(id) AS bestell_anzahl, SUM(gesamtbetrag) AS gesamt_umsatz
    FROM bestellungen WHERE status = 'abgeschlossen' GROUP BY kunde_id
)
SELECT 
    'TEST 1 (Kunden Segment CTE)' AS test_fall,
    k.name,
    COALESCE(ks.gesamt_umsatz, 0.0) AS umsatz,
    CASE 
        WHEN COALESCE(ks.gesamt_umsatz, 0) >= 2000 THEN 'VIP'
        WHEN COALESCE(ks.gesamt_umsatz, 0) >= 500 THEN 'Regulär'
        ELSE 'Basis'
    END AS segment
FROM kunden k
LEFT JOIN kunden_stats ks ON k.id = ks.kunde_id
ORDER BY umsatz DESC;

-- Test 2: Chained CTEs (TODO 2)
WITH monats_gewinn AS (
    SELECT monat, umsatz, kosten, (umsatz - kosten) AS gewinn FROM monats_umsatz_raw
),
benchmark AS (
    SELECT AVG(gewinn) AS avg_gewinn FROM monats_gewinn
)
SELECT 
    'TEST 2 (Chained CTEs)' AS test_fall,
    mg.monat,
    mg.gewinn,
    (mg.gewinn - b.avg_gewinn) AS diff
FROM monats_gewinn mg, benchmark b
WHERE mg.gewinn >= b.avg_gewinn
ORDER BY mg.monat ASC;

-- Test 3: Rekursiver Kalender (TODO 3)
WITH RECURSIVE kalender(datum) AS (
    SELECT '2024-03-01'
    UNION ALL
    SELECT DATE(datum, '+1 day') FROM kalender WHERE datum < '2024-03-07'
)
SELECT 'TEST 3 (Rekursiver Kalender)' AS test_fall, COUNT(*) AS anzahl_tage, MIN(datum) AS start_tag, MAX(datum) AS end_tag 
FROM kalender;

-- Test 4: Rekursives Organigramm (TODO 4)
WITH RECURSIVE organigramm AS (
    SELECT id, name, position, vorgesetzter_id, 1 AS ebene, name AS pfad
    FROM mitarbeiter WHERE vorgesetzter_id IS NULL
    UNION ALL
    SELECT m.id, m.name, m.position, m.vorgesetzter_id, o.ebene + 1, o.pfad || ' -> ' || m.name
    FROM mitarbeiter m JOIN organigramm o ON m.vorgesetzter_id = o.id
)
SELECT 
    'TEST 4 (Hierarchie Organigramm)' AS test_fall,
    id, name, ebene, pfad
FROM organigramm
ORDER BY pfad ASC;
