package de.syntaxwerk.aufgabe16;

import java.util.*;

public class Aufgabe {
    public static class BankAccount {
        private final String iban;
        private final String inhaber;
        private double saldo;

        public BankAccount(String iban, String inhaber, double startSaldo) {
            this.iban = iban;
            this.inhaber = inhaber;
            this.saldo = startSaldo;
        }

        public synchronized boolean einzahlen(double betrag) {
            if (betrag <= 0) return false;
            this.saldo += betrag;
            return true;
        }

        public synchronized boolean abheben(double betrag) {
            if (betrag <= 0 || betrag > this.saldo) return false;
            this.saldo -= betrag;
            return true;
        }

        public String getIban() { return iban; }
        public String getInhaber() { return inhaber; }
        public double getSaldo() { return saldo; }
    }

    public static class BankSystem {
        private final Map<String, BankAccount> konten = new HashMap<>();

        public void kontoHinzufuegen(BankAccount konto) {
            konten.put(konto.getIban(), konto);
        }

        public boolean ueberweisen(String vonIban, String zuIban, double betrag) {
            BankAccount von = konten.get(vonIban);
            BankAccount zu = konten.get(zuIban);
            if (von == null || zu == null || betrag <= 0) return false;
            if (von.abheben(betrag)) {
                zu.einzahlen(betrag);
                return true;
            }
            return false;
        }

        public double getGesamteinlagen() {
            return konten.values().stream().mapToDouble(BankAccount::getSaldo).sum();
        }
    }
}