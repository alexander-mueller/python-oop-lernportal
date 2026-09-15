#!/usr/bin/env bash
# ==============================================================================
# 🧪 TESTSUITE: DNS 05 - A- & AAAA-RECORDS
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
echo -e "${BLUE}🧪 TESTSUITE: DNS 05: A- & AAAA-Records (IPv4 / IPv6)${NC}"
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

# TEST 1: Valider A-Record
run_test "format_a_record erzeugt standardkonformen A-Record" '
  OUT=$(format_a_record "www" "192.0.2.10" 3600)
  echo "$OUT" | grep -q "www" && \
  echo "$OUT" | grep -q "3600" && \
  echo "$OUT" | grep -q "IN" && \
  echo "$OUT" | grep -q "A" && \
  echo "$OUT" | grep -q "192.0.2.10"
'

# TEST 2: Invalide IPv4 (Oktett > 255)
run_test "format_a_record lehnt ungültige IPv4 (256.0.0.1) ab" '
  format_a_record "host" "256.0.0.1" 3600 | grep -q "ERROR: Ungültige IPv4"
'

# TEST 3: Valider AAAA-Record
run_test "format_aaaa_record erzeugt AAAA-Record" '
  OUT=$(format_aaaa_record "app" "2001:db8::cafe" 7200)
  echo "$OUT" | grep -q "app" && \
  echo "$OUT" | grep -q "7200" && \
  echo "$OUT" | grep -q "AAAA" && \
  echo "$OUT" | grep -q "2001:db8::cafe"
'

# TEST 4: Round Robin Pool
run_test "generate_round_robin_pool erzeugt 3 A-Records für www" '
  OUT=$(generate_round_robin_pool "www" 300 "192.0.2.1" "192.0.2.2" "192.0.2.3")
  COUNT=$(echo "$OUT" | grep -c "IN  A")
  [ "$COUNT" -eq 3 ]
'

# TEST 5: Dual Stack Audit (Vollständig)
run_test "audit_dual_stack meldet OK wenn alle A-Hosts auch AAAA haben" '
  TMP_ZONE=$(mktemp /tmp/ds_zone_XXXXXX)
  cat << "EOF" > "$TMP_ZONE"
www   3600  IN  A     192.0.2.10
www   3600  IN  AAAA  2001:db8::10
api   3600  IN  A     192.0.2.20
api   3600  IN  AAAA  2001:db8::20
EOF
  OUT=$(audit_dual_stack "$TMP_ZONE")
  rm -f "$TMP_ZONE"
  echo "$OUT" | grep -q "DUAL_STACK_AUDIT: OK"
'

# TEST 6: Dual Stack Audit (Warnung bei fehlendem AAAA)
run_test "audit_dual_stack warnt wenn mail nur A hat" '
  TMP_ZONE=$(mktemp /tmp/ds_zone_XXXXXX)
  cat << "EOF" > "$TMP_ZONE"
www   3600  IN  A     192.0.2.10
www   3600  IN  AAAA  2001:db8::10
mail  3600  IN  A     192.0.2.25
EOF
  OUT=$(audit_dual_stack "$TMP_ZONE")
  rm -f "$TMP_ZONE"
  echo "$OUT" | grep -q "DUAL_STACK_WARNUNG" && \
  echo "$OUT" | grep -q "mail"
'

echo -e "${BLUE}================================================================${NC}"
if [ "$FAILED_TESTS" -eq 0 ]; then
  echo -e "${GREEN}🎉 ERFOLG: Alle ${PASSED_TESTS}/${TOTAL_TESTS} Tests in DNS 05 erfolgreich bestanden!${NC}"
  echo -e "${BLUE}================================================================${NC}"
  exit 0
else
  echo -e "${RED}❌ FEHLER: ${FAILED_TESTS} von ${TOTAL_TESTS} Tests fehlgeschlagen.${NC}"
  echo -e "${BLUE}================================================================${NC}"
  exit 1
fi
