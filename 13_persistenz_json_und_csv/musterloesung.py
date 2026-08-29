"""
Kapitel 13: Datei-Persistenz (JSON & CSV) 💾📁
==============================================
Musterlösung für JSON- und CSV-Persistenz in Python OOP.
"""

import json
import csv
from pathlib import Path
from typing import List, Optional, Dict, Any


# ==============================================================================
# 1. Klasse Spieler mit to_dict / from_dict
# ==============================================================================
class Spieler:
    def __init__(self, name: str, level: int, punkte: int, inventar: Optional[List[str]] = None):
        """Initialisiert ein Spieler-Objekt."""
        self.name: str = name
        self.level: int = int(level)
        self.punkte: int = int(punkte)
        self.inventar: List[str] = list(inventar) if inventar is not None else []

    def to_dict(self) -> Dict[str, Any]:
        """Konvertiert das Objekt in ein speicherbares Dictionary."""
        return {
            "name": self.name,
            "level": self.level,
            "punkte": self.punkte,
            "inventar": self.inventar,
        }

    @classmethod
    def from_dict(cls, daten: Dict[str, Any]) -> "Spieler":
        """Erstellt ein neues Spieler-Objekt aus einem Dictionary."""
        return cls(
            name=daten["name"],
            level=int(daten["level"]),
            punkte=int(daten["punkte"]),
            inventar=list(daten.get("inventar", [])),
        )

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
# 2. Klasse Spielstand mit JSON & CSV Persistenz
# ==============================================================================
class Spielstand:
    def __init__(self, titel: str = "Neuer Spielstand"):
        """Initialisiert einen Spielstand mit Titel und leerer Spielerliste."""
        self.titel: str = titel
        self.spieler_liste: List[Spieler] = []

    def spieler_hinzufuegen(self, spieler: Spieler) -> None:
        """Fügt einen Spieler hinzu."""
        self.spieler_liste.append(spieler)

    def spieler_suchen(self, name: str) -> Optional[Spieler]:
        """Findet einen Spieler anhand seines Namens."""
        for s in self.spieler_liste:
            if s.name == name:
                return s
        return None

    def bester_spieler(self) -> Optional[Spieler]:
        """Gibt den Spieler mit der höchsten Punktzahl zurück."""
        if not self.spieler_liste:
            return None
        return max(self.spieler_liste, key=lambda s: s.punkte)

    def speichern_als_json(self, dateipfad: str | Path) -> None:
        """Speichert den gesamten Zustand als JSON auf der Festplatte."""
        pfad = Path(dateipfad)
        daten = {
            "titel": self.titel,
            "spieler": [s.to_dict() for s in self.spieler_liste],
        }
        with open(pfad, "w", encoding="utf-8") as f:
            json.dump(daten, f, indent=4, ensure_ascii=False)

    def laden_aus_json(self, dateipfad: str | Path) -> None:
        """Lädt den Spielstand aus einer JSON-Datei."""
        pfad = Path(dateipfad)
        with open(pfad, "r", encoding="utf-8") as f:
            daten = json.load(f)

        self.titel = daten.get("titel", self.titel)
        spieler_rohdaten = daten.get("spieler", [])
        self.spieler_liste = [Spieler.from_dict(d) for d in spieler_rohdaten]

    def exportiere_als_csv(self, dateipfad: str | Path) -> None:
        """Exportiert eine tabellarische Zusammenfassung als CSV-Datei."""
        pfad = Path(dateipfad)
        feldnamen = ["name", "level", "punkte", "inventar_anzahl"]

        with open(pfad, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=feldnamen)
            writer.writeheader()
            for s in self.spieler_liste:
                writer.writerow({
                    "name": s.name,
                    "level": s.level,
                    "punkte": s.punkte,
                    "inventar_anzahl": len(s.inventar),
                })

    def importiere_aus_csv(self, dateipfad: str | Path) -> int:
        """Importiert Spieler aus einer CSV-Datei."""
        pfad = Path(dateipfad)
        importierte_anzahl = 0

        with open(pfad, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for zeile in reader:
                neuer_spieler = Spieler(
                    name=zeile["name"],
                    level=int(zeile["level"]),
                    punkte=int(zeile["punkte"]),
                    inventar=[]
                )
                self.spieler_hinzufuegen(neuer_spieler)
                importierte_anzahl += 1

        return importierte_anzahl


if __name__ == "__main__":
    spielstand = Spielstand("Musterloesung Spielstand")
    spielstand.spieler_hinzufuegen(Spieler("Gandalf", 99, 99999, ["Stab", "Ring"]))
    spielstand.speichern_als_json("test_muster.json")
    print("Erfolgreich ausgeführt!")
