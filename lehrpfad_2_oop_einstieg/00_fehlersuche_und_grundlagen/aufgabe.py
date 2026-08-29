"""
Vorkapitel 00: Python-Detektivin – Finde die 5 versteckten Fehler!
==================================================================

In diesem Skript haben sich 5 typische Python-Fehler eingeschlichen.
Führe das Skript mit 'python3 aufgabe.py' aus, lies die Fehlermeldungen
und behebe die Fehler der Reihe nach von BUG 1 bis BUG 5.
"""

# ==============================================================================
# BUG 1 & BUG 2: SyntaxError & IndentationError
# In dieser Funktion fehlen ein Doppelpunkt ':' und die Einrückung stimmt nicht!
# ==============================================================================
def berechne_endstand(basis_punkte, bonus)
    gesamt = basis_punkte + bonus
    if bonus > 10:
    gesamt += 5  # Hier ist ein Einrückungsfehler!
    return gesamt


# ==============================================================================
# BUG 3: NameError
# Hier hat sich ein Tippfehler bei einem Variablennamen eingeschlichen!
# ==============================================================================
def punkte_multiplizieren(spieler_punkte, faktor):
    # Finde den Tippfehler im Variablennamen:
    ergebnis = spiler_punkte * faktor
    return ergebnis


# ==============================================================================
# BUG 4: TypeError
# Hier wird versucht, eine Zahl und einen Text mit '+' zusammenzufügen.
# Tipp: Nutze stattdessen einen sauberen f-String: f"Spieler {name} hat {punkte} Punkte!"
# ==============================================================================
def formatierte_ausgabe(name, punkte):
    text = "Spieler " + name + " hat " + punkte + " Punkte!"
    return text


# ==============================================================================
# BUG 5: Logik-Fehler (Vergleichsoperator)
# Diese Funktion soll True zurückgeben, wenn ein Spieler 50 ODER MEHR Punkte hat.
# Aktuell gibt sie bei genau 50 Punkten leider False zurück!
# ==============================================================================
def ist_sieger(punkte):
    if punkte > 50:
        return True
    else:
        return False


# ==============================================================================
# Hauptprogramm zum Ausprobieren:
# (Führe dieses Skript aus mit: python3 aufgabe.py)
# ==============================================================================
if __name__ == "__main__":
    print("🕵️‍♀️ --- CODE-DETEKTIVIN QUIZ TEST --- 🕵️‍♀️")
    
    # Test 1
    endstand = berechne_endstand(20, 15)
    print(f"Endstand (sollte 40 sein): {endstand}")

    # Test 2
    multipliziert = punkte_multiplizieren(10, 3)
    print(f"Multipliziert (sollte 30 sein): {multipliziert}")

    # Test 3
    ausgabe = formatierte_ausgabe("Mia", 50)
    print(f"Formatierte Ausgabe: {ausgabe}")

    # Test 4
    sieger = ist_sieger(50)
    print(f"Ist 50 Punkte ein Sieg? (sollte True sein): {sieger}")

    print("\n🎉 Herzlichen Glückwunsch! Alle 5 Bugs wurden erfolgreich behoben!")
