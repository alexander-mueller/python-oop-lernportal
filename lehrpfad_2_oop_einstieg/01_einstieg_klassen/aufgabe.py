"""
Kapitel 01: Die erste Klasse – Aufgabenblatt
============================================

Bearbeite die Aufgaben Schritt für Schritt von TODO 1 bis TODO 5.
Wenn du fertig bist, überprüfe deine Lösung im Terminal mit:
    python3 test_aufgabe.py
"""

# ==============================================================================
# TODO 1: Definiere eine leere Klasse namens "Haustier".
# 
# Erklärung:
# Eine Klasse ist ein Bauplan.
# Schreibe 'class Haustier:' und rück in der nächsten Zeile 'pass' ein.
# ==============================================================================

# Schreibe hier deinen Code für TODO 1:



# ==============================================================================
# TODO 2: Erstelle eine Funktion namens "erstelle_bello()".
#
# Schritt-für-Schritt-Anleitung:
# 1. Erstelle ein neues Haustier-Objekt: z.B. hund = Haustier()
# 2. Setze die drei Attribute mit dem Punkt-Operator:
#    hund.name = "Bello"
#    hund.tierart = "Hund"
#    hund.alter = 3
# 3. Gib das erstellte Objekt mit 'return hund' zurück!
# ==============================================================================

def erstelle_bello():
    # Schreibe hier deinen Code für TODO 2:
    pass


# ==============================================================================
# TODO 3: Erstelle eine Funktion namens "erstelle_mimi()".
#
# Ähnlich wie bei Bello:
# - name = "Mimi"
# - tierart = "Katze"
# - alter = 5
# Vergiss nicht das 'return'!
# ==============================================================================

def erstelle_mimi():
    # Schreibe hier deinen Code für TODO 3:
    pass


# ==============================================================================
# TODO 4: Schreibe eine Funktion "steckbrief_text(haustier)".
#
# Die Funktion bekommt ein Haustier-Objekt als Parameter übergeben.
# Sie soll einen formatierten Text im folgenden Format zurückgeben:
# "{name} ist ein(e) {tierart} und ist {alter} Jahre alt."
#
# Tipp: Nutze einen f-String: f"{haustier.name} ist ein(e) {haustier.tierart} ..."
#
# Beispiel:
# Wenn bello übergeben wird: "Bello ist ein(e) Hund und ist 3 Jahre alt."
# ==============================================================================

def steckbrief_text(haustier):
    # Schreibe hier deinen Code für TODO 4:
    pass


# ==============================================================================
# TODO 5: Schreibe eine Funktion "aelteres_tier(tier1, tier2)".
#
# Die Funktion bekommt zwei Haustier-Objekte übergeben.
# Sie soll dasjenige Haustier-Objekt zurückgeben, dessen 'alter' größer ist.
# Wenn beide Tiere gleich alt sind, soll tier1 zurückgegeben werden.
#
# Tipp:
# if tier2.alter > tier1.alter:
#     return tier2
# else:
#     return tier1
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
        print(f"Das ältere Tier ist: {aelter.name} ({aelter.alter} Jahre)")
    else:
        print("💡 Hinweis: Implementiere erst die TODOs, um die Ausgabe zu sehen!")
