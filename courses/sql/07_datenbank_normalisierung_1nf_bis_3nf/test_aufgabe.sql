-- 🧪 SQL TEST SUITE: MODUL 07 (Datenbank-Normalisierung 1NF–3NF)

-- Test 1: Überprüfung aller 5 Tabellen im 3NF-Schema
SELECT name FROM sqlite_master WHERE type='table' AND name IN ('orte', 'kunden', 'artikel', 'auftraege', 'auftragspositionen') ORDER BY name;

-- Test 2: Prüfung der ausgelagerten Orte (3NF)
SELECT plz, stadt FROM orte ORDER BY plz;

-- Test 3: Prüfung der Kunden mit PLZ-Verknüpfung
SELECT k.id, k.name, o.stadt FROM kunden k JOIN orte o ON k.plz = o.plz ORDER BY k.id;

-- Test 4: Positionsbericht mit berechnetem Gesamtbetrag
SELECT 
    a.id AS auftrag_id,
    k.name AS kunden_name,
    art.bezeichnung AS artikel,
    pos.menge,
    round(pos.menge * art.einzelpreis, 2) AS positions_gesamt
FROM auftraege a
JOIN kunden k ON a.kunde_id = k.id
JOIN auftragspositionen pos ON a.id = pos.auftrag_id
JOIN artikel art ON pos.artikel_id = art.id
ORDER BY a.id, art.id;

-- Test 5: Gesamtumsatz pro Auftrag
SELECT 
    a.id AS auftrag_id,
    k.name AS kunden_name,
    round(sum(pos.menge * art.einzelpreis), 2) AS auftrags_summe
FROM auftraege a
JOIN kunden k ON a.kunde_id = k.id
JOIN auftragspositionen pos ON a.id = pos.auftrag_id
JOIN artikel art ON pos.artikel_id = art.id
GROUP BY a.id, k.name
ORDER BY a.id;
