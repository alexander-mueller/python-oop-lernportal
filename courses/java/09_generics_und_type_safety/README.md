# ☕ Java 09: Generics & Type Safety

Willkommen zu **Lehrpfad 3: Generics, Collections & Modern Streams**.
In diesem Modul meisterst du das statische Typsystem von Java auf Enterprise-Niveau: Generische Klassen, Methoden, Typschranken (Bounded Generics) und Wildcards.

---

## 🧭 1. Warum Generics?
Vor Java 5 basierten Datenstrukturen auf `Object`. Das erforderte manuelle Type-Casts und führte häufig zu `ClassCastException` zur Laufzeit:

```java
// ❌ Veraltet (Java 1.4): Unsafe & fehleranfällig
List list = new ArrayList();
list.add("Hallo");
Integer i = (Integer) list.get(0); // 💥 Laufzeitfehler: ClassCastException!

// ✅ Modern & Type-Safe (Java 5+ / 21+):
List<String> list = new ArrayList<>();
list.add("Hallo");
// list.add(42); // 🛑 Compile-Time Error – sofort vom Compiler verhindert!
```

---

## 📦 2. Generische Klassen & Bounded Types

### Generische Klasse `Box<T>`
```java
public class Box<T> {
    private T content;

    public Box(T content) {
        this.content = content;
    }

    public T getContent() {
        return content;
    }
}
```

### Bounded Type Parameters (`<T extends Comparable<T>>`)
Wenn Methoden auf Fähigkeiten des Typs angewiesen sind (z.B. Vergleiche oder mathematische Operationen):

```java
// T muss das Interface Comparable implementieren
public static <T extends Comparable<T>> T findMax(List<T> items) {
    T max = items.get(0);
    for (T item : items) {
        if (item.compareTo(max) > 0) {
            max = item;
        }
    }
    return max;
}

// N muss von Number erben (Integer, Double, BigDecimal, etc.)
public static <N extends Number> double calculateSum(List<N> numbers) {
    double sum = 0.0;
    for (N num : numbers) {
        sum += num.doubleValue();
    }
    return sum;
}
```

---

## 🛡️ 3. Wildcards & das PECS-Prinzip

Das **PECS-Prinzip** (*Producer Extends, Consumer Super*) ist die goldene Regel für generische Methoden:
- **`? extends T` (Producer):** Wenn du aus einer Liste nur **liest** (sie produziert Daten vom Typ `T`).
- **`? super T` (Consumer):** Wenn du in eine Liste nur **schreibst** (sie konsumiert Daten vom Typ `T`).

```java
public static <T> void copy(List<? extends T> src, List<? super T> dest) {
    for (T item : src) {
        dest.add(item);
    }
}
```

---

## 🎯 Aufgabenübersicht (`Aufgabe.java`)

1. **TODO 1:** `Box<T>` implementieren (Kapselung, Getter/Setter, `isEmpty()`, `toOptional()`).
2. **TODO 2:** `GenericCache<K, V>` als typsicheren Key-Value-Cache erstellen.
3. **TODO 3:** `GenericsMath` mit `findMax(...)` und `calculateSum(...)` unter Verwendung von Bounded Generics umsetzen.
4. **TODO 4:** `WildcardUtils` mit `copyList(...)` (PECS) und `countElements(...)` fertigstellen.
