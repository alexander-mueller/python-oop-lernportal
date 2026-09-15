#!/usr/bin/env bash
# ==============================================================================
# 🧪 TESTSUITE: DNS 09 - MX-RECORDS & PRIORITÄTEN
# ==============================================================================

RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

TARGET_SCRIPT="${1:-aufgabe.sh}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

TOTAL_TESTS=0
PASSED_TESTS=0
FAILED_TESTS=0

echo -e "${BLUE}================================================================${NC}"
echo -e "${BLUE}🧪 TESTSUITE: DNS 09: MX-Records & Prioritäten${NC}"
echo -e "${BLUE}   Ziel-Skript: ${YELLOW}${TARGET_SCRIPT}${NC}"
echo -e "${BLUE}================================================================${NC}\n"

if [ ! -f "$SCRIPT_DIR/$TARGET_SCRIPT" ]; then
  echo -e "${RED}❌ Fehler: Datei '$TARGET_SCRIPT' nicht gefunden!${NC}"
  exit 1
fi

source "$SCRIPT_DIR/$TARGET_SCRIPT"

run_test() {
  local name="$1"
  local cmd="$2"
  ((TOTAL_TESTS++))
  echo -e "▶ Test ${TOTAL_TESTS}: ${name}"
  if eval "$cmd"; then
    echo -e "  ${GREEN}✓ BESTANDEN${NC}\n"
    ((PASSED_TESTS++))
  else
    echo -e "  ${RED}✗ FEHLGESCHLAGEN${NC}\n"
    ((FAILED_TESTS++))
  fi
}

# TEST 1: Valider MX Record
run_test "format_mx_record erzeugt standardkonformen MX Record" '
  OUT=$(format_mx_record "@" 10 "mail.it-praxisportal.de" 86400)
  echo "$OUT" | grep -q "@" && \
  echo "$OUT" | grep -q "MX" && \
  echo "$OUT" | grep -q "10" && \
  echo "$OUT" | grep -q "mail.it-praxisportal.de."
'

# TEST 2: Prioritäts-Validierung (Zahlenprüfung)
run_test "format_mx_record lehnt ungültige Priorität (abc) ab" '
  format_mx_record "@" "abc" "mail.de" | grep -q "ERROR: Priorität muss Ganzzahl"
'

# TEST 3: CNAME Verbot nach RFC 2181
run_test "validate_mx_target_type verbietet CNAME als MX-Ziel" '
  validate_mx_target_type "CNAME" | grep -q "ERROR_RFC2181"
'

# TEST 4: A-Record als valides Ziel
run_test "validate_mx_target_type erlaubt A-Record als MX-Ziel" '
  validate_mx_target_type "A" | grep -q "VALID_MX_TARGET"
'

# TEST 5: MX Sortierung nach Priorität
run_test "sort_mx_records sortiert 10 vor 20 vor 30" '
  TMP_MX=$(mktemp /tmp/mx_sort_XXXXXX)
  cat << "EOF" > "$TMP_MX"
@  IN  MX  30  fallback.mail.de.
@  IN  MX  10  primary.mail.de.
@  IN  MX  20  secondary.mail.de.
EOF
  OUT=$(sort_mx_records "$TMP_MX")
  rm -f "$TMP_MX"
  FIRST=$(echo "$OUT" | head -n 1)
  echo "$FIRST" | grep -q "PRIO=10" && \
  echo "$FIRST" | grep -q "primary.mail.de."
'

# TEST 6: Redundantes MX-Paar (10 & 20)
run_test "generate_redundant_mx_setup erzeugt Prio 10 und 20" '
  OUT=$(generate_redundant_mx_setup "firma.de" "m1.firma.de" "m2.firma.de" 86400)
  echo "$OUT" | grep -q "10.*m1.firma.de." && \
  echo "$OUT" | grep -q "20.*m2.firma.de."
'

echo -e "${BLUE}================================================================${NC}"
if [ "$FAILED_TESTS" -eq 0 ]; then
  echo -e "${GREEN}🎉 ERFOLG: Alle ${PASSED_TESTS}/${TOTAL_TESTS} Tests in DNS 09 erfolgreich bestanden!${NC}"
  echo -e "${BLUE}================================================================${NC}"
  exit 0
else
  echo -e "${RED}❌ FEHLER: ${FAILED_TESTS} von ${TOTAL_TESTS} Tests fehlgeschlagen.${NC}"
  echo -e "${BLUE}================================================================${NC}"
  exit 1
fi
