package main

import (
	"errors"
	"fmt"
	"sync"
	"sync/atomic"
)

// ============================================================================
// 🚀 GO 12: MUTEX, RWMUTEX & ATOMIC OPERATIONS
// ============================================================================

// 🎯 TODO 1: Definiere das Struct 'SafeCache'
// Felder:
// - mu    sync.RWMutex
// - items map[string]string
type SafeCache struct {
	// TODO: Struct-Felder ergänzen
	mu    sync.RWMutex
	items map[string]string
}

// NewSafeCache erstellt eine initialisierte SafeCache-Instanz.
func NewSafeCache() *SafeCache {
	return &SafeCache{
		items: make(map[string]string),
	}
}

// 🎯 TODO 2a: Set(key, val string) - Schreibt einen Wert thread-safe in den Cache.
// Anforderungen:
// - Nutze c.mu.Lock() und per defer c.mu.Unlock()
func (c *SafeCache) Set(key, val string) {
	// TODO: Lock setzen, in items schreiben
}

// 🎯 TODO 2b: Get(key string) (string, bool) - Liest einen Wert thread-safe aus dem Cache.
// Anforderungen:
// - Nutze c.mu.RLock() und per defer c.mu.RUnlock()
func (c *SafeCache) Get(key string) (string, bool) {
	// TODO: RLock setzen, Wert und Existent-Flag zurückgeben
	return "", false
}

// 🎯 TODO 2c: Delete(key string) - Löscht einen Schlüssel thread-safe.
func (c *SafeCache) Delete(key string) {
	// TODO: Lock setzen, delete(c.items, key)
}

// 🎯 TODO 2d: Len() int - Gibt die Anzahl der Elemente thread-safe zurück.
func (c *SafeCache) Len() int {
	// TODO: RLock setzen, len(c.items) zurückgeben
	return 0
}

// 🎯 TODO 3: Implementiere 'AtomicCounter' mit lock-freiem sync/atomic
type AtomicCounter struct {
	val int64
}

// Inc erhöht den Zähler um 1 und gibt den neuen Wert zurück.
func (a *AtomicCounter) Inc() int64 {
	// TODO: atomic.AddInt64(&a.val, 1)
	return 0
}

// Add erhöht den Zähler um delta und gibt den neuen Wert zurück.
func (a *AtomicCounter) Add(delta int64) int64 {
	// TODO: atomic.AddInt64(&a.val, delta)
	return 0
}

// Value gibt den aktuellen Stand atomar zurück.
func (a *AtomicCounter) Value() int64 {
	// TODO: atomic.LoadInt64(&a.val)
	return 0
}

// Reset setzt den Zähler atomar auf 0 zurück.
func (a *AtomicCounter) Reset() {
	// TODO: atomic.StoreInt64(&a.val, 0)
}

// 🎯 TODO 4: Implementiere 'SafeBankAccount' mit sync.Mutex
type SafeBankAccount struct {
	mu      sync.Mutex
	balance float64
}

// Deposit zahlt einen Betrag sicher ein.
func (b *SafeBankAccount) Deposit(amount float64) {
	// TODO: b.mu.Lock(), Guthaben erhöhen
}

// Withdraw bucht einen Betrag ab, sofern ausreichend Guthaben vorhanden ist.
// Gibt bei unzureichendem Guthaben einen Fehler zurück: errors.New("insufficient funds").
func (b *SafeBankAccount) Withdraw(amount float64) error {
	// TODO: b.mu.Lock(), Guthaben prüfen und abbuchen oder Fehler werfen
	return nil
}

// Balance gibt das aktuelle Guthaben zurück.
func (b *SafeBankAccount) Balance() float64 {
	// TODO: b.mu.Lock(), Guthaben zurückgeben
	return 0.0
}

func main() {
	fmt.Println("=== Go 12: Mutex & Thread Safety ===")

	cache := NewSafeCache()
	var wg sync.WaitGroup

	// Parallele Schreiber
	for i := 0; i < 50; i++ {
		wg.Add(1)
		go func(id int) {
			defer wg.Done()
			cache.Set(fmt.Sprintf("key-%d", id), fmt.Sprintf("val-%d", id))
		}(i)
	}

	// Parallele Leser
	for i := 0; i < 50; i++ {
		wg.Add(1)
		go func(id int) {
			defer wg.Done()
			cache.Get(fmt.Sprintf("key-%d", id))
		}(i)
	}

	wg.Wait()
	fmt.Printf("Cache erfolgreich befüllt. Gesamtelemente: %d\n", cache.Len())
}
