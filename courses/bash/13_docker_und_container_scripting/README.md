# Bash 13: Docker & Container Lifecycle Scripting 🐳

Willkommen zu **Modul 13**! Container sind das Rückgrat moderner Cloud-Native-Architekturen. In diesem Modul lernst du, wie du Container-Lifecycles, Health-Checks, automatische Datensicherungen von Docker Volumes und Ressourcen-Bereinigungen per Bash automatisierst.

---

## 💡 1. Das Wichtigste in Kürze

### 1.1 Container Health-Polling
Bevor nachfolgende Schritte in CI/CD oder Deployments laufen, muss geprüft werden, ob Dienste (wie Datenbanken) wirklich einsatzbereit sind:
```bash
# 🎯 Polling-Schleife mit Timeout:
attempt=1
max_retries=10

while [ "$attempt" -le "$max_retries" ]; do
    status=$(docker inspect --format='{{.State.Health.Status}}' my-postgres 2>/dev/null)
    if [ "$status" = "healthy" ]; then
        echo "Datenbank ist bereit!"
        break
    fi
    sleep 2
    ((attempt++))
done
```

### 1.2 Docker Volume Backup Pattern
Docker Volumes lassen sich über einen temporären Alpine-Container sichern, ohne den Host-Pfad manuell suchen zu müssen:
```bash
# 🎯 Volume in komprimiertes tar.gz auf dem Host sichern:
docker run --rm \
  -v my_volume:/volume_data \
  -v /var/backups:/backup \
  alpine tar czf /backup/my_volume_backup.tar.gz -C /volume_data .
```

### 1.3 Ressourcen-Bereinigung & Pruning
Verhindere "No space left on device" durch automatisierte Aufräumroutinen:
```bash
# 🎯 Bereinigt ungenutzte Images, Container & Netzwerke älter als 7 Tage (168 Stunden):
docker system prune -f -a --filter "until=168h"
```

---

## 🎯 Aufgaben in `aufgabe.sh`

1. **`poll_container_health(container_name, max_retries, sleep_sec)`**:
   Prüft per Schleife `docker inspect`, ob ein Container `"healthy"` meldet.
2. **`build_volume_backup_command(volume, host_dir, archive)`**:
   Erzeugt das standardkonforme `docker run --rm -v ... alpine tar czf ...` Backup-Kommando.
3. **`build_docker_prune_command(all_flag, until_hours)`**:
   Konstruiert `docker system prune -f` mit optionalen `-a` und `--filter "until=...h"` Flags.
4. **`parse_container_stats_json(json_str)`**:
   Extrahiert Container-Statistiken und formatiert die Ausgabe: `CONTAINER: <name> | CPU: <cpu> | MEM: <mem>`.

---

## 🧪 Tests ausführen

```bash
# Eigene Lösung testen:
bash test_aufgabe.sh

# Musterlösung testen:
bash test_aufgabe.sh musterloesung.sh
```
