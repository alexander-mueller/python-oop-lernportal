"""
Kapitel 01: Die erste Klasse – Aufgabenblatt
============================================

Bearbeite die Aufgaben Schritt für Schritt von TODO 1 bis TODO 5.
Wenn du fertig bist, überprüfe deine Lösung mit:
    python3 test_aufgabe.py
"""

# ==============================================================================
# TODO 1: Definiere eine leere Klasse namens "Haustier".
# Tipp: Verwende das Schlüsselwort 'class' und vorerst 'pass' im Klassenrumpf.
# ==============================================================================

# Schreibe hier deinen Code für TODO 1:



# ==============================================================================
# TODO 2: Erstelle eine Funktion namens "erstelle_bello()".
# Diese Funktion soll:
# 1. Ein neues Haustier-Objekt erzeugen.
# 2. Dem Objekt folgende Attribute zuweisen:
#    - name: "Bello"
#    - tierart: "Hund"
#    - alter: 3
# 3. Das fertige Objekt zurückgeben (return).
# ==============================================================================

def erstelle_bello():
    # Schreibe hier deinen Code für TODO 2:
    pass


# ==============================================================================
# TODO 3: Erstelle eine Funktion namens "erstelle_mimi()".
# Diese Funktion soll:
# 1. Ein neues Haustier-Objekt erzeugen.
# 2. Dem Objekt folgende Attribute zuweisen:
#    - name: "Mimi"
#    - tierart: "Katze"
#    - alter: 5
# 3. Das fertige Objekt zurückgeben (return).
# ==============================================================================

def erstelle_mimi():
    # Schreibe hier deinen Code für TODO 3:
    pass


# ==============================================================================
# TODO 4: Schreibe eine Funktion "steckbrief_text(haustier)".
# Die Funktion bekommt ein Haustier-Objekt als Parameter übergeben.
# Sie soll einen formatierten Text im folgenden Format zurückgeben:
# "{name} ist ein(e) {tierart} und ist {alter} Jahre alt."
#
# Beispiel:
# Wenn bello übergeben wird, soll zurückgegeben werden:
# "Bello ist ein(e) Hund und ist 3 Jahre alt."
# ==============================================================================

def steckbrief_text(haustier):
    # Schreibe hier deinen Code für TODO 4:
    pass


# ==============================================================================
# TODO 5: Schreibe eine Funktion "aelteres_tier(tier1, tier2)".
# Die Funktion bekommt zwei Haustier-Objekte übergeben.
# Sie soll dasjenige Haustier-Objekt zurückgeben, dessen 'alter' größer ist.
# Wenn beide Tiere gleich alt sind, soll tier1 zurückgegeben werden.
# ==============================================================================

def aelteres_tier(tier1, tier2):
    # Schreibe hier deinen Code für TODO 5:
    pass


# ==============================================================================
# Hauptprogramm zum Ausprobieren:
# (Du kannst diese Datei direkt mit 'python3 aufgabe.py' ausführen)
# ==============================================================================
if __name__ == "__main__":
    print("--- Teste deine Haustiere ---")
    bello = erstelle_bello()
    mimi = erstelle_mimi()

    if bello and mimi:
        print(steckbrief_text(bello))
        print(steckbrief_text(mimi))
        aelter = aelteres_tier(bello, mimi)
        print(f"Das ältere Tier ist: {aelter.name}")
    else:
        print("Hinweis: Implementiere erst die TODOs, um die Ausgabe zu sehen!")
