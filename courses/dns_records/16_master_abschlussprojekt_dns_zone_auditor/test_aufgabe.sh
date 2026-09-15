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

SAMPLE_ZONE_CLEAN=$(cat <<'EOF'
@   IN  SOA ns1.firma.de. hostmaster.firma.de. (
            2026091501 ; serial
            7200       ; refresh
            3600       ; retry
            1209600    ; expire
            3600 )     ; minimum
@   IN  NS  ns1.firma.de.
@   IN  NS  ns2.firma.de.
@   IN  A   192.0.2.1
www IN  CNAME @
@   IN  TXT "v=spf1 mx -all"
_dmarc IN TXT "v=DMARC1; p=reject; rua=mailto:dmarc@firma.de"
EOF
)

SAMPLE_ZONE_BROKEN=$(cat <<'EOF'
@   IN  SOA ns1.firma.de. hostmaster.firma.de. ( 42 )
@   IN  NS  ns1.firma.de.
@   IN  CNAME server.extern.de.
EOF
)

run_test "audit_soa_record bestätigt 10-stellige Serial" '
  audit_soa_record "$SAMPLE_ZONE_CLEAN" | grep -q "SOA_OK"
'

run_test "audit_soa_record schlägt bei 42 fehl" '
  audit_soa_record "$SAMPLE_ZONE_BROKEN" | grep -q "SOA_FAIL"
'

run_test "audit_ns_redundancy erkennt 2 Nameserver" '
  audit_ns_redundancy "$SAMPLE_ZONE_CLEAN" | grep -q "NS_OK"
'

run_test "audit_apex_cname_collision findet illegalen CNAME" '
  audit_apex_cname_collision "$SAMPLE_ZONE_BROKEN" | grep -q "CRITICAL: CNAME at apex"
'

run_test "audit_email_defense bestätigt SPF und DMARC" '
  audit_email_defense "$SAMPLE_ZONE_CLEAN" | grep -q "EMAIL_DEFENSE_OK"
'

run_test "run_complete_zone_audit vergibt 100/100 an saubere Zone" '
  OUT=$(run_complete_zone_audit "$SAMPLE_ZONE_CLEAN")
  echo "$OUT" | grep -q "SCORE=100/100" &&   echo "$OUT" | grep -q "VERDICT=AUDIT_PASSED"
'

if [ "$PASSED_TESTS" -eq "$TOTAL_TESTS" ]; then
  echo -e "
[32m🎉 ERFOLG: Alle ${PASSED_TESTS}/${TOTAL_TESTS} Tests im Master-Projekt DNS 16 bestanden![0m"
  exit 0
else
  echo -e "
[31m❌ FEHLER: ${PASSED_TESTS}/${TOTAL_TESTS} Tests bestanden.[0m"
  exit 1
fi
