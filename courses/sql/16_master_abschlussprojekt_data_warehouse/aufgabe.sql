-- ============================================================================
-- 💎 SQL 16: MASTER-ABSCHLUSSPROJEKT – E-COMMERCE ANALYTICS DATA WAREHOUSE 💎
-- ============================================================================
-- In diesem Master-Projekt baust du ein produktionsreifes E-Commerce Data Warehouse:
-- 1. Sternschema DDL & Indizes (Fakten- und Dimensionstabellen)
-- 2. Kohortenanalyse (Cohort Retention Matrix mit CTEs)
-- 3. RFM-Kundensegmentierung mit NTILE Window Functions
-- 4. Executive Business Intelligence Dashboard View

-- ----------------------------------------------------------------------------
-- 1. TABELLEN-SCHEMA (STAR SCHEMA DDL) & TESTDATEN
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS dim_customers (
    customer_key INTEGER PRIMARY KEY,
    customer_id TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    city TEXT NOT NULL,
    country TEXT NOT NULL,
    signup_date TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS dim_products (
    product_key INTEGER PRIMARY KEY,
    product_id TEXT UNIQUE NOT NULL,
    product_name TEXT NOT NULL,
    category TEXT NOT NULL,
    unit_cost REAL NOT NULL,
    unit_price REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS dim_channels (
    channel_key INTEGER PRIMARY KEY,
    channel_name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS fact_orders (
    order_key INTEGER PRIMARY KEY,
    order_id TEXT UNIQUE NOT NULL,
    customer_key INTEGER NOT NULL,
    channel_key INTEGER NOT NULL,
    order_date TEXT NOT NULL,
    total_amount REAL NOT NULL,
    status TEXT NOT NULL,
    FOREIGN KEY (customer_key) REFERENCES dim_customers(customer_key),
    FOREIGN KEY (channel_key) REFERENCES dim_channels(channel_key)
);

CREATE TABLE IF NOT EXISTS fact_order_items (
    item_key INTEGER PRIMARY KEY AUTOINCREMENT,
    order_key INTEGER NOT NULL,
    product_key INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    unit_price REAL NOT NULL,
    line_total REAL NOT NULL,
    FOREIGN KEY (order_key) REFERENCES fact_orders(order_key),
    FOREIGN KEY (product_key) REFERENCES dim_products(product_key)
);

-- B-Tree Indizes für analytische Fact-Lookups
CREATE INDEX IF NOT EXISTS idx_fact_orders_customer ON fact_orders(customer_key);
CREATE INDEX IF NOT EXISTS idx_fact_orders_date ON fact_orders(order_date);
CREATE INDEX IF NOT EXISTS idx_fact_items_order ON fact_order_items(order_key);

-- Testdaten (Dimensionen)
INSERT INTO dim_customers (customer_key, customer_id, name, city, country, signup_date) VALUES
    (1, 'CUST-001', 'Alice Becker', 'Berlin', 'Germany', '2024-01-05'),
    (2, 'CUST-002', 'Bob Meier', 'Hamburg', 'Germany', '2024-01-12'),
    (3, 'CUST-003', 'Carla Wagner', 'München', 'Germany', '2024-01-20'),
    (4, 'CUST-004', 'David Fischer', 'Wien', 'Austria', '2024-02-02'),
    (5, 'CUST-005', 'Eva Klein', 'Zürich', 'Switzerland', '2024-02-15'),
    (6, 'CUST-006', 'Felix Wolf', 'Köln', 'Germany', '2024-03-01'),
    (7, 'CUST-007', 'Grace Hopper', 'Berlin', 'Germany', '2024-03-10');

INSERT INTO dim_products (product_key, product_id, product_name, category, unit_cost, unit_price) VALUES
    (1, 'PROD-01', 'Cloud Server S', 'Hosting', 20.00, 49.00),
    (2, 'PROD-02', 'Cloud Server L', 'Hosting', 60.00, 149.00),
    (3, 'PROD-03', 'Enterprise Database', 'Software', 150.00, 499.00),
    (4, 'PROD-04', 'Security Suite Pro', 'Software', 50.00, 199.00),
    (5, 'PROD-05', 'Consulting Tagessatz', 'Services', 400.00, 950.00);

INSERT INTO dim_channels (channel_key, channel_name) VALUES
    (1, 'Web Direct'),
    (2, 'Partner Referral'),
    (3, 'Sales Outbound');

-- Testdaten (Fakten: Bestellungen über Jan, Feb, Mär, Apr 2024)
INSERT INTO fact_orders (order_key, order_id, customer_key, channel_key, order_date, total_amount, status) VALUES
    (1001, 'ORD-1001', 1, 1, '2024-01-10', 49.00, 'COMPLETED'),
    (1002, 'ORD-1002', 2, 2, '2024-01-15', 149.00, 'COMPLETED'),
    (1003, 'ORD-1003', 3, 1, '2024-01-22', 499.00, 'COMPLETED'),
    (1004, 'ORD-1004', 1, 1, '2024-02-05', 199.00, 'COMPLETED'),
    (1005, 'ORD-1005', 2, 2, '2024-02-18', 149.00, 'COMPLETED'),
    (1006, 'ORD-1006', 4, 3, '2024-02-20', 950.00, 'COMPLETED'),
    (1007, 'ORD-1007', 5, 1, '2024-02-25', 49.00, 'COMPLETED'),
    (1008, 'ORD-1008', 1, 1, '2024-03-02', 499.00, 'COMPLETED'),
    (1009, 'ORD-1009', 3, 1, '2024-03-12', 49.00, 'COMPLETED'),
    (1010, 'ORD-1010', 6, 2, '2024-03-15', 950.00, 'COMPLETED'),
    (1011, 'ORD-1011', 7, 1, '2024-03-20', 149.00, 'COMPLETED'),
    (1012, 'ORD-1012', 1, 1, '2024-04-05', 950.00, 'COMPLETED'),
    (1013, 'ORD-1013', 2, 2, '2024-04-10', 149.00, 'COMPLETED'),
    (1014, 'ORD-1014', 4, 3, '2024-04-15', 499.00, 'COMPLETED');


-- ============================================================================
-- 🎯 MASTER-AUFGABEN
-- ============================================================================

-- 🎯 TODO 1: Data Warehouse Health & KPI Basis Check
-- Schreibe eine Abfrage, die über Joins die Top 3 Produkte nach Gesamtumsatz liefert:
-- - product_name, category, anzahl_verkaeufe (COUNT), gesamt_umsatz (SUM(total_amount))
-- Sortiere nach gesamt_umsatz DESC und limitiere auf 3.
-- TODO: SELECT Query für Top-3 Produkte


-- 🎯 TODO 2: Kohorten-Retention-Matrix (Cohort Analysis)
-- Ermittle für jede Akquisitions-Kohorte (Monat des ersten Kaufs) das Wiederkaufverhalten:
-- Baue folgende CTE-Pipeline:
-- 1. `kunden_kohorte`: customer_key, kohorte (strftime('%Y-%m', MIN(order_date)))
-- 2. `kunden_aktivitaet`: customer_key, kohorte, aktivitaets_monat (strftime('%Y-%m', order_date))
-- 3. `kohorten_basis`: kohorte, kohorten_groesse (COUNT(DISTINCT customer_key))
-- 4. `retention_matrix`: kohorte, aktivitaets_monat, aktive_kunden (COUNT(DISTINCT customer_key)),
--    kohorten_groesse,
--    retention_rate_pct = ROUND(aktive_kunden * 100.0 / kohorten_groesse, 1)
-- Sortiere nach kohorte ASC, aktivitaets_monat ASC.
-- TODO: Multi-CTE Kohorten-Matrix schreiben


-- 🎯 TODO 3: RFM-Kundensegmentierung (Recency, Frequency, Monetary)
-- Segmentiere alle Kunden (customer_key, name) zum Stichtag '2024-04-30':
-- 1. `rfm_raw`:
--    - customer_key
--    - recency_tage: CAST(julianday('2024-04-30') - julianday(MAX(order_date)) AS INTEGER)
--    - frequency: COUNT(order_key)
--    - monetary: SUM(total_amount)
-- 2. `rfm_scored`:
--    - r_score: NTILE(4) OVER (ORDER BY recency_tage DESC) (kürzere Tage = höherer Score)
--    - f_score: NTILE(4) OVER (ORDER BY frequency ASC)
--    - m_score: NTILE(4) OVER (ORDER BY monetary ASC)
-- 3. Haupt-SELECT mit Segment-Zuweisung:
--    CASE 
--       WHEN r_score >= 3 AND f_score >= 3 AND m_score >= 3 THEN 'Champions'
--       WHEN f_score >= 3 THEN 'Loyal Customers'
--       WHEN r_score <= 2 AND f_score >= 2 THEN 'At Risk'
--       ELSE 'Potential / Hibernating'
--    END AS kunden_segment
-- Sortiere nach monetary DESC.
-- TODO: RFM CTEs und Segmentierung schreiben


-- 🎯 TODO 4: Executive Business Intelligence View (v_executive_kpi_dashboard)
-- Erstelle einen View `v_executive_kpi_dashboard`, der monatliche Kennzahlen liefert:
-- - monat: strftime('%Y-%m', order_date)
-- - monats_umsatz: SUM(total_amount)
-- - anzahl_bestellungen: COUNT(order_key)
-- - aktive_kunden: COUNT(DISTINCT customer_key)
-- - aov: ROUND(AVG(total_amount), 2) (Average Order Value)
-- - vormonat_umsatz: LAG(SUM(total_amount), 1, 0) OVER (ORDER BY strftime('%Y-%m', order_date))
-- - mom_wachstum_pct: ROUND((SUM(total_amount) - LAG(SUM(total_amount), 1, SUM(total_amount)) OVER (ORDER BY strftime('%Y-%m', order_date))) * 100.0 / LAG(SUM(total_amount), 1, SUM(total_amount)) OVER (ORDER BY strftime('%Y-%m', order_date)), 2)
-- - kumulierter_allzeit_umsatz: SUM(SUM(total_amount)) OVER (ORDER BY strftime('%Y-%m', order_date) ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
-- Gruppiere im View nach strftime('%Y-%m', order_date).
-- TODO: CREATE VIEW v_executive_kpi_dashboard AS ...
