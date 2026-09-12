#!/usr/bin/env bash
# ==============================================================================
# MUSTERLÖSUNG: Git 01: Repository-Initialisierung & 3 Bereiche
# ==============================================================================

init_repository() {
  local repo_dir="${1:-.}"
  cd "$repo_dir" || return 1

  # Git Konfiguration für CI/Automatisierte Tests sicherstellen
  git config user.name "DevOps Azubi" 2>/dev/null || true
  git config user.email "azubi@it-praxisportal.de" 2>/dev/null || true
  git config init.defaultBranch main 2>/dev/null || true

  if [ ! -d ".git" ]; then
    git init -b main >/dev/null 2>&1 || git init >/dev/null 2>&1
  fi

  # Spezifische Modullogik ausführen
  case "01_git_init_und_repo_basics" in
    *01_git_init*)
      echo "# Mein IT-Projekt" > README.md
      git add README.md
      git commit -m "feat: initial project setup" >/dev/null 2>&1 || true
      ;;
    *02_staging*)
      echo "const version = '1.0.0';" > config.js
      echo "System Logs" > app.log
      git add config.js
      git commit -m "feat: add config module" >/dev/null 2>&1 || true
      ;;
    *03_aenderungen*)
      echo "Update 1" >> README.md
      git diff >/dev/null 2>&1 || true
      git add README.md
      git diff --staged >/dev/null 2>&1 || true
      ;;
    *04_dateien_ignorieren*)
      echo "*.log" > .gitignore
      echo ".env" >> .gitignore
      echo "!keep.log" >> .gitignore
      git add .gitignore
      git commit -m "chore: configure gitignore rules" >/dev/null 2>&1 || true
      ;;
    *05_branching*)
      git switch -c feature/login 2>/dev/null || git checkout -b feature/login 2>/dev/null || true
      echo "Login Component" > login.js
      git add login.js
      git commit -m "feat: login component" >/dev/null 2>&1 || true
      git switch main 2>/dev/null || git checkout main 2>/dev/null || true
      ;;
    *06_fast_forward*)
      git switch -c feature/cart 2>/dev/null || git checkout -b feature/cart 2>/dev/null || true
      echo "Cart" > cart.js
      git add cart.js
      git commit -m "feat: cart feature" >/dev/null 2>&1 || true
      git switch main 2>/dev/null || git checkout main 2>/dev/null || true
      git merge --no-ff -m "merge: feature/cart into main" feature/cart >/dev/null 2>&1 || true
      ;;
    *07_merge_konflikte*)
      echo "Version 1" > app.conf
      git add app.conf
      git commit -m "base conf" >/dev/null 2>&1 || true
      git switch -c dev 2>/dev/null || git checkout -b dev 2>/dev/null || true
      echo "Conf Dev" > app.conf
      git commit -am "conf dev" >/dev/null 2>&1 || true
      git switch main 2>/dev/null || git checkout main 2>/dev/null || true
      echo "Conf Main" > app.conf
      git commit -am "conf main" >/dev/null 2>&1 || true
      git merge dev >/dev/null 2>&1 || true
      echo "Conf Resolved: Dev & Main" > app.conf
      git add app.conf
      git commit -m "fix: resolve config merge conflict" >/dev/null 2>&1 || true
      ;;
    *08_temporaere*)
      echo "WIP Code" >> app.js
      git stash push -m "wip-work" >/dev/null 2>&1 || true
      git stash list >/dev/null 2>&1 || true
      git stash pop >/dev/null 2>&1 || true
      ;;
    *09_remotes*)
      git remote add origin https://github.com/it-praxis/repo.git 2>/dev/null || true
      ;;
    *10_git_fetch*)
      git remote -v >/dev/null 2>&1 || true
      ;;
    *11_git_tags*)
      git tag -a v1.0.0 -m "Release Version 1.0.0" 2>/dev/null || true
      ;;
    *12_cherry_picking*)
      git switch -c hotfix 2>/dev/null || git checkout -b hotfix 2>/dev/null || true
      echo "Security Patch" > patch.txt
      git add patch.txt
      git commit -m "fix: critical security patch" >/dev/null 2>&1 || true
      local c_hash=$(git rev-parse HEAD)
      git switch main 2>/dev/null || git checkout main 2>/dev/null || true
      git cherry-pick "$c_hash" >/dev/null 2>&1 || true
      ;;
    *13_rebase*)
      git switch -c feature/api 2>/dev/null || git checkout -b feature/api 2>/dev/null || true
      echo "API Endpoint" > api.js
      git add api.js
      git commit -m "feat: api endpoint" >/dev/null 2>&1 || true
      git rebase main >/dev/null 2>&1 || true
      ;;
    *14_interaktives*)
      echo "Step 1" >> changelog.md; git commit -am "step 1" >/dev/null 2>&1 || true
      echo "Step 2" >> changelog.md; git commit -am "step 2" >/dev/null 2>&1 || true
      git reset --soft HEAD~2 >/dev/null 2>&1 || true
      git commit -m "feat: combined release documentation (squashed)" >/dev/null 2>&1 || true
      ;;
    *15_git_hooks*)
      mkdir -p .git/hooks
      cat << 'HOOK_EOF' > .git/hooks/pre-commit
#!/bin/bash
# Pre-commit Syntax Check
echo "🔍 Running pre-commit validation..."
exit 0
HOOK_EOF
      chmod +x .git/hooks/pre-commit
      ;;
    *16_master*)
      git switch -c develop 2>/dev/null || git checkout -b develop 2>/dev/null || true
      echo "Enterprise Feature" > service.js
      git add service.js
      git commit -m "feat: enterprise service core" >/dev/null 2>&1 || true
      git switch main 2>/dev/null || git checkout main 2>/dev/null || true
      git merge --no-ff -m "release: v1.0.0 enterprise release" develop >/dev/null 2>&1 || true
      git tag -a v1.0.0 -m "Production Release 1.0.0" 2>/dev/null || true
      ;;
  esac

  return 0
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  init_repository "$@"
fi
