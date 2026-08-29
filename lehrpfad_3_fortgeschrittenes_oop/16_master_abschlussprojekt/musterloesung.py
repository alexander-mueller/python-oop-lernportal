"""
Kapitel 16: Master-Abschlussprojekt – Referenz-Musterlösung 🐾🏥
================================================================
Vollständige, fehlerfreie Musterlösung aller Klassen und Komponenten.
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
    """Wird ausgelöst, wenn eingegebene Daten unzulässig sind."""
    pass


class TierNichtGefundenFehler(TierheimFehler):
    """Wird ausgelöst, wenn ein gesuchtes Tier nicht existiert."""
    pass


class KapazitaetUeberschrittenFehler(TierheimFehler):
    """Wird ausgelöst, wenn das Tierheim voll ist."""
    pass


# ==============================================================================
# TEIL 2: DAS DATENMODELL (BASISKLASSE & KINDKLASSEN)
# ==============================================================================
class Tier:
    """
    Basisklasse für alle Tiere im Tierheim.
    """

    def __init__(
        self,
        name: str,
        alter: int,
        gewicht: float,
        geimpft: bool = False,
        hunger: int = 50,
    ) -> None:
        if not isinstance(name, str) or not name.strip():
            raise ValidierungsFehler("Name darf nicht leer sein!")
        try:
            alter_val = int(alter)
        except (ValueError, TypeError):
            raise ValidierungsFehler("Alter muss eine gültige ganze Zahl sein!")
        if alter_val < 0:
            raise ValidierungsFehler("Alter darf nicht negativ sein!")

        try:
            gewicht_val = float(gewicht)
        except (ValueError, TypeError):
            raise ValidierungsFehler("Gewicht muss eine gültige Kommazahl sein!")
        if gewicht_val <= 0:
            raise ValidierungsFehler("Gewicht muss größer als 0 sein!")

        try:
            hunger_val = int(hunger)
        except (ValueError, TypeError):
            hunger_val = 50

        self.name: str = name.strip()
        self.alter: int = alter_val
        self.gewicht: float = gewicht_val
        self.geimpft: bool = bool(geimpft)
        self.hunger: int = max(0, min(100, hunger_val))

    def fuettern(self, futtermenge_gramm: int) -> str:
        """Reduziert den Hunger (20 Punkte pro 100g Futter)."""
        if futtermenge_gramm <= 0:
            return f"{self.name} hat kein Futter erhalten."
        reduktion = int(futtermenge_gramm * 0.2)
        self.hunger = max(0, self.hunger - reduktion)
        return f"{self.name} wurde mit {futtermenge_gramm}g gefüttert. Neuer Hunger-Level: {self.hunger}/100."

    def impfen(self) -> bool:
        """Impft das Tier (setzt geimpft=True)."""
        if self.geimpft:
            return False
        self.geimpft = True
        return True

    def mache_laut(self) -> str:
        """Polymorpher Standardlaut."""
        return f"{self.name} macht ein unbestimmtes Geräusch."

    def get_details(self) -> str:
        return "Keine speziellen Merkmale"

    def to_dict(self) -> Dict[str, Any]:
        """Serialisiert das Tier in ein Dictionary."""
        return {
            "art": "Tier",
            "name": self.name,
            "alter": self.alter,
            "gewicht": self.gewicht,
            "geimpft": self.geimpft,
            "hunger": self.hunger,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> Tier:
        """Factory-Methode zur Wiederherstellung der korrekten Tier-Klasse."""
        art = data.get("art", "Tier")
        name = data.get("name", "Unbekannt")
        alter = data.get("alter", 0)
        gewicht = data.get("gewicht", 1.0)
        geimpft = data.get("geimpft", False)
        hunger = data.get("hunger", 50)

        if art == "Hund":
            return Hund(
                name=name,
                alter=alter,
                gewicht=gewicht,
                rasse=data.get("rasse", "Mischling"),
                geimpft=geimpft,
                hunger=hunger,
                gassigegangen=data.get("gassigegangen", False),
            )
        elif art == "Katze":
            return Katze(
                name=name,
                alter=alter,
                gewicht=gewicht,
                stubenrein=data.get("stubenrein", True),
                geimpft=geimpft,
                hunger=hunger,
                kratzbaum_benutzt=data.get("kratzbaum_benutzt", False),
            )
        elif art == "Vogel":
            return Vogel(
                name=name,
                alter=alter,
                gewicht=gewicht,
                spannweite_cm=data.get("spannweite_cm", 25.0),
                kann_sprechen=data.get("kann_sprechen", False),
                geimpft=geimpft,
                hunger=hunger,
            )
        else:
            return cls(
                name=name,
                alter=alter,
                gewicht=gewicht,
                geimpft=geimpft,
                hunger=hunger,
            )

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
    """Spezialisierte Kindklasse für Hunde."""

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
        super().__init__(name, alter, gewicht, geimpft, hunger)
        if not isinstance(rasse, str) or not rasse.strip():
            raise ValidierungsFehler("Rasse darf nicht leer sein!")
        self.rasse: str = rasse.strip()
        self.gassigegangen: bool = bool(gassigegangen)

    def gassi_gehen(self, minuten: int) -> str:
        self.gassigegangen = True
        self.hunger = min(100, self.hunger + max(0, int(minuten) // 5))
        return f"{self.name} war {minuten} Minuten Gassi! 🦮"

    def mache_laut(self) -> str:
        return f"{self.name} bellt: Wuff! Wuff! 🐶"

    def get_details(self) -> str:
        status = "war Gassi" if self.gassigegangen else "muss noch raus"
        return f"Rasse: {self.rasse} ({status})"

    def to_dict(self) -> Dict[str, Any]:
        d = super().to_dict()
        d["art"] = "Hund"
        d["rasse"] = self.rasse
        d["gassigegangen"] = self.gassigegangen
        return d


class Katze(Tier):
    """Spezialisierte Kindklasse für Katzen."""

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
        super().__init__(name, alter, gewicht, geimpft, hunger)
        self.stubenrein: bool = bool(stubenrein)
        self.kratzbaum_benutzt: bool = bool(kratzbaum_benutzt)

    def kratzen(self) -> str:
        self.kratzbaum_benutzt = True
        return f"{self.name} wetzt die Krallen am Kratzbaum! 🐾"

    def mache_laut(self) -> str:
        return f"{self.name} schnurrt: Miau! Schnurr... 🐱"

    def get_details(self) -> str:
        sauber = "stubenrein" if self.stubenrein else "nicht stubenrein"
        return f"Stubenrein: {sauber}"

    def to_dict(self) -> Dict[str, Any]:
        d = super().to_dict()
        d["art"] = "Katze"
        d["stubenrein"] = self.stubenrein
        d["kratzbaum_benutzt"] = self.kratzbaum_benutzt
        return d


class Vogel(Tier):
    """Spezialisierte Kindklasse für Vögel."""

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
        super().__init__(name, alter, gewicht, geimpft, hunger)
        try:
            sw = float(spannweite_cm)
        except (ValueError, TypeError):
            raise ValidierungsFehler("Spannweite muss eine Zahl sein!")
        if sw <= 0:
            raise ValidierungsFehler("Spannweite muss > 0 sein!")
        self.spannweite_cm: float = sw
        self.kann_sprechen: bool = bool(kann_sprechen)

    def fliegen(self, runden: int) -> str:
        self.hunger = min(100, self.hunger + max(0, int(runden) * 2))
        return f"{self.name} dreht {runden} elegante Runden in der Voliere! 🕊️"

    def mache_laut(self) -> str:
        if self.kann_sprechen:
            return f"{self.name} plappert: 'Hallo Mensch! Tschilp!' 🦜"
        return f"{self.name} zwitschert: Tschilp! Tschilp! 🐦"

    def get_details(self) -> str:
        spricht = "kann sprechen" if self.kann_sprechen else "singt Melodien"
        return f"Spannweite: {self.spannweite_cm:.1f} cm ({spricht})"

    def to_dict(self) -> Dict[str, Any]:
        d = super().to_dict()
        d["art"] = "Vogel"
        d["spannweite_cm"] = self.spannweite_cm
        d["kann_sprechen"] = self.kann_sprechen
        return d


# ==============================================================================
# TEIL 3: DIE GESCHÄFTSLOGIK & DER VERWALTER (MODEL)
# ==============================================================================
class Tierheim:
    """
    Das Model des Tierheims: Verwaltet Bestände, Filter, Berechnungen und Persistenz.
    """

    def __init__(self, name: str = "Tierheim Sonnenschein", max_kapazitaet: int = 20) -> None:
        if not isinstance(name, str) or not name.strip():
            raise ValidierungsFehler("Tierheim-Name darf nicht leer sein!")
        try:
            kap = int(max_kapazitaet)
        except (ValueError, TypeError):
            raise ValidierungsFehler("Kapazität muss eine positive ganze Zahl sein!")
        if kap <= 0:
            raise ValidierungsFehler("Kapazität muss größer als 0 sein!")

        self.name: str = name.strip()
        self.max_kapazitaet: int = kap
        self.tiere: List[Tier] = []

    def tier_aufnehmen(self, tier: Tier) -> None:
        if not isinstance(tier, Tier):
            raise ValidierungsFehler("Nur Tier-Objekte können aufgenommen werden!")
        if len(self.tiere) >= self.max_kapazitaet:
            raise KapazitaetUeberschrittenFehler(
                f"Tierheim ist voll! Maximale Kapazität von {self.max_kapazitaet} erreicht."
            )
        self.tiere.append(tier)

    def tier_entlassen(self, name: str) -> Tier:
        suchname = name.strip().lower()
        for i, t in enumerate(self.tiere):
            if t.name.lower() == suchname:
                return self.tiere.pop(i)
        raise TierNichtGefundenFehler(f"Kein Tier mit dem Namen '{name}' gefunden!")

    def finde_tier(self, name: str) -> Optional[Tier]:
        suchname = name.strip().lower()
        for t in self.tiere:
            if t.name.lower() == suchname:
                return t
        return None

    def filtriere_nach_art(self, art_name: str) -> List[Tier]:
        if not art_name or art_name.strip().lower() == "alle":
            return list(self.tiere)
        such_art = art_name.strip().lower()
        return [t for t in self.tiere if t.__class__.__name__.lower() == such_art]

    def ungeimpfte_tiere(self) -> List[Tier]:
        return [t for t in self.tiere if not t.geimpft]

    def hungrige_tiere(self, schwellenwert: int = 50) -> List[Tier]:
        return [t for t in self.tiere if t.hunger >= schwellenwert]

    def durchschnittsalter(self) -> float:
        if not self.tiere:
            return 0.0
        return sum(t.alter for t in self.tiere) / len(self.tiere)

    def gesamtgewicht(self) -> float:
        return sum(t.gewicht for t in self.tiere)

    def alle_fuettern(self, menge_gramm: int = 100) -> Dict[str, str]:
        ergebnisse = {}
        for t in self.tiere:
            ergebnisse[t.name] = t.fuettern(menge_gramm)
        return ergebnisse

    def alle_impfen(self) -> int:
        frisch_geimpft = 0
        for t in self.tiere:
            if t.impfen():
                frisch_geimpft += 1
        return frisch_geimpft

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "max_kapazitaet": self.max_kapazitaet,
            "tiere": [t.to_dict() for t in self.tiere],
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> Tierheim:
        heim = cls(
            name=data.get("name", "Tierheim Sonnenschein"),
            max_kapazitaet=data.get("max_kapazitaet", 20),
        )
        for t_dict in data.get("tiere", []):
            heim.tier_aufnehmen(Tier.from_dict(t_dict))
        return heim

    def speichern_json(self, dateipfad: Union[str, Path]) -> None:
        p = Path(dateipfad)
        p.parent.mkdir(parents=True, exist_ok=True)
        with open(p, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, indent=2, ensure_ascii=False)

    def laden_json(self, dateipfad: Union[str, Path]) -> None:
        p = Path(dateipfad)
        if not p.exists():
            raise FileNotFoundError(f"Datei '{dateipfad}' nicht gefunden!")
        with open(p, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.name = data.get("name", self.name)
        self.max_kapazitaet = data.get("max_kapazitaet", self.max_kapazitaet)
        self.tiere = [Tier.from_dict(t) for t in data.get("tiere", [])]

    def exportiere_csv(self, dateipfad: Union[str, Path]) -> None:
        p = Path(dateipfad)
        p.parent.mkdir(parents=True, exist_ok=True)
        with open(p, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Art", "Name", "Alter", "Gewicht", "Geimpft", "Hunger", "Details"])
            for t in self.tiere:
                writer.writerow([
                    t.__class__.__name__,
                    t.name,
                    t.alter,
                    f"{t.gewicht:.1f}",
                    "Ja" if t.geimpft else "Nein",
                    f"{t.hunger}%",
                    t.get_details(),
                ])

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
    """

    def __init__(self, root: Any, tierheim: Optional[Tierheim] = None) -> None:
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
        """Erzeugt das vollständige GUI-Layout mit Widgets."""
        # Oberer Titelbereich
        self.frame_header = tk.Frame(self.root, pady=6)
        self.frame_header.pack(fill="x", padx=10)

        self.label_titel = tk.Label(
            self.frame_header,
            text=f"🏥 {self.tierheim.name}",
            font=("Arial", 16, "bold"),
            fg="#4338ca",
        )
        self.label_titel.pack()

        self.label_kapazitaet = tk.Label(
            self.frame_header,
            text="Belegung: 0 / 20 Tiere",
            font=("Arial", 10),
            fg="#64748b",
        )
        self.label_kapazitaet.pack()

        # Hauptbereich: Split in Formular (Links) und Liste/Aktionen (Rechts)
        self.frame_main = tk.Frame(self.root)
        self.frame_main.pack(fill="both", expand=True, padx=10, pady=5)

        # ---------------- Formular (Links) ----------------
        self.frame_form = tk.Frame(self.frame_main, relief="groove", bd=1, padx=10, pady=10)
        self.frame_form.pack(side="left", fill="y", padx=5)

        tk.Label(self.frame_form, text="➕ Neues Tier aufnehmen", font=("Arial", 11, "bold")).pack(pady=4)

        # Art
        tk.Label(self.frame_form, text="Tierart:", anchor="w").pack(fill="x", pady=(4, 0))
        self.var_art = tk.StringVar(value="Hund")
        self.combo_art = ttk.Combobox(
            self.frame_form,
            textvariable=self.var_art,
            values=["Hund", "Katze", "Vogel"],
            state="readonly",
        )
        self.combo_art.pack(fill="x", pady=2)

        # Name
        tk.Label(self.frame_form, text="Name:", anchor="w").pack(fill="x", pady=(4, 0))
        self.var_name = tk.StringVar(value="")
        self.entry_name = tk.Entry(self.frame_form, textvariable=self.var_name)
        self.entry_name.pack(fill="x", pady=2)

        # Alter
        tk.Label(self.frame_form, text="Alter (Jahre):", anchor="w").pack(fill="x", pady=(4, 0))
        self.var_alter = tk.StringVar(value="2")
        self.entry_alter = tk.Entry(self.frame_form, textvariable=self.var_alter)
        self.entry_alter.pack(fill="x", pady=2)

        # Gewicht
        tk.Label(self.frame_form, text="Gewicht (kg):", anchor="w").pack(fill="x", pady=(4, 0))
        self.var_gewicht = tk.StringVar(value="10.5")
        self.entry_gewicht = tk.Entry(self.frame_form, textvariable=self.var_gewicht)
        self.entry_gewicht.pack(fill="x", pady=2)

        # Rasse / Extra
        tk.Label(self.frame_form, text="Rasse / Spannweite / Info:", anchor="w").pack(fill="x", pady=(4, 0))
        self.var_extra = tk.StringVar(value="Golden Retriever")
        self.entry_extra = tk.Entry(self.frame_form, textvariable=self.var_extra)
        self.entry_extra.pack(fill="x", pady=2)

        # Geimpft
        self.var_geimpft = tk.BooleanVar(value=False)
        self.chk_geimpft = tk.Checkbutton(self.frame_form, text="Bereits geimpft 💉", variable=self.var_geimpft)
        self.chk_geimpft.pack(anchor="w", pady=4)

        # Button Aufnahme
        self.btn_aufnehmen = tk.Button(
            self.frame_form,
            text="Tier aufnehmen ➕",
            bg="#10b981",
            fg="white",
            font=("Arial", 10, "bold"),
            command=self.tier_aufnehmen_klick,
        )
        self.btn_aufnehmen.pack(fill="x", pady=8)

        # ---------------- Listenbereich & Filter (Rechts) ----------------
        self.frame_rechts = tk.Frame(self.frame_main)
        self.frame_rechts.pack(side="right", fill="both", expand=True, padx=5)

        # Filterleiste
        self.frame_filter = tk.Frame(self.frame_rechts)
        self.frame_filter.pack(fill="x", pady=2)

        tk.Label(self.frame_filter, text="Filter:", font=("Arial", 9, "bold")).pack(side="left", padx=4)
        for f_name, f_label in [
            ("Alle", "Alle"),
            ("Hund", "Hunde 🐶"),
            ("Katze", "Katzen 🐱"),
            ("Vogel", "Vögel 🐦"),
            ("Ungeimpft", "Ungeimpft 💉"),
            ("Hungrig", "Hungrig 🍖"),
        ]:
            b = tk.Button(
                self.frame_filter,
                text=f_label,
                font=("Arial", 8),
                command=lambda fn=f_name: self.filter_setzen(fn),
            )
            b.pack(side="left", padx=2)

        # Listbox für Tiere
        self.listbox_tiere = tk.Listbox(self.frame_rechts, font=("Courier", 9), height=11)
        self.listbox_tiere.pack(fill="both", expand=True, pady=4)

        # Aktionsbuttons für ausgewähltes Tier
        self.frame_aktionen = tk.Frame(self.frame_rechts)
        self.frame_aktionen.pack(fill="x", pady=3)

        self.btn_fuettern = tk.Button(
            self.frame_aktionen,
            text="Füttern (100g) 🍖",
            bg="#f59e0b",
            fg="white",
            command=self.tier_fuettern_klick,
        )
        self.btn_fuettern.pack(side="left", fill="x", expand=True, padx=2)

        self.btn_impfen = tk.Button(
            self.frame_aktionen,
            text="Impfen 💉",
            bg="#3b82f6",
            fg="white",
            command=self.tier_impfen_klick,
        )
        self.btn_impfen.pack(side="left", fill="x", expand=True, padx=2)

        self.btn_laut = tk.Button(
            self.frame_aktionen,
            text="Laut machen 🔊",
            bg="#8b5cf6",
            fg="white",
            command=self.tier_laut_klick,
        )
        self.btn_laut.pack(side="left", fill="x", expand=True, padx=2)

        self.btn_vermitteln = tk.Button(
            self.frame_aktionen,
            text="Vermitteln 🏠",
            bg="#ef4444",
            fg="white",
            command=self.tier_vermitteln_klick,
        )
        self.btn_vermitteln.pack(side="left", fill="x", expand=True, padx=2)

        # Massen- & Dateiaufsatz
        self.frame_datei = tk.Frame(self.frame_rechts)
        self.frame_datei.pack(fill="x", pady=3)

        self.btn_alle_fuettern = tk.Button(
            self.frame_datei,
            text="Alle füttern 🍲",
            command=self.alle_fuettern_klick,
        )
        self.btn_alle_fuettern.pack(side="left", fill="x", expand=True, padx=2)

        self.btn_alle_impfen = tk.Button(
            self.frame_datei,
            text="Alle impfen 🩺",
            command=self.alle_impfen_klick,
        )
        self.btn_alle_impfen.pack(side="left", fill="x", expand=True, padx=2)

        self.btn_speichern = tk.Button(
            self.frame_datei,
            text="JSON Speichern 💾",
            command=self.speichern_klick,
        )
        self.btn_speichern.pack(side="left", fill="x", expand=True, padx=2)

        self.btn_laden = tk.Button(
            self.frame_datei,
            text="JSON Laden 📂",
            command=self.laden_klick,
        )
        self.btn_laden.pack(side="left", fill="x", expand=True, padx=2)

        self.btn_csv = tk.Button(
            self.frame_datei,
            text="CSV Export 📊",
            command=self.csv_export_klick,
        )
        self.btn_csv.pack(side="left", fill="x", expand=True, padx=2)

        # Statusleiste (Ganz unten)
        self.label_status = tk.Label(
            self.root,
            text="Bereit.",
            bd=1,
            relief="sunken",
            anchor="w",
            font=("Arial", 9),
            padx=5,
            pady=3,
        )
        self.label_status.pack(side="bottom", fill="x")

    def filter_setzen(self, filter_name: str) -> None:
        """Setzt den aktiven Ansichts-Filter und frischt die Listbox auf."""
        self._aktiver_filter = filter_name
        self.aktualisiere_ansicht()
        self.setze_status(f"Filter aktiv: {filter_name}", typ="info")

    def aktualisiere_ansicht(self) -> None:
        """Aktualisiert die Listbox und die Statistiken im Header."""
        if hasattr(self.label_kapazitaet, "config"):
            self.label_kapazitaet.config(
                text=f"Belegung: {len(self.tierheim)} / {self.tierheim.max_kapazitaet} Tiere | "
                     f"Ø {self.tierheim.durchschnittsalter():.1f} Jahre | Σ {self.tierheim.gesamtgewicht():.1f} kg"
            )

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
        """Setzt Nachricht und Farb-Theme der Statusleiste."""
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
        """Ermittelt das aktuell ausgewählte Tier."""
        try:
            selektion = self.listbox_tiere.curselection()
            if not selektion:
                return None
            index = selektion[0]

            # Liste abhängig vom aktiven Filter ermitteln
            if self._aktiver_filter == "Ungeimpft":
                tiere_anzeige = self.tierheim.ungeimpfte_tiere()
            elif self._aktiver_filter == "Hungrig":
                tiere_anzeige = self.tierheim.hungrige_tiere()
            elif self._aktiver_filter in ("Hund", "Katze", "Vogel"):
                tiere_anzeige = self.tierheim.filtriere_nach_art(self._aktiver_filter)
            else:
                tiere_anzeige = self.tierheim.tiere

            if 0 <= index < len(tiere_anzeige):
                return tiere_anzeige[index]
            return None
        except Exception:
            return None

    def tier_aufnehmen_klick(self) -> None:
        """Verarbeitet das Formular und nimmt ein neues Tier auf."""
        try:
            art = self.var_art.get().strip()
            name = self.var_name.get().strip()
            alter_str = self.var_alter.get().strip()
            gewicht_str = self.var_gewicht.get().strip()
            extra = self.var_extra.get().strip()
            geimpft = self.var_geimpft.get()

            if not name:
                raise ValidierungsFehler("Bitte einen Namen für das Tier eingeben!")

            try:
                alter = int(alter_str)
            except ValueError:
                raise ValidierungsFehler("Alter muss eine ganze Zahl sein!")

            try:
                gewicht = float(gewicht_str)
            except ValueError:
                raise ValidierungsFehler("Gewicht muss eine Zahl sein (z.B. 12.5)!")

            neues_tier: Tier
            if art == "Hund":
                neues_tier = Hund(
                    name=name,
                    alter=alter,
                    gewicht=gewicht,
                    rasse=extra if extra else "Mischling",
                    geimpft=geimpft,
                )
            elif art == "Katze":
                stubenrein = extra.lower() not in ("nein", "false", "0")
                neues_tier = Katze(
                    name=name,
                    alter=alter,
                    gewicht=gewicht,
                    stubenrein=stubenrein,
                    geimpft=geimpft,
                )
            elif art == "Vogel":
                try:
                    spannweite = float(extra) if extra else 25.0
                except ValueError:
                    spannweite = 25.0
                neues_tier = Vogel(
                    name=name,
                    alter=alter,
                    gewicht=gewicht,
                    spannweite_cm=spannweite,
                    kann_sprechen=False,
                    geimpft=geimpft,
                )
            else:
                neues_tier = Tier(name=name, alter=alter, gewicht=gewicht, geimpft=geimpft)

            self.tierheim.tier_aufnehmen(neues_tier)
            self.aktualisiere_ansicht()
            self.setze_status(f"{neues_tier.name} ({art}) erfolgreich aufgenommen!", typ="success")

            # Formular zurücksetzen
            self.var_name.set("")

        except TierheimFehler as e:
            self.setze_status(str(e), typ="warning")
        except Exception as e:
            self.setze_status(f"Unerwarteter Fehler: {e}", typ="error")

    def tier_fuettern_klick(self) -> None:
        tier = self.get_ausgewaehltes_tier()
        if not tier:
            self.setze_status("Bitte wähle zuerst ein Tier in der Liste aus!", typ="warning")
            return
        msg = tier.fuettern(100)
        self.aktualisiere_ansicht()
        self.setze_status(msg, typ="success")

    def tier_impfen_klick(self) -> None:
        tier = self.get_ausgewaehltes_tier()
        if not tier:
            self.setze_status("Bitte wähle zuerst ein Tier in der Liste aus!", typ="warning")
            return
        frisch = tier.impfen()
        self.aktualisiere_ansicht()
        if frisch:
            self.setze_status(f"{tier.name} wurde erfolgreich geimpft! 💉", typ="success")
        else:
            self.setze_status(f"{tier.name} war bereits geimpft.", typ="info")

    def tier_laut_klick(self) -> None:
        tier = self.get_ausgewaehltes_tier()
        if not tier:
            self.setze_status("Bitte wähle zuerst ein Tier in der Liste aus!", typ="warning")
            return
        laut = tier.mache_laut()
        self.setze_status(laut, typ="info")

    def tier_vermitteln_klick(self) -> None:
        tier = self.get_ausgewaehltes_tier()
        if not tier:
            self.setze_status("Bitte wähle zuerst ein Tier in der Liste aus!", typ="warning")
            return
        try:
            entlassen = self.tierheim.tier_entlassen(tier.name)
            self.aktualisiere_ansicht()
            self.setze_status(f"{entlassen.name} wurde erfolgreich vermittelt! 🏠🎉", typ="success")
        except TierheimFehler as e:
            self.setze_status(str(e), typ="warning")

    def alle_fuettern_klick(self) -> None:
        if not self.tierheim.tiere:
            self.setze_status("Keine Tiere zum Füttern im Heim.", typ="info")
            return
        self.tierheim.alle_fuettern(100)
        self.aktualisiere_ansicht()
        self.setze_status(f"Alle {len(self.tierheim)} Tiere wurden gefüttert! 🍲", typ="success")

    def alle_impfen_klick(self) -> None:
        anzahl = self.tierheim.alle_impfen()
        self.aktualisiere_ansicht()
        self.setze_status(f"Impfaktion beendet: {anzahl} Tiere frisch geimpft! 🩺", typ="success")

    def speichern_klick(self, dateipfad: str = "tierheim_save.json") -> None:
        try:
            self.tierheim.speichern_json(dateipfad)
            self.setze_status(f"Gespeichert: {len(self.tierheim)} Tiere in '{dateipfad}'.", typ="success")
        except Exception as e:
            self.setze_status(f"Fehler beim Speichern: {e}", typ="error")

    def laden_klick(self, dateipfad: str = "tierheim_save.json") -> None:
        try:
            self.tierheim.laden_json(dateipfad)
            self.aktualisiere_ansicht()
            self.setze_status(f"Geladen: {len(self.tierheim)} Tiere aus '{dateipfad}'.", typ="success")
        except Exception as e:
            self.setze_status(f"Fehler beim Laden: {e}", typ="error")

    def csv_export_klick(self, dateipfad: str = "tierheim_export.csv") -> None:
        try:
            self.tierheim.exportiere_csv(dateipfad)
            self.setze_status(f"CSV-Export erfolgreich erstellt: '{dateipfad}'.", typ="success")
        except Exception as e:
            self.setze_status(f"Fehler beim CSV-Export: {e}", typ="error")


# ==============================================================================
# HAUPTPROGRAMM (DEMO)
# ==============================================================================
if __name__ == "__main__":
    heim = Tierheim("Tierheim Sonnenschein", max_kapazitaet=15)
    heim.tier_aufnehmen(Hund("Bello", 3, 14.5, rasse="Beagle", geimpft=True))
    heim.tier_aufnehmen(Katze("Luna", 2, 4.2, stubenrein=True, geimpft=False))
    heim.tier_aufnehmen(Vogel("Tweety", 1, 0.3, spannweite_cm=18.0, kann_sprechen=True))

    root = tk.Tk()
    app = TierheimApp(root, heim)
    root.mainloop()
