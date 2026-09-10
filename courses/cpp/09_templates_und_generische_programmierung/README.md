# C++ 09: Function Templates & Class Templates

Willkommen in der Welt der **generischen Programmierung** in Modern C++20! In diesem Modul lernst du, wie du mithilfe von Templates hocheffizienten, typsicheren und wiederverwendbaren Code schreibst – ohne jeglichen Runtime-Overhead (Zero-Cost Abstraction).

---

## 🎯 Lernziele
1. **Function Templates**: Eigene Funktions-Templates mit `template<typename T>` definieren und anwenden.
2. **Class Templates**: Generische Datenstrukturen wie Vektoren und Container programmieren.
3. **Non-Type Template Parameters (NTTP)**: Compile-Zeit Konstanten wie Puffergrößen direkt in Template-Definitionen einbinden.
4. **Template-Spezialisierung**: Gezielte Sonderbehandlungen für ausgewählte Datentypen (z.B. `std::string` oder `bool`) formulieren.
5. **Generische Algorithmen**: Higher-Order-Funktionen schreiben, die beliebige Transformationsfunktionen (Funktoren, Lambdas) auf Vektoren anwenden.

---

## 💡 Schlüsselkonzepte

### 1. Function Templates
Anstatt separate Funktionen für `int`, `double` und `float` zu überladen, generiert der Compiler bei Bedarf die passende Spezialisierung:
```cpp
template <typename T>
T clamp_value(T val, T min_val, T max_val) {
    if (val < min_val) return min_val;
    if (val > max_val) return max_val;
    return val;
}
```

### 2. Class Templates & NTTP
```cpp
template <typename T, std::size_t Capacity>
class FixedRingBuffer {
private:
    T buffer_[Capacity];
    std::size_t head_{0};
    std::size_t tail_{0};
    std::size_t count_{0};
public:
    bool push(const T& item);
    T pop();
    [[nodiscard]] std::size_t size() const;
    [[nodiscard]] bool is_full() const;
};
```

### 3. Template-Spezialisierung
```cpp
template <typename T>
struct Serializer {
    static std::string serialize(const T& val) {
        return "generic: " + std::to_string(val);
    }
};

template <>
struct Serializer<std::string> {
    static std::string serialize(const std::string& val) {
        return "string: " + val;
    }
};
```

---

## 🚀 Aufgaben in `aufgabe.cpp`
- [ ] **TODO 1**: `clamp_value<T>` implementieren
- [ ] **TODO 2**: `Vector3D<T>` mit arithmetischen Operatoren & `dot_product()`
- [ ] **TODO 3**: `FixedRingBuffer<T, Capacity>` Ringpuffer mit NTTP
- [ ] **TODO 4**: `Serializer<T>` Primärtemplate + Spezialisierungen für `std::string` und `bool`
- [ ] **TODO 5**: `apply_transform(const std::vector<T>&, Func)` Higher-Order Template
