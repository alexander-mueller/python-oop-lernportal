# Bash 03: Variablen, Environment, Expansion & Arithmetik ⚡

Willkommen zu **Modul 03** des Linux Bash & DevOps Lehrpfads!

In diesem Modul meisterst du lokale vs. globale Umgebungsvariablen (`export`, `$PATH`), Subshells vs. Current-Shell, moderne Command Substitution (`$(...)`), mächtige native String-Manipulationen per Parameter Expansion und Ganzzahl-Arithmetik (`$(( ... ))`).

---

## 💡 1. Das Wichtigste in Kürze

### Lokale Variablen vs. `export`
- Lokale Variablen (`NAME="Wert"`) existieren nur in der aktuellen Shell-Instanz.
- Mit `export NAME="Wert"` wird die Variable an alle Kind-Prozesse (Subshells, Skripte, CLI-Programme) vererbt.
- `$PATH` ist die durch Doppelpunkte getrennte Liste von Verzeichnissen, in denen die Shell nach ausführbaren Programmen sucht (`export PATH="/opt/bin:$PATH"`).

### Command Substitution `$(...)`
Führt ein Shell-Kommando aus und ersetzt den Ausdruck durch dessen `stdout`:
```bash
AKTUELLER_USER=$(whoami)
HEUTIGES_DATUM=$(date +%Y-%m-%d)
BACKUP_NAME="backup_${AKTUELLER_USER}_${HEUTIGES_DATUM}.tar.gz"
```

### Native Parameter Expansion (Kein `sed`/`awk` nötig!)
Bash kann Strings intern extrem schnell und speicherschonend manipulieren:
- **Default-Wert**: `${VAR:-"standardwert"}` (nutzt Fallback, falls `$VAR` nicht gesetzt/leer)
- **Präfix entfernen**: `${PFAD#*/}` (kürzester Treffer) bzw. `${PFAD##*/}` (längster Treffer -> Dateiname)
- **Suffix entfernen**: `${PFAD%/*}` (Verzeichnis) bzw. `${DATEI%.*}` (Dateiname ohne Endung)
- **String-Länge**: `${#VAR}`

### Shell-Arithmetik `$(( ... ))`
Für Ganzzahl-Berechnungen in nativer C-Geschwindigkeit:
```bash
SUMME=$(( 10 + 25 ))
PROZENT=$(( (USED * 100) / TOTAL ))
REST=$(( 17 % 5 ))  # Modulo = 2
```

---

## 🎯 Aufgaben in `aufgabe.sh`

1. **TODO 1 (`setze_umgebungsvariable`)**: Exportiere eine Umgebungsvariable dynamisch und gib sie als `NAME=WERT` zurück.
2. **TODO 2 (`generiere_system_kennung`)**: Baue per `$(...)` eine Kennung im Format `user@host_YYYY-MM`.
3. **TODO 3 (`zerlege_dateipfad`)**: Extrahiere DIR, FILE, EXT und BASE ausschließlich mit nativer Bash Parameter Expansion (`${var#...}`, `${var%...}`).
4. **TODO 4 (`ermittle_konfigurationswert`)**: Gib den übergebenen Wert oder den Fallback mit `${var:-fallback}` zurück.
5. **TODO 5 (`berechne_disk_quota`)**: Berechne freien Speicher und prozentuale Belegung mit `$(( ... ))`.

---

## 🧪 Tests ausführen

```bash
bash test_aufgabe.sh
```
