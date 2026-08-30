-- ============================================================================
-- 🗄️ SQL 10: SUBQUERIES & MENGENOPERATIONEN (UNION / INTERSECT / EXCEPT) 🗄️
-- ============================================================================

-- ----------------------------------------------------------------------------
-- 1. TABELLEN-SCHEMA & TESTDATEN
-- ----------------------------------------------------------------------------
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

-- Testdaten
INSERT INTO kunden (id, name, email, level) VALUES
    (1, 'Max Mustermann', 'max@example.com', 'Gold'),
    (2, 'Sarah Connor', 'sarah@example.com', 'Silber'),
    (3, 'Tim Berg', 'tim@example.com', 'Bronze'),
    (4, 'Julia Sommer', 'julia@example.com', 'Gold'),
    (5, 'Felix Wolf', 'felix@example.com', 'Silber'),
    (6, 'Elena Roth', 'elena@example.com', 'Bronze');

INSERT INTO produkte (id, name, kategorie, preis) VALUES
    (1, 'Ultrabook Pro 15', 'Computer', 1299.00),
    (2, 'Wireless Mouse', 'Zubehör', 29.90),
    (3, 'Mechanical Keyboard', 'Zubehör', 119.00),
    (4, '4K Monitor 27 Zoll', 'Monitore', 389.00),
    (5, 'USB-C Hub', 'Zubehör', 45.00),
    (6, 'Ergonomischer Bürostuhl', 'Möbel', 299.00);

INSERT INTO online_bestellungen (id, kunde_id, betrag, bestell_datum) VALUES
    (101, 1, 1328.90, '2024-01-10'),
    (102, 2, 45.00, '2024-01-14'),
    (103, 3, 389.00, '2024-01-20'),
    (104, 4, 119.00, '2024-02-05'),
    (105, 5, 29.90, '2024-02-18');

INSERT INTO filial_einkaeufe (id, kunde_id, betrag, filial_stadt, kauf_datum) VALUES
    (201, 1, 299.00, 'Berlin', '2024-01-25'),
    (202, 3, 45.00, 'München', '2024-02-02'),
    (203, 6, 1299.00, 'Hamburg', '2024-02-20');

INSERT INTO retouren (id, kunde_id, grund) VALUES
    (1, 2, 'Defekt bei Ankunft'),
    (2, 5, 'Falscher Artikel');


-- ============================================================================
-- 🎯 AUFGABEN
-- ============================================================================

-- 🎯 TODO 1: Skalare Subquery & Preisabweichung
-- Finde alle Produkte (name, kategorie, preis), deren Preis ÜBER dem
-- Gesamtdurchschnitt aller Produkte liegt (preis > (SELECT AVG(preis) FROM produkte)).
-- Berechne in der 4. Spalte die Differenz zum Durchschnittspreis gerundet auf 2 Stellen:
-- ROUND(preis - (SELECT AVG(preis) FROM produkte), 2) AS preis_differenz.
-- Sortiere absteigend nach preis.
SELECT 
    name,
    kategorie,
    preis
    -- TODO: Spalte preis_differenz und WHERE Subquery ergänzen
FROM produkte;


-- 🎯 TODO 2: Korrelierte Subquery mit EXISTS und NOT EXISTS
-- Finde alle Kunden (id, name, email, level), die mindestens eine Online-Bestellung
-- getätigt haben (WHERE EXISTS ... online_bestellungen),
-- ABER bisher noch NIE eine Retoure eingereicht haben (AND NOT EXISTS ... retouren).
-- Sortiere nach kunden.id ASC.
SELECT 
    k.id,
    k.name,
    k.email,
    k.level
FROM kunden k
-- TODO: Korrelierte EXISTS / NOT EXISTS Subqueries ergänzen
ORDER BY k.id ASC;


-- 🎯 TODO 3: Multi-Channel Konsolidierung mit UNION ALL
-- Erstelle einen harmonisierten Umsatz-Feed aus beiden Kanälen (Online & Filiale).
-- Die Ergebnistabelle soll 4 Spalten haben:
-- - kanal (Entweder 'Online' oder 'Filiale')
-- - kunde_id
-- - betrag
-- - datum (aus bestell_datum bzw. kauf_datum)
-- Verwende UNION ALL zur Kombination. Sortiere nach datum ASC.
-- TODO: UNION ALL Abfrage schreiben


-- 🎯 TODO 4: Omnichannel vs. Pure-Online Analyse (INTERSECT & EXCEPT)
-- Teil 1 (Omnichannel-Käufer mit INTERSECT):
-- Finde die kunde_id aller Kunden, die sowohl online als auch in der Filiale gekauft haben.
-- TODO: INTERSECT Query

-- Teil 2 (Reine Online-Käufer mit EXCEPT):
-- Finde die kunde_id aller Kunden, die online bestellt haben, aber NIE in einer Filiale gekauft haben.
-- TODO: EXCEPT Query
