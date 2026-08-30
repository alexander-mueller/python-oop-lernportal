#!/usr/bin/env bash
# ==============================================================================
# Bash 13: Docker & Container Lifecycle Scripting
# MUSTERLÖSUNG
# ==============================================================================

poll_container_health() {
    local container_name="${1:-}"
    local max_retries="${2:-5}"
    local sleep_sec="${3:-1}"

    if [ -z "$container_name" ]; then
        return 1
    fi

    local attempt=1
    while [ "$attempt" -le "$max_retries" ]; do
        local status
        status=$(docker inspect --format='{{.State.Health.Status}}' "$container_name" 2>/dev/null || true)
        
        if [ "$status" = "healthy" ]; then
            echo "CONTAINER_HEALTHY: $container_name"
            return 0
        fi

        attempt=$((attempt + 1))
        if [ "$attempt" -le "$max_retries" ]; then
            sleep "$sleep_sec"
        fi
    done

    echo "CONTAINER_TIMEOUT: $container_name"
    return 1
}

build_volume_backup_command() {
    local volume="${1:-}"
    local host_dir="${2:-}"
    local archive="${3:-}"

    if [ -z "$volume" ] || [ -z "$host_dir" ] || [ -z "$archive" ]; then
        return 1
    fi

    echo "docker run --rm -v ${volume}:/volume_data -v ${host_dir}:/backup alpine tar czf /backup/${archive} -C /volume_data ."
}

build_docker_prune_command() {
    local all_flag="${1:-false}"
    local until_hours="${2:-}"

    local cmd="docker system prune -f"

    if [ "$all_flag" = "true" ]; then
        cmd="$cmd -a"
    fi

    if [ -n "$until_hours" ]; then
        cmd="$cmd --filter \"until=${until_hours}h\""
    fi

    echo "$cmd"
}

parse_container_stats_json() {
    local json_str="${1:-}"

    if [ -z "$json_str" ]; then
        return 1
    fi

    local name cpu mem
    if command -v jq >/dev/null 2>&1; then
        name=$(echo "$json_str" | jq -r '.name // empty' 2>/dev/null || true)
        cpu=$(echo "$json_str" | jq -r '.cpu // empty' 2>/dev/null || true)
        mem=$(echo "$json_str" | jq -r '.mem_usage // empty' 2>/dev/null || true)
    else
        # POSIX sed regex extraction
        name=$(echo "$json_str" | sed -n 's/.*"name"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p')
        cpu=$(echo "$json_str" | sed -n 's/.*"cpu"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p')
        mem=$(echo "$json_str" | sed -n 's/.*"mem_usage"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p')
    fi

    if [ -z "$name" ] || [ -z "$cpu" ] || [ -z "$mem" ]; then
        return 1
    fi

    echo "CONTAINER: $name | CPU: $cpu | MEM: $mem"
}
