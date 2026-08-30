# SQL 14: ACID Transaktionen, COMMIT, ROLLBACK & Savepoints 🛡️🏦

Willkommen zu **Modul 14 (Lehrpfad 4: Performance, Transaktionen & Analytics Master)**!
In Unternehmensdatenbanken darf niemals ein fehlerhafter Zwischenzustand persistiert werden. In diesem Modul lernst du Transaktionskontrolle (TCL - Transaction Control Language), die 4 Säulen des ACID-Prinzips und die sichere Handhabung von Savepoints.

---

## 🎯 Lernziele

1. **ACID-Prinzipien**: Atomicity, Consistency, Isolation und Durability in relationalen Datenbanken.
2. **`BEGIN TRANSACTION` & `COMMIT`**: Bündeln mehrerer DML-Statements zu einer unteilbaren Einheit.
3. **`ROLLBACK`**: Automatisches oder manuelles Verwerfen aller Änderungen bei Fehlern.
4. **`SAVEPOINT` & `ROLLBACK TO`**: Schrittweises Speichern und gezieltes Zurückrollen innerhalb aktiver Transaktionen.
5. **Datenintegrität & Bilanzprüfungen**: Validieren von Gesamtsummen und Vermeiden von Phantom-/Inkonsistenz-Zuständen.

---

## 💡 Wie Savepoints funktionieren

```sql
BEGIN TRANSACTION;
-- 1. Gültiger Hauptschritt
INSERT INTO bestellungen (id, status) VALUES (1, 'in Bearbeitung');

-- 2. Zwischenspeicherpunkt anlegen
SAVEPOINT sp_rabatt;

-- 3. Versuch, einen Gutschein anzuwenden
UPDATE bestellungen SET rabatt = 50 WHERE id = 1;

-- Falls der Gutschein abgelaufen ist -> Zurück zum Savepoint:
ROLLBACK TO SAVEPOINT sp_rabatt;

-- 4. Transaktion abschließen
COMMIT;
```

---

## 🚀 Aufgabenstellung (`aufgabe.sql`)

1. **TODO 1: Erfolgreiche Überweisung mit COMMIT** – Überweise 300 € von Konto 1 auf Konto 2 und logge den Transfer.
2. **TODO 2: Transaktionsabbruch mit ROLLBACK** – Simuliere eine ungedeckte Abbuchung und mache alles rückgängig.
3. **TODO 3: Partieller Rollback mit SAVEPOINT** – Führe eine Reservierung durch, rolle einen fehlerhaften Folgeschritt zurück und committe die Reservierung.
4. **TODO 4: Konsistenz-Audit** – Prüfe, ob die Bilanzsumme aller Bankkonten nach den Transaktionen unverändert 4.000 € beträgt.

---

## 🧪 Tests ausführen

Validierung erfolgt über `test_aufgabe.sql`.
