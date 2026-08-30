package main

import (
	"fmt"
	"net/http"
	"strings"
)

// ============================================================================
// 🚀 GO 13: HTTP SERVER, HANDLER & ROUTING
// ============================================================================

// 🎯 TODO 1: Implementiere 'HealthHandler'
// Anforderungen:
// 1. Prüfe, ob r.Method == http.MethodGet ist. Falls nicht:
//    http.Error(w, "Method not allowed", http.StatusMethodNotAllowed) und return.
// 2. Setze Status 200 OK und schreibe "STATUS: UP" in 'w'.
func HealthHandler(w http.ResponseWriter, r *http.Request) {
	// TODO: Methode prüfen, 200 OK mit "STATUS: UP" antworten
}

// 🎯 TODO 2: Implementiere 'EchoHandler'
// Anforderungen:
// 1. Prüfe auf GET-Methode (sonst 405 Method Not Allowed).
// 2. Lese den Query-Parameter 'msg' via r.URL.Query().Get("msg").
// 3. Wenn 'msg' leer ist:
//    http.Error(w, "missing msg parameter", http.StatusBadRequest) und return.
// 4. Bei gültigem Parameter: Schreibe "ECHO: " + msg in 'w' mit Status 200 OK.
func EchoHandler(w http.ResponseWriter, r *http.Request) {
	// TODO: Query-Parameter msg validieren und zurücksenden
}

// 🎯 TODO 3: Implementiere 'UserProfileHandler'
// Endpoint für Pfade wie "/users/alice" oder "/users/bob".
// Anforderungen:
// 1. Extrahiere den Nutzernamen aus dem Pfad (z.B. strings.TrimPrefix(r.URL.Path, "/users/")).
// 2. Entferne eventuelle führende/nachfolgende Slashes mit strings.Trim(username, "/").
// 3. Wenn der resultierende Nutzername leer ist:
//    http.Error(w, "username required", http.StatusBadRequest) und return.
// 4. Sonst: Status 200 OK und Body "User Profile: " + username.
func UserProfileHandler(w http.ResponseWriter, r *http.Request) {
	// TODO: Username aus URL extrahieren und Profil-Text zurückgeben
}

// 🎯 TODO 4: Implementiere 'SetupAPIRouter'
// Anforderungen:
// 1. Erstelle einen neuen Mux: mux := http.NewServeMux().
// 2. Registriere:
//    - "/health" -> HealthHandler
//    - "/echo"   -> EchoHandler
//    - "/users/" -> UserProfileHandler
// 3. Gib 'mux' zurück.
func SetupAPIRouter() *http.ServeMux {
	// TODO: Mux erstellen, Routen registrieren und zurückgeben
	return nil
}

func main() {
	fmt.Println("=== Go 13: HTTP Web Server ===")

	router := SetupAPIRouter()
	addr := ":8080"
	fmt.Printf("Starte Webserver auf http://localhost%s ...\n", addr)
	// http.ListenAndServe(addr, router)
	_ = router
}
