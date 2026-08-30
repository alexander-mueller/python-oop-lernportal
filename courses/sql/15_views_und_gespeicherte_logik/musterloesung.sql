-- ============================================================================
-- 💡 SQL 15: MUSTERLÖSUNG – VIEWS & TRIGGER 💡
-- ============================================================================

CREATE TABLE IF NOT EXISTS kunden (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    passwort_hash TEXT NOT NULL,
    stadt TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS produkte (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    preis REAL NOT NULL,
    lagerbestand INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS bestellungen (
    id INTEGER PRIMARY KEY,
    kunde_id INTEGER NOT NULL,
    bestell_datum TEXT NOT NULL,
    gesamtbetrag REAL NOT NULL,
    FOREIGN KEY (kunde_id) REFERENCES kunden(id)
);

CREATE TABLE IF NOT EXISTS bestellpositionen (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bestell_id INTEGER NOT NULL,
    produkt_id INTEGER NOT NULL,
    menge INTEGER NOT NULL,
    einzelpreis REAL NOT NULL,
    FOREIGN KEY (bestell_id) REFERENCES bestellungen(id),
    FOREIGN KEY (produkt_id) REFERENCES produkte(id)
);

CREATE TABLE IF NOT EXISTS audit_preis_historie (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    produkt_id INTEGER NOT NULL,
    alter_preis REAL NOT NULL,
    neuer_preis REAL NOT NULL,
    aenderungs_datum TEXT NOT NULL
);

INSERT OR REPLACE INTO kunden (id, name, email, passwort_hash, stadt) VALUES
    (1, 'Alice Becker', 'alice@example.com', '$2y$12$e8Y7G...', 'Berlin'),
    (2, 'Bob Meier', 'bob@example.com', '$2y$12$K9j2L...', 'Hamburg'),
    (3, 'Carla Wagner', 'carla@example.com', '$2y$12$P3m8Q...', 'München');

INSERT OR REPLACE INTO produkte (id, name, preis, lagerbestand) VALUES
    (101, '4K OLED Monitor 32"', 899.00, 50),
    (102, 'Ergonomische Tastatur Pro', 149.00, 100),
    (103, 'Wireless Noise Cancelling Headset', 249.00, 30);

INSERT OR REPLACE INTO bestellungen (id, kunde_id, bestell_datum, gesamtbetrag) VALUES
    (1, 1, '2024-02-10', 1048.00),
    (2, 1, '2024-03-01', 249.00),
    (3, 2, '2024-02-15', 899.00);

INSERT OR REPLACE INTO bestellpositionen (bestell_id, produkt_id, menge, einzelpreis) VALUES
    (1, 101, 1, 899.00),
    (1, 102, 1, 149.00),
    (2, 103, 1, 249.00),
    (3, 101, 1, 899.00);

-- 🎯 TODO 1: View v_kunden_bestell_cockpit
DROP VIEW IF EXISTS v_kunden_bestell_cockpit;
CREATE VIEW v_kunden_bestell_cockpit AS
SELECT 
    k.id AS kunde_id,
    k.name,
    k.email,
    k.stadt,
    COUNT(b.id) AS anzahl_bestellungen,
    COALESCE(SUM(b.gesamtbetrag), 0.0) AS gesamt_umsatz,
    MAX(b.bestell_datum) AS letzte_bestellung
FROM kunden k
LEFT JOIN bestellungen b ON k.id = b.kunde_id
GROUP BY k.id, k.name, k.email, k.stadt;

-- 🎯 TODO 2: View v_top_seller_uebersicht
DROP VIEW IF EXISTS v_top_seller_uebersicht;
CREATE VIEW v_top_seller_uebersicht AS
SELECT 
    p.id AS produkt_id,
    p.name AS produkt_name,
    p.preis AS aktueller_preis,
    COALESCE(SUM(bp.menge), 0) AS verkaufte_menge,
    COALESCE(SUM(bp.menge * bp.einzelpreis), 0.0) AS gesamt_erloes
FROM produkte p
LEFT JOIN bestellpositionen bp ON p.id = bp.produkt_id
GROUP BY p.id, p.name, p.preis;

-- 🎯 TODO 3: Trigger trg_lagerbestand_reduzieren
DROP TRIGGER IF EXISTS trg_lagerbestand_reduzieren;
CREATE TRIGGER trg_lagerbestand_reduzieren
AFTER INSERT ON bestellpositionen
FOR EACH ROW
BEGIN
    UPDATE produkte 
    SET lagerbestand = lagerbestand - NEW.menge 
    WHERE id = NEW.produkt_id;
END;

-- 🎯 TODO 4: Trigger trg_preis_historie_audit
DROP TRIGGER IF EXISTS trg_preis_historie_audit;
CREATE TRIGGER trg_preis_historie_audit
AFTER UPDATE OF preis ON produkte
FOR EACH ROW
BEGIN
    INSERT INTO audit_preis_historie (produkt_id, alter_preis, neuer_preis, aenderungs_datum)
    VALUES (OLD.id, OLD.preis, NEW.preis, '2024-03-15 12:00:00');
END;
