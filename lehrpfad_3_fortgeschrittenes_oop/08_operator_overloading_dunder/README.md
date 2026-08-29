# Kapitel 08: Operator Overloading & Dunder-Methoden ➕

In diesem Kapitel lernst du, wie du deine eigenen Klassen mit Pythons eingebauten Operatoren (`+`, `-`, `*`, `==`, `<`, `len()`, `abs()`) ausstattest.

---

## 🎯 Was du lernst

1. **Was sind Dunder-Methoden?** Methoden mit führenden und nachgestellten doppelten Unterstrichen (**D**ouble **Under**score, z.B. `__add__`).
2. **Magische Übersetzung:** Wenn du `a + b` schreibst, ruft Python im Hintergrund `a.__add__(b)` auf.
3. **Mathematische Operatoren überladen:**
   - `__add__(self, other)` für `+`
   - `__sub__(self, other)` für `-`
   - `__mul__(self, other)` für `*` (z.B. Skalarmultiplikation mit Zahlen oder Skalarprodukt)
   - `__rmul__(self, other)` für `*` von links (z.B. `3 * v`)
4. **Vergleiche überladen:**
   - `__eq__(self, other)` für `==`
   - `__lt__(self, other)` für `<`
   - `__le__(self, other)` für `<=`
5. **Objekt- und Container-Dunder:**
   - `__str__` (für Menschen) vs. `__repr__` (für Entwickler / Debugger)
   - `__abs__` für `abs(objekt)` (z.B. Vektorlänge)
   - `__len__` für `len(objekt)` (z.B. Anzahl von Wegpunkten)
   - `__getitem__` für Indexzugriff `objekt[i]`

---

## 📁 Die Dateien in diesem Ordner

- **`index.html`**: Interaktive Lernseite mit visuellen Tabellen, Code-Beispielen & Ausklapp-Hilfen.
- **`aufgabe.py`**: Dein Arbeitsblatt zum Implementieren von `Vektor2D` und `Wegstrecke`.
- **`test_aufgabe.py`**: Automatische Tests (`python3 test_aufgabe.py`).
- **`musterloesung.py`**: Vollständig ausprogrammierte Beispiellösung.

---

## 🚀 Schnellstart

```bash
# 1. Bearbeite aufgabe.py
# 2. Teste deine Lösung:
python3 test_aufgabe.py
```
