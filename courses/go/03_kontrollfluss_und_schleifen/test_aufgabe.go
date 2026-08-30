package main

import (
	"testing"
)

func TestSummiereBereich(t *testing.T) {
	if res := SummiereBereich(1, 5); res != 15 {
		t.Errorf("SummiereBereich(1, 5) = %d; erwartet 15", res)
	}
	if res := SummiereBereich(10, 10); res != 10 {
		t.Errorf("SummiereBereich(10, 10) = %d; erwartet 10", res)
	}
	if res := SummiereBereich(5, 2); res != 0 {
		t.Errorf("SummiereBereich(5, 2) = %d; erwartet 0", res)
	}
}

func TestBerechneFakultaet(t *testing.T) {
	cases := []struct {
		n        int
		expected int
		valid    bool
	}{
		{0, 1, true},
		{1, 1, true},
		{5, 120, true},
		{6, 720, true},
		{-3, 0, false},
	}

	for _, c := range cases {
		val, ok := BerechneFakultaet(c.n)
		if ok != c.valid || (c.valid && val != c.expected) {
			t.Errorf("BerechneFakultaet(%d) = (%d, %t); erwartet (%d, %t)", c.n, val, ok, c.expected, c.valid)
		}
	}
}

func TestFindeMaxUndMin(t *testing.T) {
	max, min, ok := FindeMaxUndMin([]int{12, 5, 89, 3, 44})
	if !ok || max != 89 || min != 3 {
		t.Errorf("FindeMaxUndMin([12, 5, 89, 3, 44]) = (%d, %d, %t); erwartet (89, 3, true)", max, min, ok)
	}

	maxSingle, minSingle, okSingle := FindeMaxUndMin([]int{42})
	if !okSingle || maxSingle != 42 || minSingle != 42 {
		t.Errorf("FindeMaxUndMin([42]) = (%d, %d, %t); erwartet (42, 42, true)", maxSingle, minSingle, okSingle)
	}

	_, _, okEmpty := FindeMaxUndMin([]int{})
	if okEmpty {
		t.Errorf("FindeMaxUndMin([]) sollte false zurückgeben")
	}
}

func TestHTTPStatusKategorie(t *testing.T) {
	tests := []struct {
		code     int
		expected string
	}{
		{200, "SUCCESS"},
		{204, "SUCCESS"},
		{301, "REDIRECT"},
		{404, "CLIENT_ERROR"},
		{403, "CLIENT_ERROR"},
		{500, "SERVER_ERROR"},
		{503, "SERVER_ERROR"},
		{100, "INVALID_STATUS"},
		{999, "INVALID_STATUS"},
	}

	for _, tc := range tests {
		res := HTTPStatusKategorie(tc.code)
		if res != tc.expected {
			t.Errorf("HTTPStatusKategorie(%d) = %q; erwartet %q", tc.code, res, tc.expected)
		}
	}
}
