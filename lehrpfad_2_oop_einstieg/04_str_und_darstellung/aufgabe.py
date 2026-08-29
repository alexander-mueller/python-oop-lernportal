"""
Kapitel 04: __str__ und Objektlisten – Supermarkt & Warenkorb
============================================================

In dieser Aufgabe erstellst du zwei Klassen: 'Artikel' und 'Warenkorb'.
"""

class Artikel:
    # ==========================================================================
    # 🎯 TEILZIEL 1 (TODO 1): Konstruktor für Artikel
    # Parameter: self, name (str), preis (float), anzahl (int, Standardwert 1)
    # Speichere: self.name, self.preis, self.anzahl
    # ==========================================================================
    def __init__(self, name, preis, anzahl=1):
        # 🎯 TEILZIEL 1: Implementiere die Logik Schritt für Schritt:
    # 💡 Tipp: Beachte Datentypen und das abschließende return!
        pass

    # ==========================================================================
    # 🎯 TEILZIEL 2 (TODO 2): Methode "gesamtpreis(self)"
    # Gibt den Preis für diesen Artikel multipliziert mit der Anzahl zurück.
    # Beispiel: 3 Äpfel à 0.50€ -> 1.50
    # Tipp: return self.preis * self.anzahl
    # ==========================================================================
    def gesamtpreis(self):
        # 🎯 TEILZIEL 2: Implementiere die Logik Schritt für Schritt:
    # 💡 Tipp: Beachte Datentypen und das abschließende return!
        pass

    # ==========================================================================
    # 🎯 TEILZIEL 3 (TODO 3): Dunder-Methode "__str__(self)"
    # Gibt einen formatierten String zurück:
    # "{anzahl}x {name} (je {preis:.2f} €) = {gesamtpreis:.2f} €"
    #
    # Beispiel: Bei name="Milch", preis=1.29, anzahl=2:
    # -> "2x Milch (je 1.29 €) = 2.58 €"
    # ==========================================================================
    def __str__(self):
        # 🎯 TEILZIEL 3: Implementiere die Logik Schritt für Schritt:
    # 💡 Tipp: Beachte Datentypen und das abschließende return!
        pass


class Warenkorb:
    # ==========================================================================
    # 🎯 TEILZIEL 4 (TODO 4): Konstruktor für Warenkorb
    # Parameter: self
    # Initialisiere: self.artikel_liste als leere Liste []
    # ==========================================================================
    def __init__(self):
        # 🎯 TEILZIEL 4: Implementiere die Logik Schritt für Schritt:
    # 💡 Tipp: Beachte Datentypen und das abschließende return!
        pass

    # ==========================================================================
    # 🎯 TEILZIEL 5 (TODO 5): Methode "artikel_hinzufuegen(self, artikel)"
    # Hängt das übergebene Artikel-Objekt an 'self.artikel_liste' an (.append).
    # ==========================================================================
    def artikel_hinzufuegen(self, artikel):
        # 🎯 TEILZIEL 5: Implementiere die Logik Schritt für Schritt:
    # 💡 Tipp: Beachte Datentypen und das abschließende return!
        pass

    # ==========================================================================
    # 🎯 TEILZIEL 6 (TODO 6): Methode "gesamtsumme(self)"
    # Berechnet die Summe der Gesamtpreise aller Artikel in self.artikel_liste
    # und gibt diese als float zurück.
    #
    # Tipp mit Schleife:
    # total = 0.0
    # for item in self.artikel_liste:
    #     total += item.gesamtpreis()
    # return total
    # ==========================================================================
    def gesamtsumme(self):
        # 🎯 TEILZIEL 6: Implementiere die Logik Schritt für Schritt:
    # 💡 Tipp: Beachte Datentypen und das abschließende return!
        pass

    # ==========================================================================
    # 🎯 TEILZIEL 7 (TODO 7): Methode "bon_text(self)"
    # Erzeugt einen formatierten mehrzeiligen String für den Kassenzettel.
    # Format:
    # --- KASSENZETTEL ---
    # 2x Milch (je 1.29 €) = 2.58 €
    # 1x Brot (je 2.49 €) = 2.49 €
    # --------------------
    # Gesamtsumme: 5.07 €
    #
    # Tipp: Baue eine Liste von Zeilen und verbinde sie am Ende mit "\n".join(...)
    # ==========================================================================
    def bon_text(self):
        # 🎯 TEILZIEL 7: Implementiere die Logik Schritt für Schritt:
    # 💡 Tipp: Beachte Datentypen und das abschließende return!
        pass


# ==============================================================================
# Hauptprogramm zum Ausprobieren:
# (Ausführen mit 'python3 aufgabe.py')
# ==============================================================================
if __name__ == "__main__":
    print("🛒 --- SUPERMARKT EINKAUF --- 🛒")
    korb = Warenkorb()

    a1 = Artikel("Milch", 1.29, 2)
    a2 = Artikel("Brot", 2.49, 1)
    a3 = Artikel("Schokolade", 0.99, 3)

    if hasattr(korb, "artikel_liste"):
        korb.artikel_hinzufuegen(a1)
        korb.artikel_hinzufuegen(a2)
        korb.artikel_hinzufuegen(a3)
        print(korb.bon_text())
    else:
        print("💡 Hinweis: Implementiere die TODOs, um den Kassenbon zu drucken!")
