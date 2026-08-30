# Go 13: HTTP Web Server & Routing 🌐

Willkommen zu **Modul 13** des Go Cloud & Concurrency Lehrpfads!

In diesem Modul tauchst du in Lehrpfad 4 ein: Du entwickelst performante HTTP-Webdienste mit der Go-Standardbibliothek `net/http`, verarbeitest Query-Parameter und URL-Pfade und lernst das Testen von Web-Handlern mit `httptest`.

---

## 💡 1. Das Wichtigste in Kürze

### Die Signatur eines Go HTTP-Handlers
```go
func MyHandler(w http.ResponseWriter, r *http.Request) {
    // 1. HTTP-Methode prüfen
    if r.Method != http.MethodGet {
        http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
        return
    }

    // 2. Query-Parameter lesen: /search?q=golang
    query := r.URL.Query().Get("q")

    // 3. Statuscode setzen & Text schreiben
    w.WriteHeader(http.StatusOK)
    fmt.Fprintf(w, "Suche nach: %s", query)
}
```

### Der `http.ServeMux` Router
Ein `ServeMux` verwaltet Routen. Pfade mit abschließendem Slash (z.B. `/users/`) fungieren als Subtree-Präfixe (matchen `/users/alice`, `/users/bob`).

---

## 🎯 Aufgaben in `aufgabe.go`

1. **TODO 1 (`HealthHandler`)**:
   - Reagiert auf GET `/health`.
   - Bei anderen HTTP-Methoden: `405 Method Not Allowed`.
   - Bei GET: Status `200 OK` mit Body `"STATUS: UP"`.
2. **TODO 2 (`EchoHandler`)**:
   - Liest den Query-Parameter `?msg=...`.
   - Wenn `msg` fehlt oder leer ist: Status `400 Bad Request` mit `"missing msg parameter"`.
   - Sonst: Status `200 OK` mit `"ECHO: " + msg`.
3. **TODO 3 (`UserProfileHandler`)**:
   - Extrahiert den Usernamen aus Pfad `/users/{username}` (z.B. `strings.TrimPrefix(r.URL.Path, "/users/")`).
   - Wenn leer: Status `400 Bad Request` ("username required").
   - Sonst: Status `200 OK` mit `"User Profile: " + username`.
4. **TODO 4 (`SetupAPIRouter`)**:
   - Erstellt einen `*http.ServeMux` und registriert:
     - `/health` -> `HealthHandler`
     - `/echo` -> `EchoHandler`
     - `/users/` -> `UserProfileHandler`

---

## 🧪 Tests ausführen

```bash
go test -v ./...
```
