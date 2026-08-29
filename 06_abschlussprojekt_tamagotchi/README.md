# Kapitel 06: Abschlussprojekt – Dein eigenes Tamagotchi! 🥚🐣

Herzlichen Glückwunsch! Du hast alle grundlegenden Konzepte der objektorientierten Programmierung gemeistert:
- Klassen & Instanzen
- `__init__` & `self`
- Methoden & Zustandsveränderungen
- `__str__` für ansprechende Textausgaben
- Beziehungen zwischen Objekten

---

## 🤖 Vollständiges Beispiel: Roboter mit Lebenszyklus

```python
class Roboter:
    def __init__(self, name):
        self.name = name
        self.energie = 100
        self.ist_aktiv = True

    def _begrenzen(self, wert):
        return max(0, min(100, wert))

    def arbeiten(self, stunden):
        if not self.ist_aktiv:
            return f"{self.name} ist ausgeschaltet!"
        verbrauch = stunden * 20
        self.energie = self._begrenzen(self.energie - verbrauch)
        if self.energie == 0:
            self.ist_aktiv = False
            return f"{self.name} schaltet sich ab!"
        return f"{self.name} hat gearbeitet (Energie: {self.energie}%)"

    def aufladen(self):
        self.energie = 100
        self.ist_aktiv = True
        return f"{self.name} ist wieder voll!"

    def __str__(self):
        status = "Aktiv ⚡" if self.ist_aktiv else "Ausgeschaltet 💤"
        return f"[{self.name}] Energie: {self.energie}% | Status: {status}"

# Testen:
bot = Roboter("Wall-E")
print(bot)
print(bot.arbeiten(3))
print(bot)
print(bot.aufladen())
```

---

## 🎮 Wie funktioniert das Tamagotchi?

- **Hunger** (0 bis 100)
- **Müdigkeit** (0 bis 100)
- **Glück** (0 bis 100)
- **Alter in Tagen**

---

## 🕹️ Das interaktive Spiel

Sobald du die `Tamagotchi`-Klasse in `aufgabe.py` fertig programmiert hast und alle Tests grün sind, kannst du das Spiel direkt im Terminal starten:

```bash
python3 tamagotchi_spiel.py
```

---

## 🎯 Deine Aufgabe

Öffne `aufgabe.py` und implementiere die `Tamagotchi`-Klasse von TODO 1 bis TODO 6.

### Tests ausführen:
```bash
python3 test_aufgabe.py
```
