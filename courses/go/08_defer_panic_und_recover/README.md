# Go 08: Ressourcensicherheit mit defer & Recover 🛡️

Willkommen zu **Modul 08** des Go (Golang) Kurses!

In diesem Modul lernst du, wie Go Ressourcenbereinigung und Crash-Prävention handhabt: Verzögerte Ausführung mit `defer` (LIFO-Stack), fatale Systemzustände mit `panic` und Absicherung kritischer Programmteile mit `recover()`.

---

## 💡 1. Das Wichtigste in Kürze

### `defer`
Anweisungen mit `defer` werden garantiert ausgeführt, sobald die umschließende Funktion beendet wird.
- **LIFO:** Mehrere `defer`-Aufrufe werden in umgekehrter Reihenfolge abgearbeitet (wie ein Stack).
- **Einsatzgebiete:** `file.Close()`, `mutex.Unlock()`, Datenbank-Verbindungen schließen.

### `panic` & `recover`
- `panic(val)` bricht die normale Funktionsausführung ab und läuft den Call-Stack hoch.
- `recover()` fängt einen laufenden Panic ab, funktioniert jedoch **ausschließlich innerhalb einer defer-Funktion**.

```go
func SafeRun() {
    defer func() {
        if r := recover(); r != nil {
            fmt.Println("Panic abgefangen:", r)
        }
    }()
    panic("Schwerwiegender Systemausfall")
}
```

---

## 🎯 Teilziele in `aufgabe.go`

1. **TODO 1:** `ProtokollierteOperation(name string, logEntries *[]string) string` mit `defer` LIFO Logging implementieren.
2. **TODO 2:** `RessourcenManager` mit `Acquire()` und `Release()` über `defer` steuern.
3. **TODO 3:** `KritischeBerechnung(teiler int) int` mit `panic("division durch null")` bei `teiler == 0`.
4. **TODO 4:** `SichereAusfuehrung(fn func()) (recoveredErr any, ok bool)` mit `defer` und `recover()` implementieren.
