# C++ 12: Lambdas, Structured Binding & std::optional

In diesem Modul erforschst du die modernen Ausdrucksmittel von C++20: Funktionale Programmierung mit **Lambdas**, Typsicherheit durch **`std::optional`** und elegantes Entpacken mit **Structured Binding**.

---

## 🎯 Lernziele
1. **Lambda Expressions**: Syntax `[capture](params) -> ret { body }` sicher beherrschen.
2. **Capture Semantics**: Unterschied zwischen Wert- (`[=]`), Referenz- (`[&]`) und selektivem Capture verstehen.
3. **Structured Binding**: Daten aus Tuples, Pairs und Structs ohne Boilerplate entpacken (`auto [a, b]`).
4. **Fehlersicherheit**: `std::optional<T>` für abwesende Werte nutzen (`has_value()`, `value_or()`).
5. **Event Callbacks**: Ereignisverarbeitung mit `std::function` und generischen Lambdas.

---

## 💡 Schlüsselkonzepte

### 1. Lambda-Funktionen & Closures
```cpp
int factor = 3;
auto multiply = [factor](int x) { return x * factor; };
```

### 2. Structured Binding
```cpp
struct Point { double x; double y; };
Point p{10.5, 20.0};
auto [px, py] = p; // px = 10.5, py = 20.0
```

### 3. Safe Querying mit `std::optional`
```cpp
std::optional<int> safe_divide(int a, int b) {
    if (b == 0) return std::nullopt;
    return a / b;
}
```

---

## 🚀 Aufgaben in `aufgabe.cpp`
- [ ] **TODO 1**: `find_user_by_id` mit `std::optional<User>`
- [ ] **TODO 2**: `unpack_metric_pair` mit Structured Binding
- [ ] **TODO 3**: Stateful Counting Lambda
- [ ] **TODO 4**: `EventDispatcher` mit `std::function`
- [ ] **TODO 5**: `process_pipeline` mit Lambda-Transformationen
