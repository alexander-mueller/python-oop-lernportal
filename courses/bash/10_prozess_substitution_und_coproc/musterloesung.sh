#!/usr/bin/env bash
# ==============================================================================
# Bash 10: Prozess-Substitution, Named Pipes & Co-Prozesse (coproc)
# MUSTERLÖSUNG
# ==============================================================================

compare_command_outputs() {
    local cmd1="${1:-}"
    local cmd2="${2:-}"

    if [ -z "$cmd1" ] || [ -z "$cmd2" ]; then
        return 1
    fi

    # Vergleiche Ausgaben via Prozess-Substitution
    if diff_output=$(diff -u <(bash -c "$cmd1") <(bash -c "$cmd2")); then
        echo "IDENTICAL"
        return 0
    else
        echo "$diff_output"
        return 1
    fi
}

stream_splitter_tee() {
    local input_text="${1:-}"
    local raw_file="${2:-}"
    local upper_file="${3:-}"

    if [ -z "$input_text" ] || [ -z "$raw_file" ] || [ -z "$upper_file" ]; then
        return 1
    fi

    # Stream-Verzweigung mit tee und Prozess-Substitution
    echo "$input_text" | tee "$raw_file" >(tr '[:lower:]' '[:upper:]' > "$upper_file") > /dev/null
    
    # Kurze Synchronisation für den asynchronen Sub-Stream
    sleep 0.05
    return 0
}

named_pipe_transfer() {
    local fifo_path="${1:-}"
    local message="${2:-}"

    if [ -z "$fifo_path" ] || [ -z "$message" ]; then
        return 1
    fi

    rm -f "$fifo_path"
    mkfifo "$fifo_path"

    # Im Hintergrund in die Pipe schreiben
    (
        echo "$message" > "$fifo_path"
    ) &

    # Synchron aus der Pipe lesen
    local received
    read -r received < "$fifo_path"

    # Aufräumen
    rm -f "$fifo_path"

    echo "RECEIVED_FIFO: $received"
    return 0
}

coproc_calculator_interactive() {
    local expr1="${1:-}"
    local expr2="${2:-}"

    if [ -z "$expr1" ] || [ -z "$expr2" ]; then
        return 1
    fi

    # Co-Prozess starten
    coproc CALC {
        while read -r expr; do
            if [ "$expr" = "EXIT" ]; then
                break
            fi
            echo "$((expr))"
        done
    }

    # Interaktiver Datenaustausch
    echo "$expr1" >&"${CALC[1]}"
    local res1
    read -r res1 <&"${CALC[0]}"

    echo "$expr2" >&"${CALC[1]}"
    local res2
    read -r res2 <&"${CALC[0]}"

    # Co-Prozess beenden
    echo "EXIT" >&"${CALC[1]}"
    wait "$CALC_PID" 2>/dev/null || true

    echo "CALC_RES1: $res1"
    echo "CALC_RES2: $res2"
    return 0
}
