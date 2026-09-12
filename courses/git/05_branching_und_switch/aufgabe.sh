#!/usr/bin/env bash
# ==============================================================================
# 🔀 Branching - Git 05: Branch-Management & HEAD-Pointer
# ==============================================================================

# 🎯 TEILZIEL 1: Neuen Feature-Branch mit git switch -c erstellen
# 🎯 TEILZIEL 2: Zwischen Branches hin- und herwechseln
# 🎯 TEILZIEL 3: Alle lokalen und remote Branches listen (git branch -a)
# 🎯 TEILZIEL 4: Veralteten Branch nach dem Mergen mit git branch -d löschen

manage_branches() {
  local repo_dir="${1:-.}"
  cd "$repo_dir" || return 1

  # TODO: Implementiere die geforderten Git-Befehle
  echo "Führe manage_branches in $repo_dir aus..."
  return 1
}

# Direkter Aufruf bei Skript-Ausführung
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  manage_branches "$@"
fi
