-- 🧪 SQL TEST SUITE: MODUL 08 (n:m Beziehungen & Junction Tables)

-- Test 1: Tabellenprüfung
SELECT count(*) AS total_studenten FROM studenten;
SELECT count(*) AS total_kurse FROM kurse;

-- Test 2: Vollständiger n:m 3-Wege-Join
SELECT 
    s.matrikelnummer,
    (s.vorname || ' ' || s.nachname) AS student_name,
    k.kurs_code,
    k.titel AS kurs_titel,
    e.semester,
    e.note,
    e.status
FROM studenten s
JOIN einschreibungen e ON s.id = e.student_id
JOIN kurse k ON e.kurs_id = k.id
ORDER BY s.nachname, k.kurs_code;

-- Test 3: Bestehensprüfung für Kurs DB101 mit Note <= 2.0 (Erwartet Felix & Hannah)
SELECT 
    s.vorname, s.nachname, e.note 
FROM studenten s
JOIN einschreibungen e ON s.id = e.student_id
JOIN kurse k ON e.kurs_id = k.id
WHERE k.kurs_code = 'DB101' AND e.note <= 2.0
ORDER BY e.note ASC;

-- Test 4: Kaskadierendes Löschen verifizieren:
-- Durch das Löschen von WEB201 dürfen keine verwaisten Einträge in einschreibungen verbleiben!
SELECT count(*) AS verwaiste_eintraege 
FROM einschreibungen 
WHERE kurs_id NOT IN (SELECT id FROM kurse);

-- Test 5: Verbleibende Gesamteinschreibungen (nach Löschen von WEB201: 7 - 2 = 5)
SELECT count(*) AS verbleibende_einschreibungen FROM einschreibungen;
