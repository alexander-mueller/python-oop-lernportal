# C++ 11: Standard Template Library (STL)

Die **Standard Template Library (STL)** ist das Herzstück moderner C++ Entwicklung. Sie bietet hochgradig optimierte Datenstrukturen und Algorithmen für Systems Engineering und Performance-Anwendungen.

---

## 🎯 Lernziele
1. **STL-Container**: `std::vector`, `std::unordered_map` und `std::set` passend zu den Zugriffsanforderungen einsetzen.
2. **STL-Algorithmen**: Komplexe Schleifen durch `std::sort`, `std::copy_if`, `std::transform` und `std::accumulate` ersetzen.
3. **Iteratoren & Custom Comparator**: Flexible Sortierkriterien mit Lambdas formulieren.
4. **Deduplizierung & Aggregation**: Eindeutige Mengen bilden und Telemetriewerte effizient aggregieren.
5. **Memory Reserve**: Performance optimieren durch Vermeidung unnötiger Heap-Reallokationen.

---

## 💡 Schlüsselkonzepte

### 1. `std::unordered_map`
```cpp
std::unordered_map<std::string, int> inventory;
inventory["potion"] += 5; // Erstellt oder inkrementiert O(1)
if (auto it = inventory.find("potion"); it != inventory.end()) {
    std::cout << "Menge: " << it->second << std::endl;
}
```

### 2. STL Algorithmen (`<algorithm>`, `<numeric>`)
```cpp
// Sortieren
std::sort(vec.begin(), vec.end(), [](const Item& a, const Item& b) {
    return a.score > b.score;
});

// Minimum / Maximum
auto min_it = std::min_element(vec.begin(), vec.end());

// Summe
double total = std::accumulate(vec.begin(), vec.end(), 0.0);
```

---

## 🚀 Aufgaben in `aufgabe.cpp`
- [ ] **TODO 1**: `InventorySystem` mit `std::unordered_map`
- [ ] **TODO 2**: `filter_and_sort_leaderboard` mit `std::copy_if` & `std::sort`
- [ ] **TODO 3**: `calculate_telemetry_stats` mit `min_element`, `max_element`, `accumulate`
- [ ] **TODO 4**: `extract_unique_sorted_tags` mit `std::set`
- [ ] **TODO 5**: `normalize_sensor_data` mit `std::transform`
