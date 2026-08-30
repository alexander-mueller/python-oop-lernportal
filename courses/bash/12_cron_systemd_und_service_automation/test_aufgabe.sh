#!/usr/bin/env bash
# ==============================================================================
# Testsuite: Bash 12 - Cronjobs, Systemd & Logrotation
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

echo "🧪 Starte Tests für Modul 12 (${TARGET_FILE})..."
echo "---------------------------------------------------------"

# TEST 1: generate_cron_entry
out1=$(generate_cron_entry "*/10 * * * *" "/opt/backup.sh" "/var/log/backup.log" || true)
expected1="*/10 * * * * /opt/backup.sh >> /var/log/backup.log 2>&1"

if [ "$out1" = "$expected1" ]; then
    echo "✓ Test 1/4: generate_cron_entry erfolgreich bestanden."
    passed=$((passed + 1))
else
    echo "✗ Test 1/4 fehlgeschlagen: Erwartete: '$expected1', Erhalten: '$out1'"
fi

# TEST 2: generate_systemd_service
out2=$(generate_systemd_service "Metric Agent" "/usr/bin/agent" "node_exporter" "on-failure" || true)
if echo "$out2" | grep -F -q "Description=Metric Agent" && \
   echo "$out2" | grep -F -q "User=node_exporter" && \
   echo "$out2" | grep -F -q "ExecStart=/usr/bin/agent" && \
   echo "$out2" | grep -F -q "Restart=on-failure" && \
   echo "$out2" | grep -F -q "WantedBy=multi-user.target"; then
    echo "✓ Test 2/4: generate_systemd_service erfolgreich bestanden."
    passed=$((passed + 1))
else
    echo "✗ Test 2/4 fehlgeschlagen: Systemd Service unvollständig. Output:
$out2"
fi

# TEST 3: generate_systemd_timer
out3=$(generate_systemd_timer "Nightly Cleanup" "*-*-* 03:00:00" "cleanup.service" || true)
if echo "$out3" | grep -F -q "Description=Nightly Cleanup" && \
   echo "$out3" | grep -F -q "OnCalendar=*-*-* 03:00:00" && \
   echo "$out3" | grep -F -q "Persistent=true" && \
   echo "$out3" | grep -F -q "Unit=cleanup.service" && \
   echo "$out3" | grep -F -q "WantedBy=timers.target"; then
    echo "✓ Test 3/4: generate_systemd_timer erfolgreich bestanden."
    passed=$((passed + 1))
else
    echo "✗ Test 3/4 fehlgeschlagen: Systemd Timer unvollständig. Output:
$out3"
fi

# TEST 4: generate_logrotate_config
out4=$(generate_logrotate_config "/var/log/nginx/*.log" "weekly" 14 "false" || true)
if echo "$out4" | grep -F -q "/var/log/nginx/*.log {" && \
   echo "$out4" | grep -F -q "weekly" && \
   echo "$out4" | grep -F -q "rotate 14" && \
   echo "$out4" | grep -F -q "missingok" && \
   echo "$out4" | grep -F -q "notifempty" && \
   echo "$out4" | grep -F -q "nocompress"; then
    echo "✓ Test 4/4: generate_logrotate_config erfolgreich bestanden."
    passed=$((passed + 1))
else
    echo "✗ Test 4/4 fehlgeschlagen: Logrotate Config unvollständig. Output:
$out4"
fi

echo "---------------------------------------------------------"
if [ "$passed" -eq "$total" ]; then
    echo "🎉 Alle $total Tests für Modul 12 erfolgreich bestanden!"
    exit 0
else
    echo "❌ $passed von $total Tests bestanden."
    exit 1
fi
