"""
Kapitel G04: Verzweigungen & Bedingungen (Schulabgleich 08.0)
============================================================
Musterlösung mit sauberen if/elif/else-Verzweigungen und logischen Operatoren.
"""

# ==============================================================================
# TODO 1: Kinokarten-Preisrechner
# ==============================================================================
def ticket_preis(alter: int, ist_student: bool) -> float:
    """Berechnet den Kinokartenpreis basierend auf Alter und Schüler/Studenten-Status."""
    if alter < 12:
        return 6.0
    elif alter >= 65:
        return 8.5
    elif ist_student:
        return 9.5
    else:
        return 12.0


# ==============================================================================
# TODO 2: Schulnoten-Ermittlung
# ==============================================================================
def schulnote_text(punkte: int) -> str:
    """Gibt die passende Textnote für eine Punktezahl zwischen 0 und 100 zurück."""
    if punkte < 0 or punkte > 100:
        return "Ungültige Punktezahl"
    elif punkte >= 90:
        return "Sehr gut"
    elif punkte >= 75:
        return "Gut"
    elif punkte >= 60:
        return "Befriedigend"
    elif punkte >= 50:
        return "Genügend"
    else:
        return "Nicht genügend"


# ==============================================================================
# TODO 3: Schaltjahr-Erkennung
# ==============================================================================
def ist_schaltjahr(jahr: int) -> bool:
    """
    Ermittelt nach den Gregorianischen Kalenderregeln, ob ein Jahr ein Schaltjahr ist.
    Teilbar durch 4, aber nicht durch 100 (außer wenn durch 400 teilbar).
    """
    if (jahr % 4 == 0 and jahr % 100 != 0) or (jahr % 400 == 0):
        return True
    return False


# ==============================================================================
# TODO 4: Achterbahn-Zulassung
# ==============================================================================
def kann_achterbahn_fahren(groesse_cm: int, begleitung_erwachsen: bool) -> bool:
    """Prüft, ob eine Person (mit oder ohne Begleitung) groß genug für die Fahrt ist."""
    if groesse_cm >= 140:
        return True
    elif groesse_cm >= 120 and begleitung_erwachsen:
        return True
    else:
        return False


# ==============================================================================
# Interaktives Hauptprogramm
# ==============================================================================
if __name__ == "__main__":
    print("=" * 60)
    print("🎢 BEDINGUNGEN & VERZWEIGUNGEN (MUSTERLÖSUNG)")
    print("=" * 60)

    print("Kino:", ticket_preis(8, False), "€ (Kind)")
    print("Kino:", ticket_preis(20, True), "€ (Student)")
    print("Kino:", ticket_preis(30, False), "€ (Erwachsen)")
    print("Kino:", ticket_preis(70, False), "€ (Senior)")

    print("\nNoten:")
    print("95 Punkte:", schulnote_text(95))
    print("75 Punkte:", schulnote_text(75))
    print("50 Punkte:", schulnote_text(50))
    print("30 Punkte:", schulnote_text(30))
    print("110 Punkte:", schulnote_text(110))

    print("\nSchaltjahre:")
    print("2024:", ist_schaltjahr(2024))
    print("2023:", ist_schaltjahr(2023))
    print("1900:", ist_schaltjahr(1900))
    print("2000:", ist_schaltjahr(2000))

    print("\nAchterbahn:")
    print("145cm alleine:", kann_achterbahn_fahren(145, False))
    print("130cm mit Begleitung:", kann_achterbahn_fahren(130, True))
    print("130cm alleine:", kann_achterbahn_fahren(130, False))
    print("110cm mit Begleitung:", kann_achterbahn_fahren(110, True))
