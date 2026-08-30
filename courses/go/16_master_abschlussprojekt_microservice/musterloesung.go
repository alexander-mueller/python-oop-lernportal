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
// 💡 MASTER 16: MUSTERLÖSUNG (Microservice API)
// ============================================================================

// URLRecord speichert Metadaten zu einer gekürzten URL.
type URLRecord struct {
	ID          int       `json:"id"`
	ShortCode   string    `json:"short_code"`
	OriginalURL string    `json:"original_url"`
	CreatedAt   time.Time `json:"created_at"`
	ClickCount  int64     `json:"click_count"`
}

// ClickEvent repräsentiert ein asynchron verarbeitetes Klick-Ereignis.
type ClickEvent struct {
	ShortCode string    `json:"short_code"`
	IP        string    `json:"ip"`
	UserAgent string    `json:"user_agent"`
	Timestamp time.Time `json:"timestamp"`
}

// AnalyticsStats liefert aggregierte Zugriffs-Auswertungen.
type AnalyticsStats struct {
	ShortCode   string `json:"short_code"`
	TotalClicks int64  `json:"total_clicks"`
	UniqueIPs   int    `json:"unique_ips"`
}

// SystemMetrics liefert den globalen Zustand des Microservices.
type SystemMetrics struct {
	TotalURLs            int   `json:"total_urls"`
	TotalClicksProcessed int64 `json:"total_clicks_processed"`
	ActiveWorkers        int   `json:"active_workers"`
	QueueLength          int   `json:"queue_length"`
}

// MicroserviceServer ist der hochgradig nebenläufige In-Memory Microservice.
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

// NewMicroserviceServer initialisiert den Server und Pufferkanäle.
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

// StartWorkerPool startet Hintergrund-Worker zur Event-Verarbeitung.
func (s *MicroserviceServer) StartWorkerPool(numWorkers int) {
	s.workerCount = numWorkers
	for i := 0; i < numWorkers; i++ {
		s.workerWG.Add(1)
		go func() {
			defer s.workerWG.Done()
			for event := range s.clickQueue {
				// 1. In Analytics-Historie speichern
				s.analyticsMu.Lock()
				s.analyticsStore[event.ShortCode] = append(s.analyticsStore[event.ShortCode], event)
				s.analyticsMu.Unlock()

				// 2. Globalen Verarbeitungszähler erhöhen
				atomic.AddInt64(&s.totalProcessed, 1)

				// 3. Klickzähler des URLs atomar hochzählen
				s.storeMu.RLock()
				if record, exists := s.urlStore[event.ShortCode]; exists {
					atomic.AddInt64(&record.ClickCount, 1)
				}
				s.storeMu.RUnlock()
			}
		}()
	}
}

// StopWorkerPool schließt die Warteschlange und wartet auf alle Worker.
func (s *MicroserviceServer) StopWorkerPool() {
	close(s.clickQueue)
	s.workerWG.Wait()
}

// ShortenURL validiert und kürzt eine URL thread-safe.
func (s *MicroserviceServer) ShortenURL(rawURL string) (*URLRecord, error) {
	trimmed := strings.TrimSpace(rawURL)
	if !strings.HasPrefix(trimmed, "http://") && !strings.HasPrefix(trimmed, "https://") {
		return nil, errors.New("invalid url format: must start with http:// or https://")
	}

	hash := sha256.Sum256([]byte(trimmed))
	shortCode := hex.EncodeToString(hash[:])[:6]

	s.storeMu.Lock()
	defer s.storeMu.Unlock()

	// Prüfen, ob bereits vorhanden
	if existing, exists := s.urlStore[shortCode]; exists {
		return existing, nil
	}

	record := &URLRecord{
		ID:          s.nextID,
		ShortCode:   shortCode,
		OriginalURL: trimmed,
		CreatedAt:   time.Now(),
		ClickCount:  0,
	}
	s.nextID++
	s.urlStore[shortCode] = record

	return record, nil
}

// ResolveURL findet die Original-URL und schickt ein Klick-Event an den Workerpool.
func (s *MicroserviceServer) ResolveURL(shortCode, ip, userAgent string) (string, error) {
	s.storeMu.RLock()
	record, exists := s.urlStore[shortCode]
	s.storeMu.RUnlock()

	if !exists {
		return "", errors.New("url not found")
	}

	event := ClickEvent{
		ShortCode: shortCode,
		IP:        ip,
		UserAgent: userAgent,
		Timestamp: time.Now(),
	}

	// Nicht-blockierender Dispatch in den Event-Bus
	select {
	case s.clickQueue <- event:
	default:
		// Queue voll: Event wird geloggt/ignoriert, um Request nicht zu verlangsamen
	}

	return record.OriginalURL, nil
}

// GetStats berechnet Klickzahlen und Unique-IPs.
func (s *MicroserviceServer) GetStats(shortCode string) (*AnalyticsStats, error) {
	s.storeMu.RLock()
	_, exists := s.urlStore[shortCode]
	s.storeMu.RUnlock()

	if !exists {
		return nil, errors.New("url not found")
	}

	s.analyticsMu.RLock()
	events := s.analyticsStore[shortCode]
	s.analyticsMu.RUnlock()

	uniqueIPs := make(map[string]bool)
	for _, ev := range events {
		uniqueIPs[ev.IP] = true
	}

	return &AnalyticsStats{
		ShortCode:   shortCode,
		TotalClicks: int64(len(events)),
		UniqueIPs:   len(uniqueIPs),
	}, nil
}

// GetSystemMetrics liefert Gesamtmetriken des Microservices.
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

// SetupMicroserviceRouter konfiguriert alle HTTP-Routen.
func SetupMicroserviceRouter(srv *MicroserviceServer) *http.ServeMux {
	mux := http.NewServeMux()

	// 1. POST /api/shorten
	mux.HandleFunc("/api/shorten", func(w http.ResponseWriter, r *http.Request) {
		if r.Method != http.MethodPost {
			http.Error(w, `{"error":"Method not allowed"}`, http.StatusMethodNotAllowed)
			return
		}

		var payload struct {
			URL string `json:"url"`
		}
		if err := json.NewDecoder(r.Body).Decode(&payload); err != nil {
			w.Header().Set("Content-Type", "application/json")
			w.WriteHeader(http.StatusBadRequest)
			json.NewEncoder(w).Encode(map[string]string{"error": "invalid json"})
			return
		}

		record, err := srv.ShortenURL(payload.URL)
		if err != nil {
			w.Header().Set("Content-Type", "application/json")
			w.WriteHeader(http.StatusBadRequest)
			json.NewEncoder(w).Encode(map[string]string{"error": err.Error()})
			return
		}

		w.Header().Set("Content-Type", "application/json")
		w.WriteHeader(http.StatusCreated)
		json.NewEncoder(w).Encode(record)
	})

	// 2. GET /r/{short_code}
	mux.HandleFunc("/r/", func(w http.ResponseWriter, r *http.Request) {
		if r.Method != http.MethodGet {
			http.Error(w, `{"error":"Method not allowed"}`, http.StatusMethodNotAllowed)
			return
		}

		code := strings.TrimPrefix(r.URL.Path, "/r/")
		code = strings.Trim(code, "/")

		origURL, err := srv.ResolveURL(code, r.RemoteAddr, r.UserAgent())
		if err != nil {
			w.Header().Set("Content-Type", "application/json")
			w.WriteHeader(http.StatusNotFound)
			json.NewEncoder(w).Encode(map[string]string{"error": "short url not found"})
			return
		}

		w.Header().Set("Content-Type", "application/json")
		w.WriteHeader(http.StatusOK)
		json.NewEncoder(w).Encode(map[string]string{"original_url": origURL})
	})

	// 3. GET /api/stats/{short_code}
	mux.HandleFunc("/api/stats/", func(w http.ResponseWriter, r *http.Request) {
		if r.Method != http.MethodGet {
			http.Error(w, `{"error":"Method not allowed"}`, http.StatusMethodNotAllowed)
			return
		}

		code := strings.TrimPrefix(r.URL.Path, "/api/stats/")
		code = strings.Trim(code, "/")

		stats, err := srv.GetStats(code)
		if err != nil {
			w.Header().Set("Content-Type", "application/json")
			w.WriteHeader(http.StatusNotFound)
			json.NewEncoder(w).Encode(map[string]string{"error": "stats not found"})
			return
		}

		w.Header().Set("Content-Type", "application/json")
		w.WriteHeader(http.StatusOK)
		json.NewEncoder(w).Encode(stats)
	})

	// 4. GET /api/metrics
	mux.HandleFunc("/api/metrics", func(w http.ResponseWriter, r *http.Request) {
		if r.Method != http.MethodGet {
			http.Error(w, `{"error":"Method not allowed"}`, http.StatusMethodNotAllowed)
			return
		}

		metrics := srv.GetSystemMetrics()
		w.Header().Set("Content-Type", "application/json")
		w.WriteHeader(http.StatusOK)
		json.NewEncoder(w).Encode(metrics)
	})

	return mux
}

func main() {
	fmt.Println("=== Master 16: Musterlösung ===")
	srv := NewMicroserviceServer(1000)
	srv.StartWorkerPool(4)

	rec, _ := srv.ShortenURL("https://golang.org")
	fmt.Printf("Kurz-URL erstellt: Code='%s' -> '%s'\n", rec.ShortCode, rec.OriginalURL)

	url, _ := srv.ResolveURL(rec.ShortCode, "127.0.0.1", "Go-Client/1.0")
	fmt.Printf("URL aufgelöst: %s\n", url)

	time.Sleep(50 * time.Millisecond)
	stats, _ := srv.GetStats(rec.ShortCode)
	fmt.Printf("Statistik: Clicks=%d, UniqueIPs=%d\n", stats.TotalClicks, stats.UniqueIPs)

	srv.StopWorkerPool()
}
