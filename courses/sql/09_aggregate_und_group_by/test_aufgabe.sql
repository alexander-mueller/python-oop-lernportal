-- ============================================================================
-- 🧪 TESTSUITE FÜR SQL 09: AGGREGATIONEN & GROUP BY 🧪
-- ============================================================================

-- Test 1: Verifikation der Kategorie-Aggregationen (TODO 1)
SELECT 
    'TEST 1 (Kategorien)' AS test_fall,
    k.name AS kategorie,
    SUM(bp.menge) AS summe_stueck,
    SUM(bp.menge * bp.einzelpreis) AS summe_euro
FROM kategorien k
JOIN produkte p ON k.id = p.kategorie_id
JOIN bestellpositionen bp ON p.id = bp.produkt_id
GROUP BY k.id, k.name
ORDER BY summe_euro DESC;

-- Test 2: Verifikation der Top-Kunden mit HAVING (TODO 2)
SELECT 
    'TEST 2 (Top-Kunden)' AS test_fall,
    k.name,
    COUNT(b.id) AS anzahl_orders,
    SUM(b.gesamtbetrag) AS gesamt_wert
FROM kunden k
JOIN bestellungen b ON k.id = b.kunde_id
WHERE b.status = 'abgeschlossen'
GROUP BY k.id, k.name, k.stadt
HAVING COUNT(b.id) >= 2 AND SUM(b.gesamtbetrag) >= 500.00;

-- Test 3: Verifikation Monatsreport (TODO 3)
SELECT 
    'TEST 3 (Monats-KPIs)' AS test_fall,
    strftime('%Y-%m', bestell_datum) AS monat,
    COUNT(id) AS bestellungen,
    SUM(gesamtbetrag) AS umsatz
FROM bestellungen
WHERE status = 'abgeschlossen'
GROUP BY strftime('%Y-%m', bestell_datum)
ORDER BY monat ASC;

-- Test 4: Verifikation Multi-Column GROUP BY mit HAVING (TODO 4)
SELECT 
    'TEST 4 (Stadt & Kategorie)' AS test_fall,
    k.stadt,
    kat.name AS kategorie,
    COUNT(DISTINCT b.id) AS bestellungen_count,
    SUM(bp.menge * bp.einzelpreis) AS summe_betrag
FROM kunden k
JOIN bestellungen b ON k.id = b.kunde_id
JOIN bestellpositionen bp ON b.id = bp.bestell_id
JOIN produkte p ON bp.produkt_id = p.id
JOIN kategorien kat ON p.kategorie_id = kat.id
WHERE b.status = 'abgeschlossen'
GROUP BY k.stadt, kat.name
HAVING SUM(bp.menge * bp.einzelpreis) > 300
ORDER BY k.stadt ASC, summe_betrag DESC;
