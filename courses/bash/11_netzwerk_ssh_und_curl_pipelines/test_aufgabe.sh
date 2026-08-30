#!/usr/bin/env bash
# ==============================================================================
# Testsuite: Bash 11 - Remote SSH, REST-Pipelines (curl) & rsync
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

echo "🧪 Starte Tests für Modul 11 (${TARGET_FILE})..."
echo "---------------------------------------------------------"

# TEST 1: build_curl_post_command
out1=$(build_curl_post_command "https://api.example.com/v1" "jwt_secret_123" '{"action":"deploy"}' || true)
expected1="curl -s -f -X POST \"https://api.example.com/v1\" -H \"Authorization: Bearer jwt_secret_123\" -H \"Content-Type: application/json\" -d '{\"action\":\"deploy\"}'"

if [ "$out1" = "$expected1" ]; then
    echo "✓ Test 1/4: build_curl_post_command erfolgreich bestanden."
    passed=$((passed + 1))
else
    echo "✗ Test 1/4 fehlgeschlagen: Erwartete:
$expected1
Erhalten:
$out1"
fi

# TEST 2: get_http_status_code (mit Sandbox-resistentem Mock)
(
    # Mock curl in Subshell
    curl() {
        # Check if flags are present
        if [[ "$*" == *"-w %{http_code}"* ]] && [[ "$*" == *"-s"* ]] && [[ "$*" == *"-o /dev/null"* ]]; then
            echo "200"
            return 0
        else
            echo "INVALID_CURL_FLAGS"
            return 1
        fi
    }
    export -f curl 2>/dev/null || true
    
    code=$(get_http_status_code "https://api.status.io/health")
    if [ "$code" = "200" ]; then
        exit 0
    else
        exit 1
    fi
)
if [ $? -eq 0 ]; then
    echo "✓ Test 2/4: get_http_status_code erfolgreich bestanden."
    passed=$((passed + 1))
else
    echo "✗ Test 2/4 fehlgeschlagen: get_http_status_code rief curl nicht mit den korrekten Flags auf."
fi

# TEST 3: build_ssh_batch_command
out3=$(build_ssh_batch_command "admin" "srv01.cloud.local" "/scripts/backup.sh" 2222 || true)
expected3="ssh -p 2222 -o BatchMode=yes -o StrictHostKeyChecking=no admin@srv01.cloud.local \"bash -s\" < /scripts/backup.sh"

if [ "$out3" = "$expected3" ]; then
    echo "✓ Test 3/4: build_ssh_batch_command erfolgreich bestanden."
    passed=$((passed + 1))
else
    echo "✗ Test 3/4 fehlgeschlagen: Erwartete:
$expected3
Erhalten:
$out3"
fi

# TEST 4: build_rsync_command
out4=$(build_rsync_command "/data/app/" "backup@nas:/data/app/" "*.tmp" "true" || true)
expected4="rsync -avz --delete --exclude=\"*.tmp\" /data/app/ backup@nas:/data/app/"

if [ "$out4" = "$expected4" ]; then
    echo "✓ Test 4/4: build_rsync_command erfolgreich bestanden."
    passed=$((passed + 1))
else
    echo "✗ Test 4/4 fehlgeschlagen: Erwartete:
$expected4
Erhalten:
$out4"
fi

echo "---------------------------------------------------------"
if [ "$passed" -eq "$total" ]; then
    echo "🎉 Alle $total Tests für Modul 11 erfolgreich bestanden!"
    exit 0
else
    echo "❌ $passed von $total Tests bestanden."
    exit 1
fi
