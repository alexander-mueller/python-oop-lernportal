# Kapitel 04: Schöne Ausgaben mit `__str__` 🧾

Hast du schon mal versucht, ein selbst erstelltes Objekt direkt mit `print()` auszugeben?

```python
class Buch:
    def __init__(self, titel, autor):
        self.titel = titel
        self.autor = autor

mein_buch = Buch("Harry Potter", "J.K. Rowling")
print(mein_buch)
```
Die Ausgabe sieht dann so aus:
```
<__main__.Buch object at 0x7fa2b0485d90>
```
Das ist kryptisch und hilft im Alltag nicht weiter. Aber Python hat dafür eine geniale Dunder-Methode: **`__str__`**!

---

## 🍕 Vollständiges Praxisbeispiel: Pizza & Pizzeria-Bestellung

```python
# 1. Klasse Pizza mit __str__:
class Pizza:
    def __init__(self, name, preis, extra_kaese=False):
        self.name = name
        self.preis = preis
        self.extra_kaese = extra_kaese
        if extra_kaese:
            self.preis += 1.50

    def __str__(self):
        kaese = " (mit Extra-Käse)" if self.extra_kaese else ""
        return f"Pizza {self.name}{kaese} - {self.preis:.2f} €"

# 2. Klasse Bestellung verwaltet Pizza-Objekte:
class Bestellung:
    def __init__(self, kunden_name):
        self.kunden_name = kunden_name
        self.pizzen = []

    def pizza_hinzufuegen(self, pizza):
        self.pizzen.append(pizza)

    def gesamtpreis(self):
        return sum(p.preis for p in self.pizzen)

    def rechnung_drucken(self):
        zeilen = [f"=== RECHNUNG FÜR {self.kunden_name} ==="]
        for p in self.pizzen:
            zeilen.append(f"- {p}")  # Ruft p.__str__() auf!
        zeilen.append(f"Gesamt: {self.gesamtpreis():.2f} €")
        return "\n".join(zeilen)

# Testen:
bestellung = Bestellung("Lisa")
bestellung.pizza_hinzufuegen(Pizza("Margherita", 8.50))
bestellung.pizza_hinzufuegen(Pizza("Salami", 9.50, extra_kaese=True))
print(bestellung.rechnung_drucken())
```

---

## ⚠️ Stolperfallen bei `__str__`

1. **`__str__` muss immer einen `str` zurückgeben (`return`), NIEMALS `print`:**
   - ❌ `def __str__(self): print(self.name)` (Falsch!)
   - ✅ `def __str__(self): return str(self.name)` (Richtig!)
2. **Unterstriche beachten:**
   - Zwei Unterstriche vor und nach `str`: `__str__`.

---

## 🎯 Deine Aufgabe: Der Supermarkt-Kassenzettel

In `aufgabe.py` programmierst du zwei Klassen:
1. `Artikel`: Ein Produkt mit Name, Einzelpreis und Anzahl.
   - `__str__`: Erzeugt einen Kassenbon-Text wie `"3x Apfel (je 0.50 €) = 1.50 €"`.
   - `gesamtpreis()`: Berechnet den Preis für diesen Artikel (`preis * anzahl`).
2. `Warenkorb`: Verwaltet eine Liste von `Artikel`-Objekten.
   - `artikel_hinzufuegen()`: Packt einen Artikel in den Warenkorb.
   - `gesamtsumme()`: Berechnet die Gesamtsumme aller Artikel.
   - `bon_text()`: Erzeugt einen formatierten mehrzeiligen Kassenbon.

### Testen:
```bash
python3 test_aufgabe.py
```
