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
    # Anleitung:
    # 1. Definiere: def __init__(self, inhaber, kontostand=0.0):
    # 2. Speichere die übergebenen Werte an self:
    #    self.inhaber = inhaber
    #    self.kontostand = kontostand
    # ==========================================================================
    def __init__(self, inhaber, kontostand=0.0):
        # Schreibe hier deinen Code für TODO 1:
        pass

    # ==========================================================================
    # TODO 2: Schreibe die Methode "einzahlen(self, betrag)".
    #
    # Regeln:
    # 1. Wenn 'betrag' größer als 0 ist:
    #    - Erhöhe 'self.kontostand' um 'betrag': self.kontostand += betrag
    #    - Gib True zurück (Einzahlung erfolgreich).
    # 2. Wenn 'betrag' kleiner oder gleich 0 ist (z.B. 0 oder -5):
    #    - Ändere nichts am Kontostand.
    #    - Gib False zurück.
    # ==========================================================================
    def einzahlen(self, betrag):
        # Schreibe hier deinen Code für TODO 2:
        pass

    # ==========================================================================
    # TODO 3: Schreibe die Methode "auszahlen(self, betrag)".
    #
    # Regeln:
    # 1. Prüfe mit 'if', ob 'betrag > 0' UND 'self.kontostand >= betrag':
    #    - Wenn ja: Ziehe den Betrag ab (self.kontostand -= betrag)
    #    - Gib True zurück.
    # 2. Wenn nicht (nicht genug Geld da oder ungültiger Betrag):
    #    - Gib False zurück.
    # ==========================================================================
    def auszahlen(self, betrag):
        # Schreibe hier deinen Code für TODO 3:
        pass

    # ==========================================================================
    # TODO 4: Schreibe die Methode "info_text(self)".
    #
    # Sie soll einen formatierten String zurückgeben:
    # "Konto von {inhaber}: {kontostand:.2f} Euro"
    #
    # Beispiel: Bei inhaber="Mia" und kontostand=25.5 -> "Konto von Mia: 25.50 Euro"
    # Tipp: f"Konto von {self.inhaber}: {self.kontostand:.2f} Euro"
    # ==========================================================================
    def info_text(self):
        # Schreibe hier deinen Code für TODO 4:
        pass


# ==============================================================================
# Hauptprogramm zum Ausprobieren:
# (Direkt ausführen mit 'python3 aufgabe.py')
# ==============================================================================
if __name__ == "__main__":
    print("--- Teste dein Bankkonto ---")
    konto = Bankkonto("Mia", 20.0)
    
    if hasattr(konto, "inhaber") and konto.inhaber:
        print(konto.info_text())

        erfolg = konto.einzahlen(15.5)
        print(f"15.50€ eingezahlt? {erfolg} -> Neuer Stand: {konto.kontostand:.2f}€")

        erfolg = konto.auszahlen(50.0)
        print(f"50.00€ ausgezahlt? {erfolg} (sollte False sein) -> Stand: {konto.kontostand:.2f}€")

        erfolg = konto.auszahlen(10.0)
        print(f"10.00€ ausgezahlt? {erfolg} -> Stand: {konto.kontostand:.2f}€")
    else:
        print("💡 Hinweis: Implementiere erst die TODOs, um die Ausgabe zu sehen!")
