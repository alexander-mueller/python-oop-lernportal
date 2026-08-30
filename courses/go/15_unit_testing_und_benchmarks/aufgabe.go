package main

import (
	"errors"
	"fmt"
	"strings"
	"unicode"
)

// ============================================================================
// 🚀 GO 15: UNIT TESTING, TABLE-DRIVEN TESTS & BENCHMARKS
// ============================================================================

// 🎯 TODO 1: Implementiere 'Slugify'
// Parameter:
// - input: Ausgangs-String (z.B. "Go 1.22 & Cloud Architecture!")
// Rückgabe:
// - Formatierter Slug (z.B. "go-1-22-cloud-architecture")
// - Fehler 'errors.New("input string cannot be empty")', falls input nach TrimSpace leer ist.
//
// Anforderungen:
// 1. Prüfe auf leeren String (nach strings.TrimSpace).
// 2. Wandle in Kleinbuchstaben um (strings.ToLower).
// 3. Ersetze alle Zeichen, die weder Buchstabe noch Ziffer sind (unicode.IsLetter / unicode.IsDigit), durch ein Leerzeichen oder direkt Bindestrich.
// 4. Teile den String an Leerzeichen/Trennzeichen auf (strings.Fields) und verbinde ihn mit "-".
// 5. Entferne führende und nachfolgende Bindestriche mit strings.Trim(slug, "-").
func Slugify(input string) (string, error) {
	// TODO: Slugify-Logik umsetzen
	return "", nil
}

// 🎯 TODO 2: Implementiere 'ValidateEmail'
// Parameter:
// - email: Zu prüfende E-Mail-Adresse
// Rückgabe:
// - true bei gültiger Struktur, sonst false
//
// Anforderungen:
// 1. Teile den String an '@' auf (parts := strings.Split(email, "@")).
// 2. Es müssen exakt 2 Teile sein (len(parts) == 2), beide dürfen nicht leer sein.
// 3. Der Domain-Teil (parts[1]) muss mindestens einen '.' enthalten, der weder am Anfang noch am Ende steht.
func ValidateEmail(email string) bool {
	// TODO: E-Mail-Struktur validieren
	return false
}

// 🎯 TODO 3: Implementiere 'FastStringJoin'
// Verbindet Elemente speichereffizient mit strings.Builder.
// Parameter:
// - parts: Slice von Strings
// - sep: Trennzeichen
// Rückgabe:
// - Zusammengesetzter String
func FastStringJoin(parts []string, sep string) string {
	// TODO: strings.Builder nutzen
	return ""
}

// 🎯 TODO 4: Struct für Table-Driven Testfall
type TestCase[I any, O any] struct {
	Name    string
	Input   I
	Want    O
	WantErr bool
}

func main() {
	fmt.Println("=== Go 15: Unit Testing & Benchmarks ===")

	slug, err := Slugify("Hello World & Cloud 2026!")
	if err == nil {
		fmt.Printf("Slugify-Ergebnis: %s\n", slug)
	}

	emails := []string{"dev@example.com", "invalid-email", "user@sub.domain.org", "@no-user.com"}
	for _, e := range emails {
		fmt.Printf("  • %-20s => Valide: %t\n", e, ValidateEmail(e))
	}
}
