package java_course.module11;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

/**
 * ☕ JAVA 11: EXCEPTIONS & RESSOURCENMANAGEMENT
 * =============================================
 * In diesem Modul meisterst du professionelles Fehlermanagement in Java:
 * Checked vs. Unchecked Exceptions, Custom Exception Hierarchien,
 * Multi-Catch und deterministisches Schließen via try-with-resources (AutoCloseable).
 */
public class Aufgabe {

    // ========================================================================
    // 🎯 MODEL & EXCEPTIONS
    // ========================================================================
    
    // Checked Exception (muss deklariert oder gefangen werden)
    public static class PaymentGatewayException extends Exception {
        public PaymentGatewayException(String message) {
            super(message);
        }

        public PaymentGatewayException(String message, Throwable cause) {
            super(message, cause);
        }
    }

    // Unchecked Exception (Runtime)
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

    // Unchecked Exception für ungültige Eingaben
    public static class InvalidAccountException extends RuntimeException {
        public InvalidAccountException(String message) {
            super(message);
        }
    }

    // ========================================================================
    // 🎯 TODO 1: Validierung & Exception-Auslösung 'BankAccount'
    // ========================================================================
    // Implementiere die BankAccount Klasse mit strikter Validierung.
    //
    // Anforderungen:
    // 1. Felder: iban (String), balance (double).
    // 2. Konstruktor: wirft InvalidAccountException, wenn iban null ist, weniger als 15 Zeichen hat
    //    oder initialBalance negativ ist.
    // 3. 'void deposit(double amount)': wirft IllegalArgumentException, wenn amount <= 0 ist.
    // 4. 'void withdraw(double amount)':
    //    - wirft IllegalArgumentException, wenn amount <= 0 ist.
    //    - wirft InsufficientFundsException, wenn amount > balance ist.
    //    - bucht den Betrag sonst ab.
    public static class BankAccount {
        private final String iban;
        private double balance;

        public BankAccount(String iban, double initialBalance) {
            // TODO: Validierung & Initialisierung
            this.iban = iban;
            this.balance = initialBalance;
        }

        public String getIban() {
            return iban;
        }

        public double getBalance() {
            return balance;
        }

        public void deposit(double amount) {
            // TODO: Einzahlung validieren & durchführen
        }

        public void withdraw(double amount) {
            // TODO: Auszahlung validieren & durchführen
        }
    }

    // ========================================================================
    // 🎯 TODO 2: AutoCloseable Ressource 'AuditLogSession'
    // ========================================================================
    // Implementiere eine Ressource, die AutoCloseable implementiert.
    //
    // Anforderungen:
    // 1. Felder: sessionId (String), isOpen (boolean), auditEntries (List<String>).
    // 2. Konstruktor(String sessionId): setzt isOpen = true.
    // 3. 'void log(String action)':
    //    - wirft IllegalStateException("Session ist geschlossen!"), wenn isOpen == false ist.
    //    - fügt den Eintrag "[sessionId] action" der Liste hinzu.
    // 4. 'close()': setzt isOpen = false und fügt "[sessionId] CLOSED" hinzu.
    public static class AuditLogSession implements AutoCloseable {
        private final String sessionId;
        private boolean isOpen;
        private final List<String> entries = new ArrayList<>();

        public AuditLogSession(String sessionId) {
            this.sessionId = sessionId;
            this.isOpen = true;
        }

        public void log(String action) {
            // TODO: Protokollieren oder Exception werfen falls geschlossen
        }

        @Override
        public void close() {
            // TODO: Session sauber schließen
        }

        public boolean isOpen() {
            return isOpen;
        }

        public List<String> getEntries() {
            return List.copyOf(entries);
        }
    }

    // ========================================================================
    // 🎯 TODO 3: Transaktionsprozessor mit Try-With-Resources & Multi-Catch
    // ========================================================================
    // Implementiere den PaymentProcessor zur Abwicklung von Überweisungen.
    //
    // Anforderungen:
    // 1. 'public static boolean processPayment(BankAccount from, BankAccount to, double amount, String sessionId) throws PaymentGatewayException'
    // 2. Nutze ein try-with-resources Statement für eine neue AuditLogSession(sessionId).
    // 3. Logge zu Beginn: "START: Transfer " + amount.
    // 4. Führe from.withdraw(amount) und to.deposit(amount) aus.
    // 5. Logge bei Erfolg: "SUCCESS: Transferred " + amount.
    // 6. Fange InsufficientFundsException oder IllegalArgumentException:
    //    - Logge: "FAILED: " + e.getMessage()
    //    - Wirf eine neue PaymentGatewayException("Zahlung fehlgeschlagen", e) mit Cause!
    // 7. Am Ende des Blocks garantiert die JVM, dass auditSession.close() aufgerufen wird.
    public static class PaymentProcessor {

        public static boolean processPayment(BankAccount from, BankAccount to, double amount, String sessionId)
                throws PaymentGatewayException {
            // TODO: Implementiere try-with-resources mit AuditLogSession & Exception Chaining
            return false;
        }
    }

    public static void main(String[] args) {
        System.out.println("☕ Java 11: Exceptions & Ressourcenmanagement");
        System.out.println("----------------------------------------------");

        BankAccount acc1 = new BankAccount("DE89370400440532013000", 500.0);
        BankAccount acc2 = new BankAccount("DE27100777770346893001", 100.0);

        try {
            PaymentProcessor.processPayment(acc1, acc2, 200.0, "TXN-8819");
            System.out.println("Überweisung erfolgreich! Neuer Saldo Acc1: " + acc1.getBalance());
        } catch (PaymentGatewayException e) {
            System.err.println("Fehler bei Überweisung: " + e.getMessage() + " | Ursache: " + e.getCause());
        }
    }
}
