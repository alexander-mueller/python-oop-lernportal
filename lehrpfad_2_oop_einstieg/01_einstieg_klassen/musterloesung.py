"""
Kapitel 01: Die erste Klasse – Musterlösung
===========================================
Hier findest du die vollständige Lösung mit Erklärungen.
"""

# TODO 1: Die Klasse Haustier definieren
class Haustier:
    pass


# TODO 2: Ein Haustier-Objekt namens Bello erstellen und Attribute zuweisen
def erstelle_bello():
    tier = Haustier()
    tier.name = "Bello"
    tier.tierart = "Hund"
    tier.alter = 3
    return tier


# TODO 3: Ein Haustier-Objekt namens Mimi erstellen
def erstelle_mimi():
    tier = Haustier()
    tier.name = "Mimi"
    tier.tierart = "Katze"
    tier.alter = 5
    return tier


# TODO 4: Steckbrief generieren
def steckbrief_text(haustier):
    return f"{haustier.name} ist ein(e) {haustier.tierart} und ist {haustier.alter} Jahre alt."


# TODO 5: Das ältere Tier ermitteln
def aelteres_tier(tier1, tier2):
    if tier2.alter > tier1.alter:
        return tier2
    else:
        return tier1


if __name__ == "__main__":
    bello = erstelle_bello()
    mimi = erstelle_mimi()
    print(steckbrief_text(bello))
    print(steckbrief_text(mimi))
    aelter = aelteres_tier(bello, mimi)
    print(f"Das ältere Tier ist: {aelter.name}")
