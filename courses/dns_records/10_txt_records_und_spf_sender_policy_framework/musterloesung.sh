#!/usr/bin/env bash
# ==============================================================================
# MUSTERLÖSUNG: DNS 10: SPF (SENDER POLICY FRAMEWORK) & 10-LOOKUP LIMIT
# ==============================================================================

build_spf_record() {
  local use_mx="$1"
  local ips="$2"
  local incs="$3"
  local qual="${4:--all}"

  local res="v=spf1"

  if [ "$use_mx" = "true" ]; then
    res="$res mx"
  fi

  if [ -n "$ips" ]; then
    for ip in $ips; do
      res="$res ip4:$ip"
    done
  fi

  if [ -n "$incs" ]; then
    for inc in $incs; do
      res="$res include:$inc"
    done
  fi

  res="$res $qual"
  echo "$res"
  return 0
}

count_spf_lookups() {
  local spf="$1"
  local count=0

  # Zerlege in Tokens
  for token in $spf; do
    case "$token" in
      include:*|redirect=*)
        ((count++))
        ;;
      a|a:*|mx|mx:*|ptr|ptr:*)
        ((count++))
        ;;
    esac
  done

  if [ "$count" -le 10 ]; then
    echo "LOOKUP_COUNT=$count | RFC7208_OK"
    return 0
  else
    echo "LOOKUP_LIMIT_EXCEEDED: $count Lookups überschreiten das 10er-Limit!"
    return 1
  fi
}

audit_spf_qualifier() {
  local spf="$1"

  if [[ "$spf" =~ \+all ]]; then
    echo "DANGEROUS: +all erlaubt jedem Server weltweit das Spoofing!"
    return 1
  elif [[ "$spf" =~ \?all ]]; then
    echo "WEAK: ?all ist neutral und bietet keinen Fälschungsschutz."
    return 1
  elif [[ "$spf" =~ \~all ]]; then
    echo "SOFTFAIL: ~all akzeptabel für Testphasen."
    return 0
  elif [[ "$spf" =~ \-all ]]; then
    echo "SECURE: -all HardFail erzwingt strikten Schutz."
    return 0
  else
    echo "ERROR: Kein gültiger All-Qualifier gefunden"
    return 1
  fi
}

format_spf_txt_record() {
  local domain="$1"
  local spf="$2"
  local ttl="${3:-3600}"

  printf "%-15s %-7s IN  TXT \"%s\"\n" "$domain" "$ttl" "$spf"
  return 0
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  build_spf_record "$@"
fi
