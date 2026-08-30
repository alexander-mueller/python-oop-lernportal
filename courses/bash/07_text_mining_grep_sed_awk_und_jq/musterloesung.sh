#!/usr/bin/env bash
# ==============================================================================
# 🐧 BASH 07: MUSTERLÖSUNG
# ==============================================================================

extrahiere_fehler_logs() {
  local log_text="$1"
  echo "$log_text" | grep -E -i '(error|critical|fatal)' | grep -v -i 'debug'
}

maskiere_passwoerter_sed() {
  local config_text="$1"
  echo "$config_text" | sed -E \
    -e 's/password="[^"]*"/password="***REDACTED***"/g' \
    -e 's/api_key="[^"]*"/api_key="***REDACTED***"/g'
}

berechne_weblog_traffic_awk() {
  local log_text="$1"
  echo "$log_text" | awk '
    NF >= 1 {
      sum += $NF
      count++
    }
    END {
      if (count > 0) {
        avg = int(sum / count)
        print "REQUESTS: " count ", BYTES: " sum ", AVG: " avg
      }
    }
  '
}

filtere_aktive_benutzer_jq() {
  local json_text="$1"
  echo "$json_text" | jq -r '.[] | select(.active == true) | .username'
}

transformiere_server_json_zu_csv() {
  local json_text="$1"
  echo "$json_text" | jq -r '.[] | "\(.hostname),\(.ip),\(.status)"'
}
