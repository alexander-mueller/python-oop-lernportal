-- ============================================================================
-- 💡 SQL 10: MUSTERLÖSUNG – SUBQUERIES & MENGENOPERATIONEN 💡
-- ============================================================================

CREATE TABLE IF NOT EXISTS kunden (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    level TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS produkte (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    kategorie TEXT NOT NULL,
    preis REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS online_bestellungen (
    id INTEGER PRIMARY KEY,
    kunde_id INTEGER NOT NULL,
    betrag REAL NOT NULL,
    bestell_datum TEXT NOT NULL,
    FOREIGN KEY (kunde_id) REFERENCES kunden(id)
);

CREATE TABLE IF NOT EXISTS filial_einkaeufe (
    id INTEGER PRIMARY KEY,
    kunde_id INTEGER NOT NULL,
    betrag REAL NOT NULL,
    filial_stadt TEXT NOT NULL,
    kauf_datum TEXT NOT NULL,
    FOREIGN KEY (kunde_id) REFERENCES kunden(id)
);

CREATE TABLE IF NOT EXISTS retouren (
    id INTEGER PRIMARY KEY,
    kunde_id INTEGER NOT NULL,
    grund TEXT NOT NULL,
    FOREIGN KEY (kunde_id) REFERENCES kunden(id)
);

INSERT OR REPLACE INTO kunden (id, name, email, level) VALUES
    (1, 'Max Mustermann', 'max@example.com', 'Gold'),
    (2, 'Sarah Connor', 'sarah@example.com', 'Silber'),
    (3, 'Tim Berg', 'tim@example.com', 'Bronze'),
    (4, 'Julia Sommer', 'julia@example.com', 'Gold'),
    (5, 'Felix Wolf', 'felix@example.com', 'Silber'),
    (6, 'Elena Roth', 'elena@example.com', 'Bronze');

INSERT OR REPLACE INTO produkte (id, name, kategorie, preis) VALUES
    (1, 'Ultrabook Pro 15', 'Computer', 1299.00),
    (2, 'Wireless Mouse', 'Zubehör', 29.90),
    (3, 'Mechanical Keyboard', 'Zubehör', 119.00),
    (4, '4K Monitor 27 Zoll', 'Monitore', 389.00),
    (5, 'USB-C Hub', 'Zubehör', 45.00),
    (6, 'Ergonomischer Bürostuhl', 'Möbel', 299.00);

INSERT OR REPLACE INTO online_bestellungen (id, kunde_id, betrag, bestell_datum) VALUES
    (101, 1, 1328.90, '2024-01-10'),
    (102, 2, 45.00, '2024-01-14'),
    (103, 3, 389.00, '2024-01-20'),
    (104, 4, 119.00, '2024-02-05'),
    (105, 5, 29.90, '2024-02-18');

INSERT OR REPLACE INTO filial_einkaeufe (id, kunde_id, betrag, filial_stadt, kauf_datum) VALUES
    (201, 1, 299.00, 'Berlin', '2024-01-25'),
    (202, 3, 45.00, 'München', '2024-02-02'),
    (203, 6, 1299.00, 'Hamburg', '2024-02-20');

INSERT OR REPLACE INTO retouren (id, kunde_id, grund) VALUES
    (1, 2, 'Defekt bei Ankunft'),
    (2, 5, 'Falscher Artikel');

-- 🎯 TODO 1: Skalare Subquery & Preisabweichung
SELECT 
    name,
    kategorie,
    preis,
    ROUND(preis - (SELECT AVG(preis) FROM produkte), 2) AS preis_differenz
FROM produkte
WHERE preis > (SELECT AVG(preis) FROM produkte)
ORDER BY preis DESC;

-- 🎯 TODO 2: Korrelierte Subquery mit EXISTS und NOT EXISTS
SELECT 
    k.id,
    k.name,
    k.email,
    k.level
FROM kunden k
WHERE EXISTS (
    SELECT 1 FROM online_bestellungen ob 
    WHERE ob.kunde_id = k.id
)
AND NOT EXISTS (
    SELECT 1 FROM retouren r 
    WHERE r.kunde_id = k.id
)
ORDER BY k.id ASC;

-- 🎯 TODO 3: Multi-Channel Konsolidierung mit UNION ALL
SELECT 
    'Online' AS kanal,
    kunde_id,
    betrag,
    bestell_datum AS datum
FROM online_bestellungen
UNION ALL
SELECT 
    'Filiale' AS kanal,
    kunde_id,
    betrag,
    kauf_datum AS datum
FROM filial_einkaeufe
ORDER BY datum ASC;

-- 🎯 TODO 4 (Teil 1): Omnichannel-Käufer (INTERSECT)
SELECT kunde_id FROM online_bestellungen
INTERSECT
SELECT kunde_id FROM filial_einkaeufe
ORDER BY kunde_id ASC;

-- 🎯 TODO 4 (Teil 2): Reine Online-Käufer (EXCEPT)
SELECT kunde_id FROM online_bestellungen
EXCEPT
SELECT kunde_id FROM filial_einkaeufe
ORDER BY kunde_id ASC;
