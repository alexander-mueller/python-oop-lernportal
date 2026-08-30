package main

import (
	"fmt"
)

func SummiereBereich(start, ende int) int {
	if start > ende {
		return 0
	}
	summe := 0
	for i := start; i <= ende; i++ {
		summe += i
	}
	return summe
}

func BerechneFakultaet(n int) (int, bool) {
	if n < 0 {
		return 0, false
	}
	if n == 0 {
		return 1, true
	}
	ergebnis := 1
	aktuell := n
	for aktuell > 1 {
		ergebnis *= aktuell
		aktuell--
	}
	return ergebnis, true
}

func FindeMaxUndMin(werte []int) (int, int, bool) {
	if len(werte) == 0 {
		return 0, 0, false
	}
	max := werte[0]
	min := werte[0]
	for _, w := range werte {
		if w > max {
			max = w
		}
		if w < min {
			min = w
		}
	}
	return max, min, true
}

func HTTPStatusKategorie(statusCode int) string {
	switch {
	case statusCode >= 200 && statusCode <= 299:
		return "SUCCESS"
	case statusCode >= 300 && statusCode <= 399:
		return "REDIRECT"
	case statusCode >= 400 && statusCode <= 499:
		return "CLIENT_ERROR"
	case statusCode >= 500 && statusCode <= 599:
		return "SERVER_ERROR"
	default:
		return "INVALID_STATUS"
	}
}

func main() {
	fmt.Println("Summe 1..5:", SummiereBereich(1, 5))
	fak, ok := BerechneFakultaet(5)
	fmt.Printf("5! = %d (Gültig: %t)\n", fak, ok)

	max, min, found := FindeMaxUndMin([]int{10, 4, 88, 2, 19})
	fmt.Printf("Max: %d, Min: %d (Found: %t)\n", max, min, found)

	fmt.Println("Status 404:", HTTPStatusKategorie(404))
}
