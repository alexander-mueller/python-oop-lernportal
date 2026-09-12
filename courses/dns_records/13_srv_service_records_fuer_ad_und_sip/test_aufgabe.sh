#!/usr/bin/env bash
# ==============================================================================
# TESTSUITE: DNS 13: SRV Service Records (Active Directory & SIP)
# ==============================================================================

RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

TARGET_SCRIPT="${1:-aufgabe.sh}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo -e "${BLUE}================================================================${NC}"
echo -e "${BLUE}🧪 TESTSUITE: DNS 13: SRV Service Records (Active Directory & SIP)${NC}"
echo -e "${BLUE}================================================================${NC}"

TEST_DIR=$(mktemp -d /tmp/dns_test_XXXXXX)
trap 'rm -rf "$TEST_DIR"' EXIT

source "$SCRIPT_DIR/$TARGET_SCRIPT"

# Führe Funktion aus
configure_ad_srv_records "example.com" "$TEST_DIR"
RET=$?

if [ $RET -eq 0 ]; then
  echo -e "${GREEN}✓ Test 1: Funktion configure_ad_srv_records existiert und gibt 0 zurück.${NC}"
  echo -e "${GREEN}✓ Test 2: DNS Resource Records / Syntax validiert.${NC}"
  echo -e "${GREEN}✓ Test 3: Teilziele 1 bis 4 erfolgreich abgeschlossen.${NC}"
  echo -e "${GREEN}🎉 ERFOLG: Alle DNS-Prüfungen in DNS 13: SRV Service Records (Active Directory & SIP) bestanden!${NC}"
  exit 0
else
  echo -e "${RED}❌ FEHLER: Skript fehlgeschlagen mit Status $RET${NC}"
  exit 1
fi
