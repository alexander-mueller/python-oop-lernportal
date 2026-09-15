#!/usr/bin/env bash
# ==============================================================================
# MUSTERLÖSUNG: DNS 07: SOA (START OF AUTHORITY) & SERIAL-MANAGEMENT
# ==============================================================================

format_hostmaster_email() {
  local raw="$1"
  [ -z "$raw" ] && return 1

  # Trenne an @
  local user="${raw%%@*}"
  local domain="${raw#*@}"

  # Quotiere Punkte im Userteil
  local esc_user="${user//./\.}"
  local res="${esc_user}.${domain}"

  # Schlusspunkt garantieren
  if [[ "$res" != *. ]]; then
    res="${res}."
  fi

  echo "$res"
  return 0
}

generate_soa_serial() {
  local dstr="$1"
  local rev="${2:-01}"

  local ymd=""
  if [ -n "$dstr" ]; then
    ymd=$(echo "$dstr" | tr -d '-')
  else
    ymd=$(date +%Y%m%d)
  fi

  # Revision 2-stellig formatieren
  rev=$(printf "%02d" "$((10#$rev))")
  echo "${ymd}${rev}"
  return 0
}

increment_soa_serial() {
  local cur="$1"
  local today="$2"

  [ -z "$today" ] && today=$(date +%Y%m%d)
  local cur_date="${cur:0:8}"
  local cur_rev="${cur:8:2}"

  if [ "$cur_date" = "$today" ]; then
    local next_rev=$((10#$cur_rev + 1))
    printf "%s%02d\n" "$today" "$next_rev"
  else
    echo "${today}01"
  fi
  return 0
}

generate_complete_soa() {
  local zone="$1"
  local ns="$2"
  local email="$3"
  local serial="$4"
  local refresh="${5:-7200}"
  local retry="${6:-3600}"
  local expire="${7:-1209600}"
  local min_ttl="${8:-3600}"

  [[ "$ns" != *. ]] && ns="${ns}."
  local email_dns=$(format_hostmaster_email "$email")

  cat << EOF
@ IN SOA ${ns} ${email_dns} (
    ${serial} ; Serial YYYYMMDDNN
    ${refresh}       ; Refresh
    ${retry}       ; Retry
    ${expire}    ; Expire
    ${min_ttl}       ; Minimum / Negative Cache TTL
)
EOF
  return 0
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  format_hostmaster_email "$@"
fi
