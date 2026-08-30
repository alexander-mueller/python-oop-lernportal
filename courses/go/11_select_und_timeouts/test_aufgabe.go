package main

import (
	"context"
	"errors"
	"fmt"
	"time"
)

// 🧪 GO 11 TESTSUITE: select, Timeouts & Context

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

// TEST: TestFastestResponse - Prüft select über zwei Kanäle
func TestFastestResponse() {
	fmt.Println("=== RUN   TestFastestResponse")
	ch1 := make(chan string, 1)
	ch2 := make(chan string, 1)

	ch1 <- "Fast-1"
	res := FastestResponse(ch1, ch2)
	assertEquals(res, "Fast-1", "Sollte den bereiten Kanal ch1 wählen")

	ch2 <- "Fast-2"
	res2 := FastestResponse(ch1, ch2)
	assertEquals(res2, "Fast-2", "Sollte den bereiten Kanal ch2 wählen")
	fmt.Println("--- PASS: TestFastestResponse")
}

// TEST: TestFetchWithTimeout - Prüft Datenempfang vs. Timeout
func TestFetchWithTimeout() {
	fmt.Println("=== RUN   TestFetchWithTimeout")
	// 1. Erfolgreicher Empfang
	readyCh := make(chan string, 1)
	readyCh <- "Data-OK"
	res, err := FetchWithTimeout(readyCh, 100*time.Millisecond)
	assertEquals(err, nil, "Sollte keinen Fehler werfen bei bereiten Daten")
	assertEquals(res, "Data-OK", "Daten müssen übereinstimmen")

	// 2. Timeout-Fall
	slowCh := make(chan string) // Nie befüllt
	start := time.Now()
	_, errTimeout := FetchWithTimeout(slowCh, 30*time.Millisecond)
	duration := time.Since(start)

	assert(errTimeout != nil, "Sollte bei blockiertem Kanal einen Timeout-Fehler liefern")
	assert(duration >= 25*time.Millisecond, "Sollte mindestens die angegebene Timeout-Dauer warten")
	fmt.Println("--- PASS: TestFetchWithTimeout")
}

// TEST: TestNonBlockingOperations - Prüft TrySend und TryReceive
func TestNonBlockingOperations() {
	fmt.Println("=== RUN   TestNonBlockingOperations")
	ch := make(chan int, 1)

	// 1. TrySend auf leeren Puffer
	okSend1 := TrySend(ch, 42)
	assertEquals(okSend1, true, "Erstes TrySend in Puffer (Größe 1) muss erfolgreich sein")

	// 2. TrySend auf vollen Puffer
	okSend2 := TrySend(ch, 99)
	assertEquals(okSend2, false, "Zweites TrySend in vollen Puffer muss false liefern")

	// 3. TryReceive mit Daten
	val, okRecv1 := TryReceive(ch)
	assertEquals(okRecv1, true, "TryReceive muss true liefern bei vorhandenen Daten")
	assertEquals(val, 42, "Gelesener Wert muss 42 sein")

	// 4. TryReceive auf leerem Channel
	_, okRecv2 := TryReceive(ch)
	assertEquals(okRecv2, false, "TryReceive auf leerem Channel muss false liefern")
	fmt.Println("--- PASS: TestNonBlockingOperations")
}

// TEST: TestQueryWithContext - Prüft Context Cancellation und Deadlines
func TestQueryWithContext() {
	fmt.Println("=== RUN   TestQueryWithContext")
	// 1. Erfolgreicher Context
	ctxSuccess, cancel1 := context.WithTimeout(context.Background(), 200*time.Millisecond)
	defer cancel1()

	res, err := QueryWithContext(ctxSuccess, func() string {
		return "DB-Data"
	})
	assertEquals(err, nil, "Sollte erfolgreich sein")
	assertEquals(res, "DB-Data", "Ergebnis muss DB-Data sein")

	// 2. Timeout Context
	ctxTimeout, cancel2 := context.WithTimeout(context.Background(), 20*time.Millisecond)
	defer cancel2()

	_, errTimeout := QueryWithContext(ctxTimeout, func() string {
		time.Sleep(100 * time.Millisecond)
		return "Too-Late"
	})
	assert(errors.Is(errTimeout, context.DeadlineExceeded), "Fehler muss context.DeadlineExceeded sein")
	fmt.Println("--- PASS: TestQueryWithContext")
}

func main() {
	fmt.Println("🧪 Starte Go 11 Testsuite...")
	TestFastestResponse()
	TestFetchWithTimeout()
	TestNonBlockingOperations()
	TestQueryWithContext()
	fmt.Println("\n✅ Alle Tests in Go 11 erfolgreich bestanden!")
}
