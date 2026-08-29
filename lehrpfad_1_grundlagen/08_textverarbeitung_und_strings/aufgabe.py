"""
Kapitel G08: Textverarbeitung & Strings in Python (Schulabgleich 11.0)
=====================================================================

In dieser Aufgabe lernst du die wichtigsten String-Methoden zur Textbereinigung,
Suche, Formatierung und Analyse kennen.
"""


def ist_palindrom(text: str) -> bool:
    """
    TODO 1: Prüft, ob ein Text ein Palindrom ist (von vorne und hinten
    gelesen exakt gleich lautet).

    Regeln:
    - Groß- und Kleinschreibung wird ignoriert ('A' == 'a').
    - Leerzeichen werden ignoriert (z.B. "Dreh mal am Herd").

    Beispiele:
        ist_palindrom("Anna") -> True
        ist_palindrom("Lagerregal") -> True
        ist_palindrom("Dreh mal am Herd") -> True
        ist_palindrom("Python") -> False

    Tipp:
        1. Wandle den Text mit `.lower()` in Kleinbuchstaben um.
        2. Entferne Leerzeichen mit `.replace(" ", "")`.
        3. Vergleiche den bereinigten Text mit seiner Umkehrung: `bereinigt == bereinigt[::-1]`.
    """
    # 🎯 TEILZIEL 1: Implementiere die Logik Schritt für Schritt:
    # 💡 Tipp: Beachte Datentypen und das abschließende return!
    pass


def zaehle_vokale(text: str) -> int:
    """
    TODO 2: Zählt die Anzahl aller Vokale im übergebenen Text.
    Als Vokale gelten: a, e, i, o, u sowie die Umlaute ä, ö, ü (Groß- und Kleinschreibung!).

    Beispiele:
        zaehle_vokale("Python") -> 1 (nur 'o')
        zaehle_vokale("Käsebrot") -> 3 ('ä', 'e', 'o')
        zaehle_vokale("SCHÖNES Wetter") -> 4 ('Ö', 'E', 'e', 'e')
        zaehle_vokale("HTML") -> 0
        zaehle_vokale("Fly") -> 0

    Tipp:
        Definiere eine Vokal-Menge oder Liste: `vokale = "aeiouäöü"`
        Wandle den Text in Kleinbuchstaben um (`text.lower()`) und zähle,
        wie viele Zeichen in `vokale` vorkommen.
    """
    # 🎯 TEILZIEL 2: Implementiere die Logik Schritt für Schritt:
    # 💡 Tipp: Beachte Datentypen und das abschließende return!
    pass


def bereinige_benutzernamen(name: str) -> str:
    """
    TODO 3: Bereinigt einen eingegebenen Benutzernamen für ein Login-System.

    Regeln:
    1. Führende und nachfolgende Leerzeichen werden entfernt (.strip()).
    2. Alle Buchstaben werden in Kleinbuchstaben umgewandelt (.lower()).
    3. Alle verbleibenden Leerzeichen zwischen Wörtern werden durch Unterstriche '_' ersetzt (.replace()).

    Beispiele:
        bereinige_benutzernamen("  Max Mustermann  ") -> "max_mustermann"
        bereinige_benutzernamen(" Super Coder 99 ") -> "super_coder_99"
        bereinige_benutzernamen("Lukas") -> "lukas"

    Tipp:
        Du kannst String-Methoden verketten: `name.strip().lower().replace(" ", "_")`
    """
    # 🎯 TEILZIEL 3: Implementiere die Logik Schritt für Schritt:
    # 💡 Tipp: Beachte Datentypen und das abschließende return!
    pass


def woerter_zaehlen(text: str) -> int:
    """
    TODO 4: Zählt, wie viele Wörter im übergebenen Text vorkommen.
    - Mehrere Leerzeichen hintereinander zählen nicht als leere Wörter.
    - Ein leerer String "" enthält 0 Wörter.

    Beispiele:
        woerter_zaehlen("Hallo Welt") -> 2
        woerter_zaehlen("   Python   macht   Spaß!   ") -> 3
        woerter_zaehlen("") -> 0

    Tipp:
        Verwende `.split()`. Ohne Parameter teilt es an beliebigen Leerzeichen
        und ignoriert doppelte Leerzeichen automatisch! `len(text.split())`
    """
    # 🎯 TEILZIEL 4: Implementiere die Logik Schritt für Schritt:
    # 💡 Tipp: Beachte Datentypen und das abschließende return!
    pass


def maskiere_kreditkarte(nummer: str) -> str:
    """
    TODO 5: Maskiert eine sensible Kartennummer oder ID, sodass nur die
    letzten 4 Zeichen sichtbar bleiben und alle vorherigen durch '*' ersetzt werden.

    Regeln:
    - Hat die Nummer 4 oder weniger Zeichen, wird sie unverändert zurückgegeben.
    - Hat sie mehr als 4 Zeichen, werden alle bis auf die letzten 4 durch '*' ersetzt.

    Beispiele:
        maskiere_kreditkarte("1234567812345678") -> "************5678"
        maskiere_kreditkarte("987654321")        -> "*****4321"
        maskiere_kreditkarte("1234")             -> "1234"
        maskiere_kreditkarte("99")               -> "99"

    Tipp:
        1. Wenn `len(nummer) <= 4`: `return nummer`
        2. Anzahl der Sterne: `anzahl_sterne = len(nummer) - 4`
        3. Die letzten 4 Zeichen: `letzte_vier = nummer[-4:]`
        4. Gib `("*" * anzahl_sterne) + letzte_vier` zurück.
    """
    # 🎯 TEILZIEL 5: Implementiere die Logik Schritt für Schritt:
    # 💡 Tipp: Beachte Datentypen und das abschließende return!
    pass


# ==============================================================================
# Hauptprogramm zum Ausprobieren:
# (Führe die Datei aus mit: python3 aufgabe.py)
# ==============================================================================
if __name__ == "__main__":
    print("--- Teste deine String-Funktionen ---")

    test_palindrom = "Dreh mal am Herd"
    print(f"Ist '{test_palindrom}' ein Palindrom (TODO 1)?", ist_palindrom(test_palindrom))

    test_vokale = "Käsebrot mit Äpfeln"
    print(f"Vokale in '{test_vokale}' (TODO 2):", zaehle_vokale(test_vokale))

    roher_name = "  Max Mustermann 2026  "
    print(f"Bereinigter Name von '{roher_name}' (TODO 3):", bereinige_benutzernamen(roher_name))

    text = "   Python   macht   wirklich großen   Spaß!   "
    print(f"Wortanzahl (TODO 4):", woerter_zaehlen(text))

    karte = "1234567812345678"
    print(f"Maskierte Karte '{karte}' (TODO 5):", maskiere_kreditkarte(karte))
