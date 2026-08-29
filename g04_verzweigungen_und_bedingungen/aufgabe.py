"""
Kapitel G04: Verzweigungen & Bedingungen (Schulabgleich 08.0)
============================================================

In diesem Kapitel lernst du:
1. Wie du Entscheidungen mit if, elif und else programmierst.
2. Vergleichsoperatoren: ==, !=, <, >, <=, >=.
3. Logische Operatoren: and, or, not.
4. Flache elif-Ketten vs. tief verschachtelte Bedingungen.
5. Wie du komplexe Geschäftslogik und Grenzwerte sauber implementierst.

Bearbeite die Aufgaben TODO 1 bis TODO 4.
Führe danach die Tests aus mit:
    python3 test_aufgabe.py
"""

# ==============================================================================
# TODO 1: Kinokarten-Preisrechner
#
# Schreibe eine Funktion 'ticket_preis(alter: int, ist_student: bool) -> float'.
# Sie berechnet den Ticketpreis nach folgenden Tarif-Regeln:
# - Kinder unter 12 Jahren (alter < 12): 6.00 € (Kindertarif)
# - Senioren ab 65 Jahren (alter >= 65): 8.50 € (Seniorentarif)
# - Alle anderen Personen (12 bis 64 Jahre):
#     - Wenn ist_student True ist: 9.50 € (Studenten-/Ermäßigungstarif)
#     - Wenn ist_student False ist: 12.00 € (Regulärer Erwachsenentarif)
#
# Beispiele:
# ticket_preis(8, False)  -> 6.0
# ticket_preis(70, False) -> 8.5
# ticket_preis(22, True)  -> 9.5
# ticket_preis(30, False) -> 12.0
# ==============================================================================

def ticket_preis(alter: int, ist_student: bool) -> float:
    # Schreibe hier deinen Code für TODO 1:
    pass


# ==============================================================================
# TODO 2: Schulnoten-Ermittlung
#
# Schreibe eine Funktion 'schulnote_text(punkte: int) -> str'.
# Sie ordnet einer erreichten Punktezahl (0 bis 100) die passende Textnote zu:
# - 90 bis 100 Punkte (punkte >= 90): "Sehr gut"
# - 75 bis 89 Punkte  (punkte >= 75): "Gut"
# - 60 bis 74 Punkte  (punkte >= 60): "Befriedigend"
# - 50 bis 59 Punkte  (punkte >= 50): "Genügend"
# - 0 bis 49 Punkte   (punkte < 50):  "Nicht genügend"
# - Werte unter 0 oder über 100:     "Ungültige Punktezahl"
#
# Beispiele:
# schulnote_text(95)  -> "Sehr gut"
# schulnote_text(75)  -> "Gut"
# schulnote_text(49)  -> "Nicht genügend"
# schulnote_text(110) -> "Ungültige Punktezahl"
# schulnote_text(-5)  -> "Ungültige Punktezahl"
# ==============================================================================

def schulnote_text(punkte: int) -> str:
    # Schreibe hier deinen Code für TODO 2:
    pass


# ==============================================================================
# TODO 3: Schaltjahr-Erkennung
#
# Schreibe eine Funktion 'ist_schaltjahr(jahr: int) -> bool'.
# Die Funktion soll prüfen, ob ein übergebenes Kalenderjahr ein Schaltjahr ist.
#
# Die Gregorianische Schaltjahr-Regel lautet:
# 1. Ein Jahr ist ein Schaltjahr, wenn es durch 4 teilbar ist (jahr % 4 == 0).
# 2. AUSNAHME: Ist es durch 100 teilbar (jahr % 100 == 0), ist es KEIN Schaltjahr...
# 3. AUSNAHME DER AUSNAHME: ...es sei denn, es ist auch durch 400 teilbar (jahr % 400 == 0)!
#
# Beispiele:
# ist_schaltjahr(2024) -> True  (durch 4 teilbar, nicht durch 100)
# ist_schaltjahr(2023) -> False (nicht durch 4 teilbar)
# ist_schaltjahr(1900) -> False (durch 100 teilbar, aber nicht durch 400)
# ist_schaltjahr(2000) -> True  (durch 400 teilbar)
# ==============================================================================

def ist_schaltjahr(jahr: int) -> bool:
    # Schreibe hier deinen Code für TODO 3:
    pass


# ==============================================================================
# TODO 4: Achterbahn-Zulassung
#
# Schreibe eine Funktion 'kann_achterbahn_fahren(groesse_cm: int, begleitung_erwachsen: bool) -> bool'.
# Ein Freizeitpark hat folgende Sicherheitsbestimmungen:
# - Ab 140 cm Körpergröße darf jede Person alleine mitfahren (True).
# - Zwischen 120 cm und 139 cm darf eine Person NUR mitfahren, wenn
#   eine erwachsene Begleitperson dabei ist (begleitung_erwachsen == True).
# - Unter 120 cm Körpergröße darf niemand mitfahren (immer False).
#
# Beispiele:
# kann_achterbahn_fahren(145, False) -> True  (Groß genug für Alleinfahrt)
# kann_achterbahn_fahren(130, True)  -> True  (Mit Begleitung erlaubt)
# kann_achterbahn_fahren(130, False) -> False (Ohne Begleitung verboten)
# kann_achterbahn_fahren(115, True)  -> False (Zu klein, auch mit Begleitung)
# ==============================================================================

def kann_achterbahn_fahren(groesse_cm: int, begleitung_erwachsen: bool) -> bool:
    # Schreibe hier deinen Code für TODO 4:
    pass


# ==============================================================================
# Interaktives Hauptprogramm zum Ausprobieren:
# (Führe dieses Skript aus mit: python3 aufgabe.py)
# ==============================================================================
if __name__ == "__main__":
    print("=" * 60)
    print("🎢 BEDINGUNGEN & VERZWEIGUNGEN DEMO")
    print("=" * 60)

    # 1. Kino-Test
    print("\n🎟️ --- Kino-Preisrechner ---")
    try:
        alter_eingabe = int(input("Alter des Besuchers: "))
        student_eingabe = input("Student/Schüler? (j/n): ").strip().lower() == "j"
        preis = ticket_preis(alter_eingabe, student_eingabe)
        if preis is not None:
            print(f"Ticketpreis: {preis:.2f} €")
        else:
            print("Implementiere TODO 1 für die Preisberechnung!")
    except ValueError:
        print("Ungültige Alterseingabe!")

    # 2. Noten-Test
    print("\n📝 --- Notenspiegel-Rechner ---")
    try:
        punkte_eingabe = int(input("Erreichte Punkte (0-100): "))
        note = schulnote_text(punkte_eingabe)
        if note is not None:
            print(f"Ergebnis: {note}")
        else:
            print("Implementiere TODO 2 für die Notenberechnung!")
    except ValueError:
        print("Ungültige Punktezahl!")

    # 3. Schaltjahr-Test
    print("\n📅 --- Schaltjahr-Prüfer ---")
    try:
        jahr_eingabe = int(input("Jahr eingeben (z.B. 2024): "))
        schalt = ist_schaltjahr(jahr_eingabe)
        if schalt is not None:
            print(f"Ist {jahr_eingabe} ein Schaltjahr? -> {'Ja! 🎉' if schalt else 'Nein.'}")
        else:
            print("Implementiere TODO 3 für die Schaltjahrprüfung!")
    except ValueError:
        print("Ungültiges Jahr!")

    # 4. Achterbahn-Test
    print("\n🎢 --- Achterbahn-Einlasskontrolle ---")
    try:
        groesse = int(input("Körpergröße in cm (z.B. 135): "))
        begl = input("Erwachsene Begleitung dabei? (j/n): ").strip().lower() == "j"
        darf_fahren = kann_achterbahn_fahren(groesse, begl)
        if darf_fahren is not None:
            print(f"Darf Achterbahn fahren? -> {'Ja, viel Spaß! 🎢' if darf_fahren else 'Leider nein 🛑'}")
        else:
            print("Implementiere TODO 4 für die Achterbahn-Zulassung!")
    except ValueError:
        print("Ungültige Größenangabe!")
