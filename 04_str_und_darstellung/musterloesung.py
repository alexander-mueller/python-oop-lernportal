"""
Kapitel 04: __str__ und Objektlisten – Musterlösung
===================================================
"""

class Artikel:
    def __init__(self, name, preis, anzahl=1):
        self.name = name
        self.preis = float(preis)
        self.anzahl = int(anzahl)

    def gesamtpreis(self):
        return self.preis * self.anzahl

    def __str__(self):
        return f"{self.anzahl}x {self.name} (je {self.preis:.2f} €) = {self.gesamtpreis():.2f} €"


class Warenkorb:
    def __init__(self):
        self.artikel_liste = []

    def artikel_hinzufuegen(self, artikel):
        self.artikel_liste.append(artikel)

    def gesamtsumme(self):
        return sum(item.gesamtpreis() for item in self.artikel_liste)

    def bon_text(self):
        zeilen = ["--- KASSENZETTEL ---"]
        for artikel in self.artikel_liste:
            zeilen.append(str(artikel))
        zeilen.append("--------------------")
        zeilen.append(f"Gesamtsumme: {self.gesamtsumme():.2f} €")
        return "\n".join(zeilen)


if __name__ == "__main__":
    korb = Warenkorb()
    korb.artikel_hinzufuegen(Artikel("Milch", 1.29, 2))
    korb.artikel_hinzufuegen(Artikel("Brot", 2.49, 1))
    korb.artikel_hinzufuegen(Artikel("Schokolade", 0.99, 3))
    print(korb.bon_text())
