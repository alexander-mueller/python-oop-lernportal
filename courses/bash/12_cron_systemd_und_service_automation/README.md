# Bash 12: Cronjobs, Systemd Service Units & Logrotation ⏱️

Willkommen zu **Modul 12**! In diesem Modul lernst du, wie Services und zyklische Aufgaben auf modernen Linux-Systemen betrieben, überwacht und automatisch rotiert werden.

---

## 💡 1. Das Wichtigste in Kürze

### 1.1 Crontab Automation
Klassische zeitgesteuerte Ausführung via `cron`:
```bash
# ┌───────────── Minute (0 - 59)
# │ ┌───────────── Stunde (0 - 23)
# │ │ ┌───────────── Tag des Monats (1 - 31)
# │ │ │ ┌───────────── Monat (1 - 12)
# │ │ │ │ ┌───────────── Wochentag (0 - 6, 0=Sonntag)
# │ │ │ │ │
# * * * * * befehl >> /var/log/cron.log 2>&1

# Alle 15 Minuten:
*/15 * * * * /opt/scripts/backup.sh >> /var/log/backup.log 2>&1
```

### 1.2 Systemd Service Units (`.service`)
Systemd ist der moderne Init- und Service-Manager unter Linux. Eine `.service`-Datei liegt in `/etc/systemd/system/`:
```ini
[Unit]
Description=My Cloud Worker
After=network.target

[Service]
Type=simple
User=devops
ExecStart=/usr/local/bin/worker.sh
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```
Befehle:
- `sudo systemctl daemon-reload`
- `sudo systemctl enable --now my-service.service`
- `sudo systemctl status my-service.service`

### 1.3 Systemd Timers (`.timer`) als moderner Cron-Ersatz
Systemd Timer bieten präziseres Scheduling, Abhängigkeitsmanagement und Boot-Time Tracking (`Persistent=true`):
```ini
[Unit]
Description=Nightly Database Backup Timer

[Timer]
OnCalendar=*-*-* 02:30:00
Persistent=true
Unit=db-backup.service

[Install]
WantedBy=timers.target
```

### 1.4 Logrotation (`logrotate`)
Verhindert das Überlaufen der Festplatte durch automatische Archivierung und Komprimierung in `/etc/logrotate.d/`:
```text
/var/log/app/*.log {
    daily
    rotate 7
    missingok
    notifempty
    compress
}
```

---

## 🎯 Aufgaben in `aufgabe.sh`

1. **`generate_cron_entry(schedule, script_path, log_path)`**:
   Erzeugt eine vollständige Crontab-Zeile inklusive `>> <log> 2>&1` Umleitung.
2. **`generate_systemd_service(description, exec_start, user, restart)`**:
   Generiert eine standardkonforme `.service` Unit mit Unit-, Service- und Install-Sektionen.
3. **`generate_systemd_timer(description, on_calendar, service_unit)`**:
   Erstellt eine korrespondierende `.timer` Unit mit `Persistent=true` und `WantedBy=timers.target`.
4. **`generate_logrotate_config(log_path, frequency, rotate_count, compress_flag)`**:
   Erzeugt eine valide `logrotate` Konfiguration.

---

## 🧪 Tests ausführen

```bash
# Eigene Lösung testen:
bash test_aufgabe.sh

# Musterlösung testen:
bash test_aufgabe.sh musterloesung.sh
```
