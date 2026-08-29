# Kapitel 12: Exceptions & Fehlerbehandlung 🛡️🛑

In diesem Kapitel lernst du, wie du deine Programme vor unkontrollierten Abstürzen schützt und saubere, selbsterklärende Fehlermeldungen mit **benutzerdefinierten Exceptions** wirfst.

---

## 🎯 Was du lernst

1. **Die Notbremse im Code (`raise`):** Wenn eine Funktion ungültige Daten erhält (z.B. negativer Betrag), wirft sie gezielt eine Exception aus.
2. **Sauberes Abfangen (`try / except`):** Wie du Fehler auffängst, ohne dass das gesamte Programm abstürzt.
3. **Vollständige Kontrollstruktur:**
   - `try`: Code, der fehlschlagen könnte.
   - `except ExceptionTyp as e`: Fehler fangen und behandeln.
   - `else`: Wird nur ausgeführt, wenn **kein** Fehler aufgetreten ist.
   - `finally`: Wird **immer** ausgeführt (z.B. Karte entnehmen, Dateien schließen).
4. **Eigene Exception-Klassen definieren:**
   ```python
   class BankFehler(Exception):
       """Basis-Fehlerklasse für unsere Bank-App."""
       pass

   class KontoGesperrtError(BankFehler):
       pass
   ```
5. **Praxisbeispiel:** Ein robuster **Bankkonto- und Geldautomat-Simulator** mit PIN-Sicherheit, Kontosperrung nach 3 Fehlversuchen und Deckungsprüfung.

---

## 📁 Die Dateien in diesem Ordner

- **`index.html`**: Die interaktive Lernseite mit visueller Notbremse-Analogie, Flowchart, Codebeispielen und Checkliste.
- **`aufgabe.py`**: Dein Arbeitsblatt zum Implementieren der Exception-Klassen, des `Bankkonto`s und der Geldautomat-Funktion.
- **`test_aufgabe.py`**: Automatische Unittest-Suite (`python3 test_aufgabe.py`).
- **`musterloesung.py`**: Vollständig ausprogrammierte Beispiellösung.

---

## 🚀 Schnellstart

```bash
# 1. Bearbeite aufgabe.py
# 2. Teste deine Lösung:
python3 test_aufgabe.py
```
