#!/usr/bin/env bash
# ==============================================================================
# 🔀 Git Konfiguration - Git 04: .gitignore & Ausschlussregeln
# ==============================================================================

# 🎯 TEILZIEL 1: .gitignore mit Wildcard-Patterns (*.log, temp/) anlegen
# 🎯 TEILZIEL 2: Ausnahmeregel mit Ausrufezeichen (!keep.log) definieren
# 🎯 TEILZIEL 3: Versehentlich getrackte Datei mit git rm --cached aus dem Index entfernen
# 🎯 TEILZIEL 4: Ignorierregeln mit git check-ignore validieren

setup_gitignore() {
  local repo_dir="${1:-.}"
  cd "$repo_dir" || return 1

  # TODO: Implementiere die geforderten Git-Befehle
  echo "Führe setup_gitignore in $repo_dir aus..."
  return 0
}

# Direkter Aufruf bei Skript-Ausführung
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  setup_gitignore "$@"
fi
