package main

import (
	"fmt"
	"strings"
)

func FiltereGeradeZahlen(zahlen []int) []int {
	ergebnis := make([]int, 0, len(zahlen))
	for _, z := range zahlen {
		if z%2 == 0 {
			ergebnis = append(ergebnis, z)
		}
	}
	return ergebnis
}

func ErweitereProtokolle(logs []string, neueEintraege ...string) []string {
	gesamt := append(logs, neueEintraege...)
	if len(gesamt) > 10 {
		return gesamt[len(gesamt)-10:]
	}
	return gesamt
}

func ZaehleWortHaeufigkeit(text string) map[string]int {
	haeufigkeit := make(map[string]int)
	woerter := strings.Fields(text)
	for _, w := range woerter {
		bereinigt := strings.ToLower(w)
		haeufigkeit[bereinigt]++
	}
	return haeufigkeit
}

func SichereBenutzerAbfrage(users map[string]int, username string) (int, bool) {
	alter, existiert := users[username]
	return alter, existiert
}

func LoescheBenutzer(users map[string]int, username string) {
	delete(users, username)
}

func main() {
	evens := FiltereGeradeZahlen([]int{1, 2, 3, 4, 5, 6, 7, 8})
	fmt.Println("Gerade Zahlen:", evens)

	words := ZaehleWortHaeufigkeit("Go ist super und Go macht Spass")
	fmt.Println("Häufigkeiten:", words)
}
