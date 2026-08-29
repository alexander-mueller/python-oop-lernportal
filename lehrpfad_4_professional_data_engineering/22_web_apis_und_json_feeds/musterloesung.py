"""
Kapitel 22: Web-APIs, REST & JSON-Feeds 🌐📡
============================================
Lehrpfad 4: Professional Data Engineering

Musterlösung für Web-APIs, JSON-Feeds und defensive Fehlerbehandlung.
"""

import json
from typing import List, Dict, Any, Tuple, Optional, Union


def parse_wetter_antwort(json_text: str) -> Dict[str, Any]:
    """
    Parst den JSON-String einer Wetter-API und extrahiert Stadt, Temperatur,
    Luftfeuchtigkeit und Wetterlage.
    """
    try:
        data = json.loads(json_text)
        stadt = data["name"]
        temperatur = float(data["main"]["temp"])
        luftfeuchtigkeit = int(data["main"]["humidity"])
        
        weather_list = data["weather"]
        if not weather_list:
            wetterlage = "Unbekannt"
        else:
            wetterlage = weather_list[0].get("description") or weather_list[0].get("main", "Unbekannt")

        return {
            "stadt": stadt,
            "temperatur": temperatur,
            "luftfeuchtigkeit": luftfeuchtigkeit,
            "wetterlage": str(wetterlage),
        }
    except (json.JSONDecodeError, KeyError, IndexError, TypeError, ValueError) as e:
        raise ValueError(f"Ungültige Wetterdaten: {e}")


def filtriere_aktien_kurse(json_feed_text: str, min_kurs: float) -> List[Dict[str, Any]]:
    """
    Filtert alle Aktien mit Kurs >= min_kurs heraus.
    """
    try:
        data = json.loads(json_feed_text)
        if isinstance(data, dict) and "aktien" in data:
            aktien_liste = data["aktien"]
        elif isinstance(data, dict) and "stocks" in data:
            aktien_liste = data["stocks"]
        elif isinstance(data, list):
            aktien_liste = data
        else:
            return []

        ergebnis = []
        for item in aktien_liste:
            if isinstance(item, dict) and "kurs" in item:
                if float(item["kurs"]) >= float(min_kurs):
                    ergebnis.append(item)
            elif isinstance(item, dict) and "price" in item:
                if float(item["price"]) >= float(min_kurs):
                    ergebnis.append(item)
        return ergebnis
    except (json.JSONDecodeError, TypeError, ValueError):
        return []


def formatiere_nachrichten_ticker(news_json_text: str) -> str:
    """
    Formatiert Schlagzeilen zu einem Ticker-String.
    """
    try:
        data = json.loads(news_json_text)
        if isinstance(data, dict):
            nachrichten = data.get("nachrichten") or data.get("articles") or []
        elif isinstance(data, list):
            nachrichten = data
        else:
            return "+++ Keine aktuellen Eilmeldungen +++"

        if not nachrichten:
            return "+++ Keine aktuellen Eilmeldungen +++"

        eintraege = []
        for item in nachrichten:
            if isinstance(item, dict):
                titel = item.get("titel") or item.get("title") or "Ohne Titel"
                ressort = item.get("ressort") or item.get("category") or "Allgemein"
                eintraege.append(f"[{ressort}] {titel}")

        if not eintraege:
            return "+++ Keine aktuellen Eilmeldungen +++"

        return " +++ ".join(eintraege) + " +++"
    except (json.JSONDecodeError, TypeError):
        return "+++ Fehler beim Laden des Nachrichten-Feeds +++"


def validiere_api_antwort(status_code: int, payload_json_text: str) -> Tuple[bool, Union[Dict[str, Any], str]]:
    """
    Prüft Statuscode und JSON-Payload einer API-Antwort.
    """
    if status_code == 200:
        try:
            data = json.loads(payload_json_text)
            return (True, data)
        except json.JSONDecodeError:
            return (False, "Ungültiges JSON-Format")
    else:
        # Fehlerstatuscode
        error_detail = None
        try:
            err_data = json.loads(payload_json_text)
            if isinstance(err_data, dict):
                error_detail = err_data.get("error") or err_data.get("message") or err_data.get("detail")
        except Exception:
            pass

        if error_detail:
            return (False, f"HTTP Fehler {status_code}: {error_detail}")
        return (False, f"HTTP Fehler {status_code}")


class WetterApiParser:
    """
    Objektorientierter Wetter-Parser.
    """

    def __init__(self, raw_json: str = ""):
        self.raw_json: str = raw_json
        self.daten: Optional[Dict[str, Any]] = None
        if raw_json:
            self.lade_daten(raw_json)

    def lade_daten(self, raw_json: str) -> bool:
        """Lädt und validiert Wetter-JSON."""
        self.raw_json = raw_json
        try:
            self.daten = parse_wetter_antwort(raw_json)
            return True
        except ValueError:
            self.daten = None
            return False

    def get_temperatur(self) -> Optional[float]:
        """Liefert die Temperatur oder None."""
        if self.daten is not None:
            return self.daten.get("temperatur")
        return None

    def get_stadt(self) -> Optional[str]:
        """Liefert die Stadt oder None."""
        if self.daten is not None:
            return self.daten.get("stadt")
        return None

    def ist_frostig(self) -> bool:
        """Gibt True zurück wenn Temperatur < 0.0 °C."""
        temp = self.get_temperatur()
        if temp is not None:
            return temp < 0.0
        return False

    def ist_gueltig(self) -> bool:
        """Prüft ob valide Daten vorliegen."""
        return self.daten is not None
