#!/usr/bin/env bash
# ==============================================================================
# 🧪 BATS-INSPIRIERTE TESTSUITE: BASH 02 - STREAMS, PIPES & REDIRECTION
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
echo -e "${BLUE}🧪 TESTSUITE: Bash 02 - Streams, Pipes & Redirection${NC}"
echo -e "${BLUE}   Ziel-Skript: ${YELLOW}${TARGET_SCRIPT}${NC}"
echo -e "${BLUE}================================================================${NC}\n"

if [ ! -f "$SCRIPT_DIR/$TARGET_SCRIPT" ]; then
  echo -e "${RED}❌ Fehler: Datei '$TARGET_SCRIPT' nicht gefunden!${NC}"
  exit 1
fi

source "$SCRIPT_DIR/$TARGET_SCRIPT"

TEST_ROOT=$(mktemp -d /tmp/bash02_test_XXXXXX)
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

# TEST: Teilziel 1 - erstelle_system_bericht
run_test "System-Bericht mit Here-Doc und Redirection schreiben" '
  REPORT="$TEST_ROOT/report.txt"
  erstelle_system_bericht "$REPORT" "prod-web-01" "Ubuntu 24.04"
  [ -f "$REPORT" ] && \
  grep -q "=== SYSTEM BERICHT ===" "$REPORT" && \
  grep -q "SERVER: prod-web-01" "$REPORT" && \
  grep -q "OS: Ubuntu 24.04" "$REPORT" && \
  grep -q "STATUS: INITIALISIERT" "$REPORT"
'

# TEST: Teilziel 2 - haenge_status_an
run_test "Statuszeile mit >> an bestehende Datei anhaengen" '
  LOG="$TEST_ROOT/app.log"
  echo "HEADER" > "$LOG"
  haenge_status_an "$LOG" "Database connection established"
  haenge_status_an "$LOG" "Listening on port 8080"
  grep -q "\[STATUS\] Database connection established" "$LOG" && \
  grep -q "\[STATUS\] Listening on port 8080" "$LOG" && \
  [ "$(wc -l < "$LOG")" -eq 3 ]
'

# TEST: Teilziel 3 - trenne_befehls_ausgabe
run_test "Standard Output (1>) und Error (2>) sauber trennen" '
  OUT="$TEST_ROOT/out.log"
  ERR="$TEST_ROOT/err.log"
  CMD="{ echo \"Erfolgreicher Job\"; echo \"Fehlerhafter Zugriff\" >&2; }"
  trenne_befehls_ausgabe "$CMD" "$OUT" "$ERR"
  grep -q "Erfolgreicher Job" "$OUT" && \
  grep -q "Fehlerhafter Zugriff" "$ERR" && \
  ! grep -q "Fehlerhafter Zugriff" "$OUT" && \
  ! grep -q "Erfolgreicher Job" "$ERR"
'

# TEST: Teilziel 4 - unterdruecke_fehler
run_test "Fehlermeldungen nach /dev/null umleiten" '
  CMD="{ echo \"Wichtige Ausgabe\"; echo \"Warnung 404\" >&2; }"
  OUTPUT=$(unterdruecke_fehler "$CMD")
  [ "$OUTPUT" = "Wichtige Ausgabe" ]
'

# TEST: Teilziel 5 - pipe_und_tee_pipeline
run_test "Pipeline mit Filter, Uppercase, tee und sort" '
  RAW=$'\
# Ignore comment\n\
nginx\n\
docker\n\
# Another comment\n\
apache\n\
redis'
  TEE_FILE="$TEST_ROOT/tee_output.log"
  FINAL_OUT=$(pipe_und_tee_pipeline "$RAW" "$TEE_FILE")
  
  # Pruefe Tee-Datei (ungestrichen, uppercase)
  [ -f "$TEE_FILE" ] && \
  grep -q "NGINX" "$TEE_FILE" && \
  grep -q "DOCKER" "$TEE_FILE" && \
  ! grep -q "#" "$TEE_FILE" && \
  
  # Pruefe Endausgabe (sortiert)
  FIRST_LINE=$(echo "$FINAL_OUT" | head -n 1)
  LAST_LINE=$(echo "$FINAL_OUT" | tail -n 1)
  [ "$FIRST_LINE" = "APACHE" ] && [ "$LAST_LINE" = "REDIS" ]
'

echo -e "${BLUE}================================================================${NC}"
if [ "$FAILED_TESTS" -eq 0 ]; then
  echo -e "${GREEN}🎉 ERFOLG: Alle ${PASSED_TESTS}/${TOTAL_TESTS} Tests in Bash 02 erfolgreich bestanden!${NC}"
  echo -e "${BLUE}================================================================${NC}"
  exit 0
else
  echo -e "${RED}❌ FEHLER: ${FAILED_TESTS} von ${TOTAL_TESTS} Tests fehlgeschlagen.${NC}"
  echo -e "${BLUE}================================================================${NC}"
  exit 1
fi
