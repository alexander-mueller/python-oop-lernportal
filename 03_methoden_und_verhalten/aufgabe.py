"""
Kapitel 03: Methoden & Verhalten – Helden-Duell
==============================================

In dieser Aufgabe programmierst du eine Klasse 'Held' für ein Rollenspiel.
"""

class Held:
    # ==========================================================================
    # TODO 1: Konstruktor __init__(self, name, leben=100, angriffskraft=15)
    #
    # Speichere die folgenden Attribute an self:
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
    #
    # Schritt-für-Schritt:
    # 1. Wenn der Held schon tot ist (not self.ist_am_leben) oder schaden <= 0:
    #    - return 0
    # 2. Berechne den Schaden und ziehe ihn von self.leben ab.
    # 3. Wenn self.leben <= 0 wird:
    #    - setze self.leben = 0
    #    - setze self.ist_am_leben = False
    # 4. Gib den erlittenen Schaden zurück (z.B. return schaden).
    # ==========================================================================
    def schaden_erleiden(self, schaden):
        # Schreibe hier deinen Code für TODO 2:
        pass

    # ==========================================================================
    # TODO 3: Methode "heilen(self, heilung)"
    #
    # Schritt-für-Schritt:
    # 1. Wenn der Held tot ist (not self.ist_am_leben) oder heilung <= 0:
    #    - return 0 (Tote können nicht geheilt werden!)
    # 2. Merke dir das aktuelle Leben: alter_wert = self.leben
    # 3. Erhöhe das Leben, aber maximal bis self.max_leben:
    #    self.leben = min(self.max_leben, self.leben + heilung)
    # 4. Berechne, wie viel tatsächlich geheilt wurde:
    #    tatsaechlich_geheilt = self.leben - alter_wert
    # 5. Gib tatsaechlich_geheilt zurück.
    # ==========================================================================
    def heilen(self, heilung):
        # Schreibe hier deinen Code für TODO 3:
        pass

    # ==========================================================================
    # TODO 4: Methode "angreifen(self, gegner)"
    # Parameter 'gegner' ist ein anderes Held-Objekt!
    #
    # Schritt-für-Schritt:
    # 1. Prüfe, ob BEIDE Helden leben: self.ist_am_leben and gegner.ist_am_leben
    # 2. Wenn ja:
    #    - Rufe auf dem Gegner schaden_erleiden auf:
    #      gegner.schaden_erleiden(self.angriffskraft)
    #    - Gib True zurück (Angriff erfolgreich).
    # 3. Wenn einer von beiden besiegt ist:
    #    - Gib False zurück.
    # ==========================================================================
    def angreifen(self, gegner):
        # Schreibe hier deinen Code für TODO 4:
        pass

    # ==========================================================================
    # TODO 5: Methode "status_text(self)"
    #
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
# (Ausführen mit 'python3 aufgabe.py')
# ==============================================================================
if __name__ == "__main__":
    print("⚔️ --- ARENA DER HELDEN --- ⚔️")
    ritter = Held("Arthur", leben=80, angriffskraft=20)
    drache = Held("Feuerspei", leben=120, angriffskraft=25)

    if hasattr(ritter, "name") and ritter.name:
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
    else:
        print("💡 Hinweis: Implementiere erst die TODOs, um die Arena zu starten!")
