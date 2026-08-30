-- 🧪 SQL TEST SUITE: MODUL 04 (Datentypen & Constraints)

-- Test 1: Tabellenprüfung in der SQLite Schema-Tabelle
SELECT name FROM sqlite_master WHERE type='table' AND name IN ('bank_kunden', 'bank_konten') ORDER BY name;

-- Test 2: Alle Kunden mit Constraints prüfen
SELECT id, kunden_nr, name, kunden_alter, bonitaets_score, status FROM bank_kunden ORDER BY id;

-- Test 3: Alle Bankkonten prüfen
SELECT iban, kunden_id, kontotyp, saldo, waehrung FROM bank_konten ORDER BY iban;

-- Test 4: Verifizierte Kunden mit Bonitäts-Score >= 600
SELECT id, name, bonitaets_score FROM bank_kunden WHERE status = 'verifiziert' AND bonitaets_score >= 600 ORDER BY bonitaets_score DESC;

-- Test 5: Dispo-Konten
SELECT iban, kunden_id, saldo FROM bank_konten WHERE saldo < 0.0;
