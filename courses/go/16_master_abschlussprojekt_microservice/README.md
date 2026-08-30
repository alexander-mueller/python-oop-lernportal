# Master 16: High-Concurrency URL Shortener & Analytics Microservice API 🏆

Willkommen zum **Master-Abschlussprojekt** des Go Cloud Microservices & Systems Lehrgangs!

In diesem Abschlussprojekt baust du einen produktionsreifen Cloud-Microservice: Einen **High-Concurrency URL Shortener mit asynchroner Analytics Ingestion Engine**.

---

## 🏛️ 1. Architektur & Konzepte

Dieses Projekt vereint alle zentralen Kernkompetenzen von Go:
1. **Goroutine Worker Pool (`sync.WaitGroup`)**: Ein Pool dedizierter Worker-Goroutines verarbeitet Klick-Events im Hintergrund, ohne HTTP-Antworten zu verzögern.
2. **Buffered Channels**: Dienen als stoßfester In-Memory Event-Bus für Klick-Analysen.
3. **Thread-Safe State (`sync.RWMutex` & `sync/atomic`)**: Schnelle parallele Lesezugriffe beim URL-Lookup und atomare Metrik-Zähler ohne Lock-Overhead.
4. **RESTful HTTP API (`net/http`)**: Vollständige JSON API mit Request Decoding, Validierung und Statuscodes.
5. **Middleware Pipeline**: Recovery- und Logging-Middlewares schützen den Dienst vor unerwarteten Panics.
6. **Integration & Concurrency Tests**: Stresstest mit parallelen Schreibern und Lesern.

---

## 📡 2. Endpunkte & Datenformate

### `POST /api/shorten`
- **Request Body**: `{"url": "https://golang.org/doc"}`
- **Response (201 Created)**: `{"id": 1, "short_code": "a1b2c3", "original_url": "https://golang.org/doc", "created_at": "...", "click_count": 0}`

### `GET /r/{short_code}`
- Löst den Kurzcode auf.
- Reiht asynchron ein `ClickEvent` in die Queue ein.
- Liefert Status `302 Found` (Redirect) oder `200 OK` mit JSON `{"original_url": "..."}`.

### `GET /api/stats/{short_code}`
- **Response (200 OK)**:
```json
{
  "short_code": "a1b2c3",
  "total_clicks": 142,
  "unique_ips": 38
}
```

### `GET /api/metrics`
- **Response (200 OK)**:
```json
{
  "total_urls": 12,
  "total_clicks_processed": 540,
  "active_workers": 4,
  "queue_length": 0
}
```

---

## 🎯 Aufgaben in `aufgabe.go`

1. **TODO 1 (`Structs`)**: Definiere die Datenmodelle `URLRecord`, `ClickEvent`, `AnalyticsStats` und `SystemMetrics` mit JSON-Tags.
2. **TODO 2 (`WorkerPool`)**: Implementiere `StartWorkerPool(numWorkers int)` und `StopWorkerPool()` mit `sync.WaitGroup` und Channel-Close.
3. **TODO 3 (`ShortenURL`)**: Validiere die URL, generiere einen deterministischen oder Zufalls-ShortCode und speichere den Eintrag thread-safe.
4. **TODO 4 (`ResolveURL`)**: Finde die URL und dispatche ein `ClickEvent` nicht-blockierend (mit `select / default`) an die Worker-Queue.
5. **TODO 5 (`GetStats`)**: Berechne Klicks und Unique IPs aus der Analytics-Tabelle.
6. **TODO 6 (`SetupMicroserviceRouter`)**: Registriere alle Endpunkte und binde die Middleware-Kette an.

---

## 🧪 Tests ausführen

```bash
go test -v -race ./...
```
