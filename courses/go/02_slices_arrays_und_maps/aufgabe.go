package main

import (
	"fmt"
	"strings"
)

// 🎯 TEILZIEL 1 (TODO 1): Filtere alle geraden Zahlen aus dem Eingabe-Slice heraus
// Nutze make([]int, 0, len(zahlen)) zur Vorallokation und append() zum Hinzufügen.
// Beispiel: [1, 2, 3, 4, 5, 6] -> [2, 4, 6]
func FiltereGeradeZahlen(zahlen []int) []int {
	// TODO: Initialisiere ein Ergebnis-Slice und füge gerade Zahlen hinzu
	return nil
}

// 🎯 TEILZIEL 2 (TODO 2): Hänge neue Log-Einträge an ein bestehendes Slice an
// Falls 'logs' mehr als 10 Einträge hat, sollen nur die letzten 10 Einträge zurückgegeben werden (Ringbuffer-Slicing).
// Beispiel: logs mit 9 Einträgen + 3 neue = 12 Einträge -> Rückgabe der letzten 10 Einträge (Index 2 bis 12).
func ErweitereProtokolle(logs []string, neueEintraege ...string) []string {
	// TODO: Hänge neueEintraege mit append an und schneide auf max 10 Einträge zu
	return nil
}

// 🎯 TEILZIEL 3 (TODO 3): Zähle die Häufigkeit jedes Worts im übergebenen Text
// Verwende strings.Fields() zum Zerlegen des Textes in Wörter.
// Wandle alle Wörter vorher mit strings.ToLower() in Kleinbuchstaben um.
// Beispiel: "Go ist schnell und Go ist einfach" -> {"go": 2, "ist": 2, "schnell": 1, "und": 1, "einfach": 1}
func ZaehleWortHaeufigkeit(text string) map[string]int {
	// TODO: Map anlegen und Worthäufigkeiten inkrementieren
	return nil
}

// 🎯 TEILZIEL 4 (TODO 4): Sichere Benutzerabfrage & Löschen
// 1. SichereBenutzerAbfrage: Gibt das Alter des Benutzers und true zurück, wenn er in der Map existiert, sonst (0, false).
// 2. LoescheBenutzer: Löscht den Benutzer aus der Map (falls vorhanden).
func SichereBenutzerAbfrage(users map[string]int, username string) (int, bool) {
	// TODO: Verwende das Comma-OK Idiom
	return 0, false
}

func LoescheBenutzer(users map[string]int, username string) {
	// TODO: Lösche den Eintrag mit delete()
}

func main() {
	evens := FiltereGeradeZahlen([]int{1, 2, 3, 4, 5, 6, 7, 8})
	fmt.Println("Gerade Zahlen:", evens)

	words := ZaehleWortHaeufigkeit("Go ist super und Go macht Spass")
	fmt.Println("Häufigkeiten:", words)
}
