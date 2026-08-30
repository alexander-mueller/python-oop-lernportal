# Bash 11: Remote SSH, REST-Pipelines (curl) & rsync Automatisierung 🌐

Willkommen zu **Modul 11**! In der modernen Cloud-Infrastruktur müssen Bash-Skripte mit Microservices über REST-APIs kommunizieren, Remote-Server per SSH headless orchestrieren und Datenbestände synchronisieren.

---

## 💡 1. Das Wichtigste in Kürze

### 1.1 REST-APIs mit `curl`
Ein professioneller API-Aufruf in Bash benötigt Fehlerbehandlung, Header und Zeitlimits:
```bash
# 🎯 Robuster POST-Request mit JSON-Payload & Token:
response=$(curl -s -f -X POST "https://api.cloud.com/v1/alerts" \
  -H "Authorization: Bearer $API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"status":"CRITICAL","message":"High CPU load"}')

# 🎯 Nur den HTTP-Statuscode abfragen (Health Check):
http_code=$(curl -s -o /dev/null -w "%{http_code}" "https://app.corp/health")
if [ "$http_code" -ne 200 ]; then
    echo "🚨 Service Down! Status: $http_code"
fi
```

### 1.2 Non-Interactive Remote SSH Automation
Um Server in CI/CD-Pipelines ohne interaktive Passwort-/Key-Prompts sicher zu steuern:
```bash
# 🎯 Lokales Skript direkt auf Remote-Server ausführen:
ssh -o BatchMode=yes -o StrictHostKeyChecking=no deploy@server.corp "bash -s" < deploy_script.sh

# 🎯 Remote-Befehlsausgabe in lokales Array einlesen:
readarray -t active_containers < <(ssh deploy@server.corp "docker ps -q")
```

### 1.3 Intelligente Synchronisation mit `rsync`
`rsync` synchronisiert nur geänderte Datenblöcke (Delta-Transfer):
```bash
# -a: Archiv (Rechte, Zeitstempel, symlinks)
# -v: Verbose
# -z: Komprimierung während der Übertragung
# --delete: Löscht Dateien im Ziel, die an der Quelle gelöscht wurden
rsync -avz --delete --exclude="*.log" --exclude=".git" /var/www/ app@backup-server:/var/www/
```

---

## 🎯 Aufgaben in `aufgabe.sh`

1. **`build_curl_post_command(endpoint, token, payload)`**:
   Formatiert einen robusten `curl -s -f -X POST` Befehl mit Auth- und Content-Type Headern.
2. **`get_http_status_code(url)`**:
   Gibt ausschließlich den HTTP Status-Code (z.B. 200, 404, 500) via `curl -s -o /dev/null -w "%{http_code}"` zurück.
3. **`build_ssh_batch_command(user, host, script_file, port)`**:
   Erstellt ein headless SSH-Kommando mit `BatchMode=yes`, `StrictHostKeyChecking=no` und `"bash -s" < script`.
4. **`build_rsync_command(src, dest, exclude_pattern, delete_flag)`**:
   Konstruiert ein `rsync -avz` Synchronisationskommando mit optionalen Flags `--delete` und `--exclude`.

---

## 🧪 Tests ausführen

```bash
# Eigene Lösung testen:
bash test_aufgabe.sh

# Musterlösung testen:
bash test_aufgabe.sh musterloesung.sh
```
