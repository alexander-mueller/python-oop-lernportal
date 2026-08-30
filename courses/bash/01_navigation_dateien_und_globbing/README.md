# Bash 01: Terminal-Navigation, Dateioperationen & Globbing 🐧

Willkommen zu **Modul 01** des Linux Bash & DevOps Lehrpfads!

In diesem Modul lernst du die fundamentale Navigation im Unix-Dateisystem, das effiziente Erstellen und Verwalten von Verzeichnisbäumen sowie mächtiges Shell-Globbing (`*`, `?`, `{a,b}`) kennen.

---

## 💡 1. Das Wichtigste in Kürze

### Pfad-Navigation & Orientierung
- `pwd`: Gibt das aktuelle Arbeitsverzeichnis (Print Working Directory) aus.
- `cd /absoluter/pfad`: Wechselt zu einem absoluten Pfad ausgehend vom Root `/`.
- `cd relativ/zum/ort`: Wechselt relativ zum aktuellen Ordner (`.` = aktuell, `..` = übergeordnet, `~` = Home-Verzeichnis, `-` = vorheriges Verzeichnis).
- `ls -la`: Zeigt alle Dateien inkl. versteckter (`.`) mit Berechtigungen, Owner und Dateigröße an.

### Verzeichnisse & Dateien verwalten
- `mkdir -p ordner/sub1/sub2`: Erstellt ganze Verzeichnispfade auf einmal ohne Fehler, falls sie schon existieren.
- `touch datei.txt`: Erstellt eine leere Datei oder aktualisiert den Zeitstempel.
- `cp -r quelle/ ziel/`: Kopiert Dateien und Ordner rekursiv.
- `mv quelle ziel`: Verschiebt oder benennt Dateien/Ordner um.
- `rm -rf ordner/`: Löscht Dateien und Verzeichnisse rekursiv und ohne Nachfrage (**Vorsicht!**).

### Shell-Globbing & Brace Expansion
- `*`: Entspricht beliebig vielen Zeichen (z.B. `*.log` für alle Logdateien).
- `?`: Entspricht genau einem beliebigen Zeichen (z.B. `data?.txt` matcht `data1.txt`, nicht `data10.txt`).
- `[abc]` / `[0-9]`: Matcht ein Zeichen aus der angegebenen Zeichenklasse.
- `{a,b,c}`: **Brace Expansion** generiert Kombinationen (z.B. `touch file_{1..3}.txt` erzeugt `file_1.txt`, `file_2.txt`, `file_3.txt`).

```bash
# Praxisbeispiel: Schnelle Projekt-Initialisierung
mkdir -p project/{src,tests,docs,config}
touch project/src/{app,utils}.js project/config/{dev,prod}.yaml
```

---

## 🎯 Aufgaben in `aufgabe.sh`

1. **TODO 1 (`erstelle_projektstruktur`)**: Lege mit `mkdir -p` die Ordner `src/components`, `src/utils`, `docs/api` und `backup/logs` an.
2. **TODO 2 (`erstelle_testdateien`)**: Erstelle die geforderten Komponenten-, Doku- und Konfigurationsdateien mit `touch`.
3. **TODO 3 (`kopiere_konfigurationen`)**: Kopiere alle `*.yaml` und `*.log` Dateien mit Shell-Globbing in den Backup-Ordner.
4. **TODO 4 (`verschiebe_dateien`)**: Verschiebe alle Markdown-Dokumente (`*.md`) in das Zielverzeichnis.
5. **TODO 5 (`bereinige_temporaere_dateien`)**: Bereinige alte Logdateien und lösche den temporären Logs-Backup-Ordner mit `rm -rf`.

---

## 🧪 Tests ausführen

Führe im Terminal folgenden Befehl aus:
```bash
bash test_aufgabe.sh
```
