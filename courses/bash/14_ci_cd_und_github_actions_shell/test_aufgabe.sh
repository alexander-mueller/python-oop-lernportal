#!/usr/bin/env bash
# ==============================================================================
# Testsuite: Bash 14 - CI/CD & GitHub Actions Shell
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

echo "🧪 Starte Tests für Modul 14 (${TARGET_FILE})..."
echo "---------------------------------------------------------"

# TEST 1: write_github_output (Single-line & Multiline)
TMP_OUT=$(mktemp)
write_github_output "version" "v2.0.4" "$TMP_OUT"
multi_val="line1
line2
line3"
write_github_output "changelog" "$multi_val" "$TMP_OUT"

out1_content=$(cat "$TMP_OUT")
rm -f "$TMP_OUT"

if echo "$out1_content" | grep -q "version=v2.0.4" && \
   echo "$out1_content" | grep -q "changelog<<EOF" && \
   echo "$out1_content" | grep -q "line2"; then
    echo "✓ Test 1/4: write_github_output erfolgreich bestanden."
    passed=$((passed + 1))
else
    echo "✗ Test 1/4 fehlgeschlagen: GITHUB_OUTPUT Format ungültig. Output:
$out1_content"
fi

# TEST 2: mask_github_secret
out2=$(mask_github_secret "ghp_TopSecret123" || true)
if [ "$out2" = "::add-mask::ghp_TopSecret123" ]; then
    echo "✓ Test 2/4: mask_github_secret erfolgreich bestanden."
    passed=$((passed + 1))
else
    echo "✗ Test 2/4 fehlgeschlagen: Erwartete '::add-mask::ghp_TopSecret123', Erhalten: '$out2'"
fi

# TEST 3: generate_step_summary_table
TMP_SUM=$(mktemp)
generate_step_summary_table "Build Metrics" "Branch:main Status:Passed Duration:12s" "$TMP_SUM"
sum_content=$(cat "$TMP_SUM")
rm -f "$TMP_SUM"

if echo "$sum_content" | grep -q "### Build Metrics" && \
   echo "$sum_content" | grep -q "| Branch | main |" && \
   echo "$sum_content" | grep -q "| Duration | 12s |"; then
    echo "✓ Test 3/4: generate_step_summary_table erfolgreich bestanden."
    passed=$((passed + 1))
else
    echo "✗ Test 3/4 fehlgeschlagen: Summary-Tabelle fehlerhaft. Output:
$sum_content"
fi

# TEST 4: detect_os_and_package_install_cmd
cmd_ubuntu=$(detect_os_and_package_install_cmd "curl" "ubuntu")
cmd_alpine=$(detect_os_and_package_install_cmd "htop" "alpine")
cmd_mac=$(detect_os_and_package_install_cmd "jq" "darwin")

if [ "$cmd_ubuntu" = "apt-get update -y && apt-get install -y curl" ] && \
   [ "$cmd_alpine" = "apk add --no-cache htop" ] && \
   [ "$cmd_mac" = "brew install jq" ]; then
    echo "✓ Test 4/4: detect_os_and_package_install_cmd erfolgreich bestanden."
    passed=$((passed + 1))
else
    echo "✗ Test 4/4 fehlgeschlagen: Unpassende Paketmanager-Befehle."
fi

echo "---------------------------------------------------------"
if [ "$passed" -eq "$total" ]; then
    echo "🎉 Alle $total Tests für Modul 14 erfolgreich bestanden!"
    exit 0
else
    echo "❌ $passed von $total Tests bestanden."
    exit 1
fi
