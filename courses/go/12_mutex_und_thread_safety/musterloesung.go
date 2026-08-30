package main

import (
	"errors"
	"fmt"
	"sync"
	"sync/atomic"
)

// ============================================================================
// 💡 GO 12: MUSTERLÖSUNG (Mutex, RWMutex & Atomics)
// ============================================================================

// SafeCache ist ein thread-sicherer In-Memory Cache mit optimiertem sync.RWMutex.
type SafeCache struct {
	mu    sync.RWMutex
	items map[string]string
}

// NewSafeCache erstellt eine initialisierte SafeCache-Instanz.
func NewSafeCache() *SafeCache {
	return &SafeCache{
		items: make(map[string]string),
	}
}

// Set speichert einen Schlüssel-Wert-Eintrag mit exklusivem Write-Lock.
func (c *SafeCache) Set(key, val string) {
	c.mu.Lock()
	defer c.mu.Unlock()
	c.items[key] = val
}

// Get liest einen Eintrag mit shared Read-Lock.
func (c *SafeCache) Get(key string) (string, bool) {
	c.mu.RLock()
	defer c.mu.RUnlock()
	val, ok := c.items[key]
	return val, ok
}

// Delete entfernt einen Eintrag mit exklusivem Write-Lock.
func (c *SafeCache) Delete(key string) {
	c.mu.Lock()
	defer c.mu.Unlock()
	delete(c.items, key)
}

// Len gibt die Anzahl der gecachten Einträge zurück.
func (c *SafeCache) Len() int {
	c.mu.RLock()
	defer c.mu.RUnlock()
	return len(c.items)
}

// AtomicCounter verwaltet einen Zähler lock-frei über Hardware-Atomics.
type AtomicCounter struct {
	val int64
}

// Inc erhöht den Zähler um 1.
func (a *AtomicCounter) Inc() int64 {
	return atomic.AddInt64(&a.val, 1)
}

// Add erhöht den Zähler um einen beliebigen Betrag.
func (a *AtomicCounter) Add(delta int64) int64 {
	return atomic.AddInt64(&a.val, delta)
}

// Value liest den aktuellen Zählerstand atomar.
func (a *AtomicCounter) Value() int64 {
	return atomic.LoadInt64(&a.val)
}

// Reset setzt den Zähler auf 0 zurück.
func (a *AtomicCounter) Reset() {
	atomic.StoreInt64(&a.val, 0)
}

// SafeBankAccount schützt Kontobuchungen mit sync.Mutex.
type SafeBankAccount struct {
	mu      sync.Mutex
	balance float64
}

// Deposit bucht einen Geldbetrag sicher ein.
func (b *SafeBankAccount) Deposit(amount float64) {
	b.mu.Lock()
	defer b.mu.Unlock()
	b.balance += amount
}

// Withdraw bucht einen Geldbetrag ab oder meldet einen Fehler bei Unterdeckung.
func (b *SafeBankAccount) Withdraw(amount float64) error {
	b.mu.Lock()
	defer b.mu.Unlock()
	if b.balance < amount {
		return errors.New("insufficient funds")
	}
	b.balance -= amount
	return nil
}

// Balance gibt das aktuelle Guthaben zurück.
func (b *SafeBankAccount) Balance() float64 {
	b.mu.Lock()
	defer b.mu.Unlock()
	return b.balance
}

func main() {
	fmt.Println("=== Go 12: Musterlösung ===")

	cache := NewSafeCache()
	var wg sync.WaitGroup

	for i := 0; i < 50; i++ {
		wg.Add(1)
		go func(id int) {
			defer wg.Done()
			cache.Set(fmt.Sprintf("key-%d", id), fmt.Sprintf("val-%d", id))
		}(i)
	}

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
