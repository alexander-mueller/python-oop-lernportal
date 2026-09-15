#!/usr/bin/env bash
# ==============================================================================
# 🧪 TESTSUITE: DNS 07 - SOA & SERIAL-MANAGEMENT
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
echo -e "${BLUE}🧪 TESTSUITE: DNS 07: SOA & Serial-Management${NC}"
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

# TEST 1: E-Mail zu SOA Notation
run_test "format_hostmaster_email wandelt @ in Punkt und ergänzt FQDN-Punkt" '
  OUT=$(format_hostmaster_email "hostmaster@it-praxisportal.de")
  [ "$OUT" = "hostmaster.it-praxisportal.de." ]
'

# TEST 2: Serial Generator
run_test "generate_soa_serial erzeugt 10-stellige Zahl YYYYMMDD01" '
  OUT=$(generate_soa_serial "2026-09-15" "01")
  [ "$OUT" = "2026091501" ]
'

# TEST 3: Serial Inkrement am selben Tag (01 -> 02)
run_test "increment_soa_serial erhöht Revision am selben Tag" '
  OUT=$(increment_soa_serial "2026091501" "20260915")
  [ "$OUT" = "2026091502" ]
'

# TEST 4: Serial Inkrement an neuem Tag setzt auf 01
run_test "increment_soa_serial setzt an neuem Tag auf YYYYMMDD01" '
  OUT=$(increment_soa_serial "2026091405" "20260915")
  [ "$OUT" = "2026091501" ]
'

# TEST 5: Vollständigen SOA Record erzeugen
run_test "generate_complete_soa erzeugt BIND-konformen SOA-Block" '
  OUT=$(generate_complete_soa "firma.de" "ns1.firma.de" "admin@firma.de" "2026091501" 7200 3600 1209600 3600)
  echo "$OUT" | grep -q "@ IN SOA ns1.firma.de. admin.firma.de. (" && \
  echo "$OUT" | grep -q "2026091501 ; Serial" && \
  echo "$OUT" | grep -q "7200" && \
  echo "$OUT" | grep -q "3600"
'

echo -e "${BLUE}================================================================${NC}"
if [ "$FAILED_TESTS" -eq 0 ]; then
  echo -e "${GREEN}🎉 ERFOLG: Alle ${PASSED_TESTS}/${TOTAL_TESTS} Tests in DNS 07 erfolgreich bestanden!${NC}"
  echo -e "${BLUE}================================================================${NC}"
  exit 0
else
  echo -e "${RED}❌ FEHLER: ${FAILED_TESTS} von ${TOTAL_TESTS} Tests fehlgeschlagen.${NC}"
  echo -e "${BLUE}================================================================${NC}"
  exit 1
fi
