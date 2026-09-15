#!/usr/bin/env bash
# ==============================================================================
# 🧪 TESTSUITE: DNS 10 - SPF SENDER POLICY FRAMEWORK
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
echo -e "${BLUE}🧪 TESTSUITE: DNS 10: SPF Sender Policy Framework${NC}"
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

# TEST 1: SPF Record Builder
run_test "build_spf_record erzeugt validen SPF-String" '
  OUT=$(build_spf_record "true" "192.0.2.1" "_spf.google.com" "-all")
  [ "$OUT" = "v=spf1 mx ip4:192.0.2.1 include:_spf.google.com -all" ]
'

# TEST 2: Lookup Count im grünen Bereich (2 Lookups)
run_test "count_spf_lookups meldet RFC7208_OK bei 2 Lookups" '
  OUT=$(count_spf_lookups "v=spf1 mx include:_spf.google.com -all")
  echo "$OUT" | grep -q "LOOKUP_COUNT=2" && \
  echo "$OUT" | grep -q "RFC7208_OK"
'

# TEST 3: Lookup Count Limit überschritten (>10)
run_test "count_spf_lookups schlägt Alarm bei 11 Lookups" '
  SPF="v=spf1 mx a include:1.de include:2.de include:3.de include:4.de include:5.de include:6.de include:7.de include:8.de include:9.de -all"
  OUT=$(count_spf_lookups "$SPF")
  echo "$OUT" | grep -q "LOOKUP_LIMIT_EXCEEDED"
'

# TEST 4: DANGEROUS +all Abweisung
run_test "audit_spf_qualifier warnt vor gefährlichem +all" '
  audit_spf_qualifier "v=spf1 mx +all" | grep -q "DANGEROUS: +all"
'

# TEST 5: SECURE -all Bestätigung
run_test "audit_spf_qualifier bestätigt striktes -all" '
  audit_spf_qualifier "v=spf1 mx -all" | grep -q "SECURE: -all"
'

# TEST 6: BIND TXT Record Formatierung
run_test "format_spf_txt_record erzeugt valides TXT-Record Format" '
  OUT=$(format_spf_txt_record "@" "v=spf1 mx -all" 3600)
  echo "$OUT" | grep -q "@" && \
  echo "$OUT" | grep -q "TXT" && \
  echo "$OUT" | grep -F -q "\"v=spf1 mx -all\""
'

echo -e "${BLUE}================================================================${NC}"
if [ "$FAILED_TESTS" -eq 0 ]; then
  echo -e "${GREEN}🎉 ERFOLG: Alle ${PASSED_TESTS}/${TOTAL_TESTS} Tests in DNS 10 erfolgreich bestanden!${NC}"
  echo -e "${BLUE}================================================================${NC}"
  exit 0
else
  echo -e "${RED}❌ FEHLER: ${FAILED_TESTS} von ${TOTAL_TESTS} Tests fehlgeschlagen.${NC}"
  echo -e "${BLUE}================================================================${NC}"
  exit 1
fi
