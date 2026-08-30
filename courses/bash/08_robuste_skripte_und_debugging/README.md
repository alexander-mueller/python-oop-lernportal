# Bash 08: Robuste Skripte, Strict Mode & Debugging 🛡️

Willkommen zu **Modul 08** (Abschluss von Lehrpfad 2) des Linux Bash & DevOps Lehrpfads!

In diesem Modul lernst du, wie professionelle DevOps-Engineers ausfallsichere, unzerstörbare Shell-Skripte für Produktivumgebungen schreiben: Der **Bash Strict Mode (`set -euo pipefail`)**, Signal-Traps (`trap ... EXIT`), Concurrency-Locks mit `flock`, strukturiertes Logging und Tracing mit `set -x`.

---

## 💡 1. Das Wichtigste in Kürze

### Der unschlagbare Bash Strict Mode
Standardmäßig ignoriert Bash Fehler und macht einfach weiter – was in Produktionsskripten verheerend sein kann. Der Strict Mode stoppt sofort:
```bash
#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'
```
- **`set -e`** (errexit): Bricht das Skript sofort ab, wenn ein Befehl fehlschlägt (`Exit != 0`).
- **`set -u`** (nounset): Behandelt ungesetzte Variablen als schweren Fehler (schützt vor Katastrophen wie `rm -rf /tmp/$SUBDIR/` wenn `$SUBDIR` leer ist!).
- **`set -o pipefail`**: Die Pipeline schlägt fehl, wenn *irgendein* Teil fehlschlägt (nicht nur der letzte).

### Cleanup mit `trap` & `mktemp`
Egal ob ein Skript erfolgreich endet, crasht oder mit STRG+C abgebrochen wird – der `EXIT`-Trap räumt immer zuverlässig auf:
```bash
TEMP_DIR=$(mktemp -d)
trap 'rm -rf "$TEMP_DIR"' EXIT
```

### Exklusive Locks mit `flock`
Verhindert, dass ein Cronjob oder Worker mehrfach parallel startet:
```bash
flock -n /var/lock/backup.lock -c "/opt/scripts/do_backup.sh" || {
  echo "Backup läuft bereits!" >&2
  exit 1
}
```

---

## 🎯 Aufgaben in `aufgabe.sh`

1. **TODO 1 (`aktiviere_strict_mode`)**: Konfiguriere `set -euo pipefail`.
2. **TODO 2 (`devops_logger`)**: Formatiere Logzeilen mit Timestamp und trenne Fehlerkanäle (ERROR/FATAL auf stderr, INFO auf stdout).
3. **TODO 3 (`erstelle_temp_verzeichnis_mit_cleanup`)**: Erstelle mit `mktemp -d` ein Verzeichnis und sichere es mit `trap 'rm -rf ...' EXIT`.
4. **TODO 4 (`fuehre_exklusiv_mit_lock_aus`)**: Schütze Befehlsausführungen mit `flock -n`.
5. **TODO 5 (`debug_trace_ausfuehren`)**: Aktiviere temporär `set -x` für Tracing und stelle den Zustand mit `set +x` wieder her.

---

## 🧪 Tests ausführen

```bash
bash test_aufgabe.sh
```
