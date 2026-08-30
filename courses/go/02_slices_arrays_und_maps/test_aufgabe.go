package main

import (
	"reflect"
	"testing"
)

func TestFiltereGeradeZahlen(t *testing.T) {
	input := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	expected := []int{2, 4, 6, 8, 10}
	res := FiltereGeradeZahlen(input)

	if !reflect.DeepEqual(res, expected) {
		t.Errorf("FiltereGeradeZahlen(%v) = %v; erwartet %v", input, res, expected)
	}

	emptyRes := FiltereGeradeZahlen([]int{1, 3, 5})
	if len(emptyRes) != 0 {
		t.Errorf("FiltereGeradeZahlen([1, 3, 5]) sollte Länge 0 haben, hat %d", len(emptyRes))
	}
}

func TestErweitereProtokolle(t *testing.T) {
	logs := []string{"log1", "log2", "log3"}
	res := ErweitereProtokolle(logs, "log4", "log5")
	if len(res) != 5 {
		t.Errorf("ErweitereProtokolle() Länge = %d; erwartet 5", len(res))
	}

	// Test auf Begrenzung auf maximal 10 Einträge
	longLogs := []string{"1", "2", "3", "4", "5", "6", "7", "8"}
	resLong := ErweitereProtokolle(longLogs, "9", "10", "11", "12")
	if len(resLong) != 10 {
		t.Errorf("ErweitereProtokolle() sollte max 10 Einträge halten, hat %d", len(resLong))
	}
	if resLong[0] != "3" || resLong[9] != "12" {
		t.Errorf("ErweitereProtokolle() Fenster inkorrekt: Erster = %s, Letzter = %s", resLong[0], resLong[9])
	}
}

func TestZaehleWortHaeufigkeit(t *testing.T) {
	text := "Go ist toll und Go ist extrem schnell"
	counts := ZaehleWortHaeufigkeit(text)

	if counts["go"] != 2 {
		t.Errorf("ZaehleWortHaeufigkeit('go') = %d; erwartet 2", counts["go"])
	}
	if counts["ist"] != 2 {
		t.Errorf("ZaehleWortHaeufigkeit('ist') = %d; erwartet 2", counts["ist"])
	}
	if counts["schnell"] != 1 {
		t.Errorf("ZaehleWortHaeufigkeit('schnell') = %d; erwartet 1", counts["schnell"])
	}
}

func TestSichereBenutzerAbfrageUndLoeschen(t *testing.T) {
	users := map[string]int{
		"alice": 28,
		"bob":   34,
	}

	alterAlice, okAlice := SichereBenutzerAbfrage(users, "alice")
	if !okAlice || alterAlice != 28 {
		t.Errorf("SichereBenutzerAbfrage('alice') = (%d, %t); erwartet (28, true)", alterAlice, okAlice)
	}

	_, okCharlie := SichereBenutzerAbfrage(users, "charlie")
	if okCharlie {
		t.Errorf("SichereBenutzerAbfrage('charlie') sollte false liefern")
	}

	LoescheBenutzer(users, "bob")
	_, okBobNachLoeschen := SichereBenutzerAbfrage(users, "bob")
	if okBobNachLoeschen {
		t.Errorf("LoescheBenutzer('bob') hat Bob nicht entfernt")
	}
}
