#!/usr/bin/env bash
# ==============================================================================
# MUSTERLÖSUNG: DNS 11: DKIM & KRYPTOGRAFISCHE E-MAIL-SIGNATUR
# ==============================================================================

build_dkim_fqdn() {
  local sel="$1"
  local dom="$2"
  [ -z "$sel" ] || [ -z "$dom" ] && return 1

  dom="${dom%.}"
  echo "${sel}._domainkey.${dom}."
  return 0
}

audit_dkim_key_security() {
  local key="$1"
  local len=${#key}

  if [ "$len" -lt 300 ]; then
    echo "INSECURE: 1024-Bit RSA Key ($len Zeichen) ist veraltet! Mindestens 2048 Bit erforderlich."
    return 1
  else
    echo "SECURE: 2048-Bit RSA Key ($len Zeichen) erfüllt moderne Sicherheitsstandards."
    return 0
  fi
}

format_dkim_record() {
  local sel="$1"
  local dom="$2"
  local key="$3"
  local ttl="${4:-86400}"

  local fqdn=$(build_dkim_fqdn "$sel" "$dom")
  local payload="v=DKIM1; k=rsa; p=${key}"

  if [ ${#payload} -gt 250 ]; then
    local chunk1="${payload:0:200}"
    local chunk2="${payload:200}"
    printf "%-30s %-7s IN  TXT ( \"%s\" \"%s\" )\n" "$fqdn" "$ttl" "$chunk1" "$chunk2"
  else
    printf "%-30s %-7s IN  TXT \"%s\"\n" "$fqdn" "$ttl" "$payload"
  fi
  return 0
}

parse_dkim_record() {
  local raw="$1"
  local clean=$(echo "$raw" | tr -d '()"' | tr ';' '\n')

  local v="DKIM1"
  local k="rsa"
  local p=""

  while IFS='=' read -r tag val; do
    tag=$(echo "$tag" | tr -d '[:space:]')
    val=$(echo "$val" | tr -d '[:space:]')
    [ "$tag" = "v" ] && v="$val"
    [ "$tag" = "k" ] && k="$val"
    [ "$tag" = "p" ] && p="$val"
  done <<< "$clean"

  local preview="${p:0:15}..."
  echo "VERSION=$v"
  echo "KEY_TYPE=$k"
  echo "KEY_PREVIEW=$preview"
  return 0
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  build_dkim_fqdn "$@"
fi
