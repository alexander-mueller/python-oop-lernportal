"""
Kapitel 02: Der Konstruktor __init__ und self – Musterlösung
=============================================================
"""

class Bankkonto:
    # TODO 1: Konstruktor
    def __init__(self, inhaber, kontostand=0.0):
        self.inhaber = inhaber
        self.kontostand = float(kontostand)

    # TODO 2: Einzahlen mit Betragsüberprüfung
    def einzahlen(self, betrag):
        if betrag > 0:
            self.kontostand += betrag
            return True
        return False

    # TODO 3: Auszahlen mit Guthabenüberprüfung
    def auszahlen(self, betrag):
        if betrag > 0 and self.kontostand >= betrag:
            self.kontostand -= betrag
            return True
        return False

    # TODO 4: Formatierter Info-Text
    def info_text(self):
        return f"Konto von {self.inhaber}: {self.kontostand:.2f} Euro"


if __name__ == "__main__":
    konto = Bankkonto("Mia", 20.0)
    print(konto.info_text())
    konto.einzahlen(15.5)
    print(konto.info_text())
    konto.auszahlen(10.0)
    print(konto.info_text())
