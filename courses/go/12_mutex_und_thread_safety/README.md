# Go 12: Race Conditions, sync.Mutex & Atomics 🛡️

Willkommen zu **Modul 12** des Go Cloud & Concurrency Lehrpfads!

In diesem Modul lernst du, wie du veränderliche Zustände in hochgradig parallelen Go-Anwendungen schützt. Du implementierst einen thread-sicheren In-Memory Cache mit `sync.RWMutex`, einen lock-freien Zähler mit `sync/atomic` und ein abgesichertes Bankkonto.

---

## 💡 1. Das Wichtigste in Kürze

### `sync.Mutex` vs. `sync.RWMutex`
- **`sync.Mutex`**:
  - `mu.Lock()` & `mu.Unlock()`
  - Schützt kritische Abschnitte exklusiv. Es darf immer nur genau eine Goroutine im Block sein.
- **`sync.RWMutex`**:
  - `mu.RLock()` & `mu.RUnlock()` für parallele Leser.
  - `mu.Lock()` & `mu.Unlock()` für exklusive Schreiber.
  - Ideal für leselastige Caches (Read-Heavy Caches).

### Lock-Free mit `sync/atomic`
Für einfache Zähler oder Flags benötigt man keinen Mutex. `sync/atomic` nutzt direkte CPU-Befehle:
- `atomic.AddInt64(&counter, 1)`
- `atomic.LoadInt64(&counter)`
- `atomic.StoreInt64(&counter, 0)`

---

## 🎯 Aufgaben in `aufgabe.go`

1. **TODO 1 & 2 (`SafeCache`)**:
   - Definiere das Struct `SafeCache` mit `mu sync.RWMutex` und `items map[string]string`.
   - `Set(key, val string)`: Schreibt mit `mu.Lock()`.
   - `Get(key string) (string, bool)`: Liest mit `mu.RLock()`.
   - `Delete(key string)`: Löscht mit `mu.Lock()`.
   - `Len() int`: Gibt die Elementanzahl mit `mu.RLock()` zurück.
2. **TODO 3 (`AtomicCounter`)**:
   - Definiere `AtomicCounter` mit `val int64`.
   - Implementiere `Inc() int64`, `Add(delta int64) int64`, `Value() int64` und `Reset()`.
3. **TODO 4 (`SafeBankAccount`)**:
   - Definiere `SafeBankAccount` mit `mu sync.Mutex` und `balance float64`.
   - `Deposit(amount float64)`: Erhöht das Guthaben sicher.
   - `Withdraw(amount float64) error`: Zieht Guthaben ab, wenn `balance >= amount`, sonst liefert es einen Fehler (`errors.New("insufficient funds")`).
   - `Balance() float64`: Gibt das aktuelle Guthaben zurück.

---

## 🧪 Tests & Race Detector ausführen

```bash
go test -v -race ./...
```
