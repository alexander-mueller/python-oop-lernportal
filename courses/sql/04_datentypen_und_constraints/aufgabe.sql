-- 🗄️ SQL 04: DATENTYPEN & CONSTRAINTS (CHECK & UNIQUE) 🗄️
-- ========================================================

-- 🎯 TEILZIEL 1 (TODO 1): Erstelle die Tabelle `bank_kunden` mit:
--    id (INTEGER PRIMARY KEY AUTOINCREMENT),
--    kunden_nr (TEXT NOT NULL UNIQUE),
--    name (TEXT NOT NULL),
--    email (TEXT NOT NULL UNIQUE),
--    kunden_alter (INTEGER NOT NULL mit CHECK kunden_alter >= 18),
--    bonitaets_score (INTEGER NOT NULL DEFAULT 500 mit CHECK bonitaets_score BETWEEN 100 AND 1000),
--    status (TEXT NOT NULL DEFAULT 'aktiv' mit CHECK status IN ('aktiv', 'verifiziert', 'gesperrt'))
CREATE TABLE IF NOT EXISTS bank_kunden (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    kunden_nr TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    kunden_alter INTEGER NOT NULL CHECK (kunden_alter >= 18),
    bonitaets_score INTEGER NOT NULL DEFAULT 500 CHECK (bonitaets_score BETWEEN 100 AND 1000),
    status TEXT NOT NULL DEFAULT 'aktiv' CHECK (status IN ('aktiv', 'verifiziert', 'gesperrt'))
);


-- 🎯 TEILZIEL 2 (TODO 2): Erstelle die Tabelle `bank_konten` mit:
--    iban (TEXT PRIMARY KEY),
--    kunden_id (INTEGER NOT NULL),
--    kontotyp (TEXT NOT NULL mit CHECK kontotyp IN ('Girokonto', 'Sparkonto', 'Tagesgeld')),
--    saldo REAL NOT NULL DEFAULT 0.0 mit CHECK saldo >= -500.0,
--    waehrung (TEXT NOT NULL DEFAULT 'EUR' mit CHECK waehrung IN ('EUR', 'USD', 'CHF'))
CREATE TABLE IF NOT EXISTS bank_konten (
    iban TEXT PRIMARY KEY,
    kunden_id INTEGER NOT NULL,
    kontotyp TEXT NOT NULL CHECK (kontotyp IN ('Girokonto', 'Sparkonto', 'Tagesgeld')),
    saldo REAL NOT NULL DEFAULT 0.0 CHECK (saldo >= -500.0),
    waehrung TEXT NOT NULL DEFAULT 'EUR' CHECK (waehrung IN ('EUR', 'USD', 'CHF'))
);


-- 🎯 TEILZIEL 3 (TODO 3): Füge 4 valide Testkunden ein.
INSERT INTO bank_kunden (id, kunden_nr, name, email, kunden_alter, bonitaets_score, status) VALUES
    (1, 'K-1001', 'Maximilian Mustermann', 'max@muster.de', 34, 750, 'verifiziert'),
    (2, 'K-1002', 'Laura Becker', 'laura@becker.de', 28, 620, 'verifiziert'),
    (3, 'K-1003', 'Tim Schneider', 'tim@schneider.de', 19, 480, 'aktiv'),
    (4, 'K-1004', 'Sabine Graf', 'sabine@graf.de', 45, 820, 'gesperrt');


-- 🎯 TEILZIEL 4 (TODO 4): Füge 4 passende Bankkonten ein.
INSERT INTO bank_konten (iban, kunden_id, kontotyp, saldo, waehrung) VALUES
    ('DE89370400440532013000', 1, 'Girokonto', 2450.50, 'EUR'),
    ('DE89370400440532013001', 1, 'Sparkonto', 15000.00, 'EUR'),
    ('DE27100110012345678900', 2, 'Girokonto', -120.00, 'EUR'),
    ('DE45200300001122334455', 3, 'Girokonto', 350.00, 'EUR');


-- 🎯 TEILZIEL 5 (TODO 5): Finde alle verifizierten Kunden mit bonitaets_score >= 600.
-- SELECT ...;
SELECT id, kunden_nr, name, bonitaets_score, status 
FROM bank_kunden 
WHERE status = 'verifiziert' AND bonitaets_score >= 600;


-- 🎯 TEILZIEL 6 (TODO 6): Finde alle Bankkonten, die sich aktuell im Dispo befinden (saldo < 0.0).
-- SELECT ...;
SELECT iban, kunden_id, kontotyp, saldo 
FROM bank_konten 
WHERE saldo < 0.0;
