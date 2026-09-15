#!/usr/bin/env bash
# ==============================================================================
# 🧪 TESTSUITE: DNS 06 - CNAME & ZONE-APEX
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
echo -e "${BLUE}🧪 TESTSUITE: DNS 06: CNAME & Zone-Apex-Regeln${NC}"
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

# TEST 1: CNAME Formatierung mit Schlusspunkt-Garantie
run_test "format_cname_record ergänzt Schlusspunkt am Ziel" '
  OUT=$(format_cname_record "shop" "lb.cloudhoster.de" 3600)
  echo "$OUT" | grep -q "shop" && \
  echo "$OUT" | grep -q "CNAME" && \
  echo "$OUT" | grep -q "lb.cloudhoster.de."
'

# TEST 2: Zone Apex CNAME Violation
run_test "validate_apex_cname_rule blockiert CNAME auf @" '
  validate_apex_cname_rule "@" "CNAME" | grep -q "ERROR_APEX_VIOLATION"
'

# TEST 3: CNAME auf normaler Subdomain erlaubt
run_test "validate_apex_cname_rule erlaubt CNAME auf blog" '
  validate_apex_cname_rule "blog" "CNAME" | grep -q "VALID: CNAME auf Subdomain"
'

# TEST 4: Kollisions-Erkennung (CNAME + TXT auf demselben Node)
run_test "detect_cname_collisions findet illegalen Koexistenz-Konflikt" '
  TMP_ZONE=$(mktemp /tmp/cname_col_XXXXXX)
  cat << "EOF" > "$TMP_ZONE"
blog  IN  CNAME myblog.wordpress.com.
blog  IN  TXT   "verification=12345"
EOF
  OUT=$(detect_cname_collisions "$TMP_ZONE")
  rm -f "$TMP_ZONE"
  echo "$OUT" | grep -q "CNAME_COLLISION_FOUND"
'

# TEST 5: Saubere Zonendatei ohne CNAME-Konflikte
run_test "detect_cname_collisions bestätigt saubere Zone" '
  TMP_ZONE=$(mktemp /tmp/cname_col_XXXXXX)
  cat << "EOF" > "$TMP_ZONE"
@     IN  A     192.0.2.1
blog  IN  CNAME myblog.wordpress.com.
shop  IN  CNAME shop.shopify.com.
EOF
  OUT=$(detect_cname_collisions "$TMP_ZONE")
  rm -f "$TMP_ZONE"
  echo "$OUT" | grep -q "CNAME_INTEGRITY_OK"
'

# TEST 6: CNAME Kette auflösen
run_test "trace_cname_chain verfolgt mehrstufige Alias-Kette" '
  TMP_MAP=$(mktemp /tmp/cname_map_XXXXXX)
  cat << "EOF" > "$TMP_MAP"
web app
app cdn
cdn srv01.cloud.de.
EOF
  OUT=$(trace_cname_chain "web" "$TMP_MAP")
  rm -f "$TMP_MAP"
  echo "$OUT" | grep -q "RESOLVED: web -> app -> cdn -> srv01.cloud.de."
'

# TEST 7: CNAME Loop Erkennung
run_test "trace_cname_chain erkennt zirkuläre Referenzen (Loop)" '
  TMP_MAP=$(mktemp /tmp/cname_map_XXXXXX)
  cat << "EOF" > "$TMP_MAP"
a b
b c
c a
EOF
  OUT=$(trace_cname_chain "a" "$TMP_MAP")
  rm -f "$TMP_MAP"
  echo "$OUT" | grep -q "ERROR_LOOP_DETECTED"
'

echo -e "${BLUE}================================================================${NC}"
if [ "$FAILED_TESTS" -eq 0 ]; then
  echo -e "${GREEN}🎉 ERFOLG: Alle ${PASSED_TESTS}/${TOTAL_TESTS} Tests in DNS 06 erfolgreich bestanden!${NC}"
  echo -e "${BLUE}================================================================${NC}"
  exit 0
else
  echo -e "${RED}❌ FEHLER: ${FAILED_TESTS} von ${TOTAL_TESTS} Tests fehlgeschlagen.${NC}"
  echo -e "${BLUE}================================================================${NC}"
  exit 1
fi
