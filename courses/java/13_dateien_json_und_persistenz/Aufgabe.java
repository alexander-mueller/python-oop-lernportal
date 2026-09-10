package de.syntaxwerk.aufgabe13;

import java.io.IOException;
import java.nio.file.*;
import java.util.List;

public class Aufgabe {
    // 🎯 TEILZIEL 1 (TODO 1): Text in eine Datei schreiben mit Files.writeString()
    public static void schreibeTextInDatei(Path pfad, String inhalt) throws IOException {
        // TODO: Implementieren
    }

    // 🎯 TEILZIEL 2 (TODO 2): Dateiinhalt als String auslesen mit Files.readString()
    public static String leseTextAusDatei(Path pfad) throws IOException {
        // TODO: Implementieren
        return "";
    }

    // 🎯 TEILZIEL 3 (TODO 3): Alle Zeilen einer Datei filtern und als Liste zurückgeben
    public static List<String> filtereZeilen(Path pfad, String suchwort) throws IOException {
        // TODO: Implementieren
        return List.of();
    }
}