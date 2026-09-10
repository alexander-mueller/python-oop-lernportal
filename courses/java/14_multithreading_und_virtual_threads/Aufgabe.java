package de.syntaxwerk.aufgabe14;

import java.util.concurrent.*;
import java.util.concurrent.atomic.AtomicInteger;

public class Aufgabe {
    // 🎯 TEILZIEL 1 (TODO 1): Starte n Virtual Threads, die einen AtomicInteger inkrementieren
    public static int starteVirtualThreads(int threadAnzahl) throws InterruptedException {
        AtomicInteger counter = new AtomicInteger(0);
        // TODO: Virtual Threads starten und warten
        return counter.get();
    }

    // 🎯 TEILZIEL 2 (TODO 2): Parallele Summenberechnung mit ExecutorService
    public static long berechneParalleleSumme(long[] zahlen) throws Exception {
        // TODO: Implementieren
        return 0L;
    }
}