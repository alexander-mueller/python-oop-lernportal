# Kapitel 07: Referenzen, Speicher & Stammbäume 🧠🌳

In diesem Kapitel lernst du ein fundamentales Konzept moderner Programmiersprachen: **Objektreferenzen und Arbeitsspeicher (RAM)**.

---

## 🎯 Was du lernst

1. **Variablen als Zeiger:** Eine Variable enthält nicht das Objekt selbst, sondern zeigt auf dessen Speicherplatz.
2. **Aliasing (`b = a`):** Zwei Variablen können auf dasselbe veränderliche Objekt zeigen.
3. **`is` vs. `==`:**
   - `==` prüft, ob zwei Objekte den **gleichen Wert** haben.
   - `is` prüft, ob es sich um **dasselbe Objekt** an derselben Speicherstelle (`id(a) == id(b)`) handelt.
4. **Mutable vs. Immutable:**
   - *Mutable:* Listen, Dictionaries, eigene Objekte (können verändert werden).
   - *Immutable:* Zahlen, Strings, Tupel (sind unveränderlich).
5. **Stammbaum-Strukturen:** Ein Objekt wird von mehreren anderen Objekten referenziert.

---

## 📁 Die Dateien in diesem Ordner

- **`index.html`**: Die interaktive Lernseite mit visuellen Boxen & Erklärungen.
- **`aufgabe.py`**: Dein Arbeitsblatt zum Implementieren der `Person`-Stammbaum-Klasse.
- **`test_aufgabe.py`**: Automatische Tests (`python3 test_aufgabe.py`).
- **`musterloesung.py`**: Vollständig ausprogrammierte Beispiellösung.

---

## 🚀 Schnellstart

```bash
# 1. Bearbeite aufgabe.py
# 2. Teste deine Lösung:
python3 test_aufgabe.py
```
