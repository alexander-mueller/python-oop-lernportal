#!/usr/bin/env bash
# ==============================================================================
# 🧪 TESTSUITE: DNS 12 - DMARC & E-MAIL-SECURITY SUITE
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
echo -e "${BLUE}🧪 TESTSUITE: DNS 12: DMARC & E-Mail-Security Suite${NC}"
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

# TEST 1: DMARC Record Format
run_test "format_dmarc_record erzeugt _dmarc.<dom>. mit p=reject" '
  OUT=$(format_dmarc_record "firma.de" "reject" "dmarc@firma.de" 100)
  echo "$OUT" | grep -q "_dmarc.firma.de." && \
  echo "$OUT" | grep -q "p=reject" && \
  echo "$OUT" | grep -q "rua=mailto:dmarc@firma.de"
'

# TEST 2: Verdict Pass wenn DKIM gültig
run_test "evaluate_dmarc_verdict liefert PASS wenn DKIM wahr ist" '
  evaluate_dmarc_verdict "false" "true" "reject" | grep -q "VERDICT_PASS"
'

# TEST 3: Verdict Reject wenn beides fehlschlägt und p=reject
run_test "evaluate_dmarc_verdict weist Mail ab bei p=reject" '
  evaluate_dmarc_verdict "false" "false" "reject" | grep -q "VERDICT_REJECT"
'

# TEST 4: Verdict Quarantine wenn beides fehlschlägt und p=quarantine
run_test "evaluate_dmarc_verdict leitet in Spam um bei p=quarantine" '
  evaluate_dmarc_verdict "false" "false" "quarantine" | grep -q "VERDICT_QUARANTINE"
'

# TEST 5: Gesamtaudit Score 100 (SPF -all + DKIM + DMARC reject)
run_test "audit_email_security_suite vergibt 100 Punkte und EXCELLENT" '
  SPF="v=spf1 mx -all"
  DKIM="v=DKIM1; k=rsa; p=MIIBIjANBgkqhki..."
  DMARC="v=DMARC1; p=reject; rua=mailto:a@b.de"
  OUT=$(audit_email_security_suite "$SPF" "$DKIM" "$DMARC")
  echo "$OUT" | grep -q "SCORE=100" && \
  echo "$OUT" | grep -q "RATING=EXCELLENT"
'

# TEST 6: Gesamtaudit Score bei schwacher Konfiguration
run_test "audit_email_security_suite stuft p=none und Softfail ab" '
  SPF="v=spf1 ~all"
  DKIM=""
  DMARC="v=DMARC1; p=none"
  OUT=$(audit_email_security_suite "$SPF" "$DKIM" "$DMARC")
  echo "$OUT" | grep -q "SCORE=25" && \
  echo "$OUT" | grep -q "RATING=INSECURE"
'

echo -e "${BLUE}================================================================${NC}"
if [ "$FAILED_TESTS" -eq 0 ]; then
  echo -e "${GREEN}🎉 ERFOLG: Alle ${PASSED_TESTS}/${TOTAL_TESTS} Tests in DNS 12 erfolgreich bestanden!${NC}"
  echo -e "${BLUE}================================================================${NC}"
  exit 0
else
  echo -e "${RED}❌ FEHLER: ${FAILED_TESTS} von ${TOTAL_TESTS} Tests fehlgeschlagen.${NC}"
  echo -e "${BLUE}================================================================${NC}"
  exit 1
fi
