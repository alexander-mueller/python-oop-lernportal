"""
🎮 PERSISTENTES GAMIFICATION-SYSTEM FÜR PYTHON LERNPORTAL 🎮
============================================================
Wissenschaftlich fundiert nach der Selbstbestimmungstheorie (Deci & Ryan)
und dem Octalysis-Framework (Yu-kai Chou).

Funktionsweise:
- Speichert den Spielstand lokal in '.gamification.json'.
- Schreibt zusätzlich 'assets/gamification_data.js', damit index.html auch
  ohne Webserver (per Doppelklick / file://) ohne CORS-Probleme darauf zugreifen kann!
- Verwaltet XP, Level-Aufstiege, Streaks und 14 didaktische Trophäen (Badges).
"""

import json
import os
from datetime import datetime, date
from pathlib import Path
from typing import Dict, List, Any, Optional

ROOT_DIR = Path(__file__).parent.resolve()
DATA_JSON_PATH = ROOT_DIR / ".gamification.json"
DATA_JS_PATH = ROOT_DIR / "assets" / "gamification_data.js"

# 10 Entwickler-Level mit XP-Schwellen und Titeln
LEVEL_STUFEN = [
    {"level": 1, "min_xp": 0, "max_xp": 150, "titel": "Code-Küken 🐣", "rang": "Bronze I"},
    {"level": 2, "min_xp": 151, "max_xp": 400, "titel": "Code-Detektivin 🔍", "rang": "Bronze II"},
    {"level": 3, "min_xp": 401, "max_xp": 800, "titel": "Logik-Bastlerin ⚙️", "rang": "Silber I"},
    {"level": 4, "min_xp": 801, "max_xp": 1300, "titel": "Klassen-Baumeisterin 🏗️", "rang": "Silber II"},
    {"level": 5, "min_xp": 1301, "max_xp": 2000, "titel": "Git-Strategin 🌿", "rang": "Gold I"},
    {"level": 6, "min_xp": 2001, "max_xp": 2900, "titel": "TDD-Qualitätsprüferin 🧪", "rang": "Gold II"},
    {"level": 7, "min_xp": 2901, "max_xp": 4000, "titel": "Vererbungs-Meisterin 🧬", "rang": "Platin I"},
    {"level": 8, "min_xp": 4001, "max_xp": 5300, "titel": "Exception-Wächterin 🛡️", "rang": "Platin II"},
    {"level": 9, "min_xp": 5301, "max_xp": 6800, "titel": "GUI-Entwicklerin 🖥️", "rang": "Diamant"},
    {"level": 10, "min_xp": 6801, "max_xp": 99999, "titel": "Software-Architektin 🏆", "rang": "Großmeisterin"},
]

# 14 freischaltbare Trophäen mit didaktischen Kriterien
BADGES_KATALOG = {
    "rechenkonegin": {
        "id": "rechenkonegin",
        "icon": "🧮",
        "name": "Rechenkönigin",
        "desc": "Grundlagen G01 & G02 abgeschlossen (Zahlen, Operatoren & Typen gemeistert).",
        "xp_bonus": 100,
        "kriterium": ["g01_erste_schritte_taschenrechner", "g02_variablen_und_datentypen"]
    },
    "dialog_profi": {
        "id": "dialog_profi",
        "icon": "💬",
        "name": "Dialog-Profi",
        "desc": "Grundlagen G03 abgeschlossen (Interaktive Ein-/Ausgabe mit f-Strings).",
        "xp_bonus": 75,
        "kriterium": ["g03_ein_und_ausgabe"]
    },
    "weichenstellerin": {
        "id": "weichenstellerin",
        "icon": "🚦",
        "name": "Weichenstellerin",
        "desc": "Grundlagen G04 abgeschlossen (Bedingungslogik & Schaltjahre gemeistert).",
        "xp_bonus": 75,
        "kriterium": ["g04_verzweigungen_und_bedingungen"]
    },
    "schleifen_dompteurin": {
        "id": "schleifen_dompteurin",
        "icon": "🎡",
        "name": "Schleifen-Dompteurin",
        "desc": "Grundlagen G05 abgeschlossen (While- & For-Schleifen gebändigt).",
        "xp_bonus": 100,
        "kriterium": ["g05_schleifen_und_wiederholungen"]
    },
    "funktions_zauberin": {
        "id": "funktions_zauberin",
        "icon": "🪄",
        "name": "Funktions-Zauberin",
        "desc": "Grundlagen G06 abgeschlossen (Eigene Funktionen & Module gebaut).",
        "xp_bonus": 100,
        "kriterium": ["g06_funktionen_und_module"]
    },
    "listen_archivarin": {
        "id": "listen_archivarin",
        "icon": "📋",
        "name": "Listen-Archivarin",
        "desc": "Grundlagen G07 & G08 abgeschlossen (Sequenzen & Strings analysiert).",
        "xp_bonus": 120,
        "kriterium": ["g07_listen_und_sequenzen", "g08_textverarbeitung_und_strings"]
    },
    "daten_strategin": {
        "id": "daten_strategin",
        "icon": "🗃️",
        "name": "Daten-Strategin",
        "desc": "Grundlagen G09 & G10 abgeschlossen (Dicts, Sets & Comprehensions gemeistert).",
        "xp_bonus": 150,
        "kriterium": ["g09_dictionaries_und_sets", "g10_comprehensions_datum_algorithmen"]
    },
    "bug_jaegerin": {
        "id": "bug_jaegerin",
        "icon": "🔍",
        "name": "Bug-Jägerin",
        "desc": "Kapitel 00 gelöst (Alle Fehler-Bugs im Warm-up aufgespürt).",
        "xp_bonus": 100,
        "kriterium": ["00_fehlersuche_und_grundlagen"]
    },
    "erste_architektin": {
        "id": "erste_architektin",
        "icon": "🏗️",
        "name": "Erste Architektin",
        "desc": "Kapitel 01 bis 03 gelöst (Erste OOP-Klassen, Konstruktoren & Methoden).",
        "xp_bonus": 200,
        "kriterium": ["01_einstieg_klassen", "02_init_und_self", "03_methoden_und_verhalten"]
    },
    "tamagotchi_mama": {
        "id": "tamagotchi_mama",
        "icon": "🥚",
        "name": "Tamagotchi-Mama",
        "desc": "Kapitel 06 Mini-Projekt abgeschlossen (Ein lebendiges Haustier gebaut).",
        "xp_bonus": 250,
        "kriterium": ["06_abschlussprojekt_tamagotchi"]
    },
    "zeit_reisende": {
        "id": "zeit_reisende",
        "icon": "🌿",
        "name": "Git-Zeitreisende",
        "desc": "Kapitel 04c Git-Versionskontrolle verstanden & Spielstände gesichert.",
        "xp_bonus": 100,
        "kriterium": ["04_str_und_darstellung"]
    },
    "qualitaets_garantin": {
        "id": "qualitaets_garantin",
        "icon": "🧪",
        "name": "TDD-Qualitätsgarantin",
        "desc": "Kapitel 09 abgeschlossen (Eigene professionelle Unit Tests geschrieben).",
        "xp_bonus": 200,
        "kriterium": ["09_eigene_unit_tests_schreiben"]
    },
    "oop_grossmeisterin": {
        "id": "oop_grossmeisterin",
        "icon": "🧬",
        "name": "Vererbungs-Koryphäe",
        "desc": "Kapitel 10 bis 12 abgeschlossen (Vererbung, Polymorphie & Exceptions).",
        "xp_bonus": 300,
        "kriterium": ["10_vererbung_und_super", "11_polymorphie_und_interfaces", "12_exceptions_und_fehlerbehandlung"]
    },
    "software_architektin": {
        "id": "software_architektin",
        "icon": "🏆",
        "name": "Meister-Entwicklerin",
        "desc": "Kapitel 16 Master-Projekt abgeschlossen & vollwertige Desktop-App gebaut!",
        "xp_bonus": 500,
        "kriterium": ["16_master_abschlussprojekt"]
    }
}


class GamificationManager:
    """Verwaltet den persistenten Gamification-Status."""

    def __init__(self):
        self.state = self._load_state()
        self.save_state()

    def _default_state(self) -> Dict[str, Any]:
        return {
            "spieler_name": "Python-Entwicklerin",
            "xp": 0,
            "level": 1,
            "titel": "Code-Küken 🐣",
            "rang": "Bronze I",
            "geloeste_kapitel": [],
            "bestandene_tests": 0,
            "freigeschaltete_badges": [],
            "streak_tage": 1,
            "letzter_aktiver_tag": str(date.today()),
            "historie": [],
            "zuletzt_aktualisiert": datetime.now().isoformat()
        }

    def _load_state(self) -> Dict[str, Any]:
        if DATA_JSON_PATH.exists():
            try:
                with open(DATA_JSON_PATH, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    return {**self._default_state(), **data}
            except Exception:
                pass
        return self._default_state()

    def save_state(self):
        """Speichert den Status in JSON und exportiert gleichzeitig gamification_data.js für den Browser."""
        self.state["zuletzt_aktualisiert"] = datetime.now().isoformat()
        
        # 1. JSON speichern
        try:
            with open(DATA_JSON_PATH, "w", encoding="utf-8") as f:
                json.dump(self.state, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Warnung beim Speichern von .gamification.json: {e}")

        # 2. JS-Export für lokale Browser-Nutzung (CORS-Frei via file://)
        try:
            DATA_JS_PATH.parent.mkdir(parents=True, exist_ok=True)
            js_content = f"""// Automatisch generierter lokaler Gamification-Spielstand
window.GAMIFICATION_DATA = {json.dumps(self.state, indent=2, ensure_ascii=False)};
window.GAMIFICATION_BADGES_KATALOG = {json.dumps(BADGES_KATALOG, indent=2, ensure_ascii=False)};
window.GAMIFICATION_LEVEL_STUFEN = {json.dumps(LEVEL_STUFEN, indent=2, ensure_ascii=False)};
"""
            with open(DATA_JS_PATH, "w", encoding="utf-8") as f:
                f.write(js_content)
        except Exception as e:
            print(f"Warnung beim Exportieren von gamification_data.js: {e}")

    def get_level_info(self, xp: int) -> Dict[str, Any]:
        """Berechnet Level, Titel und Fortschritt zur nächsten Stufe."""
        for info in LEVEL_STUFEN:
            if info["min_xp"] <= xp <= info["max_xp"]:
                naechste_xp = info["max_xp"] + 1
                xp_in_level = xp - info["min_xp"]
                xp_fuer_level = naechste_xp - info["min_xp"]
                prozent = min(100, int((xp_in_level / xp_fuer_level) * 100)) if xp_fuer_level > 0 else 100
                return {
                    "level": info["level"],
                    "titel": info["titel"],
                    "rang": info["rang"],
                    "aktuelle_xp": xp,
                    "min_xp": info["min_xp"],
                    "max_xp": info["max_xp"],
                    "naechste_stufe_xp": naechste_xp,
                    "prozent": prozent
                }
        # Fallback höchstes Level
        return {
            "level": 10,
            "titel": "Software-Architektin 🏆",
            "rang": "Großmeisterin",
            "aktuelle_xp": xp,
            "min_xp": 6801,
            "max_xp": 99999,
            "naechste_stufe_xp": 99999,
            "prozent": 100
        }

    def sync_mit_test_ergebnissen(self, bestandene_kapitel_ordner: List[str], anzahl_bestandene_tests: int) -> Dict[str, Any]:
        """
        Gleicht die aktuellen Testergebnisse ab, vergibt XP und schaltet Badges frei.
        Gibt ein Event-Dictionary für feierliche Terminal-Meldungen zurück.
        """
        alte_geloeste = set(self.state.get("geloeste_kapitel", []))
        neue_geloeste = set(bestandene_kapitel_ordner)
        alte_badges = set(self.state.get("freigeschaltete_badges", []))
        altes_level = self.state.get("level", 1)

        neu_geloest = neue_geloeste - alte_geloeste
        
        # Basis-XP Berechnung:
        # 100 XP pro gelöstem Kapitel + 10 XP pro bestandenem Test
        berechnete_xp = (len(neue_geloeste) * 100) + (anzahl_bestandene_tests * 10)

        # Badges überprüfen und Bonus-XP addieren
        neu_freigeschaltet_badges = []
        for badge_id, badge in BADGES_KATALOG.items():
            kriterien = badge["kriterium"]
            # Alle Kriterien-Ordner müssen gelöst sein
            if all(k in neue_geloeste for k in kriterien):
                if badge_id not in alte_badges:
                    neu_freigeschaltet_badges.append(badge)
                berechnete_xp += badge["xp_bonus"]

        # Streak-Berechnung
        heute = str(date.today())
        letzter_tag = self.state.get("letzter_aktiver_tag", heute)
        if letzter_tag != heute:
            try:
                diff = (date.today() - date.fromisoformat(letzter_tag)).days
                if diff == 1:
                    self.state["streak_tage"] = self.state.get("streak_tage", 1) + 1
                elif diff > 1:
                    self.state["streak_tage"] = 1
            except Exception:
                self.state["streak_tage"] = 1
            self.state["letzter_aktiver_tag"] = heute

        # Level-Update
        lvl_info = self.get_level_info(berechnete_xp)
        neues_level = lvl_info["level"]

        # Status aktualisieren
        self.state["xp"] = berechnete_xp
        self.state["level"] = neues_level
        self.state["titel"] = lvl_info["titel"]
        self.state["rang"] = lvl_info["rang"]
        self.state["geloeste_kapitel"] = list(neue_geloeste)
        self.state["bestandene_tests"] = anzahl_bestandene_tests
        self.state["freigeschaltete_badges"] = [
            b_id for b_id, b in BADGES_KATALOG.items()
            if all(k in neue_geloeste for k in b["kriterium"])
        ]

        self.save_state()

        return {
            "neue_kapitel": list(neu_geloest),
            "neue_badges": neu_freigeschaltet_badges,
            "level_up": neues_level > altes_level,
            "altes_level": altes_level,
            "neues_level": neues_level,
            "lvl_info": lvl_info,
            "gesamt_xp": berechnete_xp
        }


def report_single_chapter_result(kapitel_ordner: str, tests_erfolgreich: bool, tests_anzahl: int):
    """
    Wird von einzelnen test_aufgabe.py Skripten aufgerufen, wenn sie direkt ausgeführt werden.
    Aktualisiert den Spielstand und gibt motivierendes Feedback im Terminal aus.
    """
    gm = GamificationManager()
    aktuelle_geloeste = set(gm.state.get("geloeste_kapitel", []))
    
    if tests_erfolgreich and tests_anzahl > 0:
        war_bereits_geloest = kapitel_ordner in aktuelle_geloeste
        aktuelle_geloeste.add(kapitel_ordner)
        
        # Gesamtbestandene Tests schätzen/updaten
        alte_tests = gm.state.get("bestandene_tests", 0)
        neue_tests = alte_tests if war_bereits_geloest else alte_tests + tests_anzahl
        
        events = gm.sync_mit_test_ergebnissen(list(aktuelle_geloeste), neue_tests)
        lvl = events["lvl_info"]
        
        print("\n" + "═" * 60)
        print(f"🎉 KAPITEL BESTANDEN! ⭐ {lvl['titel']} (Level {lvl['level']})")
        print(f"💎 Aktuelle XP: {events['gesamt_xp']} XP | Rang: {lvl['rang']}")
        
        if events.get("level_up"):
            print(f"🚀 LEVEL UP! Du bist aufgestiegen zu Level {lvl['level']}!")
            
        if events.get("neue_badges"):
            for b in events["neue_badges"]:
                print(f"🏆 NEUE TROPHÄE: {b['icon']} {b['name']} (+{b['xp_bonus']} XP Bonus!)")
                
        print(f"💡 Zeige deinen Fortschrittspass mit: python3 profil.py")
        print("═" * 60 + "\n")


# Singleton-Instanz
manager = GamificationManager()
