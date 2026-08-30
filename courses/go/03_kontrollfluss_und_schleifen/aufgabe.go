package main

import (
	"fmt"
)

// 🎯 TEILZIEL 1 (TODO 1): Berechne die Summe aller Ganzzahlen von 'start' bis inklusive 'ende'
// Nutze eine klassische for-Schleife (for i := start; i <= ende; i++).
// Falls start > ende, soll 0 zurückgegeben werden.
// Beispiel: SummiereBereich(1, 5) -> 1 + 2 + 3 + 4 + 5 = 15
func SummiereBereich(start, ende int) int {
	// TODO: Klassische for-Schleife implementieren
	return 0
}

// 🎯 TEILZIEL 2 (TODO 2): Berechne die Fakultät n! (n * (n-1) * ... * 1)
// Verwende eine While-artige for-Schleife (for n > 1).
// Validierung: Für n < 0 soll (0, false) zurückgegeben werden.
// Für n >= 0 soll das Ergebnis und true zurückgegeben werden (0! = 1).
// Beispiel: BerechneFakultaet(5) -> (120, true)
func BerechneFakultaet(n int) (int, bool) {
	// TODO: While-artige for-Schleife mit Validierung
	return 0, false
}

// 🎯 TEILZIEL 3 (TODO 3): Finde das Maximum und Minimum in einem Slice mit for ... range
// Falls das Slice leer ist (len == 0), soll (0, 0, false) zurückgegeben werden.
// Sonst: (max, min, true).
// Beispiel: FindeMaxUndMin([]int{5, 2, 9, 1, 7}) -> (9, 1, true)
func FindeMaxUndMin(werte []int) (int, int, bool) {
	// TODO: Iteriere mit range über die Werte
	return 0, 0, false
}

// 🎯 TEILZIEL 4 (TODO 4): Kategorisiere den HTTP-Statuscode mit einem switch-Statement
// 200..299 -> "SUCCESS"
// 300..399 -> "REDIRECT"
// 400..499 -> "CLIENT_ERROR"
// 500..599 -> "SERVER_ERROR"
// Sonst -> "INVALID_STATUS"
func HTTPStatusKategorie(statusCode int) string {
	// TODO: Verwende ein switch-Statement mit Wertebereichen
	return ""
}

func main() {
	fmt.Println("Summe 1..5:", SummiereBereich(1, 5))
	fak, ok := BerechneFakultaet(5)
	fmt.Printf("5! = %d (Gültig: %t)\n", fak, ok)

	max, min, found := FindeMaxUndMin([]int{10, 4, 88, 2, 19})
	fmt.Printf("Max: %d, Min: %d (Found: %t)\n", max, min, found)

	fmt.Println("Status 404:", HTTPStatusKategorie(404))
}
