#!/usr/bin/env bash
# ==============================================================================
# 🐧 BASH 01: TERMINAL-NAVIGATION, DATEIOPERATIONEN & GLOBBING
# ==============================================================================

# 🎯 TEILZIEL 1 (TODO 1): Erstelle mit `mkdir -p` eine verschachtelte Projektstruktur.
# Lege im Verzeichnis "$1" folgende Ordner an:
# - src/components
# - src/utils
# - docs/api
# - backup/logs
erstelle_projektstruktur() {
  local basis_dir="$1"
  # TODO: Erstelle die Ordnerstruktur mit mkdir -p
  return 0
}

# 🎯 TEILZIEL 2 (TODO 2): Erstelle mehrere Testdateien mit `touch` und Brace Expansion `{...}`.
# Erstelle im Verzeichnis "$1" folgende Dateien:
# - src/components/button.js
# - src/components/modal.js
# - src/utils/helper.js
# - docs/api/v1.md
# - docs/api/v2.md
# - app_dev.log
# - app_prod.log
# - config.yaml
erstelle_testdateien() {
  local basis_dir="$1"
  # TODO: Erstelle die Dateien
  return 0
}

# 🎯 TEILZIEL 3 (TODO 3): Kopiere Konfigurations- und Logdateien mit Globbing.
# Kopiere alle *.yaml und *.log Dateien aus Verzeichnis "$1" in das Backup-Verzeichnis "$2".
kopiere_konfigurationen() {
  local src_dir="$1"
  local backup_dir="$2"
  # TODO: Kopiere mit cp und Globbing
  return 0
}

# 🎯 TEILZIEL 4 (TODO 4): Verschiebe Dokumentationsdateien (*.md).
# Verschiebe alle *.md Dateien aus "$1/docs/api/" in das Archiv-Verzeichnis "$2".
verschiebe_dateien() {
  local src_dir="$1"
  local target_dir="$2"
  # TODO: Verschiebe mit mv
  return 0
}

# 🎯 TEILZIEL 5 (TODO 5): Bereinige Logdateien und leere Logs-Ordner.
# Lösche alle *.log Dateien im Verzeichnis "$1" und entferne den Ordner "$1/backup/logs" rekursiv mit rm.
bereinige_temporaere_dateien() {
  local basis_dir="$1"
  # TODO: Lösche mit rm / rm -rf
  return 0
}
