"""
Kapitel G03: Interaktive Ein- & Ausgabe (Schulabgleich 07.0)
============================================================

In diesem Kapitel lernst du:
1. Wie du Benutzereingaben über die Tastatur mit input() entgegennimmst.
2. Wie du Datentypen umwandelst (int(input(...)), float(input(...))).
3. Wie du moderne f-Strings für formatierte Textausgaben einsetzt.
4. Wie du Zahlenwerte formatiert darstellst ({preis:.2f} €, {prozent:.1%}, {zahl:04d}).
5. Wie du print() mit den Parametern sep= und end= steuerst.

Bearbeite die Aufgaben TODO 1 bis TODO 4.
Führe danach die Tests aus mit:
    python3 test_aufgabe.py
"""

# ==============================================================================
# 🎯 TEILZIEL 1 (TODO 1): Begrüßungstext mit f-String
#
# Schreibe eine Funktion 'begruessungs_text(name: str, stadt: str) -> str'.
# Sie soll folgenden Text zurückgeben:
# "Hallo {name}, herzlich willkommen in {stadt}!"
#
# Beispiel:
# begruessungs_text("Anna", "Wien") -> "Hallo Anna, herzlich willkommen in Wien!"
# ==============================================================================

def begruessungs_text(name: str, stadt: str) -> str:
    # 🎯 TEILZIEL 1: Implementiere die Logik Schritt für Schritt:
    # 💡 Tipp: Beachte Datentypen und das abschließende return!
    pass


# ==============================================================================
# 🎯 TEILZIEL 2 (TODO 2): Alter in Tagen berechnen
#
# Schreibe eine Funktion 'berechne_alter_in_tagen(jahre: int) -> int'.
# Sie erhält das Alter in ganzen Jahren (z.B. 18) und soll das Alter in Tagen
# berechnen (wir rechnen vereinfacht mit genau 365 Tagen pro Jahr).
#
# Beispiel:
# berechne_alter_in_tagen(18) -> 6570
# berechne_alter_in_tagen(1)  -> 365
# ==============================================================================

def berechne_alter_in_tagen(jahre: int) -> int:
    # 🎯 TEILZIEL 2: Implementiere die Logik Schritt für Schritt:
    # 💡 Tipp: Beachte Datentypen und das abschließende return!
    pass


# ==============================================================================
# 🎯 TEILZIEL 3 (TODO 3): Rechnungsposten formatieren
#
# Schreibe eine Funktion 'formatiere_rechnungsposten(artikel: str, anzahl: int, einzelpreis: float) -> str'.
# Sie berechnet den Gesamtpreis (anzahl * einzelpreis) und gibt einen formatierten
# Rechnungs-String zurück.
#
# Format:
# "{anzahl}x {artikel} à {einzelpreis:.2f} € = {gesamtpreis:.2f} €"
#
# WICHTIG: Die Preise müssen immer auf genau 2 Nachkommastellen formatiert sein!
#
# Beispiele:
# formatiere_rechnungsposten("Kaffee", 3, 2.5)   -> "3x Kaffee à 2.50 € = 7.50 €"
# formatiere_rechnungsposten("Buch", 1, 19.99)   -> "1x Buch à 19.99 € = 19.99 €"
# formatiere_rechnungsposten("Semmel", 5, 0.40)  -> "5x Semmel à 0.40 € = 2.00 €"
# ==============================================================================

def formatiere_rechnungsposten(artikel: str, anzahl: int, einzelpreis: float) -> str:
    # 🎯 TEILZIEL 3: Implementiere die Logik Schritt für Schritt:
    # 💡 Tipp: Beachte Datentypen und das abschließende return!
    pass


# ==============================================================================
# 🎯 TEILZIEL 4 (TODO 4): Steckbrief mit BMI-Berechnung
#
# Schreibe eine Funktion 'steckbrief(name: str, groesse_m: float, gewicht_kg: float) -> str'.
# 1. Berechne den BMI (Body-Mass-Index) nach der Formel:
#    bmi = gewicht_kg / (groesse_m ** 2)
# 2. Gib folgenden formatierten Steckbrief-String zurück:
#    "Steckbrief: {name} | Größe: {groesse_m:.2f} m | Gewicht: {gewicht_kg:.1f} kg | BMI: {bmi:.1f}"
#
# WICHTIG:
# - Größe auf 2 Nachkommastellen formatiert ({groesse_m:.2f} m)
# - Gewicht auf 1 Nachkommastelle formatiert ({gewicht_kg:.1f} kg)
# - BMI auf 1 Nachkommastelle formatiert ({bmi:.1f})
#
# Beispiel:
# steckbrief("Alex", 1.80, 75.0) -> "Steckbrief: Alex | Größe: 1.80 m | Gewicht: 75.0 kg | BMI: 23.1"
# steckbrief("Mia", 1.65, 58.5)  -> "Steckbrief: Mia | Größe: 1.65 m | Gewicht: 58.5 kg | BMI: 21.5"
# ==============================================================================

def steckbrief(name: str, groesse_m: float, gewicht_kg: float) -> str:
    # 🎯 TEILZIEL 4: Implementiere die Logik Schritt für Schritt:
    # 💡 Tipp: Beachte Datentypen und das abschließende return!
    pass


# ==============================================================================
# Interaktives Hauptprogramm zum Ausprobieren:
# (Führe dieses Skript aus mit: python3 aufgabe.py)
# ==============================================================================
if __name__ == "__main__":
    print("=" * 60)
    print("💬 INTERAKTIVE EIN- & AUSGABE DEMO")
    print("=" * 60)

    # 1. Demonstration von print() mit sep und end
    print("Python", "ist", "klasse!", sep=" - ")
    print("Lade Daten", end="... ")
    print("Fertig!\n")

    # 2. Interaktiver Dialog mit Tastatureingabe
    try:
        benutzer_name = input("Wie heißt du? ")
        benutzer_stadt = input("Aus welcher Stadt kommst du? ")
        begruessung = begruessungs_text(benutzer_name, benutzer_stadt)
        if begruessung:
            print(begruessung)
        else:
            print(f"Hallo {benutzer_name} aus {benutzer_stadt} (Implementiere TODO 1)!")

        alter_str = input("\nWie alt bist du (in Jahren)? ")
        # Achtung: input() liefert immer einen String -> Umwandlung mit int() nötig!
        alter_int = int(alter_str)
        tage = berechne_alter_in_tagen(alter_int)
        if tage is not None:
            print(f"Wahnsinn, du lebst schon seit ca. {tage} Tagen!")
        else:
            print("Implementiere TODO 2 für die Tage-Berechnung!")

        print("\n--- Kassenbon-Generator ---")
        art = input("Welcher Artikel? ")
        anz = int(input("Wie viele Stück? "))
        preis = float(input("Einzelpreis in € (z.B. 2.99): "))
        posten = formatiere_rechnungsposten(art, anz, preis)
        if posten:
            print(posten)
        else:
            print("Implementiere TODO 3 für den formatierten Rechnungsposten!")

        print("\n--- Steckbrief & BMI-Rechner ---")
        gr = float(input("Deine Körpergröße in Metern (z.B. 1.75): "))
        gw = float(input("Dein Körpergewicht in kg (z.B. 68.0): "))
        sb = steckbrief(benutzer_name, gr, gw)
        if sb:
            print(sb)
        else:
            print("Implementiere TODO 4 für den Steckbrief!")

    except (ValueError, TypeError) as fehler:
        print(f"\n💡 Hinweis / Fehleingabe: {fehler}")
        print("Achte darauf, bei Zahlen nur Ziffern und bei Kommazahlen einen Punkt '.' einzugeben!")
