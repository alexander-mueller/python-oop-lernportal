package main

import (
	"errors"
	"fmt"
	"strings"
	"unicode"
)

// ============================================================================
// 💡 GO 15: MUSTERLÖSUNG (Testing & Benchmarks)
// ============================================================================

// Slugify formatiert einen beliebigen String in einen SEO-/URL-konformen Slug.
func Slugify(input string) (string, error) {
	trimmed := strings.TrimSpace(input)
	if trimmed == "" {
		return "", errors.New("input string cannot be empty")
	}

	lower := strings.ToLower(trimmed)
	var builder strings.Builder

	for _, r := range lower {
		if unicode.IsLetter(r) || unicode.IsDigit(r) {
			builder.WriteRune(r)
		} else {
			builder.WriteRune(' ')
		}
	}

	fields := strings.Fields(builder.String())
	slug := strings.Join(fields, "-")
	slug = strings.Trim(slug, "-")

	return slug, nil
}

// ValidateEmail prüft Grundkriterien einer Email-Adresse.
func ValidateEmail(email string) bool {
	parts := strings.Split(email, "@")
	if len(parts) != 2 {
		return false
	}

	user := parts[0]
	domain := parts[1]

	if user == "" || domain == "" {
		return false
	}

	if strings.HasPrefix(domain, ".") || strings.HasSuffix(domain, ".") {
		return false
	}

	return strings.Contains(domain, ".")
}

// FastStringJoin verbindet Strings speichereffizient ohne unnötige Zwischenallokationen.
func FastStringJoin(parts []string, sep string) string {
	if len(parts) == 0 {
		return ""
	}
	if len(parts) == 1 {
		return parts[0]
	}

	totalLen := 0
	for _, p := range parts {
		totalLen += len(p)
	}
	totalLen += len(sep) * (len(parts) - 1)

	var b strings.Builder
	b.Grow(totalLen)

	b.WriteString(parts[0])
	for _, p := range parts[1:] {
		b.WriteString(sep)
		b.WriteString(p)
	}

	return b.String()
}

func main() {
	fmt.Println("=== Go 15: Musterlösung ===")

	slug, err := Slugify("Hello World & Cloud 2026!")
	if err == nil {
		fmt.Printf("Slugify-Ergebnis: %s\n", slug)
	}

	emails := []string{"dev@example.com", "invalid-email", "user@sub.domain.org", "@no-user.com"}
	for _, e := range emails {
		fmt.Printf("  • %-20s => Valide: %t\n", e, ValidateEmail(e))
	}
}
