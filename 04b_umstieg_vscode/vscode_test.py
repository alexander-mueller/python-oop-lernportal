"""
🚀 VS CODE AUSPROBIER-PLAYGROUND 🚀
===================================
Willkommen in VS Code! Diese Datei ist zum Experimentieren da.
Folge den 4 Mini-Experimenten unten:
"""

# ==============================================================================
# EXPERIMENT 1: Better Comments (Farbige Kommentare)
# Wenn du die Erweiterung 'Better Comments' installiert hast, siehst du hier
# verschiedene Farben für verschiedene Kommentar-Typen:
# ==============================================================================

# TODO: Das ist ein normaler orangefarbener Aufgaben-Kommentar
# ! ACHTUNG: Das ist ein wichtiger roter Warn-Kommentar
# ? FRAGE: Das ist ein blauer Frage-Kommentar
# * INFO: Das ist ein hervorgehobener grüner Info-Kommentar


# ==============================================================================
# EXPERIMENT 2: IntelliSense (Automatische Code-Vervollständigung)
# Schau dir diese Klasse an:
# ==============================================================================
class ElektroAuto:
    def __init__(self, modell, batterie_kwh=60):
        self.modell = modell
        self.batterie_kwh = batterie_kwh
        self.ladestand_prozent = 100

    def fahren(self, kilometer):
        verbrauch = kilometer * 0.2
        self.ladestand_prozent -= verbrauch
        return f"{self.modell} ist {kilometer} km gefahren! (Akku: {self.ladestand_prozent:.0f}%)"

    def batterie_aufladen(self):
        self.ladestand_prozent = 100
        return f"{self.modell} ist wieder voll aufgeladen!"


# 👇 PROBIERE ES HIER AUS:
# 1. Entferne das '#' in der nächsten Zeile.
# 2. Tippe 'tesla.' und warte eine Millisekunde:
#    VS Code schlägt dir automatisch '.fahren', '.batterie_aufladen', '.modell' usw. vor!
#    Wähle mit den Pfeiltasten und drücke Tab oder Enter.

tesla = ElektroAuto("Tesla Model 3")
# print(tesla.fahren(50))


# ==============================================================================
# EXPERIMENT 3: Automatisches Formatieren (Format Document)
# Diese Zeilen hier unten sind absichtlich etwas unordentlich eingerückt / mit
# unschönen Abständen:
# Drücke: Alt + Shift + F (Mac: Option + Shift + F) oder speichere mit Strg + S.
# Siehst du, wie VS Code die Abstände automatisch perfekt aufräumt?
# ==============================================================================
liste_der_autos   =  [ "Tesla" , "BMW"   , "Porsche"   , "Audi"  ] 


# ==============================================================================
# EXPERIMENT 4: Ausführen im integrierten Terminal
# 1. Drücke Strg + ` (oder Cmd + ` auf Mac), um das Terminal unten zu öffnen.
# 2. Tippe: python3 04b_umstieg_vscode/vscode_test.py (oder klicke auf das Play-Symbol ▶️ oben rechts).
# ==============================================================================
if __name__ == "__main__":
    print("=" * 55)
    print("🎉 HERZLICHEN GLÜCKWUNSCH! VS CODE FUNKTIONIERT PERFEKT!")
    print("=" * 55)
    print(f"Auto erstellt: {tesla.modell}")
    print(tesla.fahren(80))
    print(f"Bereinigte Liste: {liste_der_autos}")
    print("\n👉 Du bist jetzt bereit für Kapitel 05 (Objekte kombinieren)!")
    print("=" * 55)
