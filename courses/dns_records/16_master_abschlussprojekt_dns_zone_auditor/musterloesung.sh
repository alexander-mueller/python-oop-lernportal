#!/usr/bin/env bash
# ==============================================================================
# Musterlösung Modul 16: Master-Projekt DNS Zone Auditor
# ==============================================================================

function audit_soa_record() {
    local zone_content="$1"
    local serial
    serial=$(echo "$zone_content" | grep -A 5 -i "SOA" | grep -E -o "[0-9]{10}" | head -n 1)

    if [[ "$serial" =~ ^[0-9]{10}$ ]]; then
        echo "SOA_OK: Serial ${serial} valid"
        return 0
    else
        echo "SOA_FAIL: Invalid serial"
        return 1
    fi
}

function audit_ns_redundancy() {
    local zone_content="$1"
    local count
    count=$(echo "$zone_content" | grep -E -i "\s+IN\s+NS\s+" | wc -l)

    if [ "$count" -ge 2 ]; then
        echo "NS_OK: Redundancy satisfied (Count: ${count})"
        return 0
    else
        echo "NS_FAIL: Critical lack of redundancy (Count: ${count})"
        return 1
    fi
}

function audit_apex_cname_collision() {
    local zone_content="$1"
    if echo "$zone_content" | grep -E -i "^(@|IN)\s+.*CNAME" || echo "$zone_content" | grep -E -i "^@\s+IN\s+CNAME"; then
        echo "CRITICAL: CNAME at apex detected"
        return 1
    else
        echo "APEX_OK: No apex CNAME collision"
        return 0
    fi
}

function audit_email_defense() {
    local zone_content="$1"
    local has_spf=false
    local has_dmarc=false

    if echo "$zone_content" | grep -i "v=spf1" | grep -q -- "-all"; then
        has_spf=true
    fi

    if echo "$zone_content" | grep -i "_dmarc" | grep -qiE "p=(reject|quarantine)"; then
        has_dmarc=true
    fi

    if [ "$has_spf" = true ] && [ "$has_dmarc" = true ]; then
        echo "EMAIL_DEFENSE_OK: Both SPF and DMARC enforced"
        return 0
    else
        echo "EMAIL_DEFENSE_WARN: Incomplete SPF or DMARC protection"
        return 1
    fi
}

function run_complete_zone_audit() {
    local zone_content="$1"
    local score=0

    audit_soa_record "$zone_content" > /dev/null && ((score += 25))
    audit_ns_redundancy "$zone_content" > /dev/null && ((score += 25))
    audit_apex_cname_collision "$zone_content" > /dev/null && ((score += 25))
    audit_email_defense "$zone_content" > /dev/null && ((score += 25))

    echo "=================================================="
    echo "📋 ENTERPRISE DNS ZONE AUDIT REPORT"
    echo "=================================================="
    echo "SCORE=${score}/100"
    if [ "$score" -ge 75 ]; then
        echo "VERDICT=AUDIT_PASSED"
        return 0
    else
        echo "VERDICT=AUDIT_FAILED"
        return 1
    fi
}
