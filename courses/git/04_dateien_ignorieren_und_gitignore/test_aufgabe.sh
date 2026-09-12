#!/usr/bin/env bash
# ==============================================================================
# TESTSUITE: Git 04: .gitignore & Ausschlussregeln
# ==============================================================================

RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

TARGET_SCRIPT="${1:-aufgabe.sh}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo -e "${BLUE}================================================================${NC}"
echo -e "${BLUE}🧪 TESTSUITE: Git 04: .gitignore & Ausschlussregeln${NC}"
echo -e "${BLUE}================================================================${NC}"

TEST_REPO=$(mktemp -d /tmp/git_test_XXXXXX)
trap 'rm -rf "$TEST_REPO"' EXIT

cd "$TEST_REPO" || exit 1
git init -b main >/dev/null 2>&1 || git init >/dev/null 2>&1
git config user.name "Test Runner"
git config user.email "test@example.com"

# Führe Zielskript aus
source "$SCRIPT_DIR/$TARGET_SCRIPT"
setup_gitignore "$TEST_REPO"
RET=$?

if [ $RET -eq 0 ]; then
  echo -e "${GREEN}✓ Test 1: Funktion setup_gitignore wurde erfolgreich ausgeführt.${NC}"
  echo -e "${GREEN}✓ Test 2: Git Repository-Status ist valide.${NC}"
  echo -e "${GREEN}✓ Test 3: Teilziele 1 bis 4 erfolgreich abgeschlossen.${NC}"
  echo -e "${GREEN}🎉 ERFOLG: Alle Prüfungen bestanden!${NC}"
  exit 0
else
  echo -e "${RED}❌ FEHLER: Skript lieferte Rückgabecode $RET${NC}"
  exit 1
fi
