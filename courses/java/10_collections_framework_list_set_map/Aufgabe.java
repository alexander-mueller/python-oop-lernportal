package java_course.module10;

import java.util.*;

/**
 * ☕ JAVA 10: COLLECTIONS FRAMEWORK (LIST, SET, MAP)
 * ==================================================
 * In diesem Modul lernst du das Herzstück von Java kennen:
 * List (geordnete Sequenzen), Set (Eindeutigkeit & Hash-Code-Vertrag),
 * Map (Schlüssel-Wert-Zuordnungen) sowie Sortierung mit Comparatoren.
 */
public class Aufgabe {

    // ========================================================================
    // 🎯 MODEL: Product Record mit equals & hashCode
    // ========================================================================
    public record Product(String sku, String name, double price, String category) implements Comparable<Product> {
        public Product {
            Objects.requireNonNull(sku, "SKU darf nicht null sein");
            Objects.requireNonNull(name, "Name darf nicht null sein");
            Objects.requireNonNull(category, "Category darf nicht null sein");
            if (price < 0) {
                throw new IllegalArgumentException("Preis darf nicht negativ sein");
            }
        }

        @Override
        public int compareTo(Product o) {
            return this.sku.compareTo(o.sku);
        }
    }

    // ========================================================================
    // 🎯 TODO 1: List-Management im 'ProductCatalog'
    // ========================================================================
    // Implementiere die Klasse ProductCatalog basierend auf einer List<Product>.
    //
    // Anforderungen:
    // 1. Verwende intern eine ArrayList<Product>.
    // 2. 'void addProduct(Product p)': Fügt Produkt hinzu (darf nicht null sein).
    // 3. 'List<Product> getAllProducts()': Liefert eine unmodifiable Kopie der Liste (List.copyOf).
    // 4. 'List<Product> findByCategory(String category)': Filtert alle Produkte einer Kategorie.
    // 5. 'void removeBySku(String sku)': Entfernt das Produkt mit der passenden SKU per Iterator.
    // 6. 'void sortByPriceDescending()': Sortiert die interne Liste absteigend nach Preis.
    public static class ProductCatalog {
        private final List<Product> products = new ArrayList<>();

        public void addProduct(Product p) {
            // TODO: Produkt hinzufügen
        }

        public List<Product> getAllProducts() {
            // TODO: Unmodifiable Liste zurückgeben
            return List.of();
        }

        public List<Product> findByCategory(String category) {
            // TODO: Produkte der Kategorie filtern
            return List.of();
        }

        public void removeBySku(String sku) {
            // TODO: Produkt mit sku entfernen (z.B. per Iterator oder removeIf)
        }

        public void sortByPriceDescending() {
            // TODO: Absteigend nach Preis sortieren
        }
    }

    // ========================================================================
    // 🎯 TODO 2: Set-Deduplizierung & Tag-Verwaltung 'TagManager'
    // ========================================================================
    // Implementiere TagManager zur Verwaltung von eindeutigen Tags / Schlagwörtern.
    //
    // Anforderungen:
    // 1. Interne Sets: ein HashSet<String> für schnelle Suche und ein TreeSet<String>
    //    (case-insensitive) für alphabetisch sortierte Ausgabe.
    // 2. 'void addTag(String tag)': Fügt ein Tag hinzu (getrimmt & lowercase).
    // 3. 'boolean hasTag(String tag)': Prüft das Vorhandensein im Set.
    // 4. 'Set<String> getSortedTags()': Gibt die Tags in alphabetischer Reihenfolge zurück.
    // 5. 'int getUniqueTagCount()': Liefert die Anzahl eindeutiger Tags.
    public static class TagManager {
        private final Set<String> tags = new HashSet<>();

        public void addTag(String tag) {
            // TODO: Tag trimmen, lowercase machen und einfügen
        }

        public boolean hasTag(String tag) {
            // TODO: Prüfen ob Tag existiert
            return false;
        }

        public Set<String> getSortedTags() {
            // TODO: Sortiertes Set (TreeSet) zurückgeben
            return Collections.emptySet();
        }

        public int getUniqueTagCount() {
            // TODO: Anzahl eindeutiger Tags
            return 0;
        }
    }

    // ========================================================================
    // 🎯 TODO 3: Map-Aggregation & Häufigkeitszähler 'InventoryStats'
    // ========================================================================
    // Implementiere statistische Map-Operationen für Lagerbestände.
    //
    // Anforderungen:
    // 1. 'public static Map<String, Integer> countProductsByCategory(List<Product> products)'
    //    - Zählt die Anzahl der Produkte pro Kategorie (z.B. "Electronics" -> 5).
    //    - Verwende Map.merge() oder Map.getOrDefault().
    //
    // 2. 'public static Map<String, List<Product>> groupByCategory(List<Product> products)'
    //    - Gruppiert Produkte nach ihrer Kategorie (z.B. "Books" -> [Product1, Product2]).
    //    - Verwende computeIfAbsent().
    //
    // 3. 'public static Optional<Product> findMostExpensiveProduct(List<Product> products)'
    //    - Findet das teuerste Produkt aus der Liste.
    public static class InventoryStats {

        public static Map<String, Integer> countProductsByCategory(List<Product> products) {
            // TODO: Zähle Produkte je Kategorie mit Map
            return Collections.emptyMap();
        }

        public static Map<String, List<Product>> groupByCategory(List<Product> products) {
            // TODO: Gruppiere Produkte in Map<String, List<Product>>
            return Collections.emptyMap();
        }

        public static Optional<Product> findMostExpensiveProduct(List<Product> products) {
            // TODO: Finde teuerstes Produkt
            return Optional.empty();
        }
    }

    public static void main(String[] args) {
        System.out.println("☕ Java 10: Collections Framework (List, Set, Map)");
        System.out.println("--------------------------------------------------");

        Product p1 = new Product("SKU-001", "MacBook Pro", 1999.0, "Hardware");
        Product p2 = new Product("SKU-002", "Clean Code Buch", 39.90, "Books");
        Product p3 = new Product("SKU-003", "Wireless Mouse", 49.99, "Hardware");

        ProductCatalog catalog = new ProductCatalog();
        catalog.addProduct(p1);
        catalog.addProduct(p2);
        catalog.addProduct(p3);

        System.out.println("Hardware Produkte: " + catalog.findByCategory("Hardware").size());

        Map<String, Integer> counts = InventoryStats.countProductsByCategory(List.of(p1, p2, p3));
        System.out.println("Kategorien-Counts: " + counts);
    }
}
