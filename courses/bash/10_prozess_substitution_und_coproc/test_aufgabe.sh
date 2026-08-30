#!/usr/bin/env bash
# ==============================================================================
# Testsuite: Bash 10 - Prozess-Substitution & Co-Prozesse
# ==============================================================================
set -e

TARGET_FILE="${1:-aufgabe.sh}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_PATH="${SCRIPT_DIR}/${TARGET_FILE}"

if [ ! -f "$TARGET_PATH" ]; then
    echo "❌ Fehler: Zieldatei '$TARGET_PATH' nicht gefunden!"
    exit 1
fi

source "$TARGET_PATH"

passed=0
total=4

echo "🧪 Starte Tests für Modul 10 (${TARGET_FILE})..."
echo "---------------------------------------------------------"

# TEST 1: compare_command_outputs
out1_same=$(compare_command_outputs "echo 'hello world'" "printf '%s\n' 'hello world'" || true)
if [ "$out1_same" = "IDENTICAL" ]; then
    echo "✓ Test 1/4: compare_command_outputs erfolgreich bestanden."
    passed=$((passed + 1))
else
    echo "✗ Test 1/4 fehlgeschlagen: Erwartete 'IDENTICAL', erhalten: $out1_same"
fi

# TEST 2: stream_splitter_tee
TMP_RAW=$(mktemp)
TMP_UPPER=$(mktemp)
stream_splitter_tee "nginx error 502" "$TMP_RAW" "$TMP_UPPER"
sleep 0.1

raw_content=$(cat "$TMP_RAW")
upper_content=$(cat "$TMP_UPPER")
rm -f "$TMP_RAW" "$TMP_UPPER"

if [ "$raw_content" = "nginx error 502" ] && [ "$upper_content" = "NGINX ERROR 502" ]; then
    echo "✓ Test 2/4: stream_splitter_tee erfolgreich bestanden."
    passed=$((passed + 1))
else
    echo "✗ Test 2/4 fehlgeschlagen: raw='$raw_content', upper='$upper_content'"
fi

# TEST 3: named_pipe_transfer
TMP_FIFO="/tmp/test_pipe_$(date +%s)_$$"
out3=$(named_pipe_transfer "$TMP_FIFO" "DEPLOY_PAYLOAD_889" || true)

if [ "$out3" = "RECEIVED_FIFO: DEPLOY_PAYLOAD_889" ] && [ ! -e "$TMP_FIFO" ]; then
    echo "✓ Test 3/4: named_pipe_transfer erfolgreich bestanden."
    passed=$((passed + 1))
else
    echo "✗ Test 3/4 fehlgeschlagen: Output: $out3 (FIFO gelöscht: $([ ! -e "$TMP_FIFO" ] && echo ja || echo nein))"
fi

# TEST 4: coproc_calculator_interactive
out4=$(coproc_calculator_interactive "15 + 35" "12 * 12" || true)
expected4="CALC_RES1: 50
CALC_RES2: 144"

if [ "$(echo "$out4" | tr -d '\r')" = "$expected4" ]; then
    echo "✓ Test 4/4: coproc_calculator_interactive erfolgreich bestanden."
    passed=$((passed + 1))
else
    echo "✗ Test 4/4 fehlgeschlagen: Erwartete:
$expected4
Erhalten:
$out4"
fi

echo "---------------------------------------------------------"
if [ "$passed" -eq "$total" ]; then
    echo "🎉 Alle $total Tests für Modul 10 erfolgreich bestanden!"
    exit 0
else
    echo "❌ $passed von $total Tests bestanden."
    exit 1
fi
