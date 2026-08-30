-- ============================================================================
-- 🧪 TESTSUITE FÜR SQL 14: ACID TRANSAKTIONEN & SAVEPOINTS 🧪
-- ============================================================================

-- Test 1: Überprüfe Kontostände nach erfolgreicher Überweisung (Konto 1: 700€, Konto 2: 2800€, Konto 3: 500€)
SELECT 
    'TEST 1 (Kontostaende)' AS test_fall,
    konto_id,
    inhaber,
    kontostand
FROM konten
ORDER BY konto_id ASC;

-- Test 2: Bilanzsummenprüfung (Gesamt muss exakt 4000.00 sein)
SELECT 
    'TEST 2 (Bilanzgleichgewicht)' AS test_fall,
    SUM(kontostand) AS aktuelle_bilanzsumme,
    CASE WHEN SUM(kontostand) = 4000.00 THEN 'OK (Integrität gewahrt)' ELSE 'FEHLER (Differenz)' END AS audit_status
FROM konten;

-- Test 3: Log-Eintrag Prüfung (TODO 1)
SELECT 
    'TEST 3 (Transaktionslog)' AS test_fall,
    von_konto,
    an_konto,
    betrag,
    status
FROM transaktions_log
WHERE status = 'ERFOLGREICH';

-- Test 4: Savepoint-Prüfung (Es darf nur die gültige Reservierung mit menge=2 existieren, nicht menge=100)
SELECT 
    'TEST 4 (Savepoint Isolation)' AS test_fall,
    kunde_id,
    artikel_id,
    menge,
    status
FROM warenkorb_reservierung;
