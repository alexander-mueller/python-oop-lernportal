# Go 11: select Multiplexing, Context & Timeouts ⚡

Willkommen zu **Modul 11** des Go Cloud & Concurrency Lehrpfads!

In verteilten Cloud-Systemen müssen Services tolerant gegenüber Netzwerklatenzen und Ausfällen sein. Mit `select`, nicht-blockierenden Channel-Operationen und `context.Context` baust du robuste, zeitgesteuerte und abbrechbare Workflows.

---

## 💡 1. Das Wichtigste in Kürze

### `select` Multiplexing
- Lauscht gleichzeitig auf mehrere Channels.
- Der erste bereite Channel-Case gewinnt.
- Sind mehrere bereit, entscheidet Go pseudozufällig.
- Mit `default` wird der Code sofort nicht-blockierend ausgeführt, falls kein Channel bereit ist.

### Timeouts mit `time.After`
```go
select {
case res := <-responseCh:
    fmt.Println("Ergebnis erhalten:", res)
case <-time.After(500 * time.Millisecond):
    fmt.Println("Timeout nach 500ms!")
}
```

### Cancellation mit `context.Context`
```go
ctx, cancel := context.WithTimeout(context.Background(), 2*time.Second)
defer cancel()

select {
case <-ctx.Done():
    return "", ctx.Err() // context.DeadlineExceeded oder context.Canceled
case data := <-workCh:
    return data, nil
}
```

---

## 🎯 Aufgaben in `aufgabe.go`

1. **TODO 1 (`FastestResponse`)**: Lies aus zwei Kanälen `ch1` und `ch2` mit `select` das schnellste Ergebnis aus und gib es zurück.
2. **TODO 2 (`FetchWithTimeout`)**: Warte auf Daten aus `ch`. Wenn innerhalb von `timeout` keine Daten eintreffen, gib einen Fehler `errors.New("timeout exceeded")` zurück.
3. **TODO 3 (`TrySend` & `TryReceive`)**:
   - `TrySend(ch chan<- int, val int) bool`: Sende ohne zu blockieren (gibt `true` bei Erfolg, `false` bei vollem Kanal).
   - `TryReceive(ch <-chan int) (int, bool)`: Lies ohne zu blockieren (gibt `(val, true)` bei Daten, `(0, false)` bei leerem Kanal).
4. **TODO 4 (`QueryWithContext`)**: Führe die Funktion `fn func() string` in einer Goroutine aus und reagiere auf `<-ctx.Done()` für saubere Stornierung.

---

## 🧪 Tests ausführen

```bash
go test -v ./...
```
