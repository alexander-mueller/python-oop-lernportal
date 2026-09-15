#!/usr/bin/env bash
# ==============================================================================
# MUSTERLÖSUNG: DNS 01: DNS-HIERARCHIE, FQDN-STRUKTUR & ROOT-SERVER
# ==============================================================================

parse_fqdn() {
  local raw="$1"
  [ -z "$raw" ] && return 1

  local has_root="NO"
  if [[ "$raw" == *. ]]; then
    has_root="YES"
  fi

  local clean="${raw%.}"
  IFS='.' read -ra labels <<< "$clean"
  local count=${#labels[@]}

  if [ "$count" -lt 2 ]; then
    echo "ERROR: Mindestens SLD und TLD erforderlich"
    return 1
  fi

  local host="${labels[0]}"
  local tld="${labels[-1]}"
  local sld="${labels[-2]}"
  
  local domain=""
  for (( i=1; i<count; i++ )); do
    if [ -z "$domain" ]; then
      domain="${labels[i]}"
    else
      domain="$domain.${labels[i]}"
    fi
  done

  echo "HOST=$host"
  echo "DOMAIN=$domain"
  echo "SLD=$sld"
  echo "TLD=$tld"
  echo "HAS_ROOT_DOT=$has_root"
  return 0
}

list_root_server() {
  local req="${1:-all}"
  req=$(echo "$req" | tr '[:upper:]' '[:lower:]')

  declare -A OPERATORS=(
    ["a"]="Verisign, Inc."
    ["b"]="University of Southern California"
    ["c"]="Cogent Communications"
    ["d"]="University of Maryland"
    ["e"]="NASA Ames Research Center"
    ["f"]="Internet Systems Consortium (ISC)"
    ["g"]="US Department of Defense"
    ["h"]="US Army Research Lab"
    ["i"]="Netnod"
    ["j"]="Verisign, Inc."
    ["k"]="RIPE NCC"
    ["l"]="ICANN"
    ["m"]="WIDE Project"
  )

  if [ "$req" = "all" ]; then
    for letter in a b c d e f g h i j k l m; do
      local u=$(echo "$letter" | tr '[:lower:]' '[:upper:]')
      echo "CLUSTER=$u | OPERATOR=${OPERATORS[$letter]} | HOST=${letter}.root-servers.net"
    done
    return 0
  fi

  if [[ -n "${OPERATORS[$req]}" ]]; then
    local u=$(echo "$req" | tr '[:lower:]' '[:upper:]')
    echo "CLUSTER=$u | OPERATOR=${OPERATORS[$req]} | HOST=${req}.root-servers.net"
    return 0
  else
    echo "ERROR: Ungültiger Cluster"
    return 1
  fi
}

build_delegation_path() {
  local domain="$1"
  [ -z "$domain" ] && return 1

  local clean="${domain%.}"
  IFS='.' read -ra labels <<< "$clean"
  local count=${#labels[@]}

  if [ "$count" -lt 2 ]; then
    echo "ERROR: Domain ungültig"
    return 1
  fi

  local tld="${labels[-1]}"
  local sld="${labels[-2]}"

  echo "[ROOT] . -> [TLD] ${tld}. -> [SLD] ${sld}.${tld}. -> [FQDN] ${clean}."
  return 0
}

validate_fqdn_syntax() {
  local raw="$1"
  local clean="${raw%.}"

  if [ ${#clean} -gt 253 ]; then
    echo "INVALID: Gesamtlänge überschreitet 253 Zeichen"
    return 1
  fi

  if [[ "$clean" =~ \.\. ]]; then
    echo "INVALID: Leeres Label gefunden (Doppelpunkt)"
    return 1
  fi

  IFS='.' read -ra labels <<< "$clean"
  for lbl in "${labels[@]}"; do
    if [ ${#lbl} -eq 0 ]; then
      echo "INVALID: Label darf nicht leer sein"
      return 1
    fi
    if [ ${#lbl} -gt 63 ]; then
      echo "INVALID: Label '${lbl}' überschreitet 63 Zeichen"
      return 1
    fi
    if [[ "$lbl" =~ ^- ]] || [[ "$lbl" =~ -$ ]]; then
      echo "INVALID: Bindestrich am Anfang oder Ende von '${lbl}' unzulässig"
      return 1
    fi
    if [[ ! "$lbl" =~ ^[a-zA-Z0-9-]+$ ]]; then
      echo "INVALID: Unerlaubte Zeichen in '${lbl}'"
      return 1
    fi
  done

  echo "VALID: ${raw}"
  return 0
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  parse_fqdn "$@"
fi
