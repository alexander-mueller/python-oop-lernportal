#!/usr/bin/env bash
# ==============================================================================
# Musterlösung Modul 15: DNS-Troubleshooting
# ==============================================================================

function diagnose_dns_rcode() {
    local rcode="$1"
    case "$rcode" in
        "NOERROR")
            echo "OK: Query successful. Records returned or NODATA."
            ;;
        "NXDOMAIN")
            echo "ERROR_NXDOMAIN: Domain or hostname does not exist. Check spelling or registrar status."
            ;;
        "SERVFAIL")
            echo "ERROR_SERVFAIL: Nameserver failed to answer. Check DNSSEC validation or authoritative connectivity."
            ;;
        "REFUSED")
            echo "ERROR_REFUSED: Nameserver refused query. Check zone ACLs and recursion permissions."
            ;;
        *)
            echo "UNKNOWN_RCODE: ${rcode}"
            ;;
    esac
}

function extract_dig_ips() {
    local dig_output="$1"
    echo "$dig_output" | grep -E -o "([0-9]{1,3}\.){3}[0-9]{1,3}" | sort -u
}

function detect_soa_desync() {
    local primary_serial="$1"
    local secondary_serial="$2"

    if [ "$primary_serial" -eq "$secondary_serial" ]; then
        echo "IN_SYNC: Serials match (${primary_serial})"
        return 0
    else
        echo "DESYNC: Slave lag detected (Primary: ${primary_serial}, Slave: ${secondary_serial})"
        return 1
    fi
}

function verify_axfr_blocked() {
    local axfr_output="$1"

    if echo "$axfr_output" | grep -qiE "(Transfer failed|REFUSED|connection refused)"; then
        echo "SECURE: AXFR transfer blocked"
        return 0
    else
        echo "CRITICAL_LEAK: AXFR open to public"
        return 1
    fi
}
