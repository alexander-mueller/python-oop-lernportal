using System;
using System.Collections.Generic;

namespace CSharpKurs.Modul12;

// ============================================================================
// 🎯 TODO 1: Domain-Exceptions
// Erstelle die Exception-Hierarchie für das Bankensystem:
// - BankDomainException (erbt von Exception) mit Property 'string ErrorCode'
// - AccountNotFoundException (erbt von BankDomainException) mit Property 'Guid AccountId'
// - InsufficientFundsException (erbt von BankDomainException) mit 'Guid AccountId', 'decimal RequestedAmount', 'decimal CurrentBalance'
// ============================================================================
public class BankDomainException : Exception
{
    public string ErrorCode { get; }

    public BankDomainException(string message, string errorCode = "BANK_ERROR") 
        : base(message)
    {
        ErrorCode = errorCode;
    }
}

public class AccountNotFoundException : BankDomainException
{
    public Guid AccountId { get; }

    public AccountNotFoundException(Guid accountId)
        : base($"Konto mit ID '{accountId}' wurde nicht gefunden.", "ACCOUNT_NOT_FOUND")
    {
        // TODO 1a: Setze AccountId
        throw new NotImplementedException();
    }
}

public class InsufficientFundsException : BankDomainException
{
    public Guid AccountId { get; }
    public decimal RequestedAmount { get; }
    public decimal CurrentBalance { get; }

    public InsufficientFundsException(Guid accountId, decimal requestedAmount, decimal currentBalance)
        : base($"Konto '{accountId}' verfügt nicht über ausreichend Guthaben. Verfügbar: {currentBalance}, Angefordert: {requestedAmount}", "INSUFFICIENT_FUNDS")
    {
        // TODO 1b: Setze AccountId, RequestedAmount und CurrentBalance
        throw new NotImplementedException();
    }
}

// ============================================================================
// 🎯 TODO 2: IDisposable Resource Management
// ============================================================================
public class AuditTransactionScope : IDisposable
{
    private bool _disposed = false;
    public string TransactionId { get; }
    public List<string> LogEntries { get; } = new();
    public bool IsDisposed => _disposed;

    public AuditTransactionScope(string transactionId)
    {
        TransactionId = transactionId;
        LogEntries.Add($"Scope gestartet für TX {transactionId}");
    }

    public void Record(string message)
    {
        // TODO 2a: Wenn _disposed == true ist, wirf eine ObjectDisposedException(nameof(AuditTransactionScope)).
        // Andernfalls füge die Nachricht zur LogEntries-Liste hinzu.
        throw new NotImplementedException();
    }

    public void Dispose()
    {
        // TODO 2b: Wenn noch nicht disposed, füge "Scope beendet für TX {TransactionId}" zu LogEntries hinzu
        // und setze _disposed auf true.
        throw new NotImplementedException();
    }
}

// ============================================================================
// 🎯 TODO 3: BankAccount Entität
// ============================================================================
public class BankAccount
{
    public Guid Id { get; }
    public string Owner { get; }
    public decimal Balance { get; private set; }

    public BankAccount(Guid id, string owner, decimal initialBalance = 0m)
    {
        if (initialBalance < 0)
            throw new ArgumentOutOfRangeException(nameof(initialBalance), "Startguthaben darf nicht negativ sein.");

        Id = id;
        Owner = owner;
        Balance = initialBalance;
    }

    public void Deposit(decimal amount)
    {
        // TODO 3a: Wenn amount <= 0, wirf eine ArgumentOutOfRangeException.
        // Andernfalls erhöhe Balance um amount.
        throw new NotImplementedException();
    }

    public void Withdraw(decimal amount)
    {
        // TODO 3b: Wenn amount <= 0, wirf ArgumentOutOfRangeException.
        // Wenn amount > Balance, wirf eine InsufficientFundsException(Id, amount, Balance).
        // Andernfalls ziehe amount von Balance ab.
        throw new NotImplementedException();
    }
}

// ============================================================================
// 🎯 TODO 4: BankTransferService
// ============================================================================
public class BankTransferService
{
    private readonly Dictionary<Guid, BankAccount> _accounts = new();

    public void RegisterAccount(BankAccount account)
    {
        ArgumentNullException.ThrowIfNull(account);
        _accounts[account.Id] = account;
    }

    public void TransferFunds(Guid fromId, Guid toId, decimal amount, out List<string> auditLogs)
    {
        // TODO 4:
        // 1. Initialisiere using var scope = new AuditTransactionScope($"TX-{Guid.NewGuid():N}");
        // 2. Finde Quell- und Zielkonto. Wenn nicht vorhanden, wirf AccountNotFoundException.
        // 3. Buche amount von fromAccount ab (Withdraw) und buche auf toAccount auf (Deposit).
        // 4. Protokolliere erfolgreiche Buchung mit scope.Record($"Überwiesen: {amount} von {fromId} an {toId}");
        // 5. Gib scope.LogEntries über den out-Parameter auditLogs zurück.
        throw new NotImplementedException();
    }
}
