# Bash 05: Kontrollfluss, Test-Operatoren & Regex ⚡

Willkommen zu **Modul 05** (Lehrpfad 2) des Linux Bash & DevOps Lehrpfads!

In diesem Modul lernst du moderne Entscheidungslogik mit doppelten eckigen Klammern (`[[ ... ]]`), Dateitests (`-f`, `-d`, `-x`), String-Prüfungen (`-z`, `-n`), reguläre Ausdrücke mit `=~`, numerische Vergleiche und `case`-Verzweigungen kennen.

---

## 💡 1. Das Wichtigste in Kürze

### Die moderne Bash-Test-Syntax `[[ ... ]]`
Verwende in Bash-Skripten immer `[[ ... ]]` statt des veralteten POSIX `[ ... ]`. Es verhindert fehlerhaftes Word-Splitting und unterstützt logische Operatoren (`&&`, `||`) sowie Regex `=~`.

### Wichtige Test-Operatoren
- **Dateisystem**:
  - `-e "$path"`: Pfad existiert
  - `-f "$path"`: Reguläre Datei
  - `-d "$path"`: Verzeichnis
  - `-x "$path"`: Datei ist ausführbar (Executable)
  - `-s "$path"`: Datei existiert und ist nicht leer (Größe > 0)
- **Strings**:
  - `-z "$str"`: String ist leer (`length == 0`)
  - `-n "$str"`: String ist nicht leer
  - `"$a" == "$b"` / `"$a" != "$b"`: Gleichheit/Ungleichheit
- **Numerisch**:
  - `-eq`, `-ne`, `-lt`, `-le`, `-gt`, `-ge` oder Arithmetik `(( a >= 90 ))`

### Regex-Matching mit `=~` & `BASH_REMATCH`
```bash
EMAIL="devops@company.com"
if [[ $EMAIL =~ ^([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$ ]]; then
  echo "Valide E-Mail!"
  echo "Benutzername: ${BASH_REMATCH[1]}"
  echo "Domain: ${BASH_REMATCH[2]}"
fi
```

### Exit-Codes & `case`
Jeder Linux-Befehl gibt beim Beenden einen Statuscode von `0` (Erfolg) bis `255` (Fehler) zurück (`$?`).
```bash
case "$ACTION" in
  start|boot)
    echo "Starting..." ;;
  stop)
    echo "Stopping..." ;;
  *)
    echo "Unknown" ;;
esac
```

---

## 🎯 Aufgaben in `aufgabe.sh`

1. **TODO 1 (`analysiere_pfad_status`)**: Prüfe Dateipfade auf DIRECTORY, EXECUTABLE_FILE, REGULAR_FILE oder NOT_FOUND.
2. **TODO 2 (`validiere_ipv4_format`)**: Validiere eine IPv4-Adresse mit Regex `=~` und `BASH_REMATCH`.
3. **TODO 3 (`bewerte_server_metrik`)**: Bewerte Server-Auslastungen (CRITICAL, WARNING, OK).
4. **TODO 4 (`service_dispatcher`)**: Verarbeite Start/Stop/Restart-Aktionen mit `case ... in ... esac`.
5. **TODO 5 (`fuehre_sicher_aus`)**: Fange den Exit-Code `$?` ab und melde SUCCESS oder den Fehlercode.

---

## 🧪 Tests ausführen

```bash
bash test_aufgabe.sh
```
