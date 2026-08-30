# Go 14: REST JSON APIs & Middleware-Pipelines 🛡️

Willkommen zu **Modul 14** des Go Cloud & Concurrency Lehrpfads!

RESTful JSON APIs sind das Rückgrat moderner Cloud-Microservices. In diesem Modul lernst du das Zusammenspiel von Struct-Tags, JSON-Streaming und modularen Middleware-Chains (Authentication, Recovery & Logging).

---

## 💡 1. Das Wichtigste in Kürze

### JSON Struct Tags
```go
type Device struct {
    ID     int    `json:"id"`
    Name   string `json:"name"`
    IP     string `json:"ip"`
    Active bool   `json:"active"`
}
```

### JSON Dekodierung & Enkodierung
```go
// 1. JSON lesen:
var req Device
if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
    http.Error(w, `{"error":"invalid json"}`, http.StatusBadRequest)
    return
}

// 2. JSON antworten:
w.Header().Set("Content-Type", "application/json")
w.WriteHeader(http.StatusOK)
json.NewEncoder(w).Encode(response)
```

### Das Middleware Chaining Pattern
```go
func ApplyMiddleware(h http.Handler, middlewares ...func(http.Handler) http.Handler) http.Handler {
    for i := len(middlewares) - 1; i >= 0; i-- {
        h = middlewares[i](h)
    }
    return h
}
```

---

## 🎯 Aufgaben in `aufgabe.go`

1. **TODO 1 (`Device` & `APIResponse`)**: Definiere die Structs mit passenden JSON-Tags (`json:"id"`, `json:"name"`, `json:"ip"`, `json:"active"`, `json:"success"`, `json:"message"`, `json:"data,omitempty"`).
2. **TODO 2 (`GetDevicesHandler` & `CreateDeviceHandler`)**:
   - `GetDevicesHandler`: Gibt die aktuelle Liste als JSON zurück.
   - `CreateDeviceHandler`: Parst den JSON-Body, validiert `Name` und `IP` (dürfen nicht leer sein), vergibt ID und hängt das Gerät an.
3. **TODO 3 (`AuthMiddleware`)**: Prüft den Header `X-API-Key`. Stimmt er nicht mit dem erwarteten Schlüssel überein, liefert die Middleware `401 Unauthorized`.
4. **TODO 4 (`RecoveryMiddleware` & `ApplyMiddleware`)**: Fängt unerwartete Panics mit `recover()` ab und antwortet mit Status `500 Internal Server Error`.

---

## 🧪 Tests ausführen

```bash
go test -v ./...
```
