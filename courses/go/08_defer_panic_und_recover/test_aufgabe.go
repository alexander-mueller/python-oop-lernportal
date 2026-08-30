package main

import (
	"reflect"
	"testing"
)

func TestProtokollierteOperationDefer(t *testing.T) {
	var logs []string
	res := ProtokollierteOperation("SyncJob", &logs)

	if res != "ERFOLG: SyncJob" {
		t.Errorf("ProtokollierteOperation() = %q; erwartet 'ERFOLG: SyncJob'", res)
	}

	expectedLogs := []string{"START: SyncJob", "ENDE: SyncJob"}
	if !reflect.DeepEqual(logs, expectedLogs) {
		t.Errorf("Logs = %v; erwartet %v", logs, expectedLogs)
	}
}

func TestRessourcenManager(t *testing.T) {
	rm := &RessourcenManager{}

	res := rm.FuehreTransaktionAus(func() int {
		if rm.ActiveLocks != 1 {
			t.Errorf("ActiveLocks während Transaktion = %d; erwartet 1", rm.ActiveLocks)
		}
		return 100
	})

	if res != 100 {
		t.Errorf("Transaktionsergebnis = %d; erwartet 100", res)
	}

	if rm.ActiveLocks != 0 {
		t.Errorf("ActiveLocks nach Transaktion = %d; erwartet 0", rm.ActiveLocks)
	}
}

func TestKritischeBerechnungPanic(t *testing.T) {
	if res := KritischeBerechnung(10); res != 100 {
		t.Errorf("KritischeBerechnung(10) = %d; erwartet 100", res)
	}

	defer func() {
		r := recover()
		if r == nil {
			t.Errorf("KritischeBerechnung(0) sollte gepanickt haben")
		} else if r != "division durch null" {
			t.Errorf("Panic Grund = %v; erwartet 'division durch null'", r)
		}
	}()

	KritischeBerechnung(0)
}

func TestSichereAusfuehrungRecover(t *testing.T) {
	// Test Normalfall
	recVal, okSuccess := SichereAusfuehrung(func() {
		_ = 1 + 1
	})
	if !okSuccess || recVal != nil {
		t.Errorf("SichereAusfuehrung normal = (%v, %t); erwartet (nil, true)", recVal, okSuccess)
	}

	// Test Panic-Abfangung
	panicReason, okPanic := SichereAusfuehrung(func() {
		panic("datenbank verbindung verloren")
	})
	if okPanic != false || panicReason != "datenbank verbindung verloren" {
		t.Errorf("SichereAusfuehrung mit Panic = (%v, %t); erwartet ('datenbank verbindung verloren', false)", panicReason, okPanic)
	}
}
