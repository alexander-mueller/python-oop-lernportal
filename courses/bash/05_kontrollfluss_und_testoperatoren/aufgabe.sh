#!/usr/bin/env bash
# ==============================================================================
# 🐧 BASH 05: KONTROLLFLUSS, TEST-OPERATOREN & REGEX-MATCHING
# ==============================================================================

# 🎯 TEILZIEL 1 (TODO 1): Dateityp & Berechtigungs-Prüfung mit [[ ... ]].
# Prüfe "$1":
# - Nicht existent -> "NOT_FOUND"
# - Ist Verzeichnis (-d) -> "DIRECTORY"
# - Ist reguläre Datei (-f) UND ausführbar (-x) -> "EXECUTABLE_FILE"
# - Ist reguläre Datei (-f) und NICHT ausführbar -> "REGULAR_FILE"
# - Sonst -> "OTHER"
analysiere_pfad_status() {
  local pfad="$1"
  # TODO: Prüfe den Pfad mit [[ ... ]] und -d, -f, -x, -e
  return 0
}

# 🎯 TEILZIEL 2 (TODO 2): IPv4-Validierung mit Regex `=~` und BASH_REMATCH.
# Prüfe per Regex, ob "$1" aus 4 Oktetten besteht und jedes Oktett zwischen 0 und 255 liegt.
# Gib Return-Code 0 (Erfolg) zurück wenn gültig, sonst 1.
validiere_ipv4_format() {
  local ip="$1"
  # TODO: Validiere IPv4 mit [[ $ip =~ ... ]] und prüfe Zahlenbereich
  return 0
}

# 🎯 TEILZIEL 3 (TODO 3): Schwellenwert-Logik mit numerischen Operatoren (-ge, -gt).
# Prüfe "$1" (CPU%) und "$2" (RAM%):
# - CPU >= 90 ODER RAM >= 90 -> "CRITICAL"
# - CPU >= 75 ODER RAM >= 75 -> "WARNING"
# - Sonst -> "OK"
bewerte_server_metrik() {
  local cpu="$1"
  local ram="$2"
  # TODO: Implementiere Schwellenwertvergleich mit if [[ ... ]]
  return 0
}

# 🎯 TEILZIEL 4 (TODO 4): Befehls-Dispatcher mit `case ... in ... esac`.
# Behandle "$1" (Aktion) für Dienst "$2" (Service-Name):
# - "start"           -> "Starte $service_name..."
# - "stop"            -> "Stoppe $service_name..."
# - "restart"|"reload"-> "Starte $service_name neu..."
# - "status"          -> "Pruefe Status von $service_name..."
# - Alles andere (*)  -> "Unbekannte Aktion: $aktion" (und Return-Code 1)
service_dispatcher() {
  local aktion="$1"
  local service_name="$2"
  # TODO: Implementiere case-Verzweigung
  return 0
}

# 🎯 TEILZIEL 5 (TODO 5): Befehlsausführung mit Exit-Code Überprüfung ($?).
# Führe "$1" per eval aus:
# - Wenn Exit-Code == 0: Gib "SUCCESS" aus und beende mit Return 0
# - Wenn Exit-Code != 0: Gib "ERROR_CODE: $?" aus und gib den konkreten Exit-Code als Return zurück.
fuehre_sicher_aus() {
  local befehl="$1"
  # TODO: Führe Befehl aus, fange $? ab und bewerte
  return 0
}
