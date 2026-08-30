-- ============================================================================
-- 🗄️ SQL 09: AGGREGATIONEN (COUNT/SUM/AVG) & GROUP BY / HAVING 🗄️
-- ============================================================================
-- In diesem Modul analysierst du Verkaufs- und Kundendaten mit Aggregatfunktionen,
-- mehrdimensionalen GROUP BY Gruppierungen und HAVING-Filtern.

-- ----------------------------------------------------------------------------
-- 1. TABELLEN-SCHEMA & TESTDATEN
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS kunden (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    stadt TEXT NOT NULL,
    status TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS kategorien (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS produkte (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    kategorie_id INTEGER NOT NULL,
    preis REAL NOT NULL,
    FOREIGN KEY (kategorie_id) REFERENCES kategorien(id)
);

CREATE TABLE IF NOT EXISTS bestellungen (
    id INTEGER PRIMARY KEY,
    kunde_id INTEGER NOT NULL,
    bestell_datum TEXT NOT NULL,
    status TEXT NOT NULL,
    gesamtbetrag REAL NOT NULL,
    FOREIGN KEY (kunde_id) REFERENCES kunden(id)
);

CREATE TABLE IF NOT EXISTS bestellpositionen (
    id INTEGER PRIMARY KEY,
    bestell_id INTEGER NOT NULL,
    produkt_id INTEGER NOT NULL,
    menge INTEGER NOT NULL,
    einzelpreis REAL NOT NULL,
    FOREIGN KEY (bestell_id) REFERENCES bestellungen(id),
    FOREIGN KEY (produkt_id) REFERENCES produkte(id)
);

-- Testdaten einfügen
INSERT INTO kunden (id, name, stadt, status) VALUES
    (1, 'Alice Becker', 'Berlin', 'aktiv'),
    (2, 'Bob Meier', 'Hamburg', 'aktiv'),
    (3, 'Carla Wagner', 'München', 'aktiv'),
    (4, 'David Fischer', 'Berlin', 'inaktiv'),
    (5, 'Eva Klein', 'Hamburg', 'aktiv');

INSERT INTO kategorien (id, name) VALUES
    (1, 'Elektronik'),
    (2, 'Bücher'),
    (3, 'Kleidung');

INSERT INTO produkte (id, name, kategorie_id, preis) VALUES
    (101, 'Smartphone Pro', 1, 799.00),
    (102, 'Kopfhörer Wireless', 1, 149.00),
    (103, 'SQL Handbuch', 2, 49.90),
    (104, 'Python Kochbuch', 2, 39.90),
    (105, 'Outdoor Jacke', 3, 120.00),
    (106, 'Laufschuhe', 3, 89.00);

INSERT INTO bestellungen (id, kunde_id, bestell_datum, status, gesamtbetrag) VALUES
    (1001, 1, '2024-01-15', 'abgeschlossen', 948.00),
    (1002, 2, '2024-01-20', 'abgeschlossen', 149.00),
    (1003, 1, '2024-02-10', 'abgeschlossen', 89.80),
    (1004, 3, '2024-02-15', 'abgeschlossen', 799.00),
    (1005, 4, '2024-03-01', 'storniert', 300.00),
    (1006, 2, '2024-03-12', 'abgeschlossen', 450.00),
    (1007, 5, '2024-03-25', 'abgeschlossen', 209.00);

INSERT INTO bestellpositionen (id, bestell_id, produkt_id, menge, einzelpreis) VALUES
    (1, 1001, 101, 1, 799.00),
    (2, 1001, 102, 1, 149.00),
    (3, 1002, 102, 1, 149.00),
    (4, 1003, 103, 1, 49.90),
    (5, 1003, 104, 1, 39.90),
    (6, 1004, 101, 1, 799.00),
    (7, 1006, 105, 3, 120.00),
    (8, 1006, 106, 1, 89.00),
    (9, 1007, 105, 1, 120.00),
    (10, 1007, 106, 1, 89.00);


-- ============================================================================
-- 🎯 AUFGABEN
-- ============================================================================

-- 🎯 TODO 1: Kategorie-Umsatz-Statistik
-- Aggregiere die verkauften Artikel nach Kategorie (kategorien.name).
-- Berechne:
-- - anzahl_verkaeufe: Summe aller verkauften Mengen (SUM(bp.menge))
-- - gesamtumsatz: Summe aus menge * einzelpreis
-- - avg_preis: Runder Durchschnittspreis der verkauften Artikel (ROUND(AVG(bp.einzelpreis), 2))
-- - min_preis: Minimaler Einzelpreis (MIN(bp.einzelpreis))
-- - max_preis: Maximaler Einzelpreis (MAX(bp.einzelpreis))
-- Sortiere absteigend nach gesamtumsatz.
SELECT 
    k.name AS kategorie_name
    -- TODO: Aggregatfunktionen ergänzen
FROM kategorien k
JOIN produkte p ON k.id = p.kategorie_id
JOIN bestellpositionen bp ON p.id = bp.produkt_id
GROUP BY k.id, k.name;


-- 🎯 TODO 2: Top-Kunden mit HAVING
-- Finde alle aktiven Kunden (kunden.name, kunden.stadt), die mindestens 2
-- abgeschlossene Bestellungen (status = 'abgeschlossen') getätigt haben
-- UND deren Gesamtbestellwert über alle Bestellungen >= 500.00 Euro liegt.
-- Sortiere absteigend nach kunden_umsatz.
SELECT 
    k.name,
    k.stadt,
    COUNT(b.id) AS bestell_anzahl,
    SUM(b.gesamtbetrag) AS kunden_umsatz
FROM kunden k
JOIN bestellungen b ON k.id = b.kunde_id
WHERE b.status = 'abgeschlossen'
-- TODO: GROUP BY & HAVING hinzufügen
ORDER BY kunden_umsatz DESC;


-- 🎯 TODO 3: Monatlicher Umsatz- & KPI-Report
-- Erstelle einen monatlichen Report für alle abgeschlossenen Bestellungen.
-- Extrahiere den Monat mit strftime('%Y-%m', bestell_datum) AS monat.
-- Berechne:
-- - anzahl_bestellungen: COUNT(id)
-- - monats_umsatz: SUM(gesamtbetrag)
-- - avg_warenkorb: ROUND(AVG(gesamtbetrag), 2)
-- Sortiere chronologisch aufsteigend nach monat.
SELECT 
    strftime('%Y-%m', bestell_datum) AS monat
    -- TODO: Aggregatfunktionen und GROUP BY ergänzen
FROM bestellungen
WHERE status = 'abgeschlossen';


-- 🎯 TODO 4: Multi-Column GROUP BY (Städte & Kategorien)
-- Ermittle für jede Kombination aus Stadt (kunden.stadt) und Kategorie (kategorien.name):
-- - eindeutige_bestellungen: COUNT(DISTINCT b.id)
-- - umsatz_summe: SUM(bp.menge * bp.einzelpreis)
-- Filtere nur Gruppen mit HAVING SUM(bp.menge * bp.einzelpreis) > 300.
-- Sortiere nach kunden.stadt ASC, umsatz_summe DESC.
SELECT 
    k.stadt,
    kat.name AS kategorie_name
    -- TODO: Aggregate und Bedingungen ergänzen
FROM kunden k
JOIN bestellungen b ON k.id = b.kunde_id
JOIN bestellpositionen bp ON b.id = bp.bestell_id
JOIN produkte p ON bp.produkt_id = p.id
JOIN kategorien kat ON p.kategorie_id = kat.id
WHERE b.status = 'abgeschlossen'
GROUP BY k.stadt, kat.name;
