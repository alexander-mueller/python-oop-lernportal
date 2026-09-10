package de.syntaxwerk;

public class Aufgabe { public static String bewerteNote(int note) { return switch(note) { case 1 -> "Sehr gut"; case 2 -> "Gut"; default -> "Bestanden"; }; } }
