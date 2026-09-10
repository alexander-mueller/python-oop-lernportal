package java_course.module11;

/**
 * 🧪 TESTSUITE: Java 11 - Exceptions & Ressourcenmanagement
 */
public class TestAufgabe {

    private static int testsPassed = 0;
    private static int testsTotal = 0;

    private static void assertEquals(Object actual, Object expected, String message) {
        if (actual == null && expected == null) return;
        if (actual == null || !actual.equals(expected)) {
            throw new AssertionError("❌ FAILED: " + message + " (Erwartet: " + expected + ", Erhalten: " + actual + ")");
        }
    }

    private static void assertTrue(boolean condition, String message) {
        if (!condition) {
            throw new AssertionError("❌ FAILED: " + message);
        }
    }

    private static void assertFalse(boolean condition, String message) {
        if (condition) {
            throw new AssertionError("❌ FAILED: " + message);
        }
    }

    // @Test
    // TEST: TestBankAccountValidation - Prüft Exception-Auslösung bei ungültigen Werten
    public static void testBankAccountValidation() {
        testsTotal++;
        System.out.println("=== RUN   testBankAccountValidation");

        // Gültiges Konto
        Aufgabe.BankAccount account = new Aufgabe.BankAccount("DE89370400440532013000", 1000.0);
        assertEquals(account.getBalance(), 1000.0, "Initialer Saldo muss 1000.0 sein");

        // Ungültige IBAN
        boolean threwInvalidAccount = false;
        try {
            new Aufgabe.BankAccount("DE123", 50.0);
        } catch (Aufgabe.InvalidAccountException e) {
            threwInvalidAccount = true;
        }
        assertTrue(threwInvalidAccount, "Zu kurze IBAN muss InvalidAccountException werfen");

        // Negativer Initial-Saldo
        threwInvalidAccount = false;
        try {
            new Aufgabe.BankAccount("DE89370400440532013000", -10.0);
        } catch (Aufgabe.InvalidAccountException e) {
            threwInvalidAccount = true;
        }
        assertTrue(threwInvalidAccount, "Negativer Initial-Saldo muss InvalidAccountException werfen");

        testsPassed++;
        System.out.println("--- PASS: testBankAccountValidation");
    }

    // @Test
    // TEST: TestDepositAndWithdrawExceptions - Prüft Ein- und Auszahlungslimits
    public static void testDepositAndWithdrawExceptions() {
        testsTotal++;
        System.out.println("=== RUN   testDepositAndWithdrawExceptions");

        Aufgabe.BankAccount account = new Aufgabe.BankAccount("DE89370400440532013000", 200.0);
        account.deposit(50.0);
        assertEquals(account.getBalance(), 250.0, "Saldo nach Einzahlung muss 250.0 sein");

        // Negative Einzahlung
        boolean threwIllegalArgument = false;
        try {
            account.deposit(-20.0);
        } catch (IllegalArgumentException e) {
            threwIllegalArgument = true;
        }
        assertTrue(threwIllegalArgument, "Negative Einzahlung muss IllegalArgumentException werfen");

        // Überziehung ohne Dispo
        boolean threwInsufficientFunds = false;
        try {
            account.withdraw(300.0);
        } catch (Aufgabe.InsufficientFundsException e) {
            threwInsufficientFunds = true;
            assertEquals(e.getRequestedAmount(), 300.0, "Requested Amount in Exception muss 300.0 sein");
            assertEquals(e.getCurrentBalance(), 250.0, "Current Balance in Exception muss 250.0 sein");
        }
        assertTrue(threwInsufficientFunds, "Überziehung muss InsufficientFundsException werfen");

        // Gültige Auszahlung
        account.withdraw(50.0);
        assertEquals(account.getBalance(), 200.0, "Saldo nach 50.0 Auszahlung muss 200.0 sein");

        testsPassed++;
        System.out.println("--- PASS: testDepositAndWithdrawExceptions");
    }

    // @Test
    // TEST: TestAuditLogSessionAutoCloseable - Prüft AutoCloseable & Exception nach Schließen
    public static void testAuditLogSessionAutoCloseable() {
        testsTotal++;
        System.out.println("=== RUN   testAuditLogSessionAutoCloseable");

        Aufgabe.AuditLogSession session = new Aufgabe.AuditLogSession("SES-01");
        assertTrue(session.isOpen(), "Session muss initial offen sein");
        session.log("Action 1");

        session.close();
        assertFalse(session.isOpen(), "Nach close() muss isOpen false sein");
        assertTrue(session.getEntries().contains("[SES-01] CLOSED"), "Eintrag [SES-01] CLOSED muss existieren");

        boolean threwIllegalState = false;
        try {
            session.log("Action after close");
        } catch (IllegalStateException e) {
            threwIllegalState = true;
        }
        assertTrue(threwIllegalState, "Log nach Session-Schluss muss IllegalStateException werfen");

        testsPassed++;
        System.out.println("--- PASS: testAuditLogSessionAutoCloseable");
    }

    // @Test
    // TEST: TestPaymentProcessorTryWithResources - Prüft Transaktion & Exception Chaining
    public static void testPaymentProcessorTryWithResources() {
        testsTotal++;
        System.out.println("=== RUN   testPaymentProcessorTryWithResources");

        Aufgabe.BankAccount from = new Aufgabe.BankAccount("DE89370400440532013000", 500.0);
        Aufgabe.BankAccount to = new Aufgabe.BankAccount("DE27100777770346893001", 100.0);

        try {
            boolean success = Aufgabe.PaymentProcessor.processPayment(from, to, 150.0, "TXN-101");
            assertTrue(success, "processPayment muss true zurückgeben");
            assertEquals(from.getBalance(), 350.0, "From Kontostand muss 350 sein");
            assertEquals(to.getBalance(), 250.0, "To Kontostand muss 250 sein");
        } catch (Aufgabe.PaymentGatewayException e) {
            throw new AssertionError("Unerwartete PaymentGatewayException: " + e.getMessage());
        }

        // Fehlgeschlagene Transaktion (Überziehung)
        boolean threwPaymentGatewayException = false;
        try {
            Aufgabe.PaymentProcessor.processPayment(from, to, 9999.0, "TXN-102");
        } catch (Aufgabe.PaymentGatewayException e) {
            threwPaymentGatewayException = true;
            assertTrue(e.getCause() instanceof Aufgabe.InsufficientFundsException, "Cause muss InsufficientFundsException sein");
        }
        assertTrue(threwPaymentGatewayException, "Überziehung muss PaymentGatewayException auslösen");

        testsPassed++;
        System.out.println("--- PASS: testPaymentProcessorTryWithResources");
    }

    public static void main(String[] args) {
        System.out.println("🧪 Führe Java 11 Exceptions Testsuite aus...\n----------------------------------------");
        try {
            testBankAccountValidation();
            testDepositAndWithdrawExceptions();
            testAuditLogSessionAutoCloseable();
            testPaymentProcessorTryWithResources();
            System.out.println("\n🎉 JUnit 5: Alle " + testsPassed + "/" + testsTotal + " Tests erfolgreich bestanden!");
        } catch (AssertionError e) {
            System.err.println("\n" + e.getMessage());
            System.exit(1);
        }
    }
}
