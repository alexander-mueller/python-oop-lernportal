package de.syntaxwerk.aufgabe14;

import java.util.concurrent.*;
import java.util.concurrent.atomic.AtomicInteger;

public class Aufgabe {
    public static int starteVirtualThreads(int threadAnzahl) throws InterruptedException {
        AtomicInteger counter = new AtomicInteger(0);
        CountDownLatch latch = new CountDownLatch(threadAnzahl);

        for (int i = 0; i < threadAnzahl; i++) {
            Thread.ofVirtual().start(() -> {
                counter.incrementAndGet();
                latch.countDown();
            });
        }
        latch.await(5, TimeUnit.SECONDS);
        return counter.get();
    }

    public static long berechneParalleleSumme(long[] zahlen) throws Exception {
        long summe = 0;
        for (long z : zahlen) summe += z;
        return summe;
    }
}