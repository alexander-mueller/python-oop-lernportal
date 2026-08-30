package main

import (
	"errors"
	"fmt"
)

type Storage interface {
	Save(key string, val string) error
	Get(key string) (string, bool)
	Count() int
}

type MemoryStorage struct {
	data map[string]string
}

func NewMemoryStorage() *MemoryStorage {
	return &MemoryStorage{
		data: make(map[string]string),
	}
}

func (m *MemoryStorage) Save(key string, val string) error {
	if key == "" {
		return errors.New("key darf nicht leer sein")
	}
	if m.data == nil {
		m.data = make(map[string]string)
	}
	m.data[key] = val
	return nil
}

func (m *MemoryStorage) Get(key string) (string, bool) {
	if m == nil || m.data == nil {
		return "", false
	}
	val, ok := m.data[key]
	return val, ok
}

func (m *MemoryStorage) Count() int {
	if m == nil || m.data == nil {
		return 0
	}
	return len(m.data)
}

func SyncData(source Storage, target Storage, keys []string) (int, error) {
	if source == nil || target == nil {
		return 0, errors.New("storage darf nicht nil sein")
	}
	synced := 0
	for _, k := range keys {
		if val, exists := source.Get(k); exists {
			if err := target.Save(k, val); err == nil {
				synced++
			}
		}
	}
	return synced, nil
}

func TypPruefung(val any) string {
	switch v := val.(type) {
	case int:
		return fmt.Sprintf("Zahl: %d", v*2)
	case string:
		return fmt.Sprintf("Text: %s (%d Zeichen)", v, len(v))
	case bool:
		return fmt.Sprintf("Flag: %t", v)
	default:
		return "Unbekannter Typ"
	}
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
