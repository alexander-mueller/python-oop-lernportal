#!/usr/bin/env bash
# ==============================================================================
# 🐧 BASH 06: MUSTERLÖSUNG
# ==============================================================================

summiere_zahlen_array() {
  local summe=0
  for z in "$@"; do
    summe=$(( summe + z ))
  done
  echo "$summe"
}

lese_csv_zeilenweise() {
  local csv_text="$1"
  local spalten_nr="$2"
  local idx=$(( spalten_nr - 1 ))

  while IFS=',' read -r -a felder; do
    # Überspringe leere Zeilen
    [[ ${#felder[@]} -eq 0 ]] && continue
    echo "${felder[$idx]}"
  done <<< "$csv_text"
}

verwalte_server_hashmap() {
  local aktion="$1"
  local key="$2"
  local wert="$3"

  declare -A server_map=(
    ["gateway"]="10.0.0.1"
    ["database"]="10.0.0.2"
    ["cache"]="10.0.0.3"
  )

  case "$aktion" in
    get)
      echo "${server_map[$key]}"
      ;;
    set)
      server_map["$key"]="$wert"
      echo "$key=${server_map[$key]}"
      ;;
    keys)
      echo "${!server_map[@]}" | tr ' ' '\n' | sort | tr '\n' ' ' | sed 's/ $//'
      echo
      ;;
  esac
}

zaehle_element_haeufigkeit() {
  declare -A counter

  for item in "$@"; do
    ((counter["$item"]++))
  done

  for k in $(printf "%s\n" "${!counter[@]}" | sort); do
    echo "$k: ${counter[$k]}"
  done
}

parse_cli_flags() {
  local env="production"
  local port=8080
  local verbose="false"
  local OPTIND=1

  while getopts ":e:p:v" opt; do
    case "$opt" in
      e) env="$OPTARG" ;;
      p) port="$OPTARG" ;;
      v) verbose="true" ;;
      *) ;;
    esac
  done

  echo "ENV=$env,PORT=$port,VERBOSE=$verbose"
}
