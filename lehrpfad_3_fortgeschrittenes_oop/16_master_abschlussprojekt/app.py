#!/usr/bin/env python3
"""
Kapitel 16: Master-Abschlussprojekt – Desktop App Launcher 🐾🖥️
===============================================================
Startet die vollwertige grafische Desktop-Applikation 'Tierheim & PetCare Pro'.

Ausführen mit:
    python3 app.py
"""

import sys
from pathlib import Path

# Pfad hinzufügen, um Module des Kapitels sauber zu importieren
sys.path.insert(0, str(Path(__file__).parent))

try:
    import tkinter as tk
    from tkinter import messagebox
    TK_AVAILABLE = True
except ImportError:
    TK_AVAILABLE = False

# Importiere Klassen aus aufgabe oder musterloesung
try:
    from musterloesung import Tierheim, TierheimApp, Hund, Katze, Vogel
except ImportError:
    from aufgabe import Tierheim, TierheimApp, Hund, Katze, Vogel


def starte_musterdaten_tierheim() -> Tierheim:
    """Erstellt ein Tierheim mit liebevoll gestalteten Beispieltieren."""
    heim = Tierheim(name="Tierheim Sonnenschein & Pfotenglück", max_kapazitaet=15)
    
    # Beispieldaten hinzufügen
    bello = Hund("Bello", alter=3, gewicht=16.5, rasse="Golden Retriever", geimpft=True, hunger=30, gassigegangen=True)
    luna = Katze("Luna", alter=2, gewicht=4.1, stubenrein=True, geimpft=True, hunger=40)
    rocky = Hund("Rocky", alter=5, gewicht=22.0, rasse="Deutscher Schäferhund", geimpft=False, hunger=70)
    mimi = Katze("Mimi", alter=1, gewicht=3.2, stubenrein=True, geimpft=False, hunger=60)
    tweety = Vogel("Tweety", alter=1, gewicht=0.25, spannweite_cm=18.5, kann_sprechen=True, geimpft=True, hunger=20)
    charly = Vogel("Charly", alter=4, gewicht=0.45, spannweite_cm=28.0, kann_sprechen=False, geimpft=False, hunger=80)

    for t in (bello, luna, rocky, mimi, tweety, charly):
        heim.tier_aufnehmen(t)

    return heim


def main():
    print("=" * 65)
    print("🐾 Tierheim- & PetCare-Manager Pro (Master-Abschlussprojekt)")
    print("=" * 65)

    if not TK_AVAILABLE:
        print("⚠️ Hinweis: Tkinter ist auf diesem System nicht verfügbar.")
        print("💡 Führe 'python3 test_aufgabe.py' aus, um das System headless zu testen!")
        return

    try:
        root = tk.Tk()
        heim = starte_musterdaten_tierheim()
        app = TierheimApp(root, heim)
        print(f"✨ GUI erfolgreich gestartet mit {len(heim)} Beispieltieren.")
        print("🖥️ Schließe das Fenster, um die Anwendung zu beenden.")
        root.mainloop()
    except Exception as e:
        print(f"⚠️ Konnte GUI nicht im Display anzeigen: {e}")
        print("💡 Auf Servern ohne Monitor (Headless) kannst du die Logik mit 'python3 test_aufgabe.py' prüfen.")


if __name__ == "__main__":
    main()
