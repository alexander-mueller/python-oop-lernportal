-- 🧪 SQL TEST SUITE: MODUL 05 (Foreign Keys & Relationen)

-- Test 1: Fremdschlüssel-Aktivierung prüfen
PRAGMA foreign_keys;

-- Test 2: Verbleibende Kunden (Kunde 1 gelöscht -> verbleiben Bob & Carolin)
SELECT id, name, email FROM kunden ORDER BY id;

-- Test 3: Verbleibende Profile (Profil 1 muss durch CASCADE mitgelöscht worden sein!)
SELECT id, kunde_id, lieferadresse FROM kunden_profile ORDER BY id;

-- Test 4: Verbleibende Bestellungen (Bestellungen von Kunde 1 müssen durch CASCADE gelöscht sein!)
SELECT id, kunde_id, gesamtbetrag, status FROM bestellungen ORDER BY id;

-- Test 5: Konsistenzcheck: Es dürfen KEINE verwaisten Fremdschlüssel existieren
SELECT count(*) AS verwaiste_bestellungen 
FROM bestellungen b 
LEFT JOIN kunden k ON b.kunde_id = k.id 
WHERE k.id IS NULL;
