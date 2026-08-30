-- 🧪 SQL TEST SUITE: MODUL 06 (INNER & OUTER JOINS)

-- Test 1: INNER JOIN Prüfung (Erwartet 4 feste Mitarbeiter)
SELECT 
    m.name AS mitarbeiter_name, 
    m.rolle, 
    a.name AS abteilung_name
FROM mitarbeiter m
INNER JOIN abteilungen a ON m.abteilung_id = a.id
ORDER BY m.id;

-- Test 2: LEFT JOIN Prüfung (Erwartet 5 Zeilen inkl. Dr. Aris Thorne)
SELECT 
    m.name AS mitarbeiter_name, 
    COALESCE(a.name, 'Keine Abteilung') AS abteilung_name
FROM mitarbeiter m
LEFT JOIN abteilungen a ON m.abteilung_id = a.id
ORDER BY m.id;

-- Test 3: Anti-Join Prüfung (Erwartet genau Abteilung 'Forschung & KI')
SELECT 
    a.id AS abteilung_id, 
    a.name AS abteilung_name
FROM abteilungen a
LEFT JOIN mitarbeiter m ON a.id = m.abteilung_id
WHERE m.id IS NULL
ORDER BY a.id;

-- Test 4: Multi-Table JOIN Prüfung über 3 Tabellen
SELECT 
    m.name AS mitarbeiter, 
    a.name AS abteilung, 
    s.stadt, 
    s.land
FROM mitarbeiter m
INNER JOIN abteilungen a ON m.abteilung_id = a.id
INNER JOIN standorte s ON a.standort_id = s.id
ORDER BY m.id;
