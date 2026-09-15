#!/usr/bin/env bash
# ==============================================================================
# Musterlösung Modul 13: SRV-Service Records für AD & SIP
# ==============================================================================

function format_srv_record() {
    local service="$1"
    local proto="$2"
    local domain="$3"
    local prio="$4"
    local weight="$5"
    local port="$6"
    local target="$7"
    local ttl="${8:-86400}"

    [[ "$service" != _* ]] && service="_${service}"
    [[ "$proto" != _* ]] && proto="_${proto}"
    [[ "$domain" != *. ]] && domain="${domain}."
    [[ "$target" != *. ]] && target="${target}."

    echo "${service}.${proto}.${domain} ${ttl} IN SRV ${prio} ${weight} ${port} ${target}"
}

function parse_srv_record() {
    local srv_line="$1"
    read -r fqdn ttl in_kw srv_kw prio weight port target <<< "$srv_line"

    local service proto domain
    service=$(echo "$fqdn" | awk -F. '{print $1}')
    proto=$(echo "$fqdn" | awk -F. '{print $2}')

    echo "SERVICE=${service} PROTO=${proto} PRIO=${prio} WEIGHT=${weight} PORT=${port} TARGET=${target}"
}

function generate_ad_srv_records() {
    local domain="$1"
    local dc_hostname="$2"
    local prio="${3:-0}"
    local weight="${4:-100}"

    format_srv_record "_ldap" "_tcp" "$domain" "$prio" "$weight" 389 "$dc_hostname" 600
    format_srv_record "_kerberos" "_tcp" "$domain" "$prio" "$weight" 88 "$dc_hostname" 600
    format_srv_record "_gc" "_tcp" "$domain" "$prio" "$weight" 3268 "$dc_hostname" 600
}

function select_srv_target_by_prio() {
    local srv_records="$1"
    local best_target=""
    local best_prio=999999

    while IFS= read -r line; do
        [[ -z "$line" ]] && continue
        read -r _ _ _ _ prio _ _ target <<< "$line"
        if [ "$prio" -lt "$best_prio" ]; then
            best_prio="$prio"
            best_target="$target"
        fi
    done <<< "$srv_records"

    echo "$best_target"
}
