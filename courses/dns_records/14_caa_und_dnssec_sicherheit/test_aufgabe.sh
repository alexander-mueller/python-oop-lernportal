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

run_test "format_caa_record erzeugt validen CAA-Eintrag" '
  OUT=$(format_caa_record "firma.de" "issue" "letsencrypt.org" 0 3600)
  echo "$OUT" | grep -q "firma.de." && \
  echo "$OUT" | grep -q "CAA 0 issue" && \
  echo "$OUT" | grep -q "letsencrypt.org"
'

run_test "format_caa_wildcard_block sperrt Wildcard-Zertifikate" '
  OUT=$(format_caa_wildcard_block "it-praxisportal.de")
  echo "$OUT" | grep -q "issue" && \
  echo "$OUT" | grep -q "issuewild" && \
  echo "$OUT" | grep -q "iodef"
'

run_test "parse_ds_record extrahiert DNSSEC Parameter" '
  LINE="meinedomain.de. 3600 IN DS 19842 13 2 AABBCCDDEEFF0011223344"
  OUT=$(parse_ds_record "$LINE")
  echo "$OUT" | grep -q "KEY_TAG=19842" &&   echo "$OUT" | grep -q "ALGO=13" &&   echo "$OUT" | grep -q "HASH=AABBCCDDEEFF0011223344"
'

run_test "verify_dnssec_chain_status meldet SECURE bei Übereinstimmung" '
  verify_dnssec_chain_status "HASH123" "HASH123" | grep -q "DNSSEC_SECURE"
'

run_test "verify_dnssec_chain_status meldet BOGUS bei Abweichung" '
  verify_dnssec_chain_status "HASH123" "HASH999" | grep -q "BOGUS_CHAIN_BROKEN"
'

if [ "$PASSED_TESTS" -eq "$TOTAL_TESTS" ]; then
  echo -e "
[32m🎉 ERFOLG: Alle ${PASSED_TESTS}/${TOTAL_TESTS} Tests in DNS 14 bestanden![0m"
  exit 0
else
  echo -e "
[31m❌ FEHLER: ${PASSED_TESTS}/${TOTAL_TESTS} Tests bestanden.[0m"
  exit 1
fi
