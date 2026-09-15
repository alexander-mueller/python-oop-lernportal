#!/usr/bin/env bash
# ==============================================================================
# MUSTERLÖSUNG: DNS 02: REKURSIVE VS. ITERATIVE ABFRAGEN & DNS-FLAGS
# ==============================================================================

parse_dns_flags() {
  local raw="$1"
  local lower=$(echo "$raw" | tr '[:upper:]' '[:lower:]')

  local qr="0_QUERY"
  local aa="NO"
  local tc="NO"
  local rd="NO"
  local ra="NO"

  [[ "$lower" =~ (^|[[:space:]])qr([[:space:]]|$) ]] && qr="1_RESPONSE"
  [[ "$lower" =~ (^|[[:space:]])aa([[:space:]]|$) ]] && aa="YES"
  [[ "$lower" =~ (^|[[:space:]])tc([[:space:]]|$) ]] && tc="YES"
  [[ "$lower" =~ (^|[[:space:]])rd([[:space:]]|$) ]] && rd="YES"
  [[ "$lower" =~ (^|[[:space:]])ra([[:space:]]|$) ]] && ra="YES"

  echo "QR=$qr"
  echo "AA=$aa"
  echo "TC=$tc"
  echo "RD=$rd"
  echo "RA=$ra"
  return 0
}

simulate_iterative_steps() {
  local domain="$1"
  [ -z "$domain" ] && return 1

  local clean="${domain%.}"
  IFS='.' read -ra labels <<< "$clean"
  local count=${#labels[@]}

  local tld="${labels[-1]}"
  local sld="${labels[-2]}"

  echo "SCHRITT 1: Query an Root (.) -> Referral zu TLD Nameserver (${tld}.)"
  echo "SCHRITT 2: Query an TLD Server (${tld}.) -> Referral zu autoritativem Nameserver (${sld}.${tld}.)"
  echo "SCHRITT 3: Query an autoritativen Server (${sld}.${tld}.) -> Antwort erhalten (AA=1)"
  echo "SCHRITT 4: Resolver speichert Ergebnis im Cache und sendet Antwort an Client (RA=1)"
  return 0
}

detect_open_resolver() {
  local flags="$1"
  local network="$2"
  local lower=$(echo "$flags" | tr '[:upper:]' '[:lower:]')

  if [[ ! "$lower" =~ (^|[[:space:]])ra([[:space:]]|$) ]]; then
    echo "INFO: Reiner autoritativer Server (keine Rekursion)."
    return 0
  fi

  if [ "$network" = "0.0.0.0/0" ] || [ "$network" = "any" ]; then
    echo "SECURITY_ALERT: Open Resolver erkannt! Rekursion aus 0.0.0.0/0 muss gesperrt werden."
    return 1
  else
    echo "SECURE: Rekursiver Resolver auf internes Netz beschränkt."
    return 0
  fi
}

generate_forwarder_config() {
  local out_file="$1"
  local ip1="$2"
  local ip2="$3"

  [ -z "$out_file" ] || [ -z "$ip1" ] || [ -z "$ip2" ] && return 1
  mkdir -p "$(dirname "$out_file")" 2>/dev/null

  cat << EOF > "$out_file"
options {
    directory "/var/cache/bind";
    recursion yes;
    allow-query { 192.168.0.0/16; 10.0.0.0/8; localhost; };
    forwarders {
        ${ip1};
        ${ip2};
    };
    forward only;
    dnssec-validation auto;
};
EOF
  return 0
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  parse_dns_flags "$@"
fi
