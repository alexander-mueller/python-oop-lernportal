package main

import (
	"fmt"
	"strings"
	"sync"
	"time"
)

// 🧪 GO 09 TESTSUITE: Goroutines & sync.WaitGroup

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

// TEST: TestServerMetricStruct - Überprüft Struct-Definition
func TestServerMetricStruct() {
	fmt.Println("=== RUN   TestServerMetricStruct")
	m := ServerMetric{
		ServerID:  "srv-test-1",
		LatencyMs: 25,
		Status:    "ONLINE",
		Timestamp: time.Now(),
	}
	assertEquals(m.ServerID, "srv-test-1", "ServerID muss korrekt gesetzt sein")
	assertEquals(m.LatencyMs, 25, "LatencyMs muss 25 sein")
	assertEquals(m.Status, "ONLINE", "Status muss ONLINE sein")
	fmt.Println("--- PASS: TestServerMetricStruct")
}

// TEST: TestCheckServerWorker - Prüft die CheckServer Worker-Funktion
func TestCheckServerWorker() {
	fmt.Println("=== RUN   TestCheckServerWorker")
	var wg sync.WaitGroup
	out := make(chan ServerMetric, 3)

	wg.Add(3)
	go CheckServer("srv-fast", &wg, out)
	go CheckServer("slow-db", &wg, out)
	go CheckServer("offline-gateway", &wg, out)

	wg.Wait()
	close(out)

	results := make(map[string]ServerMetric)
	for m := range out {
		results[m.ServerID] = m
	}

	assertEquals(len(results), 3, "Alle 3 Server-Checks müssen im Channel ankommen")
	assertEquals(results["srv-fast"].Status, "ONLINE", "srv-fast sollte ONLINE sein")
	assertEquals(results["slow-db"].Status, "DEGRADED", "slow-db sollte DEGRADED sein")
	assertEquals(results["offline-gateway"].Status, "OFFLINE", "offline-gateway sollte OFFLINE sein")
	fmt.Println("--- PASS: TestCheckServerWorker")
}

// TEST: TestBatchHealthCheckConcurrency - Prüft Batch-Health-Check und Sortierung
func TestBatchHealthCheckConcurrency() {
	fmt.Println("=== RUN   TestBatchHealthCheckConcurrency")
	servers := []string{"srv-gamma", "slow-beta", "srv-alpha", "offline-delta"}
	start := time.Now()
	metrics := BatchHealthCheck(servers)
	duration := time.Since(start)

	assertEquals(len(metrics), 4, "BatchHealthCheck sollte 4 Metriken liefern")
	// Prüfen auf aufsteigende Sortierung nach ServerID
	assertEquals(metrics[0].ServerID, "offline-delta", "Erstes Element muss sortiert sein")
	assertEquals(metrics[1].ServerID, "slow-beta", "Zweites Element muss sortiert sein")
	assertEquals(metrics[2].ServerID, "srv-alpha", "Drittes Element muss sortiert sein")
	assertEquals(metrics[3].ServerID, "srv-gamma", "Viertes Element muss sortiert sein")

	assert(duration < 2*time.Second, "Parallele Ausführung darf nicht sequentiell blockieren")
	fmt.Println("--- PASS: TestBatchHealthCheckConcurrency")
}

// TEST: TestParallelTaskRunnerOrdering - Prüft Task-Runner mit Index-Erhalt
func TestParallelTaskRunnerOrdering() {
	fmt.Println("=== RUN   TestParallelTaskRunnerOrdering")
	tasks := []func() string{
		func() string { return "Result-0" },
		func() string { return "Result-1" },
		func() string { return "Result-2" },
		func() string { return "Result-3" },
	}

	results := ParallelTaskRunner(tasks)
	assertEquals(len(results), 4, "ParallelTaskRunner muss 4 Ergebnisse zurückgeben")
	for i := 0; i < 4; i++ {
		expected := fmt.Sprintf("Result-%d", i)
		assertEquals(results[i], expected, fmt.Sprintf("Index %d muss übereinstimmen", i))
	}
	fmt.Println("--- PASS: TestParallelTaskRunnerOrdering")
}

func main() {
	fmt.Println("🧪 Starte Go 09 Testsuite...")
	TestServerMetricStruct()
	TestCheckServerWorker()
	TestBatchHealthCheckConcurrency()
	TestParallelTaskRunnerOrdering()
	fmt.Println("\n✅ Alle Tests in Go 09 erfolgreich bestanden!")
}
