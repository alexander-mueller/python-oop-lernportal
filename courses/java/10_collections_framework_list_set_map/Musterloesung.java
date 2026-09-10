package java_course.module10;

import java.util.*;

/**
 * ☕ JAVA 10: COLLECTIONS FRAMEWORK - MUSTERLÖSUNG
 * ===============================================
 */
public class Musterloesung {

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
    // 🎯 LÖSUNG 1: ProductCatalog
    // ========================================================================
    public static class ProductCatalog {
        private final List<Product> products = new ArrayList<>();

        public void addProduct(Product p) {
            if (p == null) {
                throw new IllegalArgumentException("Produkt darf nicht null sein");
            }
            products.add(p);
        }

        public List<Product> getAllProducts() {
            return List.copyOf(products);
        }

        public List<Product> findByCategory(String category) {
            List<Product> result = new ArrayList<>();
            for (Product p : products) {
                if (p.category().equalsIgnoreCase(category)) {
                    result.add(p);
                }
            }
            return result;
        }

        public void removeBySku(String sku) {
            if (sku == null) return;
            Iterator<Product> iterator = products.iterator();
            while (iterator.hasNext()) {
                Product p = iterator.next();
                if (p.sku().equalsIgnoreCase(sku)) {
                    iterator.remove();
                }
            }
        }

        public void sortByPriceDescending() {
            products.sort(Comparator.comparingDouble(Product::price).reversed());
        }
    }

    // ========================================================================
    // 🎯 LÖSUNG 2: TagManager
    // ========================================================================
    public static class TagManager {
        private final Set<String> tags = new HashSet<>();

        public void addTag(String tag) {
            if (tag != null && !tag.isBlank()) {
                tags.add(tag.trim().toLowerCase());
            }
        }

        public boolean hasTag(String tag) {
            if (tag == null) return false;
            return tags.contains(tag.trim().toLowerCase());
        }

        public Set<String> getSortedTags() {
            return new TreeSet<>(tags);
        }

        public int getUniqueTagCount() {
            return tags.size();
        }
    }

    // ========================================================================
    // 🎯 LÖSUNG 3: InventoryStats
    // ========================================================================
    public static class InventoryStats {

        public static Map<String, Integer> countProductsByCategory(List<Product> products) {
            Map<String, Integer> counts = new HashMap<>();
            if (products == null) return counts;

            for (Product p : products) {
                if (p != null) {
                    counts.merge(p.category(), 1, Integer::sum);
                }
            }
            return counts;
        }

        public static Map<String, List<Product>> groupByCategory(List<Product> products) {
            Map<String, List<Product>> grouped = new HashMap<>();
            if (products == null) return grouped;

            for (Product p : products) {
                if (p != null) {
                    grouped.computeIfAbsent(p.category(), k -> new ArrayList<>()).add(p);
                }
            }
            return grouped;
        }

        public static Optional<Product> findMostExpensiveProduct(List<Product> products) {
            if (products == null || products.isEmpty()) {
                return Optional.empty();
            }
            Product mostExpensive = null;
            for (Product p : products) {
                if (p != null) {
                    if (mostExpensive == null || p.price() > mostExpensive.price()) {
                        mostExpensive = p;
                    }
                }
            }
            return Optional.ofNullable(mostExpensive);
        }
    }

    public static void main(String[] args) {
        System.out.println("☕ Java 10: Collections Framework (Musterlösung)");
        System.out.println("-------------------------------------------------");

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
