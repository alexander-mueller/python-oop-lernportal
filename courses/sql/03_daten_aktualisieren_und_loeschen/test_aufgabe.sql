-- 🧪 SQL TEST SUITE: MODUL 03 (UPDATE, DELETE & ALTER TABLE)

-- Test 1: Prüfung nach UPDATE für ID 2
SELECT id, vorname, nachname, abteilung, status FROM mitarbeiter WHERE id = 2;

-- Test 2: Prüfung der Gehaltserhöhung in der IT
SELECT id, nachname, abteilung, round(gehalt, 2) AS gehalt FROM mitarbeiter WHERE abteilung = 'IT' ORDER BY id;

-- Test 3: Prüfung der neuen Spalte 'bonus'
SELECT id, nachname, round(gehalt, 2) AS gehalt, bonus FROM mitarbeiter WHERE bonus > 0 ORDER BY id;

-- Test 4: Prüfung, dass inaktiver Mitarbeiter mit Gehalt < 35000 gelöscht wurde
SELECT count(*) AS geloeschte_inaktive FROM mitarbeiter WHERE id = 4;

-- Test 5: Gesamtübersicht der verbleibenden Mitarbeiter
SELECT id, vorname, nachname, abteilung, round(gehalt, 2) AS gehalt, bonus, status FROM mitarbeiter ORDER BY id;
