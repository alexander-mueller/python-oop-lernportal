-- ============================================================================
-- 💡 SQL 14: MUSTERLÖSUNG – ACID TRANSAKTIONEN & SAVEPOINTS 💡
-- ============================================================================

CREATE TABLE IF NOT EXISTS konten (
    konto_id INTEGER PRIMARY KEY,
    inhaber TEXT NOT NULL,
    iban TEXT UNIQUE NOT NULL,
    kontostand REAL NOT NULL CHECK (kontostand >= 0)
);

CREATE TABLE IF NOT EXISTS transaktions_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    von_konto INTEGER NOT NULL,
    an_konto INTEGER NOT NULL,
    betrag REAL NOT NULL,
    status TEXT NOT NULL,
    zeitstempel TEXT NOT NULL,
    FOREIGN KEY (von_konto) REFERENCES konten(konto_id),
    FOREIGN KEY (an_konto) REFERENCES konten(konto_id)
);

CREATE TABLE IF NOT EXISTS warenkorb_reservierung (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    kunde_id INTEGER NOT NULL,
    artikel_id INTEGER NOT NULL,
    menge INTEGER NOT NULL,
    status TEXT NOT NULL
);

INSERT OR REPLACE INTO konten (konto_id, inhaber, iban, kontostand) VALUES
    (1, 'Max Mustermann', 'DE89370400440532013000', 1000.00),
    (2, 'Sarah Connor', 'DE89370400440532013001', 2500.00),
    (3, 'Tim Berg', 'DE89370400440532013002', 500.00);

-- 🎯 TODO 1: Erfolgreiche Banküberweisung mit COMMIT
BEGIN TRANSACTION;
UPDATE konten SET kontostand = kontostand - 300.00 WHERE konto_id = 1;
UPDATE konten SET kontostand = kontostand + 300.00 WHERE konto_id = 2;
INSERT INTO transaktions_log (von_konto, an_konto, betrag, status, zeitstempel) 
VALUES (1, 2, 300.00, 'ERFOLGREICH', '2024-03-01 10:00:00');
COMMIT;

-- 🎯 TODO 2: Transaktionsabbruch mit ROLLBACK
BEGIN TRANSACTION;
UPDATE konten SET kontostand = kontostand + 1000.00 WHERE konto_id = 1;
-- Simulierter Fehlerzustand: Rollback macht alle Änderungen ungeschehen
ROLLBACK;

-- 🎯 TODO 3: Teil-Rollback mit SAVEPOINT
BEGIN TRANSACTION;
INSERT INTO warenkorb_reservierung (kunde_id, artikel_id, menge, status) 
VALUES (1, 101, 2, 'RESERVIERT');

SAVEPOINT sp_zusatz_buchung;

INSERT INTO warenkorb_reservierung (kunde_id, artikel_id, menge, status) 
VALUES (1, 999, 100, 'UNGÜLTIG');

ROLLBACK TO SAVEPOINT sp_zusatz_buchung;

COMMIT;

-- 🎯 TODO 4: Konsistenz-Audit (Bilanzprüfung)
SELECT 
    (SELECT SUM(kontostand) FROM konten) AS bilanz_summe,
    (SELECT COUNT(*) FROM transaktions_log WHERE status = 'ERFOLGREICH') AS erfolgreiche_transfers;
