#!/usr/bin/env bash
# ==============================================================================
# 🐧 BASH 06: SCHLEIFEN, ARRAYS, ASSOZIATIVE HASHMAPS & GETOPTS
# ==============================================================================

# 🎯 TEILZIEL 1 (TODO 1): Summiere alle übergebenen Zahlen mit einer for-Schleife.
# Iteriere über "$@" und berechne die Summe.
summiere_zahlen_array() {
  local summe=0
  # TODO: Iteriere über alle Argumente mit for
  echo "$summe"
}

# 🎯 TEILZIEL 2 (TODO 2): CSV zeilenweise mit while read einlesen.
# Lies den String "$1" zeilenweise ein (IFS=',') und gib für jede Zeile die Spalte "$2" (1-basiert) aus.
lese_csv_zeilenweise() {
  local csv_text="$1"
  local spalten_nr="$2"
  # TODO: Verwende while IFS=',' read -r -a felder
  return 0
}

# 🎯 TEILZIEL 3 (TODO 3): Assoziatives Array (declare -A) für Server-Mapping.
# Verwalte eine Map mit: gateway=10.0.0.1, database=10.0.0.2, cache=10.0.0.3
# - Wenn "$1" == "get" -> Gib IP für Key "$2" aus
# - Wenn "$1" == "set" -> Setze Key "$2" auf "$3" und gib "$2=$3" aus
# - Wenn "$1" == "keys" -> Gib alle Schlüssel sortiert (einzelne Zeile, leerzeichengetrennt) aus
verwalte_server_hashmap() {
  local aktion="$1"
  local key="$2"
  local wert="$3"
  # TODO: Nutze declare -A
  return 0
}

# 🎯 TEILZIEL 4 (TODO 4): Zähle Häufigkeiten von Elementen mit assoziativer Map.
# Nimm alle übergebenen Argumente ("$@"), zähle ihre Vorkommen mit `declare -A counter`
# und gib die Ergebnisse zeilenweise formatiert als `element: anzahl` (alphabetisch sortiert) aus.
zaehle_element_haeufigkeit() {
  # TODO: Zähle Vorkommen und gib sortiert aus
  return 0
}

# 🎯 TEILZIEL 5 (TODO 5): Parse CLI-Flags mit getopts.
# Parameter:
# -e <env>   -> Umgebung (Standard: production)
# -p <port>  -> Portnummer (Standard: 8080)
# -v         -> Verbose Flag (Standard: false, wenn -v gesetzt: true)
# Ausgabeformat: "ENV=<env>,PORT=<port>,VERBOSE=<verbose>"
parse_cli_flags() {
  # TODO: Verwende getopts ":e:p:v" opt
  return 0
}
