# Kapitel 02: Der Konstruktor `__init__` und das geheimnisvolle `self` 💳

Im ersten Kapitel haben wir Attribute noch manuell nach dem Erstellen zugewiesen:
```python
bello = Haustier()
bello.name = "Bello"
bello.alter = 3
```
Das ist mühsam und fehleranfällig: Was passiert, wenn man vergisst, `.alter` zu setzen? Richtig: Das Programm stürzt ab, sobald jemand darauf zugreift!

Deshalb gibt es in Python den **Konstruktor**: `__init__`.

---

## 🛠️ Was ist `__init__`?

`__init__` steht für *initialisieren* (vorbereiten/startklar machen). 

Es ist eine **spezielle Methode**, die Python **automatisch aufruft**, sobald du ein neues Objekt erstellst.

---

## 📱 Vollständiges Praxisbeispiel: Die Smartphone-Klasse

```python
class Smartphone:
    # Der Konstruktor wird automatisch beim Erstellen aufgerufen:
    def __init__(self, modell, speicher_gb, akku=100):
        self.modell = modell              # z.B. "iPhone 15"
        self.speicher_gb = speicher_gb      # z.B. 128
        self.akku = akku                  # Standardwert ist 100%

    def benutzen(self, minuten):
        verbrauch = minuten * 0.5
        if self.akku >= verbrauch:
            self.akku -= verbrauch
            return f"{self.modell}: {minuten} Min. genutzt. Akku: {self.akku:.0f}%"
        else:
            self.akku = 0
            return f"{self.modell}: Akku ist leer!"

    def aufladen(self):
        self.akku = 100
        return f"{self.modell} ist wieder voll aufgeladen (100%)!"

# Verwendung:
mein_handy = Smartphone("iPhone 15", 256)
altes_handy = Smartphone("Galaxy S10", 64, akku=40)

print(mein_handy.benutzen(30))   # Verbraucht 15% -> 85% Rest
print(altes_handy.benutzen(90))  # Akku wird leer!
print(altes_handy.aufladen())     # Wieder 100%
```

---

## 🪞 Was bedeutet eigentlich `self`?

- `self` bedeutet auf Deutsch **"ich selbst"** oder **"dieses konkrete Objekt hier"**.
- Wenn du `mein_handy.benutzen(30)` aufrufst, übergibt Python das neu entstandene `mein_handy`-Objekt automatisch als erstes Argument `self`.
- `self.akku -= verbrauch` zieht den Strom genau vom Akku dieses einen Handys ab.

---

## ⚠️ Typische Fehler vermeiden

1. **`__init__` mit zwei Unterstrichen schreiben:**
   - ❌ `def _init_(self):` (wird nicht aufgerufen!)
   - ✅ `def __init__(self):` (korrekt!)
2. **`self` bei jeder Methode als ersten Parameter:**
   - ❌ `def einzahlen(betrag):` -> führt zu `TypeError: einzahlen() takes 1 positional argument but 2 were given`
   - ✅ `def einzahlen(self, betrag):`
3. **Zuweisungsrichtung beachten:**
   - ❌ `inhaber = self.inhaber` (falsch herum!)
   - ✅ `self.inhaber = inhaber` (speichert den Parameter im Attribut)

---

## 🎯 Deine Aufgabe: Das Bankkonto

Öffne `aufgabe.py`. Du programmierst eine Klasse `Bankkonto`:
1. Schreibe den Konstruktor `__init__`.
2. Ergänze Methoden zum Einzahlen (`einzahlen`) und Auszahlen (`auszahlen`), die darauf achten, dass man nicht ins Minus rutscht.
3. Ergänze eine Methode `info_text()`.

### Testen:
```bash
python3 test_aufgabe.py
```
