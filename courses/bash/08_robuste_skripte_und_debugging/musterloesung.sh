#!/usr/bin/env bash
# ==============================================================================
# 🐧 BASH 08: MUSTERLÖSUNG
# ==============================================================================

aktiviere_strict_mode() {
  set -euo pipefail
  echo "STRICT_MODE_ON"
}

devops_logger() {
  local level="$1"
  local meldung="$2"
  local timestamp
  timestamp="$(date +'%Y-%m-%d %H:%M:%S')"
  local log_line="[$timestamp] [$level] $meldung"

  case "$level" in
    ERROR|FATAL)
      echo "$log_line" >&2
      ;;
    *)
      echo "$log_line"
      ;;
  esac
}

erstelle_temp_verzeichnis_mit_cleanup() {
  local temp_dir
  temp_dir=$(mktemp -d /tmp/devops_XXXXXX)
  trap 'rm -rf "$temp_dir"' EXIT
  echo "$temp_dir"
}

fuehre_exklusiv_mit_lock_aus() {
  local lock_file="$1"
  local befehl="$2"

  if flock -n "$lock_file" -c "$befehl"; then
    return 0
  else
    echo "RESOURCE_LOCKED" >&2
    return 1
  fi
}

debug_trace_ausfuehren() {
  local befehl="$1"
  set -x
  eval "$befehl"
  { set +x; } 2>/dev/null
}
