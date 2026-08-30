#!/usr/bin/env bash
# ==============================================================================
# Bash 12: Cronjobs, Systemd Service Units & Logrotation
# MUSTERLÖSUNG
# ==============================================================================

generate_cron_entry() {
    local schedule="${1:-}"
    local script_path="${2:-}"
    local log_path="${3:-}"

    if [ -z "$schedule" ] || [ -z "$script_path" ] || [ -z "$log_path" ]; then
        return 1
    fi

    echo "$schedule $script_path >> $log_path 2>&1"
}

generate_systemd_service() {
    local description="${1:-}"
    local exec_start="${2:-}"
    local user="${3:-}"
    local restart="${4:-always}"

    if [ -z "$description" ] || [ -z "$exec_start" ] || [ -z "$user" ]; then
        return 1
    fi

    cat <<EOF
[Unit]
Description=$description
After=network.target

[Service]
Type=simple
User=$user
ExecStart=$exec_start
Restart=$restart
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF
}

generate_systemd_timer() {
    local description="${1:-}"
    local on_calendar="${2:-}"
    local service_unit="${3:-}"

    if [ -z "$description" ] || [ -z "$on_calendar" ] || [ -z "$service_unit" ]; then
        return 1
    fi

    cat <<EOF
[Unit]
Description=$description

[Timer]
OnCalendar=$on_calendar
Persistent=true
Unit=$service_unit

[Install]
WantedBy=timers.target
EOF
}

generate_logrotate_config() {
    local log_path="${1:-}"
    local frequency="${2:-daily}"
    local rotate_count="${3:-7}"
    local compress_flag="${4:-true}"

    if [ -z "$log_path" ] || [ -z "$frequency" ] || [ -z "$rotate_count" ]; then
        return 1
    fi

    local comp_str="compress"
    if [ "$compress_flag" = "false" ]; then
        comp_str="nocompress"
    fi

    cat <<EOF
$log_path {
    $frequency
    rotate $rotate_count
    missingok
    notifempty
    $comp_str
}
EOF
}
