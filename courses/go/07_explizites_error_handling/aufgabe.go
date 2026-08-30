package main

import (
	"errors"
	"fmt"
)

// 🎯 TEILZIEL 1 (TODO 1): Definiere globale Sentinel Errors mit errors.New()
// - ErrInvalidAmount = "ungültiger betrag: muss positiv sein"
// - ErrInsufficientFunds = "nicht genügend guthaben verfügbar"
var (
	ErrInvalidAmount     = errors.New("ungültiger betrag: muss positiv sein")
	ErrInsufficientFunds = errors.New("nicht genügend guthaben verfügbar")
)

// 🎯 TEILZIEL 2 (TODO 2): BankAccount Struct mit Methoden
type BankAccount struct {
	Owner   string
	Balance float64
}

func NewBankAccount(owner string, initialBalance float64) *BankAccount {
	return &BankAccount{
		Owner:   owner,
		Balance: initialBalance,
	}
}

// Deposit: Zahlt einen Betrag ein.
// Falls amount <= 0: gib ErrInvalidAmount zurück.
// Andernfalls: Balance erhöhen und nil zurückgeben.
func (b *BankAccount) Deposit(amount float64) error {
	// TODO: Validierung und Einzahlung
	return nil
}

// Withdraw: Hebt einen Betrag ab.
// Falls amount <= 0: gib ErrInvalidAmount zurück.
// Falls amount > b.Balance: gib ErrInsufficientFunds zurück.
// Andernfalls: Balance verringern und nil zurückgeben.
func (b *BankAccount) Withdraw(amount float64) error {
	// TODO: Validierung und Auszahlung
	return nil
}

// 🎯 TEILZIEL 3 (TODO 3): Custom Struct APIError
// Felder:
// - StatusCode (int)
// - Endpoint   (string)
// - Details    (string)
type APIError struct {
	StatusCode int
	Endpoint   string
	Details    string
}

// Implementiere die Error() string Methode für *APIError
// Format: "HTTP [StatusCode] Fehler bei [Endpoint]: [Details]"
// Beispiel: "HTTP 401 Fehler bei /api/v1/auth: ungültiges token"
func (e *APIError) Error() string {
	// TODO: String mit fmt.Sprintf formatieren
	return ""
}

// 🎯 TEILZIEL 4 (TODO 4): ExecuteRequest mit Error Wrapping & Custom Errors
// Logik:
// 1. Wenn token != "valid-token-123":
//    Gib ein APIError zurück: StatusCode = 401, Endpoint = endpoint, Details = "ungültiges token"
// 2. Wenn endpoint == "/error":
//    Gib einen gewrappten Fehler mit fmt.Errorf("interner fehler: %w", errors.New("datenbank timeout")) zurück.
// 3. Sonst: Gib ("200 OK: Daten für " + endpoint, nil) zurück.
func ExecuteRequest(endpoint string, token string) (string, error) {
	// TODO: Token prüfen, Fehler mit %w wrappen oder Erfolgsstring zurückgeben
	return "", nil
}

func main() {
	acc := NewBankAccount("Alice", 100.0)
	if err := acc.Deposit(50); err != nil {
		fmt.Println("Einzahlungsfehler:", err)
	}
	if err := acc.Withdraw(200); err != nil {
		fmt.Println("Abhebungsfehler:", err)
	}
	fmt.Printf("Konto %s Stand: %.2f EUR\n", acc.Owner, acc.Balance)

	res, err := ExecuteRequest("/api/v1/users", "valid-token-123")
	fmt.Printf("API Response: %s (Err: %v)\n", res, err)
}
