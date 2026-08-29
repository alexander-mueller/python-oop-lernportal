"""
Kapitel 13: Datei-Persistenz (JSON & CSV) 💾📁
==============================================
Schulabgleich: 14.0 CSV & Dateien / Savegame-Persistenz

Aufgabe:
Implementiere ein modulares Savegame- und Highscore-System:
1. Klasse 'Spieler': mit Serialisierung (to_dict, from_dict).
2. Klasse 'Spielstand': mit JSON-Speichern/Laden und CSV-Tabellen-Export.
"""

import json
import csv
from pathlib import Path
from typing import List, Optional, Dict, Any


# ==============================================================================
# 🎯 TEILZIEL 1 (TODO 1): Klasse Spieler mit Serialisierung
# ==============================================================================
class Spieler:
    def __init__(self, name: str, level: int, punkte: int, inventar: Optional[List[str]] = None):
        """
        Initialisiert einen Spieler.
        Attribute:
            - self.name: str = name
            - self.level: int = int(level)
            - self.punkte: int = int(punkte)
            - self.inventar: list[str] = inventar (oder [] falls None)
        """
        # TODO: Implementieren
        pass

    def to_dict(self) -> Dict[str, Any]:
        """
        Wandelt das Spieler-Objekt in ein Dictionary um, damit es als JSON
        gespeichert werden kann.
        
        Rückgabe-Format:
        {
            "name": self.name,
            "level": self.level,
            "punkte": self.punkte,
            "inventar": self.inventar
        }
        """
        # TODO: Implementieren
        pass

    @classmethod
    def from_dict(cls, daten: Dict[str, Any]) -> "Spieler":
        """
        Erstellt ein neues Spieler-Objekt aus einem Dictionary.
        Beispiel: Spieler.from_dict({"name": "Alex", "level": 5, "punkte": 1200, "inventar": ["Schwert"]})
        """
        # TODO: Implementieren
        pass

    def __repr__(self) -> str:
        return f"Spieler(name='{self.name}', level={self.level}, punkte={self.punkte}, inventar={self.inventar})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Spieler):
            return False
        return (
            self.name == other.name
            and self.level == other.level
            and self.punkte == other.punkte
            and self.inventar == other.inventar
        )


# ==============================================================================
# 🎯 TEILZIEL 2 (TODO 2): Klasse Spielstand mit JSON- und CSV-Persistenz
# ==============================================================================
class Spielstand:
    def __init__(self, titel: str = "Neuer Spielstand"):
        """
        Initialisiert einen Spielstand.
        Attribute:
            - self.titel: str = titel
            - self.spieler_liste: list[Spieler] = []
        """
        # TODO: Implementieren
        pass

    def spieler_hinzufuegen(self, spieler: Spieler) -> None:
        """Fügt ein Spieler-Objekt zur internen Spieler-Liste hinzu."""
        # TODO: Implementieren
        pass

    def spieler_suchen(self, name: str) -> Optional[Spieler]:
        """
        Sucht einen Spieler nach Name.
        Gibt das gefundene Spieler-Objekt zurück oder None, wenn nicht vorhanden.
        """
        # TODO: Implementieren
        pass

    def bester_spieler(self) -> Optional[Spieler]:
        """
        Gibt den Spieler mit den meisten Punkten zurück.
        Gibt None zurück, wenn die Liste leer ist.
        """
        # TODO: Implementieren
        pass

    def speichern_als_json(self, dateipfad: str | Path) -> None:
        """
        Speichert den gesamten Spielstand als formatierte JSON-Datei ab.
        
        Struktur der JSON-Datei:
        {
            "titel": self.titel,
            "spieler": [
                { "name": ..., "level": ..., "punkte": ..., "inventar": [...] },
                ...
            ]
        }
        
        WICHTIG:
        - Nutze 'with open(dateipfad, "w", encoding="utf-8") as f:'
        - Nutze 'json.dump(daten, f, indent=4, ensure_ascii=False)'
        """
        # TODO: Implementieren
        pass

    def laden_aus_json(self, dateipfad: str | Path) -> None:
        """
        Lädt den Spielstand aus einer JSON-Datei und stellt alle Spieler wieder her.
        
        Ablauf:
        1. Öffne die Datei mit 'with open(dateipfad, "r", encoding="utf-8") as f:'
        2. Lade die Daten mit 'json.load(f)'
        3. Setze self.titel auf den geladenen Titel
        4. Erstelle für jeden Eintrag in der Spieler-Liste ein neues Spieler-Objekt
           mittels 'Spieler.from_dict(d)' und weise die neue Liste 'self.spieler_liste' zu.
        """
        # TODO: Implementieren
        pass

    def exportiere_als_csv(self, dateipfad: str | Path) -> None:
        """
        Exportiert eine Tabellen-Übersicht aller Spieler als CSV-Datei.
        
        Spalten (Header):
        ["name", "level", "punkte", "inventar_anzahl"]
        
        WICHTIG:
        - Nutze 'with open(dateipfad, "w", newline="", encoding="utf-8") as f:'
        - Nutze 'csv.DictWriter(f, fieldnames=...)'
        - Schreibe zuerst den Header mit 'writer.writeheader()'
        - Schreibe dann für jeden Spieler eine Zeile (inventar_anzahl = len(s.inventar))
        """
        # TODO: Implementieren
        pass

    def importiere_aus_csv(self, dateipfad: str | Path) -> int:
        """
        Liest Spieler aus einer CSV-Datei ein und fügt sie zur spieler_liste hinzu.
        (Hinweis: Das Inventar wird beim einfachen CSV-Import als leere Liste [] initialisiert).
        
        Gibt die Anzahl der neu importierten Spieler zurück.
        """
        # TODO: Implementieren
        pass


# ==============================================================================
# Kleiner Test zum Ausprobieren im Terminal:
# (python3 aufgabe.py)
# ==============================================================================
if __name__ == "__main__":
    spielstand = Spielstand("Highscore-Tabelle RPG")

    p1 = Spieler("Arthur", 12, 4500, ["Excalibur", "Heiltrank"])
    p2 = Spieler("Morgana", 15, 6200, ["Zauberstab", "Manatrank", "Schriftrolle"])
    p3 = Spieler("Lancelot", 10, 3800, ["Schild"])

    spielstand.spieler_hinzufuegen(p1)
    spielstand.spieler_hinzufuegen(p2)
    spielstand.spieler_hinzufuegen(p3)

    print("Bester Spieler:", spielstand.bester_spieler())

    # JSON Test
    json_pfad = Path("test_savegame.json")
    spielstand.speichern_als_json(json_pfad)
    print(f"Gespeichert in {json_pfad}!")

    # CSV Test
    csv_pfad = Path("test_export.csv")
    spielstand.exportiere_als_csv(csv_pfad)
    print(f"Exportiert nach {csv_pfad}!")
