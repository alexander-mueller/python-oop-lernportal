"""
Vorkapitel 00: Python-Detektivin – Musterlösung
==============================================
Hier ist die vollständig fehlerfreie Version des Skripts.
"""

# BUG 1 & 2 behoben: Doppelpunkt hinzugefügt und 'gesamt += 5' sauber eingerückt:
def berechne_endstand(basis_punkte, bonus):
    gesamt = basis_punkte + bonus
    if bonus > 10:
        gesamt += 5
    return gesamt


# BUG 3 behoben: Tippfehler 'spiler_punkte' -> 'spieler_punkte' korrigiert:
def punkte_multiplizieren(spieler_punkte, faktor):
    ergebnis = spieler_punkte * faktor
    return ergebnis


# BUG 4 behoben: f-String verwendet, um Zahl und Text sauber zu verbinden:
def formatierte_ausgabe(name, punkte):
    text = f"Spieler {name} hat {punkte} Punkte!"
    return text


# BUG 5 behoben: >= statt > verwendet:
def ist_sieger(punkte):
    if punkte >= 50:
        return True
    else:
        return False


if __name__ == "__main__":
    print("🕵️‍♀️ --- CODE-DETEKTIVIN QUIZ TEST (Musterlösung) --- 🕵️‍♀️")
    print("Endstand (40):", berechne_endstand(20, 15))
    print("Multipliziert (30):", punkte_multiplizieren(10, 3))
    print("Ausgabe:", formatierte_ausgabe("Mia", 50))
    print("Sieg bei 50:", ist_sieger(50))
