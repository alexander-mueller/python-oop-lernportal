#!/usr/bin/env bash
# ==============================================================================
# 🔀 Git Stash - Git 08: Zwischenspeichern mit Git Stash
# ==============================================================================

# 🎯 TEILZIEL 1: Arbeitsverzeichnis mit git stash push -m 'wip' sichern
# 🎯 TEILZIEL 2: Auf sauberen Branch wechseln und Hotfix committen
# 🎯 TEILZIEL 3: Stash-Einträge mit git stash list inspizieren
# 🎯 TEILZIEL 4: Gestashte Änderungen mit git stash pop wiederherstellen

use_stash() {
  local repo_dir="${1:-.}"
  cd "$repo_dir" || return 1

  # TODO: Implementiere die geforderten Git-Befehle
  echo "Führe use_stash in $repo_dir aus..."
  return 0
}

# Direkter Aufruf bei Skript-Ausführung
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  use_stash "$@"
fi
