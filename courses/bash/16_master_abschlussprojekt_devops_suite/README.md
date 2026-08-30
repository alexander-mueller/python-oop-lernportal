# Master 16: DevOps Multi-Server Automation Suite 💎

Herzlichen Glückwunsch zum Erreichen des **Master-Abschlussprojekts (Modul 16)**! In diesem Projekt führst du alle Techniken aus den Lehrpfaden 1 bis 4 zu einer produktionsreifen DevOps-Orchestrierungs- und Monitoring-Suite zusammen.

---

## 💡 1. Das Projekt im Überblick

Die Multi-Server Automation Suite erfüllt alle Kernaufgaben moderner SRE- & DevOps-Teams:

1. **CLI Steuerung & Flags**: Flexible Steuerung über Optionen (`-c / --config`, `-p / --parallel`, `--dry-run`).
2. **Multi-Threaded Server Health Fleet Check**: Hunderte Server parallel mit Background-Worker Pools und Drosselung auf Verfügbarkeit prüfen.
3. **Parallele Log-Mining & Incident Engine**: Verteiltes Durchsuchen von GB-großen Server-Log-Verzeichnissen mit `xargs -P` nach Fehlern (`HTTP 5xx`, `Kernel Panics`, `OOM-Kills`).
4. **Webhook Alert Dispatcher**: Automatische Alarmierung über REST-Webhooks (Slack, Discord, Teams) bei Ausfällen.
5. **Dashboard-Generierung**: Automatisierte Erstellung übersichtlicher HTML-Statusberichte für Teams und Dashboards.

---

## 🏗️ 2. Architektur & Workflow

```text
[CLI Arguments] ──▶ [Worker Pool: Health Checks] ──▶ [Incident Log Mining (xargs -P)]
                             │                                    │
                             ▼                                    ▼
                 [Webhook Alert Dispatcher] ◀───────── [HTML Dashboard Generator]
```

---

## 🎯 Aufgaben in `aufgabe.sh`

1. **`parse_devops_cli_args("$@")`**:
   Parst Kommandozeilen-Argumente (`-c`, `-p`, `--dry-run`) und formatiert die Konfiguration.
2. **`parallel_server_health_check(servers_file, max_workers)`**:
   Prüft Server parallel im Hintergrund, drosselt Concurrency und synchronisiert mit `wait`.
3. **`analyze_server_logs_parallel(log_dir, pattern, max_threads)`**:
   Durchsucht Logdateien parallel mit `xargs -P` und summiert Treffer auf.
4. **`build_webhook_payload(webhook_url, title, message, severity)`**:
   Erzeugt den formatierten `curl -X POST` Webhook-Befehl mit JSON-Body.
5. **`generate_devops_html_report(title, healthy, total, incidents, output_file)`**:
   Generiert eine vollständige HTML-Dashboard Datei für den Flotten-Status.

---

## 🧪 Tests ausführen

```bash
# Eigene Lösung testen:
bash test_aufgabe.sh

# Musterlösung testen:
bash test_aufgabe.sh musterloesung.sh
```
