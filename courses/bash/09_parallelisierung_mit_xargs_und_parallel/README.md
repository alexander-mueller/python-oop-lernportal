# Bash 09: Multithreading & Parallelisierung im Terminal 🚀

Willkommen zu **Modul 09** des Bash & Cloud DevOps Kurses! In modernen Server- und Cloud-Umgebungen müssen Skripte oft hunderte oder tausende I/O- oder CPU-Aufgaben gleichzeitig ausführen (z.B. Log-Analysen, API-Pollings, Dateitransfers, Bildkompression).

In diesem Modul meisterst du die Kunst der Parallelisierung direkt auf der Linux-Kommandozeile.

---

## 💡 1. Das Wichtigste in Kürze

### 1.1 `xargs -P <n>` (Parallele Ausführung mit Standard-Tools)
`xargs` liest Einträge von `stdin` und führt Befehle aus. Mit dem Parameter `-P <n>` (oder `--max-procs`) bestimmst du, wie viele Prozesse parallel laufen:
```bash
# Verarbeitet URLs parallel mit maximal 8 Threads:
cat urls.txt | xargs -P 8 -I {} curl -s -O "{}"

# Null-terminierte Strings für sichere Dateinamen mit Leerzeichen:
find . -type f -name "*.log" -print0 | xargs -0 -P 4 gzip
```

### 1.2 GNU `parallel` (Die Königsklasse der Shell-Parallelisierung)
GNU `parallel` bietet erweiterte Features wie Job-Tagging, CPU-Kern-Erkennung (`-j+0`), Fortschrittsbalken (`--bar`) und strukturierte Ausgabe (`--keep-order`):
```bash
# Führt Bildoptimierung auf allen CPU-Kernen parallel aus:
parallel -j $(nproc) --bar "convert {} -resize 800x600 opt_{}" ::: *.jpg
```

### 1.3 Native Bash Background Workers (`&`, `$!`, `wait`)
Reine Bash-Mittel ohne externe Werkzeuge für maximale Portabilität:
```bash
pids=()

for server in web01 web02 db01; do
    (
        echo "Prüfe $server..."
        ping -c 1 "$server" > /dev/null 2>&1
        echo "Fertig: $server"
    ) &
    pids+=($!)
done

# Warten auf alle Prozesse:
for pid in "${pids[@]}"; do
    wait "$pid"
done
echo "Alle Server geprüft!"
```

### 1.4 Concurrency Throttling (Worker Pool)
Um das System vor Überlastung (Too many open files / Out of Memory) zu schützen, drosseln wir die Anzahl aktiver Prozesse:
```bash
MAX_JOBS=4
for item in $(cat items.txt); do
    process_item "$item" &
    
    # Solange MAX_JOBS erreicht sind, kurz warten
    while [ $(jobs -rp | wc -l) -ge "$MAX_JOBS" ]; do
        sleep 0.05
    done
done
wait
```

---

## 🎯 Aufgaben in `aufgabe.sh`

1. **`parallel_xargs_process(input_file, max_procs)`**:
   Liest eine Textdatei und gibt für jede Zeile `PROCESSED: <item>` über `xargs -P` parallel aus.
2. **`background_workers_wait(task1, task2, ...)`**:
   Startet Hintergrund-Subshells mit `&`, sammelt deren PIDs in einem Array und synchronisiert mit `wait`.
3. **`parallel_batch_calculator(numbers_file, max_procs)`**:
   Liest Zahlen aus einer Datei, berechnet deren Quadrat parallel und liefert das Ergebnis numerisch sortiert zurück (`<n>^2 = <quadrat>`).
4. **`throttle_concurrent_jobs(total_jobs, max_concurrent)`**:
   Implementiert einen gedrosselten Worker-Pool, sodass niemals mehr als `max_concurrent` Prozesse gleichzeitig im Hintergrund laufen.

---

## 🧪 Tests ausführen

```bash
# Eigene Lösung testen:
bash test_aufgabe.sh

# Musterlösung testen:
bash test_aufgabe.sh musterloesung.sh
```
