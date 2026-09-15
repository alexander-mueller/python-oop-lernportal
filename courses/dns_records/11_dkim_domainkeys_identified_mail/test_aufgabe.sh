#!/usr/bin/env bash
# ==============================================================================
# 🧪 TESTSUITE: DNS 11 - DKIM SIGNATUREN & SCHLÜSSEL
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
echo -e "${BLUE}🧪 TESTSUITE: DNS 11: DKIM E-Mail-Signatur${NC}"
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

# TEST 1: DKIM FQDN Erzeugung mit Selector
run_test "build_dkim_fqdn erzeugt s1._domainkey.firma.de." '
  OUT=$(build_dkim_fqdn "s1" "firma.de")
  [ "$OUT" = "s1._domainkey.firma.de." ]
'

# TEST 2: Unsicheren 1024-Bit Schlüssel erkennen
run_test "audit_dkim_key_security warnt vor 1024-Bit RSA Key (<300 Zeichen)" '
  SHORT_KEY="MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC3QVRXA1rNu7eBwI+2fW=="
  audit_dkim_key_security "$SHORT_KEY" | grep -q "INSECURE: 1024-Bit"
'

# TEST 3: Sicheren 2048-Bit Schlüssel bestätigen
run_test "audit_dkim_key_security bestätigt 2048-Bit RSA Key (>=300 Zeichen)" '
  LONG_KEY=$(head -c 392 < /dev/zero | tr "\0" "A")
  audit_dkim_key_security "$LONG_KEY" | grep -q "SECURE: 2048-Bit"
'

# TEST 4: BIND TXT Splitting bei >250 Zeichen
run_test "format_dkim_record splittet lange Keys in BIND Multi-String ( ... )" '
  LONG_KEY=$(head -c 350 < /dev/zero | tr "\0" "X")
  OUT=$(format_dkim_record "s2026" "it-praxisportal.de" "$LONG_KEY" 86400)
  echo "$OUT" | grep -q "s2026._domainkey.it-praxisportal.de." && \
  echo "$OUT" | grep -q "TXT ("
'

# TEST 5: DKIM Tags parsen
run_test "parse_dkim_record extrahiert v, k und Key-Preview" '
  SAMPLE="v=DKIM1; k=rsa; p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA012345"
  OUT=$(parse_dkim_record "$SAMPLE")
  echo "$OUT" | grep -q "VERSION=DKIM1" && \
  echo "$OUT" | grep -q "KEY_TYPE=rsa" && \
  echo "$OUT" | grep -q "KEY_PREVIEW=MIIBIjANBgkqhki..."
'

echo -e "${BLUE}================================================================${NC}"
if [ "$FAILED_TESTS" -eq 0 ]; then
  echo -e "${GREEN}🎉 ERFOLG: Alle ${PASSED_TESTS}/${TOTAL_TESTS} Tests in DNS 11 erfolgreich bestanden!${NC}"
  echo -e "${BLUE}================================================================${NC}"
  exit 0
else
  echo -e "${RED}❌ FEHLER: ${FAILED_TESTS} von ${TOTAL_TESTS} Tests fehlgeschlagen.${NC}"
  echo -e "${BLUE}================================================================${NC}"
  exit 1
fi
