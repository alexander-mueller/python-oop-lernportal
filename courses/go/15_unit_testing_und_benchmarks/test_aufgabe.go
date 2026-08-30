package main

import (
	"fmt"
	"strings"
	"time"
)

// 🧪 GO 15 TESTSUITE: Unit Testing, Table-Driven Tests & Benchmarks

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

// TEST: TestSlugify_TableDriven - Führt Table-Driven Tests für Slugify aus
func TestSlugify_TableDriven() {
	fmt.Println("=== RUN   TestSlugify_TableDriven")
	tests := []struct {
		name    string
		input   string
		want    string
		wantErr bool
	}{
		{"Einfacher Satz", "Hello World", "hello-world", false},
		{"Sonderzeichen und Zahlen", "Go 1.22 & Concurrency!", "go-1-22-concurrency", false},
		{"Mehrere Leerzeichen", "  cloud   native   microservices  ", "cloud-native-microservices", false},
		{"Leerer Input", "   ", "", true},
	}

	for _, tt := range tests {
		got, err := Slugify(tt.input)
		if tt.wantErr {
			assert(err != nil, fmt.Sprintf("[%s] Fehler erwartet bei leerem String", tt.name))
		} else {
			assert(err == nil, fmt.Sprintf("[%s] Unerwarteter Fehler: %v", tt.name, err))
			assertEquals(got, tt.want, fmt.Sprintf("[%s] Slug-Formatierung fehlerhaft", tt.name))
		}
	}
	fmt.Println("--- PASS: TestSlugify_TableDriven")
}

// TEST: TestValidateEmail_TableDriven - Führt Table-Driven Tests für E-Mail-Validierung aus
func TestValidateEmail_TableDriven() {
	fmt.Println("=== RUN   TestValidateEmail_TableDriven")
	tests := []struct {
		name  string
		email string
		want  bool
	}{
		{"Gültige Standard-Mail", "alice@example.com", true},
		{"Gültige Subdomain", "bob@mail.cloud.org", true},
		{"Fehlendes @", "alice.example.com", false},
		{"Fehlender User", "@example.com", false},
		{"Fehlende Domain", "alice@", false},
		{"Kein Punkt in Domain", "alice@localhost", false},
		{"Punkt am Ende der Domain", "alice@example.", false},
	}

	for _, tt := range tests {
		got := ValidateEmail(tt.email)
		assertEquals(got, tt.want, fmt.Sprintf("[%s] Validierungsergebnis für '%s' stimmt nicht", tt.name, tt.email))
	}
	fmt.Println("--- PASS: TestValidateEmail_TableDriven")
}

// TEST: TestFastStringJoin - Prüft FastStringJoin Funktionalität und Performance
func TestFastStringJoin() {
	fmt.Println("=== RUN   TestFastStringJoin")
	parts := []string{"cloud", "concurrency", "golang", "microservices"}
	joined := FastStringJoin(parts, "/")
	assertEquals(joined, "cloud/concurrency/golang/microservices", "StringJoin muss korrekt konkatenieren")

	empty := FastStringJoin([]string{}, ",")
	assertEquals(empty, "", "Leere Liste muss leeren String liefern")

	single := FastStringJoin([]string{"solo"}, ",")
	assertEquals(single, "solo", "Einzelnes Element muss unverändert zurückgegeben werden")
	fmt.Println("--- PASS: TestFastStringJoin")
}

// TEST: BenchmarkFastStringJoinSimulation - Führt Micro-Benchmark aus
func BenchmarkFastStringJoinSimulation() {
	fmt.Println("=== RUN   BenchmarkFastStringJoinSimulation")
	parts := []string{"microservice", "worker", "queue", "pipeline", "router", "cache"}
	iterations := 100000

	start := time.Now()
	for i := 0; i < iterations; i++ {
		_ = FastStringJoin(parts, "-")
	}
	duration := time.Since(start)

	nsPerOp := duration.Nanoseconds() / int64(iterations)
	fmt.Printf("    BenchmarkFastStringJoin: %d Iterationen, ~%d ns/op\n", iterations, nsPerOp)
	fmt.Println("--- PASS: BenchmarkFastStringJoinSimulation")
}

func main() {
	fmt.Println("🧪 Starte Go 15 Testsuite...")
	TestSlugify_TableDriven()
	TestValidateEmail_TableDriven()
	TestFastStringJoin()
	BenchmarkFastStringJoinSimulation()
	fmt.Println("\n✅ Alle Tests in Go 15 erfolgreich bestanden!")
}
