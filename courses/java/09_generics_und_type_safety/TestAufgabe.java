package java_course.module09;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

/**
 * 🧪 TESTSUITE: Java 09 - Generics & Type Safety
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
    // TEST: TestBoxGenerics - Prüft Box<T> mit Typisierung & Optional
    public static void testBoxGenerics() {
        testsTotal++;
        System.out.println("=== RUN   testBoxGenerics");
        Aufgabe.Box<String> emptyBox = new Aufgabe.Box<>();
        assertTrue(emptyBox.isEmpty(), "Neue Standardbox sollte leer sein");
        assertEquals(emptyBox.toOptional(), Optional.empty(), "toOptional() einer leeren Box muss Optional.empty() sein");

        Aufgabe.Box<Integer> intBox = new Aufgabe.Box<>(100);
        assertFalse(intBox.isEmpty(), "Box mit 100 ist nicht leer");
        assertEquals(intBox.getContent(), 100, "getContent() muss 100 liefern");
        assertEquals(intBox.toOptional(), Optional.of(100), "toOptional() muss Optional[100] liefern");

        intBox.setContent(250);
        assertEquals(intBox.getContent(), 250, "setContent() muss Wert aktualisieren");

        testsPassed++;
        System.out.println("--- PASS: testBoxGenerics");
    }

    // @Test
    // TEST: TestGenericCache - Prüft GenericCache<K, V> put/get/containsKey/size/clear
    public static void testGenericCache() {
        testsTotal++;
        System.out.println("=== RUN   testGenericCache");
        Aufgabe.GenericCache<String, Double> cache = new Aufgabe.GenericCache<>();
        assertEquals(cache.size(), 0, "Initialer Cache muss leer sein (size 0)");

        cache.put("EUR_USD", 1.085);
        cache.put("EUR_GBP", 0.855);
        assertEquals(cache.size(), 2, "Cache muss 2 Einträge enthalten");
        assertTrue(cache.containsKey("EUR_USD"), "Cache muss EUR_USD enthalten");
        assertFalse(cache.containsKey("EUR_JPY"), "Cache darf EUR_JPY nicht enthalten");

        assertEquals(cache.get("EUR_USD"), Optional.of(1.085), "get(EUR_USD) muss 1.085 liefern");
        assertEquals(cache.get("UNKNOWN"), Optional.empty(), "get(UNKNOWN) muss empty liefern");

        // Überschreiben
        cache.put("EUR_USD", 1.090);
        assertEquals(cache.size(), 2, "Größe bleibt 2 nach Update");
        assertEquals(cache.get("EUR_USD"), Optional.of(1.090), "EUR_USD muss aktualisiert sein");

        cache.clear();
        assertEquals(cache.size(), 0, "Nach clear() muss Größe 0 sein");

        testsPassed++;
        System.out.println("--- PASS: testGenericCache");
    }

    // @Test
    // TEST: TestBoundedGenericsMath - Prüft findMax() und calculateSum()
    public static void testBoundedGenericsMath() {
        testsTotal++;
        System.out.println("=== RUN   testBoundedGenericsMath");
        List<Integer> zahlen = List.of(10, 50, 3, 99, 42);
        assertEquals(Aufgabe.GenericsMath.findMax(zahlen), 99, "findMax muss 99 finden");

        List<String> worte = List.of("Apfel", "Zebra", "Banane");
        assertEquals(Aufgabe.GenericsMath.findMax(worte), "Zebra", "findMax auf Strings muss 'Zebra' finden");

        List<Double> doubleList = List.of(1.5, 2.5, 3.0);
        assertEquals(Aufgabe.GenericsMath.calculateSum(doubleList), 7.0, "Summe von 1.5 + 2.5 + 3.0 muss 7.0 sein");

        List<Number> gemischt = List.of(10, 20.5f, 5.5);
        assertEquals(Aufgabe.GenericsMath.calculateSum(gemischt), 36.0, "Summe gemischter Numbers muss 36.0 sein");

        boolean threwException = false;
        try {
            Aufgabe.GenericsMath.findMax(List.of());
        } catch (IllegalArgumentException e) {
            threwException = true;
        }
        assertTrue(threwException, "findMax auf leerer Liste muss IllegalArgumentException werfen");

        testsPassed++;
        System.out.println("--- PASS: testBoundedGenericsMath");
    }

    // @Test
    // TEST: TestWildcardsPECS - Prüft copyList() und countElements()
    public static void testWildcardsPECS() {
        testsTotal++;
        System.out.println("=== RUN   testWildcardsPECS");
        List<Integer> ints = List.of(1, 2, 3, 4, 5);
        List<Number> numbers = new ArrayList<>();

        // PECS: Integer extends Number (src = ? extends Number, dest = ? super Number)
        Aufgabe.WildcardUtils.copyList(ints, numbers);
        assertEquals(numbers.size(), 5, "numbers muss nach copy 5 Elemente haben");
        assertEquals(numbers.get(0), 1, "Erstes Element muss 1 sein");

        assertEquals(Aufgabe.WildcardUtils.countElements(numbers), 5, "countElements muss 5 liefern");
        assertEquals(Aufgabe.WildcardUtils.countElements(null), 0, "countElements bei null muss 0 liefern");

        testsPassed++;
        System.out.println("--- PASS: testWildcardsPECS");
    }

    public static void main(String[] args) {
        System.out.println("🧪 Führe Java 09 Generics & Type Safety Testsuite aus...\n----------------------------------------");
        try {
            testBoxGenerics();
            testGenericCache();
            testBoundedGenericsMath();
            testWildcardsPECS();
            System.out.println("\n🎉 JUnit 5: Alle " + testsPassed + "/" + testsTotal + " Tests erfolgreich bestanden!");
        } catch (AssertionError e) {
            System.err.println("\n" + e.getMessage());
            System.exit(1);
        }
    }
}
