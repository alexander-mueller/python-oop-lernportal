# Kapitel 09: Eigene Unit Tests schreiben & TDD 🧪

In diesem Kapitel lernst du, wie professionelle Software-Entwickler ihren Code mit automatischen Tests absichern und wie **Test-Driven Development (TDD)** funktioniert.

---

## 🎯 Was du lernst

1. **Warum automatische Unit Tests?**
   - Nie wieder manuelle `print()`-Ausgaben kontrollieren.
   - Sofortiges Feedback bei Fehlern (Regression Prevention).
   - Saubere Schnittstellendokumentation.
2. **Das `unittest`-Modul in Python:**
   - Eigene Testklassen erstellen: `class MeinTest(unittest.TestCase)`
   - Jede Testmethode muss mit `test_` beginnen (z.B. `def test_add(self):`).
   - Die `setUp(self)`-Methode: Wird automatisch vor **jedem einzelnen Test** ausgeführt, um frische Testdaten bereitzustellen.
3. **Die wichtigsten Assert-Methoden:**
   - `self.assertEqual(a, b)`: Prüft $a == b$.
   - `self.assertAlmostEqual(a, b, places=2)`: Prüft Float-Rundung bei Kommazahlen.
   - `self.assertTrue(x)` / `self.assertFalse(x)`: Prüft Wahrheitswerte.
   - `self.assertIn(item, list)` / `self.assertNotIn(item, list)`: Prüft Enthaltensein.
   - `with self.assertRaises(FehlerTyp):`: Prüft, ob erwartete Fehler (Exceptions wie `ValueError`, `ZeroDivisionError`) geworfen werden.
4. **Test-Driven Development (TDD):**
   - 🔴 **Red:** Schreibe zuerst den Test (schlägt fehl).
   - 🟢 **Green:** Schreibe den minimalen Code, der den Test besteht.
   - 🔵 **Refactor:** Verbessere und säubere den Code ohne Angst vor Regressionen.

---

## 📁 Die Dateien in diesem Ordner

- **`index.html`**: Ausführliche interaktive HTML-Erklärung mit Assert-Tabelle, visuellen Boxen & Tipps.
- **`aufgabe.py`**: Vorgegebene Klassen `Taschenrechner` und `Bankkonto` sowie die Test-Klassen mit TODOs zum Selbstausfüllen.
- **`test_aufgabe.py`**: Der Metatest-Runner, der deine geschriebenen Unit Tests validiert (`python3 test_aufgabe.py`).
- **`musterloesung.py`**: Vollständig ausprogrammierte Testsuite.

---

## 🚀 Schnellstart

```bash
# 1. Bearbeite die Test-Klassen in aufgabe.py
# 2. Führe deine eigenen Tests aus:
python3 aufgabe.py

# 3. Validiere deine Tests mit dem Metatest-Skript:
python3 test_aufgabe.py
```
