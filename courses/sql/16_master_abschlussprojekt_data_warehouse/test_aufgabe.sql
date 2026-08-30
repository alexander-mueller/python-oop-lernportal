-- ============================================================================
-- 🧪 TESTSUITE FÜR SQL 16: MASTER DATA WAREHOUSE & ANALYTICS 🧪
-- ============================================================================

-- Test 1: Dimensions- und Faktencheck
SELECT 
    'TEST 1 (Warehouse Schema Validierung)' AS test_fall,
    (SELECT COUNT(*) FROM dim_customers) AS kunden_count,
    (SELECT COUNT(*) FROM dim_products) AS produkte_count,
    (SELECT COUNT(*) FROM fact_orders) AS orders_count;

-- Test 2: Kohorten-Matrix Retention Test (TODO 2)
WITH kunden_kohorte AS (
    SELECT customer_key, strftime('%Y-%m', MIN(order_date)) AS kohorte FROM fact_orders GROUP BY customer_key
),
kunden_aktivitaet AS (
    SELECT DISTINCT fo.customer_key, kk.kohorte, strftime('%Y-%m', fo.order_date) AS aktivitaets_monat
    FROM fact_orders fo JOIN kunden_kohorte kk ON fo.customer_key = kk.customer_key
),
kohorten_basis AS (
    SELECT kohorte, COUNT(DISTINCT customer_key) AS kohorten_groesse FROM kunden_kohorte GROUP BY kohorte
)
SELECT 
    'TEST 2 (Kohorten Retention)' AS test_fall,
    ka.kohorte,
    ka.aktivitaets_monat,
    COUNT(DISTINCT ka.customer_key) AS active_users,
    kb.kohorten_groesse,
    ROUND(COUNT(DISTINCT ka.customer_key) * 100.0 / kb.kohorten_groesse, 1) AS retention_pct
FROM kunden_aktivitaet ka
JOIN kohorten_basis kb ON ka.kohorte = kb.kohorte
GROUP BY ka.kohorte, ka.aktivitaets_monat, kb.kohorten_groesse
ORDER BY ka.kohorte ASC, ka.aktivitaets_monat ASC;

-- Test 3: RFM-Segmentierungs Test (TODO 3)
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
        monetary,
        NTILE(4) OVER (ORDER BY recency_tage DESC) AS r_score,
        NTILE(4) OVER (ORDER BY frequency ASC) AS f_score,
        NTILE(4) OVER (ORDER BY monetary ASC) AS m_score
    FROM rfm_raw
)
SELECT 
    'TEST 3 (RFM Segmentierung)' AS test_fall,
    customer_key,
    kunden_name,
    monetary,
    CASE 
        WHEN r_score >= 3 AND f_score >= 3 AND m_score >= 3 THEN 'Champions'
        WHEN f_score >= 3 THEN 'Loyal Customers'
        WHEN r_score <= 2 AND f_score >= 2 THEN 'At Risk'
        ELSE 'Potential / Hibernating'
    END AS kunden_segment
FROM rfm_scored
ORDER BY monetary DESC;

-- Test 4: Executive KPI Dashboard View (TODO 4)
SELECT 
    'TEST 4 (Executive BI View)' AS test_fall,
    monat,
    monats_umsatz,
    anzahl_bestellungen,
    aktive_kunden,
    aov,
    kumulierter_allzeit_umsatz
FROM v_executive_kpi_dashboard
ORDER BY monat ASC;
