package de.syntaxwerk.aufgabe15;

public class Aufgabe {
    public static double dividiere(double a, double b) {
        if (b == 0.0) {
            throw new IllegalArgumentException("Division durch 0 nicht erlaubt");
        }
        return a / b;
    }

    public static boolean istGueltigeIban(String iban) {
        if (iban == null) return false;
        return iban.matches("^[A-Z]{2}[0-9]{20}$");
    }
}