# Kapitel 13: Datei-Persistenz (JSON & CSV) 💾📁

In diesem Kapitel lernst du, wie du deine Python-Objekte dauerhaft auf der Festplatte speicherst, sodass deine Daten auch nach dem Beenden des Skripts oder Ausschalten des Computers erhalten bleiben.

---

## 🎯 Was du lernst

1. **Flüchtiger RAM vs. Dauerhafte Festplatte:** Warum Daten im Arbeitsspeicher beim Programmende verschwinden und wie Dateien für dauerhafte Speicherung (Persistenz) sorgen.
2. **Sauberer Dateizugriff mit `with open(...)`:**
   ```python
   with open("savegame.json", "w", encoding="utf-8") as f:
       # Datei wird automatisch sicher geschlossen, selbst bei Fehlern!
   ```
3. **JSON (JavaScript Object Notation):**
   - Das Standard-Format für verschachtelte Daten und Konfigurationen.
   - `json.dump(daten, f, indent=4, ensure_ascii=False)` zum Schreiben.
   - `daten = json.load(f)` zum Einlesen.
4. **Objekt-Serialisierung in OOP:**
   - `to_dict(self)`: Wandelt ein Objekt in ein serialisierbares Dictionary um.
   - `from_dict(cls, data)`: Erstellt aus einem Dictionary wieder eine echte Klasseninstanz.
5. **CSV (Comma-Separated Values):**
   - Ideal für flache Tabellendaten (z.B. für Excel, Google Sheets oder Numbers).
   - `csv.DictWriter` und `csv.DictReader`.
6. **Praxisbeispiel:** Ein **Savegame- und Highscore-Manager** für ein RPG / Spiel.

---

## 📁 Die Dateien in diesem Ordner

- **`index.html`**: Die interaktive Lernseite mit Tagebuch-Analogie, JSON- vs. CSV-Vergleichstabelle, Codebeispielen und Checkliste.
- **`aufgabe.py`**: Dein Arbeitsblatt zum Implementieren der Klassen `Spieler` und `Spielstand`.
- **`test_aufgabe.py`**: Automatische Unittest-Suite (`python3 test_aufgabe.py`).
- **`musterloesung.py`**: Vollständig ausprogrammierte Beispiellösung.

---

## 🚀 Schnellstart

```bash
# 1. Bearbeite aufgabe.py
# 2. Teste deine Lösung:
python3 test_aufgabe.py
```
