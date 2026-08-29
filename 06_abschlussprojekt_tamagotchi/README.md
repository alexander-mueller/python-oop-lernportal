# Kapitel 06: Abschlussprojekt – Dein eigenes Tamagotchi! 🥚🐣

Herzlichen Glückwunsch! Du hast alle grundlegenden Konzepte der objektorientierten Programmierung gemeistert:
- Klassen & Instanzen
- `__init__` & `self`
- Methoden & Zustandsveränderungen
- `__str__` für ansprechende Textausgaben
- Beziehungen zwischen Objekten

Jetzt setzen wir alles in einem **vollwertigen, interaktiven Mini-Projekt** zusammen: Einem virtuellen Haustier (Tamagotchi)!

---

## 🎮 Wie funktioniert das Tamagotchi?

Dein Tamagotchi hat Eigenschaften, die sich durch deine Aktionen (und mit der Zeit) verändern:
- **Hunger** (0 = vollgefressen, 100 = verhungert)
- **Müdigkeit** (0 = voller Energie, 100 = total erschöpft)
- **Glück** (0 = unglücklich, 100 = überglücklich)
- **Alter in Tagen**

Du kannst mit ihm interagieren:
- 🍎 **Füttern** (`fuettern`): Senkt den Hunger, macht etwas müde und etwas glücklicher.
- ⚽ **Spielen** (`spielen`): Steigert das Glück, macht aber hungrig und müde. Zu müde Haustiere weigern sich zu spielen!
- 💤 **Schlafen** (`schlafen`): Setzt die Müdigkeit auf 0, lässt einen Tag vergehen (`alter_tage += 1`), macht aber etwas hungrig.
- ⏳ **Zeit vergeht** (`zeit_vergeht`): Das Haustier wird hungriger, müder und etwas trauriger. Wenn der Hunger 100 erreicht oder Glück 0 wird, schläft es für immer ein...

---

## 🕹️ Das interaktive Spiel

Sobald du die `Tamagotchi`-Klasse in `aufgabe.py` fertig programmiert hast und alle Tests grün sind, kannst du das Spiel direkt im Terminal starten:

```bash
python3 tamagotchi_spiel.py
```
Dort kannst du deinem Haustier einen Namen geben und dich live um es kümmern!

---

## 🎯 Deine Aufgabe

Öffne `aufgabe.py` und implementiere die `Tamagotchi`-Klasse von TODO 1 bis TODO 6.

### Tests ausführen:
```bash
python3 test_aufgabe.py
```
