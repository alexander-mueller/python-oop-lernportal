#!/usr/bin/env bash
# ==============================================================================
# 🐧 BASH 01: MUSTERLÖSUNG
# ==============================================================================

erstelle_projektstruktur() {
  local basis_dir="$1"
  mkdir -p "$basis_dir/src/components" "$basis_dir/src/utils" "$basis_dir/docs/api" "$basis_dir/backup/logs"
}

erstelle_testdateien() {
  local basis_dir="$1"
  touch "$basis_dir/src/components/button.js" \
        "$basis_dir/src/components/modal.js" \
        "$basis_dir/src/utils/helper.js" \
        "$basis_dir/docs/api/v1.md" \
        "$basis_dir/docs/api/v2.md" \
        "$basis_dir/app_dev.log" \
        "$basis_dir/app_prod.log" \
        "$basis_dir/config.yaml"
}

kopiere_konfigurationen() {
  local src_dir="$1"
  local backup_dir="$2"
  mkdir -p "$backup_dir"
  cp "$src_dir"/*.yaml "$src_dir"/*.log "$backup_dir/" 2>/dev/null || true
}

verschiebe_dateien() {
  local src_dir="$1"
  local target_dir="$2"
  mkdir -p "$target_dir"
  mv "$src_dir"/docs/api/*.md "$target_dir/" 2>/dev/null || true
}

bereinige_temporaere_dateien() {
  local basis_dir="$1"
  rm -f "$basis_dir"/*.log
  rm -rf "$basis_dir/backup/logs"
}
