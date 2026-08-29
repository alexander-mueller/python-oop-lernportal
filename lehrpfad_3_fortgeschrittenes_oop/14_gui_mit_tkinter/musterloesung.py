"""
Kapitel 14: Desktop-GUIs mit Tkinter & OOP 🖥️🔢
=================================================
Musterlösung: Vollständige Implementierung von ZaehlerLogik und ZaehlerApp.
"""

from typing import Optional

# ==============================================================================
# Tkinter Import mit Fallback für Headless- / Server-Umgebungen
# ==============================================================================
try:
    import tkinter as tk
except ImportError:
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

    def __init__(self, startwert: int = 0, min_wert: int = -100, max_wert: int = 100):
        self.wert: int = startwert
        self.min_wert: int = min_wert
        self.max_wert: int = max_wert
        self.schrittweite: int = 1
        self.klick_anzahl: int = 0

    def erhoehen(self) -> int:
        """Erhöht den Zählerstand um die Schrittweite (maximal bis max_wert)."""
        self.klick_anzahl += 1
        self.wert = min(self.max_wert, self.wert + self.schrittweite)
        return self.wert

    def verringern(self) -> int:
        """Verringert den Zählerstand um die Schrittweite (minimal bis min_wert)."""
        self.klick_anzahl += 1
        self.wert = max(self.min_wert, self.wert - self.schrittweite)
        return self.wert

    def zuruecksetzen(self) -> int:
        """Setzt den Zählerstand auf 0 zurück."""
        self.klick_anzahl += 1
        self.wert = 0
        return self.wert

    def setze_schrittweite(self, schritt: int) -> bool:
        """Setzt eine neue positive Schrittweite (> 0)."""
        if schritt > 0:
            self.schrittweite = schritt
            return True
        return False

    def ist_gerade(self) -> bool:
        """Gibt True zurück, wenn der Zählerstand gerade ist."""
        return self.wert % 2 == 0

    def __str__(self) -> str:
        return f"Zählerstand: {self.wert} (Schrittweite: {self.schrittweite}, Klicks: {self.klick_anzahl})"


# ==============================================================================
# TEIL 2: DIE GUI-KLASSE (VIEW & CONTROLLER)
# ==============================================================================
class ZaehlerApp:
    """
    Die Benutzeroberfläche (GUI) für den Klick-Zähler mit Tkinter.
    Erstellt Fenster, Labels, Buttons und Eingabefelder.
    """

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Python OOP Zähler 🔢")
        self.root.geometry("380x360")

        # 1. Datenmodell (Logik)
        self.logik = ZaehlerLogik(startwert=0, min_wert=-100, max_wert=100)

        # 2. Widgets erstellen & per Grid anordnen
        # Titel-Label
        self.label_titel = tk.Label(
            self.root,
            text="🔢 Python Klick-Zähler",
            font=("Arial", 16, "bold"),
        )
        self.label_titel.grid(row=0, column=0, columnspan=2, padx=15, pady=(15, 5))

        # Große Zähleranzeige
        self.label_anzeige = tk.Label(
            self.root,
            text="0",
            font=("Arial", 36, "bold"),
            fg="#4f46e5",
        )
        self.label_anzeige.grid(row=1, column=0, columnspan=2, padx=15, pady=10)

        # Info- / Statusanzeige
        self.label_info = tk.Label(
            self.root,
            text="Klicks: 0 | Gerade Zahl",
            font=("Arial", 10),
            fg="#64748b",
        )
        self.label_info.grid(row=2, column=0, columnspan=2, padx=15, pady=(0, 15))

        # Buttons zum Erhöhen und Verringern
        self.btn_plus = tk.Button(
            self.root,
            text="➕ Erhöhen",
            font=("Arial", 11, "bold"),
            bg="#10b981",
            fg="white",
            command=self.klick_plus,
        )
        self.btn_plus.grid(row=3, column=0, padx=10, pady=5, sticky="ew")

        self.btn_minus = tk.Button(
            self.root,
            text="➖ Verringern",
            font=("Arial", 11, "bold"),
            bg="#ef4444",
            fg="white",
            command=self.klick_minus,
        )
        self.btn_minus.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

        # Reset-Button
        self.btn_reset = tk.Button(
            self.root,
            text="↺ Zurücksetzen",
            font=("Arial", 10),
            command=self.klick_reset,
        )
        self.btn_reset.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

        # Container für die Schrittweite
        self.frame_schritt = tk.Frame(self.root)
        self.frame_schritt.grid(row=5, column=0, columnspan=2, padx=10, pady=(15, 10))

        self.label_schritt = tk.Label(self.frame_schritt, text="Schrittweite:")
        self.label_schritt.pack(side="left", padx=5)

        self.entry_schritt = tk.Entry(self.frame_schritt, width=6, font=("Arial", 10))
        self.entry_schritt.insert(0, "1")
        self.entry_schritt.pack(side="left", padx=5)

        self.btn_schritt = tk.Button(
            self.frame_schritt,
            text="Setzen",
            font=("Arial", 9),
            command=self.klick_schritt_setzen,
        )
        self.btn_schritt.pack(side="left", padx=5)

        # Initiale Anzeige synchronisieren
        self.aktualisiere_anzeige()

    def klick_plus(self) -> None:
        """Handler für Klick auf den Plus-Button."""
        self.logik.erhoehen()
        self.aktualisiere_anzeige()

    def klick_minus(self) -> None:
        """Handler für Klick auf den Minus-Button."""
        self.logik.verringern()
        self.aktualisiere_anzeige()

    def klick_reset(self) -> None:
        """Handler für Klick auf den Reset-Button."""
        self.logik.zuruecksetzen()
        self.aktualisiere_anzeige()

    def klick_schritt_setzen(self) -> None:
        """Handler zum Auslesen und Anwenden der Schrittweite."""
        eingabe = self.entry_schritt.get().strip()
        try:
            neuer_schritt = int(eingabe)
            if self.logik.setze_schrittweite(neuer_schritt):
                self.aktualisiere_anzeige()
            else:
                self.label_info.config(text="⚠️ Schrittweite muss größer als 0 sein!", fg="#ef4444")
        except ValueError:
            self.label_info.config(text="⚠️ Bitte eine ganze Zahl eingeben!", fg="#ef4444")

    def aktualisiere_anzeige(self) -> None:
        """Aktualisiert alle Anzeige-Elemente mit den Daten aus dem Logik-Modell."""
        # 1. Zählerstand
        self.label_anzeige.config(text=str(self.logik.wert))

        # 2. Farb-Feedback
        if self.logik.wert > 0:
            self.label_anzeige.config(fg="#10b981")  # Grün
        elif self.logik.wert < 0:
            self.label_anzeige.config(fg="#ef4444")  # Rot
        else:
            self.label_anzeige.config(fg="#4f46e5")  # Indigo

        # 3. Statusinfo
        paritaet = "Gerade" if self.logik.ist_gerade() else "Ungerade"
        info = f"Klicks: {self.logik.klick_anzahl} | {paritaet} | Schritt: {self.logik.schrittweite}"

        if self.logik.wert >= self.logik.max_wert:
            info += " (Maximum erreicht!)"
        elif self.logik.wert <= self.logik.min_wert:
            info += " (Minimum erreicht!)"

        self.label_info.config(text=info, fg="#64748b")


# ==============================================================================
# Startblock
# ==============================================================================
if __name__ == "__main__":
    print("🚀 Starte Tkinter Klick-Zähler (Musterlösung)...")
    try:
        root = tk.Tk()
        app = ZaehlerApp(root)
        print("💡 Fenster geöffnet! Schließe das Fenster, um das Programm zu beenden.")
        root.mainloop()
    except Exception as e:
        print(f"⚠️ GUI konnte nicht im Display geöffnet werden ({e}).")
        print("💡 Führe 'python3 test_aufgabe.py' aus, um deine Lösung automatisch zu prüfen!")
