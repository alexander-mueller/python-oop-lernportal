"""
Kapitel 16: Master-Abschlussprojekt – Tierheim- & PetCare-Manager 🐾🏥
=====================================================================
Das große Meisterstück: Die Vereinigung aller drei Lehrpfade!

1. Modellierung & Vererbung:
   - Basisklasse 'Tier' mit Polymorphie und Validierung
   - Spezialisierte Kindklassen: 'Hund', 'Katze', 'Vogel'
2. Robuste Fehlerbehandlung:
   - Eigene Exception-Hierarchie ('TierheimFehler', 'ValidierungsFehler', etc.)
3. Persistenz:
   - Vollständiges JSON Savegame (Speichern & Laden mit Factory-Muster)
   - Tabellarischer CSV-Export
4. Architektur & GUI (MVC):
   - 'Tierheim' als reines Daten- & Geschäftslogik-Modell (Model)
   - 'TierheimApp' als interaktive Tkinter Desktop-Applikation (View & Controller)
"""

from __future__ import annotations
import csv
import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

# ==============================================================================
# Tkinter Import mit sicherem Fallback für Headless- & Server-Umgebungen
# ==============================================================================
try:
    import tkinter as tk
    from tkinter import ttk, messagebox
except ImportError:
    # Headless Mock-Objekte (ermöglicht Ausführung und Tests ohne X11-Display)
    class _MockWidget:
        def __init__(self, master=None, text="", **kwargs):
            self.master = master
            self._config = dict(kwargs)
            if text:
                self._config["text"] = text
            self._entry_text = str(kwargs.get("textvariable", text))
            self._items: list[Any] = []
            self._selection: list[int] = []

        def config(self, **kwargs):
            self._config.update(kwargs)

        def configure(self, **kwargs):
            self.config(**kwargs)

        def cget(self, key):
            return self._config.get(key, "")

        def __getitem__(self, key):
            return self._config.get(key, "")

        def __setitem__(self, key, value):
            self._config[key] = value

        def grid(self, **kwargs):
            pass

        def pack(self, **kwargs):
            pass

        def get(self):
            return self._entry_text

        def set(self, val):
            self._entry_text = str(val)

        def delete(self, first=0, last=None):
            if hasattr(self, "_items") and self._items:
                self._items.clear()
            self._entry_text = ""

        def insert(self, index, string):
            if hasattr(self, "_items"):
                self._items.append(str(string))
            self._entry_text = str(string)

        def curselection(self):
            return tuple(self._selection) if self._selection else (0,) if self._items else ()

        def size(self):
            return len(self._items)

        def get_item(self, index):
            if 0 <= index < len(self._items):
                return self._items[index]
            return ""

        def invoke(self):
            cmd = self._config.get("command")
            if callable(cmd):
                return cmd()

    class _MockTk(_MockWidget):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._title = ""
            self._geometry = ""

        def title(self, title: str):
            self._title = title

        def geometry(self, geom: str):
            self._geometry = geom

        def mainloop(self):
            pass

        def destroy(self):
            pass

    class _MockStringVar:
        def __init__(self, value=""):
            self._val = str(value)

        def get(self):
            return self._val

        def set(self, val):
            self._val = str(val)

    class _MockBooleanVar:
        def __init__(self, value=False):
            self._val = bool(value)

        def get(self):
            return self._val

        def set(self, val):
            self._val = bool(val)

    class _MockMessageBox:
        @staticmethod
        def showinfo(title, message):
            pass

        @staticmethod
        def showwarning(title, message):
            pass

        @staticmethod
        def showerror(title, message):
            pass

    class _MockTkModule:
        Tk = _MockTk
        Label = _MockWidget
        Button = _MockWidget
        Entry = _MockWidget
        Frame = _MockWidget
        Listbox = _MockWidget
        Scrollbar = _MockWidget
        Checkbutton = _MockWidget
        StringVar = _MockStringVar
        BooleanVar = _MockBooleanVar
        OptionMenu = _MockWidget
        END = "end"
        SINGLE = "single"
        BOTH = "both"
        Y = "y"
        W = "w"
        E = "e"

    class _MockTtkModule:
        Combobox = _MockWidget
        LabelFrame = _MockWidget
        Button = _MockWidget
        Label = _MockWidget
        Entry = _MockWidget
        Frame = _MockWidget

    tk = _MockTkModule()
    ttk = _MockTtkModule()
    messagebox = _MockMessageBox()


# ==============================================================================
# TEIL 1: EIGENE EXCEPTION-HIERARCHIE
# ==============================================================================
class TierheimFehler(Exception):
    """Basis-Exception für alle fachlichen Fehler im Tierheim."""
    pass


class ValidierungsFehler(TierheimFehler):
    """Wird ausgelöst, wenn eingegebene Daten (Name, Alter, Gewicht) unzulässig sind."""
    pass


class TierNichtGefundenFehler(TierheimFehler):
    """Wird ausgelöst, wenn ein gesuchtes Tier nicht im Tierheim existiert."""
    pass


class KapazitaetUeberschrittenFehler(TierheimFehler):
    """Wird ausgelöst, wenn das Tierheim voll ist und kein Tier mehr aufgenommen werden kann."""
    pass


# ==============================================================================
# TEIL 2: DAS DATENMODELL (BASISKLASSE & KINDKLASSEN)
# ==============================================================================
class Tier:
    """
    Abstrakte Basisklasse für alle Tiere im Tierheim.
    
    Attribute:
        name (str): Name des Tiers (darf nicht leer sein).
        alter (int): Alter in Jahren (muss >= 0 sein).
        gewicht (float): Gewicht in kg (muss > 0 sein).
        geimpft (bool): Impfstatus (Standard: False).
        hunger (int): Hunger-Level von 0 (satt) bis 100 (verhungert) (Standard: 50).
    """

    def __init__(
        self,
        name: str,
        alter: int,
        gewicht: float,
        geimpft: bool = False,
        hunger: int = 50,
    ) -> None:
        """
        Initialisiert ein Tier und validiert alle Attribute.
        Löst ValidierungsFehler aus bei:
        - leerem oder nur aus Leerzeichen bestehendem Namen
        - alter < 0
        - gewicht <= 0
        Hunger wird auf den Bereich [0, 100] begrenzt (geclampt).
        """
        # TODO: Validierung & Zuweisung implementieren
        pass

    def fuettern(self, futtermenge_gramm: int) -> str:
        """
        Reduziert das Hunger-Level des Tiers.
        Jede 100g Futter senken den Hunger um 20 Punkte (Minimum: 0).
        Beispiel: Bei 250g Futter sinkt der Hunger um int(250 * 0.2) = 50.
        Gibt einen Bestätigungstext zurück, z.B.:
        "Bello wurde mit 200g gefüttert. Neuer Hunger-Level: 10/100."
        """
        # TODO: Implementieren
        pass

    def impfen(self) -> bool:
        """
        Setzt self.geimpft auf True.
        Gibt True zurück, wenn das Tier frisch geimpft wurde,
        oder False, falls es bereits geimpft war.
        """
        # TODO: Implementieren
        pass

    def mache_laut(self) -> str:
        """Polymorphe Methode: Gibt den artspezifischen Laut des Tiers zurück."""
        # Basis-Standard
        return f"{self.name} macht ein unbestimmtes Geräusch."

    def get_details(self) -> str:
        """Gibt eine Zusammenfassung der artspezifischen Zusatzmerkmale zurück."""
        return "Keine speziellen Merkmale"

    def to_dict(self) -> Dict[str, Any]:
        """
        Wandelt das Tier in ein Dictionary für den JSON-Export um.
        Enthält zwingend den Schlüssel 'art': 'Tier'.
        """
        # TODO: Implementieren
        pass

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> Tier:
        """
        Factory-Methode: Erstellt anhand des 'art'-Schlüssels
        die korrekte Instanz (Hund, Katze, Vogel oder Tier).
        """
        # TODO: Implementieren
        pass

    def __str__(self) -> str:
        impf_icon = "💉 Geimpft" if self.geimpft else "❌ Ungeimpft"
        return f"[{self.__class__.__name__}] {self.name} ({self.alter} Jahre, {self.gewicht:.1f} kg, Hunger: {self.hunger}/100, {impf_icon})"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}', alter={self.alter}, gewicht={self.gewicht}, geimpft={self.geimpft}, hunger={self.hunger})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Tier):
            return False
        return (
            self.name == other.name
            and self.alter == other.alter
            and abs(self.gewicht - other.gewicht) < 0.001
            and self.geimpft == other.geimpft
            and self.hunger == other.hunger
        )


class Hund(Tier):
    """
    Spezialisierte Kindklasse für Hunde.
    
    Zusatzattribute:
        rasse (str): Hunderasse (Standard: "Mischling", darf nicht leer sein).
        gassigegangen (bool): Ob der Hund heute schon Gassi war (Standard: False).
    """

    def __init__(
        self,
        name: str,
        alter: int,
        gewicht: float,
        rasse: str = "Mischling",
        geimpft: bool = False,
        hunger: int = 50,
        gassigegangen: bool = False,
    ) -> None:
        """Initialisiert einen Hund mit super().__init__() und validiert rasse."""
        # TODO: Implementieren
        pass

    def gassi_gehen(self, minuten: int) -> str:
        """
        Führt den Hund Gassi.
        - Setzt self.gassigegangen auf True.
        - Erhöht den Hunger um 1 Punkt pro 5 Minuten (Hunger maximal 100).
        - Gibt Rückgabetext zurück: "Bello war 30 Minuten Gassi! 🦮"
        """
        # TODO: Implementieren
        pass

    def mache_laut(self) -> str:
        """Gibt Hundegebell zurück: '{self.name} bellt: Wuff! Wuff! 🐶'"""
        # TODO: Implementieren
        pass

    def get_details(self) -> str:
        status = "war Gassi" if self.gassigegangen else "muss noch raus"
        return f"Rasse: {self.rasse} ({status})"

    def to_dict(self) -> Dict[str, Any]:
        """Erweitert das Basis-Dictionary um 'art': 'Hund', 'rasse' und 'gassigegangen'."""
        # TODO: Implementieren
        pass


class Katze(Tier):
    """
    Spezialisierte Kindklasse für Katzen.
    
    Zusatzattribute:
        stubenrein (bool): Ob die Katze ein Katzenklo benutzt (Standard: True).
        kratzbaum_benutzt (bool): Ob sie heute gekratzt hat (Standard: False).
    """

    def __init__(
        self,
        name: str,
        alter: int,
        gewicht: float,
        stubenrein: bool = True,
        geimpft: bool = False,
        hunger: int = 50,
        kratzbaum_benutzt: bool = False,
    ) -> None:
        """Initialisiert eine Katze mit super().__init__()."""
        # TODO: Implementieren
        pass

    def kratzen(self) -> str:
        """
        Katze wetzt ihre Krallen.
        - Setzt self.kratzbaum_benutzt auf True.
        - Gibt Rückgabetext zurück: "{self.name} wetzt die Krallen am Kratzbaum! 🐾"
        """
        # TODO: Implementieren
        pass

    def mache_laut(self) -> str:
        """Gibt Katzenlaut zurück: '{self.name} schnurrt: Miau! Schnurr... 🐱'"""
        # TODO: Implementieren
        pass

    def get_details(self) -> str:
        sauber = "stubenrein" if self.stubenrein else "nicht stubenrein"
        return f"Stubenrein: {sauber}"

    def to_dict(self) -> Dict[str, Any]:
        """Erweitert das Basis-Dictionary um 'art': 'Katze', 'stubenrein' und 'kratzbaum_benutzt'."""
        # TODO: Implementieren
        pass


class Vogel(Tier):
    """
    Spezialisierte Kindklasse für Vögel.
    
    Zusatzattribute:
        spannweite_cm (float): Flügelspannweite in cm (muss > 0 sein, Standard: 25.0).
        kann_sprechen (bool): Kann der Vogel sprechen/nachplappern (Standard: False).
    """

    def __init__(
        self,
        name: str,
        alter: int,
        gewicht: float,
        spannweite_cm: float = 25.0,
        kann_sprechen: bool = False,
        geimpft: bool = False,
        hunger: int = 50,
    ) -> None:
        """Initialisiert einen Vogel mit super().__init__() und validiert spannweite_cm."""
        # TODO: Implementieren
        pass

    def fliegen(self, runden: int) -> str:
        """
        Lässt den Vogel Runden in der Voliere fliegen.
        - Erhöht den Hunger um 2 Punkte pro Runde (maximal 100).
        - Gibt Text zurück: "{self.name} dreht {runden} elegante Runden in der Voliere! 🕊️"
        """
        # TODO: Implementieren
        pass

    def mache_laut(self) -> str:
        """
        Gibt Laut zurück:
        - Falls self.kann_sprechen: "{self.name} plappert: 'Hallo Mensch! Tschilp!' 🦜"
        - Sonst: "{self.name} zwitschert: Tschilp! Tschilp! 🐦"
        """
        # TODO: Implementieren
        pass

    def get_details(self) -> str:
        spricht = "kann sprechen" if self.kann_sprechen else "singt Melodien"
        return f"Spannweite: {self.spannweite_cm:.1f} cm ({spricht})"

    def to_dict(self) -> Dict[str, Any]:
        """Erweitert das Basis-Dictionary um 'art': 'Vogel', 'spannweite_cm' und 'kann_sprechen'."""
        # TODO: Implementieren
        pass


# ==============================================================================
# TEIL 3: DIE GESCHÄFTSLOGIK & DER VERWALTER (MODEL)
# ==============================================================================
class Tierheim:
    """
    Das Model des Tierheims: Verwaltet Tierbestände, Kapazitäten,
    Filter, Berechnungen und Dateipersistenz (JSON & CSV).
    Komplett unabhängig von der Benutzeroberfläche (100% testbar).
    """

    def __init__(self, name: str = "Tierheim Sonnenschein", max_kapazitaet: int = 20) -> None:
        """
        Initialisiert das Tierheim.
        - self.name = name
        - self.max_kapazitaet = max_kapazitaet (muss > 0 sein, sonst ValidierungsFehler)
        - self.tiere: List[Tier] = []
        """
        # TODO: Implementieren
        pass

    def tier_aufnehmen(self, tier: Tier) -> None:
        """
        Nimmt ein Tier auf.
        - Löst ValidierungsFehler aus, wenn tier kein Objekt der Klasse Tier (oder Subklasse) ist.
        - Löst KapazitaetUeberschrittenFehler aus, wenn len(self.tiere) >= self.max_kapazitaet.
        - Fügt das Tier zu self.tiere hinzu.
        """
        # TODO: Implementieren
        pass

    def tier_entlassen(self, name: str) -> Tier:
        """
        Entlässt (vermittelt) ein Tier anhand seines Namens (case-insensitive).
        - Findet das Tier, entfernt es aus self.tiere und gibt das entfernte Tier zurück.
        - Löst TierNichtGefundenFehler aus, falls kein Tier mit diesem Namen existiert.
        """
        # TODO: Implementieren
        pass

    def finde_tier(self, name: str) -> Optional[Tier]:
        """
        Sucht ein Tier nach Namen (case-insensitive).
        Gibt das Tier-Objekt zurück oder None, falls nicht gefunden.
        """
        # TODO: Implementieren
        pass

    def filtriere_nach_art(self, art_name: str) -> List[Tier]:
        """
        Gibt eine Liste aller Tiere zurück, deren Klassenname (z.B. 'Hund', 'Katze', 'Vogel')
        mit art_name (case-insensitive) übereinstimmt.
        Bei art_name == 'Alle' oder leerer Eingabe wird die gesamte Liste zurückgegeben.
        """
        # TODO: Implementieren
        pass

    def ungeimpfte_tiere(self) -> List[Tier]:
        """Gibt eine Liste aller Tiere zurück, bei denen self.geimpft == False ist."""
        # TODO: Implementieren
        pass

    def hungrige_tiere(self, schwellenwert: int = 50) -> List[Tier]:
        """Gibt alle Tiere zurück, deren Hunger-Level >= schwellenwert ist."""
        # TODO: Implementieren
        pass

    def durchschnittsalter(self) -> float:
        """
        Berechnet das durchschnittliche Alter aller Tiere im Heim.
        Gibt 0.0 zurück, wenn das Tierheim leer ist.
        """
        # TODO: Implementieren
        pass

    def gesamtgewicht(self) -> float:
        """
        Berechnet das Gesamtgewicht aller Tiere im Heim.
        Gibt 0.0 zurück, wenn das Tierheim leer ist.
        """
        # TODO: Implementieren
        pass

    def alle_fuettern(self, menge_gramm: int = 100) -> Dict[str, str]:
        """
        Füttert jedes Tier im Heim mit der angegebenen Futtermenge.
        Gibt ein Dictionary {tier.name: bestaetigungstext} zurück.
        """
        # TODO: Implementieren
        pass

    def alle_impfen(self) -> int:
        """
        Impft alle noch ungeimpften Tiere im Heim.
        Gibt die Anzahl der frisch geimpften Tiere zurück.
        """
        # TODO: Implementieren
        pass

    def to_dict(self) -> Dict[str, Any]:
        """
        Serialisiert das gesamte Tierheim in ein Dictionary.
        Format:
        {
            "name": self.name,
            "max_kapazitaet": self.max_kapazitaet,
            "tiere": [tier.to_dict() for tier in self.tiere]
        }
        """
        # TODO: Implementieren
        pass

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> Tierheim:
        """
        Erstellt ein Tierheim-Objekt aus einem Dictionary
        und rekonstruiert alle Tiere via Tier.from_dict().
        """
        # TODO: Implementieren
        pass

    def speichern_json(self, dateipfad: Union[str, Path]) -> None:
        """
        Speichert den gesamten Datenbestand als formatierte JSON-Datei (indent=2, utf-8).
        """
        # TODO: Implementieren
        pass

    def laden_json(self, dateipfad: Union[str, Path]) -> None:
        """
        Lädt Tierheimdaten aus einer JSON-Datei.
        Aktualisiert Name, max_kapazitaet und ersetzt self.tiere mit den geladenen Tieren.
        Löst FileNotFoundError aus, wenn die Datei nicht existiert.
        """
        # TODO: Implementieren
        pass

    def exportiere_csv(self, dateipfad: Union[str, Path]) -> None:
        """
        Exportiert den Tierbestand in eine CSV-Datei mit folgenden Spalten:
        Art,Name,Alter,Gewicht,Geimpft,Hunger,Details
        """
        # TODO: Implementieren
        pass

    def __len__(self) -> int:
        return len(self.tiere)

    def __str__(self) -> str:
        return f"Tierheim '{self.name}' ({len(self.tiere)}/{self.max_kapazitaet} Tiere)"


# ==============================================================================
# TEIL 4: DIE DESKTOP-BENUTZEROBERFLÄCHE (VIEW & CONTROLLER)
# ==============================================================================
class TierheimApp:
    """
    Die grafische Benutzeroberfläche (Tkinter) nach dem MVC-Muster.
    Verbindet GUI-Ereignisse mit den Methoden der Model-Klasse Tierheim.
    """

    def __init__(self, root: Any, tierheim: Optional[Tierheim] = None) -> None:
        """
        Initialisiert das GUI-Fenster und alle Widgets.
        """
        self.root = root
        self.tierheim = tierheim if tierheim is not None else Tierheim()

        if hasattr(self.root, "title"):
            self.root.title("🐾 PetCare & Tierheim-Manager Pro")
        if hasattr(self.root, "geometry"):
            self.root.geometry("850x620")

        self._aktiver_filter = "Alle"
        self._erzeuge_widgets()
        self.aktualisiere_ansicht()

    def _erzeuge_widgets(self) -> None:
        """Erzeugt alle visuellen Komponenten (Formular, Liste, Buttons, Statusleiste)."""
        self.label_titel = tk.Label(
            self.root,
            text=f"🏥 {self.tierheim.name}",
            font=("Arial", 16, "bold"),
        )
        self.label_titel.pack(pady=5)

        self.label_kapazitaet = tk.Label(
            self.root,
            text="Belegung: 0 / 20 Tiere",
            font=("Arial", 11),
        )
        self.label_kapazitaet.pack(pady=2)

        # Formular-Variablen
        self.var_art = tk.StringVar(value="Hund")
        self.var_name = tk.StringVar()
        self.var_alter = tk.StringVar(value="2")
        self.var_gewicht = tk.StringVar(value="10.5")
        self.var_extra = tk.StringVar(value="Golden Retriever")
        self.var_geimpft = tk.BooleanVar(value=False)

        # Listbox für Tierbestand
        self.listbox_tiere = tk.Listbox(self.root, font=("Courier", 10), height=12)
        self.listbox_tiere.pack(fill=tk.BOTH, expand=True, padx=15, pady=5)

        # Statusleiste
        self.label_status = tk.Label(
            self.root,
            text="Bereit.",
            bd=1,
            relief="sunken",
            anchor="w",
            font=("Arial", 9),
        )
        self.label_status.pack(side="bottom", fill="x")

    def aktualisiere_ansicht(self) -> None:
        """
        Aktualisiert die Anzeige in der Listbox und den Kapazitätszähler
        basierend auf dem aktuellen Datenmodell und Filter.
        """
        # 1. Kapazitätstext aktualisieren
        if hasattr(self.label_kapazitaet, "config"):
            self.label_kapazitaet.config(
                text=f"Belegung: {len(self.tierheim)} / {self.tierheim.max_kapazitaet} Tiere (Ø {self.tierheim.durchschnittsalter():.1f} Jahre, Σ {self.tierheim.gesamtgewicht():.1f} kg)"
            )

        # 2. Listbox leeren und neu befüllen
        self.listbox_tiere.delete(0, tk.END)

        if self._aktiver_filter == "Ungeimpft":
            tiere_anzeige = self.tierheim.ungeimpfte_tiere()
        elif self._aktiver_filter == "Hungrig":
            tiere_anzeige = self.tierheim.hungrige_tiere()
        elif self._aktiver_filter in ("Hund", "Katze", "Vogel"):
            tiere_anzeige = self.tierheim.filtriere_nach_art(self._aktiver_filter)
        else:
            tiere_anzeige = self.tierheim.tiere

        for tier in tiere_anzeige:
            impf_symbol = "💉" if tier.geimpft else "❌"
            eintrag = f"{tier.__class__.__name__:5s} | {tier.name:12s} | {tier.alter:2d} J. | {tier.gewicht:5.1f} kg | Hunger: {tier.hunger:3d}% | {impf_symbol} | {tier.get_details()}"
            self.listbox_tiere.insert(tk.END, eintrag)

    def setze_status(self, nachricht: str, typ: str = "info") -> None:
        """Setzt den Text und die Farbe der Statusleiste."""
        farben = {
            "info": "#1e293b",
            "success": "#166534",
            "warning": "#854d0e",
            "error": "#991b1b",
        }
        icon = {"info": "ℹ️ ", "success": "✅ ", "warning": "⚠️ ", "error": "❌ "}.get(typ, "")
        if hasattr(self.label_status, "config"):
            self.label_status.config(text=f"{icon}{nachricht}", fg=farben.get(typ, "#1e293b"))

    def get_ausgewaehltes_tier(self) -> Optional[Tier]:
        """Ermittelt das aktuell in der Listbox ausgewählte Tier-Objekt."""
        try:
            selektion = self.listbox_tiere.curselection()
            if not selektion:
                return None
            index = selektion[0]
            if 0 <= index < len(self.tierheim.tiere):
                return self.tierheim.tiere[index]
            return None
        except Exception:
            return None

    def tier_aufnehmen_klick(self) -> None:
        """
        Liest die Formulardaten aus, instanziiert das passende Tier-Objekt (Hund, Katze, Vogel)
        und fügt es dem Tierheim hinzu. Fängt ValidierungsFehler und KapazitaetUeberschrittenFehler ab.
        """
        # TODO: Implementieren
        pass

    def tier_fuettern_klick(self) -> None:
        """Füttert das ausgewählte Tier und aktualisiert die Ansicht."""
        # TODO: Implementieren
        pass

    def tier_impfen_klick(self) -> None:
        """Impft das ausgewählte Tier und aktualisiert die Ansicht."""
        # TODO: Implementieren
        pass

    def tier_laut_klick(self) -> None:
        """Lässt das ausgewählte Tier seinen artspezifischen Laut von sich geben."""
        # TODO: Implementieren
        pass

    def tier_vermitteln_klick(self) -> None:
        """Vermittelt (entlässt) das ausgewählte Tier aus dem Heim."""
        # TODO: Implementieren
        pass

    def speichern_klick(self, dateipfad: str = "tierheim_save.json") -> None:
        """Speichert den aktuellen Stand als JSON-Datei."""
        try:
            self.tierheim.speichern_json(dateipfad)
            self.setze_status(f"Erfolgreich gespeichert in '{dateipfad}'.", typ="success")
        except Exception as e:
            self.setze_status(f"Fehler beim Speichern: {e}", typ="error")

    def laden_klick(self, dateipfad: str = "tierheim_save.json") -> None:
        """Lädt den Stand aus einer JSON-Datei."""
        try:
            self.tierheim.laden_json(dateipfad)
            self.aktualisiere_ansicht()
            self.setze_status(f"Erfolgreich geladen aus '{dateipfad}'.", typ="success")
        except Exception as e:
            self.setze_status(f"Fehler beim Laden: {e}", typ="error")

    def csv_export_klick(self, dateipfad: str = "tierheim_export.csv") -> None:
        """Exportiert den Tierbestand als CSV-Tabelle."""
        try:
            self.tierheim.exportiere_csv(dateipfad)
            self.setze_status(f"CSV-Tabelle erfolgreich exportiert nach '{dateipfad}'.", typ="success")
        except Exception as e:
            self.setze_status(f"Fehler beim CSV-Export: {e}", typ="error")


# ==============================================================================
# HAUPTPROGRAMM (FÜR MANUELLES TESTEN)
# ==============================================================================
if __name__ == "__main__":
    print("🐾 Initialisiere Tierheim Sonnenschein...")
    heim = Tierheim("Tierheim Sonnenschein", max_kapazitaet=10)

    try:
        bello = Hund("Bello", alter=3, gewicht=14.5, rasse="Beagle")
        luna = Katze("Luna", alter=2, gewicht=4.2, stubenrein=True)
        tweety = Vogel("Tweety", alter=1, gewicht=0.3, spannweite_cm=18.0, kann_sprechen=True)

        heim.tier_aufnehmen(bello)
        heim.tier_aufnehmen(luna)
        heim.tier_aufnehmen(tweety)

        print(f"✅ {heim}")
        for t in heim.tiere:
            print(f"  • {t} -> Laut: {t.mache_laut()}")

    except TierheimFehler as e:
        print(f"⚠️ Tierheim-Fehler: {e}")
