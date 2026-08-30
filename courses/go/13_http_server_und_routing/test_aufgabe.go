package main

import (
	"fmt"
	"net/http"
	"net/http/httptest"
	"strings"
)

// 🧪 GO 13 TESTSUITE: HTTP Web Server & Routing

func assertEquals[T comparable](actual, expected T, msg string) {
	if actual != expected {
		panic(fmt.Sprintf("❌ Test fehlgeschlagen: %s (Erwartet: '%v', Erhalten: '%v')", msg, expected, actual))
	}
}

// TEST: TestHealthHandler - Prüft /health Endpoint
func TestHealthHandler() {
	fmt.Println("=== RUN   TestHealthHandler")
	// 1. GET Request
	reqGet := httptest.NewRequest(http.MethodGet, "/health", nil)
	recGet := httptest.NewRecorder()
	HealthHandler(recGet, reqGet)

	assertEquals(recGet.Code, http.StatusOK, "Statuscode muss 200 OK sein")
	assertEquals(strings.TrimSpace(recGet.Body.String()), "STATUS: UP", "Body muss 'STATUS: UP' enthalten")

	// 2. POST Request (soll 405 liefern)
	reqPost := httptest.NewRequest(http.MethodPost, "/health", nil)
	recPost := httptest.NewRecorder()
	HealthHandler(recPost, reqPost)

	assertEquals(recPost.Code, http.StatusMethodNotAllowed, "POST auf /health muss 405 Method Not Allowed liefern")
	fmt.Println("--- PASS: TestHealthHandler")
}

// TEST: TestEchoHandler - Prüft /echo Query-Parameter
func TestEchoHandler() {
	fmt.Println("=== RUN   TestEchoHandler")
	// 1. Gültiger Query Parameter
	reqValid := httptest.NewRequest(http.MethodGet, "/echo?msg=GolangCloud", nil)
	recValid := httptest.NewRecorder()
	EchoHandler(recValid, reqValid)

	assertEquals(recValid.Code, http.StatusOK, "Statuscode muss 200 OK sein")
	assertEquals(recValid.Body.String(), "ECHO: GolangCloud", "Body muss 'ECHO: GolangCloud' sein")

	// 2. Fehlender Query Parameter
	reqMissing := httptest.NewRequest(http.MethodGet, "/echo", nil)
	recMissing := httptest.NewRecorder()
	EchoHandler(recMissing, reqMissing)

	assertEquals(recMissing.Code, http.StatusBadRequest, "Fehlender Parameter muss 400 Bad Request liefern")
	fmt.Println("--- PASS: TestEchoHandler")
}

// TEST: TestUserProfileHandler - Prüft Pfad-Parameter /users/{username}
func TestUserProfileHandler() {
	fmt.Println("=== RUN   TestUserProfileHandler")
	// 1. Gültiger Username
	reqUser := httptest.NewRequest(http.MethodGet, "/users/gopher123", nil)
	recUser := httptest.NewRecorder()
	UserProfileHandler(recUser, reqUser)

	assertEquals(recUser.Code, http.StatusOK, "Statuscode muss 200 OK sein")
	assertEquals(recUser.Body.String(), "User Profile: gopher123", "Body muss 'User Profile: gopher123' sein")

	// 2. Leerer Username
	reqEmpty := httptest.NewRequest(http.MethodGet, "/users/", nil)
	recEmpty := httptest.NewRecorder()
	UserProfileHandler(recEmpty, reqEmpty)

	assertEquals(recEmpty.Code, http.StatusBadRequest, "Leerer Username muss 400 Bad Request liefern")
	fmt.Println("--- PASS: TestUserProfileHandler")
}

// TEST: TestRouterDispatch - Prüft ServeMux Routing
func TestRouterDispatch() {
	fmt.Println("=== RUN   TestRouterDispatch")
	router := SetupAPIRouter()

	req := httptest.NewRequest(http.MethodGet, "/health", nil)
	rec := httptest.NewRecorder()
	router.ServeHTTP(rec, req)

	assertEquals(rec.Code, http.StatusOK, "Router muss /health an HealthHandler routen")
	assertEquals(strings.TrimSpace(rec.Body.String()), "STATUS: UP", "Router-Response muss stimmen")
	fmt.Println("--- PASS: TestRouterDispatch")
}

func main() {
	fmt.Println("🧪 Starte Go 13 Testsuite...")
	TestHealthHandler()
	TestEchoHandler()
	TestUserProfileHandler()
	TestRouterDispatch()
	fmt.Println("\n✅ Alle Tests in Go 13 erfolgreich bestanden!")
}
