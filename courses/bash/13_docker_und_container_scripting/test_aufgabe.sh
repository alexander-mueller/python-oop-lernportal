#!/usr/bin/env bash
# ==============================================================================
# Testsuite: Bash 13 - Docker & Container Lifecycle Scripting
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

echo "🧪 Starte Tests für Modul 13 (${TARGET_FILE})..."
echo "---------------------------------------------------------"

# TEST 1: poll_container_health (mit Mock)
(
    CALL_COUNT_FILE="/tmp/docker_mock_cnt_$$"
    echo "0" > "$CALL_COUNT_FILE"

    docker() {
        if [ "$1" = "inspect" ]; then
            local cnt
            cnt=$(cat "$CALL_COUNT_FILE")
            cnt=$((cnt + 1))
            echo "$cnt" > "$CALL_COUNT_FILE"

            if [ "$cnt" -ge 2 ]; then
                echo "healthy"
            else
                echo "starting"
            fi
            return 0
        fi
        return 1
    }
    export -f docker 2>/dev/null || true

    res=$(poll_container_health "redis-cache" 3 0)
    rm -f "$CALL_COUNT_FILE"

    if [ "$res" = "CONTAINER_HEALTHY: redis-cache" ]; then
        exit 0
    else
        exit 1
    fi
)
if [ $? -eq 0 ]; then
    echo "✓ Test 1/4: poll_container_health erfolgreich bestanden."
    passed=$((passed + 1))
else
    echo "✗ Test 1/4 fehlgeschlagen: poll_container_health erkannte Health-Zustand nicht."
fi

# TEST 2: build_volume_backup_command
out2=$(build_volume_backup_command "db_data" "/var/backups" "db_2026.tar.gz" || true)
expected2="docker run --rm -v db_data:/volume_data -v /var/backups:/backup alpine tar czf /backup/db_2026.tar.gz -C /volume_data ."

if [ "$out2" = "$expected2" ]; then
    echo "✓ Test 2/4: build_volume_backup_command erfolgreich bestanden."
    passed=$((passed + 1))
else
    echo "✗ Test 2/4 fehlgeschlagen: Erwartete:
$expected2
Erhalten:
$out2"
fi

# TEST 3: build_docker_prune_command
out3=$(build_docker_prune_command "true" "48" || true)
expected3="docker system prune -f -a --filter \"until=48h\""

if [ "$out3" = "$expected3" ]; then
    echo "✓ Test 3/4: build_docker_prune_command erfolgreich bestanden."
    passed=$((passed + 1))
else
    echo "✗ Test 3/4 fehlgeschlagen: Erwartete: '$expected3', Erhalten: '$out3'"
fi

# TEST 4: parse_container_stats_json
test_json='{"name":"auth_microservice","cpu":"1.8%","mem_usage":"128MiB / 4GiB"}'
out4=$(parse_container_stats_json "$test_json" || true)
expected4="CONTAINER: auth_microservice | CPU: 1.8% | MEM: 128MiB / 4GiB"

if [ "$out4" = "$expected4" ]; then
    echo "✓ Test 4/4: parse_container_stats_json erfolgreich bestanden."
    passed=$((passed + 1))
else
    echo "✗ Test 4/4 fehlgeschlagen: Erwartete: '$expected4', Erhalten: '$out4'"
fi

echo "---------------------------------------------------------"
if [ "$passed" -eq "$total" ]; then
    echo "🎉 Alle $total Tests für Modul 13 erfolgreich bestanden!"
    exit 0
else
    echo "❌ $passed von $total Tests bestanden."
    exit 1
fi
