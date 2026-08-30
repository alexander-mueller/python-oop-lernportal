# Go 10: Channels, Pufferung & Daten-Pipelines 📦

Willkommen zu **Modul 10** des Go Cloud & Concurrency Lehrpfads!

Channels sind das Herzstück von Gos Concurrency-Philosophie (nach Hoares CSP &ndash; Communicating Sequential Processes). In diesem Modul baust du datengetriebene Streaming-Pipelines zur Verarbeitung strukturierter Server-Logs.

---

## 💡 1. Das Wichtigste in Kürze

### Channel-Typen
- **Ungepuffert (`make(chan T)`)**: Senden und Empfangen finden zeitgleich statt (Handshake / Rendezvous). Blockiert, bis die Gegenseite bereit ist.
- **Gepuffert (`make(chan T, n)`)**: Fasst bis zu `n` Elemente in einer Warteschlange. Senden blockiert erst, wenn der Puffer voll ist.

### Channel-Direktionen
- `chan T`: Bidirektionaler Kanal (kann senden und empfangen).
- `chan<- T`: Send-only Kanal (darf nur befüllt werden: `ch <- item`).
- `<-chan T`: Receive-only Kanal (darf nur ausgelesen werden: `item := <-ch`).

### Sauberes Schließen und Iterieren
```go
// Producer:
func Generator() <-chan int {
    out := make(chan int, 10)
    go func() {
        defer close(out) // Wichtig: Immer schließen, wenn keine Daten mehr folgen!
        for i := 1; i <= 5; i++ {
            out <- i
        }
    }()
    return out
}

// Consumer:
ch := Generator()
for val := range ch { // for..range bricht automatisch ab, sobald der Channel geschlossen ist
    fmt.Println(val)
}
```

---

## 🎯 Aufgaben in `aufgabe.go`

1. **TODO 1 (`LogRecord`)**: Definiere das Struct `LogRecord` mit `ID int`, `Level string` ("INFO", "WARN", "ERROR"), `Message string` und `Source string`.
2. **TODO 2 (`ProduceLogs`)**: Erstelle einen Generator `ProduceLogs(records []LogRecord) <-chan LogRecord`, der alle Records in einer Hintergrund-Goroutine sendet und den Kanal am Ende schließt.
3. **TODO 3 (`FilterLogs`)**: Schreibe die Pipeline-Stufe `FilterLogs(in <-chan LogRecord, targetLevel string) <-chan LogRecord`, die nur Einträge mit `Level == targetLevel` an den Ausgangskanal weiterleitet.
4. **TODO 4 (`CountLogsByLevel`)**: Schreibe die Aggregator-Funktion `CountLogsByLevel(in <-chan LogRecord) map[string]int`, die alle Events liest und ein Dictionary mit den Vorkommen pro Log-Level zurückgibt.

---

## 🧪 Tests ausführen

```bash
go test -v ./...
```
