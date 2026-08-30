package main

import (
	"errors"
	"testing"
)

func TestBankAccountDepositErrors(t *testing.T) {
	acc := NewBankAccount("Tester", 50.0)

	errValid := acc.Deposit(25.0)
	if errValid != nil || acc.Balance != 75.0 {
		t.Errorf("Deposit(25) = %v, Balance = %.2f; erwartet nil, 75.00", errValid, acc.Balance)
	}

	errZero := acc.Deposit(0.0)
	if !errors.Is(errZero, ErrInvalidAmount) {
		t.Errorf("Deposit(0) = %v; erwartet ErrInvalidAmount", errZero)
	}

	errNeg := acc.Deposit(-10.0)
	if !errors.Is(errNeg, ErrInvalidAmount) {
		t.Errorf("Deposit(-10) = %v; erwartet ErrInvalidAmount", errNeg)
	}
}

func TestBankAccountWithdrawErrors(t *testing.T) {
	acc := NewBankAccount("Tester", 100.0)

	errValid := acc.Withdraw(40.0)
	if errValid != nil || acc.Balance != 60.0 {
		t.Errorf("Withdraw(40) = %v, Balance = %.2f; erwartet nil, 60.00", errValid, acc.Balance)
	}

	errOver := acc.Withdraw(100.0)
	if !errors.Is(errOver, ErrInsufficientFunds) {
		t.Errorf("Withdraw(100) bei Stand 60 = %v; erwartet ErrInsufficientFunds", errOver)
	}

	errNeg := acc.Withdraw(-5.0)
	if !errors.Is(errNeg, ErrInvalidAmount) {
		t.Errorf("Withdraw(-5) = %v; erwartet ErrInvalidAmount", errNeg)
	}
}

func TestCustomAPIError(t *testing.T) {
	apiErr := &APIError{
		StatusCode: 404,
		Endpoint:   "/api/v1/resource",
		Details:    "nicht gefunden",
	}

	expected := "HTTP 404 Fehler bei /api/v1/resource: nicht gefunden"
	if apiErr.Error() != expected {
		t.Errorf("APIError.Error() = %q; erwartet %q", apiErr.Error(), expected)
	}
}

func TestExecuteRequestWrapping(t *testing.T) {
	// 1. Ungültiges Token
	_, errAuth := ExecuteRequest("/data", "bad-token")
	if errAuth == nil {
		t.Fatalf("ExecuteRequest mit falschem Token sollte Fehler liefern")
	}
	var apiErr *APIError
	if !errors.As(errAuth, &apiErr) {
		t.Errorf("Fehler sollte Typ *APIError sein, ist aber %T", errAuth)
	} else if apiErr.StatusCode != 401 {
		t.Errorf("APIError StatusCode = %d; erwartet 401", apiErr.StatusCode)
	}

	// 2. Datenbank Timeout Error
	_, errTimeout := ExecuteRequest("/error", "valid-token-123")
	if errTimeout == nil {
		t.Fatalf("ExecuteRequest('/error') sollte Fehler liefern")
	}
	if errTimeout.Error() != "interner fehler: datenbank timeout" {
		t.Errorf("Fehlermeldung = %q; erwartet 'interner fehler: datenbank timeout'", errTimeout.Error())
	}

	// 3. Erfolgreicher Request
	res, errSuccess := ExecuteRequest("/users", "valid-token-123")
	if errSuccess != nil || res != "200 OK: Daten für /users" {
		t.Errorf("ExecuteRequest() = (%q, %v); erwartet ('200 OK: Daten für /users', nil)", res, errSuccess)
	}
}
