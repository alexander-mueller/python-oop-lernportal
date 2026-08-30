#!/usr/bin/env bash
# ==============================================================================
# 🐧 BASH 02: I/O STREAMS, PIPES & REDIRECTION
# ==============================================================================

# 🎯 TEILZIEL 1 (TODO 1): Erstelle einen System-Bericht per Here-Doc (`<<EOF`) und `>`.
# Schreibe in "$1" folgenden Block (Ersetze "$2" für Server und "$3" für OS):
# === SYSTEM BERICHT ===
# SERVER: <server_name>
# OS: <os_typ>
# STATUS: INITIALISIERT
# ======================
erstelle_system_bericht() {
  local ziel_datei="$1"
  local server_name="$2"
  local os_typ="$3"
  # TODO: Erstelle Bericht mit Here-Doc und Redirection (>)
  return 0
}

# 🎯 TEILZIEL 2 (TODO 2): Hänge Statusmeldungen mit `>>` an eine bestehende Datei an.
# Formatiere die Ausgabe als: `[STATUS] <status_meldung>`
haenge_status_an() {
  local ziel_datei="$1"
  local status_meldung="$2"
  # TODO: Hänge Meldung mit >> an
  return 0
}

# 🎯 TEILZIEL 3 (TODO 3): Führe einen Befehl aus und trenne stdout (1>) und stderr (2>).
# Führe `$1` mit eval oder bash -c aus und leite stdout nach "$2" und stderr nach "$3" um.
trenne_befehls_ausgabe() {
  local befehl="$1"
  local out_datei="$2"
  local err_datei="$3"
  # TODO: Führe Befehl aus mit getrennten Streams (1> und 2>)
  return 0
}

# 🎯 TEILZIEL 4 (TODO 4): Führe einen Befehl aus und unterdrücke Fehlermeldungen (2> /dev/null).
# stderr soll nach /dev/null umgeleitet werden, stdout soll ganz normal ausgegeben werden.
unterdruecke_fehler() {
  local befehl="$1"
  # TODO: Führe befehl aus, leite stderr nach /dev/null
  return 0
}

# 🎯 TEILZIEL 5 (TODO 5): Baue eine Stream-Pipeline mit Filterung, Großschreibung, `tee` und `sort`.
# 1. Nimm $1 als Eingabestrom
# 2. Filtere Kommentarzeilen heraus, die mit '#' beginnen (grep -v '^#')
# 3. Wandle alles in Großbuchstaben um (tr '[:lower:]' '[:upper:]')
# 4. Speichere das Zwischenergebnis mit `tee "$2"` in die Logdatei
# 5. Gib das Endergebnis alphabetisch sortiert (`sort`) auf stdout aus.
pipe_und_tee_pipeline() {
  local eingabe_text="$1"
  local tee_datei="$2"
  # TODO: Implementiere die Pipeline mit |, tee und sort
  return 0
}
