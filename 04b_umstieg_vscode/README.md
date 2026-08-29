# Kapitel 04b: Umstieg von Thonny auf Visual Studio Code (VS Code) 🚀💻

Herzlich willkommen zum Exkurs!

Bisher hast du deine Aufgaben vielleicht in **Thonny** bearbeitet. Thonny ist super für die ersten Schritte. Aber ab jetzt werden unsere Projekte größer (mehrere Dateien, Klassen, Tests). 

**Visual Studio Code (VS Code)** ist die beliebteste und mächtigste Entwicklungsumgebung der Welt. Hier lernst du, wie du sie einrichtest und wie ein Profi nutzt!

---

## 🏗️ Das wichtigste Grundkonzept: "Ordner öffnen" (Open Folder)

- In Thonny öffnet man meistens nur einzelne Dateien (wie `aufgabe.py`).
- In **VS Code öffnet man immer den gesamten Projektordner**:
  1. Starte VS Code.
  2. Klicke auf **Datei &rarr; Ordner öffnen...** (oder `Strg + K`, dann `Strg + O` / auf Mac: `Cmd + O`).
  3. Wähle den Ordner `Aufgaben-Python` aus.

Jetzt hast du links im Explorer die volle Übersicht über alle Kapitel!

---

## 🧩 Die besten Erweiterungen (Extensions)

Drücke `Strg + Shift + X` (Mac: `Cmd + Shift + X`), um den Erweiterungs-Store zu öffnen. Installiere folgende Plugins:

1. **Python & Pylance (von Microsoft):**
   Aktiviert Autovervollständigung (IntelliSense), Syntaxprüfung und den Ausführen-Button.
2. **Error Lens (⭐ Geheimtipp!):**
   Zeigt Fehler und Warnungen direkt als Text in der Codezeile an! Du musst nicht erst lange im Terminal nach Zeilennummern suchen.
3. **Material Icon Theme:**
   Hübsche, bunte Datei-Symbole für Python, Markdown, HTML und Git.
4. **Better Comments:**
   Färbt `# TODO`, `# !` und `# ?` farblich ein.
5. **Black Formatter:**
   Formatiert deinen Code beim Speichern automatisch sauber und ordentlich.

---

## ⌨️ Die wichtigsten Tastenkombinationen (Shortcuts)

| Aktion | Windows / Linux | macOS |
| :--- | :--- | :--- |
| **Datei speichern** | `Strg + S` | `Cmd + S` |
| **Terminal öffnen / schließen** | `Strg + \`` (oder `Strg + J`) | `Cmd + \`` (oder `Cmd + J`) |
| **Command Palette (Befehle suchen)** | `Strg + Shift + P` | `Cmd + Shift + P` |
| **Code formatieren** | `Alt + Shift + F` | `Option + Shift + F` |
| **Nächstes gleiches Wort markieren** | `Strg + D` | `Cmd + D` |
| **Skript ausführen** | `Strg + F5` (oder Play-Button oben) | `Cmd + F5` |

---

## 🧪 Ausprobieren in `vscode_test.py`

Öffne `vscode_test.py` in VS Code und teste:
1. Wie **Error Lens** Fehler in Echtzeit anzeigt.
2. Wie **IntelliSense** Methoden vorschlägt, wenn du `auto.` tippst.
3. Öffne das Terminal mit `Strg + \`` und führe `python3 test_all.py` aus!
