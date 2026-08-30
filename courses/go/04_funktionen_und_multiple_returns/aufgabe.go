package main

import (
	"errors"
	"fmt"
)

// 🎯 TEILZIEL 1 (TODO 1): Implementiere die sichere Division mit Multiple Returns
// Falls b == 0.0 ist, gib (0.0, errors.New("Division durch Null nicht erlaubt")) zurück.
// Andernfalls: (a / b, nil).
func SichereDivision(a, b float64) (float64, error) {
	// TODO: Division durchführen und Error prüfen
	return 0.0, nil
}

// 🎯 TEILZIEL 2 (TODO 2): Berechne statistische Kennzahlen mit benannten Rückgabewerten
// Falls werte leer ist (len == 0): gib (0, 0, 0, 0.0) zurück.
// min: Kleinster Wert
// max: Größter Wert
// summe: Summe aller Werte
// schnitt: Arithmetisches Mittel als float64
func BerechneStatistik(werte []int) (min int, max int, summe int, schnitt float64) {
	// TODO: Fülle die benannten Rückgabewerte
	return
}

// 🎯 TEILZIEL 3 (TODO 3): Variadisches Summieren mit Präfix
// Berechne die Summe aller übergebenen 'zahlen' und formatiere das Ergebnis als:
// "[prefix]: [summe] (Anzahl: [anzahl])"
// Beispiel: VariadischesSummieren("Umsatz", 10, 20, 30) -> "Umsatz: 60 (Anzahl: 3)"
// Beispiel: VariadischesSummieren("Leer") -> "Leer: 0 (Anzahl: 0)"
func VariadischesSummieren(prefix string, zahlen ...int) string {
	// TODO: Iteriere über zahlen und nutze fmt.Sprintf
	return ""
}

// 🎯 TEILZIEL 4 (TODO 4): Erstelle eine Closure-Generatorfunktion für einen Zähler
// ErstelleZaehler gibt eine Funktion zurück. Jeder Aufruf dieser inneren Funktion
// erhöht den Zählerstand um 1 und gibt den neuen Wert zurück.
// Der erste Aufruf nach ErstelleZaehler(10) soll 11 liefern.
func ErstelleZaehler(start int) func() int {
	// TODO: Innere Funktion zurückgeben, die die äußere Variable inkrementiert
	return nil
}

func main() {
	res, err := SichereDivision(10, 2)
	fmt.Printf("10 / 2 = %.2f (Err: %v)\n", res, err)

	min, max, sum, avg := BerechneStatistik([]int{5, 10, 15, 20})
	fmt.Printf("Stats: Min=%d, Max=%d, Sum=%d, Avg=%.2f\n", min, max, sum, avg)

	fmt.Println(VariadischesSummieren("Test", 1, 2, 3, 4))

	counter := ErstelleZaehler(100)
	fmt.Println("Counter:", counter(), counter(), counter())
}
