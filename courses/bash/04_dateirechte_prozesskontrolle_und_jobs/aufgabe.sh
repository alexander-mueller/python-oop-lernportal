#!/usr/bin/env bash
# ==============================================================================
# 🐧 BASH 04: DATEIRECHTE (CHMOD), PROZESSKONTROLLE & JOB CONTROL
# ==============================================================================

# 🎯 TEILZIEL 1 (TODO 1): Setze Dateirechte mit `chmod` basierend auf dem Zweck.
# - Wenn "$2" == "secret" -> chmod 600 "$1" und gib "600" aus
# - Wenn "$2" == "script" -> chmod 755 "$1" und gib "755" aus
# - Wenn "$2" == "config" -> chmod 644 "$1" und gib "644" aus
# - Sonst -> chmod 644 "$1" und gib "644" aus
setze_sichere_rechte() {
  local datei="$1"
  local modus_typ="$2"
  # TODO: Setze Rechte per chmod und gib den Oktalwert aus
  return 0
}

# 🎯 TEILZIEL 2 (TODO 2): Lese die Dateirechte als 3-stellige Oktalzahl aus.
# Nutze `stat -c "%a" "$1"` und gib den Wert aus (z.B. "755").
lese_oktal_rechte() {
  local datei="$1"
  # TODO: Lese Oktalrechte per stat aus
  return 0
}

# 🎯 TEILZIEL 3 (TODO 3): Starte einen Prozess im Hintergrund mit `&`.
# Starte `sleep "$1" &`, ermittle die Prozess-ID mit `$!` und gib die PID aus.
starte_hintergrund_prozess() {
  local dauer_sek="$1"
  # TODO: Starte sleep im Hintergrund und gib $! zurück
  return 0
}

# 🎯 TEILZIEL 4 (TODO 4): Prüfe, ob eine PID noch aktiv ist (Signal 0).
# Nutze `kill -0 "$1" 2>/dev/null`.
# Gib Return-Code 0 zurück, wenn der Prozess läuft, sonst 1.
ist_prozess_am_leben() {
  local pid="$1"
  # TODO: Prüfe Prozess-Existenz mit kill -0
  return 0
}

# 🎯 TEILZIEL 5 (TODO 5): Beende einen Prozess sanft (SIGTERM 15) mit Fallback (SIGKILL 9).
# 1. Sende `kill -15 "$1"` (SIGTERM)
# 2. Warte kurz (sleep 0.1)
# 3. Wenn Prozess immer noch lebt (kill -0), sende `kill -9 "$1"` (SIGKILL)
# Gib 0 zurück.
stoppe_prozess_mit_fallback() {
  local pid="$1"
  # TODO: Sende Signal 15, prüfe und sende bei Bedarf Signal 9
  return 0
}
