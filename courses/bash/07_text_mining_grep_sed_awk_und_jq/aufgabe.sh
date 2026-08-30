#!/usr/bin/env bash
# ==============================================================================
# 🐧 BASH 07: TEXT-MINING MIT GREP, SED, AWK & JQ
# ==============================================================================

# 🎯 TEILZIEL 1 (TODO 1): Fehler-Logs mit `grep` extrahieren.
# Filtere aus "$1" alle Zeilen, die "ERROR", "CRITICAL" oder "FATAL" enthalten (Case-Insensitive -i, Extended Regex -E),
# schließe jedoch Zeilen aus, die das Wort "DEBUG" enthalten (-v).
extrahiere_fehler_logs() {
  local log_text="$1"
  # TODO: Verwende grep -E -i und grep -v -i
  return 0
}

# 🎯 TEILZIEL 2 (TODO 2): Sensible Daten mit `sed` maskieren.
# Ersetze in "$1" per sed -E:
# - password="<beliebig>" durch password="***REDACTED***"
# - api_key="<beliebig>"  durch api_key="***REDACTED***"
maskiere_passwoerter_sed() {
  local config_text="$1"
  # TODO: Nutze sed -E 's/.../.../g'
  return 0
}

# 🎯 TEILZIEL 3 (TODO 3): Weblog Traffic-Statistik mit `awk` aggregieren.
# Format jeder Zeile in "$1":
# 192.168.1.1 - - [30/Aug/2026:12:00:00] "GET /index.html HTTP/1.1" 200 4500
# Das letzte Feld ($NF) enthält die übertragenen Bytes.
# Berechne:
# - Anzahl Requests (count)
# - Gesamt-Bytes (sum)
# - Durchschnittliche Bytes pro Request (avg = int(sum / count))
# Ausgabeformat: "REQUESTS: <count>, BYTES: <sum>, AVG: <avg>"
berechne_weblog_traffic_awk() {
  local log_text="$1"
  # TODO: Verwende awk '{ sum += $NF; count++ } END { ... }'
  return 0
}

# 🎯 TEILZIEL 4 (TODO 4): Aktive Benutzer mit `jq` filtern.
# Filtere aus dem JSON-Array "$1" alle Objekte mit `.active == true` und gib deren `.username` aus.
# Tipp (jq): echo "$json_text" | jq -r '.[] | select(.active == true) | .username'
filtere_aktive_benutzer_jq() {
  local json_text="$1"
  # TODO: Verwende jq '.[] | select(.active == true) | .username'
  return 0
}

# 🎯 TEILZIEL 5 (TODO 5): JSON in CSV transformieren mit `jq`.
# Wandle das JSON-Array "$1" (Objekte mit hostname, ip, status) in kommagetrennte CSV-Zeilen um:
# Format: <hostname>,<ip>,<status>
# Tipp (jq): echo "$json_text" | jq -r '.[] | "\(.hostname),\(.ip),\(.status)"'
transformiere_server_json_zu_csv() {
  local json_text="$1"
  # TODO: Verwende jq '.[] | "\(.hostname),\(.ip),\(.status)"'
  return 0
}
