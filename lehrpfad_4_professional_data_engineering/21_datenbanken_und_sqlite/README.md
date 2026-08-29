# Kapitel 21: Relationale Datenbanken & SQLite (sqlite3) 🗄️⚡

In diesem Kapitel lernst du, wie du strukturierte relationale Datenbanken mit Pythons eingebautem Modul `sqlite3` erstellst, verwaltest und sicher abfragst.

---

## 🎯 Was du lernst

1. **Relationale Datenbanken vs. Einfache Textdateien:** Warum relationale Datenbanken (Tabellen, Primärschlüssel, Relationen) für große Datenmengen und gleichzeitigen Zugriff unverzichtbar sind.
2. **Die Aktenschrank-Analogie:**
   - **Datenbankdatei:** Der Aktenschrank.
   - **Tabelle:** Eine Schublade mit Registerkarten.
   - **Spalte (Column):** Ein vorgegebenes Feld auf der Registerkarte (z.B. Name, E-Mail, Guthaben).
   - **Zeile (Row/Record):** Eine einzelne ausgefüllte Registerkarte (ein Kunde).
3. **Verbindung & Cursor:**
   ```python
   import sqlite3
   
   conn = sqlite3.connect("kunden.db")  # oder ":memory:" für flüchtige RAM-Datenbank
   conn.row_factory = sqlite3.Row      # Zugriff per Spaltennamen wie im Dict!
   cursor = conn.cursor()
   ```
4. **CRUD-Operationen in SQL:**
   - **C**reate: `CREATE TABLE IF NOT EXISTS ...` und `INSERT INTO ...`
   - **R**ead: `SELECT ... FROM ... WHERE ...`
   - **U**pdate: `UPDATE ... SET ... WHERE ...`
   - **D**elete: `DELETE FROM ... WHERE ...`
5. **Transaktionen & Persistenz:** Warum Änderungen erst nach `conn.commit()` dauerhaft auf der Festplatte gespeichert werden.
6. **Sicherheit & SQL-Injection-Schutz:** Niemals Strings formatieren (`f"SELECT ... {user_input}"`), sondern immer Platzhalter (`?`) verwenden!

---

## 📁 Die Dateien in diesem Ordner

- **`index.html`**: Die interaktive Lernseite mit Aktenschrank-Analogie, SQL-Cheat-Sheet, Injection-Demo und Subgoals.
- **`aufgabe.py`**: Dein Arbeitsblatt mit der Klasse `KundenDatenbank`.
- **`test_aufgabe.py`**: Automatische Unittest-Suite (`python3 test_aufgabe.py`).
- **`musterloesung.py`**: Vollständig ausprogrammierte Beispiellösung.

---

## 🚀 Schnellstart

```bash
# 1. Bearbeite aufgabe.py
# 2. Teste deine Lösung:
python3 test_aufgabe.py
```
