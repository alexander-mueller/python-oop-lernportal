package main

import (
	"context"
	"errors"
	"fmt"
	"time"
)

// ============================================================================
// 🚀 GO 11: SELECT, TIMEOUTS & CONTEXT CANCELLATION
// ============================================================================

var ErrTimeout = errors.New("timeout exceeded")

// 🎯 TODO 1: Implementiere 'FastestResponse'
// Parameter:
// - ch1: Erster Antwortkanal (<-chan string)
// - ch2: Zweiter Antwortkanal (<-chan string)
// Rückgabe:
// - Der Wert des Kanals, der zuerst Daten liefert
//
// Anforderungen:
// Nutze ein 'select'-Statement, um auf den schnellsten Kanal zu warten.
func FastestResponse(ch1, ch2 <-chan string) string {
	// TODO: select auf ch1 und ch2
	return ""
}

// 🎯 TODO 2: Implementiere 'FetchWithTimeout'
// Parameter:
// - ch: Antwortkanal (<-chan string)
// - timeout: Maximale Wartezeit (time.Duration)
// Rückgabe:
// - Daten-String und nil bei Erfolg
// - "", ErrTimeout wenn die Zeit abläuft
//
// Anforderungen:
// Nutze 'select' mit 'case res := <-ch' und 'case <-time.After(timeout)'.
func FetchWithTimeout(ch <-chan string, timeout time.Duration) (string, error) {
	// TODO: select mit Channel-Empfang und time.After
	return "", nil
}

// 🎯 TODO 3a: Implementiere 'TrySend' (Non-Blocking Send)
// Parameter:
// - ch: Sende-Kanal (chan<- int)
// - val: Zu sendender Integer
// Rückgabe:
// - true, wenn der Wert sofort ohne Blockieren gesendet werden konnte
// - false, wenn der Channel voll ist
func TrySend(ch chan<- int, val int) bool {
	// TODO: select mit ch <- val und default: return false
	return false
}

// 🎯 TODO 3b: Implementiere 'TryReceive' (Non-Blocking Receive)
// Parameter:
// - ch: Empfangs-Kanal (<-chan int)
// Rückgabe:
// - (val, true), wenn ein Wert sofort gelesen werden konnte
// - (0, false), wenn der Channel leer ist
func TryReceive(ch <-chan int) (int, bool) {
	// TODO: select mit case v := <-ch und default: return 0, false
	return 0, false
}

// 🎯 TODO 4: Implementiere 'QueryWithContext'
// Parameter:
// - ctx: context.Context (z.B. mit Timeout oder Cancel)
// - fn: Eine langwierige synchrone Abfragefunktion func() string
// Rückgabe:
// - Ergebnis-String und nil bei Erfolg
// - "", ctx.Err() wenn der Kontext abbricht oder timed out
//
// Anforderungen:
// 1. Erstelle einen gepufferten Ergebniskanal: resCh := make(chan string, 1).
// 2. Starte 'fn' in einer Goroutine und sende das Ergebnis in 'resCh'.
// 3. Nutze 'select', um auf '<-resCh' oder '<-ctx.Done()' zu warten.
func QueryWithContext(ctx context.Context, fn func() string) (string, error) {
	// TODO: Goroutine mit Ergebniskanal und select auf ctx.Done()
	return "", nil
}

func main() {
	fmt.Println("=== Go 11: select, Timeouts & Context ===")

	// 1. Schneller vs. langsamer Service
	fastCh := make(chan string, 1)
	slowCh := make(chan string, 1)

	fastCh <- "Antwort von Node-A (10ms)"
	slowCh <- "Antwort von Node-B (150ms)"

	winner := FastestResponse(fastCh, slowCh)
	fmt.Println("Schnellster Server:", winner)

	// 2. Timeout Demo
	unresponsiveCh := make(chan string)
	res, err := FetchWithTimeout(unresponsiveCh, 50*time.Millisecond)
	if err != nil {
		fmt.Printf("Erwarteter Timeout-Fehler: %v\n", err)
	} else {
		fmt.Println("Ergebnis:", res)
	}
}
