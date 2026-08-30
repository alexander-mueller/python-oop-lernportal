# SQL 15: Virtuelle Views & Trigger 👁️⚡

Willkommen zu **Modul 15 (Lehrpfad 4: Performance, Transaktionen & Analytics Master)**!
In Unternehmensarchitekturen müssen komplexe Abfragen für BI-Tools vereinfacht und geschäftskritische Regeln automatisiert werden. In diesem Modul lernst du virtuelle Views (`CREATE VIEW`) und reaktive Datenbank-Trigger (`CREATE TRIGGER`).

---

## 🎯 Lernziele

1. **Virtuelle Sichten (`CREATE VIEW`)**: Kapseln komplexer Multi-Tabellen-Joins und Aggregationen in saubere, wiederverwendbare Schnittstellen.
2. **Daten-Sicherheit & Maskierung**: Ausblenden sensibler Spalten (wie Passwort-Hashes oder PII) über spezialisierte Views.
3. **Event-Driven Database Triggers (`CREATE TRIGGER`)**: Automatisches Ausführen von SQL-Logik bei `INSERT`, `UPDATE` oder `DELETE`.
4. **`NEW` und `OLD` Pseudotabellen**: Verarbeiten veränderter Datensätze vor und nach DML-Operationen.
5. **Revisionssichere Audit-Trails**: Automatisches Protokollieren von Preisänderungen für Compliance & Rechnungsprüfung.

---

## 💡 Syntax im Detail

```sql
-- Trigger zur Bestandsreduzierung
CREATE TRIGGER trg_lager_update
AFTER INSERT ON bestellpositionen
FOR EACH ROW
BEGIN
    UPDATE produkte 
    SET lagerbestand = lagerbestand - NEW.menge 
    WHERE id = NEW.produkt_id;
END;
```

---

## 🚀 Aufgabenstellung (`aufgabe.sql`)

1. **TODO 1: View `v_kunden_bestell_cockpit`** – Erstelle ein Aggregations-Cockpit für Kundendaten ohne sensitive Passwortspalten.
2. **TODO 2: View `v_top_seller_uebersicht`** – Erstelle einen Top-Seller-Report für Produkte.
3. **TODO 3: Trigger `trg_lagerbestand_reduzieren`** – Aktualisiere bei jedem `INSERT ON bestellpositionen` automatisch den Lagerbestand.
4. **TODO 4: Trigger `trg_preis_historie_audit`** – Schreibe bei jeder Preisänderung auf `produkte` einen Historien-Eintrag in `audit_preis_historie`.

---

## 🧪 Tests ausführen

Validierung erfolgt über `test_aufgabe.sql`.
