package main

import (
	"context"
	"errors"
	"fmt"
	"time"
)

// ============================================================================
// 💡 GO 11: MUSTERLÖSUNG (select, Timeouts & Context)
// ============================================================================

var ErrTimeout = errors.New("timeout exceeded")

// FastestResponse liest mit select den Kanal aus, der zuerst liefert.
func FastestResponse(ch1, ch2 <-chan string) string {
	select {
	case res := <-ch1:
		return res
	case res := <-ch2:
		return res
	}
}

// FetchWithTimeout liest aus dem Kanal oder bricht nach Ablauf der Zeit ab.
func FetchWithTimeout(ch <-chan string, timeout time.Duration) (string, error) {
	select {
	case res := <-ch:
		return res, nil
	case <-time.After(timeout):
		return "", ErrTimeout
	}
}

// TrySend sendet nicht-blockierend in den Kanal.
func TrySend(ch chan<- int, val int) bool {
	select {
	case ch <- val:
		return true
	default:
		return false
	}
}

// TryReceive liest nicht-blockierend aus dem Kanal.
func TryReceive(ch <-chan int) (int, bool) {
	select {
	case val := <-ch:
		return val, true
	default:
		return 0, false
	}
}

// QueryWithContext führt eine Funktion asynchron aus und reagiert auf context.Done().
func QueryWithContext(ctx context.Context, fn func() string) (string, error) {
	resCh := make(chan string, 1)

	go func() {
		resCh <- fn()
	}()

	select {
	case <-ctx.Done():
		return "", ctx.Err()
	case res := <-resCh:
		return res, nil
	}
}

func main() {
	fmt.Println("=== Go 11: Musterlösung ===")

	fastCh := make(chan string, 1)
	slowCh := make(chan string, 1)

	fastCh <- "Antwort von Node-A (10ms)"
	slowCh <- "Antwort von Node-B (150ms)"

	winner := FastestResponse(fastCh, slowCh)
	fmt.Println("Schnellster Server:", winner)

	unresponsiveCh := make(chan string)
	res, err := FetchWithTimeout(unresponsiveCh, 50*time.Millisecond)
	if err != nil {
		fmt.Printf("Erwarteter Timeout-Fehler: %v\n", err)
	} else {
		fmt.Println("Ergebnis:", res)
	}
}
