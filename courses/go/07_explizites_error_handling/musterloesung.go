package main

import (
	"errors"
	"fmt"
)

var (
	ErrInvalidAmount     = errors.New("ungültiger betrag: muss positiv sein")
	ErrInsufficientFunds = errors.New("nicht genügend guthaben verfügbar")
)

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

func (b *BankAccount) Deposit(amount float64) error {
	if amount <= 0 {
		return ErrInvalidAmount
	}
	b.Balance += amount
	return nil
}

func (b *BankAccount) Withdraw(amount float64) error {
	if amount <= 0 {
		return ErrInvalidAmount
	}
	if amount > b.Balance {
		return ErrInsufficientFunds
	}
	b.Balance -= amount
	return nil
}

type APIError struct {
	StatusCode int
	Endpoint   string
	Details    string
}

func (e *APIError) Error() string {
	return fmt.Sprintf("HTTP %d Fehler bei %s: %s", e.StatusCode, e.Endpoint, e.Details)
}

func ExecuteRequest(endpoint string, token string) (string, error) {
	if token != "valid-token-123" {
		return "", &APIError{
			StatusCode: 401,
			Endpoint:   endpoint,
			Details:    "ungültiges token",
		}
	}

	if endpoint == "/error" {
		dbErr := errors.New("datenbank timeout")
		return "", fmt.Errorf("interner fehler: %w", dbErr)
	}

	return "200 OK: Daten für " + endpoint, nil
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
