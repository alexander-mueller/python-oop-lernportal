#!/usr/bin/env bash
# ==============================================================================
# 🧪 TESTSUITE: DNS 03 - UDP VS. TCP PORT 53 & EDNS0
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
echo -e "${BLUE}🧪 TESTSUITE: DNS 03: UDP vs. TCP Port 53 & EDNS0${NC}"
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

# TEST 1: Zonentransfer erfordert immer TCP
run_test "select_dns_transport: AXFR wählt TCP" '
  select_dns_transport 200 "AXFR" "false" | grep -q "TCP (Grund: Zonentransfer"
'

# TEST 2: Kleines Paket wählt Standard UDP
run_test "select_dns_transport: Paket <= 512B wählt UDP" '
  select_dns_transport 350 "A" "false" | grep -q "UDP (Grund: Paket passt in Standard-512B-Puffer)"
'

# TEST 3: Großes Paket mit EDNS0 bleibt auf UDP
run_test "select_dns_transport: Paket 1400B mit EDNS0 bleibt UDP_EDNS0" '
  select_dns_transport 1400 "TXT" "true" | grep -q "UDP_EDNS0"
'

# TEST 4: Großes Paket ohne EDNS0 triggert TC Truncation Fallback
run_test "select_dns_transport: Paket 800B ohne EDNS0 meldet TCP_TRUNCATED" '
  select_dns_transport 800 "ANY" "false" | grep -q "TCP_TRUNCATED"
'

# TEST 5: Sektionszähler parsen
run_test "parse_section_counts ermittelt HAS_ANSWERS Status" '
  OUT=$(parse_section_counts 1 3 2 1)
  echo "$OUT" | grep -q "QUESTIONS=1" && \
  echo "$OUT" | grep -q "ANSWERS=3" && \
  echo "$OUT" | grep -q "STATUS=HAS_ANSWERS"
'

# TEST 6: EDNS0 Erkennung aus dig-Mock
run_test "verify_edns0_in_dig erkennt OPT PSEUDOSECTION" '
  TMP_DIG=$(mktemp /tmp/dig_mock_XXXXXX)
  cat << "EOF" > "$TMP_DIG"
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 1234
;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;example.com. IN A
EOF
  OUT=$(verify_edns0_in_dig "$TMP_DIG")
  rm -f "$TMP_DIG"
  echo "$OUT" | grep -q "EDNS0_ACTIVE: Puffergröße 4096 Bytes"
'

# TEST 7: BIND Zonentransfer Absicherung
run_test "secure_zone_transfers schreibt allow-transfer Direktive" '
  TMP_ZONE=$(mktemp /tmp/zone_conf_XXXXXX)
  secure_zone_transfers "firma.de" "10.0.0.20" "$TMP_ZONE"
  [ -f "$TMP_ZONE" ] && \
  grep -q "zone "firma.de"" "$TMP_ZONE" && \
  grep -q "allow-transfer { 10.0.0.20; };" "$TMP_ZONE"
  rm -f "$TMP_ZONE"
'

echo -e "${BLUE}================================================================${NC}"
if [ "$FAILED_TESTS" -eq 0 ]; then
  echo -e "${GREEN}🎉 ERFOLG: Alle ${PASSED_TESTS}/${TOTAL_TESTS} Tests in DNS 03 erfolgreich bestanden!${NC}"
  echo -e "${BLUE}================================================================${NC}"
  exit 0
else
  echo -e "${RED}❌ FEHLER: ${FAILED_TESTS} von ${TOTAL_TESTS} Tests fehlgeschlagen.${NC}"
  echo -e "${BLUE}================================================================${NC}"
  exit 1
fi
