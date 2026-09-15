#!/usr/bin/env bash
# ==============================================================================
# MUSTERLÖSUNG: DNS 05: A- & AAAA-RECORDS (IPV4 & IPV6 DUAL-STACK)
# ==============================================================================

format_a_record() {
  local host="$1"
  local ip="$2"
  local ttl="${3:-3600}"

  # IPv4 Validierung
  local valid_ip=false
  if [[ "$ip" =~ ^([0-9]{1,3}\.){3}[0-9]{1,3}$ ]]; then
    valid_ip=true
    IFS='.' read -ra octets <<< "$ip"
    for oct in "${octets[@]}"; do
      if [ "$oct" -gt 255 ]; then
        valid_ip=false
        break
      fi
    done
  fi

  if [ "$valid_ip" = false ]; then
    echo "ERROR: Ungültige IPv4-Adresse"
    return 1
  fi

  printf "%-15s %-7s IN  A     %s\n" "$host" "$ttl" "$ip"
  return 0
}

format_aaaa_record() {
  local host="$1"
  local ipv6="$2"
  local ttl="${3:-3600}"

  if [[ ! "$ipv6" =~ : ]] || [[ "$ipv6" =~ [^0-9a-fA-F:] ]]; then
    echo "ERROR: Ungültige IPv6-Adresse"
    return 1
  fi

  printf "%-15s %-7s IN  AAAA  %s\n" "$host" "$ttl" "$ipv6"
  return 0
}

generate_round_robin_pool() {
  local host="$1"
  local ttl="$2"
  shift 2
  local ips=("$@")

  for ip in "${ips[@]}"; do
    format_a_record "$host" "$ip" "$ttl"
  done
  return 0
}

audit_dual_stack() {
  local zfile="$1"
  [ ! -f "$zfile" ] && return 1

  # Finde alle A-Hosts (Spalte 1)
  local a_hosts=($(awk '$3 == "A" || $4 == "A" { print $1 }' "$zfile" | sort -u))
  local missing=()

  for h in "${a_hosts[@]}"; do
    if ! awk -v host="$h" '($1 == host) && ($3 == "AAAA" || $4 == "AAAA") { found=1 } END { exit !found }' "$zfile"; then
      missing+=("$h")
    fi
  done

  if [ ${#missing[@]} -eq 0 ]; then
    echo "DUAL_STACK_AUDIT: OK (Alle IPv4-Hosts besitzen IPv6 AAAA)"
    return 0
  else
    echo "DUAL_STACK_WARNUNG: Fehlendes IPv6 für Host(s): ${missing[*]}"
    return 1
  fi
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  format_a_record "$@"
fi
