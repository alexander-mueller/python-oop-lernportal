#!/usr/bin/env bash
# ==============================================================================
# Bash 14: CI/CD Workflows & GitHub Actions Shell Scripting
# MUSTERLÖSUNG
# ==============================================================================

write_github_output() {
    local name="${1:-}"
    local value="${2:-}"
    local output_file="${3:-}"

    if [ -z "$name" ] || [ -z "$output_file" ]; then
        return 1
    fi

    # Prüfe ob value mehrzeilig ist
    if [[ "$value" == *$'\n'* ]]; then
        cat <<_HEREDOC_ >> "$output_file"
${name}<<EOF
${value}
EOF
_HEREDOC_
    else
        echo "${name}=${value}" >> "$output_file"
    fi
}

mask_github_secret() {
    local secret="${1:-}"

    if [ -z "$secret" ]; then
        return 1
    fi

    echo "::add-mask::${secret}"
}

generate_step_summary_table() {
    local title="${1:-}"
    local pairs_str="${2:-}"
    local summary_file="${3:-}"

    if [ -z "$title" ] || [ -z "$summary_file" ]; then
        return 1
    fi

    cat <<EOF >> "$summary_file"
### $title

| Metric | Value |
|---|---|
EOF

    # Pairs zerlegen (Leerzeichen-separierte "Key:Value" Paare)
    for item in $pairs_str; do
        local key="${item%%:*}"
        local val="${item#*:}"
        echo "| $key | $val |" >> "$summary_file"
    done
}

detect_os_and_package_install_cmd() {
    local pkg="${1:-}"
    local os_type="${2:-}"

    if [ -z "$pkg" ]; then
        return 1
    fi

    if [ -z "$os_type" ]; then
        if [ "$(uname -s)" = "Darwin" ]; then
            os_type="darwin"
        elif [ -f /etc/os-release ]; then
            # os-release auswerten
            local id
            id=$(grep "^ID=" /etc/os-release | cut -d= -f2 | tr -d '"' | tr '[:upper:]' '[:lower:]')
            os_type="$id"
        else
            os_type="unknown"
        fi
    fi

    os_type=$(echo "$os_type" | tr '[:upper:]' '[:lower:]')

    case "$os_type" in
        ubuntu|debian)
            echo "apt-get update -y && apt-get install -y $pkg"
            ;;
        alpine)
            echo "apk add --no-cache $pkg"
            ;;
        rhel|centos|fedora)
            echo "dnf install -y $pkg"
            ;;
        darwin)
            echo "brew install $pkg"
            ;;
        *)
            return 1
            ;;
    esac
}
