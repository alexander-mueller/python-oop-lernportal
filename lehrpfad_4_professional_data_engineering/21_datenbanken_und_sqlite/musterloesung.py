"""
Kapitel 21: Relationale Datenbanken & SQLite (sqlite3) 🗄️⚡
=========================================================
Lehrpfad 4: Professional Data Engineering

Musterlösung für die KundenDatenbank mit SQLite3.
"""

import sqlite3
from typing import List, Optional, Dict, Any


class KundenDatenbank:
    """
    Vollständig implementierte KundenDatenbank mit sqlite3.
    """

    def __init__(self, db_pfad: str = ":memory:"):
        """
        Initialisiert die Datenbankverbindung und erstellt die Tabelle 'kunden'.
        """
        self.db_pfad = db_pfad
        self.conn = sqlite3.connect(db_pfad)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

        # Tabelle anlegen
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS kunden (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                guthaben REAL DEFAULT 0.0
            )
            """
        )
        self.conn.commit()

    def kunde_hinzufuegen(self, name: str, email: str, startguthaben: float = 0.0) -> int:
        """
        Fügt einen neuen Kunden per parametrisiertem INSERT ein.
        """
        self.cursor.execute(
            "INSERT INTO kunden (name, email, guthaben) VALUES (?, ?, ?)",
            (name, email, float(startguthaben))
        )
        self.conn.commit()
        return self.cursor.lastrowid

    def kunde_suchen_nach_id(self, kunden_id: int) -> Optional[Dict[str, Any]]:
        """
        Sucht einen Kunden anhand der ID und liefert ein Dictionary zurück.
        """
        self.cursor.execute(
            "SELECT id, name, email, guthaben FROM kunden WHERE id = ?",
            (kunden_id,)
        )
        row = self.cursor.fetchone()
        if row is None:
            return None
        return {
            "id": row["id"],
            "name": row["name"],
            "email": row["email"],
            "guthaben": float(row["guthaben"]),
        }

    def guthaben_aufladen(self, kunden_id: int, betrag: float) -> bool:
        """
        Erhöht das Guthaben eines Kunden um einen positiven Betrag.
        """
        if betrag <= 0:
            return False

        self.cursor.execute(
            "UPDATE kunden SET guthaben = guthaben + ? WHERE id = ?",
            (float(betrag), kunden_id)
        )
        self.conn.commit()
        return self.cursor.rowcount > 0

    def kunden_mit_mindestguthaben(self, min_guthaben: float) -> List[Dict[str, Any]]:
        """
        Liefert alle Kunden mit mindestens min_guthaben, sortiert absteigend.
        """
        self.cursor.execute(
            "SELECT id, name, email, guthaben FROM kunden WHERE guthaben >= ? ORDER BY guthaben DESC",
            (float(min_guthaben),)
        )
        rows = self.cursor.fetchall()
        return [
            {
                "id": r["id"],
                "name": r["name"],
                "email": r["email"],
                "guthaben": float(r["guthaben"]),
            }
            for r in rows
        ]

    def kunde_loeschen(self, kunden_id: int) -> bool:
        """
        Löscht einen Kunden anhand der ID.
        """
        self.cursor.execute(
            "DELETE FROM kunden WHERE id = ?",
            (kunden_id,)
        )
        self.conn.commit()
        return self.cursor.rowcount > 0

    def alle_kunden(self) -> List[Dict[str, Any]]:
        """
        Gibt eine Liste aller Kunden zurück.
        """
        self.cursor.execute("SELECT id, name, email, guthaben FROM kunden ORDER BY id ASC")
        rows = self.cursor.fetchall()
        return [
            {
                "id": r["id"],
                "name": r["name"],
                "email": r["email"],
                "guthaben": float(r["guthaben"]),
            }
            for r in rows
        ]

    def schliessen(self) -> None:
        """Schließt die Verbindung."""
        if hasattr(self, "conn") and self.conn:
            self.conn.close()


if __name__ == "__main__":
    db = KundenDatenbank(":memory:")
    i1 = db.kunde_hinzufuegen("Max Mustermann", "max@test.de", 100.0)
    print("Kunde hinzugefügt mit ID:", i1)
    print("Kunde gesucht:", db.kunde_suchen_nach_id(i1))
    db.schliessen()
