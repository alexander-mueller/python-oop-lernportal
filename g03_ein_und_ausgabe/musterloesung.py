"""
Kapitel G03: Interaktive Ein- & Ausgabe (Schulabgleich 07.0)
============================================================
Musterlösung mit sauberen f-Strings, Typkonvertierungen und Formatangaben.
"""

# ==============================================================================
# TODO 1: Begrüßungstext mit f-String
# ==============================================================================
def begruessungs_text(name: str, stadt: str) -> str:
    """Gibt einen freundlichen Begrüßungstext mit f-String zurück."""
    return f"Hallo {name}, herzlich willkommen in {stadt}!"


# ==============================================================================
# TODO 2: Alter in Tagen berechnen
# ==============================================================================
def berechne_alter_in_tagen(jahre: int) -> int:
    """Berechnet das ungefähre Alter in Tagen (365 Tage pro Jahr)."""
    return jahre * 365


# ==============================================================================
# TODO 3: Rechnungsposten formatieren
# ==============================================================================
def formatiere_rechnungsposten(artikel: str, anzahl: int, einzelpreis: float) -> str:
    """Formatiert einen Rechnungsposten mit 2 Nachkommastellen für Preise."""
    gesamtpreis = anzahl * einzelpreis
    return f"{anzahl}x {artikel} à {einzelpreis:.2f} € = {gesamtpreis:.2f} €"


# ==============================================================================
# TODO 4: Steckbrief mit BMI-Berechnung
# ==============================================================================
def steckbrief(name: str, groesse_m: float, gewicht_kg: float) -> str:
    """Berechnet den BMI und gibt einen formatierten Steckbrief zurück."""
    bmi = gewicht_kg / (groesse_m ** 2)
    return f"Steckbrief: {name} | Größe: {groesse_m:.2f} m | Gewicht: {gewicht_kg:.1f} kg | BMI: {bmi:.1f}"


# ==============================================================================
# Interaktives Hauptprogramm
# ==============================================================================
if __name__ == "__main__":
    print("=" * 60)
    print("💬 INTERAKTIVE EIN- & AUSGABE (MUSTERLÖSUNG)")
    print("=" * 60)

    # 1. Demonstration von print() Parametern:
    print("Python", "ist", "klasse!", sep=" - ")
    print("Lade Daten", end="... ")
    print("Fertig!\n")

    # 2. Demonstration der Funktionen:
    print(begruessungs_text("Anna", "Wien"))
    print(f"18 Jahre entsprechen ca. {berechne_alter_in_tagen(18)} Tagen.")
    print(formatiere_rechnungsposten("Kaffee", 3, 2.5))
    print(steckbrief("Alex", 1.80, 75.0))
