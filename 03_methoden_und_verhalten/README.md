# Kapitel 03: Methoden & Verhalten – Wenn Objekte lebendig werden ⚔️

Bisher haben unsere Objekte hauptsächlich Daten gespeichert (wie Name oder Kontostand). Aber Objekte können noch viel mehr: **Sie können Aktionen ausführen!**

Funktionen, die innerhalb einer Klasse definiert sind, nennt man **Methoden**.

---

## 🏃‍♀️ Was unterscheidet eine Methode von einer normalen Funktion?

1. Eine Methode steht **eingerückt in der Klasse**.
2. Das **erste Argument ist immer `self`**.
3. Über `self` hat die Methode direkten Zugriff auf alle Eigenschaften des Objekts und kann diese verändern.

```python
class Zauberer:
    def __init__(self, name, mana=50):
        self.name = name
        self.mana = mana

    # Das hier ist eine Methode:
    def zauberspruch_wirken(self, mana_kosten):
        if self.mana >= mana_kosten:
            self.mana -= mana_kosten
            print(f"{self.name} wirkt einen Zauber! Verbleibendes Mana: {self.mana}")
            return True
        else:
            print(f"{self.name} hat nicht genug Mana!")
            return False

merlin = Zauberer("Merlin", 30)
merlin.zauberspruch_wirken(10)  # self wird automatisch merlin!
```

---

## 🤝 Wenn Objekte miteinander interagieren!

Das Spannendste an der objektorientierten Programmierung ist, wenn **ein Objekt mit einem anderen Objekt interagiert**.

Du kannst ein ganzes Objekt als Parameter an die Methode eines anderen Objekts übergeben:

```python
class Spieler:
    def __init__(self, name, geld):
        self.name = name
        self.geld = geld

    def bezahle_an(self, empfaenger, betrag):
        if self.geld >= betrag:
            self.geld -= betrag
            empfaenger.geld += betrag  # Wir greifen direkt auf das andere Objekt zu!
            return True
        return False
```

---

## 🎯 Deine Aufgabe: Das RPG-Duell

In `aufgabe.py` erstellst du eine Klasse `Held` für ein Rollenspiel:
- Ein Held hat `name`, `leben`, `max_leben` und `angriffskraft`.
- Ein Held kann Schaden erleiden (`schaden_erleiden`), geheilt werden (`heilen`) und einen anderen Helden angreifen (`angreifen(gegner)`).
- Du sorgst mit Bedingungen dafür, dass die Lebenspunkte nicht unter `0` fallen und nicht über `max_leben` steigen!

### Testen:
```bash
python3 test_aufgabe.py
```
