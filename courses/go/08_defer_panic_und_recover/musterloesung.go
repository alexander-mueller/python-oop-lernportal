package main

import (
	"fmt"
)

func ProtokollierteOperation(name string, logEntries *[]string) string {
	if logEntries != nil {
		*logEntries = append(*logEntries, "START: "+name)
		defer func() {
			*logEntries = append(*logEntries, "ENDE: "+name)
		}()
	}
	return "ERFOLG: " + name
}

type RessourcenManager struct {
	ActiveLocks int
}

func (rm *RessourcenManager) Acquire() {
	if rm != nil {
		rm.ActiveLocks++
	}
}

func (rm *RessourcenManager) Release() {
	if rm != nil && rm.ActiveLocks > 0 {
		rm.ActiveLocks--
	}
}

func (rm *RessourcenManager) FuehreTransaktionAus(workFn func() int) int {
	if rm == nil {
		if workFn != nil {
			return workFn()
		}
		return 0
	}
	rm.Acquire()
	defer rm.Release()

	if workFn != nil {
		return workFn()
	}
	return 0
}

func KritischeBerechnung(teiler int) int {
	if teiler == 0 {
		panic("division durch null")
	}
	return 1000 / teiler
}

func SichereAusfuehrung(fn func()) (recoveredErr any, ok bool) {
	defer func() {
		if r := recover(); r != nil {
			recoveredErr = r
			ok = false
		}
	}()

	if fn != nil {
		fn()
	}
	return nil, true
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
