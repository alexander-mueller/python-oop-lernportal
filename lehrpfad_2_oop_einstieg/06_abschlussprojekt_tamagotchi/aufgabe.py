"""
Kapitel 06: Abschlussprojekt – Tamagotchi (Virtuelles Haustier)
==============================================================

Programmiere hier die Klasse 'Tamagotchi'.
"""

class Tamagotchi:
    # ==========================================================================
    # 🎯 TEILZIEL 1 (TODO 1): Konstruktor __init__(self, name, tierart="Drache")
    #
    # Initialisiere die folgenden Attribute an self:
    # - self.name = name
    # - self.tierart = tierart
    # - self.hunger = 50          (0 = pappsatt, 100 = verhungert)
    # - self.muedigkeit = 20      (0 = fit, 100 = erschöpft)
    # - self.glueck = 80          (0 = traurig, 100 = super glücklich)
    # - self.alter_tage = 0
    # - self.ist_lebendig = True
    # ==========================================================================
    def __init__(self, name, tierart="Drache"):
        # 🎯 TEILZIEL 1: Implementiere die Logik Schritt für Schritt:
    # 💡 Tipp: Beachte Datentypen und das abschließende return!
        pass

    # Hilfsmethode: Begrenzt Werte immer zwischen min_wert (0) und max_wert (100)
    def _begrenze(self, wert, min_wert=0, max_wert=100):
        return max(min_wert, min(max_wert, wert))

    # ==========================================================================
    # 🎯 TEILZIEL 2 (TODO 2): Methode "fuettern(self, menge=20)"
    #
    # Regeln:
    # 1. Wenn not self.ist_lebendig:
    #    - Gib zurück: f"{self.name} reagiert nicht mehr..."
    # 2. Wenn lebendig:
    #    - Verringere self.hunger um menge (mit _begrenze, darf nicht unter 0 fallen).
    #    - Erhöhe self.glueck um 5 (max 100).
    #    - Erhöhe self.muedigkeit um 5 (max 100).
    #    - Gib zurück: f"{self.name} mampft genüsslich! (Hunger: {self.hunger}/100)"
    # ==========================================================================
    def fuettern(self, menge=20):
        # 🎯 TEILZIEL 2: Implementiere die Logik Schritt für Schritt:
    # 💡 Tipp: Beachte Datentypen und das abschließende return!
        pass

    # ==========================================================================
    # 🎯 TEILZIEL 3 (TODO 3): Methode "spielen(self, spass=25)"
    #
    # Regeln:
    # 1. Wenn not self.ist_lebendig:
    #    - Gib zurück: f"{self.name} reagiert nicht mehr..."
    # 2. Wenn self.muedigkeit > 80 ist:
    #    - Zu müde zum Spielen! Ändere keine Werte und gib zurück:
    #      f"{self.name} ist zu müde zum Spielen und gähnt nur..."
    # 3. Wenn fit genug:
    #    - Erhöhe self.glueck um spass (max 100).
    #    - Erhöhe self.hunger um 15 (max 100).
    #    - Erhöhe self.muedigkeit um 20 (max 100).
    #    - Gib zurück: f"{self.name} hatte riesigen Spaß beim Spielen! (Glück: {self.glueck}/100)"
    # ==========================================================================
    def spielen(self, spass=25):
        # 🎯 TEILZIEL 3: Implementiere die Logik Schritt für Schritt:
    # 💡 Tipp: Beachte Datentypen und das abschließende return!
        pass

    # ==========================================================================
    # 🎯 TEILZIEL 4 (TODO 4): Methode "schlafen(self)"
    #
    # Regeln:
    # 1. Wenn not self.ist_lebendig:
    #    - Gib zurück: f"{self.name} reagiert nicht mehr..."
    # 2. Wenn lebendig:
    #    - Setze self.muedigkeit auf 0.
    #    - Erhöhe self.hunger um 15 (max 100).
    #    - Erhöhe self.alter_tage um 1.
    #    - Gib zurück: f"{self.name} hat tief geschlafen und ist ausgeruht! Ein neuer Tag bricht an."
    # ==========================================================================
    def schlafen(self):
        # 🎯 TEILZIEL 4: Implementiere die Logik Schritt für Schritt:
    # 💡 Tipp: Beachte Datentypen und das abschließende return!
        pass

    # ==========================================================================
    # 🎯 TEILZIEL 5 (TODO 5): Methode "zeit_vergeht(self)"
    # Simuliert das Verstreichen von Zeit.
    #
    # Regeln:
    # 1. Wenn not self.ist_lebendig:
    #    - Mach nichts, gib False zurück.
    # 2. Wenn lebendig:
    #    - Erhöhe self.hunger um 10 (max 100).
    #    - Erhöhe self.muedigkeit um 10 (max 100).
    #    - Verringere self.glueck um 10 (min 0).
    #    - Prüfe, ob das Haustier stirbt:
    #      Wenn self.hunger >= 100 oder self.glueck <= 0:
    #         self.ist_lebendig = False
    #    - Gib self.ist_lebendig zurück (True wenn noch am Leben, False wenn gestorben).
    # ==========================================================================
    def zeit_vergeht(self):
        # 🎯 TEILZIEL 5: Implementiere die Logik Schritt für Schritt:
    # 💡 Tipp: Beachte Datentypen und das abschließende return!
        pass

    # ==========================================================================
    # 🎯 TEILZIEL 6 (TODO 6): Dunder-Methode "__str__(self)"
    # Gibt eine hübsche Statusübersicht als mehrzeiligen String zurück.
    #
    # Format (wenn lebendig):
    # "=== {self.name} ({self.tierart}, {self.alter_tage} Tage alt) ===\n"
    # "Hunger:     {self.hunger}/100\n"
    # "Müdigkeit:  {self.muedigkeit}/100\n"
    # "Glück:      {self.glueck}/100"
    #
    # Format (wenn tot / not self.ist_lebendig):
    # "=== {self.name} ({self.tierart}) - RIP 🪦 ==="
    # ==========================================================================
    def __str__(self):
        # 🎯 TEILZIEL 6: Implementiere die Logik Schritt für Schritt:
    # 💡 Tipp: Beachte Datentypen und das abschließende return!
        pass


# ==============================================================================
# Schneller Testlauf:
# (Ausführen mit 'python3 aufgabe.py' oder starte 'python3 tamagotchi_spiel.py')
# ==============================================================================
if __name__ == "__main__":
    pet = Tamagotchi("Yoshi", "Dino")
    if hasattr(pet, "name") and pet.name:
        print(pet)
        print()
        print(pet.fuettern())
        print(pet.spielen())
        print(pet.schlafen())
        print(pet)
    else:
        print("💡 Hinweis: Implementiere erst die TODOs, um Yoshi zum Leben zu erwecken!")
