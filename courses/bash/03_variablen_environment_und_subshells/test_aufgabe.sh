#!/usr/bin/env bash
# ==============================================================================
# 🧪 BATS-INSPIRIERTE TESTSUITE: BASH 03 - VARIABLEN & ENVIRONMENT
# ==============================================================================

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

TARGET_SCRIPT="${1:-aufgabe.sh}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

TOTAL_TESTS=0
PASSED_TESTS=0
FAILED_TESTS=0

echo -e "${BLUE}================================================================${NC}"
echo -e "${BLUE}🧪 TESTSUITE: Bash 03 - Variablen, Environment & Expansion${NC}"
echo -e "${BLUE}   Ziel-Skript: ${YELLOW}${TARGET_SCRIPT}${NC}"
echo -e "${BLUE}================================================================${NC}\n"

if [ ! -f "$SCRIPT_DIR/$TARGET_SCRIPT" ]; then
  echo -e "${RED}❌ Fehler: Datei '$TARGET_SCRIPT' nicht gefunden!${NC}"
  exit 1
fi

source "$SCRIPT_DIR/$TARGET_SCRIPT"

run_test() {
  local test_name="$1"
  local test_cmd="$2"
  ((TOTAL_TESTS++))

  echo -e "▶ Test ${TOTAL_TESTS}: ${test_name}"
  if eval "$test_cmd"; then
    echo -e "  ${GREEN}✓ BESTANDEN${NC}\n"
    ((PASSED_TESTS++))
  else
    echo -e "  ${RED}✗ FEHLGESCHLAGEN${NC}\n"
    ((FAILED_TESTS++))
  fi
}

# TEST: Teilziel 1 - setze_umgebungsvariable
run_test "Umgebungsvariable exportieren und formatieren" '
  OUT=$(setze_umgebungsvariable "APP_ENV" "staging_cluster")
  setze_umgebungsvariable "APP_ENV" "staging_cluster" > /dev/null
  [ "$OUT" = "APP_ENV=staging_cluster" ] && \
  [ "$APP_ENV" = "staging_cluster" ]
'

# TEST: Teilziel 2 - generiere_system_kennung
run_test "System-Kennung mit Command Substitution" '
  KENNUNG=$(generiere_system_kennung)
  EXPECTED="$(whoami)@$(hostname)_$(date +%Y-%m)"
  [ "$KENNUNG" = "$EXPECTED" ]
'

# TEST: Teilziel 3 - zerlege_dateipfad
run_test "Pfadzerlegung mit reiner Bash Parameter Expansion" '
  RES1=$(zerlege_dateipfad "/var/log/nginx/access.log")
  RES2=$(zerlege_dateipfad "/etc/systemd/system/app.service")
  [ "$RES1" = "DIR: /var/log/nginx | FILE: access.log | EXT: log | BASE: access" ] && \
  [ "$RES2" = "DIR: /etc/systemd/system | FILE: app.service | EXT: service | BASE: app" ]
'

# TEST: Teilziel 4 - ermittle_konfigurationswert
run_test "Parameter Expansion mit Standardwert" '
  VAL1=$(ermittle_konfigurationswert "production" "development")
  VAL2=$(ermittle_konfigurationswert "" "development")
  [ "$VAL1" = "production" ] && \
  [ "$VAL2" = "development" ]
'

# TEST: Teilziel 5 - berechne_disk_quota
run_test "Speicherberechnung mit Shell-Arithmetik" '
  OUT=$(berechne_disk_quota 1000 250)
  [ "$OUT" = "TOTAL: 1000MB, USED: 250MB (25%), FREE: 750MB" ] && \
  OUT2=$(berechne_disk_quota 2048 1024) && \
  [ "$OUT2" = "TOTAL: 2048MB, USED: 1024MB (50%), FREE: 1024MB" ]
'

echo -e "${BLUE}================================================================${NC}"
if [ "$FAILED_TESTS" -eq 0 ]; then
  echo -e "${GREEN}🎉 ERFOLG: Alle ${PASSED_TESTS}/${TOTAL_TESTS} Tests in Bash 03 erfolgreich bestanden!${NC}"
  echo -e "${BLUE}================================================================${NC}"
  exit 0
else
  echo -e "${RED}❌ FEHLER: ${FAILED_TESTS} von ${TOTAL_TESTS} Tests fehlgeschlagen.${NC}"
  echo -e "${BLUE}================================================================${NC}"
  exit 1
fi
