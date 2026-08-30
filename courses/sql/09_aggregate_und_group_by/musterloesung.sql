-- ============================================================================
-- 💡 SQL 09: MUSTERLÖSUNG – AGGREGATIONEN & GROUP BY 💡
-- ============================================================================

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
INSERT OR REPLACE INTO kunden (id, name, stadt, status) VALUES
    (1, 'Alice Becker', 'Berlin', 'aktiv'),
    (2, 'Bob Meier', 'Hamburg', 'aktiv'),
    (3, 'Carla Wagner', 'München', 'aktiv'),
    (4, 'David Fischer', 'Berlin', 'inaktiv'),
    (5, 'Eva Klein', 'Hamburg', 'aktiv');

INSERT OR REPLACE INTO kategorien (id, name) VALUES
    (1, 'Elektronik'),
    (2, 'Bücher'),
    (3, 'Kleidung');

INSERT OR REPLACE INTO produkte (id, name, kategorie_id, preis) VALUES
    (101, 'Smartphone Pro', 1, 799.00),
    (102, 'Kopfhörer Wireless', 1, 149.00),
    (103, 'SQL Handbuch', 2, 49.90),
    (104, 'Python Kochbuch', 2, 39.90),
    (105, 'Outdoor Jacke', 3, 120.00),
    (106, 'Laufschuhe', 3, 89.00);

INSERT OR REPLACE INTO bestellungen (id, kunde_id, bestell_datum, status, gesamtbetrag) VALUES
    (1001, 1, '2024-01-15', 'abgeschlossen', 948.00),
    (1002, 2, '2024-01-20', 'abgeschlossen', 149.00),
    (1003, 1, '2024-02-10', 'abgeschlossen', 89.80),
    (1004, 3, '2024-02-15', 'abgeschlossen', 799.00),
    (1005, 4, '2024-03-01', 'storniert', 300.00),
    (1006, 2, '2024-03-12', 'abgeschlossen', 450.00),
    (1007, 5, '2024-03-25', 'abgeschlossen', 209.00);

INSERT OR REPLACE INTO bestellpositionen (id, bestell_id, produkt_id, menge, einzelpreis) VALUES
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

-- 🎯 TODO 1: Kategorie-Umsatz-Statistik
SELECT 
    k.name AS kategorie_name,
    SUM(bp.menge) AS anzahl_verkaeufe,
    SUM(bp.menge * bp.einzelpreis) AS gesamtumsatz,
    ROUND(AVG(bp.einzelpreis), 2) AS avg_preis,
    MIN(bp.einzelpreis) AS min_preis,
    MAX(bp.einzelpreis) AS max_preis
FROM kategorien k
JOIN produkte p ON k.id = p.kategorie_id
JOIN bestellpositionen bp ON p.id = bp.produkt_id
GROUP BY k.id, k.name
ORDER BY gesamtumsatz DESC;

-- 🎯 TODO 2: Top-Kunden mit HAVING
SELECT 
    k.name,
    k.stadt,
    COUNT(b.id) AS bestell_anzahl,
    SUM(b.gesamtbetrag) AS kunden_umsatz
FROM kunden k
JOIN bestellungen b ON k.id = b.kunde_id
WHERE b.status = 'abgeschlossen'
GROUP BY k.id, k.name, k.stadt
HAVING COUNT(b.id) >= 2 AND SUM(b.gesamtbetrag) >= 500.00
ORDER BY kunden_umsatz DESC;

-- 🎯 TODO 3: Monatlicher Umsatz- & KPI-Report
SELECT 
    strftime('%Y-%m', bestell_datum) AS monat,
    COUNT(id) AS anzahl_bestellungen,
    SUM(gesamtbetrag) AS monats_umsatz,
    ROUND(AVG(gesamtbetrag), 2) AS avg_warenkorb
FROM bestellungen
WHERE status = 'abgeschlossen'
GROUP BY strftime('%Y-%m', bestell_datum)
ORDER BY monat ASC;

-- 🎯 TODO 4: Multi-Column GROUP BY (Städte & Kategorien)
SELECT 
    k.stadt,
    kat.name AS kategorie_name,
    COUNT(DISTINCT b.id) AS eindeutige_bestellungen,
    SUM(bp.menge * bp.einzelpreis) AS umsatz_summe
FROM kunden k
JOIN bestellungen b ON k.id = b.kunde_id
JOIN bestellpositionen bp ON b.id = bp.bestell_id
JOIN produkte p ON bp.produkt_id = p.id
JOIN kategorien kat ON p.kategorie_id = kat.id
WHERE b.status = 'abgeschlossen'
GROUP BY k.stadt, kat.name
HAVING SUM(bp.menge * bp.einzelpreis) > 300
ORDER BY k.stadt ASC, umsatz_summe DESC;
