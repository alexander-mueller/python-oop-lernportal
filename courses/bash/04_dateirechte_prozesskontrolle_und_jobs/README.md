# Bash 04: Dateirechte (chmod) & Prozesskontrolle 🛡️

Willkommen zu **Modul 04** des Linux Bash & DevOps Lehrpfads!

In diesem Modul lernst du das Unix-Berechtigungssystem (`chmod`, `chown`, Oktal vs. Symbolisch), Prozessanalyse (`ps aux`), Signal-Handling (`kill -15` vs. `kill -9`, `kill -0`) und asynchrone Job-Control (`&`, `$!`, `jobs`) kennen.

---

## 💡 1. Das Wichtigste in Kürze

### Unix-Dateirechte (Oktal-Modell)
Jede Datei besitzt Rechte für drei Entitäten: **User (u)**, **Group (g)** und **Others (o)**.
- `r` (Read) = 4
- `w` (Write) = 2
- `x` (Execute) = 1

| Modus | Bedeutung | Typischer Einsatzzweck |
|---|---|---|
| `755` | `rwxr-xr-x` | Ausführbare Skripte, Binaries, Ordner |
| `644` | `rw-r--r--` | Standard-Dateien, Konfigurationen |
| `600` | `rw-------` | Sensible Secrets, SSH Private Keys |
| `700` | `rwx------` | Private Verzeichnisse (`~/.ssh`, `~/.gnupg`) |

### Prozessüberwachung & Signale
- `ps aux` / `pgrep <name>`: Zeigt alle laufenden Prozesse an.
- `kill -0 <pid>`: Sendet ein Null-Signal zum Testen der Existenz (Exit-Code 0 = Prozess existiert und antwortet).
- `kill -15 <pid>` (**SIGTERM**): Bittet den Prozess höflich, sich sauber zu beenden (Ressourcen schließen, Buffer flushen).
- `kill -9 <pid>` (**SIGKILL**): Zwingt den Linux-Kernel, den Prozess sofort und unweigerlich zu terminieren.

### Job-Control & Hintergrundprozesse
```bash
# 1. Befehl im Hintergrund starten:
./backup.sh &

# 2. PID des zuletzt gestarteten Hintergrundprozesses:
PID=$!
echo "Backup läuft unter PID $PID"

# 3. Auf Beendigung warten:
wait $PID
```

---

## 🎯 Aufgaben in `aufgabe.sh`

1. **TODO 1 (`setze_sichere_rechte`)**: Setze per `chmod` die Rechte nach Vorgabe (`secret` -> 600, `script` -> 755, `config` -> 644).
2. **TODO 2 (`lese_oktal_rechte`)**: Lies die Oktalrechte mit `stat -c "%a"` aus.
3. **TODO 3 (`starte_hintergrund_prozess`)**: Starte `sleep` im Hintergrund mit `&` und gib die PID (`$!`) zurück.
4. **TODO 4 (`ist_prozess_am_leben`)**: Prüfe die Prozess-Existenz mit `kill -0`.
5. **TODO 5 (`stoppe_prozess_mit_fallback`)**: Sende SIGTERM (15), warte kurz und erzwinge bei Bedarf SIGKILL (9).

---

## 🧪 Tests ausführen

```bash
bash test_aufgabe.sh
```
