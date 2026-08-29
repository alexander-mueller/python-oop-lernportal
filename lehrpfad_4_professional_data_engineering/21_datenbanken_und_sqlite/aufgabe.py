"""
Kapitel 21: Relationale Datenbanken & SQLite (sqlite3) 🗄️⚡
=========================================================
Lehrpfad 4: Professional Data Engineering

Thema:
Relationales Datenmanagement mit SQLite und Pythons eingebautem Modul `sqlite3`.

Lernziele:
1. Verbindungsaufbau mit `sqlite3.connect()` und Arbeiten mit dem Cursor `conn.cursor()`.
2. Tabellen definieren mit `CREATE TABLE IF NOT EXISTS`.
3. Datensätze einfügen mit `INSERT INTO` und `conn.commit()`.
4. Daten gezielt abfragen mit `SELECT ... WHERE` und `fetchall()` / `fetchone()`.
5. Datensätze aktualisieren mit `UPDATE ... SET` und löschen mit `DELETE FROM`.
6. Schutz vor SQL-Injections durch parametrisierte Abfragen (`?`).
7. Verwendung von `row_factory = sqlite3.Row` für benannte Spaltenzugriffe.
"""

import sqlite3
from typing import List, Optional, Dict, Any


class KundenDatenbank:
    """
    Verwaltet Kundenkonten und Guthaben in einer relationalen SQLite-Datenbank.
    """

    def __init__(self, db_pfad: str = ":memory:"):
        """
        Initialisiert die Datenbankverbindung und erstellt die Tabelle 'kunden',
        falls sie noch nicht existiert.
        
        Tabelle 'kunden':
            - id: INTEGER PRIMARY KEY AUTOINCREMENT
            - name: TEXT NOT NULL
            - email: TEXT NOT NULL UNIQUE
            - guthaben: REAL DEFAULT 0.0
            
        Tipps:
            - self.db_pfad = db_pfad
            - self.conn = sqlite3.connect(db_pfad)
            - self.conn.row_factory = sqlite3.Row  # Ermöglicht dict-artigen Zugriff
            - self.cursor = self.conn.cursor()
            - Führe den CREATE TABLE Befehl mit self.cursor.execute(...) aus
            - Führe self.conn.commit() aus
        """
        # TODO: Implementieren
        pass

    def kunde_hinzufuegen(self, name: str, email: str, startguthaben: float = 0.0) -> int:
        """
        Fügt einen neuen Kunden in die Datenbank ein.
        
        WICHTIG:
        - Verwende IMMER parametrisierte SQL-Queries mit '?' gegen SQL-Injections!
        - SQL: "INSERT INTO kunden (name, email, guthaben) VALUES (?, ?, ?)"
        - Führe nach dem INSERT self.conn.commit() auf.
        
        Rückgabewert:
            - Die automatisch vergebene ID des neuen Kunden (int) via self.cursor.lastrowid
        """
        # TODO: Implementieren
        pass

    def kunde_suchen_nach_id(self, kunden_id: int) -> Optional[Dict[str, Any]]:
        """
        Sucht einen Kunden anhand seiner ID.
        
        SQL:
            "SELECT id, name, email, guthaben FROM kunden WHERE id = ?"
        
        Rückgabewert:
            - Ein Dictionary mit den Spalten als Keys:
              {"id": row["id"], "name": row["name"], "email": row["email"], "guthaben": row["guthaben"]}
            - None, falls kein Kunde mit dieser ID gefunden wurde.
        """
        # TODO: Implementieren
        pass

    def guthaben_aufladen(self, kunden_id: int, betrag: float) -> bool:
        """
        Lädt das Guthaben eines bestehenden Kunden um den angegebenen Betrag auf.
        
        Bedingungen:
        - betrag muss größer als 0 sein (andernfalls direkt False zurückgeben).
        - SQL: "UPDATE kunden SET guthaben = guthaben + ? WHERE id = ?"
        - Führe self.conn.commit() aus.
        
        Rückgabewert:
            - True, wenn der Datensatz aktualisiert wurde (self.cursor.rowcount > 0).
            - False, wenn kein Kunde mit dieser ID existiert oder betrag <= 0 ist.
        """
        # TODO: Implementieren
        pass

    def kunden_mit_mindestguthaben(self, min_guthaben: float) -> List[Dict[str, Any]]:
        """
        Gibt alle Kunden zurück, deren Guthaben >= min_guthaben ist.
        Sortiert nach Guthaben absteigend (höchstes Guthaben zuerst).
        
        SQL:
            "SELECT id, name, email, guthaben FROM kunden WHERE guthaben >= ? ORDER BY guthaben DESC"
        
        Rückgabewert:
            - Liste von Dictionaries der passenden Kunden.
              [{"id": ..., "name": ..., "email": ..., "guthaben": ...}, ...]
        """
        # TODO: Implementieren
        pass

    def kunde_loeschen(self, kunden_id: int) -> bool:
        """
        Löscht einen Kunden anhand seiner ID aus der Datenbank.
        
        SQL:
            "DELETE FROM kunden WHERE id = ?"
        
        Rückgabewert:
            - True, wenn ein Kunde gelöscht wurde (self.cursor.rowcount > 0).
            - False, wenn kein Kunde mit dieser ID existierte.
        """
        # TODO: Implementieren
        pass

    def alle_kunden(self) -> List[Dict[str, Any]]:
        """
        Gibt eine Liste aller Kunden zurück.
        """
        # TODO: Implementieren
        pass

    def schliessen(self) -> None:
        """Schließt die Datenbankverbindung."""
        if hasattr(self, "conn") and self.conn:
            self.conn.close()


# ==============================================================================
# Interaktiver Test im Terminal:
# (python3 aufgabe.py)
# ==============================================================================
if __name__ == "__main__":
    print("🗄️ Initialisiere KundenDatenbank im Arbeitsspeicher (:memory:)...")
    db = KundenDatenbank(":memory:")

    # 1. Kunden anlegen
    id1 = db.kunde_hinzufuegen("Alice Schmidt", "alice@example.com", 150.0)
    id2 = db.kunde_hinzufuegen("Bob Müller", "bob@example.com", 50.0)
    id3 = db.kunde_hinzufuegen("Charlie Braun", "charlie@example.com", 320.0)
    print(f"Kunden erstellt: IDs = {id1}, {id2}, {id3}")

    # 2. Kunde suchen
    kunde = db.kunde_suchen_nach_id(id1)
    print(f"Gefundener Kunde: {kunde}")

    # 3. Guthaben aufladen
    erfolg = db.guthaben_aufladen(id2, 100.0)
    print(f"Guthaben von Bob aufgeladen: {erfolg} -> Neuer Stand: {db.kunde_suchen_nach_id(id2)}")

    # 4. Mindestguthaben filtern
    reiche_kunden = db.kunden_mit_mindestguthaben(140.0)
    print(f"Kunden mit mind. 140€ Guthaben: {reiche_kunden}")

    # 5. Kunde löschen
    db.kunde_loeschen(id3)
    print(f"Nach Löschen von Charlie: {db.alle_kunden()}")

    db.schliessen()
    print("Fertig!")
