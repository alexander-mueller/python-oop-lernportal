package main

import (
	"testing"
)

func TestMemoryStorageInterface(t *testing.T) {
	var s Storage = NewMemoryStorage()
	if s == nil {
		t.Fatalf("NewMemoryStorage lieferte nil")
	}

	err := s.Save("token", "secret123")
	if err != nil {
		t.Errorf("s.Save() unerwarteter Fehler: %v", err)
	}

	val, ok := s.Get("token")
	if !ok || val != "secret123" {
		t.Errorf("s.Get('token') = (%q, %t); erwartet ('secret123', true)", val, ok)
	}

	if count := s.Count(); count != 1 {
		t.Errorf("s.Count() = %d; erwartet 1", count)
	}

	errEmptyKey := s.Save("", "value")
	if errEmptyKey == nil {
		t.Errorf("s.Save('') mit leerem Key sollte einen Fehler werfen")
	}
}

func TestSyncDataPolymorphism(t *testing.T) {
	src := NewMemoryStorage()
	dst := NewMemoryStorage()

	src.Save("app.name", "CloudService")
	src.Save("app.port", "8080")
	src.Save("app.env", "prod")

	synced, err := SyncData(src, dst, []string{"app.name", "app.port", "nonexistent"})
	if err != nil {
		t.Errorf("SyncData() unerwarteter Fehler: %v", err)
	}
	if synced != 2 {
		t.Errorf("SyncData() synced count = %d; erwartet 2", synced)
	}

	val, ok := dst.Get("app.name")
	if !ok || val != "CloudService" {
		t.Errorf("dst.Get('app.name') = (%q, %t); erwartet ('CloudService', true)", val, ok)
	}

	_, errNil := SyncData(nil, dst, []string{"key"})
	if errNil == nil {
		t.Errorf("SyncData mit nil Storage sollte Fehler liefern")
	}
}

func TestTypPruefungTypeSwitch(t *testing.T) {
	resInt := TypPruefung(10)
	if resInt != "Zahl: 20" {
		t.Errorf("TypPruefung(10) = %q; erwartet 'Zahl: 20'", resInt)
	}

	resStr := TypPruefung("Golang")
	if resStr != "Text: Golang (6 Zeichen)" {
		t.Errorf("TypPruefung('Golang') = %q; erwartet 'Text: Golang (6 Zeichen)'", resStr)
	}

	resBool := TypPruefung(true)
	if resBool != "Flag: true" {
		t.Errorf("TypPruefung(true) = %q; erwartet 'Flag: true'", resBool)
	}

	resOther := TypPruefung(3.14159)
	if resOther != "Unbekannter Typ" {
		t.Errorf("TypPruefung(3.14159) = %q; erwartet 'Unbekannter Typ'", resOther)
	}
}

func TestEmptyInterfaceHandling(t *testing.T) {
	res := TypPruefung(struct{}{})
	if res != "Unbekannter Typ" {
		t.Errorf("TypPruefung(struct) = %q; erwartet 'Unbekannter Typ'", res)
	}
}
