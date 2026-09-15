#!/usr/bin/env bash
# ==============================================================================
# 🧪 TESTSUITE: DNS 08 - NS-DELEGATION & REVERSE DNS (PTR)
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
echo -e "${BLUE}🧪 TESTSUITE: DNS 08: NS-Delegation & Reverse DNS (PTR)${NC}"
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

# TEST 1: IPv4 zu PTR Name (Umkehrung der Oktette)
run_test "ipv4_to_ptr_name kehrt 192.0.2.42 korrekt zu 42.2.0.192.in-addr.arpa. um" '
  OUT=$(ipv4_to_ptr_name "192.0.2.42")
  [ "$OUT" = "42.2.0.192.in-addr.arpa." ]
'

# TEST 2: Vollständiger PTR-Record
run_test "format_ptr_record erzeugt standardkonformen BIND PTR-Record" '
  OUT=$(format_ptr_record "188.245.100.5" "mail.it-praxisportal.de" 86400)
  echo "$OUT" | grep -q "5.100.245.188.in-addr.arpa." && \
  echo "$OUT" | grep -q "PTR" && \
  echo "$OUT" | grep -q "mail.it-praxisportal.de."
'

# TEST 3: NS Delegation mit 2 redundanten Servern
run_test "format_ns_delegation erzeugt 2 redundante NS Records" '
  OUT=$(format_ns_delegation "intern.firma.de" "ns1.provider.de" "ns2.provider.de" 86400)
  echo "$OUT" | grep -q "intern.firma.de." && \
  echo "$OUT" | grep -q "ns1.provider.de." && \
  echo "$OUT" | grep -q "ns2.provider.de."
'

# TEST 4: FCrDNS Bestanden
run_test "verify_fcrdns meldet FCRDNS_PASS bei IP-Gleichheit" '
  OUT=$(verify_fcrdns "188.245.100.5" "mail.it-praxisportal.de" "188.245.100.5")
  echo "$OUT" | grep -q "FCRDNS_PASS: Validiert"
'

# TEST 5: FCrDNS Fehlgeschlagen (Spoofing)
run_test "verify_fcrdns meldet FCRDNS_FAIL bei IP-Diskrepanz" '
  OUT=$(verify_fcrdns "188.245.100.5" "mail.evil.com" "10.0.0.99")
  echo "$OUT" | grep -q "FCRDNS_FAIL: Spoofing-Verdacht"
'

echo -e "${BLUE}================================================================${NC}"
if [ "$FAILED_TESTS" -eq 0 ]; then
  echo -e "${GREEN}🎉 ERFOLG: Alle ${PASSED_TESTS}/${TOTAL_TESTS} Tests in DNS 08 erfolgreich bestanden!${NC}"
  echo -e "${BLUE}================================================================${NC}"
  exit 0
else
  echo -e "${RED}❌ FEHLER: ${FAILED_TESTS} von ${TOTAL_TESTS} Tests fehlgeschlagen.${NC}"
  echo -e "${BLUE}================================================================${NC}"
  exit 1
fi
