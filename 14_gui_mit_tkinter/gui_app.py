#!/usr/bin/env python3
"""
Kapitel 14: Grafische Desktop-Anwendung (Startbares Skript) 🖥️✨
================================================================
Führe diese Datei auf deinem Desktop aus (z.B. in VS Code auf Mac/Windows/Linux):
    python3 gui_app.py

Features dieser erweiterten Version:
- Saubere Model-View-Controller (MVC) Architektur
- Farb-Feedback (Grün bei positiven, Rot bei negativen Zahlen)
- Tastatur-Shortcuts:
    [Pfeil nach oben]   -> Erhöhen
    [Pfeil nach unten]  -> Verringern
    [R]                 -> Zurücksetzen
- Warnung bei Grenzwert-Überschreitungen
"""

import sys
from typing import Optional

try:
    import tkinter as tk
    from tkinter import messagebox
    TK_AVAILABLE = True
except ImportError:
    TK_AVAILABLE = False
    class _MockWidget:
        def __init__(self, *args, **kwargs): pass
        def pack(self, *args, **kwargs): pass
        def grid(self, *args, **kwargs): pass
        def columnconfigure(self, *args, **kwargs): pass
        def bind(self, *args, **kwargs): pass
        def config(self, *args, **kwargs): pass
        def insert(self, *args, **kwargs): pass
        def delete(self, *args, **kwargs): pass
        def get(self): return "1"

    class _MockTkModule:
        Tk = _MockWidget
        Label = _MockWidget
        Button = _MockWidget
        Entry = _MockWidget
        Frame = _MockWidget
        LabelFrame = _MockWidget

    tk = _MockTkModule()
    messagebox = None


class ZaehlerLogik:
    """Modell für Zähler, Grenzwerte und Schrittweite."""

    def __init__(self, startwert: int = 0, min_wert: int = -100, max_wert: int = 100):
        self.wert: int = startwert
        self.min_wert: int = min_wert
        self.max_wert: int = max_wert
        self.schrittweite: int = 1
        self.klick_anzahl: int = 0

    def erhoehen(self) -> int:
        self.klick_anzahl += 1
        self.wert = min(self.max_wert, self.wert + self.schrittweite)
        return self.wert

    def verringern(self) -> int:
        self.klick_anzahl += 1
        self.wert = max(self.min_wert, self.wert - self.schrittweite)
        return self.wert

    def zuruecksetzen(self) -> int:
        self.klick_anzahl += 1
        self.wert = 0
        return self.wert

    def setze_schrittweite(self, schritt: int) -> bool:
        if schritt > 0:
            self.schrittweite = schritt
            return True
        return False

    def ist_gerade(self) -> bool:
        return self.wert % 2 == 0

    def __str__(self) -> str:
        return f"Zählerstand: {self.wert} (Schritt: {self.schrittweite})"


class DesktopZaehlerGUI:
    """Moderne grafische Desktop-Benutzeroberfläche mit Tkinter."""

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Python OOP • Desktop Zähler 🔢")
        self.root.geometry("420x440")
        self.root.minsize(360, 400)
        self.root.configure(bg="#f8fafc")

        self.logik = ZaehlerLogik(startwert=0, min_wert=-100, max_wert=100)

        # UI Komponenten aufbauen
        self._erstelle_widgets()
        self._binde_tasten()
        self.aktualisiere_anzeige()

    def _erstelle_widgets(self):
        # 1. Header Frame
        frame_header = tk.Frame(self.root, bg="#4f46e5", pady=14)
        frame_header.pack(fill="x")

        self.label_titel = tk.Label(
            frame_header,
            text="🔢 Python Desktop Zähler",
            font=("Helvetica", 16, "bold"),
            bg="#4f46e5",
            fg="white",
        )
        self.label_titel.pack()

        self.label_sub = tk.Label(
            frame_header,
            text="Kapitel 14 • Tkinter & OOP",
            font=("Helvetica", 9),
            bg="#4f46e5",
            fg="#c7d2fe",
        )
        self.label_sub.pack()

        # 2. Haupt-Anzeige Frame
        frame_card = tk.Frame(self.root, bg="#ffffff", bd=1, relief="solid", padx=20, pady=15)
        frame_card.pack(fill="x", padx=25, pady=15)

        self.label_anzeige = tk.Label(
            frame_card,
            text="0",
            font=("Helvetica", 42, "bold"),
            bg="#ffffff",
            fg="#4f46e5",
        )
        self.label_anzeige.pack(pady=(5, 0))

        self.label_info = tk.Label(
            frame_card,
            text="Klicks: 0 | Gerade Zahl",
            font=("Helvetica", 10),
            bg="#ffffff",
            fg="#64748b",
        )
        self.label_info.pack(pady=(0, 5))

        # 3. Button Steuerungsbereich
        frame_buttons = tk.Frame(self.root, bg="#f8fafc")
        frame_buttons.pack(fill="x", padx=25, pady=5)
        frame_buttons.columnconfigure(0, weight=1)
        frame_buttons.columnconfigure(1, weight=1)

        self.btn_plus = tk.Button(
            frame_buttons,
            text="➕ Erhöhen  [↑]",
            font=("Helvetica", 11, "bold"),
            bg="#10b981",
            fg="white",
            activebackground="#059669",
            activeforeground="white",
            relief="flat",
            pady=8,
            cursor="hand2",
            command=self.klick_plus,
        )
        self.btn_plus.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.btn_minus = tk.Button(
            frame_buttons,
            text="➖ Verringern  [↓]",
            font=("Helvetica", 11, "bold"),
            bg="#ef4444",
            fg="white",
            activebackground="#dc2626",
            activeforeground="white",
            relief="flat",
            pady=8,
            cursor="hand2",
            command=self.klick_minus,
        )
        self.btn_minus.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        self.btn_reset = tk.Button(
            frame_buttons,
            text="↺ Zurücksetzen  [R]",
            font=("Helvetica", 10),
            bg="#e2e8f0",
            fg="#1e293b",
            activebackground="#cbd5e1",
            relief="flat",
            pady=6,
            cursor="hand2",
            command=self.klick_reset,
        )
        self.btn_reset.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        # 4. Schrittweite Konfiguration
        frame_settings = tk.LabelFrame(
            self.root,
            text=" ⚙️ Einstellungen ",
            font=("Helvetica", 9, "bold"),
            bg="#f8fafc",
            fg="#475569",
            padx=10,
            pady=8,
        )
        frame_settings.pack(fill="x", padx=25, pady=10)

        tk.Label(frame_settings, text="Schrittweite:", bg="#f8fafc", font=("Helvetica", 10)).pack(
            side="left", padx=5
        )

        self.entry_schritt = tk.Entry(
            frame_settings, width=6, font=("Helvetica", 11), justify="center"
        )
        self.entry_schritt.insert(0, "1")
        self.entry_schritt.pack(side="left", padx=5)

        self.btn_schritt = tk.Button(
            frame_settings,
            text="Übernehmen",
            font=("Helvetica", 9),
            bg="#6366f1",
            fg="white",
            relief="flat",
            cursor="hand2",
            command=self.klick_schritt_setzen,
        )
        self.btn_schritt.pack(side="left", padx=5)

    def _binde_tasten(self):
        """Bindet bequeme Tastatur-Shortcuts an das Fenster."""
        self.root.bind("<Up>", lambda event: self.klick_plus())
        self.root.bind("<Down>", lambda event: self.klick_minus())
        self.root.bind("<r>", lambda event: self.klick_reset())
        self.root.bind("<R>", lambda event: self.klick_reset())
        self.root.bind("<Return>", lambda event: self.klick_schritt_setzen())

    def klick_plus(self) -> None:
        self.logik.erhoehen()
        self.aktualisiere_anzeige()

    def klick_minus(self) -> None:
        self.logik.verringern()
        self.aktualisiere_anzeige()

    def klick_reset(self) -> None:
        self.logik.zuruecksetzen()
        self.aktualisiere_anzeige()

    def klick_schritt_setzen(self) -> None:
        eingabe = self.entry_schritt.get().strip()
        try:
            schritt = int(eingabe)
            if self.logik.setze_schrittweite(schritt):
                self.aktualisiere_anzeige()
            else:
                self.label_info.config(
                    text="⚠️ Schrittweite muss größer als 0 sein!", fg="#ef4444"
                )
        except ValueError:
            self.label_info.config(
                text="⚠️ Bitte eine ganze Zahl eingeben!", fg="#ef4444"
            )

    def aktualisiere_anzeige(self) -> None:
        # Zählerwert darstellen
        self.label_anzeige.config(text=str(self.logik.wert))

        # Farb-Feedback
        if self.logik.wert > 0:
            self.label_anzeige.config(fg="#10b981")  # Grün
        elif self.logik.wert < 0:
            self.label_anzeige.config(fg="#ef4444")  # Rot
        else:
            self.label_anzeige.config(fg="#4f46e5")  # Neutral

        # Info-Text
        paritaet = "Gerade" if self.logik.ist_gerade() else "Ungerade"
        info = f"Klicks: {self.logik.klick_anzahl} | {paritaet} | Schritt: {self.logik.schrittweite}"

        if self.logik.wert >= self.logik.max_wert:
            info += " ⚠️ Max erreicht!"
        elif self.logik.wert <= self.logik.min_wert:
            info += " ⚠️ Min erreicht!"

        self.label_info.config(text=info, fg="#64748b")


def main():
    if not TK_AVAILABLE:
        print("=" * 60)
        print("⚠️ Hinweis: Tkinter ist in dieser Linux-Umgebung nicht installiert.")
        print("Um die grafische Oberfläche mit echtem Fenster zu sehen:")
        print("  1. Klone oder öffne diesen Ordner auf deinem PC/Laptop (Windows/Mac/Linux).")
        print("  2. Führe 'python3 gui_app.py' aus!")
        print("=" * 60)
        return

    try:
        root = tk.Tk()
        app = DesktopZaehlerGUI(root)
        print("🖥️ GUI-Fenster gestartet! Schließe das Fenster zum Beenden.")
        root.mainloop()
    except Exception as e:
        print(f"⚠️ Konnte GUI nicht initialisieren (kein X11-Display gefunden): {e}")
        print("💡 Teste deinen Code headless mit: python3 test_aufgabe.py")


if __name__ == "__main__":
    main()
