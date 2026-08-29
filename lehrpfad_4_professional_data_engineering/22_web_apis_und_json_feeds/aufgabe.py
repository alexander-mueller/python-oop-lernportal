"""
Kapitel 22: Web-APIs, REST & JSON-Feeds 🌐📡
============================================
Lehrpfad 4: Professional Data Engineering

Thema:
REST-APIs, JSON als Datenformat, strukturierte Extraktion verschachtelter Payloads
und defensive Fehlerbehandlung (KeyError, JSONDecodeError).

Lernziele:
1. JSON-Strings parsen mit `json.loads(text)` und erzeugen mit `json.dumps(obj)`.
2. Extrahieren von Werten aus mehrfach verschachtelten Dictionaries und Listen.
3. Filtern und Transformieren von Web-Feeds (z.B. Aktienkurse, News-Ticker).
4. Validieren von HTTP-Statuscodes (200 OK vs. 404/500) und Fehler-Payloads.
5. Kapselung der API-Logik in einer wiederverwendbaren Klasse `WetterApiParser`.
"""

import json
from typing import List, Dict, Any, Tuple, Optional, Union


# ==============================================================================
# 🎯 TEILZIEL 1 (TODO 1): Wetter-Antwort parsen
# ==============================================================================
def parse_wetter_antwort(json_text: str) -> Dict[str, Any]:
    """
    Parst den JSON-String einer Wetter-API (z.B. OpenWeatherMap-Format)
    und extrahiert die wichtigsten Kenngrößen in ein kompaktes Dictionary.

    Erwartete Eingabe-Struktur (Beispiel):
    {
        "name": "Wien",
        "main": {
            "temp": 21.5,
            "humidity": 65
        },
        "weather": [
            {
                "main": "Clouds",
                "description": "Leicht bewölkt"
            }
        ]
    }

    Rückgabe-Format:
    {
        "stadt": str,             # aus data["name"]
        "temperatur": float,      # aus data["main"]["temp"]
        "luftfeuchtigkeit": int,  # aus data["main"]["humidity"]
        "wetterlage": str         # aus data["weather"][0]["description"] (oder data["weather"][0]["main"])
    }

    Fehlerbehandlung:
    - Wenn json_text ungültiges JSON ist (json.JSONDecodeError)
      oder erwartete Schlüssel fehlen (KeyError, IndexError, TypeError):
      Wirf einen ValueError("Ungültige Wetterdaten: " + str(e))
    """
    # TODO: Implementieren
    pass


# ==============================================================================
# 🎯 TEILZIEL 2 (TODO 2): Aktienkurse aus JSON-Feed filtern
# ==============================================================================
def filtriere_aktien_kurse(json_feed_text: str, min_kurs: float) -> List[Dict[str, Any]]:
    """
    Parst einen Finanzmarkt-Feed und filtert alle Aktien heraus, deren Kurs
    größer oder gleich `min_kurs` ist.

    Akzeptiert Formate:
    1. {"aktien": [{"symbol": "AAPL", "kurs": 185.5, "waehrung": "USD"}, ...]}
    2. oder direkt eine Liste: [{"symbol": "AAPL", "kurs": 185.5}, ...]

    Rückgabewert:
    - Eine Liste von Dictionaries der gefilterten Aktien (z.B. [ {"symbol": "AAPL", "kurs": 185.5, ...}, ... ])
    - Bei ungültigem JSON oder leerem Feed: leere Liste [] zurückgeben.
    """
    # TODO: Implementieren
    pass


# ==============================================================================
# 🎯 TEILZIEL 3 (TODO 3): Schlagzeilen-Ticker formatieren
# ==============================================================================
def formatiere_nachrichten_ticker(news_json_text: str) -> str:
    """
    Parst einen News-JSON-Feed und formatiert die Schlagzeilen zu einem durchgehenden
    Laufband-String für einen Nachrichtenticker.

    Erwartete Eingabe-Struktur:
    {
        "nachrichten": [
            {"titel": "Python 3.13 veröffentlicht", "ressort": "Tech"},
            {"titel": "DAX schließt im Plus", "ressort": "Wirtschaft"}
        ]
    }

    Formatierungsregel:
    - Jede Nachricht wird formatiert als: "[<Ressort>] <Titel> +++ "
    - Beispiel-Ergebnis:
      "[Tech] Python 3.13 veröffentlicht +++ [Wirtschaft] DAX schließt im Plus +++"
    - Falls keine Nachrichten vorhanden sind oder die Liste leer ist:
      "+++ Keine aktuellen Eilmeldungen +++" zurückgeben.
    - Bei ungültigem JSON: "+++ Fehler beim Laden des Nachrichten-Feeds +++" zurückgeben.
    """
    # TODO: Implementieren
    pass


# ==============================================================================
# 🎯 TEILZIEL 4 (TODO 4): HTTP-Antwort & Statuscode validieren
# ==============================================================================
def validiere_api_antwort(status_code: int, payload_json_text: str) -> Tuple[bool, Union[Dict[str, Any], str]]:
    """
    Überprüft den HTTP-Statuscode und den JSON-Payload einer Web-API-Antwort.

    Regeln:
    1. Wenn status_code == 200:
       - Versuche payload_json_text mit json.loads() zu parsen.
       - Bei Erfolg: Gib (True, geparstes_dict) zurück.
       - Bei json.JSONDecodeError: Gib (False, "Ungültiges JSON-Format") zurück.
       
    2. Wenn status_code != 200 (z.B. 400, 404, 500):
       - Versuche aus dem JSON-Payload eine Fehlermeldung zu extrahieren (Schlüssel 'error' oder 'message').
       - Falls vorhanden: Gib (False, f"HTTP Fehler {status_code}: {fehlermeldung}") zurück.
       - Falls nicht parsebar oder kein Schlüssel: Gib (False, f"HTTP Fehler {status_code}") zurück.
    """
    # TODO: Implementieren
    pass


# ==============================================================================
# 🎯 TEILZIEL 5 (TODO 5): Klasse WetterApiParser
# ==============================================================================
class WetterApiParser:
    """
    Objektorientierter Wrapper für Wetterdaten aus einer REST-API.
    """

    def __init__(self, raw_json: str = ""):
        """
        Initialisiert den Parser.
        Falls raw_json übergeben wurde, wird sofort lade_daten() ausgeführt.
        """
        self.raw_json: str = raw_json
        self.daten: Optional[Dict[str, Any]] = None
        if raw_json:
            self.lade_daten(raw_json)

    def lade_daten(self, raw_json: str) -> bool:
        """
        Versucht den JSON-String mittels parse_wetter_antwort() einzulesen.
        - Bei Erfolg: Speichert das extrahierte Dict in self.daten und gibt True zurück.
        - Bei Fehler (ValueError): Setzt self.daten = None und gibt False zurück.
        """
        # TODO: Implementieren
        pass

    def get_temperatur(self) -> Optional[float]:
        """Gibt die Temperatur zurück oder None, wenn keine Daten geladen sind."""
        # TODO: Implementieren
        pass

    def get_stadt(self) -> Optional[str]:
        """Gibt den Stadtnamen zurück oder None, wenn keine Daten geladen sind."""
        # TODO: Implementieren
        pass

    def ist_frostig(self) -> bool:
        """Gibt True zurück, wenn die Temperatur unter 0.0 °C liegt, sonst False."""
        # TODO: Implementieren
        pass

    def ist_gueltig(self) -> bool:
        """Gibt True zurück, wenn gültige Wetterdaten geladen sind (self.daten is not None)."""
        # TODO: Implementieren
        pass


# ==============================================================================
# Interaktiver Test im Terminal:
# (python3 aufgabe.py)
# ==============================================================================
if __name__ == "__main__":
    beispiel_wetter = """
    {
        "name": "München",
        "main": {"temp": 18.2, "humidity": 72},
        "weather": [{"main": "Rain", "description": "Leichter Regen"}]
    }
    """
    print("🌤️ Teste parse_wetter_antwort():")
    wetter = parse_wetter_antwort(beispiel_wetter)
    print(wetter)

    beispiel_aktien = """
    {
        "aktien": [
            {"symbol": "AAPL", "kurs": 189.5, "waehrung": "USD"},
            {"symbol": "GOOGL", "kurs": 142.0, "waehrung": "USD"},
            {"symbol": "PENNY", "kurs": 0.45, "waehrung": "USD"}
        ]
    }
    """
    print("\n📈 Teste filtriere_aktien_kurse() (min_kurs = 100):")
    gefiltert = filtriere_aktien_kurse(beispiel_aktien, 100.0)
    print(gefiltert)

    beispiel_news = """
    {
        "nachrichten": [
            {"titel": "Python 3.13 bringt Performance-Schub", "ressort": "Technologie"},
            {"titel": "Mars-Rover findet neue Gesteinsproben", "ressort": "Wissenschaft"}
        ]
    }
    """
    print("\n📰 Teste formatiere_nachrichten_ticker():")
    print(formatiere_nachrichten_ticker(beispiel_news))

    print("\n🛡️ Teste validiere_api_antwort():")
    print("Status 200:", validiere_api_antwort(200, '{"status": "ok", "items": [1, 2, 3]}'))
    print("Status 404:", validiere_api_antwort(404, '{"error": "Ressource nicht gefunden"}'))
