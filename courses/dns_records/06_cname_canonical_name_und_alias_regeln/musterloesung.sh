#!/usr/bin/env bash
# ==============================================================================
# MUSTERLÖSUNG: DNS 06: CNAME (CANONICAL NAME) & DAS ZONE-APEX PROBLEM
# ==============================================================================

format_cname_record() {
  local alias="$1"
  local target="$2"
  local ttl="${3:-3600}"

  [ -z "$alias" ] || [ -z "$target" ] && return 1

  # Schlusspunkt garantieren
  if [[ "$target" != *. ]]; then
    target="${target}."
  fi

  printf "%-15s %-7s IN  CNAME %s\n" "$alias" "$ttl" "$target"
  return 0
}

validate_apex_cname_rule() {
  local node="$1"
  local rtype=$(echo "$2" | tr '[:lower:]' '[:upper:]')

  if [ "$rtype" = "CNAME" ]; then
    if [ "$node" = "@" ] || [ "$node" = "" ]; then
      echo "ERROR_APEX_VIOLATION: CNAME am Zone-Apex verboten! Kollidiert mit SOA und NS Records."
      return 1
    fi
  fi

  echo "VALID: CNAME auf Subdomain erlaubt."
  return 0
}

detect_cname_collisions() {
  local zfile="$1"
  [ ! -f "$zfile" ] && return 1

  local cnames=($(awk '$3 == "CNAME" || $4 == "CNAME" { print $1 }' "$zfile"))
  local collisions=()

  for c in "${cnames[@]}"; do
    local other_count=$(awk -v host="$c" '($1 == host) && ($3 != "CNAME" && $4 != "CNAME") { count++ } END { print count+0 }' "$zfile")
    if [ "$other_count" -gt 0 ]; then
      collisions+=("$c")
    fi
  done

  if [ ${#collisions[@]} -gt 0 ]; then
    echo "CNAME_COLLISION_FOUND: Node '${collisions[0]}' besitzt unerlaubt CNAME und weitere Records!"
    return 1
  else
    echo "CNAME_INTEGRITY_OK: Keine Koexistenz-Konflikte gefunden."
    return 0
  fi
}

trace_cname_chain() {
  local curr="$1"
  local map="$2"
  [ ! -f "$map" ] && return 1

  local path=("$curr")
  local visited=("$curr")

  while true; do
    local next=$(awk -v k="$curr" '$1 == k { print $2 }' "$map")
    if [ -z "$next" ]; then
      # Ende der Kette erreicht
      local out=""
      for p in "${path[@]}"; do
        if [ -z "$out" ]; then out="$p"; else out="$out -> $p"; fi
      done
      echo "RESOLVED: $out"
      return 0
    fi

    # Prüfe auf Loop
    for v in "${visited[@]}"; do
      if [ "$v" = "$next" ]; then
        echo "ERROR_LOOP_DETECTED: Zirkuläre CNAME-Referenz bei '$next'!"
        return 1
      fi
    done

    visited+=("$next")
    path+=("$next")
    curr="$next"
  done
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  format_cname_record "$@"
fi
