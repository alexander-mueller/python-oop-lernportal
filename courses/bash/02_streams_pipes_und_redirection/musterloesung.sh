#!/usr/bin/env bash
# ==============================================================================
# 🐧 BASH 02: MUSTERLÖSUNG
# ==============================================================================

erstelle_system_bericht() {
  local ziel_datei="$1"
  local server_name="$2"
  local os_typ="$3"

  cat <<EOF > "$ziel_datei"
=== SYSTEM BERICHT ===
SERVER: $server_name
OS: $os_typ
STATUS: INITIALISIERT
======================
EOF
}

haenge_status_an() {
  local ziel_datei="$1"
  local status_meldung="$2"
  echo "[STATUS] $status_meldung" >> "$ziel_datei"
}

trenne_befehls_ausgabe() {
  local befehl="$1"
  local out_datei="$2"
  local err_datei="$3"
  eval "$befehl" > "$out_datei" 2> "$err_datei"
}

unterdruecke_fehler() {
  local befehl="$1"
  eval "$befehl" 2> /dev/null
}

pipe_und_tee_pipeline() {
  local eingabe_text="$1"
  local tee_datei="$2"
  printf "%s\n" "$eingabe_text" | grep -v '^#' | tr '[:lower:]' '[:upper:]' | tee "$tee_datei" | sort
}
