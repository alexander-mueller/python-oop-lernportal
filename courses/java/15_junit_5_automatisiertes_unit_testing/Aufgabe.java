package de.syntaxwerk.aufgabe15;

public class Aufgabe {
    // 🎯 TEILZIEL 1 (TODO 1): Rechnerklasse mit Validierung
    public static double dividiere(double a, double b) {
        if (b == 0.0) {
            throw new IllegalArgumentException("Division durch 0 nicht erlaubt");
        }
        return a / b;
    }

    // 🎯 TEILZIEL 2 (TODO 2): Prüfe ob String eine gültige IBAN ist
    public static boolean istGueltigeIban(String iban) {
        if (iban == null) return false;
        return iban.matches("^[A-Z]{2}[0-9]{20}$");
    }
}