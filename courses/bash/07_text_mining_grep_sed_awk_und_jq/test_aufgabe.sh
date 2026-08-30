#!/usr/bin/env bash
# ==============================================================================
# 🧪 BATS-INSPIRIERTE TESTSUITE: BASH 07 - TEXT-MINING (GREP, SED, AWK & JQ)
# ==============================================================================

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

TARGET_SCRIPT="${1:-aufgabe.sh}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# JQ Emulation Fallback falls jq nicht systemweit installiert ist
if ! command -v jq >/dev/null 2>&1; then
  jq() {
    python3 -c '
import sys, json

args = sys.argv[1:]
query = [a for a in args if not a.startswith("-")][0] if any(not a.startswith("-") for a in args) else "."
data = json.load(sys.stdin)

if "active == true" in query:
    for item in data:
        if item.get("active") is True:
            print(item.get("username", ""))
elif "hostname" in query:
    for item in data:
        print("%s,%s,%s" % (item.get("hostname"), item.get("ip"), item.get("status")))
elif query == ".":
    print(json.dumps(data, indent=2))
' "$@"
  }
  export -f jq 2>/dev/null || true
fi

TOTAL_TESTS=0
PASSED_TESTS=0
FAILED_TESTS=0

echo -e "${BLUE}================================================================${NC}"
echo -e "${BLUE}🧪 TESTSUITE: Bash 07 - Text-Mining mit grep, sed, awk & jq${NC}"
echo -e "${BLUE}   Ziel-Skript: ${YELLOW}${TARGET_SCRIPT}${NC}"
echo -e "${BLUE}================================================================${NC}\n"

if [ ! -f "$SCRIPT_DIR/$TARGET_SCRIPT" ]; then
  echo -e "${RED}❌ Fehler: Datei '$TARGET_SCRIPT' nicht gefunden!${NC}"
  exit 1
fi

source "$SCRIPT_DIR/$TARGET_SCRIPT"

run_test() {
  local test_name="$1"
  local test_cmd="$2"
  ((TOTAL_TESTS++))

  echo -e "▶ Test ${TOTAL_TESTS}: ${test_name}"
  if eval "$test_cmd"; then
    echo -e "  ${GREEN}✓ BESTANDEN${NC}\n"
    ((PASSED_TESTS++))
  else
    echo -e "  ${RED}✗ FEHLGESCHLAGEN${NC}\n"
    ((FAILED_TESTS++))
  fi
}

# TEST: Teilziel 1 - extrahiere_fehler_logs
run_test "Fehler-Logs mit grep filtern und Debug ignorieren" '
  LOGS="2026-08-30 [INFO] System gestartet
2026-08-30 [ERROR] Datenbank nicht erreichbar
2026-08-30 [DEBUG] ERROR 404 in debug context
2026-08-30 [CRITICAL] Out of Memory Exception"
  RES=$(extrahiere_fehler_logs "$LOGS")
  [ "$(echo "$RES" | wc -l)" -eq 2 ] && \
  echo "$RES" | grep -q "Datenbank nicht erreichbar" && \
  echo "$RES" | grep -q "Out of Memory Exception" && \
  ! echo "$RES" | grep -q "debug context"
'

# TEST: Teilziel 2 - maskiere_passwoerter_sed
run_test "Passwoerter und API-Keys mit sed maskieren" '
  CONF="db_user=\"admin\" password=\"SuperSecret123!\"
api_key=\"sk-live-999abc\" timeout=30"
  MASKED=$(maskiere_passwoerter_sed "$CONF")
  echo "$MASKED" | grep -q "password=\"\*\*\*REDACTED\*\*\*\"" && \
  echo "$MASKED" | grep -q "api_key=\"\*\*\*REDACTED\*\*\*\"" && \
  ! echo "$MASKED" | grep -q "SuperSecret" && \
  ! echo "$MASKED" | grep -q "sk-live-999abc"
'

# TEST: Teilziel 3 - berechne_weblog_traffic_awk
run_test "Weblog-Statistiken mit awk aggregieren" '
  ACCESS="192.168.1.1 - - [30/Aug/2026:12:00:01] \"GET /api/v1 HTTP/1.1\" 200 1000
192.168.1.2 - - [30/Aug/2026:12:00:02] \"GET /index.html HTTP/1.1\" 200 2000
192.168.1.3 - - [30/Aug/2026:12:00:03] \"GET /style.css HTTP/1.1\" 200 3000"
  STAT=$(berechne_weblog_traffic_awk "$ACCESS")
  [ "$STAT" = "REQUESTS: 3, BYTES: 6000, AVG: 2000" ]
'

# TEST: Teilziel 4 - filtere_aktive_benutzer_jq
run_test "Aktive Benutzer aus JSON mit jq extrahieren" '
  JSON="[
    {\"username\": \"alice\", \"active\": true},
    {\"username\": \"bob\", \"active\": false},
    {\"username\": \"charlie\", \"active\": true}
  ]"
  ACTIVE=$(filtere_aktive_benutzer_jq "$JSON")
  [ "$(echo "$ACTIVE" | xargs)" = "alice charlie" ]
'

# TEST: Teilziel 5 - transformiere_server_json_zu_csv
run_test "JSON-Serverliste in CSV umwandeln mit jq" '
  SERVERS="[
    {\"hostname\": \"srv-web1\", \"ip\": \"10.0.1.10\", \"status\": \"running\"},
    {\"hostname\": \"srv-db1\", \"ip\": \"10.0.2.20\", \"status\": \"standby\"}
  ]"
  CSV=$(transformiere_server_json_zu_csv "$SERVERS")
  LINE1=$(echo "$CSV" | head -n 1)
  LINE2=$(echo "$CSV" | tail -n 1)
  [ "$LINE1" = "srv-web1,10.0.1.10,running" ] && \
  [ "$LINE2" = "srv-db1,10.0.2.20,standby" ]
'

echo -e "${BLUE}================================================================${NC}"
if [ "$FAILED_TESTS" -eq 0 ]; then
  echo -e "${GREEN}🎉 ERFOLG: Alle ${PASSED_TESTS}/${TOTAL_TESTS} Tests in Bash 07 erfolgreich bestanden!${NC}"
  echo -e "${BLUE}================================================================${NC}"
  exit 0
else
  echo -e "${RED}❌ FEHLER: ${FAILED_TESTS} von ${TOTAL_TESTS} Tests fehlgeschlagen.${NC}"
  echo -e "${BLUE}================================================================${NC}"
  exit 1
fi
