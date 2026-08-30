#!/usr/bin/env bash
# ==============================================================================
# 🧪 BATS-INSPIRIERTE TESTSUITE: BASH 05 - KONTROLLFLUSS & OPERATOREN
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
echo -e "${BLUE}🧪 TESTSUITE: Bash 05 - Kontrollfluss & Test-Operatoren${NC}"
echo -e "${BLUE}   Ziel-Skript: ${YELLOW}${TARGET_SCRIPT}${NC}"
echo -e "${BLUE}================================================================${NC}\n"

if [ ! -f "$SCRIPT_DIR/$TARGET_SCRIPT" ]; then
  echo -e "${RED}❌ Fehler: Datei '$TARGET_SCRIPT' nicht gefunden!${NC}"
  exit 1
fi

source "$SCRIPT_DIR/$TARGET_SCRIPT"

TEST_ROOT=$(mktemp -d /tmp/bash05_test_XXXXXX)
trap 'rm -rf "$TEST_ROOT"' EXIT

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

# TEST: Teilziel 1 - analysiere_pfad_status
run_test "Pfad- und Dateityppruefung mit [[ ... ]]" '
  DIR="$TEST_ROOT/somedir"
  EXEC="$TEST_ROOT/run.sh"
  REG="$TEST_ROOT/data.txt"
  mkdir -p "$DIR"
  touch "$EXEC" "$REG"
  chmod +x "$EXEC"
  
  [ "$(analysiere_pfad_status "$DIR")" = "DIRECTORY" ] && \
  [ "$(analysiere_pfad_status "$EXEC")" = "EXECUTABLE_FILE" ] && \
  [ "$(analysiere_pfad_status "$REG")" = "REGULAR_FILE" ] && \
  [ "$(analysiere_pfad_status "$TEST_ROOT/nonexistent")" = "NOT_FOUND" ]
'

# TEST: Teilziel 2 - validiere_ipv4_format
run_test "IPv4-Validierung mit Regex (=~) und Bereichspruefung" '
  validiere_ipv4_format "192.168.1.1" && \
  validiere_ipv4_format "10.0.0.254" && \
  validiere_ipv4_format "127.0.0.1" && \
  ! validiere_ipv4_format "256.1.1.1" && \
  ! validiere_ipv4_format "192.168.1" && \
  ! validiere_ipv4_format "abc.def.ghi.jkl"
'

# TEST: Teilziel 3 - bewerte_server_metrik
run_test "Server-Metrik Schwellenwertvergleich (CRITICAL / WARNING / OK)" '
  [ "$(bewerte_server_metrik 95 40)" = "CRITICAL" ] && \
  [ "$(bewerte_server_metrik 30 92)" = "CRITICAL" ] && \
  [ "$(bewerte_server_metrik 78 50)" = "WARNING" ] && \
  [ "$(bewerte_server_metrik 60 76)" = "WARNING" ] && \
  [ "$(bewerte_server_metrik 45 60)" = "OK" ]
'

# TEST: Teilziel 4 - service_dispatcher
run_test "Service Dispatcher mit case-Verzweigung" '
  [ "$(service_dispatcher "start" "nginx")" = "Starte nginx..." ] && \
  [ "$(service_dispatcher "stop" "docker")" = "Stoppe docker..." ] && \
  [ "$(service_dispatcher "restart" "redis")" = "Starte redis neu..." ] && \
  [ "$(service_dispatcher "status" "mysql")" = "Pruefe Status von mysql..." ] && \
  [ "$(service_dispatcher "invalid" "test")" = "Unbekannte Aktion: invalid" ]
'

# TEST: Teilziel 5 - fuehre_sicher_aus
run_test "Befehlsausfuehrung mit Exit-Code (\$?) Abfangen" '
  OUT1=$(fuehre_sicher_aus "true")
  EC1=$?
  OUT2=$(fuehre_sicher_aus "false")
  EC2=$?
  [ "$OUT1" = "SUCCESS" ] && [ "$EC1" -eq 0 ] && \
  [ "$OUT2" = "ERROR_CODE: 1" ] && [ "$EC2" -eq 1 ]
'

echo -e "${BLUE}================================================================${NC}"
if [ "$FAILED_TESTS" -eq 0 ]; then
  echo -e "${GREEN}🎉 ERFOLG: Alle ${PASSED_TESTS}/${TOTAL_TESTS} Tests in Bash 05 erfolgreich bestanden!${NC}"
  echo -e "${BLUE}================================================================${NC}"
  exit 0
else
  echo -e "${RED}❌ FEHLER: ${FAILED_TESTS} von ${TOTAL_TESTS} Tests fehlgeschlagen.${NC}"
  echo -e "${BLUE}================================================================${NC}"
  exit 1
fi
