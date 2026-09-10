# ☕ Java 10: Collections Framework (List, Set, Map)

Das **Java Collections Framework (JCF)** ist das Rückgrat professioneller Datenverarbeitung in Java. In diesem Modul lernst du die Kerninterfaces `List`, `Set` und `Map`, deren typische Implementierungen sowie den fundamentalen `equals()`/`hashCode()`-Vertrag kennen.

---

## 🗺️ 1. Die Collection-Hierarchie

```
                  Iterable<T>
                      ▲
                  Collection<T>
         ┌────────────┼────────────┐
       List<T>      Set<T>      Queue<T>
     (geordnet)  (eindeutig)     (FIFO)
         │            │
   ┌─────┴─────┐  ┌───┴───┐
ArrayList  LinkedList  HashSet TreeSet
```
*(Hinweis: `Map<K, V>` ist ein eigenständiges Interface, das Schlüssel-Wert-Paare speichert).*

---

## ⚡ 2. Wann welche Collection wählen?

| Collection | Typischer Einsatz | Zugriffszeit ($O$) | Sortiert? | Duplikate? |
| :--- | :--- | :--- | :--- | :--- |
| **`ArrayList<T>`** | Standard-Liste, Indexzugriff | $O(1)$ Lesen, $O(n)$ Einfügen Mitte | Einfügereihenfolge | Ja |
| **`LinkedList<T>`** | Queue/Deque, häufiges Einfügen | $O(n)$ Index, $O(1)$ Kopf/Ende | Einfügereihenfolge | Ja |
| **`HashSet<T>`** | Schnelle Eindeutigkeitsprüfung | $O(1)$ Lookup / Insert | Nein (Hash-Bucket) | Nein |
| **`TreeSet<T>`** | Sortierte Mengen (Natural Order) | $O(\log n)$ (Rot-Schwarz-Baum) | Ja (`Comparable`) | Nein |
| **`HashMap<K,V>`** | Standard Key-Value Cache/Lookup | $O(1)$ Lookup / Insert | Nein | Keys eindeutig |
| **`TreeMap<K,V>`** | Sortierte Keys / Range Queries | $O(\log n)$ | Ja nach Key | Keys eindeutig |

---

## 🔑 3. Der equals() & hashCode() Vertrag

Damit Objekte in `HashSet` oder als Keys in `HashMap` korrekt gefunden werden, gilt:
1. Wenn `a.equals(b) == true`, dann **MUSS** `a.hashCode() == b.hashCode()`.
2. Wer `equals()` überschreibt, **MUSS** auch `hashCode()` überschreiben.
3. In Java 16+ Records (`record Product(...)`) generiert der Compiler dies automatisch und fehlerfrei!

---

## 🎯 Aufgabenübersicht (`Aufgabe.java`)

1. **TODO 1:** `ProductCatalog` mit `ArrayList<Product>` (Filterung nach Kategorie, SKU-Löschung per Iterator, Preis-Sortierung).
2. **TODO 2:** `TagManager` mit `HashSet` für schnellen Lookup und `TreeSet` für alphabetische Ausgabe.
3. **TODO 3:** `InventoryStats` mit Map-Aggregationen (`countProductsByCategory` via `Map.merge()` und `groupByCategory` via `computeIfAbsent()`).
