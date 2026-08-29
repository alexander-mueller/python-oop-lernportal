"""
Kapitel 02: Der Konstruktor __init__ und self
==============================================

In dieser Aufgabe erstellst du eine Klasse "Bankkonto" für eine Taschengeld-App.
"""

class Bankkonto:
    # ==========================================================================
    # TODO 1: Schreibe die __init__-Methode.
    # Parameter: self, inhaber (String), kontostand (Float, Standardwert 0.0)
    #
    # Speichere die Parameter als Attribute an 'self':
    # - self.inhaber
    # - self.kontostand
    # ==========================================================================
    def __init__(self, inhaber, kontostand=0.0):
        # Schreibe hier deinen Code für TODO 1:
        pass

    # ==========================================================================
    # TODO 2: Schreibe die Methode "einzahlen(self, betrag)".
    # Regeln:
    # 1. Wenn 'betrag' größer als 0 ist:
    #    - Erhöhe 'self.kontostand' um 'betrag'.
    #    - Gib True zurück (Einzahlung erfolgreich).
    # 2. Wenn 'betrag' kleiner oder gleich 0 ist:
    #    - Verändere den Kontostand nicht.
    #    - Gib False zurück (ungültiger Betrag).
    # ==========================================================================
    def einzahlen(self, betrag):
        # Schreibe hier deinen Code für TODO 2:
        pass

    # ==========================================================================
    # TODO 3: Schreibe die Methode "auszahlen(self, betrag)".
    # Regeln:
    # 1. Der Betrag muss größer als 0 sein UND es muss genug Geld auf dem Konto
    #    sein (self.kontostand >= betrag).
    #    - Ziehe 'betrag' von 'self.kontostand' ab.
    #    - Gib True zurück (Auszahlung erfolgreich).
    # 2. Andernfalls (nicht genug Geld oder ungültiger Betrag):
    #    - Verändere den Kontostand nicht.
    #    - Gib False zurück.
    # ==========================================================================
    def auszahlen(self, betrag):
        # Schreibe hier deinen Code für TODO 3:
        pass

    # ==========================================================================
    # TODO 4: Schreibe die Methode "info_text(self)".
    # Sie soll einen String im folgenden Format zurückgeben:
    # "Konto von {inhaber}: {kontostand:.2f} Euro"
    #
    # Beispiel: Bei inhaber="Mia" und kontostand=25.5 -> "Konto von Mia: 25.50 Euro"
    # ==========================================================================
    def info_text(self):
        # Schreibe hier deinen Code für TODO 4:
        pass


# ==============================================================================
# Hauptprogramm zum Ausprobieren:
# ==============================================================================
if __name__ == "__main__":
    print("--- Teste dein Bankkonto ---")
    konto = Bankkonto("Mia", 20.0)
    print(konto.info_text())

    erfolg = konto.einzahlen(15.5)
    print(f"15.50€ eingezahlt? {erfolg} -> Neuer Stand: {konto.kontostand}€")

    erfolg = konto.auszahlen(50.0)
    print(f"50.00€ ausgezahlt? {erfolg} (sollte False sein) -> Stand: {konto.kontostand}€")

    erfolg = konto.auszahlen(10.0)
    print(f"10.00€ ausgezahlt? {erfolg} -> Stand: {konto.kontostand}€")
