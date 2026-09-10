package java_course.module09;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import java.util.Optional;

/**
 * ☕ JAVA 09: GENERICS & TYPE SAFETY
 * ==================================
 * In diesem Modul lernst du die Grundlagen und fortgeschrittenen Konzepte
 * generischer Typen in Java kennen: Typparameter <T>, Bounded Generics <T extends Comparable<T>>,
 * Wildcards (<? extends T>, <? super T>) und das PECS-Prinzip.
 */
public class Aufgabe {

    // ========================================================================
    // 🎯 TODO 1: Generische Container-Klasse 'Box<T>'
    // ========================================================================
    // Implementiere eine generische Klasse Box<T>, die genau ein Element speichert.
    // Anforderungen:
    // 1. Privates Feld 'content' vom Typ T.
    // 2. Standardkonstruktor und Konstruktor mit Parameter 'T content'.
    // 3. Getter 'getContent()' und Setter 'setContent(T content)'.
    // 4. Methode 'boolean isEmpty()', die true zurückgibt, wenn content == null ist.
    // 5. Methode 'Optional<T> toOptional()', die Optional.ofNullable(content) liefert.
    public static class Box<T> {
        private T content;

        public Box() {
            // TODO: Initialisiere leere Box
        }

        public Box(T content) {
            // TODO: Initialisiere mit Inhalt
        }

        public T getContent() {
            // TODO: Rückgabe
            return null;
        }

        public void setContent(T content) {
            // TODO: Setze Inhalt
        }

        public boolean isEmpty() {
            // TODO: Prüfe ob content null ist
            return true;
        }

        public Optional<T> toOptional() {
            // TODO: Optional zurückgeben
            return Optional.empty();
        }
    }

    // ========================================================================
    // 🎯 TODO 2: Generischer Cache mit Schlüssel-Wert-Paaren 'GenericCache<K, V>'
    // ========================================================================
    // Implementiere einen Key-Value In-Memory Cache.
    // Anforderungen:
    // 1. Interne Listen oder Datenstrukturen für Schlüssel (List<K>) und Werte (List<V>)
    //    oder eine List von CacheEntry<K, V>.
    // 2. Methode 'void put(K key, V value)': Fügt das Paar hinzu oder überschreibt den Wert,
    //    falls der Schlüssel bereits existiert (Objects.equals).
    // 3. Methode 'Optional<V> get(K key)': Gibt den Wert als Optional zurück.
    // 4. Methode 'boolean containsKey(K key)'.
    // 5. Methode 'int size()': Anzahl der gespeicherten Einträge.
    // 6. Methode 'void clear()': Leert den Cache.
    public static class GenericCache<K, V> {
        private final List<K> keys = new ArrayList<>();
        private final List<V> values = new ArrayList<>();

        public void put(K key, V value) {
            // TODO: Einfügen oder Aktualisieren
        }

        public Optional<V> get(K key) {
            // TODO: Wert anhand von Schlüssel finden
            return Optional.empty();
        }

        public boolean containsKey(K key) {
            // TODO: Prüfen ob Schlüssel existiert
            return false;
        }

        public int size() {
            // TODO: Größe zurückgeben
            return 0;
        }

        public void clear() {
            // TODO: Cache leeren
        }
    }

    // ========================================================================
    // 🎯 TODO 3: Bounded Generics - Maximum & Statistik Finder
    // ========================================================================
    // Implementiere statische Hilfsmethoden mit Typ-Einschränkungen (Bounds).
    //
    // Anforderungen:
    // 1. 'public static <T extends Comparable<T>> T findMax(List<T> items)'
    //    - Findet das größte Element in der Liste.
    //    - Wirft IllegalArgumentException, wenn die Liste null oder leer ist.
    //
    // 2. 'public static <N extends Number> double calculateSum(List<N> numbers)'
    //    - Berechnet die Summe aller Zahlen als double (nutze n.doubleValue()).
    //    - Gibt 0.0 zurück, wenn die Liste null oder leer ist.
    public static class GenericsMath {

        public static <T extends Comparable<T>> T findMax(List<T> items) {
            // TODO: Größtes Element finden mit compareTo
            return null;
        }

        public static <N extends Number> double calculateSum(List<N> numbers) {
            // TODO: Summe berechnen via doubleValue()
            return 0.0;
        }
    }

    // ========================================================================
    // 🎯 TODO 4: Wildcards & PECS-Prinzip (Producer Extends, Consumer Super)
    // ========================================================================
    // Implementiere Hilfsmethoden mit Wildcards für flexible Sammlungen.
    //
    // Anforderungen:
    // 1. 'public static <T> void copyList(List<? extends T> src, List<? super T> dest)'
    //    - Kopiert alle Elemente aus 'src' (Producer -> ? extends T) in 'dest' (Consumer -> ? super T).
    //
    // 2. 'public static int countElements(List<?> list)'
    //    - Zählt die Anzahl der Elemente einer beliebigen Liste (Unbounded Wildcard).
    //    - Gibt 0 zurück bei null.
    public static class WildcardUtils {

        public static <T> void copyList(List<? extends T> src, List<? super T> dest) {
            // TODO: Elemente aus src in dest übertragen (PECS)
        }

        public static int countElements(List<?> list) {
            // TODO: Anzahl der Elemente zählen
            return 0;
        }
    }

    public static void main(String[] args) {
        System.out.println("☕ Java 09: Generics & Type Safety");
        System.out.println("----------------------------------");

        // Test Box
        Box<String> stringBox = new Box<>("Enterprise Java 21");
        System.out.println("Box Inhalt: " + stringBox.getContent());

        // Test Cache
        GenericCache<String, Integer> cache = new GenericCache<>();
        cache.put("User_101", 42);
        System.out.println("Cache Größe: " + cache.size());

        // Test Bounded Generics
        List<Integer> zahlen = List.of(12, 45, 7, 89, 23);
        System.out.println("Maximum: " + GenericsMath.findMax(zahlen));
        System.out.println("Summe: " + GenericsMath.calculateSum(zahlen));
    }
}
