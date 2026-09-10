package java_course.module10;

import java.util.*;

/**
 * 🧪 TESTSUITE: Java 10 - Collections Framework (List, Set, Map)
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
    // TEST: TestProductCatalogList - Prüft List-Methoden, Filter & Sortierung
    public static void testProductCatalogList() {
        testsTotal++;
        System.out.println("=== RUN   testProductCatalogList");
        Aufgabe.ProductCatalog catalog = new Aufgabe.ProductCatalog();

        Aufgabe.Product p1 = new Aufgabe.Product("SKU-1", "Laptop", 1200.0, "Tech");
        Aufgabe.Product p2 = new Aufgabe.Product("SKU-2", "Headphones", 150.0, "Tech");
        Aufgabe.Product p3 = new Aufgabe.Product("SKU-3", "Java Buch", 45.0, "Books");

        catalog.addProduct(p1);
        catalog.addProduct(p2);
        catalog.addProduct(p3);

        assertEquals(catalog.getAllProducts().size(), 3, "Katalog muss 3 Produkte enthalten");

        List<Aufgabe.Product> techProducts = catalog.findByCategory("Tech");
        assertEquals(techProducts.size(), 2, "2 Produkte in Kategorie Tech erwartet");

        // Löschen per SKU
        catalog.removeBySku("SKU-2");
        assertEquals(catalog.getAllProducts().size(), 2, "Nach Löschen von SKU-2 müssen 2 Produkte verbleiben");

        // Sortieren
        catalog.sortByPriceDescending();
        assertEquals(catalog.getAllProducts().get(0).sku(), "SKU-1", "Teuerstes Produkt muss an Index 0 sein");
        assertEquals(catalog.getAllProducts().get(1).sku(), "SKU-3", "Günstigeres Produkt an Index 1");

        testsPassed++;
        System.out.println("--- PASS: testProductCatalogList");
    }

    // @Test
    // TEST: TestTagManagerSet - Prüft HashSet & TreeSet Funktionalität
    public static void testTagManagerSet() {
        testsTotal++;
        System.out.println("=== RUN   testTagManagerSet");
        Aufgabe.TagManager tagManager = new Aufgabe.TagManager();

        tagManager.addTag("Java");
        tagManager.addTag("  JAVA  "); // Duplikat & Whitespace
        tagManager.addTag("cloud");
        tagManager.addTag("Architecture");

        assertEquals(tagManager.getUniqueTagCount(), 3, "Eindeutige Tags müssen 3 sein ('java', 'cloud', 'architecture')");
        assertTrue(tagManager.hasTag("java"), "Tag 'java' muss existieren");
        assertTrue(tagManager.hasTag("JAVA"), "Tag 'JAVA' muss unabhängig von Groß-/Kleinschreibung gefunden werden");
        assertFalse(tagManager.hasTag("python"), "Tag 'python' existiert nicht");

        Set<String> sorted = tagManager.getSortedTags();
        List<String> list = new ArrayList<>(sorted);
        assertEquals(list.get(0), "architecture", "Erstes alphabetisches Tag muss 'architecture' sein");
        assertEquals(list.get(1), "cloud", "Zweites Tag 'cloud'");
        assertEquals(list.get(2), "java", "Drittes Tag 'java'");

        testsPassed++;
        System.out.println("--- PASS: testTagManagerSet");
    }

    // @Test
    // TEST: TestInventoryStatsMap - Prüft Map Aggregationen & Gruppierungen
    public static void testInventoryStatsMap() {
        testsTotal++;
        System.out.println("=== RUN   testInventoryStatsMap");
        Aufgabe.Product p1 = new Aufgabe.Product("SKU-1", "Monitor", 300.0, "Hardware");
        Aufgabe.Product p2 = new Aufgabe.Product("SKU-2", "Keyboard", 80.0, "Hardware");
        Aufgabe.Product p3 = new Aufgabe.Product("SKU-3", "Design Patterns", 55.0, "Books");
        Aufgabe.Product p4 = new Aufgabe.Product("SKU-4", "Refactoring", 60.0, "Books");
        Aufgabe.Product p5 = new Aufgabe.Product("SKU-5", "Server Rack", 2500.0, "Hardware");

        List<Aufgabe.Product> list = List.of(p1, p2, p3, p4, p5);

        Map<String, Integer> counts = Aufgabe.InventoryStats.countProductsByCategory(list);
        assertEquals(counts.get("Hardware"), 3, "Hardware muss 3 Produkte haben");
        assertEquals(counts.get("Books"), 2, "Books muss 2 Produkte haben");

        Map<String, List<Aufgabe.Product>> grouped = Aufgabe.InventoryStats.groupByCategory(list);
        assertEquals(grouped.get("Books").size(), 2, "Grouped Books muss 2 Elemente haben");
        assertEquals(grouped.get("Hardware").size(), 3, "Grouped Hardware muss 3 Elemente haben");

        Optional<Aufgabe.Product> mostExpensive = Aufgabe.InventoryStats.findMostExpensiveProduct(list);
        assertTrue(mostExpensive.isPresent(), "Teuerstes Produkt muss vorhanden sein");
        assertEquals(mostExpensive.get().sku(), "SKU-5", "Server Rack mit SKU-5 ist das teuerste Produkt");

        testsPassed++;
        System.out.println("--- PASS: testInventoryStatsMap");
    }

    public static void main(String[] args) {
        System.out.println("🧪 Führe Java 10 Collections Testsuite aus...\n----------------------------------------");
        try {
            testProductCatalogList();
            testTagManagerSet();
            testInventoryStatsMap();
            System.out.println("\n🎉 JUnit 5: Alle " + testsPassed + "/" + testsTotal + " Tests erfolgreich bestanden!");
        } catch (AssertionError e) {
            System.err.println("\n" + e.getMessage());
            System.exit(1);
        }
    }
}
