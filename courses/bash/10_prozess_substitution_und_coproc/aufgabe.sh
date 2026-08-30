#!/usr/bin/env bash
# ==============================================================================
# Bash 10: Prozess-Substitution, Named Pipes & Co-Prozesse (coproc)
# ==============================================================================
# In diesem Modul lernst du fortschrittliche Linux IPC-Mechanismen:
# Process Substitution <(...), Stream-Fächerung >(...), Named Pipes (mkfifo)
# und interaktive Co-Prozesse (coproc).
# ==============================================================================

# ------------------------------------------------------------------------------
# TODO 1: Befehlsausgaben ohne temporäre Dateien vergleichen (<(...))
# ------------------------------------------------------------------------------
# Implementiere die Funktion `compare_command_outputs`.
# Parameter:
#   $1: Erster Bash-Befehl als String (z.B. "sort liste1.txt")
#   $2: Zweiter Bash-Befehl als String (z.B. "sort liste2.txt")
# Verhalten:
#   - Vergleicht die Ausgaben beider Befehle direkt mit `diff -u` und Prozess-Substitution:
#     diff -u <(bash -c "$1") <(bash -c "$2")
#   - Wenn beide Ausgaben identisch sind: Gib "IDENTICAL" aus und return 0.
#   - Wenn Unterschiede existieren: Gib den Diff aus und return 1.
# ------------------------------------------------------------------------------
compare_command_outputs() {
    local cmd1="${1:-}"
    local cmd2="${2:-}"

    # TODO: Prüfe Parameter
    # TODO: Führe diff -u mit <(bash -c "$cmd1") und <(bash -c "$cmd2") aus
    echo "TODO: Implementiere compare_command_outputs"
    return 1
}

# ------------------------------------------------------------------------------
# TODO 2: Stream-Verzweigung mit tee & >(...)
# ------------------------------------------------------------------------------
# Implementiere die Funktion `stream_splitter_tee`.
# Parameter:
#   $1: Eingabetext (z.B. "Fehler: Connection Timeout auf DB-Server")
#   $2: Pfad zur Roh-Logdatei (z.B. "/tmp/raw.log")
#   $3: Pfad zur transformierten Datei (z.B. "/tmp/uppercase.log")
# Verhalten:
#   - Schreibt den Eingabetext unverändert in $2.
#   - Leitet den Text gleichzeitig über Prozess-Substitution `>(tr '[:lower:]' '[:upper:]' > "$3")`
#     in Großbuchstaben nach $3 um (mit `tee`).
#   - Wartet kurz/synchronisiert, sodass beide Dateien vollständig geschrieben sind.
#   - Return 0 bei Erfolg.
# ------------------------------------------------------------------------------
stream_splitter_tee() {
    local input_text="${1:-}"
    local raw_file="${2:-}"
    local upper_file="${3:-}"

    # TODO: Validiere Parameter
    # TODO: Nutze echo "$input_text" | tee "$raw_file" >(tr '[:lower:]' '[:upper:]' > "$upper_file") > /dev/null
    echo "TODO: Implementiere stream_splitter_tee"
    return 1
}

# ------------------------------------------------------------------------------
# TODO 3: Interprozesskommunikation über Named Pipe (FIFO)
# ------------------------------------------------------------------------------
# Implementiere die Funktion `named_pipe_transfer`.
# Parameter:
#   $1: Pfad zur Named Pipe (z.B. "/tmp/test_fifo")
#   $2: Zu übertragende Nachricht (z.B. "DEPLOYMENT_TRIGGER_V2")
# Verhalten:
#   - Erstellt eine Named Pipe mit `mkfifo "$1"`. Falls die Pipe existiert, vorher löschen.
#   - Schreibt im Hintergrund (`&`) die Nachricht $2 in die Pipe.
#   - Liest im Hauptprozess die Nachricht aus der Pipe in eine Variable `received`.
#   - Löscht die Pipe nach erfolgreichem Lesen (`rm -f "$1"`).
#   - Gibt aus: "RECEIVED_FIFO: $received"
#   - Return 0.
# ------------------------------------------------------------------------------
named_pipe_transfer() {
    local fifo_path="${1:-}"
    local message="${2:-}"

    # TODO: Erstelle FIFO mit mkfifo
    # TODO: Schreibe im Hintergrund ($message > $fifo_path &)
    # TODO: Lies synchron (read -r received < $fifo_path)
    # TODO: Bereinige FIFO und gib "RECEIVED_FIFO: $received" aus
    echo "TODO: Implementiere named_pipe_transfer"
    return 1
}

# ------------------------------------------------------------------------------
# TODO 4: Interaktiver Co-Prozess (coproc)
# ------------------------------------------------------------------------------
# Implementiere die Funktion `coproc_calculator_interactive`.
# Parameter:
#   $1: Erster mathematischer Ausdruck (z.B. "10 + 25")
#   $2: Zweiter mathematischer Ausdruck (z.B. "100 * 4")
# Verhalten:
#   - Startet einen Co-Prozess namens CALC mit Bash:
#     coproc CALC {
#         while read -r expr; do
#             [ "$expr" = "EXIT" ] && break
#             echo "$((expr))"
#         done
#     }
#   - Sendet $1 an den Co-Prozess (`${CALC[1]}`), liest das Ergebnis aus (`${CALC[0]}`).
#   - Sendet $2 an den Co-Prozess, liest das zweite Ergebnis aus.
#   - Sendet "EXIT" an den Co-Prozess zum sauberen Beenden.
#   - Gibt die Ergebnisse aus:
#       CALC_RES1: <ergebnis1>
#       CALC_RES2: <ergebnis2>
#   - Return 0.
# ------------------------------------------------------------------------------
coproc_calculator_interactive() {
    local expr1="${1:-}"
    local expr2="${2:-}"

    # TODO: Starte coproc CALC
    # TODO: Sende expr1, lies res1
    # TODO: Sende expr2, lies res2
    # TODO: Sende EXIT
    # TODO: Gib formatiertes Ergebnis aus
    echo "TODO: Implementiere coproc_calculator_interactive"
    return 1
}
