#!/usr/bin/env bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_SCRIPT="${1:-$SCRIPT_DIR/aufgabe.sh}"
source "$TARGET_SCRIPT"

PASSED_TESTS=0
TOTAL_TESTS=0

run_test() {
  local desc="$1"
  local cmd="$2"
  ((TOTAL_TESTS++))
  echo -e "
▶ Test ${TOTAL_TESTS}: ${desc}"
  if eval "$cmd"; then
    echo -e "  [32m✓ BESTANDEN[0m"
    ((PASSED_TESTS++))
  else
    echo -e "  [31m✗ FEHLGESCHLAGEN[0m
"
  fi
}

run_test "diagnose_dns_rcode identifiziert NXDOMAIN" '
  diagnose_dns_rcode "NXDOMAIN" | grep -q "ERROR_NXDOMAIN"
'

run_test "diagnose_dns_rcode identifiziert SERVFAIL" '
  diagnose_dns_rcode "SERVFAIL" | grep -q "ERROR_SERVFAIL"
'

run_test "extract_dig_ips filtert IPv4 Adressen sauber" '
  RAW=";; ANSWER SECTION:
www.test.de. 300 IN A 192.0.2.1
www.test.de. 300 IN A 198.51.100.2"
  IPS=$(extract_dig_ips "$RAW")
  echo "$IPS" | grep -q "192.0.2.1" &&   echo "$IPS" | grep -q "198.51.100.2"
'

run_test "detect_soa_desync erkennt synchrone Zonen" '
  detect_soa_desync 2026091501 2026091501 | grep -q "IN_SYNC"
'

run_test "detect_soa_desync schlägt Alarm bei veraltetem Slave" '
  detect_soa_desync 2026091505 2026091501 | grep -q "DESYNC"
'

run_test "verify_axfr_blocked meldet SECURE bei Abweisung" '
  verify_axfr_blocked ";; Transfer failed. REFUSED" | grep -q "SECURE: AXFR"
'

if [ "$PASSED_TESTS" -eq "$TOTAL_TESTS" ]; then
  echo -e "
[32m🎉 ERFOLG: Alle ${PASSED_TESTS}/${TOTAL_TESTS} Tests in DNS 15 bestanden![0m"
  exit 0
else
  echo -e "
[31m❌ FEHLER: ${PASSED_TESTS}/${TOTAL_TESTS} Tests bestanden.[0m"
  exit 1
fi
