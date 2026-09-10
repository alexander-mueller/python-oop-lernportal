package de.syntaxwerk;

public class Aufgabe { public static abstract class Tier { public abstract String laut(); } public static class Hund extends Tier { @Override public String laut() { return "Wuff"; } } }
