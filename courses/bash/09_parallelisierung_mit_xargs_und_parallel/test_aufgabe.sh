#!/usr/bin/env bash
# ==============================================================================
# Testsuite: Bash 09 - Parallelisierung mit xargs & parallel
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

echo "🧪 Starte Tests für Modul 09 (${TARGET_FILE})..."
echo "---------------------------------------------------------"

# TEST 1: parallel_xargs_process
TMP_INPUT=$(mktemp)
echo -e "server01\nserver02\nserver03" > "$TMP_INPUT"
output1=$(parallel_xargs_process "$TMP_INPUT" 3 || true)
rm -f "$TMP_INPUT"

if echo "$output1" | grep -q "PROCESSED: server01" && \
   echo "$output1" | grep -q "PROCESSED: server02" && \
   echo "$output1" | grep -q "PROCESSED: server03"; then
    echo "✓ Test 1/4: parallel_xargs_process erfolgreich bestanden."
    passed=$((passed + 1))
else
    echo "✗ Test 1/4 fehlgeschlagen: parallel_xargs_process liefert nicht erwartete Ausgaben. Output: $output1"
fi

# TEST 2: background_workers_wait
output2=$(background_workers_wait "alpha" "beta" "gamma" || true)
if echo "$output2" | grep -q "WORKER_START: alpha" && \
   echo "$output2" | grep -q "WORKER_DONE: gamma" && \
   echo "$output2" | grep -q "ALL_WORKERS_FINISHED"; then
    echo "✓ Test 2/4: background_workers_wait erfolgreich bestanden."
    passed=$((passed + 1))
else
    echo "✗ Test 2/4 fehlgeschlagen: background_workers_wait fehlerhaft. Output: $output2"
fi

# TEST 3: parallel_batch_calculator
TMP_NUMS=$(mktemp)
echo -e "5\n2\n8\n1" > "$TMP_NUMS"
output3=$(parallel_batch_calculator "$TMP_NUMS" 4 || true)
rm -f "$TMP_NUMS"

expected3="1^2 = 1
2^2 = 4
5^2 = 25
8^2 = 64"

if [ "$(echo "$output3" | tr -d '\r')" = "$expected3" ]; then
    echo "✓ Test 3/4: parallel_batch_calculator erfolgreich bestanden."
    passed=$((passed + 1))
else
    echo "✗ Test 3/4 fehlgeschlagen: Erwartete:
$expected3
Erhalten:
$output3"
fi

# TEST 4: throttle_concurrent_jobs
output4=$(throttle_concurrent_jobs 4 2 || true)
if echo "$output4" | grep -q "JOB_RUNNING: 1" && \
   echo "$output4" | grep -q "JOB_RUNNING: 4" && \
   echo "$output4" | grep -q "THROTTLE_POOL_COMPLETED"; then
    echo "✓ Test 4/4: throttle_concurrent_jobs erfolgreich bestanden."
    passed=$((passed + 1))
else
    echo "✗ Test 4/4 fehlgeschlagen: throttle_concurrent_jobs fehlerhaft. Output: $output4"
fi

echo "---------------------------------------------------------"
if [ "$passed" -eq "$total" ]; then
    echo "🎉 Alle $total Tests für Modul 09 erfolgreich bestanden!"
    exit 0
else
    echo "❌ $passed von $total Tests bestanden."
    exit 1
fi
