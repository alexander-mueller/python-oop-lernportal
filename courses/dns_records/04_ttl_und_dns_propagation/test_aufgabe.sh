#!/usr/bin/env bash
# ==============================================================================
# 🧪 TESTSUITE: DNS 04 - TTL & DNS-PROPAGATION
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
echo -e "${BLUE}🧪 TESTSUITE: DNS 04: TTL & DNS-Propagation${NC}"
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

# TEST 1: TTL Formatierung Tage
run_test "format_ttl_human: 86400 Sekunden zu 1d 0h 0m 0s" '
  format_ttl_human 86400 | grep -q "1d 0h 0m 0s"
'

# TEST 2: TTL Formatierung Minuten
run_test "format_ttl_human: 300 Sekunden zu 5m 0s" '
  format_ttl_human 300 | grep -q "5m 0s"
'

# TEST 3: Migrations-Zeitplaner mit ausreichend Vorlauf
run_test "plan_dns_migration: 86400s TTL mit 48h Vorlauf ist planbar" '
  OUT=$(plan_dns_migration 86400 48)
  echo "$OUT" | grep -q "ADVANCE_HOURS=24" && \
  echo "$OUT" | grep -q "TEMP_TTL=300" && \
  echo "$OUT" | grep -q "STATUS=READY_TO_SCHEDULE"
'

# TEST 4: Migrations-Zeitplaner warnt bei zu kurzem Vorlauf
run_test "plan_dns_migration: Warnt bei 12h Vorlauf bei 24h TTL" '
  OUT=$(plan_dns_migration 86400 12)
  echo "$OUT" | grep -q "MIGRATION_RISK: Wartungsfenster zu nah"
'

# TEST 5: Cache Decay (Noch im Cache)
run_test "simulate_cache_decay meldet CACHE_HIT bei Restzeit" '
  simulate_cache_decay 3600 1000 | grep -q "CACHE_HIT: Rest-TTL beträgt 2600s"
'

# TEST 6: Cache Decay (Abgelaufen)
run_test "simulate_cache_decay meldet CACHE_EXPIRED nach Ablauf" '
  simulate_cache_decay 3600 4000 | grep -q "CACHE_EXPIRED"
'

# TEST 7: SOA Negative Caching TTL Extraktion
run_test "extract_soa_negative_ttl liest 3600s aus SOA und meldet COMPLIANT" '
  SOA_LINE="@ IN SOA ns1.example.de. admin.example.de. 2026091501 7200 3600 1209600 3600"
  extract_soa_negative_ttl "$SOA_LINE" | grep -q "NEG_TTL=3600s | COMPLIANT=YES"
'

echo -e "${BLUE}================================================================${NC}"
if [ "$FAILED_TESTS" -eq 0 ]; then
  echo -e "${GREEN}🎉 ERFOLG: Alle ${PASSED_TESTS}/${TOTAL_TESTS} Tests in DNS 04 erfolgreich bestanden!${NC}"
  echo -e "${BLUE}================================================================${NC}"
  exit 0
else
  echo -e "${RED}❌ FEHLER: ${FAILED_TESTS} von ${TOTAL_TESTS} Tests fehlgeschlagen.${NC}"
  echo -e "${BLUE}================================================================${NC}"
  exit 1
fi
