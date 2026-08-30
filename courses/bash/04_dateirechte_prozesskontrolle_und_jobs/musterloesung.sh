#!/usr/bin/env bash
# ==============================================================================
# 🐧 BASH 04: MUSTERLÖSUNG
# ==============================================================================

setze_sichere_rechte() {
  local datei="$1"
  local modus_typ="$2"
  local octal="644"

  case "$modus_typ" in
    secret)
      octal="600"
      ;;
    script)
      octal="755"
      ;;
    config|*)
      octal="644"
      ;;
  esac

  chmod "$octal" "$datei"
  echo "$octal"
}

lese_oktal_rechte() {
  local datei="$1"
  stat -c "%a" "$datei" 2>/dev/null || stat -f "%OLp" "$datei" 2>/dev/null
}

starte_hintergrund_prozess() {
  local dauer_sek="$1"
  sleep "$dauer_sek" &
  echo $!
}

ist_prozess_am_leben() {
  local pid="$1"
  kill -0 "$pid" 2>/dev/null
}

stoppe_prozess_mit_fallback() {
  local pid="$1"
  kill -15 "$pid" 2>/dev/null || true
  sleep 0.1
  if kill -0 "$pid" 2>/dev/null; then
    kill -9 "$pid" 2>/dev/null || true
  fi
  return 0
}
