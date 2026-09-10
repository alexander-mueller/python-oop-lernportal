# ☕ Java 11: Exceptions & Ressourcenmanagement

Professionelles Fehlermanagement entscheidet über die Stabilität unternehmenskritischer Java-Anwendungen. In diesem Modul lernst du die Differenzierung zwischen **Checked** und **Unchecked** Exceptions, das Design robuster Business-Exception-Hierarchien und das deterministische Ressourcenmanagement mit `try-with-resources`.

---

## 🏛️ 1. Die Java Exception-Hierarchie

```
                       Throwable
                           ▲
             ┌─────────────┴─────────────┐
           Error                      Exception
     (z.B. OutOfMemory)                  ▲
                           ┌─────────────┴─────────────┐
                   Checked Exceptions           RuntimeException
                   (z.B. IOException)          (Unchecked Exceptions)
                                                (z.B. NullPointer,
                                                 IllegalArgument)
```

- **Checked Exceptions (`extends Exception`):** Müssen mit `throws` im Methodenkopf deklariert oder per `try-catch` behandelt werden. Signalisiert erwartbare Fehlerzustände (Netzwerk, I/O, Payment Gateway).
- **Unchecked Exceptions (`extends RuntimeException`):** Müssen nicht explizit deklariert werden. Weisen typischerweise auf Programmierfehler oder verletzte Vorbedingungen hin.

---

## 🔄 2. Try-With-Resources & AutoCloseable

Früher wurden Ressourcen (Dateien, Datenbankverbindungen, Sockets) in fehleranfälligen `finally`-Blöcken geschlossen. Seit Java 7 übernimmt **`try-with-resources`** das Schließen automatisch und garantiert:

```java
public class DatabaseClient implements AutoCloseable {
    @Override
    public void close() {
        System.out.println("Datenbankverbindung deterministisch geschlossen.");
    }
}

// Sichere Verwendung:
try (DatabaseClient db = new DatabaseClient()) {
    db.query("SELECT * FROM users");
} // <- Hier wird db.close() IMMER aufgerufen, auch bei Exceptions!
```

---

## 🔗 3. Exception Chaining & Multi-Catch

```java
try {
    service.executeTransfer(from, to, amount);
} catch (InsufficientFundsException | InvalidAccountException e) {
    // Multi-Catch für ähnliche Fehlertypen
    logger.error("Geschäftsfehler: " + e.getMessage());
    // Chaining: Neue Exception mit Originalursache (cause)
    throw new PaymentGatewayException("Transaktion abgebrochen", e);
}
```

---

## 🎯 Aufgabenübersicht (`Aufgabe.java`)

1. **TODO 1:** `BankAccount` mit Validierung, `deposit()` und `withdraw()` inklusive `InsufficientFundsException`.
2. **TODO 2:** `AuditLogSession` mit `AutoCloseable` implementieren (deterministischer Log & State-Prüfung).
3. **TODO 3:** `PaymentProcessor.processPayment(...)` mit `try-with-resources`, Multi-Catch und Exception-Chaining fertigstellen.
