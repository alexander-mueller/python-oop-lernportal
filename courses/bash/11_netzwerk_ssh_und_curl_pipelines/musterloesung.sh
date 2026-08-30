#!/usr/bin/env bash
# ==============================================================================
# Bash 11: Remote SSH, REST-Pipelines (curl) & rsync Automatisierung
# MUSTERLÖSUNG
# ==============================================================================

build_curl_post_command() {
    local endpoint="${1:-}"
    local token="${2:-}"
    local payload="${3:-}"

    if [ -z "$endpoint" ] || [ -z "$token" ] || [ -z "$payload" ]; then
        return 1
    fi

    echo "curl -s -f -X POST \"$endpoint\" -H \"Authorization: Bearer $token\" -H \"Content-Type: application/json\" -d '$payload'"
}

get_http_status_code() {
    local url="${1:-}"

    if [ -z "$url" ]; then
        return 1
    fi

    curl -s -o /dev/null -w "%{http_code}" "$url"
}

build_ssh_batch_command() {
    local user="${1:-}"
    local host="${2:-}"
    local script_file="${3:-}"
    local port="${4:-22}"

    if [ -z "$user" ] || [ -z "$host" ] || [ -z "$script_file" ]; then
        return 1
    fi

    echo "ssh -p $port -o BatchMode=yes -o StrictHostKeyChecking=no ${user}@${host} \"bash -s\" < $script_file"
}

build_rsync_command() {
    local src="${1:-}"
    local dest="${2:-}"
    local exclude="${3:-}"
    local delete_flag="${4:-false}"

    if [ -z "$src" ] || [ -z "$dest" ]; then
        return 1
    fi

    local cmd="rsync -avz"

    if [ "$delete_flag" = "true" ]; then
        cmd="$cmd --delete"
    fi

    if [ -n "$exclude" ]; then
        cmd="$cmd --exclude=\"$exclude\""
    fi

    cmd="$cmd $src $dest"
    echo "$cmd"
}
