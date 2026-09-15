#!/usr/bin/env bash
# ==============================================================================
# MUSTERLÖSUNG: DNS 04: TTL (TIME TO LIVE), CACHING & DNS-PROPAGATION
# ==============================================================================

format_ttl_human() {
  local s="$1"
  [ -z "$s" ] && return 1

  local d=$((s / 86400))
  local rem=$((s % 86400))
  local h=$((rem / 3600))
  rem=$((rem % 3600))
  local m=$((rem / 60))
  local sec=$((rem % 60))

  if [ "$s" -ge 86400 ]; then
    echo "${d}d ${h}h ${m}m ${sec}s"
  elif [ "$s" -ge 3600 ]; then
    echo "${h}h ${m}m ${sec}s"
  elif [ "$s" -ge 60 ]; then
    echo "${m}m ${sec}s"
  else
    echo "${sec}s"
  fi
  return 0
}

plan_dns_migration() {
  local current_ttl="$1"
  local maint_hours="$2"

  local ttl_hours=$((current_ttl / 3600))
  [ "$ttl_hours" -lt 1 ] && ttl_hours=1

  if [ "$maint_hours" -lt "$ttl_hours" ]; then
    echo "MIGRATION_RISK: Wartungsfenster zu nah! Mindestens ${ttl_hours}h Vorlaufzeit erforderlich."
    return 1
  fi

  echo "ADVANCE_HOURS=${ttl_hours}"
  echo "TEMP_TTL=300"
  echo "STATUS=READY_TO_SCHEDULE"
  echo "EMPFEHLUNG=Senke die TTL ${ttl_hours} Stunden vor Beginn auf 300s."
  return 0
}

simulate_cache_decay() {
  local init="$1"
  local elapsed="$2"

  local rest=$((init - elapsed))
  if [ "$rest" -gt 0 ]; then
    echo "CACHE_HIT: Rest-TTL beträgt ${rest}s"
    return 0
  else
    echo "CACHE_EXPIRED: TTL abgelaufen (0s). Neuer iterativer Query erforderlich."
    return 1
  fi
}

extract_soa_negative_ttl() {
  local line="$1"
  local clean=$(echo "$line" | tr -d '()' | tr -s '[:space:]' ' ')
  clean="${clean## }"
  clean="${clean%% }"

  # Extrahiere das letzte Token
  local last_token="${clean##* }"

  if [[ ! "$last_token" =~ ^[0-9]+$ ]]; then
    echo "ERROR: Ungültiges SOA-Format"
    return 1
  fi

  if [ "$last_token" -ge 600 ] && [ "$last_token" -le 86400 ]; then
    echo "NEG_TTL=${last_token}s | COMPLIANT=YES"
    return 0
  else
    echo "NEG_TTL=${last_token}s | COMPLIANT=NO (Empfehlung: 1800s bis 7200s)"
    return 1
  fi
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  format_ttl_human "$@"
fi
