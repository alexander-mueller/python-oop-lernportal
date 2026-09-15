#!/usr/bin/env bash
# ==============================================================================
# MUSTERLÖSUNG: DNS 08: NS-DELEGATION, REVERSE DNS (PTR) & FCRDNS
# ==============================================================================

ipv4_to_ptr_name() {
  local ip="$1"
  [ -z "$ip" ] && return 1

  IFS='.' read -ra octs <<< "$ip"
  if [ ${#octs[@]} -ne 4 ]; then
    echo "ERROR: Ungültige IPv4"
    return 1
  fi

  echo "${octs[3]}.${octs[2]}.${octs[1]}.${octs[0]}.in-addr.arpa."
  return 0
}

format_ptr_record() {
  local ip="$1"
  local target="$2"
  local ttl="${3:-86400}"

  local ptr_name=$(ipv4_to_ptr_name "$ip")
  [[ "$target" != *. ]] && target="${target}."

  printf "%-30s %-7s IN  PTR %s\n" "$ptr_name" "$ttl" "$target"
  return 0
}

format_ns_delegation() {
  local zone="$1"
  local ns1="$2"
  local ns2="$3"
  local ttl="${4:-86400}"

  [[ "$zone" != *. ]] && zone="${zone}."
  [[ "$ns1" != *. ]] && ns1="${ns1}."
  [[ "$ns2" != *. ]] && ns2="${ns2}."

  printf "%-25s %-7s IN  NS  %s\n" "$zone" "$ttl" "$ns1"
  printf "%-25s %-7s IN  NS  %s\n" "$zone" "$ttl" "$ns2"
  return 0
}

verify_fcrdns() {
  local cip="$1"
  local ptr_host="$2"
  local fip="$3"

  if [ "$cip" = "$fip" ]; then
    echo "FCRDNS_PASS: Validiert! Forward- und Reverse-Lookup stimmen überein (${cip} <-> ${ptr_host})."
    return 0
  else
    echo "FCRDNS_FAIL: Spoofing-Verdacht! PTR '${ptr_host}' löst auf '${fip}' auf, nicht '${cip}'!"
    return 1
  fi
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  ipv4_to_ptr_name "$@"
fi
