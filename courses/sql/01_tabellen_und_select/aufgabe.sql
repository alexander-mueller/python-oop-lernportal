-- 🗄️ SQL 01: TABELLEN ANLEGEN & DATEN ABFRAGEN 🗄️
-- ===============================================

-- 🎯 TEILZIEL 1 (TODO 1): Erstelle eine Tabelle `mitarbeiter` mit:
--    id (INTEGER PRIMARY KEY), name (TEXT), abteilung (TEXT), gehalt (REAL)
CREATE TABLE IF NOT EXISTS mitarbeiter (
    -- TODO: Spalten definieren
    id INTEGER PRIMARY KEY
);

-- 🎯 TEILZIEL 2 (TODO 2): Füge mindestens 3 Test-Mitarbeiter ein
INSERT INTO mitarbeiter (name, abteilung, gehalt) VALUES 
    ('Anna Schmidt', 'Entwicklung', 65000),
    ('Ben Weber', 'Marketing', 48000),
    ('Clara Schulz', 'Entwicklung', 72000);

-- 🎯 TEILZIEL 3 (TODO 3): Schreibe eine SELECT-Abfrage, die alle Mitarbeiter aus der 'Entwicklung' anzeigt
SELECT * FROM mitarbeiter WHERE abteilung = 'Entwicklung';
