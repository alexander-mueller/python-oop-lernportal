-- ============================================================================
-- 🗄️ SQL 15: VIRTUELLE VIEWS & DATENBANK-TRIGGER 🗄️
-- ============================================================================

-- ----------------------------------------------------------------------------
-- 1. TABELLEN-SCHEMA & TESTDATEN
-- ----------------------------------------------------------------------------
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

-- Testdaten
INSERT INTO kunden (id, name, email, passwort_hash, stadt) VALUES
    (1, 'Alice Becker', 'alice@example.com', '$2y$12$e8Y7G...', 'Berlin'),
    (2, 'Bob Meier', 'bob@example.com', '$2y$12$K9j2L...', 'Hamburg'),
    (3, 'Carla Wagner', 'carla@example.com', '$2y$12$P3m8Q...', 'München');

INSERT INTO produkte (id, name, preis, lagerbestand) VALUES
    (101, '4K OLED Monitor 32"', 899.00, 50),
    (102, 'Ergonomische Tastatur Pro', 149.00, 100),
    (103, 'Wireless Noise Cancelling Headset', 249.00, 30);

INSERT INTO bestellungen (id, kunde_id, bestell_datum, gesamtbetrag) VALUES
    (1, 1, '2024-02-10', 1048.00),
    (2, 1, '2024-03-01', 249.00),
    (3, 2, '2024-02-15', 899.00);

INSERT INTO bestellpositionen (bestell_id, produkt_id, menge, einzelpreis) VALUES
    (1, 101, 1, 899.00),
    (1, 102, 1, 149.00),
    (2, 103, 1, 249.00),
    (3, 101, 1, 899.00);


-- ============================================================================
-- 🎯 AUFGABEN
-- ============================================================================

-- 🎯 TODO 1: Virtueller View `v_kunden_bestell_cockpit`
-- Erstelle einen View `v_kunden_bestell_cockpit` (OHNE die Spalte passwort_hash!),
-- der für jeden Kunden folgende Spalten bündelt:
-- - kunde_id: k.id
-- - name: k.name
-- - email: k.email
-- - stadt: k.stadt
-- - anzahl_bestellungen: COUNT(b.id)
-- - gesamt_umsatz: COALESCE(SUM(b.gesamtbetrag), 0.0)
-- - letzte_bestellung: MAX(b.bestell_datum)
-- Gruppiere nach k.id, k.name, k.email, k.stadt.
-- TODO: CREATE VIEW v_kunden_bestell_cockpit AS ...


-- 🎯 TODO 2: Virtueller View `v_top_seller_uebersicht`
-- Erstelle einen View `v_top_seller_uebersicht`, der für jedes Produkt folgende Spalten berechnet:
-- - produkt_id: p.id
-- - produkt_name: p.name
-- - aktueller_preis: p.preis
-- - verkaufte_menge: COALESCE(SUM(bp.menge), 0)
-- - gesamt_erloes: COALESCE(SUM(bp.menge * bp.einzelpreis), 0.0)
-- Nutze LEFT JOIN von produkte auf bestellpositionen und gruppiere nach p.id, p.name, p.preis.
-- TODO: CREATE VIEW v_top_seller_uebersicht AS ...


-- 🎯 TODO 3: Trigger `trg_lagerbestand_reduzieren`
-- Erstelle einen Trigger, der bei JEDEM neuen Eintrag in `bestellpositionen`
-- (AFTER INSERT ON bestellpositionen FOR EACH ROW) den Lagerbestand in der Tabelle `produkte`
-- automatisch um NEW.menge verringert:
-- UPDATE produkte SET lagerbestand = lagerbestand - NEW.menge WHERE id = NEW.produkt_id;
-- TODO: CREATE TRIGGER trg_lagerbestand_reduzieren ...


-- 🎯 TODO 4: Trigger `trg_preis_historie_audit`
-- Erstelle einen Trigger, der bei JEDER Änderung des Preises eines Produkts
-- (AFTER UPDATE OF preis ON produkte FOR EACH ROW)
-- einen Audit-Eintrag in `audit_preis_historie` schreibt:
-- INSERT INTO audit_preis_historie (produkt_id, alter_preis, neuer_preis, aenderungs_datum)
-- VALUES (OLD.id, OLD.preis, NEW.preis, '2024-03-15 12:00:00');
-- TODO: CREATE TRIGGER trg_preis_historie_audit ...
