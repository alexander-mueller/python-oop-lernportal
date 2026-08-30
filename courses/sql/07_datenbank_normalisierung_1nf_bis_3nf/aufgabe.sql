-- 🗄️ SQL 07: DATENBANK-NORMALISIERUNG (1NF BIS 3NF) 🗄️
-- ====================================================

PRAGMA foreign_keys = ON;

-- 🎯 TEILZIEL 1 (TODO 1): Stammdatentabellen `orte` und `artikel` anlegen.
-- orte: plz (TEXT PRIMARY KEY), stadt (TEXT NOT NULL)
-- artikel: id (INTEGER PRIMARY KEY AUTOINCREMENT), bezeichnung (TEXT NOT NULL), einzelpreis (REAL NOT NULL CHECK > 0)
CREATE TABLE IF NOT EXISTS orte (
    plz TEXT PRIMARY KEY,
    stadt TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS artikel (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bezeichnung TEXT NOT NULL,
    einzelpreis REAL NOT NULL CHECK (einzelpreis > 0.0)
);


-- 🎯 TEILZIEL 2 (TODO 2): Tabelle `kunden` anlegen (3NF-konform mit Referenz auf orte.plz).
-- id (INTEGER PRIMARY KEY AUTOINCREMENT), name (TEXT NOT NULL), email (TEXT NOT NULL UNIQUE), plz (TEXT NOT NULL)
CREATE TABLE IF NOT EXISTS kunden (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    plz TEXT NOT NULL,
    FOREIGN KEY (plz) REFERENCES orte(plz)
);


-- 🎯 TEILZIEL 3 (TODO 3): Auftragskopf `auftraege` und Positionstabelle `auftragspositionen` anlegen.
-- auftragspositionen nutzt einen zusammengesetzten Primärschlüssel (auftrag_id, artikel_id).
CREATE TABLE IF NOT EXISTS auftraege (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    kunde_id INTEGER NOT NULL,
    auftragsdatum TEXT NOT NULL,
    FOREIGN KEY (kunde_id) REFERENCES kunden(id)
);

CREATE TABLE IF NOT EXISTS auftragspositionen (
    auftrag_id INTEGER NOT NULL,
    artikel_id INTEGER NOT NULL,
    menge INTEGER NOT NULL CHECK (menge > 0),
    PRIMARY KEY (auftrag_id, artikel_id),
    FOREIGN KEY (auftrag_id) REFERENCES auftraege(id),
    FOREIGN KEY (artikel_id) REFERENCES artikel(id)
);


-- 🎯 TEILZIEL 4 (TODO 4): Testdaten einfügen.
INSERT INTO orte (plz, stadt) VALUES
    ('10115', 'Berlin'),
    ('80331', 'München'),
    ('50667', 'Köln');

INSERT INTO kunden (id, name, email, plz) VALUES
    (1, 'Max Mustermann', 'max@beispiel.de', '10115'),
    (2, 'Erika Musterfrau', 'erika@beispiel.de', '80331');

INSERT INTO artikel (id, bezeichnung, einzelpreis) VALUES
    (1, 'Ergonomische Tastatur', 89.90),
    (2, 'USB-C Dockingstation', 149.00),
    (3, '4K Monitor 27 Zoll', 329.00);

INSERT INTO auftraege (id, kunde_id, auftragsdatum) VALUES
    (1, 1, '2026-08-15'),
    (2, 2, '2026-08-16');

INSERT INTO auftragspositionen (auftrag_id, artikel_id, menge) VALUES
    (1, 1, 1),
    (1, 2, 2),
    (2, 3, 1);


-- 🎯 TEILZIEL 5 (TODO 5): Reporting-Abfrage: Verbinde alle Tabellen und berechne den Positionspreis (menge * einzelpreis).
-- SELECT ...;
SELECT 
    a.id AS auftrag_id,
    k.name AS kunden_name,
    o.stadt AS kunden_stadt,
    art.bezeichnung AS artikel,
    pos.menge,
    art.einzelpreis,
    round(pos.menge * art.einzelpreis, 2) AS position_gesamt
FROM auftraege a
JOIN kunden k ON a.kunde_id = k.id
JOIN orte o ON k.plz = o.plz
JOIN auftragspositionen pos ON a.id = pos.auftrag_id
JOIN artikel art ON pos.artikel_id = art.id
ORDER BY a.id, art.id;
