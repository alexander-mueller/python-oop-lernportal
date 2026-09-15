#!/usr/bin/env bash
# ==============================================================================
# 🧪 TESTSUITE: DNS 02 - REKURSIVE VS. ITERATIVE ABFRAGEN
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
echo -e "${BLUE}🧪 TESTSUITE: DNS 02: Rekursive vs. Iterative Abfragen${NC}"
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

# TEST 1: Flag-Parsing (Response, autoritativ, keine Rekursion)
run_test "parse_dns_flags: qr aa (Authoritative Answer)" '
  OUT=$(parse_dns_flags "qr aa")
  echo "$OUT" | grep -q "QR=1_RESPONSE" && \
  echo "$OUT" | grep -q "AA=YES" && \
  echo "$OUT" | grep -q "RA=NO"
'

# TEST 2: Flag-Parsing (Query mit Rekursionswunsch)
run_test "parse_dns_flags: rd (Recursion Desired Query)" '
  OUT=$(parse_dns_flags "rd")
  echo "$OUT" | grep -q "QR=0_QUERY" && \
  echo "$OUT" | grep -q "RD=YES" && \
  echo "$OUT" | grep -q "AA=NO"
'

# TEST 3: Iterations-Simulation
run_test "simulate_iterative_steps für shop.kunde.de" '
  OUT=$(simulate_iterative_steps "shop.kunde.de")
  echo "$OUT" | grep -q "SCHRITT 1:.*Root.*de\." && \
  echo "$OUT" | grep -q "SCHRITT 2:.*TLD.*kunde\.de\." && \
  echo "$OUT" | grep -q "SCHRITT 3:.*autoritativen.*AA=1" && \
  echo "$OUT" | grep -q "SCHRITT 4:.*Cache.*RA=1"
'

# TEST 4: Open Resolver Erkennung (Gefahr bei 0.0.0.0/0)
run_test "detect_open_resolver schlägt Alarm bei freier Rekursion" '
  OUT=$(detect_open_resolver "qr rd ra" "0.0.0.0/0")
  echo "$OUT" | grep -q "SECURITY_ALERT: Open Resolver erkannt"
'

# TEST 5: Sicherer interner Resolver
run_test "detect_open_resolver meldet sicher bei privatem Subnetz" '
  OUT=$(detect_open_resolver "qr rd ra" "192.168.1.0/24")
  echo "$OUT" | grep -q "SECURE: Rekursiver Resolver"
'

# TEST 6: BIND Forwarder Konfigurationsdatei
run_test "generate_forwarder_config erzeugt valides named.conf.options" '
  TMP_CONF=$(mktemp /tmp/named_conf_XXXXXX)
  generate_forwarder_config "$TMP_CONF" "1.1.1.1" "8.8.8.8"
  [ -f "$TMP_CONF" ] && \
  grep -q "forwarders {" "$TMP_CONF" && \
  grep -q "1.1.1.1;" "$TMP_CONF" && \
  grep -q "8.8.8.8;" "$TMP_CONF" && \
  grep -q "forward only;" "$TMP_CONF"
  rm -f "$TMP_CONF"
'

echo -e "${BLUE}================================================================${NC}"
if [ "$FAILED_TESTS" -eq 0 ]; then
  echo -e "${GREEN}🎉 ERFOLG: Alle ${PASSED_TESTS}/${TOTAL_TESTS} Tests in DNS 02 erfolgreich bestanden!${NC}"
  echo -e "${BLUE}================================================================${NC}"
  exit 0
else
  echo -e "${RED}❌ FEHLER: ${FAILED_TESTS} von ${TOTAL_TESTS} Tests fehlgeschlagen.${NC}"
  echo -e "${BLUE}================================================================${NC}"
  exit 1
fi
