#include <iostream>
#include <vector>
#include <string>
#include <stdexcept>
#include <cstddef>
#include <cmath>

namespace cpp09 {

// ============================================================================
// 🎯 TODO 1: Function Template clamp_value
// Begrenzt einen Wert 'val' auf den Bereich zwischen 'min_val' und 'max_val'.
// Falls val < min_val: gib min_val zurück.
// Falls val > max_val: gib max_val zurück.
// Sonst: gib val zurück.
// ============================================================================
template <typename T>
T clamp_value(T val, T min_val, T max_val) {
    // TODO 1: Implementiere die generische Begrenzungsfunktion
    return val;
}

// ============================================================================
// 🎯 TODO 2: Class Template Vector3D<T>
// Generischer 3D-Vektor mit Komponenten x, y, z vom Typ T.
// Methoden / Operatoren:
// - Konstruktor Vector3D(T x, T y, T z)
// - operator+ (Vektoraddition: addiert korrespondierende Komponenten)
// - operator* (Skalarmultiplikation mit Faktor T: multipliziert jede Komponente)
// - dot_product(const Vector3D<T>& other) const -> Berechnet das Skalarprodukt (x1*x2 + y1*y2 + z1*z2)
// - length_squared() const -> x*x + y*y + z*z
// ============================================================================
template <typename T>
struct Vector3D {
    T x{0};
    T y{0};
    T z{0};

    Vector3D() = default;
    Vector3D(T x_val, T y_val, T z_val) : x(x_val), y(y_val), z(z_val) {}

    Vector3D<T> operator+(const Vector3D<T>& other) const {
        // TODO 2a: Vektor-Addition
        return *this;
    }

    Vector3D<T> operator*(T scalar) const {
        // TODO 2b: Skalar-Multiplikation
        return *this;
    }

    T dot_product(const Vector3D<T>& other) const {
        // TODO 2c: Skalarprodukt berechnen
        return T{0};
    }

    T length_squared() const {
        // TODO 2d: Quadratische Länge (x*x + y*y + z*z)
        return T{0};
    }

    bool operator==(const Vector3D<T>& other) const {
        return x == other.x && y == other.y && z == other.z;
    }
};

// ============================================================================
// 🎯 TODO 3: Class Template FixedRingBuffer<T, Capacity> mit NTTP
// Implementiere einen Ringpuffer mit fester Compile-Zeit-Kapazität 'Capacity'.
// Methoden:
// - bool push(const T& item): Fügt item hinzu. Gibt true zurück, wenn erfolgreich.
//                             Gibt false zurück, wenn der Puffer voll ist (size == Capacity).
// - T pop(): Entfernt das älteste Element und gibt es zurück.
//            Wirft std::underflow_error("Buffer is empty"), falls der Puffer leer ist.
// - std::size_t size() const: Gibt aktuelle Anzahl der Elemente zurück.
// - std::size_t capacity() const: Gibt Capacity zurück.
// - bool is_full() const: Gibt true zurück, wenn size == Capacity.
// - bool is_empty() const: Gibt true zurück, wenn size == 0.
// ============================================================================
template <typename T, std::size_t Capacity>
class FixedRingBuffer {
private:
    T data_[Capacity]{};
    std::size_t head_{0};
    std::size_t tail_{0};
    std::size_t count_{0};

public:
    FixedRingBuffer() = default;

    bool push(const T& item) {
        // TODO 3a: Element am Tail einfügen falls nicht voll
        return false;
    }

    T pop() {
        // TODO 3b: Ältestes Element am Head entfernen und zurückgeben
        if (is_empty()) {
            throw std::underflow_error("Buffer is empty");
        }
        return data_[0];
    }

    [[nodiscard]] std::size_t size() const {
        // TODO 3c: Anzahl der Elemente
        return 0;
    }

    [[nodiscard]] std::size_t capacity() const {
        return Capacity;
    }

    [[nodiscard]] bool is_full() const {
        return size() == Capacity;
    }

    [[nodiscard]] bool is_empty() const {
        return size() == 0;
    }
};

// ============================================================================
// 🎯 TODO 4: Template Specialization - Serializer<T>
// - Primärtemplate: static std::string serialize(const T& val) -> "generic: " + std::to_string(val)
// - Spezialisierung für std::string: static std::string serialize(const std::string& val) -> "string: \"" + val + "\""
// - Spezialisierung für bool: static std::string serialize(const bool& val) -> "bool: " + (val ? "true" : "false")
// ============================================================================
template <typename T>
struct Serializer {
    static std::string serialize(const T& val) {
        // TODO 4a: Primärtemplate
        return "";
    }
};

template <>
struct Serializer<std::string> {
    static std::string serialize(const std::string& val) {
        // TODO 4b: Spezialisierung für std::string
        return "";
    }
};

template <>
struct Serializer<bool> {
    static std::string serialize(const bool& val) {
        // TODO 4c: Spezialisierung für bool
        return "";
    }
};

// ============================================================================
// 🎯 TODO 5: Higher-Order Generic Algorithm - apply_transform
// Wendet ein Funktionsobjekt / Lambda 'func' auf jedes Element von 'input' an
// und gibt einen neuen std::vector mit den transformierten Resultaten zurück.
// ============================================================================
template <typename T, typename Func>
auto apply_transform(const std::vector<T>& input, Func func) {
    using ResultType = decltype(func(std::declval<T>()));
    std::vector<ResultType> result;
    // TODO 5: Vektor transformieren und befüllen
    return result;
}

} // namespace cpp09

int main() {
    std::cout << "=== C++ 09: Templates & Generische Programmierung ===" << std::endl;
    int c = cpp09::clamp_value(15, 0, 10);
    std::cout << "clamp_value(15, 0, 10) = " << c << std::endl;
    return 0;
}
