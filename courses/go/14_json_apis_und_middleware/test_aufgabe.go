package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"net/http"
	"net/http/httptest"
)

// 🧪 GO 14 TESTSUITE: REST JSON APIs & Middleware

func assertEquals[T comparable](actual, expected T, msg string) {
	if actual != expected {
		panic(fmt.Sprintf("❌ Test fehlgeschlagen: %s (Erwartet: '%v', Erhalten: '%v')", msg, expected, actual))
	}
}

// TEST: TestCreateAndGetDevices - Prüft REST Endpoints
func TestCreateAndGetDevices() {
	fmt.Println("=== RUN   TestCreateAndGetDevices")
	store := NewDeviceStore()

	// 1. Create Device
	payload := `{"name":"Switch-01","ip":"192.168.1.1","active":true}`
	reqPost := httptest.NewRequest(http.MethodPost, "/devices", bytes.NewBufferString(payload))
	recPost := httptest.NewRecorder()
	store.CreateDeviceHandler(recPost, reqPost)

	assertEquals(recPost.Code, http.StatusCreated, "CreateDeviceHandler muss Status 201 Created liefern")

	var created Device
	err := json.Unmarshal(recPost.Body.Bytes(), &created)
	assertEquals(err, nil, "Response muss valides JSON sein")
	assertEquals(created.ID, 1, "Erstes Device muss ID 1 erhalten")
	assertEquals(created.Name, "Switch-01", "Name muss Switch-01 sein")

	// 2. Get Devices
	reqGet := httptest.NewRequest(http.MethodGet, "/devices", nil)
	recGet := httptest.NewRecorder()
	store.GetDevicesHandler(recGet, reqGet)

	assertEquals(recGet.Code, http.StatusOK, "GetDevicesHandler muss Status 200 OK liefern")

	var list []Device
	errGet := json.Unmarshal(recGet.Body.Bytes(), &list)
	assertEquals(errGet, nil, "Get-Response muss als Device-Slice parsbar sein")
	assertEquals(len(list), 1, "Liste muss 1 Device enthalten")
	fmt.Println("--- PASS: TestCreateAndGetDevices")
}

// TEST: TestAuthMiddleware - Prüft X-API-Key Validierung
func TestAuthMiddleware() {
	fmt.Println("=== RUN   TestAuthMiddleware")
	protectedHandler := http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusOK)
		w.Write([]byte(`{"success":true}`))
	})

	authMw := AuthMiddleware("valid-secret-key")
	secured := authMw(protectedHandler)

	// 1. Request OHNE Key -> 401
	reqUnauthorized := httptest.NewRequest(http.MethodGet, "/secure", nil)
	recUnauthorized := httptest.NewRecorder()
	secured.ServeHTTP(recUnauthorized, reqUnauthorized)
	assertEquals(recUnauthorized.Code, http.StatusUnauthorized, "Ohne Key muss 401 Unauthorized kommen")

	// 2. Request MIT gültigem Key -> 200
	reqAuthorized := httptest.NewRequest(http.MethodGet, "/secure", nil)
	reqAuthorized.Header.Set("X-API-Key", "valid-secret-key")
	recAuthorized := httptest.NewRecorder()
	secured.ServeHTTP(recAuthorized, reqAuthorized)
	assertEquals(recAuthorized.Code, http.StatusOK, "Mit gültigem Key muss 200 OK kommen")
	fmt.Println("--- PASS: TestAuthMiddleware")
}

// TEST: TestRecoveryMiddleware - Prüft Panic-Abfang
func TestRecoveryMiddleware() {
	fmt.Println("=== RUN   TestRecoveryMiddleware")
	panickingHandler := http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		panic("Simulierter kritischer Null-Pointer-Crash!")
	})

	recovered := RecoveryMiddleware(panickingHandler)
	req := httptest.NewRequest(http.MethodGet, "/crash", nil)
	rec := httptest.NewRecorder()

	recovered.ServeHTTP(rec, req)

	assertEquals(rec.Code, http.StatusInternalServerError, "Panic muss als 500 Internal Server Error abgefangen werden")
	fmt.Println("--- PASS: TestRecoveryMiddleware")
}

func main() {
	fmt.Println("🧪 Starte Go 14 Testsuite...")
	TestCreateAndGetDevices()
	TestAuthMiddleware()
	TestRecoveryMiddleware()
	fmt.Println("\n✅ Alle Tests in Go 14 erfolgreich bestanden!")
}
