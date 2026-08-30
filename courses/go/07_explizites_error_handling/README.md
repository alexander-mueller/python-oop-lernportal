# Go 07: Explizites Error-Handling ⚡

Willkommen zu **Modul 07** des Go (Golang) Kurses!

In diesem Modul lernst du das fehlerrobuste Paradigma von Go kennen: Keine unkontrollierten Exceptions, sondern explizite Rückgabewerte (`if err != nil`), vordefinierte Sentinel Errors, Error-Wrapping mit `%w` und Custom Error-Structs.

---

## 💡 1. Das Wichtigste in Kürze

### Fehler sind Werte
Das Go `error`-Interface erfordert lediglich eine Methode:
```go
type error interface {
    Error() string
}
```

### Sentinel Errors
Globale, unveränderliche Fehlervariablen:
```go
var ErrNotFound = errors.New("eintrag nicht gefunden")
```

### Error Wrapping
Kontextinformationen hinzufügen, ohne die ursprüngliche Fehlerursache zu zerstören:
```go
return fmt.Errorf("datenbank-abfrage fehlgeschlagen: %w", err)
```

### Eigene Error-Structs
Strukturierte Zusatzdaten (wie Fehlercodes) als Struct kapseln:
```go
type QueryError struct {
    Query string
    Err   error
}
func (e *QueryError) Error() string { return fmt.Sprintf("Fehler bei %s: %v", e.Query, e.Err) }
```

---

## 🎯 Teilziele in `aufgabe.go`

1. **TODO 1:** Sentinel Errors `ErrInvalidAmount` und `ErrInsufficientFunds` definieren.
2. **TODO 2:** Struct `BankAccount` mit `Deposit` und `Withdraw` Methoden implementieren.
3. **TODO 3:** Custom Struct `APIError` mit `Error() string` definieren.
4. **TODO 4:** `ExecuteRequest(endpoint, token string) (string, error)` mit Error-Wrapping umsetzen.
