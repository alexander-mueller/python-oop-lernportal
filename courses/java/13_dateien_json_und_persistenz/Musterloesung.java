package de.syntaxwerk.aufgabe13;

import java.io.IOException;
import java.nio.file.*;
import java.util.List;
import java.util.stream.Collectors;

public class Aufgabe {
    public static void schreibeTextInDatei(Path pfad, String inhalt) throws IOException {
        Files.writeString(pfad, inhalt, StandardOpenOption.CREATE, StandardOpenOption.TRUNCATE_EXISTING);
    }

    public static String leseTextAusDatei(Path pfad) throws IOException {
        return Files.readString(pfad);
    }

    public static List<String> filtereZeilen(Path pfad, String suchwort) throws IOException {
        return Files.lines(pfad)
                    .filter(line -> line.contains(suchwort))
                    .collect(Collectors.toList());
    }
}