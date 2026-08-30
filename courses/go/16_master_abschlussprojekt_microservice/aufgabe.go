package main

import (
	"crypto/sha256"
	"encoding/hex"
	"encoding/json"
	"errors"
	"fmt"
	"net/http"
	"strings"
	"sync"
	"sync/atomic"
	"time"
)

// ============================================================================
// 🏆 MASTER 16: HIGH-CONCURRENCY URL SHORTENER & ANALYTICS MICROSERVICE
// ============================================================================

// 🎯 TODO 1a: Definiere das Struct 'URLRecord'
type URLRecord struct {
	ID          int       `json:"id"`
	ShortCode   string    `json:"short_code"`
	OriginalURL string    `json:"original_url"`
	CreatedAt   time.Time `json:"created_at"`
	ClickCount  int64     `json:"click_count"`
}

// 🎯 TODO 1b: Definiere das Struct 'ClickEvent'
type ClickEvent struct {
	ShortCode string    `json:"short_code"`
	IP        string    `json:"ip"`
	UserAgent string    `json:"user_agent"`
	Timestamp time.Time `json:"timestamp"`
}

// 🎯 TODO 1c: Definiere das Struct 'AnalyticsStats'
type AnalyticsStats struct {
	ShortCode   string `json:"short_code"`
	TotalClicks int64  `json:"total_clicks"`
	UniqueIPs   int    `json:"unique_ips"`
}

// 🎯 TODO 1d: Definiere das Struct 'SystemMetrics'
type SystemMetrics struct {
	TotalURLs            int   `json:"total_urls"`
	TotalClicksProcessed int64 `json:"total_clicks_processed"`
	ActiveWorkers        int   `json:"active_workers"`
	QueueLength          int   `json:"queue_length"`
}

// MicroserviceServer ist der zentrale Zustand des Microservices.
type MicroserviceServer struct {
	urlStore       map[string]*URLRecord
	analyticsStore map[string][]ClickEvent
	storeMu        sync.RWMutex
	analyticsMu    sync.RWMutex

	clickQueue     chan ClickEvent
	workerWG       sync.WaitGroup
	totalProcessed int64
	workerCount    int
	nextID         int
}

// NewMicroserviceServer initialisiert die Strukturen und den Event-Kanal.
func NewMicroserviceServer(queueCapacity int) *MicroserviceServer {
	if queueCapacity <= 0 {
		queueCapacity = 1000
	}
	return &MicroserviceServer{
		urlStore:       make(map[string]*URLRecord),
		analyticsStore: make(map[string][]ClickEvent),
		clickQueue:     make(chan ClickEvent, queueCapacity),
		nextID:         1,
	}
}

// 🎯 TODO 2a: Implementiere 'StartWorkerPool'
// Parameter:
// - numWorkers: Anzahl parallel laufender Worker-Goroutines
//
// Anforderungen:
// 1. Speichere s.workerCount = numWorkers.
// 2. Starte für jeden Worker (1..numWorkers) eine Goroutine mit s.workerWG.Add(1).
// 3. Jede Goroutine liest mit 'for event := range s.clickQueue':
//    - Speichert das Event in s.analyticsStore[event.ShortCode] (mit s.analyticsMu.Lock()).
//    - Erhöht s.totalProcessed atomar mit atomic.AddInt64(&s.totalProcessed, 1).
//    - Erhöht atomar den ClickCount des zugehörigen URLRecords in s.urlStore.
// 4. Bei Schließen des Channels: defer s.workerWG.Done().
func (s *MicroserviceServer) StartWorkerPool(numWorkers int) {
	// TODO: Worker-Goroutines starten und mit WaitGroup synchronisieren
}

// 🎯 TODO 2b: Implementiere 'StopWorkerPool'
// Schließt die clickQueue und wartet mit s.workerWG.Wait() auf die Beendigung aller Worker.
func (s *MicroserviceServer) StopWorkerPool() {
	// TODO: close(s.clickQueue) und s.workerWG.Wait()
}

// 🎯 TODO 3: Implementiere 'ShortenURL'
// Parameter:
// - rawURL: Die lange Original-URL (z.B. "https://go.dev/doc")
// Rückgabe:
// - Zeiger auf URLRecord und nil bei Erfolg
// - nil und Fehler bei ungültiger URL
//
// Anforderungen:
// 1. Validiere rawURL: Muss mit "http://" oder "https://" beginnen (sonst errors.New("invalid url format")).
// 2. Erzeuge einen ShortCode (z.B. die ersten 6 Zeichen des SHA256-Hashes von rawURL).
// 3. Speichere den URLRecord thread-safe in s.urlStore.
func (s *MicroserviceServer) ShortenURL(rawURL string) (*URLRecord, error) {
	// TODO: URL validieren, ShortCode generieren, in Store speichern
	return nil, nil
}

// 🎯 TODO 4: Implementiere 'ResolveURL'
// Parameter:
// - shortCode: Der Kurzcode
// - ip: IP-Adresse des anfragenden Clients
// - userAgent: User-Agent des Clients
// Rückgabe:
// - Original-URL und nil bei Fund
// - "", errors.New("url not found") bei unbekanntem Code
//
// Anforderungen:
// 1. Hole den URLRecord thread-safe mit s.storeMu.RLock().
// 2. Erstelle ein ClickEvent mit Timestamp time.Now().
// 3. Sende das Event nicht-blockierend (select mit default) in s.clickQueue.
// 4. Gib record.OriginalURL zurück.
func (s *MicroserviceServer) ResolveURL(shortCode, ip, userAgent string) (string, error) {
	// TODO: URL auflösen und Klick-Event asynchron dispatchen
	return "", nil
}

// 🎯 TODO 5: Implementiere 'GetStats'
// Liefert Klick-Statistiken und die Anzahl der Unique IPs für einen ShortCode.
func (s *MicroserviceServer) GetStats(shortCode string) (*AnalyticsStats, error) {
	// TODO: s.analyticsMu.RLock(), Events zählen und Unique IPs berechnen
	return nil, nil
}

// GetSystemMetrics liefert Gesamt-Metriken.
func (s *MicroserviceServer) GetSystemMetrics() SystemMetrics {
	s.storeMu.RLock()
	totalURLs := len(s.urlStore)
	s.storeMu.RUnlock()

	return SystemMetrics{
		TotalURLs:            totalURLs,
		TotalClicksProcessed: atomic.LoadInt64(&s.totalProcessed),
		ActiveWorkers:        s.workerCount,
		QueueLength:          len(s.clickQueue),
	}
}

// 🎯 TODO 6: Implementiere 'SetupMicroserviceRouter'
// Registriert alle REST Endpunkte:
// - POST /api/shorten
// - GET  /r/
// - GET  /api/stats/
// - GET  /api/metrics
func SetupMicroserviceRouter(srv *MicroserviceServer) *http.ServeMux {
	mux := http.NewServeMux()

	// TODO: HTTP-Handler registrieren
	return mux
}

func main() {
	fmt.Println("=== Master 16: URL Shortener & Analytics Microservice ===")
	srv := NewMicroserviceServer(1000)
	srv.StartWorkerPool(4)

	rec, _ := srv.ShortenURL("https://golang.org")
	fmt.Printf("Kurz-URL erstellt: Code='%s' -> '%s'\n", rec.ShortCode, rec.OriginalURL)

	// Klick simulieren
	url, _ := srv.ResolveURL(rec.ShortCode, "127.0.0.1", "Go-Client/1.0")
	fmt.Printf("URL aufgelöst: %s\n", url)

	time.Sleep(50 * time.Millisecond) // Worker kurz Zeit zur Verarbeitung geben
	stats, _ := srv.GetStats(rec.ShortCode)
	fmt.Printf("Statistik: Clicks=%d, UniqueIPs=%d\n", stats.TotalClicks, stats.UniqueIPs)

	srv.StopWorkerPool()
}
