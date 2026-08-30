-- ============================================================================
-- 💡 SQL 13: MUSTERLÖSUNG – INDIZES & QUERY-OPTIMIERUNG 💡
-- ============================================================================

CREATE TABLE IF NOT EXISTS kunden (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    stadt TEXT NOT NULL,
    status TEXT NOT NULL,
    registriert_am TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS artikel (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    kategorie_id INTEGER NOT NULL,
    preis REAL NOT NULL,
    verfuegbar INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS server_logs (
    id INTEGER PRIMARY KEY,
    ip TEXT NOT NULL,
    pfad TEXT NOT NULL,
    status_code INTEGER NOT NULL,
    zeitstempel TEXT NOT NULL
);

INSERT OR REPLACE INTO kunden (id, name, email, stadt, status, registriert_am) VALUES
    (1, 'Max Mustermann', 'max@example.com', 'Berlin', 'aktiv', '2023-01-10'),
    (2, 'Sarah Connor', 'sarah@example.com', 'Hamburg', 'aktiv', '2023-05-14'),
    (3, 'Tim Berg', 'tim@example.com', 'München', 'inaktiv', '2023-08-20'),
    (4, 'Julia Sommer', 'julia@example.com', 'Berlin', 'aktiv', '2024-02-05'),
    (5, 'Felix Wolf', 'felix@example.com', 'Köln', 'gesperrt', '2024-03-18');

INSERT OR REPLACE INTO artikel (id, name, kategorie_id, preis, verfuegbar) VALUES
    (1, 'High-End Gaming PC', 1, 2499.00, 1),
    (2, 'Office Laptop 14', 1, 799.00, 1),
    (3, 'Budget Notebook', 1, 399.00, 1),
    (4, 'Ergonomische Tastatur', 2, 149.00, 1),
    (5, 'Mechanische Tastatur', 2, 89.00, 1),
    (6, 'Standard Maus', 2, 19.00, 1);

INSERT OR REPLACE INTO server_logs (id, ip, pfad, status_code, zeitstempel) VALUES
    (1, '192.168.1.1', '/api/v1/users', 200, '2024-01-15 10:00:00'),
    (2, '192.168.1.2', '/api/v1/login', 401, '2024-01-15 10:05:00'),
    (3, '192.168.1.3', '/api/v1/checkout', 500, '2024-02-01 14:20:00'),
    (4, '192.168.1.1', '/api/v1/products', 200, '2024-02-15 11:30:00'),
    (5, '192.168.1.4', '/api/v1/orders', 200, '2024-03-01 09:15:00');

-- 🎯 TODO 1: Unique & Composite Indizes
CREATE UNIQUE INDEX IF NOT EXISTS idx_kunden_email_unique ON kunden(email);
CREATE INDEX IF NOT EXISTS idx_artikel_kat_preis ON artikel(kategorie_id, preis DESC);

-- 🎯 TODO 2: Partieller Index
CREATE INDEX IF NOT EXISTS idx_aktive_kunden_stadt ON kunden(stadt) WHERE status = 'aktiv';

-- 🎯 TODO 3: Index für Server-Logs & SARGable Range Filter
CREATE INDEX IF NOT EXISTS idx_server_logs_zeitstempel ON server_logs(zeitstempel);

SELECT id, ip, pfad, status_code, zeitstempel 
FROM server_logs
WHERE zeitstempel >= '2024-01-01 00:00:00' AND zeitstempel < '2025-01-01 00:00:00'
ORDER BY zeitstempel ASC;

-- 🎯 TODO 4: Query-Plan Analyse mit EXPLAIN QUERY PLAN
EXPLAIN QUERY PLAN SELECT * FROM kunden WHERE email = 'sarah@example.com';
EXPLAIN QUERY PLAN SELECT * FROM artikel WHERE kategorie_id = 1 AND preis > 500;
