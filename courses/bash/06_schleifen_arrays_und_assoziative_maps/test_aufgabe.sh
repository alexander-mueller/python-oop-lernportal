#!/usr/bin/env bash
# ==============================================================================
# 🧪 BATS-INSPIRIERTE TESTSUITE: BASH 06 - SCHLEIFEN & ARRAYS
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
echo -e "${BLUE}🧪 TESTSUITE: Bash 06 - Schleifen, Arrays & Assoziative Maps${NC}"
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

# TEST: Teilziel 1 - summiere_zahlen_array
run_test "Array-Summe mit for-Schleife berechnen" '
  RES1=$(summiere_zahlen_array 10 20 30 40)
  RES2=$(summiere_zahlen_array 5 15 25)
  [ "$RES1" -eq 100 ] && [ "$RES2" -eq 45 ]
'

# TEST: Teilziel 2 - lese_csv_zeilenweise
run_test "CSV zeilenweise einlesen und Spalte filtern" '
  CSV="user1,admin,active
user2,editor,inactive
user3,viewer,active"
  SPALTE2=$(lese_csv_zeilenweise "$CSV" 2)
  [ "$(echo "$SPALTE2" | xargs)" = "admin editor viewer" ]
'

# TEST: Teilziel 3 - verwalte_server_hashmap
run_test "Assoziatives Array (declare -A) abfragen und modifizieren" '
  IP=$(verwalte_server_hashmap "get" "database")
  SET_RES=$(verwalte_server_hashmap "set" "loadbalancer" "10.0.0.99")
  KEYS=$(verwalte_server_hashmap "keys" | xargs)
  [ "$IP" = "10.0.0.2" ] && \
  [ "$SET_RES" = "loadbalancer=10.0.0.99" ] && \
  [ "$KEYS" = "cache database gateway" ]
'

# TEST: Teilziel 4 - zaehle_element_haeufigkeit
run_test "Elementhaeufigkeit mit assoziativer Counter-Map zaehlen" '
  OUT=$(zaehle_element_haeufigkeit "nginx" "redis" "nginx" "docker" "nginx" "redis")
  LINE1=$(echo "$OUT" | sed -n "1p")
  LINE2=$(echo "$OUT" | sed -n "2p")
  LINE3=$(echo "$OUT" | sed -n "3p")
  [ "$LINE1" = "docker: 1" ] && \
  [ "$LINE2" = "nginx: 3" ] && \
  [ "$LINE3" = "redis: 2" ]
'

# TEST: Teilziel 5 - parse_cli_flags
run_test "CLI-Flags mit getopts parsen" '
  DEF=$(parse_cli_flags)
  CUSTOM=$(parse_cli_flags -e staging -p 9000 -v)
  [ "$DEF" = "ENV=production,PORT=8080,VERBOSE=false" ] && \
  [ "$CUSTOM" = "ENV=staging,PORT=9000,VERBOSE=true" ]
'

echo -e "${BLUE}================================================================${NC}"
if [ "$FAILED_TESTS" -eq 0 ]; then
  echo -e "${GREEN}🎉 ERFOLG: Alle ${PASSED_TESTS}/${TOTAL_TESTS} Tests in Bash 06 erfolgreich bestanden!${NC}"
  echo -e "${BLUE}================================================================${NC}"
  exit 0
else
  echo -e "${RED}❌ FEHLER: ${FAILED_TESTS} von ${TOTAL_TESTS} Tests fehlgeschlagen.${NC}"
  echo -e "${BLUE}================================================================${NC}"
  exit 1
fi
