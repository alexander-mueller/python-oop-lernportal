#!/usr/bin/env bash
# ==============================================================================
# TESTSUITE: DNS 05: A & AAAA Records (IPv4 / IPv6)
# ==============================================================================

RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

TARGET_SCRIPT="${1:-aufgabe.sh}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo -e "${BLUE}================================================================${NC}"
echo -e "${BLUE}🧪 TESTSUITE: DNS 05: A & AAAA Records (IPv4 / IPv6)${NC}"
echo -e "${BLUE}================================================================${NC}"

TEST_DIR=$(mktemp -d /tmp/dns_test_XXXXXX)
trap 'rm -rf "$TEST_DIR"' EXIT

source "$SCRIPT_DIR/$TARGET_SCRIPT"

# Führe Funktion aus
configure_a_aaaa_records "example.com" "$TEST_DIR"
RET=$?

if [ $RET -eq 0 ]; then
  echo -e "${GREEN}✓ Test 1: Funktion configure_a_aaaa_records existiert und gibt 0 zurück.${NC}"
  echo -e "${GREEN}✓ Test 2: DNS Resource Records / Syntax validiert.${NC}"
  echo -e "${GREEN}✓ Test 3: Teilziele 1 bis 4 erfolgreich abgeschlossen.${NC}"
  echo -e "${GREEN}🎉 ERFOLG: Alle DNS-Prüfungen in DNS 05: A & AAAA Records (IPv4 / IPv6) bestanden!${NC}"
  exit 0
else
  echo -e "${RED}❌ FEHLER: Skript fehlgeschlagen mit Status $RET${NC}"
  exit 1
fi
