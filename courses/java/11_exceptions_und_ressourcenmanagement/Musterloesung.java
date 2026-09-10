package java_course.module11;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

/**
 * ☕ JAVA 11: EXCEPTIONS & RESSOURCENMANAGEMENT - MUSTERLÖSUNG
 * ============================================================
 */
public class Musterloesung {

    public static class PaymentGatewayException extends Exception {
        public PaymentGatewayException(String message) {
            super(message);
        }

        public PaymentGatewayException(String message, Throwable cause) {
            super(message, cause);
        }
    }

    public static class InsufficientFundsException extends RuntimeException {
        private final double requestedAmount;
        private final double currentBalance;

        public InsufficientFundsException(String message, double requestedAmount, double currentBalance) {
            super(message);
            this.requestedAmount = requestedAmount;
            this.currentBalance = currentBalance;
        }

        public double getRequestedAmount() {
            return requestedAmount;
        }

        public double getCurrentBalance() {
            return currentBalance;
        }
    }

    public static class InvalidAccountException extends RuntimeException {
        public InvalidAccountException(String message) {
            super(message);
        }
    }

    // ========================================================================
    // 🎯 LÖSUNG 1: BankAccount
    // ========================================================================
    public static class BankAccount {
        private final String iban;
        private double balance;

        public BankAccount(String iban, double initialBalance) {
            if (iban == null || iban.trim().length() < 15) {
                throw new InvalidAccountException("Ungültige IBAN: Mindestens 15 Zeichen erforderlich.");
            }
            if (initialBalance < 0) {
                throw new InvalidAccountException("Initialer Kontostand darf nicht negativ sein.");
            }
            this.iban = iban.trim();
            this.balance = initialBalance;
        }

        public String getIban() {
            return iban;
        }

        public double getBalance() {
            return balance;
        }

        public void deposit(double amount) {
            if (amount <= 0) {
                throw new IllegalArgumentException("Einzahlungsbetrag muss positiv sein: " + amount);
            }
            this.balance += amount;
        }

        public void withdraw(double amount) {
            if (amount <= 0) {
                throw new IllegalArgumentException("Auszahlungsbetrag muss positiv sein: " + amount);
            }
            if (amount > this.balance) {
                throw new InsufficientFundsException(
                        "Nicht genügend Deckung für Auszahlung von " + amount + " (Saldo: " + this.balance + ")",
                        amount,
                        this.balance
                );
            }
            this.balance -= amount;
        }
    }

    // ========================================================================
    // 🎯 LÖSUNG 2: AuditLogSession mit AutoCloseable
    // ========================================================================
    public static class AuditLogSession implements AutoCloseable {
        private final String sessionId;
        private boolean isOpen;
        private final List<String> entries = new ArrayList<>();

        public AuditLogSession(String sessionId) {
            this.sessionId = sessionId != null ? sessionId : "ANON_SESSION";
            this.isOpen = true;
        }

        public void log(String action) {
            if (!isOpen) {
                throw new IllegalStateException("Session ist geschlossen!");
            }
            entries.add("[" + sessionId + "] " + action);
        }

        @Override
        public void close() {
            if (isOpen) {
                entries.add("[" + sessionId + "] CLOSED");
                isOpen = false;
            }
        }

        public boolean isOpen() {
            return isOpen;
        }

        public List<String> getEntries() {
            return List.copyOf(entries);
        }
    }

    // ========================================================================
    // 🎯 LÖSUNG 3: PaymentProcessor mit Try-With-Resources
    // ========================================================================
    public static class PaymentProcessor {

        public static boolean processPayment(BankAccount from, BankAccount to, double amount, String sessionId)
                throws PaymentGatewayException {
            if (from == null || to == null) {
                throw new PaymentGatewayException("Absender- oder Empfängerkonto darf nicht null sein.");
            }

            try (AuditLogSession session = new AuditLogSession(sessionId)) {
                session.log("START: Transfer " + amount);
                try {
                    from.withdraw(amount);
                    to.deposit(amount);
                    session.log("SUCCESS: Transferred " + amount);
                    return true;
                } catch (InsufficientFundsException | IllegalArgumentException e) {
                    session.log("FAILED: " + e.getMessage());
                    throw new PaymentGatewayException("Zahlung fehlgeschlagen: " + e.getMessage(), e);
                }
            }
        }
    }

    public static void main(String[] args) {
        System.out.println("☕ Java 11: Exceptions (Musterlösung)");
        System.out.println("-------------------------------------");

        BankAccount acc1 = new BankAccount("DE89370400440532013000", 500.0);
        BankAccount acc2 = new BankAccount("DE27100777770346893001", 100.0);

        try {
            PaymentProcessor.processPayment(acc1, acc2, 200.0, "TXN-8819");
            System.out.println("Überweisung erfolgreich! Neuer Saldo Acc1: " + acc1.getBalance());
        } catch (PaymentGatewayException e) {
            System.err.println("Fehler: " + e.getMessage());
        }
    }
}
