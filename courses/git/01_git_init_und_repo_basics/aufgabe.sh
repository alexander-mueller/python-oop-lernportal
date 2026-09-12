#!/usr/bin/env bash
# ==============================================================================
# 🔀 Git Grundlagen - Git 01: Repository-Initialisierung & 3 Bereiche
# ==============================================================================

# 🎯 TEILZIEL 1: Repository mit git init initialisieren
# 🎯 TEILZIEL 2: Konfiguration von user.name und user.email setzen
# 🎯 TEILZIEL 3: Status prüfen mit git status --short
# 🎯 TEILZIEL 4: Ersten Commit auf dem Branch main erstellen

init_repository() {
  local repo_dir="${1:-.}"
  cd "$repo_dir" || return 1

  # TODO: Implementiere die geforderten Git-Befehle
  echo "Führe init_repository in $repo_dir aus..."
  return 0
}

# Direkter Aufruf bei Skript-Ausführung
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  init_repository "$@"
fi
