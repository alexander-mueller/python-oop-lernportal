#!/usr/bin/env bash
# ==============================================================================
# Testsuite: Master 16 - DevOps Multi-Server Automation Suite
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
total=5

echo "🧪 Starte Tests für Master-Modul 16 (${TARGET_FILE})..."
echo "---------------------------------------------------------"

# TEST 1: parse_devops_cli_args
out1=$(parse_devops_cli_args --config /etc/nodes.conf -p 8 --dry-run || true)
expected1="CONFIG: /etc/nodes.conf | WORKERS: 8 | DRY_RUN: true"

if [ "$out1" = "$expected1" ]; then
    echo "✓ Test 1/5: parse_devops_cli_args erfolgreich bestanden."
    passed=$((passed + 1))
else
    echo "✗ Test 1/5 fehlgeschlagen: Erwartete '$expected1', Erhalten: '$out1'"
fi

# TEST 2: parallel_server_health_check
TMP_SERVERS=$(mktemp)
echo -e "prod-web01\nprod-db01-offline\nprod-redis" > "$TMP_SERVERS"
out2=$(parallel_server_health_check "$TMP_SERVERS" 3 || true)
rm -f "$TMP_SERVERS"

if echo "$out2" | grep -q "\[HEALTH\] prod-web01 -> ONLINE" && \
   echo "$out2" | grep -q "\[HEALTH\] prod-db01-offline -> OFFLINE" && \
   echo "$out2" | grep -q "\[HEALTH_SUMMARY\] ALL_CHECKS_COMPLETED"; then
    echo "✓ Test 2/5: parallel_server_health_check erfolgreich bestanden."
    passed=$((passed + 1))
else
    echo "✗ Test 2/5 fehlgeschlagen: Health-Check Output inkorrekt. Output:
$out2"
fi

# TEST 3: analyze_server_logs_parallel
TMP_DIR=$(mktemp -d)
echo -e "2026-08-30 INFO ok\n2026-08-30 ERROR db connection failed\n2026-08-30 ERROR timeout" > "${TMP_DIR}/srv1.log"
echo -e "2026-08-30 INFO ok\n2026-08-30 FATAL out of memory" > "${TMP_DIR}/srv2.log"
echo -e "2026-08-30 INFO all good" > "${TMP_DIR}/srv3.log"

out3=$(analyze_server_logs_parallel "$TMP_DIR" "ERROR|FATAL" 4 || true)
rm -rf "$TMP_DIR"

if [ "$out3" = "INCIDENTS_FOUND: 3 | LOGS_SCANNED: 3" ]; then
    echo "✓ Test 3/5: analyze_server_logs_parallel erfolgreich bestanden."
    passed=$((passed + 1))
else
    echo "✗ Test 3/5 fehlgeschlagen: Erwartete 'INCIDENTS_FOUND: 3 | LOGS_SCANNED: 3', Erhalten: '$out3'"
fi

# TEST 4: build_webhook_payload
out4=$(build_webhook_payload "https://discord.com/api/webhooks/123" "NODE DOWN" "Server 04 unresponsive" "CRITICAL" || true)
expected4="curl -s -f -X POST \"https://discord.com/api/webhooks/123\" -H \"Content-Type: application/json\" -d '{\"title\":\"NODE DOWN\",\"message\":\"Server 04 unresponsive\",\"severity\":\"CRITICAL\"}'"

if [ "$out4" = "$expected4" ]; then
    echo "✓ Test 4/5: build_webhook_payload erfolgreich bestanden."
    passed=$((passed + 1))
else
    echo "✗ Test 4/5 fehlgeschlagen: Erwartete:
$expected4
Erhalten:
$out4"
fi

# TEST 5: generate_devops_html_report
TMP_HTML=$(mktemp)
generate_devops_html_report "Production Fleet Q3" 48 50 2 "$TMP_HTML"
html_content=$(cat "$TMP_HTML")
rm -f "$TMP_HTML"

if echo "$html_content" | grep -q "Production Fleet Q3" && \
   echo "$html_content" | grep -q "48 / 50" && \
   echo "$html_content" | grep -q "badge-error"; then
    echo "✓ Test 5/5: generate_devops_html_report erfolgreich bestanden."
    passed=$((passed + 1))
else
    echo "✗ Test 5/5 fehlgeschlagen: HTML Report unvollständig. Content:
$html_content"
fi

echo "---------------------------------------------------------"
if [ "$passed" -eq "$total" ]; then
    echo "🎉 Alle $total Tests für Master-Modul 16 erfolgreich bestanden!"
    exit 0
else
    echo "❌ $passed von $total Tests bestanden."
    exit 1
fi
