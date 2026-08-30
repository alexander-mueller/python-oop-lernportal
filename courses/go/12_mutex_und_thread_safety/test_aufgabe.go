package main

import (
	"fmt"
	"sync"
)

// 🧪 GO 12 TESTSUITE: Mutex, RWMutex & Atomics

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

// TEST: TestSafeCacheConcurrency - Stresstest mit parallelen Schreibern und Lesern
func TestSafeCacheConcurrency() {
	fmt.Println("=== RUN   TestSafeCacheConcurrency")
	cache := NewSafeCache()
	var wg sync.WaitGroup
	numOps := 100

	// 100 parallele Schreiber
	for i := 0; i < numOps; i++ {
		wg.Add(1)
		go func(id int) {
			defer wg.Done()
			cache.Set(fmt.Sprintf("k-%d", id), fmt.Sprintf("v-%d", id))
		}(i)
	}

	// 100 parallele Leser
	for i := 0; i < numOps; i++ {
		wg.Add(1)
		go func(id int) {
			defer wg.Done()
			cache.Get(fmt.Sprintf("k-%d", id))
		}(i)
	}

	wg.Wait()
	assertEquals(cache.Len(), numOps, "Alle 100 Elemente müssen im Cache vorhanden sein")

	// Löschen testen
	cache.Delete("k-0")
	assertEquals(cache.Len(), numOps-1, "Cache-Größe muss nach Delete 99 sein")
	_, exists := cache.Get("k-0")
	assertEquals(exists, false, "Gelöschter Key darf nicht mehr existieren")
	fmt.Println("--- PASS: TestSafeCacheConcurrency")
}

// TEST: TestAtomicCounterConcurrency - Stresstest für lock-freie Atomics
func TestAtomicCounterConcurrency() {
	fmt.Println("=== RUN   TestAtomicCounterConcurrency")
	var counter AtomicCounter
	var wg sync.WaitGroup
	numGoroutines := 1000

	for i := 0; i < numGoroutines; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			counter.Inc()
		}()
	}

	wg.Wait()
	assertEquals(counter.Value(), int64(1000), "Zähler muss nach 1000 atomaren Incs exakt 1000 sein")

	counter.Add(500)
	assertEquals(counter.Value(), int64(1500), "Add(500) muss Zähler auf 1500 setzen")

	counter.Reset()
	assertEquals(counter.Value(), int64(0), "Reset() muss Zähler auf 0 zurücksetzen")
	fmt.Println("--- PASS: TestAtomicCounterConcurrency")
}

// TEST: TestSafeBankAccountConcurrency - Prüft Kontoüberweisungen und Schutz vor Überziehung
func TestSafeBankAccountConcurrency() {
	fmt.Println("=== RUN   TestSafeBankAccountConcurrency")
	account := &SafeBankAccount{}
	account.Deposit(1000.0)

	var wg sync.WaitGroup
	numWithdraws := 10

	// 10 Goroutines buchen jeweils 50 Euro ab
	for i := 0; i < numWithdraws; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			err := account.Withdraw(50.0)
			assert(err == nil, "Auszahlung muss erfolgreich sein")
		}()
	}

	wg.Wait()
	assertEquals(account.Balance(), 500.0, "Restguthaben muss exakt 500.0 betragen")

	// Überziehungstest
	errOverdraft := account.Withdraw(600.0)
	assert(errOverdraft != nil, "Überziehung über 500 Euro muss mit Fehler abbrechen")
	assertEquals(account.Balance(), 500.0, "Guthaben darf sich bei fehlgeschlagener Abbuchung nicht ändern")
	fmt.Println("--- PASS: TestSafeBankAccountConcurrency")
}

func main() {
	fmt.Println("🧪 Starte Go 12 Testsuite...")
	TestSafeCacheConcurrency()
	TestAtomicCounterConcurrency()
	TestSafeBankAccountConcurrency()
	fmt.Println("\n✅ Alle Tests in Go 12 erfolgreich bestanden!")
}
