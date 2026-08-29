"""
Kapitel G08: Textverarbeitung & Strings – Musterlösung
======================================================
"""


def ist_palindrom(text: str) -> bool:
    """Prüft, ob text ein Palindrom ist (ignoriert Groß/Klein und Leerzeichen)."""
    bereinigt = text.lower().replace(" ", "")
    return bereinigt == bereinigt[::-1]


def zaehle_vokale(text: str) -> int:
    """Zählt Vokale inklusive deutscher Umlaute."""
    vokale = set("aeiouäöü")
    return sum(1 for c in text.lower() if c in vokale)


def bereinige_benutzernamen(name: str) -> str:
    """Strippt, wandelt in Kleinbuchstaben um und ersetzt Leerzeichen durch Unterstriche."""
    return name.strip().lower().replace(" ", "_")


def woerter_zaehlen(text: str) -> int:
    """Zählt Wörter anhand von Whitespace-Trennung."""
    return len(text.split())


def maskiere_kreditkarte(nummer: str) -> str:
    """Maskiert alle Zeichen bis auf die letzten 4 mit Sternchen."""
    if len(nummer) <= 4:
        return nummer
    return "*" * (len(nummer) - 4) + nummer[-4:]


if __name__ == "__main__":
    print("Palindrom 'Anna':", ist_palindrom("Anna"))
    print("Palindrom 'Dreh mal am Herd':", ist_palindrom("Dreh mal am Herd"))
    print("Vokale 'Käsebrot':", zaehle_vokale("Käsebrot"))
    print("Benutzername '  Max Mustermann  ':", bereinige_benutzernamen("  Max Mustermann  "))
    print("Wörter 'Python macht Spaß':", woerter_zaehlen("Python macht Spaß"))
    print("Maskiert '1234567812345678':", maskiere_kreditkarte("1234567812345678"))
