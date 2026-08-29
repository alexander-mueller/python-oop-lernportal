# Kapitel 04b: Umstieg & Installation von Visual Studio Code (VS Code) 🚀💻

Herzlich willkommen zum Praxis-Guide!

Bisher hast du deine Aufgaben vielleicht in **Thonny** bearbeitet. Thonny ist super für die ersten Schritte. Aber ab jetzt werden unsere Projekte größer (mehrere Dateien, Klassen, Tests). 

**Visual Studio Code (VS Code)** von Microsoft ist die beliebteste und modernste Entwicklungsumgebung der Welt. Hier erfährst du, wie du sie installierst und einrichtest.

---

## 📥 1. Installation Schritt-für-Schritt

### 🪟 Für Windows (Windows 10 / 11):
1. Gehe auf [code.visualstudio.com](https://code.visualstudio.com) und lade den **Windows Installer** herunter.
2. Starte die Datei `VSCodeUserSetup-x64-...exe`.
3. **⚠️ SEHR WICHTIG:** Setze im Schritt *"Zusätzliche Aufgaben"* alle 4 Haken:
   - [x] *Aktion 'Mit Code öffnen' zum Windows Explorer-Dateikontextmenü hinzufügen*
   - [x] *Aktion 'Mit Code öffnen' zum Windows Explorer-Verzeichniskontextmenü hinzufügen*
   - [x] *Code als Editor für unterstützte Dateitypen registrieren*
   - [x] *Zu PATH hinzufügen*
4. Klicke auf **Installieren** und **Fertigstellen**.

### 🍎 Für macOS (MacBook / iMac):
1. Lade auf [code.visualstudio.com](https://code.visualstudio.com) die Mac-Version (`.zip`) herunter.
2. Entpacke die Datei im Downloads-Ordner.
3. **⚠️ Wichtig:** Ziehe die Datei `Visual Studio Code.app` in deinen Ordner **Programme (Applications)**!
4. Starte VS Code aus dem Programme-Ordner.

### 🐧 Für Linux (Ubuntu / Debian):
```bash
sudo apt update && sudo apt install snapd
sudo snap install --classic code
```

---

## 🇩🇪 2. Sprache auf Deutsch umstellen (Optional)

1. Drücke `Strg + Shift + P` (Mac: `Cmd + Shift + P`).
2. Tippe: `Configure Display Language` und drücke `Enter`.
3. Wähle `Deutsch (German)` aus und starte VS Code neu.

---

## 📁 3. Das Projekt in VS Code öffnen

- In Thonny öffnet man meistens nur einzelne Dateien (`aufgabe.py`).
- In **VS Code öffnet man immer den gesamten Hauptordner**:
  1. Klicke oben auf **Datei &rarr; Ordner öffnen...** (Mac: `Cmd + O`).
  2. Wähle den Ordner `Aufgaben-Python` aus.
  3. Bestätige *"Vertrauen Sie den Autoren"* mit **Ja**.

Jetzt siehst du links im Explorer alle Kapitel und Dateien!

---

## 🧩 4. Die besten Erweiterungen (Extensions)

Drücke `Strg + Shift + X` (Mac: `Cmd + Shift + X`), um den Extension-Store zu öffnen:

1. **Python & Pylance (von Microsoft):** IntelliSense, Syntaxprüfung & Ausführen.
2. **Error Lens (⭐ Must-Have!):** Zeigt Fehler direkt farbig in der Zeile an.
3. **Material Icon Theme:** Bunte Datei-Symbole.
4. **Better Comments:** Farbige Kommentare (`# TODO`, `# !`).
5. **Black Formatter:** Automatisches Formatieren beim Speichern (`Strg + S`).

---

## ⌨️ 5. Die wichtigsten Shortcuts

| Aktion | Windows / Linux | macOS |
| :--- | :--- | :--- |
| **Datei speichern** | `Strg + S` | `Cmd + S` |
| **Terminal öffnen / schließen** | `Strg + \`` (oder `Strg + J`) | `Cmd + \`` (oder `Cmd + J`) |
| **Command Palette (Befehle suchen)** | `Strg + Shift + P` | `Cmd + Shift + P` |
| **Code automatisch formatieren** | `Alt + Shift + F` | `Option + Shift + F` |
| **Nächstes gleiches Wort markieren** | `Strg + D` | `Cmd + D` |
| **Skript starten** | `Strg + F5` (oder Play-Button ▶️) | `Cmd + F5` |

---

## 🧪 6. Ausprobieren in `vscode_test.py`

Öffne `vscode_test.py` in VS Code und teste:
1. Wie **Error Lens** Fehler in Echtzeit anzeigt.
2. Wie **IntelliSense** Methoden vorschlägt, wenn du `tesla.` tippst.
3. Öffne das Terminal mit `Strg + \`` und führe `python3 04b_umstieg_vscode/vscode_test.py` aus!
