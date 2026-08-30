package main

import (
	"fmt"
	"net/http"
	"strings"
)

// ============================================================================
// 💡 GO 13: MUSTERLÖSUNG (HTTP Server & Routing)
// ============================================================================

// HealthHandler antwortet auf GET /health mit dem Serverstatus.
func HealthHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodGet {
		http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
		return
	}
	w.WriteHeader(http.StatusOK)
	fmt.Fprint(w, "STATUS: UP")
}

// EchoHandler liefert den übergebenen Query-Parameter ?msg=... zurück.
func EchoHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodGet {
		http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
		return
	}

	msg := r.URL.Query().Get("msg")
	if msg == "" {
		http.Error(w, "missing msg parameter", http.StatusBadRequest)
		return
	}

	w.WriteHeader(http.StatusOK)
	fmt.Fprintf(w, "ECHO: %s", msg)
}

// UserProfileHandler extrahiert den Usernamen aus dem URL-Pfad.
func UserProfileHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodGet {
		http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
		return
	}

	username := strings.TrimPrefix(r.URL.Path, "/users/")
	username = strings.Trim(username, "/")

	if username == "" {
		http.Error(w, "username required", http.StatusBadRequest)
		return
	}

	w.WriteHeader(http.StatusOK)
	fmt.Fprintf(w, "User Profile: %s", username)
}

// SetupAPIRouter initialisiert die ServeMux-Routen.
func SetupAPIRouter() *http.ServeMux {
	mux := http.NewServeMux()
	mux.HandleFunc("/health", HealthHandler)
	mux.HandleFunc("/echo", EchoHandler)
	mux.HandleFunc("/users/", UserProfileHandler)
	return mux
}

func main() {
	fmt.Println("=== Go 13: Musterlösung ===")

	router := SetupAPIRouter()
	addr := ":8080"
	fmt.Printf("Starte Webserver auf http://localhost%s ...\n", addr)
	// http.ListenAndServe(addr, router)
	_ = router
}
