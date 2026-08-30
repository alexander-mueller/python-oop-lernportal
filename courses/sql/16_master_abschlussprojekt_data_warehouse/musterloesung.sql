-- ============================================================================
-- 💡 SQL 16: MUSTERLÖSUNG – MASTER DATA WAREHOUSE & ADVANCED ANALYTICS 💡
-- ============================================================================

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

CREATE INDEX IF NOT EXISTS idx_fact_orders_customer ON fact_orders(customer_key);
CREATE INDEX IF NOT EXISTS idx_fact_orders_date ON fact_orders(order_date);
CREATE INDEX IF NOT EXISTS idx_fact_items_order ON fact_order_items(order_key);

INSERT OR REPLACE INTO dim_customers (customer_key, customer_id, name, city, country, signup_date) VALUES
    (1, 'CUST-001', 'Alice Becker', 'Berlin', 'Germany', '2024-01-05'),
    (2, 'CUST-002', 'Bob Meier', 'Hamburg', 'Germany', '2024-01-12'),
    (3, 'CUST-003', 'Carla Wagner', 'München', 'Germany', '2024-01-20'),
    (4, 'CUST-004', 'David Fischer', 'Wien', 'Austria', '2024-02-02'),
    (5, 'CUST-005', 'Eva Klein', 'Zürich', 'Switzerland', '2024-02-15'),
    (6, 'CUST-006', 'Felix Wolf', 'Köln', 'Germany', '2024-03-01'),
    (7, 'CUST-007', 'Grace Hopper', 'Berlin', 'Germany', '2024-03-10');

INSERT OR REPLACE INTO dim_products (product_key, product_id, product_name, category, unit_cost, unit_price) VALUES
    (1, 'PROD-01', 'Cloud Server S', 'Hosting', 20.00, 49.00),
    (2, 'PROD-02', 'Cloud Server L', 'Hosting', 60.00, 149.00),
    (3, 'PROD-03', 'Enterprise Database', 'Software', 150.00, 499.00),
    (4, 'PROD-04', 'Security Suite Pro', 'Software', 50.00, 199.00),
    (5, 'PROD-05', 'Consulting Tagessatz', 'Services', 400.00, 950.00);

INSERT OR REPLACE INTO dim_channels (channel_key, channel_name) VALUES
    (1, 'Web Direct'),
    (2, 'Partner Referral'),
    (3, 'Sales Outbound');

INSERT OR REPLACE INTO fact_orders (order_key, order_id, customer_key, channel_key, order_date, total_amount, status) VALUES
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

-- 🎯 TODO 1: Top-Produkte & Analytics Check
SELECT 
    p.product_name,
    p.category,
    COUNT(fo.order_key) AS anzahl_verkaeufe,
    SUM(fo.total_amount) AS gesamt_umsatz
FROM dim_products p
JOIN fact_orders fo ON p.product_key = fo.channel_key
GROUP BY p.product_key, p.product_name, p.category
ORDER BY gesamt_umsatz DESC;

-- 🎯 TODO 2: Kohorten-Retention-Matrix (Cohort Analysis)
WITH kunden_kohorte AS (
    SELECT 
        customer_key,
        strftime('%Y-%m', MIN(order_date)) AS kohorte
    FROM fact_orders
    GROUP BY customer_key
),
kunden_aktivitaet AS (
    SELECT DISTINCT
        fo.customer_key,
        kk.kohorte,
        strftime('%Y-%m', fo.order_date) AS aktivitaets_monat
    FROM fact_orders fo
    JOIN kunden_kohorte kk ON fo.customer_key = kk.customer_key
),
kohorten_basis AS (
    SELECT 
        kohorte,
        COUNT(DISTINCT customer_key) AS kohorten_groesse
    FROM kunden_kohorte
    GROUP BY kohorte
)
SELECT 
    ka.kohorte,
    ka.aktivitaets_monat,
    COUNT(DISTINCT ka.customer_key) AS aktive_kunden,
    kb.kohorten_groesse,
    ROUND(COUNT(DISTINCT ka.customer_key) * 100.0 / kb.kohorten_groesse, 1) AS retention_rate_pct
FROM kunden_aktivitaet ka
JOIN kohorten_basis kb ON ka.kohorte = kb.kohorte
GROUP BY ka.kohorte, ka.aktivitaets_monat, kb.kohorten_groesse
ORDER BY ka.kohorte ASC, ka.aktivitaets_monat ASC;

-- 🎯 TODO 3: RFM-Kundensegmentierung (Recency, Frequency, Monetary)
WITH rfm_raw AS (
    SELECT 
        fo.customer_key,
        c.name AS kunden_name,
        CAST(julianday('2024-04-30') - julianday(MAX(fo.order_date)) AS INTEGER) AS recency_tage,
        COUNT(fo.order_key) AS frequency,
        SUM(fo.total_amount) AS monetary
    FROM fact_orders fo
    JOIN dim_customers c ON fo.customer_key = c.customer_key
    GROUP BY fo.customer_key, c.name
),
rfm_scored AS (
    SELECT 
        customer_key,
        kunden_name,
        recency_tage,
        frequency,
        monetary,
        NTILE(4) OVER (ORDER BY recency_tage DESC) AS r_score,
        NTILE(4) OVER (ORDER BY frequency ASC) AS f_score,
        NTILE(4) OVER (ORDER BY monetary ASC) AS m_score
    FROM rfm_raw
)
SELECT 
    customer_key,
    kunden_name,
    recency_tage,
    frequency,
    monetary,
    r_score,
    f_score,
    m_score,
    CASE 
        WHEN r_score >= 3 AND f_score >= 3 AND m_score >= 3 THEN 'Champions'
        WHEN f_score >= 3 THEN 'Loyal Customers'
        WHEN r_score <= 2 AND f_score >= 2 THEN 'At Risk'
        ELSE 'Potential / Hibernating'
    END AS kunden_segment
FROM rfm_scored
ORDER BY monetary DESC;

-- 🎯 TODO 4: Executive Business Intelligence View
DROP VIEW IF EXISTS v_executive_kpi_dashboard;
CREATE VIEW v_executive_kpi_dashboard AS
SELECT 
    strftime('%Y-%m', order_date) AS monat,
    SUM(total_amount) AS monats_umsatz,
    COUNT(order_key) AS anzahl_bestellungen,
    COUNT(DISTINCT customer_key) AS aktive_kunden,
    ROUND(AVG(total_amount), 2) AS aov,
    LAG(SUM(total_amount), 1, 0) OVER (ORDER BY strftime('%Y-%m', order_date)) AS vormonat_umsatz,
    ROUND(
        (SUM(total_amount) - LAG(SUM(total_amount), 1, SUM(total_amount)) OVER (ORDER BY strftime('%Y-%m', order_date))) * 100.0 / 
        LAG(SUM(total_amount), 1, SUM(total_amount)) OVER (ORDER BY strftime('%Y-%m', order_date)),
        2
    ) AS mom_wachstum_pct,
    SUM(SUM(total_amount)) OVER (
        ORDER BY strftime('%Y-%m', order_date) 
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS kumulierter_allzeit_umsatz
FROM fact_orders
GROUP BY strftime('%Y-%m', order_date);
