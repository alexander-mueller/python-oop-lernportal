-- ============================================================================
-- 🧪 TESTSUITE FÜR SQL 10: SUBQUERIES & MENGENOPERATIONEN 🧪
-- ============================================================================

-- Test 1: Überdurchschnittliche Produkte (TODO 1)
SELECT 
    'TEST 1 (Skalare Subquery)' AS test_fall,
    name,
    preis,
    ROUND(preis - (SELECT AVG(preis) FROM produkte), 2) AS diff
FROM produkte
WHERE preis > (SELECT AVG(preis) FROM produkte)
ORDER BY preis DESC;

-- Test 2: Kunden mit Online-Kauf und ohne Retoure (TODO 2)
SELECT 
    'TEST 2 (EXISTS / NOT EXISTS)' AS test_fall,
    k.id,
    k.name
FROM kunden k
WHERE EXISTS (SELECT 1 FROM online_bestellungen WHERE kunde_id = k.id)
AND NOT EXISTS (SELECT 1 FROM retouren WHERE kunde_id = k.id)
ORDER BY k.id ASC;

-- Test 3: Gesamttransaktionen per UNION ALL (TODO 3)
SELECT 
    'TEST 3 (UNION ALL Zählung)' AS test_fall,
    COUNT(*) AS total_transaktionen,
    SUM(betrag) AS gesamt_umsatz
FROM (
    SELECT 'Online' AS kanal, betrag FROM online_bestellungen
    UNION ALL
    SELECT 'Filiale' AS kanal, betrag FROM filial_einkaeufe
);

-- Test 4a: Omnichannel Kunden (TODO 4a)
SELECT 
    'TEST 4a (INTERSECT Omnichannel)' AS test_fall,
    kunde_id
FROM (
    SELECT kunde_id FROM online_bestellungen
    INTERSECT
    SELECT kunde_id FROM filial_einkaeufe
)
ORDER BY kunde_id ASC;

-- Test 4b: Reine Online-Käufer (TODO 4b)
SELECT 
    'TEST 4b (EXCEPT Pure Online)' AS test_fall,
    kunde_id
FROM (
    SELECT kunde_id FROM online_bestellungen
    EXCEPT
    SELECT kunde_id FROM filial_einkaeufe
)
ORDER BY kunde_id ASC;
