# SQL 09: Aggregationen (COUNT/SUM) & GROUP BY 📊

Willkommen zu **Modul 09 (Lehrpfad 3: Aggregationen, CTEs & Window Functions)**!
In diesem Modul meisterst du das Fundament moderner Data Analytics & Business Intelligence: Das Zusammenfassen von Einzeltransaktionen zu wertvollen Geschäftskennzahlen.

---

## 🎯 Lernziele

1. **Aggregatfunktionen**: Zeilenübergreifende Berechnungen mit `COUNT(*)`, `COUNT(DISTINCT ...)`, `SUM()`, `AVG()`, `MIN()` und `MAX()`.
2. **`GROUP BY`**: Gruppieren von Rohdaten nach Kategorien, Kunden, Zeiträumen und Regionen.
3. **`HAVING` vs. `WHERE`**: Verstehen des kritischen Unterschieds zwischen Zeilenfiltern (vor der Aggregation) und Gruppenfiltern (nach der Aggregation).
4. **Multi-Column Grouping**: Mehrdimensionale Analysen über mehrere Dimensionen (z.B. Stadt + Produktkategorie).
5. **Zeit-Aggregation**: Aggregieren von Transaktionsdaten nach Monaten mit `strftime('%Y-%m', datum)`.

---

## 💡 Kernkonzepte & Syntax

### 1. Zeilen filtern vs. Gruppen filtern (WHERE vs. HAVING)

Ein häufiger Denkfehler in SQL ist die Verwendung von Aggregaten in der `WHERE`-Klausel. Dies führt zu einem Syntaxfehler!

- `WHERE`: Filtert Zeilen **bevor** gruppiert wird. (z.B. `WHERE status = 'abgeschlossen'`)
- `GROUP BY`: Fasst gleiche Werte in Gruppen zusammen. (z.B. `GROUP BY kunde_id`)
- `HAVING`: Filtert die aggregierten Gruppen **nach** der Berechnung. (z.B. `HAVING SUM(gesamtbetrag) > 1000`)

```sql
SELECT 
    k.stadt,
    COUNT(b.id) AS anzahl_bestellungen,
    SUM(b.gesamtbetrag) AS umsatz_stadt
FROM kunden k
JOIN bestellungen b ON k.id = b.kunde_id
WHERE b.status = 'abgeschlossen'
GROUP BY k.stadt
HAVING SUM(b.gesamtbetrag) >= 500
ORDER BY umsatz_stadt DESC;
```

---

## 🚀 Aufgabenstellung (`aufgabe.sql`)

1. **TODO 1: Kategorie-Umsatz-Statistik** – Berechne pro Kategorie die Anzahl verkaufter Artikel, den Gesamtumsatz, den Durchschnittspreis sowie Min/Max-Preise.
2. **TODO 2: Top-Kunden mit HAVING** – Identifiziere Kunden mit mindestens 2 abgeschlossenen Bestellungen und einem Gesamtwert von mindestens 500 €.
3. **TODO 3: Monatlicher Umsatz-Report** – Gruppiere nach Monat (`strftime('%Y-%m', bestell_datum)`), berechne Bestellanzahl, Monatsumsatz und AOV (Average Order Value).
4. **TODO 4: Multi-Dimensionale Performance (Stadt & Kategorie)** – Gruppiere nach Stadt und Kategorie, zähle eindeutige Bestellungen und summiere den Umsatz mit `HAVING SUM(gesamtbetrag) > 300`.

---

## 🧪 Tests ausführen

Führe in der Web-IDE oder lokal deine Abfragen aus und validiere sie mit `test_aufgabe.sql`.
