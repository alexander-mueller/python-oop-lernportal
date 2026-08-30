-- ============================================================================
-- 🗄️ SQL 14: ACID TRANSAKTIONEN, COMMIT, ROLLBACK & SAVEPOINTS 🗄️
-- ============================================================================

-- ----------------------------------------------------------------------------
-- 1. TABELLEN-SCHEMA & TESTDATEN
-- ----------------------------------------------------------------------------
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

-- Testdaten (Gesamtsumme aller Konten = 1000 + 2500 + 500 = 4000 €)
INSERT INTO konten (konto_id, inhaber, iban, kontostand) VALUES
    (1, 'Max Mustermann', 'DE89370400440532013000', 1000.00),
    (2, 'Sarah Connor', 'DE89370400440532013001', 2500.00),
    (3, 'Tim Berg', 'DE89370400440532013002', 500.00);


-- ============================================================================
-- 🎯 AUFGABEN
-- ============================================================================

-- 🎯 TODO 1: Erfolgreiche Banküberweisung mit COMMIT
-- Führe eine vollständige Transaktion durch:
-- 1. BEGIN TRANSACTION;
-- 2. Ziehe 300.00 € von Konto 1 ab.
-- 3. Schreibe 300.00 € auf Konto 2 gut.
-- 4. Trage den Transfer in transaktions_log ein:
--    von_konto: 1, an_konto: 2, betrag: 300.00, status: 'ERFOLGREICH', zeitstempel: '2024-03-01 10:00:00'
-- 5. COMMIT;
-- TODO: Transaktion implementieren


-- 🎯 TODO 2: Transaktionsabbruch mit ROLLBACK bei Fehler / Überziehung
-- Simuliere eine Transaktion, die fehlschlägt und rückgängig gemacht wird:
-- 1. BEGIN TRANSACTION;
-- 2. Schreibe testweise 1000.00 € von Konto 3 auf Konto 1 um.
-- 3. Stelle fest, dass Konto 3 nicht genug Deckung hätte oder simuliere einen Abbruch:
-- 4. ROLLBACK;
-- TODO: Transaktionsblock mit ROLLBACK schreiben


-- 🎯 TODO 3: Teil-Rollback mit SAVEPOINT
-- Führe eine mehrstufige Transaktion mit Zwischenspeicherpunkt aus:
-- 1. BEGIN TRANSACTION;
-- 2. Füge eine gültige Reservierung ein:
--    kunde_id: 1, artikel_id: 101, menge: 2, status: 'RESERVIERT'
-- 3. Erstelle einen SAVEPOINT namens `sp_zusatz_buchung`;
-- 4. Füge testweise eine ungültige Reservierung ein:
--    kunde_id: 1, artikel_id: 999, menge: 100, status: 'UNGÜLTIG'
-- 5. Setze die fehlerhafte Buchung zurück mit:
--    ROLLBACK TO SAVEPOINT sp_zusatz_buchung;
-- 6. Bestätige die Transaktion mit COMMIT;
-- TODO: SAVEPOINT Transaktion implementieren


-- 🎯 TODO 4: Konsistenz-Audit (Bilanzprüfung)
-- Schreibe eine SELECT-Abfrage, die:
-- - die Gesamtsumme des Bankvermögens (SUM(kontostand) AS bilanz_summe)
-- - die Anzahl der erfolgreichen Transaktionen im Log (COUNT(*) AS erfolgreiche_transfers)
-- ermittelt.
SELECT 
    (SELECT SUM(kontostand) FROM konten) AS bilanz_summe,
    (SELECT COUNT(*) FROM transaktions_log WHERE status = 'ERFOLGREICH') AS erfolgreiche_transfers;
