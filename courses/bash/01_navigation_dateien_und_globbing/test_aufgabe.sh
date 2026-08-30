#!/usr/bin/env bash
# ==============================================================================
# 🧪 BATS-INSPIRIERTE TESTSUITE: BASH 01 - NAVIGATION & GLOBBING
# ==============================================================================

# Farben für formatierte Terminal-Ausgabe
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

TARGET_SCRIPT="${1:-aufgabe.sh}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

TOTAL_TESTS=0
PASSED_TESTS=0
FAILED_TESTS=0

echo -e "${BLUE}================================================================${NC}"
echo -e "${BLUE}🧪 TESTSUITE: Bash 01 - Navigation, Dateioperationen & Globbing${NC}"
echo -e "${BLUE}   Ziel-Skript: ${YELLOW}${TARGET_SCRIPT}${NC}"
echo -e "${BLUE}================================================================${NC}\n"

if [ ! -f "$SCRIPT_DIR/$TARGET_SCRIPT" ]; then
  echo -e "${RED}❌ Fehler: Datei '$TARGET_SCRIPT' nicht gefunden!${NC}"
  exit 1
fi

# Source Target Script
source "$SCRIPT_DIR/$TARGET_SCRIPT"

# Temporäres Testverzeichnis anlegen
TEST_ROOT=$(mktemp -d /tmp/bash01_test_XXXXXX)
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

# TEST: Teilziel 1 - erstelle_projektstruktur
run_test "Projektstruktur mit mkdir -p anlegen" '
  WORK="$TEST_ROOT/p1"
  mkdir -p "$WORK"
  erstelle_projektstruktur "$WORK"
  [ -d "$WORK/src/components" ] && \
  [ -d "$WORK/src/utils" ] && \
  [ -d "$WORK/docs/api" ] && \
  [ -d "$WORK/backup/logs" ]
'

# TEST: Teilziel 2 - erstelle_testdateien
run_test "Testdateien mit Touch und Brace Expansion anlegen" '
  WORK="$TEST_ROOT/p2"
  mkdir -p "$WORK/src/components" "$WORK/src/utils" "$WORK/docs/api" "$WORK/backup/logs"
  erstelle_testdateien "$WORK"
  [ -f "$WORK/src/components/button.js" ] && \
  [ -f "$WORK/src/components/modal.js" ] && \
  [ -f "$WORK/src/utils/helper.js" ] && \
  [ -f "$WORK/docs/api/v1.md" ] && \
  [ -f "$WORK/docs/api/v2.md" ] && \
  [ -f "$WORK/app_dev.log" ] && \
  [ -f "$WORK/app_prod.log" ] && \
  [ -f "$WORK/config.yaml" ]
'

# TEST: Teilziel 3 - kopiere_konfigurationen
run_test "Konfigurationen und Logs mit Globbing kopieren (*.yaml, *.log)" '
  SRC="$TEST_ROOT/p3_src"
  BAK="$TEST_ROOT/p3_bak"
  mkdir -p "$SRC" "$BAK"
  touch "$SRC/app.log" "$SRC/db.log" "$SRC/settings.yaml" "$SRC/ignore.txt"
  kopiere_konfigurationen "$SRC" "$BAK"
  [ -f "$BAK/app.log" ] && \
  [ -f "$BAK/db.log" ] && \
  [ -f "$BAK/settings.yaml" ] && \
  [ ! -f "$BAK/ignore.txt" ]
'

# TEST: Teilziel 4 - verschiebe_dateien
run_test "Dokumentationsdateien (*.md) verschieben" '
  SRC="$TEST_ROOT/p4_src"
  ARCH="$TEST_ROOT/p4_arch"
  mkdir -p "$SRC/docs/api" "$ARCH"
  touch "$SRC/docs/api/guide.md" "$SRC/docs/api/reference.md" "$SRC/docs/api/index.html"
  verschiebe_dateien "$SRC" "$ARCH"
  [ -f "$ARCH/guide.md" ] && \
  [ -f "$ARCH/reference.md" ] && \
  [ ! -f "$SRC/docs/api/guide.md" ] && \
  [ -f "$SRC/docs/api/index.html" ]
'

# TEST: Teilziel 5 - bereinige_temporaere_dateien
run_test "Logdateien und backup/logs Ordner bereinigen" '
  WORK="$TEST_ROOT/p5"
  mkdir -p "$WORK/backup/logs" "$WORK/keep"
  touch "$WORK/error.log" "$WORK/debug.log" "$WORK/keep/safe.txt" "$WORK/backup/logs/old.log"
  bereinige_temporaere_dateien "$WORK"
  [ ! -f "$WORK/error.log" ] && \
  [ ! -f "$WORK/debug.log" ] && \
  [ ! -d "$WORK/backup/logs" ] && \
  [ -f "$WORK/keep/safe.txt" ]
'

echo -e "${BLUE}================================================================${NC}"
if [ "$FAILED_TESTS" -eq 0 ]; then
  echo -e "${GREEN}🎉 ERFOLG: Alle ${PASSED_TESTS}/${TOTAL_TESTS} Tests in Bash 01 erfolgreich bestanden!${NC}"
  echo -e "${BLUE}================================================================${NC}"
  exit 0
else
  echo -e "${RED}❌ FEHLER: ${FAILED_TESTS} von ${TOTAL_TESTS} Tests fehlgeschlagen.${NC}"
  echo -e "${BLUE}================================================================${NC}"
  exit 1
fi
