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

run_test "format_srv_record erzeugt RFC 2782 konformen SRV Eintrag" '
  OUT=$(format_srv_record "ldap" "tcp" "corp.de" 0 100 389 "dc1.corp.de" 86400)
  [ "$OUT" = "_ldap._tcp.corp.de. 86400 IN SRV 0 100 389 dc1.corp.de." ]
'

run_test "parse_srv_record extrahiert Prio, Port und Target" '
  LINE="_sip._udp.firma.de. 3600 IN SRV 10 60 5060 pbx01.firma.de."
  OUT=$(parse_srv_record "$LINE")
  echo "$OUT" | grep -q "SERVICE=_sip" &&   echo "$OUT" | grep -q "PORT=5060" &&   echo "$OUT" | grep -q "TARGET=pbx01.firma.de."
'

run_test "generate_ad_srv_records erzeugt LDAP, Kerberos und GC Records" '
  OUT=$(generate_ad_srv_records "ad.local" "dc01.ad.local" 0 100)
  echo "$OUT" | grep -q "_ldap._tcp.ad.local." &&   echo "$OUT" | grep -q "_kerberos._tcp.ad.local." &&   echo "$OUT" | grep -q "_gc._tcp.ad.local."
'

run_test "select_srv_target_by_prio wählt Host mit kleinster Priorität" '
  RECS=$(cat <<EOF
_ldap._tcp.dom.de. 300 IN SRV 20 50 389 backup.dom.de.
_ldap._tcp.dom.de. 300 IN SRV 5 100 389 primary.dom.de.
_ldap._tcp.dom.de. 300 IN SRV 10 80 389 secondary.dom.de.
EOF
)
  TARGET=$(select_srv_target_by_prio "$RECS")
  [ "$TARGET" = "primary.dom.de." ]
'

if [ "$PASSED_TESTS" -eq "$TOTAL_TESTS" ]; then
  echo -e "
[32m🎉 ERFOLG: Alle ${PASSED_TESTS}/${TOTAL_TESTS} Tests in DNS 13 bestanden![0m"
  exit 0
else
  echo -e "
[31m❌ FEHLER: ${PASSED_TESTS}/${TOTAL_TESTS} Tests bestanden.[0m"
  exit 1
fi
