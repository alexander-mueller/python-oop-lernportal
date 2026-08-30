#!/usr/bin/env bash
# ==============================================================================
# 🧪 BATS-INSPIRIERTE TESTSUITE: BASH 08 - ROBUSTE SKRIPTE & STRICT MODE
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
echo -e "${BLUE}🧪 TESTSUITE: Bash 08 - Robuste Skripte, Strict Mode & Traps${NC}"
echo -e "${BLUE}   Ziel-Skript: ${YELLOW}${TARGET_SCRIPT}${NC}"
echo -e "${BLUE}================================================================${NC}\n"

if [ ! -f "$SCRIPT_DIR/$TARGET_SCRIPT" ]; then
  echo -e "${RED}❌ Fehler: Datei '$TARGET_SCRIPT' nicht gefunden!${NC}"
  exit 1
fi

source "$SCRIPT_DIR/$TARGET_SCRIPT"

TEST_ROOT=$(mktemp -d /tmp/bash08_test_XXXXXX)
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

# TEST: Teilziel 1 - aktiviere_strict_mode
run_test "Strict Mode Aktivierung (set -euo pipefail)" '
  bash -c "
    source \"$SCRIPT_DIR/$TARGET_SCRIPT\"
    aktiviere_strict_mode >/dev/null
    # Unset-Variable soll zum sofortigen Abbruch fuehren
    if [ -o nounset ] && [ -o errexit ]; then
      exit 0
    else
      exit 1
    fi
  "
'

# TEST: Teilziel 2 - devops_logger
run_test "DevOps-Logger mit Zeitstempel und Stream-Trennung" '
  OUT_LOG="$TEST_ROOT/out.log"
  ERR_LOG="$TEST_ROOT/err.log"
  
  devops_logger "INFO" "Dienst gestartet" > "$OUT_LOG" 2> "$ERR_LOG"
  grep -q "\[INFO\] Dienst gestartet" "$OUT_LOG" && \
  [ ! -s "$ERR_LOG" ] && \
  
  devops_logger "ERROR" "Kritischer Verbindungsabbruch" > "$OUT_LOG" 2> "$ERR_LOG" && \
  grep -q "\[ERROR\] Kritischer Verbindungsabbruch" "$ERR_LOG"
'

# TEST: Teilziel 3 - erstelle_temp_verzeichnis_mit_cleanup
run_test "Temporaeres Verzeichnis mit mktemp anlegen" '
  TEMP_DIR=$(erstelle_temp_verzeichnis_mit_cleanup)
  [ -d "$TEMP_DIR" ] && [[ "$TEMP_DIR" =~ ^/tmp/devops_ ]]
'

# TEST: Teilziel 4 - fuehre_exklusiv_mit_lock_aus
run_test "Exklusive File-Locks mit flock verwalten" '
  LOCK_FILE="$TEST_ROOT/test.lock"
  # 1. Normaler Aufruf muss erfolgreich sein
  fuehre_exklusiv_mit_lock_aus "$LOCK_FILE" "echo Job1_Done" > "$TEST_ROOT/job1.out" && \
  grep -q "Job1_Done" "$TEST_ROOT/job1.out" && \
  
  # 2. Wenn Lock blockiert ist, muss Fehler gemeldet werden
  bash -c "
    source \"$SCRIPT_DIR/$TARGET_SCRIPT\"
    (
      flock 200
      sleep 0.5
    ) 200>\"$LOCK_FILE\" &
    BG_PID=\$!
    sleep 0.1
    fuehre_exklusiv_mit_lock_aus \"$LOCK_FILE\" \"echo Should_Not_Run\" 2>\"$TEST_ROOT/lock_err.log\"
    RET=\$?
    wait \$BG_PID 2>/dev/null || true
    [ \$RET -ne 0 ] && grep -q \"RESOURCE_LOCKED\" \"$TEST_ROOT/lock_err.log\"
  "
'

# TEST: Teilziel 5 - debug_trace_ausfuehren
run_test "Debug Trace mit set -x temporaer ausfuehren" '
  TRACE_ERR="$TEST_ROOT/trace.err"
  debug_trace_ausfuehren "echo TRACE_TEST" 2> "$TRACE_ERR" > /dev/null
  grep -q "+ " "$TRACE_ERR" || grep -q "echo TRACE_TEST" "$TRACE_ERR"
'

echo -e "${BLUE}================================================================${NC}"
if [ "$FAILED_TESTS" -eq 0 ]; then
  echo -e "${GREEN}🎉 ERFOLG: Alle ${PASSED_TESTS}/${TOTAL_TESTS} Tests in Bash 08 erfolgreich bestanden!${NC}"
  echo -e "${BLUE}================================================================${NC}"
  exit 0
else
  echo -e "${RED}❌ FEHLER: ${FAILED_TESTS} von ${TOTAL_TESTS} Tests fehlgeschlagen.${NC}"
  echo -e "${BLUE}================================================================${NC}"
  exit 1
fi
