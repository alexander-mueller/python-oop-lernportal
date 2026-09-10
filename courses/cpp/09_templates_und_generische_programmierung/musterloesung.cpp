#include <iostream>
#include <vector>
#include <string>
#include <stdexcept>
#include <cstddef>
#include <cmath>

namespace cpp09 {

// 🎯 TODO 1: Function Template clamp_value
template <typename T>
T clamp_value(T val, T min_val, T max_val) {
    if (val < min_val) return min_val;
    if (val > max_val) return max_val;
    return val;
}

// 🎯 TODO 2: Class Template Vector3D<T>
template <typename T>
struct Vector3D {
    T x{0};
    T y{0};
    T z{0};

    Vector3D() = default;
    Vector3D(T x_val, T y_val, T z_val) : x(x_val), y(y_val), z(z_val) {}

    Vector3D<T> operator+(const Vector3D<T>& other) const {
        return Vector3D<T>(x + other.x, y + other.y, z + other.z);
    }

    Vector3D<T> operator*(T scalar) const {
        return Vector3D<T>(x * scalar, y * scalar, z * scalar);
    }

    T dot_product(const Vector3D<T>& other) const {
        return (x * other.x) + (y * other.y) + (z * other.z);
    }

    T length_squared() const {
        return (x * x) + (y * y) + (z * z);
    }

    bool operator==(const Vector3D<T>& other) const {
        return x == other.x && y == other.y && z == other.z;
    }
};

// 🎯 TODO 3: Class Template FixedRingBuffer<T, Capacity> mit NTTP
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
        if (is_full()) {
            return false;
        }
        data_[tail_] = item;
        tail_ = (tail_ + 1) % Capacity;
        ++count_;
        return true;
    }

    T pop() {
        if (is_empty()) {
            throw std::underflow_error("Buffer is empty");
        }
        T item = data_[head_];
        head_ = (head_ + 1) % Capacity;
        --count_;
        return item;
    }

    [[nodiscard]] std::size_t size() const {
        return count_;
    }

    [[nodiscard]] std::size_t capacity() const {
        return Capacity;
    }

    [[nodiscard]] bool is_full() const {
        return count_ == Capacity;
    }

    [[nodiscard]] bool is_empty() const {
        return count_ == 0;
    }
};

// 🎯 TODO 4: Template Specialization - Serializer<T>
template <typename T>
struct Serializer {
    static std::string serialize(const T& val) {
        return "generic: " + std::to_string(val);
    }
};

template <>
struct Serializer<std::string> {
    static std::string serialize(const std::string& val) {
        return "string: \"" + val + "\"";
    }
};

template <>
struct Serializer<bool> {
    static std::string serialize(const bool& val) {
        return std::string("bool: ") + (val ? "true" : "false");
    }
};

// 🎯 TODO 5: Higher-Order Generic Algorithm - apply_transform
template <typename T, typename Func>
auto apply_transform(const std::vector<T>& input, Func func) {
    using ResultType = decltype(func(std::declval<T>()));
    std::vector<ResultType> result;
    result.reserve(input.size());
    for (const auto& item : input) {
        result.push_back(func(item));
    }
    return result;
}

} // namespace cpp09

int main() {
    std::cout << "=== C++ 09: Musterlösung ===" << std::endl;
    int c = cpp09::clamp_value(15, 0, 10);
    std::cout << "clamp_value(15, 0, 10) = " << c << std::endl;

    cpp09::Vector3D<float> v1(1.0f, 2.0f, 3.0f);
    cpp09::Vector3D<float> v2(4.0f, 5.0f, 6.0f);
    auto v3 = v1 + v2;
    std::cout << "v3: (" << v3.x << ", " << v3.y << ", " << v3.z << ")\n";

    cpp09::FixedRingBuffer<int, 3> ring;
    ring.push(10);
    ring.push(20);
    ring.push(30);
    std::cout << "Ring full? " << (ring.is_full() ? "true" : "false") << "\n";
    std::cout << "Pop: " << ring.pop() << "\n";

    std::cout << cpp09::Serializer<int>::serialize(42) << "\n";
    std::cout << cpp09::Serializer<std::string>::serialize("Hello C++20") << "\n";
    std::cout << cpp09::Serializer<bool>::serialize(true) << "\n";

    return 0;
}
