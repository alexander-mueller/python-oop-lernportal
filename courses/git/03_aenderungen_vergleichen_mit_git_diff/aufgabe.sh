#!/usr/bin/env bash
# ==============================================================================
# 🔀 Git Inspection - Git 03: Diff-Analysen & Änderungen untersuchen
# ==============================================================================

# 🎯 TEILZIEL 1: Arbeitsverzeichnis mit Staging-Area vergleichen (git diff)
# 🎯 TEILZIEL 2: Staging-Area mit HEAD vergleichen (git diff --staged)
# 🎯 TEILZIEL 3: Änderungen eines spezifischen Commits mit git show anzeigen
# 🎯 TEILZIEL 4: Statistiken mit git diff --stat auswerten

diff_inspection() {
  local repo_dir="${1:-.}"
  cd "$repo_dir" || return 1

  # TODO: Implementiere die geforderten Git-Befehle
  echo "Führe diff_inspection in $repo_dir aus..."
  return 1
}

# Direkter Aufruf bei Skript-Ausführung
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  diff_inspection "$@"
fi
