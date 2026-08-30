#!/usr/bin/env bash
# ==============================================================================
# 🧪 BATS-INSPIRIERTE TESTSUITE: BASH 04 - DATEIRECHTE & PROZESSE
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
echo -e "${BLUE}🧪 TESTSUITE: Bash 04 - Dateirechte & Prozesskontrolle${NC}"
echo -e "${BLUE}   Ziel-Skript: ${YELLOW}${TARGET_SCRIPT}${NC}"
echo -e "${BLUE}================================================================${NC}\n"

if [ ! -f "$SCRIPT_DIR/$TARGET_SCRIPT" ]; then
  echo -e "${RED}❌ Fehler: Datei '$TARGET_SCRIPT' nicht gefunden!${NC}"
  exit 1
fi

source "$SCRIPT_DIR/$TARGET_SCRIPT"

TEST_ROOT=$(mktemp -d /tmp/bash04_test_XXXXXX)
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

# TEST: Teilziel 1 - setze_sichere_rechte
run_test "Dateirechte per chmod setzen (600, 755, 644)" '
  KEY="$TEST_ROOT/id_rsa"
  SH="$TEST_ROOT/deploy.sh"
  CONF="$TEST_ROOT/app.conf"
  touch "$KEY" "$SH" "$CONF"
  
  R1=$(setze_sichere_rechte "$KEY" "secret")
  R2=$(setze_sichere_rechte "$SH" "script")
  R3=$(setze_sichere_rechte "$CONF" "config")
  
  [ "$R1" = "600" ] && [ "$R2" = "755" ] && [ "$R3" = "644" ]
'

# TEST: Teilziel 2 - lese_oktal_rechte
run_test "Oktalrechte mit stat auslesen" '
  FILE="$TEST_ROOT/test_stat.txt"
  touch "$FILE"
  chmod 755 "$FILE"
  MODE=$(lese_oktal_rechte "$FILE")
  [ "$MODE" = "755" ]
'

# TEST: Teilziel 3 - starte_hintergrund_prozess
run_test "Prozess im Hintergrund starten (&) und PID erfassen (\$!)" '
  PID=$(starte_hintergrund_prozess 5)
  # PID muss eine valide Zahl sein und Prozess muss existieren
  [[ "$PID" =~ ^[0-9]+$ ]] && kill -0 "$PID" 2>/dev/null && kill -9 "$PID" 2>/dev/null
'

# TEST: Teilziel 4 - ist_prozess_am_leben
run_test "Prozess-Existenz pruefen mit kill -0" '
  sleep 5 &
  PID=$!
  ist_prozess_am_leben "$PID"
  ALIVE=$?
  kill -9 "$PID" 2>/dev/null
  wait "$PID" 2>/dev/null || true
  ist_prozess_am_leben "$PID"
  DEAD=$?
  [ "$ALIVE" -eq 0 ] && [ "$DEAD" -ne 0 ]
'

# TEST: Teilziel 5 - stoppe_prozess_mit_fallback
run_test "Prozess sanft beenden mit Fallback (Signal 15 / Signal 9)" '
  sleep 10 &
  PID=$!
  stoppe_prozess_mit_fallback "$PID"
  ! kill -0 "$PID" 2>/dev/null
'

echo -e "${BLUE}================================================================${NC}"
if [ "$FAILED_TESTS" -eq 0 ]; then
  echo -e "${GREEN}🎉 ERFOLG: Alle ${PASSED_TESTS}/${TOTAL_TESTS} Tests in Bash 04 erfolgreich bestanden!${NC}"
  echo -e "${BLUE}================================================================${NC}"
  exit 0
else
  echo -e "${RED}❌ FEHLER: ${FAILED_TESTS} von ${TOTAL_TESTS} Tests fehlgeschlagen.${NC}"
  echo -e "${BLUE}================================================================${NC}"
  exit 1
fi
