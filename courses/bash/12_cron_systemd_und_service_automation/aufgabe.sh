#!/usr/bin/env bash
# ==============================================================================
# Bash 12: Cronjobs, Systemd Service Units & Logrotation
# ==============================================================================
# In diesem Modul lernst du, wie Hintergrunddienste und periodische Automatisierungen
# in professionellen Linux-Server-Umgebungen aufgesetzt und verwaltet werden.
# ==============================================================================

# ------------------------------------------------------------------------------
# TODO 1: Crontab-Eintrag mit Output-Redirection generieren
# ------------------------------------------------------------------------------
# Implementiere die Funktion `generate_cron_entry`.
# Parameter:
#   $1: Zeitplan im Cron-Format (z.B. "*/15 * * * *")
#   $2: Absoluter Pfad zum Skript (z.B. "/opt/scripts/backup.sh")
#   $3: Absoluter Pfad zur Logdatei (z.B. "/var/log/backup.log")
# Verhalten:
#   - Validiert, dass alle 3 Parameter übergeben wurden (sonst return 1).
#   - Gibt die formatierte Crontab-Zeile aus:
#     <schedule> <script_path> >> <log_path> 2>&1
# ------------------------------------------------------------------------------
generate_cron_entry() {
    local schedule="${1:-}"
    local script_path="${2:-}"
    local log_path="${3:-}"

    # TODO: Validiere Parameter
    # TODO: Gib formatierte Zeile aus
    echo "TODO: Implementiere generate_cron_entry"
    return 1
}

# ------------------------------------------------------------------------------
# TODO 2: Standardkonforme Systemd Service Unit (.service) erstellen
# ------------------------------------------------------------------------------
# Implementiere die Funktion `generate_systemd_service`.
# Parameter:
#   $1: Service Name / Description (z.B. "DevOps Metric Collector")
#   $2: ExecStart Befehl / Skriptpfad (z.B. "/usr/local/bin/collector.sh")
#   $3: Linux Benutzer für Ausführung (z.B. "devops")
#   $4: Restart-Verhalten (z.B. "always" oder "on-failure", Default: "always")
# Verhalten:
#   - Gibt eine saubere Systemd Unit im INI-Format aus:
#     [Unit]
#     Description=<description>
#     After=network.target
#
#     [Service]
#     Type=simple
#     User=<user>
#     ExecStart=<exec_start>
#     Restart=<restart>
#     RestartSec=5
#
#     [Install]
#     WantedBy=multi-user.target
#   - Bei fehlenden Pflicht-Parametern ($1, $2, $3): Return 1.
# ------------------------------------------------------------------------------
generate_systemd_service() {
    local description="${1:-}"
    local exec_start="${2:-}"
    local user="${3:-}"
    local restart="${4:-always}"

    # TODO: Validiere Parameter
    # TODO: Gib Systemd Service Definition aus
    echo "TODO: Implementiere generate_systemd_service"
    return 1
}

# ------------------------------------------------------------------------------
# TODO 3: Systemd Timer Unit (.timer) erstellen
# ------------------------------------------------------------------------------
# Implementiere die Funktion `generate_systemd_timer`.
# Parameter:
#   $1: Beschreibung (z.B. "Run Metric Collector Every 10 Minutes")
#   $2: OnCalendar Zeitplan (z.B. "*:0/10" oder "daily")
#   $3: Name des zugehörigen Services (z.B. "collector.service")
# Verhalten:
#   - Gibt eine saubere Systemd Timer Unit aus:
#     [Unit]
#     Description=<description>
#
#     [Timer]
#     OnCalendar=<on_calendar>
#     Persistent=true
#     Unit=<service_unit>
#
#     [Install]
#     WantedBy=timers.target
#   - Bei fehlenden Parametern: Return 1.
# ------------------------------------------------------------------------------
generate_systemd_timer() {
    local description="${1:-}"
    local on_calendar="${2:-}"
    local service_unit="${3:-}"

    # TODO: Validiere Parameter
    # TODO: Gib Systemd Timer Definition aus
    echo "TODO: Implementiere generate_systemd_timer"
    return 1
}

# ------------------------------------------------------------------------------
# TODO 4: Logrotate Konfigurationsdatei generieren
# ------------------------------------------------------------------------------
# Implementiere die Funktion `generate_logrotate_config`.
# Parameter:
#   $1: Logdatei-Pfad (z.B. "/var/log/app/*.log")
#   $2: Rotations-Frequenz (z.B. "daily" oder "weekly")
#   $3: Anzahl aufzubewahrender Archive (z.B. 7)
#   $4: Komprimierung aktivieren ("true" oder "false", Default: "true")
# Verhalten:
#   - Format:
#     <log_path> {
#         <frequency>
#         rotate <count>
#         missingok
#         notifempty
#         compress (nur wenn $4 == "true", sonst "nocompress")
#     }
#   - Bei fehlenden Parametern ($1, $2, $3): Return 1.
# ------------------------------------------------------------------------------
generate_logrotate_config() {
    local log_path="${1:-}"
    local frequency="${2:-daily}"
    local rotate_count="${3:-7}"
    local compress_flag="${4:-true}"

    # TODO: Validiere Parameter
    # TODO: Baue Logrotate Konfiguration und gib sie aus
    echo "TODO: Implementiere generate_logrotate_config"
    return 1
}
