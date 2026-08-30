# Master 16: E-Commerce Analytics Data Warehouse 💎⭐

Herzlichen Glückwunsch zum Erreichen des **Master-Abschlussprojekts (Modul 16)** im SQL-Kurs!
In diesem Abschlussprojekt führst du alle Techniken aus den Lehrpfaden 1 bis 4 zu einem produktionsreifen Enterprise Data Warehouse für moderne E-Commerce-Analytik zusammen.

---

## 💡 1. Das Projekt im Überblick

Das Analytics Data Warehouse bildet das Rückgrat moderner datengetriebener Unternehmen:

1. **Dimensionales Sternschema (Star Schema)**:
   - Dimensionen: `dim_customers`, `dim_products`, `dim_dates`, `dim_channels`
   - Fakten: `fact_orders`, `fact_order_items`
2. **Robuste ETL / ELT Transformationen**:
   - Bereinigung und Laden von operativen Rohdaten in das analytische Modell.
3. **Kohorten-Retention-Matrix (Cohort Retention Analysis)**:
   - Gruppierung von Kunden nach ihrem Akquisitionsmonat und Nachverfolgung der Aktivität über Folgemonate ($t+0, t+1, t+2$).
4. **RFM-Kundensegmentierung (Recency, Frequency, Monetary Value)**:
   - Segmentierung der Kundenbasis über `NTILE(4)` Window Functions in *Champions*, *Loyal Customers*, *At Risk* und *Lost*.
5. **Executive Business Intelligence Dashboard**:
   - Erstellung des Views `v_executive_kpi_dashboard` mit Key Performance Indicators: Umsatz, MoM-Wachstum (via `LAG`), Average Order Value (AOV) und Lifetime-Trajectory (via `SUM() OVER`).

---

## 🏗️ 2. Star Schema Architektur

```text
[dim_customers] ────────┐
                        │
[dim_products]  ────────┼──▶ [ fact_orders ] ◀── [dim_channels]
                        │
[dim_dates]     ────────┘
```

---

## 🎯 Aufgaben in `aufgabe.sql`

- **TODO 1: Sternschema & DDL**: Anlegen der Dimensionstabellen und Faktentabellen mit Foreign Keys und B-Tree Indizes.
- **TODO 2: Kohorten-Retention-Matrix**: Mehrstufige CTE-Pipeline zur Berechnung der Monat-zu-Monat Retention Rate in %.
- **TODO 3: RFM-Segmentierung**: Berechnung der RFM-Scores und Zuweisung zielgerichteter Kundensegmente via `CASE WHEN`.
- **TODO 4: Executive KPI Dashboard View**: Erstellung von `v_executive_kpi_dashboard` mit Window Functions und Trendberechnungen.

---

## 🧪 Tests ausführen

Validierung erfolgt über `test_aufgabe.sql`.
