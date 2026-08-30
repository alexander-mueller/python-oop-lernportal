package main

import (
	"fmt"
)

// 🎯 TEILZIEL 1 (TODO 1): Protokolliere den Start und das Ende einer Operation mit defer
// Ablauf in ProtokollierteOperation:
// 1. Hänge "START: " + name an *logEntries an.
// 2. Registriere ein defer, das "ENDE: " + name an *logEntries anhängt.
// 3. Gib "ERFOLG: " + name zurück.
func ProtokollierteOperation(name string, logEntries *[]string) string {
	// TODO: Start eintragen, defer für Ende registrieren und Ergebnis zurückgeben
	return ""
}

// 🎯 TEILZIEL 2 (TODO 2): Ressourcen-Manager
type RessourcenManager struct {
	ActiveLocks int
}

func (rm *RessourcenManager) Acquire() {
	rm.ActiveLocks++
}

func (rm *RessourcenManager) Release() {
	if rm.ActiveLocks > 0 {
		rm.ActiveLocks--
	}
}

// FuehreTransaktionAus soll:
// 1. rm.Acquire() aufrufen
// 2. per defer rm.Release() sicherstellen
// 3. workFn() ausführen und das Ergebnis zurückgeben
func (rm *RessourcenManager) FuehreTransaktionAus(workFn func() int) int {
	// TODO: Acquire aufrufen, defer Release registrieren, workFn ausführen
	return 0
}

// 🎯 TEILZIEL 3 (TODO 3): Kritische Berechnung mit explizitem panic
// Falls teiler == 0 ist: rufe panic("division durch null") auf.
// Andernfalls: gib 1000 / teiler zurück.
func KritischeBerechnung(teiler int) int {
	// TODO: Bei teiler == 0 panicken, sonst Ganzzahldivision
	return 0
}

// 🎯 TEILZIEL 4 (TODO 4): Sichere Ausführung mit defer und recover()
// Führe 'fn()' geschützt aus:
// - Wenn fn() ohne Panic durchläuft: gib (nil, true) zurück.
// - Wenn fn() einen Panic auslöst: fange ihn mit recover() ab und gib (panicGrund, false) zurück.
func SichereAusfuehrung(fn func()) (recoveredErr any, ok bool) {
	// TODO: Nutze defer mit anonymer Funktion und recover()
	return nil, false
}

func main() {
	var logs []string
	res := ProtokollierteOperation("Datenbank-Backup", &logs)
	fmt.Printf("%s | Logs: %v\n", res, logs)

	rm := &RessourcenManager{}
	tRes := rm.FuehreTransaktionAus(func() int {
		return 42 * 2
	})
	fmt.Printf("Transaktion Resultat: %d, Locks nach Ende: %d\n", tRes, rm.ActiveLocks)

	err, ok := SichereAusfuehrung(func() {
		KritischeBerechnung(0)
	})
	fmt.Printf("Panic abgefangen: ok=%t, Fehler=%v\n", ok, err)
}
