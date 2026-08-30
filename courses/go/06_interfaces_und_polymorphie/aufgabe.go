package main

import (
	"errors"
	"fmt"
)

// 🎯 TEILZIEL 1 (TODO 1): Definiere das Interface Storage
// Methoden:
// - Save(key string, val string) error
// - Get(key string) (string, bool)
// - Count() int
type Storage interface {
	Save(key string, val string) error
	Get(key string) (string, bool)
	Count() int
}

// 🎯 TEILZIEL 2 (TODO 2): Implementiere MemoryStorage, das das Interface Storage implizit erfüllt
type MemoryStorage struct {
	data map[string]string
}

// NewMemoryStorage initialisiert die interne Map und gibt *MemoryStorage zurück.
func NewMemoryStorage() *MemoryStorage {
	// TODO: Initialisiere MemoryStorage mit leerer Map
	return nil
}

// Save speichert den Key-Value-Eintrag.
// Falls key leer ist (""), gib errors.New("key darf nicht leer sein") zurück.
func (m *MemoryStorage) Save(key string, val string) error {
	// TODO: Validierung und Speichern in Map
	return nil
}

// Get liest den Wert aus. Gibt (Wert, true) oder ("", false) zurück.
func (m *MemoryStorage) Get(key string) (string, bool) {
	// TODO: Wert aus Map abrufen
	return "", false
}

// Count gibt die Anzahl der gespeicherten Elemente zurück.
func (m *MemoryStorage) Count() int {
	// TODO: Anzahl der Elemente in der Map zurückgeben
	return 0
}

// 🎯 TEILZIEL 3 (TODO 3): Polymorphe Datensynchronisation
// SyncData kopiert alle in 'keys' genannten Einträge von 'source' nach 'target'.
// Falls source oder target nil ist, gib (0, errors.New("storage darf nicht nil sein")) zurück.
// Gibt die Anzahl der erfolgreich übertragenen Schlüssel zurück.
func SyncData(source Storage, target Storage, keys []string) (int, error) {
	// TODO: Daten über das Storage Interface synchronisieren
	return 0, nil
}

// 🎯 TEILZIEL 4 (TODO 4): Type Switch mit dem leeren Interface (any)
// Untersuche den Typ von 'val':
// - int: "Zahl: [val * 2]" (z.B. 10 -> "Zahl: 20")
// - string: "Text: [val] ([Länge] Zeichen)" (z.B. "Go" -> "Text: Go (2 Zeichen)")
// - bool: "Flag: [true/false]"
// - Default: "Unbekannter Typ"
func TypPruefung(val any) string {
	// TODO: Verwende switch v := val.(type)
	return ""
}

func main() {
	s1 := NewMemoryStorage()
	if s1 != nil {
		s1.Save("k1", "v1")
		s1.Save("k2", "v2")
		val, _ := s1.Get("k1")
		fmt.Printf("Storage Count: %d, k1 = %s\n", s1.Count(), val)
	}

	fmt.Println(TypPruefung(42))
	fmt.Println(TypPruefung("Golang"))
	fmt.Println(TypPruefung(true))
}
