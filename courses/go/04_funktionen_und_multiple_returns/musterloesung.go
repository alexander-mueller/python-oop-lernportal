package main

import (
	"errors"
	"fmt"
)

func SichereDivision(a, b float64) (float64, error) {
	if b == 0 {
		return 0, errors.New("Division durch Null nicht erlaubt")
	}
	return a / b, nil
}

func BerechneStatistik(werte []int) (min int, max int, summe int, schnitt float64) {
	if len(werte) == 0 {
		return 0, 0, 0, 0.0
	}

	min = werte[0]
	max = werte[0]
	summe = 0

	for _, w := range werte {
		if w < min {
			min = w
		}
		if w > max {
			max = w
		}
		summe += w
	}

	schnitt = float64(summe) / float64(len(werte))
	return min, max, summe, schnitt
}

func VariadischesSummieren(prefix string, zahlen ...int) string {
	summe := 0
	for _, z := range zahlen {
		summe += z
	}
	return fmt.Sprintf("%s: %d (Anzahl: %d)", prefix, summe, len(zahlen))
}

func ErstelleZaehler(start int) func() int {
	zaehler := start
	return func() int {
		zaehler++
		return zaehler
	}
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
