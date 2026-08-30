# Bash 15: BATS Automatisiertes Unit-Testing & Mocking 🧪

Willkommen zu **Modul 15**! Auch Bash-Skripte verdienen echte automatisierte Unittests. Mit dem **BATS-Framework (Bash Automated Testing System)** schreibst du wartbare, isolierte und reproduzierbare Tests für deine DevOps-Pipelines.

---

## 💡 1. Das Wichtigste in Kürze

### 1.1 Was ist BATS?
BATS ist ein standardisiertes Test-Framework für Bash, das auf dem TAP-Standard (Test Anything Protocol) basiert:
```bash
#!/usr/bin/env bats

setup() {
    # Wird VOR jedem Testfall ausgeführt
    export TEST_TMP="/tmp/test_dir_$$"
    mkdir -p "$TEST_TMP"
}

teardown() {
    # Wird NACH jedem Testfall ausgeführt
    rm -rf "$TEST_TMP"
}

@test "Prüfe ob Backup-Skript mit Exit-Code 0 beendet" {
    run /opt/backup.sh "$TEST_TMP"
    [ "$status" -eq 0 ]
    [ "${lines[0]}" = "Backup erfolgreich" ]
}

@test "Fehler bei ungültigen Parametern" {
    run /opt/backup.sh
    [ "$status" -ne 0 ]
}
```

### 1.2 Die BATS Spezial-Variablen
- `run <befehl>`: Führt den Befehl aus und unterdrückt unkontrolliertes Abbrechen.
- `$status`: Der Exit-Code des ausgeführten Befehls.
- `$output`: Der gesamte Output (stdout & stderr kombiniert).
- `${lines[0]}`, `${lines[1]}`: Array aller Ausgabezeilen.

### 1.3 Mocking in Shell-Skripten
Da Skripte oft externe Befehle wie `curl`, `docker` oder `systemctl` aufrufen, fangen wir diese in Tests über ein temporäres Verzeichnis in `$PATH` ab:
```bash
# 🎯 Mock-Binary erstellen:
mkdir -p /tmp/mocks
cat <<'EOF' > /tmp/mocks/docker
#!/usr/bin/env bash
echo "healthy"
exit 0
EOF
chmod +x /tmp/mocks/docker

# 🎯 Skript mit Mock-PATH testen:
PATH="/tmp/mocks:$PATH" ./mein_skript.sh
```

---

## 🎯 Aufgaben in `aufgabe.sh`

1. **`generate_bats_test_file(test_name, target_cmd, expected_exit, expected_text)`**:
   Erzeugt dynamisch eine standardkonforme `.bats` Testdatei.
2. **`create_executable_mock(mock_dir, cmd_name, exit_code, output_text)`**:
   Erstellt ein ausführbares Mock-Skript mit gewünschtem Exit-Code und Output.
3. **`parse_tap_test_summary(tap_stream)`**:
   Parst TAP-13 Protokoll-Zeilen (`ok`, `not ok`) und gibt Gesamtzahlen aus.
4. **`run_sandboxed_test_runner(test_cmd, mock_dir)`**:
   Führt Tests in einer isolierten Subshell mit Mock-PATH aus und liefert Status & Output.

---

## 🧪 Tests ausführen

```bash
# Eigene Lösung testen:
bash test_aufgabe.sh

# Musterlösung testen:
bash test_aufgabe.sh musterloesung.sh
```
