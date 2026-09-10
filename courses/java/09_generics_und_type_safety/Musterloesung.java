package java_course.module09;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import java.util.Optional;

/**
 * ☕ JAVA 09: GENERICS & TYPE SAFETY - MUSTERLÖSUNG
 * ================================================
 */
public class Musterloesung {

    // ========================================================================
    // 🎯 LÖSUNG 1: Generische Container-Klasse 'Box<T>'
    // ========================================================================
    public static class Box<T> {
        private T content;

        public Box() {
            this.content = null;
        }

        public Box(T content) {
            this.content = content;
        }

        public T getContent() {
            return content;
        }

        public void setContent(T content) {
            this.content = content;
        }

        public boolean isEmpty() {
            return content == null;
        }

        public Optional<T> toOptional() {
            return Optional.ofNullable(content);
        }
    }

    // ========================================================================
    // 🎯 LÖSUNG 2: Generischer Cache mit Schlüssel-Wert-Paaren 'GenericCache<K, V>'
    // ========================================================================
    public static class GenericCache<K, V> {
        private static class Entry<K, V> {
            final K key;
            V value;

            Entry(K key, V value) {
                this.key = key;
                this.value = value;
            }
        }

        private final List<Entry<K, V>> entries = new ArrayList<>();

        public void put(K key, V value) {
            for (Entry<K, V> entry : entries) {
                if (Objects.equals(entry.key, key)) {
                    entry.value = value;
                    return;
                }
            }
            entries.add(new Entry<>(key, value));
        }

        public Optional<V> get(K key) {
            for (Entry<K, V> entry : entries) {
                if (Objects.equals(entry.key, key)) {
                    return Optional.ofNullable(entry.value);
                }
            }
            return Optional.empty();
        }

        public boolean containsKey(K key) {
            for (Entry<K, V> entry : entries) {
                if (Objects.equals(entry.key, key)) {
                    return true;
                }
            }
            return false;
        }

        public int size() {
            return entries.size();
        }

        public void clear() {
            entries.clear();
        }
    }

    // ========================================================================
    // 🎯 LÖSUNG 3: Bounded Generics - Maximum & Statistik Finder
    // ========================================================================
    public static class GenericsMath {

        public static <T extends Comparable<T>> T findMax(List<T> items) {
            if (items == null || items.isEmpty()) {
                throw new IllegalArgumentException("Liste darf weder null noch leer sein.");
            }
            T max = items.get(0);
            for (T item : items) {
                if (item != null && (max == null || item.compareTo(max) > 0)) {
                    max = item;
                }
            }
            return max;
        }

        public static <N extends Number> double calculateSum(List<N> numbers) {
            if (numbers == null || numbers.isEmpty()) {
                return 0.0;
            }
            double sum = 0.0;
            for (N number : numbers) {
                if (number != null) {
                    sum += number.doubleValue();
                }
            }
            return sum;
        }
    }

    // ========================================================================
    // 🎯 LÖSUNG 4: Wildcards & PECS-Prinzip
    // ========================================================================
    public static class WildcardUtils {

        public static <T> void copyList(List<? extends T> src, List<? super T> dest) {
            if (src == null || dest == null) {
                return;
            }
            for (T item : src) {
                dest.add(item);
            }
        }

        public static int countElements(List<?> list) {
            if (list == null) {
                return 0;
            }
            return list.size();
        }
    }

    public static void main(String[] args) {
        System.out.println("☕ Java 09: Generics & Type Safety (Musterlösung)");
        System.out.println("-------------------------------------------------");

        Box<String> stringBox = new Box<>("Enterprise Java 21");
        System.out.println("Box Inhalt: " + stringBox.getContent());

        GenericCache<String, Integer> cache = new GenericCache<>();
        cache.put("User_101", 42);
        System.out.println("Cache Größe: " + cache.size());

        List<Integer> zahlen = List.of(12, 45, 7, 89, 23);
        System.out.println("Maximum: " + GenericsMath.findMax(zahlen));
        System.out.println("Summe: " + GenericsMath.calculateSum(zahlen));
    }
}
