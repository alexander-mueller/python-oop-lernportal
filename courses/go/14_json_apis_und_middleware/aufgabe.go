package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"sync"
)

// ============================================================================
// 🚀 GO 14: REST JSON APIS & MIDDLEWARE CHAINING
// ============================================================================

// 🎯 TODO 1a: Definiere das Struct 'Device' mit JSON-Tags
// Felder:
// - ID     int    `json:"id"`
// - Name   string `json:"name"`
// - IP     string `json:"ip"`
// - Active bool   `json:"active"`
type Device struct {
	// TODO: Felder mit json-Tags ergänzen
	ID     int    `json:"id"`
	Name   string `json:"name"`
	IP     string `json:"ip"`
	Active bool   `json:"active"`
}

// 🎯 TODO 1b: Definiere das Struct 'APIResponse'
// Felder:
// - Success bool        `json:"success"`
// - Message string      `json:"message"`
// - Data    interface{} `json:"data,omitempty"`
type APIResponse struct {
	// TODO: Felder mit json-Tags ergänzen
	Success bool        `json:"success"`
	Message string      `json:"message"`
	Data    interface{} `json:"data,omitempty"`
}

// DeviceStore verwaltet Devices im Speicher
type DeviceStore struct {
	mu      sync.RWMutex
	devices []Device
	nextID  int
}

func NewDeviceStore() *DeviceStore {
	return &DeviceStore{
		devices: make([]Device, 0),
		nextID:  1,
	}
}

// 🎯 TODO 2a: Implementiere 'GetDevicesHandler'
// Gibt alle Devices aus dem Store als JSON mit Status 200 OK zurück.
func (s *DeviceStore) GetDevicesHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodGet {
		http.Error(w, `{"error":"Method not allowed"}`, http.StatusMethodNotAllowed)
		return
	}

	// TODO: Content-Type Header setzen, s.mu.RLock nutzen und s.devices mit json.NewEncoder enkodieren
}

// 🎯 TODO 2b: Implementiere 'CreateDeviceHandler'
// Parst einen neuen Device-Eintrag aus dem JSON-Body.
// Validierung:
// - 'Name' und 'IP' dürfen nicht leer sein (sonst 400 Bad Request mit Fehlermeldung).
// - Bei Erfolg: ID vergeben, an 'devices' anhängen, Status 201 Created und das erstellte Device zurückgeben.
func (s *DeviceStore) CreateDeviceHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, `{"error":"Method not allowed"}`, http.StatusMethodNotAllowed)
		return
	}

	// TODO: JSON decode, validieren, ID zuweisen und antworten
}

// 🎯 TODO 3: Implementiere 'AuthMiddleware'
// Prüft den Request-Header 'X-API-Key'.
// - Wenn r.Header.Get("X-API-Key") != secretKey:
//   Setze Content-Type: application/json, Status 401 Unauthorized und antworte mit:
//   `{"success":false,"message":"unauthorized"}`
// - Sonst: next.ServeHTTP(w, r)
func AuthMiddleware(secretKey string) func(http.Handler) http.Handler {
	return func(next http.Handler) http.Handler {
		return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
			// TODO: Header prüfen und delegieren
			next.ServeHTTP(w, r)
		})
	}
}

// 🎯 TODO 4a: Implementiere 'RecoveryMiddleware'
// Fängt Panics im Handler-Baum ab mit 'defer func() { if err := recover(); err != nil ... }()'.
// Bei einer Panic:
// - Schreibe Content-Type: application/json, Status 500 Internal Server Error
// - Body: `{"success":false,"message":"internal server error"}`
func RecoveryMiddleware(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		// TODO: defer recover() einbauen und next.ServeHTTP(w, r) aufrufen
		next.ServeHTTP(w, r)
	})
}

// 🎯 TODO 4b: Implementiere 'ApplyMiddleware'
// Verkettet eine Liste von Middleware-Funktionen um den Handler 'h'.
func ApplyMiddleware(h http.Handler, middlewares ...func(http.Handler) http.Handler) http.Handler {
	// TODO: Von rechts nach links um 'h' wrappen
	for i := len(middlewares) - 1; i >= 0; i-- {
		h = middlewares[i](h)
	}
	return h
}

func main() {
	fmt.Println("=== Go 14: REST JSON APIs & Middleware ===")
	store := NewDeviceStore()

	mux := http.NewServeMux()
	mux.HandleFunc("/api/v1/devices", func(w http.ResponseWriter, r *http.Request) {
		if r.Method == http.MethodGet {
			store.GetDevicesHandler(w, r)
		} else if r.Method == http.MethodPost {
			store.CreateDeviceHandler(w, r)
		}
	})

	handler := ApplyMiddleware(mux,
		RecoveryMiddleware,
		AuthMiddleware("secret-token-123"),
	)

	_ = handler
	fmt.Println("API-Server mit Auth- und Recovery-Middleware konfiguriert.")
}
