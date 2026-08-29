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

## ✨ Die `__str__`-Methode

Wann immer Python ein Objekt in einen Text umwandeln soll (z.B. bei `print(mein_objekt)` oder `str(mein_objekt)` oder in einem f-String `f"Das Buch: {mein_objekt}"`), schaut Python nach, ob deine Klasse eine `__str__`-Methode hat.

Wenn ja, ruft Python sie automatisch auf:

```python
class Buch:
    def __init__(self, titel, autor):
        self.titel = titel
        self.autor = autor

    def __str__(self):
        # Muss immer einen STRING zurückgeben (return)!
        return f"'{self.titel}' von {self.autor}"

mein_buch = Buch("Harry Potter", "J.K. Rowling")
print(mein_buch)  # Ausgabe: 'Harry Potter' von J.K. Rowling 🎉
```

---

## 🧺 Objekte in Listen verwalten

Oft hat man Objekte, die eine Liste von *anderen* Objekten verwalten (z.B. ein Warenkorb, der Artikel enthält, oder ein Bus, der Fahrgäste enthält):

```python
class Schultasche:
    def __init__(self):
        self.buecher = []  # Startet mit einer leeren Liste

    def buch_einpacken(self, buch):
        self.buecher.append(buch)

    def inhalt_anzeigen(self):
        for b in self.buecher:
            print(f"- {b}")  # Hier wird automatisch b.__str__() genutzt!
```

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
