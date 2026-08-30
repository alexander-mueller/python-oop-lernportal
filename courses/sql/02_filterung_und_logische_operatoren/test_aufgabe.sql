-- 🧪 SQL TEST SUITE: MODUL 02 (Filterung & Logische Operatoren)

-- Test 1: Tabellenexistenz & Datenbestand
SELECT count(*) AS total_artikel FROM shop_artikel;

-- Test 2: Filter Elektronik & Preis > 100
SELECT id, titel, preis FROM shop_artikel WHERE kategorie = 'Elektronik' AND preis > 100.0 ORDER BY preis ASC;

-- Test 3: BETWEEN & IN
SELECT id, titel, kategorie, preis FROM shop_artikel WHERE preis BETWEEN 20.0 AND 150.0 AND kategorie IN ('Zubehör', 'Audio') ORDER BY id;

-- Test 4: Textmustersuche mit LIKE
SELECT id, titel FROM shop_artikel WHERE titel LIKE 'Smart%' OR titel LIKE '%Pro%' ORDER BY id;

-- Test 5: NULL-Werte Prüfung
SELECT id, titel, rabatt_code FROM shop_artikel WHERE rabatt_code IS NULL AND lagerbestand > 0 ORDER BY id;

-- Test 6: NOT Elektronik & Top 3
SELECT id, titel, kategorie, preis FROM shop_artikel WHERE ist_verfuegbar = 1 AND kategorie != 'Elektronik' ORDER BY preis DESC LIMIT 3;
