#!/usr/bin/env bash
# ==============================================================================
# 🐧 BASH 03: VARIABLEN, ENVIRONMENT, EXPANSION & ARITHMETIK
# ==============================================================================

# 🎯 TEILZIEL 1 (TODO 1): Exportiere eine Umgebungsvariable dynamisch.
# Setze und exportiere "$1" mit dem Wert "$2" und gib den String "$1=$2" auf stdout aus.
setze_umgebungsvariable() {
  local name="$1"
  local wert="$2"
  # TODO: Exportiere die Variable und gib "NAME=WERT" aus
  return 0
}

# 🎯 TEILZIEL 2 (TODO 2): Nutze Command Substitution $(...) für eine System-Kennung.
# Kombiniere $(whoami), $(hostname) und $(date +%Y-%m) im Format:
# "USER@HOST_YYYY-MM"
generiere_system_kennung() {
  # TODO: Erzeuge und gib die Kennung per Command Substitution $(...) aus
  return 0
}

# 🎯 TEILZIEL 3 (TODO 3): Dateipfad mit reiner Bash Parameter Expansion zerlegen.
# Extrahiere aus "$1" (z.B. "/var/log/nginx/access.log"):
# - Verzeichnis (DIR): z.B. /var/log/nginx
# - Dateiname (FILE): z.B. access.log
# - Endung (EXT): z.B. log
# - Basisname ohne Endung (BASE): z.B. access
# Ausgabeformat: "DIR: <dir> | FILE: <file> | EXT: <ext> | BASE: <base>"
# ⚠️ WICHTIG: Verwende keine externen Tools (kein basename, dirname, sed, awk)!
zerlege_dateipfad() {
  local voller_pfad="$1"
  # TODO: Nutze ${pfad%/*}, ${pfad##*/}, ${datei##*.}, ${datei%.*}
  return 0
}

# 🎯 TEILZIEL 4 (TODO 4): Parameter Expansion mit Standardwerten (${var:-default}).
# Gib "$1" zurück. Wenn "$1" leer oder nicht gesetzt ist, gib "$2" (Fallback) zurück.
ermittle_konfigurationswert() {
  local wert="$1"
  local fallback="$2"
  # TODO: Nutze Parameter Expansion mit Default-Wert
  return 0
}

# 🎯 TEILZIEL 5 (TODO 5): Quota-Berechnung mit Shell-Arithmetik $(( ... )).
# Berechne aus "$1" (total_mb) und "$2" (used_mb):
# - freier Speicher: total_mb - used_mb
# - Prozentuale Belegung (Ganzzahl): (used_mb * 100) / total_mb
# Ausgabeformat: "TOTAL: <total>MB, USED: <used>MB (<prozent>%), FREE: <free>MB"
berechne_disk_quota() {
  local total_mb="$1"
  local used_mb="$2"
  # TODO: Berechne freie MB und Prozent per $(( ... ))
  return 0
}
