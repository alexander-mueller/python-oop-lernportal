#!/usr/bin/env python3
"""
🎮 TAMAGOTCHI TERMINAL SPIEL 🎮
===============================
Führe dieses Skript aus, um dein Tamagotchi live im Terminal zu spielen:
    python3 tamagotchi_spiel.py
"""

import sys
import time

try:
    from aufgabe import Tamagotchi
except ImportError:
    from musterloesung import Tamagotchi


def zeichne_balken(wert, max_wert=100, laenge=15, umgekehrt=False):
    """Erzeugt einen visuellen Ladebalken."""
    gefuellt = int((wert / max_wert) * laenge)
    ungefuellt = laenge - gefuellt
    
    if umgekehrt:
        # Bei Hunger/Müdigkeit ist weniger besser (grün -> rot)
        farbe = "🟢" if wert < 40 else ("🟡" if wert < 75 else "🔴")
    else:
        # Bei Glück ist mehr besser
        farbe = "🟢" if wert > 60 else ("🟡" if wert > 30 else "🔴")
        
    balken = "█" * gefuellt + "░" * ungefuellt
    return f"[{balken}] {wert:3d}% {farbe}"


def zeige_tamagotchi_dashboard(pet):
    print("\n" + "=" * 45)
    print(f"       🥚 VIRTUAL PET: {pet.name.upper()} 🥚")
    print(f"       Tierart: {pet.tierart} | Alter: {pet.alter_tage} Tag(e)")
    print("=" * 45)
    
    if not pet.ist_lebendig:
        print("\n        🪦  R. I. P.  🪦")
        print(f"   {pet.name} ist leider verstorben...")
        print("=" * 45 + "\n")
        return

    print(f" 🍖 Hunger:     {zeichne_balken(pet.hunger, umgekehrt=True)}")
    print(f" 💤 Müdigkeit:  {zeichne_balken(pet.muedigkeit, umgekehrt=True)}")
    print(f" 💖 Glück:      {zeichne_balken(pet.glueck)}")
    print("=" * 45)


def main():
    print("\n" + "*" * 50)
    print("      WILLKOMMEN BEIM TAMAGOTCHI SIMULATOR!")
    print("*" * 50)
    
    name = input("\nWie soll dein Haustier heißen? (z.B. Yoshi): ").strip()
    if not name:
        name = "Yoshi"
        
    tierart = input(f"Welche Tierart ist {name}? (z.B. Drache / Katze / Pinguin): ").strip()
    if not tierart:
        tierart = "Drache"

    pet = Tamagotchi(name, tierart)
    print(f"\n🎉 Herzlichen Glückwunsch! {pet.name} das {pet.tierart}-Baby ist geschlüpft!\n")

    while pet.ist_lebendig:
        zeige_tamagotchi_dashboard(pet)
        print("\nWas möchtest du tun?")
        print("  [1] 🍎 Füttern")
        print("  [2] ⚽ Spielen")
        print("  [3] 💤 Schlafen legen")
        print("  [4] ⏳ Nichts tun (Zeit vergeht)")
        print("  [q] 🚪 Spiel beenden")

        wahl = input("\nDeine Wahl (1/2/3/4/q): ").strip().lower()

        nachricht = ""
        if wahl == "1":
            nachricht = pet.fuettern()
        elif wahl == "2":
            nachricht = pet.spielen()
        elif wahl == "3":
            nachricht = pet.schlafen()
        elif wahl == "4":
            nachricht = f"Du schaust {pet.name} eine Weile beim Dösen zu..."
        elif wahl == "q":
            print(f"\nTschüss! Pass gut auf {pet.name} auf!\n")
            break
        else:
            print("❌ Ungültige Eingabe, bitte wähle 1, 2, 3, 4 oder q.")
            continue

        # Wenn eine Aktion ausgeführt wurde, vergeht auch etwas Zeit:
        if wahl in ("1", "2", "4"):
            pet.zeit_vergeht()

        print("\n👉 " + nachricht)
        time.sleep(0.5)

    if not pet.ist_lebendig:
        zeige_tamagotchi_dashboard(pet)
        print("Game Over! Versuche es beim nächsten Mal besser zu versorgen.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nSpiel abgebrochen. Auf Wiedersehen!")
