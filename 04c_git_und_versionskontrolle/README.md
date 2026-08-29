# Kapitel 04c: Git & Versionskontrolle: Deine Programmier-Zeitmaschine 🌿⏱️

Herzlich willkommen zum Git-Guide!

**Git** ist das weltweit am meisten genutzte Versionskontrollsystem. Es ermöglicht dir, deinen Code in sauberen Spielständen (Commits) zu speichern, jederzeit alte Versionen wiederherzustellen und im Team zu arbeiten.

---

## 🎮 Der Lebenszyklus eines Codes in Git

1. **Arbeitsverzeichnis (Working Tree):** Deine Dateien, die du in VS Code bearbeitest.
2. **Staging Area (`git add .`):** Die Bereitstellung. Du wählst aus, welche geänderten Dateien in den nächsten Speicherpunkt gehören.
3. **Commit (`git commit -m "Nachricht"`):** Der fertige Speicherpunkt mit Zeitstempel und Erklärung.
4. **Push (`git push`):** Hochladen deiner Commits auf den entfernten Server (z.B. dein Aufgaben-Repository).

---

## 🖥️ Git in VS Code nutzen

1. Drücke `Strg + Shift + G` (Mac: `Cmd + Shift + G`), um links das Git-Panel zu öffnen.
2. Klicke auf eine veränderte Datei &rarr; Du siehst sofort den **Diff** (Rot = alter Code, Grün = neuer Code).
3. Klicke auf `+` neben der Datei (Staging).
4. Tippe eine Commit-Nachricht ins Textfeld und klicke auf das Häkchen **&check; Commit**.
5. Klicke auf **Sync Changes / Push**, um alles auf den Server zu laden!

---

## ⌨️ Die wichtigsten Terminal-Befehle

| Befehl | Erklärung |
| :--- | :--- |
| `git status` | Zeigt geänderte und neue Dateien an |
| `git add .` | Packt alle aktuellen Änderungen in die Staging Area |
| `git commit -m "Text"` | Erstellt einen Commit mit einer Beschreibung |
| `git push` | Lädt neue Commits auf den Server hoch |
| `git log --oneline` | Zeigt die bisherige Versions-Historie an |

---

## 🧪 Mitmach-Übung in `git_uebung.py`

1. Öffne `git_uebung.py`, ändere den Text und speichere.
2. Öffne den Git-Tab in VS Code (`Strg + Shift + G`).
3. Betrachte die Änderung und erstelle einen Commit mit der Nachricht: *"Mein erster eigener Git-Commit"*.
4. Überprüfe die Historie mit `git log --oneline -n 3`.
