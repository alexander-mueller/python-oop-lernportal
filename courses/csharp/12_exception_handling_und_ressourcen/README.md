# C# 12: Exception Handling & Ressourcenverwaltung (IDisposable) 🛡️

Willkommen zu **Modul 12**! In diesem Kapitel lernst du professionelle Fehlerbehandlung und deterministisches Ressourcenmanagement nach Enterprise-.NET-Standards.

---

## 💡 1. Das Wichtigste in Kürze

### Eigene Domain Exceptions
Ausnahmen sollten fachliche Fehler ausdrücken und dem Aufrufer relevante Kontextdaten bereitstellen:
```csharp
public class InsufficientFundsException : BankDomainException
{
    public Guid AccountId { get; }
    public decimal RequestedAmount { get; }
    public decimal CurrentBalance { get; }

    public InsufficientFundsException(Guid accountId, decimal requestedAmount, decimal currentBalance)
        : base($"Konto {accountId} hat unzureichende Deckung ({currentBalance:C}). Gefordert: {requestedAmount:C}")
    {
        AccountId = accountId;
        RequestedAmount = requestedAmount;
        CurrentBalance = currentBalance;
    }
}
```

### Exception Filters (`when`)
Mit `when` entscheidest du im `catch`-Block anhand von Bedingungen, ob die Exception gefangen werden soll:
```csharp
catch (InsufficientFundsException ex) when (ex.RequestedAmount > 10_000m)
{
    // Greift nur bei Großtransaktionen
}
```

### Das `IDisposable` Muster & `using` Declarations
Seit C# 8 reicht die schlanke Syntax `using var resource = ...`, die das Objekt am Ende des aktuellen Gültigkeitsbereichs automatisch entsorgt:
```csharp
{
    using var scope = new AuditTransactionScope("TX-1234");
    // scope.Dispose() wird beim Verlassen dieses Blocks garantiert aufgerufen!
}
```

---

## 🎯 Teilziele in `Aufgabe.cs`

1. **TODO 1: Exception-Klassenhierarchie**  
   Erstelle `BankDomainException`, `AccountNotFoundException` und `InsufficientFundsException`.

2. **TODO 2: `AuditTransactionScope : IDisposable`**  
   Implementiere die `IDisposable`-Schnittstelle mit Statusfeld `_disposed` und werfe `ObjectDisposedException`, wenn auf ein bereits freigegebenes Objekt zugegriffen wird.

3. **TODO 3: `BankAccount` Entität**  
   Implementiere `Deposit(decimal amount)` und `Withdraw(decimal amount)` mit entsprechenden Exception-Prüfungen.

4. **TODO 4: `BankTransferService.TransferFunds`**  
   Implementiere atomare Überweisungen mit `using var scope` und Exception Handling.
