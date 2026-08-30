# Go 09: Leichtgewichtige Goroutines & sync.WaitGroup 🚀

Willkommen zu **Modul 09** des Go Cloud & Concurrency Lehrpfads!

In diesem Modul lernst du, wie Gos bahnbrechendes Concurrency-Modell funktioniert, wie du Goroutines mit dem `go`-Schlüsselwort startest und wie du nebenläufige Workloads mit `sync.WaitGroup` deterministisch synchronisierst.

---

## 💡 1. Das Wichtigste in Kürze

### Was macht Goroutines so mächtig?
- **Geringer Footprint**: Eine Goroutine benötigt anfangs nur **ca. 2 KB** Stack (im Vergleich zu 1–2 MB bei klassischen OS-Threads).
- **Go Runtime Scheduler**: Go verwendet ein **M:N Multiplexing-Modell** (G-P-M Modell: Goroutines werden auf logische Prozessoren und physische OS-Threads gemappt).
- **Nicht-präemptiv / Kooperativ**: Umschalten zwischen Goroutines passiert blitzschnell bei I/O, Channel-Operationen, Mutex-Sperren oder Funktionsaufrufen.

### Das `sync.WaitGroup` Dreigespann
Um auf das Beenden von Hintergrund-Goroutines zu warten, verwenden wir `sync.WaitGroup`:
1. `wg.Add(n)`: Erhöht den Zähler um die Anzahl geplanter Goroutines (immer **vor** dem `go`-Aufruf ausführen!).
2. `defer wg.Done()`: Dekrementiert den Zähler beim Beenden der Goroutine.
3. `wg.Wait()`: Blockiert, bis der Zähler 0 erreicht.

```go
var wg sync.WaitGroup

for i := 0; i < 5; i++ {
    wg.Add(1)
    go func(workerID int) {
        defer wg.Done()
        fmt.Printf("Worker %d erledigt Aufgabe\n", workerID)
    }(i) // Variable als Parameter übergeben
}

wg.Wait()
fmt.Println("Alle 5 Worker sind fertig!")
```

> ⚠️ **ACHTUNG**: `sync.WaitGroup` darf **niemals als Wertkopie** an Funktionen übergeben werden, sondern immer als Pointer (`*sync.WaitGroup`), da sonst die interne Zählung verloren geht und ein Deadlock entsteht!

---

## 🎯 Aufgaben in `aufgabe.go`

1. **TODO 1 (`ServerMetric`)**: Definiere das Struct `ServerMetric` mit Feldern `ServerID string`, `LatencyMs int`, `Status string` und `Timestamp time.Time`.
2. **TODO 2 (`CheckServer`)**: Schreibe die Worker-Funktion `CheckServer(serverID string, wg *sync.WaitGroup, out chan<- ServerMetric)`. Nutze `defer wg.Done()`.
3. **TODO 3 (`BatchHealthCheck`)**: Starte für eine Server-Liste parallele Goroutines mit `sync.WaitGroup`, sammle alle Metriken ein und gib sie sortiert nach ServerID zurück.
4. **TODO 4 (`ParallelTaskRunner`)**: Führe einen Slice von `tasks []func() string` nebenläufig aus und sammle alle Ergebnisse exakt in der Reihenfolge ihrer Indizes ein.

---

## 🧪 Tests ausführen

Starte die Testsuite im Terminal oder in der Web-IDE:
```bash
go test -v ./...
```
