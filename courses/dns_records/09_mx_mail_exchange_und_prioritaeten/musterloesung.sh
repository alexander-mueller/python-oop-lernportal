#!/usr/bin/env bash
# ==============================================================================
# MUSTERLÖSUNG: DNS 09: MX-RECORDS & PRIORITÄTS-ROUTING
# ==============================================================================

format_mx_record() {
  local zone="$1"
  local prio="$2"
  local mhost="$3"
  local ttl="${4:-86400}"

  if [[ ! "$prio" =~ ^[0-9]+$ ]]; then
    echo "ERROR: Priorität muss Ganzzahl >= 0 sein"
    return 1
  fi

  [[ "$mhost" != *. ]] && mhost="${mhost}."

  printf "%-15s %-7s IN  MX  %-5s %s\n" "$zone" "$ttl" "$prio" "$mhost"
  return 0
}

sort_mx_records() {
  local mfile="$1"
  [ ! -f "$mfile" ] && return 1

  # Finde Zeilen mit MX
  # Format typischerweise: zone ttl IN MX prio host
  awk '$3 == "MX" || $4 == "MX" {
    for (i=1; i<=NF; i++) {
      if ($i == "MX") {
        prio = $(i+1)
        host = $(i+2)
        print prio, host
      }
    }
  }' "$mfile" | sort -n -k1,1 | while read -r p h; do
    echo "PRIO=$p | HOST=$h"
  done
  return 0
}

validate_mx_target_type() {
  local rtype=$(echo "$1" | tr '[:lower:]' '[:upper:]')

  if [ "$rtype" = "CNAME" ]; then
    echo "ERROR_RFC2181: MX-Ziel darf NIEMALS ein CNAME sein! Muss A oder AAAA sein."
    return 1
  elif [ "$rtype" = "A" ] || [ "$rtype" = "AAAA" ]; then
    echo "VALID_MX_TARGET: Ziel verweist direkt auf A/AAAA IP-Adresse."
    return 0
  else
    echo "UNKNOWN_TYPE"
    return 1
  fi
}

generate_redundant_mx_setup() {
  local zone="$1"
  local prim="$2"
  local bak="$3"
  local ttl="${4:-86400}"

  format_mx_record "$zone" 10 "$prim" "$ttl"
  format_mx_record "$zone" 20 "$bak" "$ttl"
  return 0
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  format_mx_record "$@"
fi
