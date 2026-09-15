#!/usr/bin/env bash
# ==============================================================================
# 🧪 TESTSUITE: DNS 01 - DNS-HIERARCHIE & ROOT-SERVER
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
echo -e "${BLUE}🧪 TESTSUITE: DNS 01: DNS-Hierarchie & Root-Server${NC}"
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

# TEST 1: FQDN Zerlegung mit Schlusspunkt
run_test "parse_fqdn mit Schlusspunkt (srv01.intern.example.de.)" '
  OUT=$(parse_fqdn "srv01.intern.example.de.")
  echo "$OUT" | grep -q "HOST=srv01" && \
  echo "$OUT" | grep -q "DOMAIN=intern.example.de" && \
  echo "$OUT" | grep -q "SLD=example" && \
  echo "$OUT" | grep -q "TLD=de" && \
  echo "$OUT" | grep -q "HAS_ROOT_DOT=YES"
'

# TEST 2: FQDN Zerlegung ohne Schlusspunkt
run_test "parse_fqdn ohne Schlusspunkt (api.cloud.kunde.com)" '
  OUT=$(parse_fqdn "api.cloud.kunde.com")
  echo "$OUT" | grep -q "HOST=api" && \
  echo "$OUT" | grep -q "DOMAIN=cloud.kunde.com" && \
  echo "$OUT" | grep -q "SLD=kunde" && \
  echo "$OUT" | grep -q "TLD=com" && \
  echo "$OUT" | grep -q "HAS_ROOT_DOT=NO"
'

# TEST 3: Root-Server Auskunft Einzelcluster
run_test "list_root_server Cluster K (RIPE NCC)" '
  OUT=$(list_root_server "k")
  echo "$OUT" | grep -q "CLUSTER=K" && \
  echo "$OUT" | grep -q "RIPE NCC" && \
  echo "$OUT" | grep -q "k.root-servers.net"
'

# TEST 4: Root-Server Auskunft alle 13
run_test "list_root_server alle 13 Cluster (A-M)" '
  OUT=$(list_root_server "all")
  COUNT=$(echo "$OUT" | grep -c "root-servers.net")
  [ "$COUNT" -eq 13 ]
'

# TEST 5: Delegationspfad
run_test "build_delegation_path für www.it-praxisportal.de" '
  OUT=$(build_delegation_path "www.it-praxisportal.de")
  echo "$OUT" | grep -q "\[ROOT\] \." && \
  echo "$OUT" | grep -q "\[TLD\] de\." && \
  echo "$OUT" | grep -q "\[SLD\] it-praxisportal\.de\." && \
  echo "$OUT" | grep -q "\[FQDN\] www\.it-praxisportal\.de\."
'

# TEST 6: FQDN-Validierung (Valider Name)
run_test "validate_fqdn_syntax mit gültigem FQDN" '
  validate_fqdn_syntax "sub-01.kunde.de" | grep -q "VALID:"
'

# TEST 7: FQDN-Validierung (Ungültiger Name mit führendem Bindestrich)
run_test "validate_fqdn_syntax fängt fehlerhafte Bindestriche ab (-bad.de)" '
  validate_fqdn_syntax "-bad.firma.de" | grep -q "INVALID:"
'

echo -e "${BLUE}================================================================${NC}"
if [ "$FAILED_TESTS" -eq 0 ]; then
  echo -e "${GREEN}🎉 ERFOLG: Alle ${PASSED_TESTS}/${TOTAL_TESTS} Tests in DNS 01 erfolgreich bestanden!${NC}"
  echo -e "${BLUE}================================================================${NC}"
  exit 0
else
  echo -e "${RED}❌ FEHLER: ${FAILED_TESTS} von ${TOTAL_TESTS} Tests fehlgeschlagen.${NC}"
  echo -e "${BLUE}================================================================${NC}"
  exit 1
fi
