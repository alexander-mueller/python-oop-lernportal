package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"sync"
)

// ============================================================================
// 💡 GO 14: MUSTERLÖSUNG (JSON APIs & Middleware)
// ============================================================================

// Device repräsentiert eine verwaltete Netzwerkkomponente.
type Device struct {
	ID     int    `json:"id"`
	Name   string `json:"name"`
	IP     string `json:"ip"`
	Active bool   `json:"active"`
}

// APIResponse ist das standardisierte JSON-Antwortformat.
type APIResponse struct {
	Success bool        `json:"success"`
	Message string      `json:"message"`
	Data    interface{} `json:"data,omitempty"`
}

// DeviceStore verwaltet Devices thread-safe im Speicher.
type DeviceStore struct {
	mu      sync.RWMutex
	devices []Device
	nextID  int
}

// NewDeviceStore instanziiert einen neuen DeviceStore.
func NewDeviceStore() *DeviceStore {
	return &DeviceStore{
		devices: make([]Device, 0),
		nextID:  1,
	}
}

// GetDevicesHandler gibt alle Devices als JSON-Array zurück.
func (s *DeviceStore) GetDevicesHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodGet {
		http.Error(w, `{"error":"Method not allowed"}`, http.StatusMethodNotAllowed)
		return
	}

	s.mu.RLock()
	defer s.mu.RUnlock()

	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)
	json.NewEncoder(w).Encode(s.devices)
}

// CreateDeviceHandler dekodiert ein neues Device und speichert es.
func (s *DeviceStore) CreateDeviceHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, `{"error":"Method not allowed"}`, http.StatusMethodNotAllowed)
		return
	}

	var req Device
	if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
		w.Header().Set("Content-Type", "application/json")
		w.WriteHeader(http.StatusBadRequest)
		json.NewEncoder(w).Encode(APIResponse{
			Success: false,
			Message: "invalid json body",
		})
		return
	}

	if req.Name == "" || req.IP == "" {
		w.Header().Set("Content-Type", "application/json")
		w.WriteHeader(http.StatusBadRequest)
		json.NewEncoder(w).Encode(APIResponse{
			Success: false,
			Message: "name and ip are required",
		})
		return
	}

	s.mu.Lock()
	req.ID = s.nextID
	s.nextID++
	s.devices = append(s.devices, req)
	s.mu.Unlock()

	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(req)
}

// AuthMiddleware sichert Routen per X-API-Key Header ab.
func AuthMiddleware(secretKey string) func(http.Handler) http.Handler {
	return func(next http.Handler) http.Handler {
		return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
			apiKey := r.Header.Get("X-API-Key")
			if apiKey != secretKey {
				w.Header().Set("Content-Type", "application/json")
				w.WriteHeader(http.StatusUnauthorized)
				json.NewEncoder(w).Encode(APIResponse{
					Success: false,
					Message: "unauthorized",
				})
				return
			}
			next.ServeHTTP(w, r)
		})
	}
}

// RecoveryMiddleware fängt Panics ab und liefert einen sauberen 500 Fehler.
func RecoveryMiddleware(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		defer func() {
			if err := recover(); err != nil {
				w.Header().Set("Content-Type", "application/json")
				w.WriteHeader(http.StatusInternalServerError)
				json.NewEncoder(w).Encode(APIResponse{
					Success: false,
					Message: "internal server error",
				})
			}
		}()
		next.ServeHTTP(w, r)
	})
}

// ApplyMiddleware verkettet Middlewares um einen Core-Handler.
func ApplyMiddleware(h http.Handler, middlewares ...func(http.Handler) http.Handler) http.Handler {
	for i := len(middlewares) - 1; i >= 0; i-- {
		h = middlewares[i](h)
	}
	return h
}

func main() {
	fmt.Println("=== Go 14: Musterlösung ===")
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
