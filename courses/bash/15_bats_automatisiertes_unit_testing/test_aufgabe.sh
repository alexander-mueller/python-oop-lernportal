#!/usr/bin/env bash
# ==============================================================================
# Testsuite: Bash 15 - BATS Testing & Mocking
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

echo "🧪 Starte Tests für Modul 15 (${TARGET_FILE})..."
echo "---------------------------------------------------------"

# TEST 1: generate_bats_test_file
out1=$(generate_bats_test_file "Verify HTTP 200" "curl -s http://api" 0 "200" || true)
if echo "$out1" | grep -q '@test "Verify HTTP 200"' && \
   echo "$out1" | grep -q 'run curl -s http://api' && \
   echo "$out1" | grep -q '\[ "$status" -eq 0 \]'; then
    echo "✓ Test 1/4: generate_bats_test_file erfolgreich bestanden."
    passed=$((passed + 1))
else
    echo "✗ Test 1/4 fehlgeschlagen: BATS Datei unvollständig. Output:
$out1"
fi

# TEST 2: create_executable_mock
MOCK_DIR=$(mktemp -d)
create_executable_mock "$MOCK_DIR" "systemctl" 0 "active (running)"
mock_file="${MOCK_DIR}/systemctl"

if [ -x "$mock_file" ] && [ "$("$mock_file")" = "active (running)" ]; then
    echo "✓ Test 2/4: create_executable_mock erfolgreich bestanden."
    passed=$((passed + 1))
else
    echo "✗ Test 2/4 fehlgeschlagen: Mock-Binary nicht ausführbar oder falsche Ausgabe."
fi

# TEST 3: parse_tap_test_summary
tap_sample="1..4
ok 1 Test initial migration
ok 2 Test database connection
not ok 3 Test payment webhook
ok 4 Test session logout"

out3=$(parse_tap_test_summary "$tap_sample" || true)
if [ "$out3" = "TOTAL: 4 | PASSED: 3 | FAILED: 1" ]; then
    echo "✓ Test 3/4: parse_tap_test_summary erfolgreich bestanden."
    passed=$((passed + 1))
else
    echo "✗ Test 3/4 fehlgeschlagen: Erwartete 'TOTAL: 4 | PASSED: 3 | FAILED: 1', Erhalten: '$out3'"
fi

# TEST 4: run_sandboxed_test_runner
out4=$(run_sandboxed_test_runner "systemctl is-active app" "$MOCK_DIR" || true)
rm -rf "$MOCK_DIR"

if [ "$out4" = "STATUS: 0 | OUTPUT: active (running)" ]; then
    echo "✓ Test 4/4: run_sandboxed_test_runner erfolgreich bestanden."
    passed=$((passed + 1))
else
    echo "✗ Test 4/4 fehlgeschlagen: Erwartete 'STATUS: 0 | OUTPUT: active (running)', Erhalten: '$out4'"
fi

echo "---------------------------------------------------------"
if [ "$passed" -eq "$total" ]; then
    echo "🎉 Alle $total Tests für Modul 15 erfolgreich bestanden!"
    exit 0
else
    echo "❌ $passed von $total Tests bestanden."
    exit 1
fi
