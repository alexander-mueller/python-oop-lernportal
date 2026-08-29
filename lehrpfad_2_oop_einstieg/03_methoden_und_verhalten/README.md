# Kapitel 03: Methoden & Verhalten – Wenn Objekte lebendig werden ⚔️

Bisher haben unsere Objekte hauptsächlich Daten gespeichert (wie Name oder Kontostand). Aber Objekte können noch viel mehr: **Sie können Aktionen ausführen!**

Funktionen, die innerhalb einer Klasse definiert sind, nennt man **Methoden**.

---

## 🏎️ Vollständiges Praxisbeispiel: Die Rennauto-Klasse

```python
class Rennauto:
    def __init__(self, fahrer, speed, tank=50):
        self.fahrer = fahrer
        self.speed = speed          # z.B. 220 km/h
        self.tank = tank            # Aktueller Tank in Litern
        self.max_tank = tank        # Maximales Tankvolumen
        self.gefahrene_km = 0

    def fahren(self, km):
        verbrauch = km * 0.2
        if self.tank >= verbrauch:
            self.tank -= verbrauch
            self.gefahrene_km += km
            return f"{self.fahrer} fährt {km} km (Tank: {self.tank:.1f}L übrig)"
        else:
            return f"{self.fahrer} hat nicht genug Sprit für {km} km!"

    def tanken(self, liter):
        freier_platz = self.max_tank - self.tank
        getankt = min(freier_platz, liter)
        self.tank += getankt
        return f"{self.fahrer} tankt {getankt:.1f} Liter nach"

    def duell_gegen(self, gegner_auto):
        if self.speed > gegner_auto.speed:
            return f"{self.fahrer} überholt {gegner_auto.fahrer}!"
        else:
            return f"{gegner_auto.fahrer} zieht an {self.fahrer} vorbei!"

# Testen:
auto1 = Rennauto("Max", 240, 40)
auto2 = Rennauto("Lewis", 235, 50)
print(auto1.fahren(100))
print(auto1.duell_gegen(auto2))
```

---

## 🤝 Wenn Objekte miteinander interagieren!

Du kannst ein ganzes Objekt als Parameter an die Methode eines anderen Objekts übergeben (wie bei `auto1.duell_gegen(auto2)` oder `ritter.angreifen(drache)`).

---

## ⚠️ Typische Stolperfallen in diesem Kapitel

1. **Grenzen beachten (Min/Max Clamping):**
   - Lebenspunkte dürfen nach Schaden nie negativ werden: `if self.leben < 0: self.leben = 0`
   - Lebenspunkte dürfen nach Heilung nie über `max_leben` steigen: `self.leben = min(self.max_leben, self.leben + heilung)`
2. **Besiegte Objekte können nicht mehr handeln:**
   - Vor Aktionen wie Angreifen oder Heilen immer prüfen: `if not self.ist_am_leben: return False` bzw. `return 0`

---

## 🎯 Deine Aufgabe: Das RPG-Duell

In `aufgabe.py` erstellst du die Klasse `Held`:
- `__init__(self, name, leben=100, angriffskraft=15)`
- `schaden_erleiden(self, schaden)`
- `heilen(self, heilung)`
- `angreifen(self, gegner)`
- `status_text(self)`

### Testen:
```bash
python3 test_aufgabe.py
```
