"""
Kapitel 06: Abschlussprojekt – Tamagotchi (Virtuelles Haustier)
==============================================================

Programmiere hier die Klasse 'Tamagotchi'.
"""

class Tamagotchi:
    # ==========================================================================
    # TODO 1: Konstruktor __init__(self, name, tierart="Drache")
    #
    # Initialisiere die folgenden Attribute:
    # - self.name = name
    # - self.tierart = tierart
    # - self.hunger = 50          (0 = pappsatt, 100 = verhungert)
    # - self.muedigkeit = 20      (0 = fit, 100 = erschöpft)
    # - self.glueck = 80          (0 = traurig, 100 = super glücklich)
    # - self.alter_tage = 0
    # - self.ist_lebendig = True
    # ==========================================================================
    def __init__(self, name, tierart="Drache"):
        # Schreibe hier deinen Code für TODO 1:
        pass

    # Hilfsmethode (optional, aber sehr nützlich):
    # Hält einen Wert zwischen minimal 0 und maximal 100.
    def _begrenze(self, wert):
        return max(0, min(100, wert))

    # ==========================================================================
    # TODO 2: Methode "fuettern(self, menge=20)"
    #
    # Regeln:
    # 1. Wenn not self.ist_lebendig:
    #    - Gib zurück: f"{self.name} reagiert nicht mehr..."
    # 2. Wenn lebendig:
    #    - Verringere 'self.hunger' um 'menge' (darf nicht unter 0 fallen).
    #    - Erhöhe 'self.glueck' um 5 (darf nicht über 100 steigen).
    #    - Erhöhe 'self.muedigkeit' um 5 (darf nicht über 100 steigen).
    #    - Gib zurück: f"{self.name} mampft genüsslich! (Hunger: {self.hunger}/100)"
    # ==========================================================================
    def fuettern(self, menge=20):
        # Schreibe hier deinen Code für TODO 2:
        pass

    # ==========================================================================
    # TODO 3: Methode "spielen(self, spass=25)"
    #
    # Regeln:
    # 1. Wenn not self.ist_lebendig:
    #    - Gib zurück: f"{self.name} reagiert nicht mehr..."
    # 2. Wenn 'self.muedigkeit' > 80 ist:
    #    - Zu müde zum Spielen! Ändere keine Werte und gib zurück:
    #      f"{self.name} ist zu müde zum Spielen und gähnt nur..."
    # 3. Wenn fit genug:
    #    - Erhöhe 'self.glueck' um 'spass' (max 100).
    #    - Erhöhe 'self.hunger' um 15 (max 100).
    #    - Erhöhe 'self.muedigkeit' um 20 (max 100).
    #    - Gib zurück: f"{self.name} hatte riesigen Spaß beim Spielen! (Glück: {self.glueck}/100)"
    # ==========================================================================
    def spielen(self, spass=25):
        # Schreibe hier deinen Code für TODO 3:
        pass

    # ==========================================================================
    # TODO 4: Methode "schlafen(self)"
    #
    # Regeln:
    # 1. Wenn not self.ist_lebendig:
    #    - Gib zurück: f"{self.name} reagiert nicht mehr..."
    # 2. Wenn lebendig:
    #    - Setze 'self.muedigkeit' auf 0.
    #    - Erhöhe 'self.hunger' um 15 (max 100).
    #    - Erhöhe 'self.alter_tage' um 1.
    #    - Gib zurück: f"{self.name} hat tief geschlafen und ist ausgeruht! Ein neuer Tag bricht an."
    # ==========================================================================
    def schlafen(self):
        # Schreibe hier deinen Code für TODO 4:
        pass

    # ==========================================================================
    # TODO 5: Methode "zeit_vergeht(self)"
    # Simuliert das Verstreichen von Zeit.
    #
    # Regeln:
    # 1. Wenn not self.ist_lebendig:
    #    - Mach nichts, gib False zurück.
    # 2. Wenn lebendig:
    #    - Erhöhe 'self.hunger' um 10 (max 100).
    #    - Erhöhe 'self.muedigkeit' um 10 (max 100).
    #    - Verringere 'self.glueck' um 10 (min 0).
    #    - Prüfe, ob das Haustier stirbt:
    #      Wenn self.hunger >= 100 oder self.glueck <= 0:
    #         self.ist_lebendig = False
    #    - Gib self.ist_lebendig zurück (True wenn noch am Leben, False wenn gestorben).
    # ==========================================================================
    def zeit_vergeht(self):
        # Schreibe hier deinen Code für TODO 5:
        pass

    # ==========================================================================
    # TODO 6: Dunder-Methode "__str__(self)"
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
        # Schreibe hier deinen Code für TODO 6:
        pass


# ==============================================================================
# Schneller Testlauf:
# ==============================================================================
if __name__ == "__main__":
    pet = Tamagotchi("Yoshi", "Dino")
    print(pet)
    print()
    print(pet.fuettern())
    print(pet.spielen())
    print(pet.schlafen())
    print(pet)
