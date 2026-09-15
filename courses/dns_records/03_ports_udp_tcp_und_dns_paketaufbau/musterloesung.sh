#!/usr/bin/env bash
# ==============================================================================
# MUSTERLÖSUNG: DNS 03: UDP VS. TCP PORT 53, TRUNCATION & EDNS0
# ==============================================================================

select_dns_transport() {
  local size="$1"
  local qtype=$(echo "$2" | tr '[:lower:]' '[:upper:]')
  local edns=$(echo "$3" | tr '[:upper:]' '[:lower:]')

  if [ "$qtype" = "AXFR" ] || [ "$qtype" = "IXFR" ]; then
    echo "TCP (Grund: Zonentransfer erfordert zwingend TCP)"
    return 0
  fi

  if [ "$size" -le 512 ]; then
    echo "UDP (Grund: Paket passt in Standard-512B-Puffer)"
    return 0
  fi

  if [ "$size" -gt 512 ] && [ "$edns" = "true" ] && [ "$size" -le 4096 ]; then
    echo "UDP_EDNS0 (Grund: EDNS0 erweitert UDP-Puffer auf bis zu 4096 Bytes)"
    return 0
  fi

  if [ "$size" -gt 512 ] && [ "$edns" = "false" ]; then
    echo "TCP_TRUNCATED (Grund: TC=1 gesetzt, Fallback auf TCP erforderlich)"
    return 0
  fi

  echo "TCP_FALLBACK"
  return 0
}

parse_section_counts() {
  local qd="${1:-1}"
  local an="${2:-0}"
  local ns="${3:-0}"
  local ar="${4:-0}"

  local status="EMPTY_RESPONSE"
  if [ "$an" -gt 0 ]; then
    status="HAS_ANSWERS"
  elif [ "$ns" -gt 0 ]; then
    status="REFERRAL_ONLY"
  fi

  echo "QUESTIONS=$qd"
  echo "ANSWERS=$an"
  echo "AUTHORITY=$ns"
  echo "ADDITIONAL=$ar"
  echo "STATUS=$status"
  return 0
}

verify_edns0_in_dig() {
  local file="$1"
  [ ! -f "$file" ] && return 1

  if grep -q "OPT PSEUDOSECTION:" "$file"; then
    local size=$(grep -oE "udp:[[:space:]]*[0-9]+" "$file" | grep -oE "[0-9]+")
    [ -z "$size" ] && size="4096"
    echo "EDNS0_ACTIVE: Puffergröße ${size} Bytes"
    return 0
  else
    echo "EDNS0_INACTIVE: Kein OPT Pseudo-Record gefunden (512B Limit)"
    return 1
  fi
}

secure_zone_transfers() {
  local zone="$1"
  local slave_ip="$2"
  local out_file="$3"

  [ -z "$zone" ] || [ -z "$slave_ip" ] || [ -z "$out_file" ] && return 1
  mkdir -p "$(dirname "$out_file")" 2>/dev/null

  cat << EOF > "$out_file"
zone "${zone}" {
    type master;
    file "/var/lib/bind/db.${zone}";
    allow-transfer { ${slave_ip}; };
};
EOF
  return 0
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  select_dns_transport "$@"
fi
