"""
Kapitel 03: Methoden & Verhalten – Helden-Duell – Musterlösung
=============================================================
"""

class Held:
    def __init__(self, name, leben=100, angriffskraft=15):
        self.name = name
        self.leben = leben
        self.max_leben = leben
        self.angriffskraft = angriffskraft
        self.ist_am_leben = True

    def schaden_erleiden(self, schaden):
        if not self.ist_am_leben or schaden <= 0:
            return 0
        
        tatsaechlicher_schaden = min(schaden, self.leben)
        self.leben -= schaden
        if self.leben <= 0:
            self.leben = 0
            self.ist_am_leben = False
        return tatsaechlicher_schaden

    def heilen(self, heilung):
        if not self.ist_am_leben or heilung <= 0:
            return 0
        
        alter_wert = self.leben
        self.leben = min(self.max_leben, self.leben + heilung)
        tatsaechlich_geheilt = self.leben - alter_wert
        return tatsaechlich_geheilt

    def angreifen(self, gegner):
        if self.ist_am_leben and gegner.ist_am_leben:
            gegner.schaden_erleiden(self.angriffskraft)
            return True
        return False

    def status_text(self):
        status_str = "Lebendig" if self.ist_am_leben else "Besiegt"
        return f"[{self.name}] HP: {self.leben}/{self.max_leben} | Kraft: {self.angriffskraft} | Status: {status_str}"


if __name__ == "__main__":
    ritter = Held("Arthur", 80, 20)
    drache = Held("Feuerspei", 120, 25)
    print(ritter.status_text())
    print(drache.status_text())
    ritter.angreifen(drache)
    print(drache.status_text())
