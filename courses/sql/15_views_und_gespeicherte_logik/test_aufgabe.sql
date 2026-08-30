-- ============================================================================
-- 🧪 TESTSUITE FÜR SQL 15: VIEWS & TRIGGER 🧪
-- ============================================================================

-- Test 1: Überprüfe View v_kunden_bestell_cockpit (TODO 1)
SELECT 
    'TEST 1 (View Kunden Cockpit)' AS test_fall,
    kunde_id,
    name,
    email,
    anzahl_bestellungen,
    gesamt_umsatz
FROM v_kunden_bestell_cockpit
ORDER BY gesamt_umsatz DESC;

-- Test 2: Überprüfe View v_top_seller_uebersicht (TODO 2)
SELECT 
    'TEST 2 (View Top Seller)' AS test_fall,
    produkt_id,
    produkt_name,
    verkaufte_menge,
    gesamt_erloes
FROM v_top_seller_uebersicht
ORDER BY gesamt_erloes DESC;

-- Test 3: Trigger-Test: Lagerbestand automatisch reduzieren bei INSERT (TODO 3)
-- Vorab-Bestand von Produkt 102 war 100.
INSERT INTO bestellungen (id, kunde_id, bestell_datum, gesamtbetrag) VALUES (99, 3, '2024-03-20', 298.00);
INSERT INTO bestellpositionen (bestell_id, produkt_id, menge, einzelpreis) VALUES (99, 102, 5, 149.00);

SELECT 
    'TEST 3 (Trigger Lagerbestand Update)' AS test_fall,
    id,
    name,
    lagerbestand AS restbestand_nach_kauf
FROM produkte
WHERE id = 102;

-- Test 4: Trigger-Test: Revisionssicheres Preis-Audit bei UPDATE (TODO 4)
-- Preis von Produkt 103 von 249.00 auf 229.00 senken
UPDATE produkte SET preis = 229.00 WHERE id = 103;

SELECT 
    'TEST 4 (Trigger Preis-Audit)' AS test_fall,
    produkt_id,
    alter_preis,
    neuer_preis,
    aenderungs_datum
FROM audit_preis_historie
WHERE produkt_id = 103;
