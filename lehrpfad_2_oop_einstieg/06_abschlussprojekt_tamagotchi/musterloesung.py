"""
Kapitel 06: Abschlussprojekt – Tamagotchi – Musterlösung
========================================================
"""

class Tamagotchi:
    def __init__(self, name, tierart="Drache"):
        self.name = name
        self.tierart = tierart
        self.hunger = 50
        self.muedigkeit = 20
        self.glueck = 80
        self.alter_tage = 0
        self.ist_lebendig = True

    def _begrenze(self, wert):
        return max(0, min(100, wert))

    def fuettern(self, menge=20):
        if not self.ist_lebendig:
            return f"{self.name} reagiert nicht mehr..."
        
        self.hunger = self._begrenze(self.hunger - menge)
        self.glueck = self._begrenze(self.glueck + 5)
        self.muedigkeit = self._begrenze(self.muedigkeit + 5)
        return f"{self.name} mampft genüsslich! (Hunger: {self.hunger}/100)"

    def spielen(self, spass=25):
        if not self.ist_lebendig:
            return f"{self.name} reagiert nicht mehr..."
        
        if self.muedigkeit > 80:
            return f"{self.name} ist zu müde zum Spielen und gähnt nur..."
        
        self.glueck = self._begrenze(self.glueck + spass)
        self.hunger = self._begrenze(self.hunger + 15)
        self.muedigkeit = self._begrenze(self.muedigkeit + 20)
        return f"{self.name} hatte riesigen Spaß beim Spielen! (Glück: {self.glueck}/100)"

    def schlafen(self):
        if not self.ist_lebendig:
            return f"{self.name} reagiert nicht mehr..."
        
        self.muedigkeit = 0
        self.hunger = self._begrenze(self.hunger + 15)
        self.alter_tage += 1
        return f"{self.name} hat tief geschlafen und ist ausgeruht! Ein neuer Tag bricht an."

    def zeit_vergeht(self):
        if not self.ist_lebendig:
            return False
        
        self.hunger = self._begrenze(self.hunger + 10)
        self.muedigkeit = self._begrenze(self.muedigkeit + 10)
        self.glueck = self._begrenze(self.glueck - 10)

        if self.hunger >= 100 or self.glueck <= 0:
            self.ist_lebendig = False
            return False
        return True

    def __str__(self):
        if not self.ist_lebendig:
            return f"=== {self.name} ({self.tierart}) - RIP 🪦 ==="
        
        zeilen = [
            f"=== {self.name} ({self.tierart}, {self.alter_tage} Tage alt) ===",
            f"Hunger:     {self.hunger}/100",
            f"Müdigkeit:  {self.muedigkeit}/100",
            f"Glück:      {self.glueck}/100"
        ]
        return "\n".join(zeilen)


if __name__ == "__main__":
    pet = Tamagotchi("Yoshi", "Dino")
    print(pet)
    print(pet.fuettern())
    print(pet.spielen())
    print(pet.schlafen())
    print(pet)
