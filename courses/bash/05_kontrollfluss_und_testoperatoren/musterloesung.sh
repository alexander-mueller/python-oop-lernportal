#!/usr/bin/env bash
# ==============================================================================
# 🐧 BASH 05: MUSTERLÖSUNG
# ==============================================================================

analysiere_pfad_status() {
  local pfad="$1"
  if [[ ! -e "$pfad" ]]; then
    echo "NOT_FOUND"
  elif [[ -d "$pfad" ]]; then
    echo "DIRECTORY"
  elif [[ -f "$pfad" && -x "$pfad" ]]; then
    echo "EXECUTABLE_FILE"
  elif [[ -f "$pfad" ]]; then
    echo "REGULAR_FILE"
  else
    echo "OTHER"
  fi
}

validiere_ipv4_format() {
  local ip="$1"
  if [[ $ip =~ ^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$ ]]; then
    local o1="${BASH_REMATCH[1]}"
    local o2="${BASH_REMATCH[2]}"
    local o3="${BASH_REMATCH[3]}"
    local o4="${BASH_REMATCH[4]}"

    if (( o1 <= 255 && o2 <= 255 && o3 <= 255 && o4 <= 255 )); then
      return 0
    fi
  fi
  return 1
}

bewerte_server_metrik() {
  local cpu="$1"
  local ram="$2"
  if (( cpu >= 90 || ram >= 90 )); then
    echo "CRITICAL"
  elif (( cpu >= 75 || ram >= 75 )); then
    echo "WARNING"
  else
    echo "OK"
  fi
}

service_dispatcher() {
  local aktion="$1"
  local service_name="$2"

  case "$aktion" in
    start)
      echo "Starte $service_name..."
      ;;
    stop)
      echo "Stoppe $service_name..."
      ;;
    restart|reload)
      echo "Starte $service_name neu..."
      ;;
    status)
      echo "Pruefe Status von $service_name..."
      ;;
    *)
      echo "Unbekannte Aktion: $aktion"
      return 1
      ;;
  esac
}

fuehre_sicher_aus() {
  local befehl="$1"
  eval "$befehl" >/dev/null 2>&1
  local exit_code=$?

  if [[ $exit_code -eq 0 ]]; then
    echo "SUCCESS"
    return 0
  else
    echo "ERROR_CODE: $exit_code"
    return $exit_code
  fi
}
