"""
Kapitel 03: Methoden & Verhalten – Helden-Duell
==============================================

In dieser Aufgabe programmierst du eine Klasse 'Held' für ein Rollenspiel.
"""

class Held:
    # ==========================================================================
    # TODO 1: Konstruktor __init__(self, name, leben=100, angriffskraft=15)
    # Speichere:
    # - self.name = name
    # - self.leben = leben
    # - self.max_leben = leben (das maximale Leben entspricht dem Startleben)
    # - self.angriffskraft = angriffskraft
    # - self.ist_am_leben = True
    # ==========================================================================
    def __init__(self, name, leben=100, angriffskraft=15):
        # Schreibe hier deinen Code für TODO 1:
        pass

    # ==========================================================================
    # TODO 2: Methode "schaden_erleiden(self, schaden)"
    # Regeln:
    # 1. Wenn der Held bereits besiegt ist (not self.ist_am_leben) oder schaden <= 0:
    #    - Es passiert nichts, gib 0 zurück.
    # 2. Ziehe 'schaden' von 'self.leben' ab.
    # 3. Wenn 'self.leben' <= 0 wird:
    #    - Setze 'self.leben' genau auf 0.
    #    - Setze 'self.ist_am_leben' auf False.
    # 4. Gib den erlittenen Schaden (int/float) zurück.
    # ==========================================================================
    def schaden_erleiden(self, schaden):
        # Schreibe hier deinen Code für TODO 2:
        pass

    # ==========================================================================
    # TODO 3: Methode "heilen(self, heilung)"
    # Regeln:
    # 1. Wenn der Held besiegt ist (not self.ist_am_leben) oder heilung <= 0:
    #    - Tote Helden können nicht geheilt werden! Gib 0 zurück.
    # 2. Erhöhe das Leben um 'heilung', aber ACHTUNG:
    #    - 'self.leben' darf niemals größer als 'self.max_leben' werden!
    #    - Beispiel: Wenn leben=90, max_leben=100 und heilung=20:
    #      Das Leben wird 100 (nicht 110) und die tatsächliche Heilung war 10.
    # 3. Gib die tatsächlich geheilte Menge an Lebenspunkten zurück.
    # ==========================================================================
    def heilen(self, heilung):
        # Schreibe hier deinen Code für TODO 3:
        pass

    # ==========================================================================
    # TODO 4: Methode "angreifen(self, gegner)"
    # Parameter 'gegner' ist ein anderes Held-Objekt!
    # Regeln:
    # 1. Prüfe, ob BEIDE Helden noch am Leben sind (self.ist_am_leben und gegner.ist_am_leben).
    # 2. Wenn ja:
    #    - Rufe auf dem 'gegner' die Methode 'schaden_erleiden' auf mit self.angriffskraft als Wert.
    #    - Gib True zurück.
    # 3. Wenn einer von beiden (oder beide) nicht mehr am Leben ist:
    #    - Greife nicht an und gib False zurück.
    # ==========================================================================
    def angreifen(self, gegner):
        # Schreibe hier deinen Code für TODO 4:
        pass

    # ==========================================================================
    # TODO 5: Methode "status_text(self)"
    # Gibt einen formatierten String zurück:
    # Wenn am Leben:
    #   "[{self.name}] HP: {self.leben}/{self.max_leben} | Kraft: {self.angriffskraft} | Status: Lebendig"
    # Wenn besiegt:
    #   "[{self.name}] HP: 0/{self.max_leben} | Kraft: {self.angriffskraft} | Status: Besiegt"
    # ==========================================================================
    def status_text(self):
        # Schreibe hier deinen Code für TODO 5:
        pass


# ==============================================================================
# Kampfsimulator zum Ausprobieren:
# ==============================================================================
if __name__ == "__main__":
    print("⚔️ --- ARENA DER HELDEN --- ⚔️")
    ritter = Held("Arthur", leben=80, angriffskraft=20)
    drache = Held("Feuerspei", leben=120, angriffskraft=25)

    print(ritter.status_text())
    print(drache.status_text())

    print("\n--- Runde 1 ---")
    ritter.angreifen(drache)
    print(drache.status_text())

    drache.angreifen(ritter)
    print(ritter.status_text())

    print("\n--- Arthur trinkt einen Heiltrank ---")
    geheilt = ritter.heilen(15)
    print(f"Arthur heilt sich um {geheilt} HP!")
    print(ritter.status_text())
