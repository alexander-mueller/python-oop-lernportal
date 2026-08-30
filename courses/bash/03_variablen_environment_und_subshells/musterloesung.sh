#!/usr/bin/env bash
# ==============================================================================
# 🐧 BASH 03: MUSTERLÖSUNG
# ==============================================================================

setze_umgebungsvariable() {
  local name="$1"
  local wert="$2"
  export "$name"="$wert"
  echo "$name=$wert"
}

generiere_system_kennung() {
  local u h d
  u=$(whoami)
  h=$(hostname)
  d=$(date +%Y-%m)
  echo "${u}@${h}_${d}"
}

zerlege_dateipfad() {
  local voller_pfad="$1"
  local verzeichnis="${voller_pfad%/*}"
  local dateiname="${voller_pfad##*/}"
  local extension="${dateiname##*.}"
  local basisname="${dateiname%.*}"
  echo "DIR: $verzeichnis | FILE: $dateiname | EXT: $extension | BASE: $basisname"
}

ermittle_konfigurationswert() {
  local wert="$1"
  local fallback="$2"
  echo "${wert:-$fallback}"
}

berechne_disk_quota() {
  local total_mb="$1"
  local used_mb="$2"
  local free_mb=$(( total_mb - used_mb ))
  local prozent=$(( (used_mb * 100) / total_mb ))
  echo "TOTAL: ${total_mb}MB, USED: ${used_mb}MB (${prozent}%), FREE: ${free_mb}MB"
}
