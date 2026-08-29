CREATE TABLE IF NOT EXISTS mitarbeiter (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    abteilung TEXT NOT NULL,
    gehalt REAL NOT NULL
);

INSERT INTO mitarbeiter (name, abteilung, gehalt) VALUES 
    ('Anna Schmidt', 'Entwicklung', 65000),
    ('Ben Weber', 'Marketing', 48000),
    ('Clara Schulz', 'Entwicklung', 72000);

SELECT * FROM mitarbeiter WHERE abteilung = 'Entwicklung';
