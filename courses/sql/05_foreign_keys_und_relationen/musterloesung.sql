PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS kunden (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS kunden_profile (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    kunde_id INTEGER NOT NULL UNIQUE,
    telefon TEXT,
    lieferadresse TEXT NOT NULL,
    FOREIGN KEY (kunde_id) REFERENCES kunden(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS bestellungen (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    kunde_id INTEGER NOT NULL,
    gesamtbetrag REAL NOT NULL CHECK (gesamtbetrag >= 0.0),
    status TEXT NOT NULL DEFAULT 'offen' CHECK (status IN ('offen', 'bezahlt', 'versendet', 'storniert')),
    FOREIGN KEY (kunde_id) REFERENCES kunden(id) ON DELETE CASCADE
);

INSERT INTO kunden (id, name, email) VALUES
    (1, 'Alice Müller', 'alice@mueller.de'),
    (2, 'Bob Fischer', 'bob@fischer.de'),
    (3, 'Carolin Weber', 'caro@weber.de');

INSERT INTO kunden_profile (id, kunde_id, telefon, lieferadresse) VALUES
    (1, 1, '0170-112233', 'Hauptstr. 12, 10115 Berlin'),
    (2, 2, '0171-445566', 'Musterweg 5, 80331 München'),
    (3, 3, '0172-778899', 'Rheinstr. 42, 50667 Köln');

INSERT INTO bestellungen (id, kunde_id, gesamtbetrag, status) VALUES
    (1, 1, 89.90, 'bezahlt'),
    (2, 1, 149.00, 'versendet'),
    (3, 2, 29.50, 'offen'),
    (4, 3, 499.00, 'bezahlt'),
    (5, 3, 19.99, 'offen');

-- Kaskadierendes Löschen testen
DELETE FROM kunden WHERE id = 1;

-- Abfrage der verbleibenden Bestellungen
SELECT * FROM bestellungen;
