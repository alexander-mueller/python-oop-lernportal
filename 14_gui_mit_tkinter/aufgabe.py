"""
Kapitel 14: Desktop-GUIs mit Tkinter & OOP 🖥️🔢
=================================================
Aufgabe: Erstelle eine modulare Klick-Zähler- & Rechner-Applikation
mit sauberer Trennung von Logik (Model) und Benutzeroberfläche (View/Controller).

1. ZaehlerLogik: Verwaltet den Wert, Grenzwerte und Schrittweiten (Headless / Reines Python).
2. ZaehlerApp: Erzeugt das Tkinter-Fenster, platziert Buttons & Labels und fängt Klicks ab.
"""

from typing import Optional

# ==============================================================================
# Tkinter Import mit Fallback für Headless- / Server-Umgebungen
# ==============================================================================
try:
    import tkinter as tk
except ImportError:
    # Headless Mock-Objekte (ermöglicht Ausführung und Tests auch ohne GUI-Server)
    class _MockWidget:
        def __init__(self, master=None, text="", **kwargs):
            self.master = master
            self._config = dict(kwargs)
            if text:
                self._config["text"] = text
            self._entry_text = str(kwargs.get("textvariable", text))

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

        def delete(self, first=0, last=None):
            self._entry_text = ""

        def insert(self, index, string):
            self._entry_text = str(string)

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

    class _MockTkModule:
        Tk = _MockTk
        Label = _MockWidget
        Button = _MockWidget
        Entry = _MockWidget
        Frame = _MockWidget

    tk = _MockTkModule()


# ==============================================================================
# TEIL 1: DIE LOGIK-KLASSE (MODEL)
# ==============================================================================
class ZaehlerLogik:
    """
    Das Datenmodell (Model) des Klick-Zählers.
    Verwaltet den aktuellen Zählerstand, Grenzwerte und Schrittweiten.
    Komplett unabhängig von Tkinter (reines Python).
    """

    # ==========================================================================
    # TODO 1: Konstruktor __init__
    # Parameter:
    #   - startwert (int, Standard: 0)
    #   - min_wert (int, Standard: -100)
    #   - max_wert (int, Standard: 100)
    # Attribute initialisieren:
    #   - self.wert: int = startwert
    #   - self.min_wert: int = min_wert
    #   - self.max_wert: int = max_wert
    #   - self.schrittweite: int = 1
    #   - self.klick_anzahl: int = 0
    # ==========================================================================
    def __init__(self, startwert: int = 0, min_wert: int = -100, max_wert: int = 100):
        pass

    # ==========================================================================
    # TODO 2a: Methode erhoehen(self) -> int
    # 1. Erhöhe self.klick_anzahl um 1.
    # 2. Addiere self.schrittweite zu self.wert, aber maximal bis self.max_wert!
    #    Tipp: min(self.max_wert, self.wert + self.schrittweite)
    # 3. Gib den neuen self.wert zurück.
    # ==========================================================================
    def erhoehen(self) -> int:
        pass

    # ==========================================================================
    # TODO 2b: Methode verringern(self) -> int
    # 1. Erhöhe self.klick_anzahl um 1.
    # 2. Subtrahiere self.schrittweite von self.wert, aber minimal bis self.min_wert!
    #    Tipp: max(self.min_wert, self.wert - self.schrittweite)
    # 3. Gib den neuen self.wert zurück.
    # ==========================================================================
    def verringern(self) -> int:
        pass

    # ==========================================================================
    # TODO 2c: Methode zuruecksetzen(self) -> int
    # 1. Erhöhe self.klick_anzahl um 1.
    # 2. Setze self.wert auf 0 zurück.
    # 3. Gib den neuen self.wert (0) zurück.
    # ==========================================================================
    def zuruecksetzen(self) -> int:
        pass

    # ==========================================================================
    # TODO 3a: Methode setze_schrittweite(self, schritt: int) -> bool
    # Wenn schritt > 0 ist:
    #   - Setze self.schrittweite = schritt
    #   - Gib True zurück
    # Wenn schritt <= 0 ist:
    #   - Verändere die Schrittweite nicht und gib False zurück
    # ==========================================================================
    def setze_schrittweite(self, schritt: int) -> bool:
        pass

    # ==========================================================================
    # TODO 3b: Methode ist_gerade(self) -> bool
    # Gibt True zurück, wenn self.wert eine gerade Zahl ist (wert % 2 == 0),
    # andernfalls False.
    # ==========================================================================
    def ist_gerade(self) -> bool:
        pass

    # ==========================================================================
    # TODO 3c: Dunder-Methode __str__(self) -> str
    # Gibt einen formatierten String zurück:
    # "Zählerstand: <wert> (Schrittweite: <schrittweite>, Klicks: <klick_anzahl>)"
    # ==========================================================================
    def __str__(self) -> str:
        pass


# ==============================================================================
# TEIL 2: DIE GUI-KLASSE (VIEW & CONTROLLER)
# ==============================================================================
class ZaehlerApp:
    """
    Die Benutzeroberfläche (GUI) für den Klick-Zähler mit Tkinter.
    Erstellt Fenster, Labels, Buttons und Eingabefelder.
    """

    # ==========================================================================
    # TODO 4: Konstruktor __init__(self, root: tk.Tk)
    # Parameter: root (das Tkinter-Hauptfenster)
    #
    # 1. Speichere das Fenster:
    #    self.root = root
    #    self.root.title("Python OOP Zähler 🔢")
    #    self.root.geometry("380x360")
    #
    # 2. Erstelle eine Instanz der Logik-Klasse:
    #    self.logik = ZaehlerLogik(startwert=0, min_wert=-100, max_wert=100)
    #
    # 3. Erstelle und platziere alle Widgets:
    #    - self.label_titel: tk.Label(self.root, text="🔢 Python Klick-Zähler", font=("Arial", 16, "bold"))
    #      Platzierung mit .grid(row=0, column=0, columnspan=2, padx=15, pady=(15, 5))
    #
    #    - self.label_anzeige: tk.Label(self.root, text="0", font=("Arial", 36, "bold"))
    #      Platzierung mit .grid(row=1, column=0, columnspan=2, padx=15, pady=10)
    #
    #    - self.label_info: tk.Label(self.root, text="Klicks: 0 | Gerade Zahl", font=("Arial", 10))
    #      Platzierung mit .grid(row=2, column=0, columnspan=2, padx=15, pady=(0, 15))
    #
    #    - self.btn_plus: tk.Button(self.root, text="➕ Erhöhen", font=("Arial", 11, "bold"), command=self.klick_plus)
    #      Platzierung mit .grid(row=3, column=0, padx=10, pady=5, sticky="ew")
    #
    #    - self.btn_minus: tk.Button(self.root, text="➖ Verringern", font=("Arial", 11, "bold"), command=self.klick_minus)
    #      Platzierung mit .grid(row=3, column=1, padx=10, pady=5, sticky="ew")
    #
    #    - self.btn_reset: tk.Button(self.root, text="↺ Zurücksetzen", font=("Arial", 10), command=self.klick_reset)
    #      Platzierung mit .grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="ew")
    #
    #    - Container für Schrittweite:
    #      self.frame_schritt = tk.Frame(self.root)
    #      self.frame_schritt.grid(row=5, column=0, columnspan=2, padx=10, pady=(15, 10))
    #
    #      self.label_schritt = tk.Label(self.frame_schritt, text="Schrittweite:")
    #      self.label_schritt.pack(side="left", padx=5)
    #
    #      self.entry_schritt = tk.Entry(self.frame_schritt, width=6, font=("Arial", 10))
    #      self.entry_schritt.insert(0, "1")
    #      self.entry_schritt.pack(side="left", padx=5)
    #
    #      self.btn_schritt = tk.Button(self.frame_schritt, text="Setzen", command=self.klick_schritt_setzen)
    #      self.btn_schritt.pack(side="left", padx=5)
    #
    # 4. Rufe am Ende self.aktualisiere_anzeige() auf, um die Startwerte anzuzeigen!
    # ==========================================================================
    def __init__(self, root: tk.Tk):
        pass

    # ==========================================================================
    # TODO 5a: Methode klick_plus(self) -> None
    # 1. Rufe self.logik.erhoehen() auf.
    # 2. Rufe self.aktualisiere_anzeige() auf.
    # ==========================================================================
    def klick_plus(self) -> None:
        pass

    # ==========================================================================
    # TODO 5b: Methode klick_minus(self) -> None
    # 1. Rufe self.logik.verringern() auf.
    # 2. Rufe self.aktualisiere_anzeige() auf.
    # ==========================================================================
    def klick_minus(self) -> None:
        pass

    # ==========================================================================
    # TODO 5c: Methode klick_reset(self) -> None
    # 1. Rufe self.logik.zuruecksetzen() auf.
    # 2. Rufe self.aktualisiere_anzeige() auf.
    # ==========================================================================
    def klick_reset(self) -> None:
        pass

    # ==========================================================================
    # TODO 5d: Methode klick_schritt_setzen(self) -> None
    # 1. Hole den Text aus self.entry_schritt mit self.entry_schritt.get().strip()
    # 2. Versuche (try-except) den Text mit int() in eine Ganzzahl umzuwandeln.
    # 3. Wenn die Umwandlung klappt:
    #    - Rufe self.logik.setze_schrittweite(neuer_wert) auf.
    #    - Wenn setze_schrittweite True liefert: self.aktualisiere_anzeige() aufrufen.
    #    - Wenn False geliefert wird: self.label_info.config(text="⚠️ Schrittweite muss > 0 sein!")
    # 4. Wenn ein ValueError auftritt (z.B. Buchstabe eingegeben):
    #    - Setze self.label_info.config(text="⚠️ Bitte eine ganze Zahl eingeben!")
    # ==========================================================================
    def klick_schritt_setzen(self) -> None:
        pass

    # ==========================================================================
    # TODO 6: Methode aktualisiere_anzeige(self) -> None
    # Synchronisiert die Oberfläche mit den aktuellen Werten aus self.logik:
    #
    # 1. Hauptanzeige:
    #    self.label_anzeige.config(text=str(self.logik.wert))
    #
    # 2. Info-Text zusammenbauen:
    #    paritaet = "Gerade" if self.logik.ist_gerade() else "Ungerade"
    #    info = f"Klicks: {self.logik.klick_anzahl} | {paritaet} | Schritt: {self.logik.schrittweite}"
    #    if self.logik.wert >= self.logik.max_wert:
    #        info += " (Maximum erreicht!)"
    #    elif self.logik.wert <= self.logik.min_wert:
    #        info += " (Minimum erreicht!)"
    #    self.label_info.config(text=info)
    # ==========================================================================
    def aktualisiere_anzeige(self) -> None:
        pass


# ==============================================================================
# Startblock: Führe dieses Skript aus (python3 aufgabe.py), um die GUI zu testen!
# ==============================================================================
if __name__ == "__main__":
    print("🚀 Starte Tkinter Klick-Zähler...")
    try:
        root = tk.Tk()
        app = ZaehlerApp(root)
        print("💡 Fenster geöffnet! Schließe das Fenster, um das Programm zu beenden.")
        root.mainloop()
    except Exception as e:
        print(f"⚠️ GUI konnte nicht im Display geöffnet werden ({e}).")
        print("💡 Führe 'python3 test_aufgabe.py' aus, um deine Lösung automatisch zu prüfen!")
