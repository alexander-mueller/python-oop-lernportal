package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"net/http"
	"net/http/httptest"
	"sync"
	"time"
)

// 🧪 MASTER 16 TESTSUITE: High-Concurrency Microservice API

func assert(condition bool, msg string) {
	if !condition {
		panic("❌ Test fehlgeschlagen: " + msg)
	}
}

func assertEquals[T comparable](actual, expected T, msg string) {
	if actual != expected {
		panic(fmt.Sprintf("❌ Test fehlgeschlagen: %s (Erwartet: '%v', Erhalten: '%v')", msg, expected, actual))
	}
}

// TEST: TestShortenAndResolve - Prüft grundlegende URL-Kürzung und Auflösung
func TestShortenAndResolve() {
	fmt.Println("=== RUN   TestShortenAndResolve")
	srv := NewMicroserviceServer(100)
	srv.StartWorkerPool(2)
	defer srv.StopWorkerPool()

	// 1. URL kürzen
	rec, err := srv.ShortenURL("https://cloud.google.com/go")
	assert(err == nil, "ShortenURL sollte bei valider HTTPS-URL erfolgreich sein")
	assert(len(rec.ShortCode) >= 6, "ShortCode muss mindestens 6 Zeichen lang sein")
	assertEquals(rec.OriginalURL, "https://cloud.google.com/go", "OriginalURL muss übereinstimmen")

	// 2. Ungültige URL prüfen
	_, errInvalid := srv.ShortenURL("ftp://invalid-protocol")
	assert(errInvalid != nil, "Ungültiges URL-Protokoll muss abgewiesen werden")

	// 3. URL auflösen
	orig, errResolve := srv.ResolveURL(rec.ShortCode, "192.168.1.100", "Mozilla/5.0")
	assert(errResolve == nil, "ResolveURL muss den ShortCode auflösen")
	assertEquals(orig, "https://cloud.google.com/go", "Aufgelöste URL muss mit Original übereinstimmen")
	fmt.Println("--- PASS: TestShortenAndResolve")
}

// TEST: TestWorkerPoolAsyncAnalytics - Prüft asynchrone Klick-Verarbeitung
func TestWorkerPoolAsyncAnalytics() {
	fmt.Println("=== RUN   TestWorkerPoolAsyncAnalytics")
	srv := NewMicroserviceServer(1000)
	srv.StartWorkerPool(4)

	rec, _ := srv.ShortenURL("https://golang.org/pkg")

	// 5 Klicks von 3 verschiedenen IPs simulieren
	ips := []string{"10.0.0.1", "10.0.0.2", "10.0.0.1", "10.0.0.3", "10.0.0.2"}
	for _, ip := range ips {
		_, _ = srv.ResolveURL(rec.ShortCode, ip, "Go-Test-Agent")
	}

	// Workerpool stoppen -> Wartet bis alle Events in der Queue verarbeitet sind!
	srv.StopWorkerPool()

	stats, err := srv.GetStats(rec.ShortCode)
	assert(err == nil, "GetStats sollte für bestehenden Code Daten liefern")
	assertEquals(stats.TotalClicks, int64(5), "TotalClicks muss 5 sein")
	assertEquals(stats.UniqueIPs, 3, "UniqueIPs muss exakt 3 sein")
	fmt.Println("--- PASS: TestWorkerPoolAsyncAnalytics")
}

// TEST: TestConcurrentClickStressTest - 100 gleichzeitige Klicks
func TestConcurrentClickStressTest() {
	fmt.Println("=== RUN   TestConcurrentClickStressTest")
	srv := NewMicroserviceServer(5000)
	srv.StartWorkerPool(8)

	rec, _ := srv.ShortenURL("https://kubernetes.io")
	var wg sync.WaitGroup
	numClicks := 100

	for i := 0; i < numClicks; i++ {
		wg.Add(1)
		go func(id int) {
			defer wg.Done()
			ip := fmt.Sprintf("172.16.0.%d", id%10) // 10 distinct IPs
			_, _ = srv.ResolveURL(rec.ShortCode, ip, "StressTestBot")
		}(i)
	}

	wg.Wait()
	srv.StopWorkerPool()

	stats, _ := srv.GetStats(rec.ShortCode)
	assertEquals(stats.TotalClicks, int64(numClicks), "Alle 100 parallelen Klicks müssen registriert sein")
	assertEquals(stats.UniqueIPs, 10, "Genau 10 Unique IPs sollten erfasst sein")
	fmt.Println("--- PASS: TestConcurrentClickStressTest")
}

// TEST: TestHTTPRouterEndpoints - Prüft REST HTTP Integration
func TestHTTPRouterEndpoints() {
	fmt.Println("=== RUN   TestHTTPRouterEndpoints")
	srv := NewMicroserviceServer(100)
	srv.StartWorkerPool(2)
	defer srv.StopWorkerPool()

	router := SetupMicroserviceRouter(srv)

	// 1. POST /api/shorten
	payload := `{"url":"https://github.com/golang/go"}`
	reqPost := httptest.NewRequest(http.MethodPost, "/api/shorten", bytes.NewBufferString(payload))
	recPost := httptest.NewRecorder()
	router.ServeHTTP(recPost, reqPost)

	assertEquals(recPost.Code, http.StatusCreated, "POST /api/shorten muss 201 Created liefern")

	var created URLRecord
	json.Unmarshal(recPost.Body.Bytes(), &created)
	assert(created.ShortCode != "", "ShortCode muss generiert worden sein")

	// 2. GET /r/{short_code}
	reqGet := httptest.NewRequest(http.MethodGet, "/r/"+created.ShortCode, nil)
	recGet := httptest.NewRecorder()
	router.ServeHTTP(recGet, reqGet)

	assertEquals(recGet.Code, http.StatusOK, "GET /r/{code} muss 200 OK liefern")

	// 3. GET /api/metrics
	reqMetrics := httptest.NewRequest(http.MethodGet, "/api/metrics", nil)
	recMetrics := httptest.NewRecorder()
	router.ServeHTTP(recMetrics, reqMetrics)

	assertEquals(recMetrics.Code, http.StatusOK, "GET /api/metrics muss 200 OK liefern")
	fmt.Println("--- PASS: TestHTTPRouterEndpoints")
}

func main() {
	fmt.Println("🧪 Starte Master 16 Abschlussprojekt Testsuite...")
	TestShortenAndResolve()
	TestWorkerPoolAsyncAnalytics()
	TestConcurrentClickStressTest()
	TestHTTPRouterEndpoints()
	fmt.Println("\n🏆 GRATULATION! Alle Tests im Master-Abschlussprojekt 16 erfolgreich bestanden!")
}
