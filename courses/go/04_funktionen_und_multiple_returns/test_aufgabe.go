package main

import (
	"testing"
)

func TestSichereDivision(t *testing.T) {
	val, err := SichereDivision(10, 2)
	if err != nil || val != 5.0 {
		t.Errorf("SichereDivision(10, 2) = (%.2f, %v); erwartet (5.0, nil)", val, err)
	}

	_, errZero := SichereDivision(5, 0)
	if errZero == nil {
		t.Errorf("SichereDivision(5, 0) sollte einen Error zurückgeben")
	}
}

func TestBerechneStatistik(t *testing.T) {
	min, max, sum, avg := BerechneStatistik([]int{10, 20, 30, 40})
	if min != 10 || max != 40 || sum != 100 || avg != 25.0 {
		t.Errorf("BerechneStatistik([10, 20, 30, 40]) = (%d, %d, %d, %.2f); erwartet (10, 40, 100, 25.0)", min, max, sum, avg)
	}

	minE, maxE, sumE, avgE := BerechneStatistik([]int{})
	if minE != 0 || maxE != 0 || sumE != 0 || avgE != 0.0 {
		t.Errorf("BerechneStatistik([]) sollte (0,0,0,0) liefern, lieferte (%d, %d, %d, %.2f)", minE, maxE, sumE, avgE)
	}
}

func TestVariadischesSummieren(t *testing.T) {
	s1 := VariadischesSummieren("Umsatz", 10, 20, 30)
	expected1 := "Umsatz: 60 (Anzahl: 3)"
	if s1 != expected1 {
		t.Errorf("VariadischesSummieren() = %q; erwartet %q", s1, expected1)
	}

	s2 := VariadischesSummieren("Leer")
	expected2 := "Leer: 0 (Anzahl: 0)"
	if s2 != expected2 {
		t.Errorf("VariadischesSummieren() = %q; erwartet %q", s2, expected2)
	}
}

func TestErstelleZaehler(t *testing.T) {
	c1 := ErstelleZaehler(0)
	if c1 == nil {
		t.Fatalf("ErstelleZaehler lieferte nil")
	}

	if v := c1(); v != 1 {
		t.Errorf("Erster Aufruf c1() = %d; erwartet 1", v)
	}
	if v := c1(); v != 2 {
		t.Errorf("Zweiter Aufruf c1() = %d; erwartet 2", v)
	}

	c2 := ErstelleZaehler(50)
	if v := c2(); v != 51 {
		t.Errorf("Aufruf c2() = %d; erwartet 51", v)
	}
	// c1 muss unabhängig sein
	if v := c1(); v != 3 {
		t.Errorf("Dritter Aufruf c1() = %d; erwartet 3", v)
	}
}
