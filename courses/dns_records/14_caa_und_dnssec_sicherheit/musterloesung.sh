#!/usr/bin/env bash
# ==============================================================================
# Musterlösung Modul 14: CAA & DNSSEC Sicherheit
# ==============================================================================

function format_caa_record() {
    local domain="$1"
    local tag="$2"
    local value="$3"
    local flags="${4:-0}"
    local ttl="${5:-3600}"

    [[ "$domain" != *. ]] && domain="${domain}."

    echo "${domain} ${ttl} IN CAA ${flags} ${tag} "${value}""
}

function format_caa_wildcard_block() {
    local domain="$1"

    format_caa_record "$domain" "issue" "letsencrypt.org" 0 3600
    format_caa_record "$domain" "issuewild" ";" 0 3600
    format_caa_record "$domain" "iodef" "mailto:security@${domain}" 0 3600
}

function parse_ds_record() {
    local ds_line="$1"
    read -r domain ttl in_kw ds_kw key_tag algo digest_type hash <<< "$ds_line"

    echo "KEY_TAG=${key_tag} ALGO=${algo} DIGEST_TYPE=${digest_type} HASH=${hash}"
}

function verify_dnssec_chain_status() {
    local ksk_hash="$1"
    local ds_hash="$2"

    if [ -n "$ksk_hash" ] && [ "$ksk_hash" = "$ds_hash" ]; then
        echo "DNSSEC_SECURE: Chain of trust verified"
        return 0
    else
        echo "BOGUS_CHAIN_BROKEN: Key tag or hash mismatch"
        return 1
    fi
}
