#include <iostream>
#include <vector>
#include <string>
#include <cassert>
#include <cmath>
#include <sstream>
#include "aufgabe.cpp"

// ============================================================================
// 🧪 GOOGLETEST SUITE: C++ 09 - TEMPLATES & GENERISCHE PROGRAMMIERUNG
// ============================================================================

#ifndef TEST
#define TEST(Suite, Name) void Suite##_##Name()
#define EXPECT_EQ(a, b) assert((a) == (b))
#define EXPECT_TRUE(a) assert(a)
#define EXPECT_FALSE(a) assert(!(a))
#define EXPECT_NEAR(a, b, eps) assert(std::fabs((a) - (b)) <= (eps))
#define EXPECT_THROW(stmt, ex_type) \
    try { stmt; assert(false && "Expected exception not thrown"); } \
    catch (const ex_type&) {} \
    catch (...) { assert(false && "Wrong exception type thrown"); }
#endif

// TEST: Teilziel 1 - clamp_value Function Template
TEST(Cpp09Templates, ClampValueFunctionTemplate) {
    EXPECT_EQ(cpp09::clamp_value(5, 0, 10), 5);
    EXPECT_EQ(cpp09::clamp_value(-5, 0, 10), 0);
    EXPECT_EQ(cpp09::clamp_value(25, 0, 10), 10);
    EXPECT_NEAR(cpp09::clamp_value(3.14, 0.0, 2.5), 2.5, 0.0001);
    EXPECT_NEAR(cpp09::clamp_value(-1.5, -1.0, 5.0), -1.0, 0.0001);
}

// TEST: Teilziel 2 - Vector3D Class Template
TEST(Cpp09Templates, Vector3DClassTemplate) {
    cpp09::Vector3D<int> a(1, 2, 3);
    cpp09::Vector3D<int> b(4, 5, 6);
    auto sum = a + b;
    EXPECT_EQ(sum.x, 5);
    EXPECT_EQ(sum.y, 7);
    EXPECT_EQ(sum.z, 9);

    auto scaled = a * 3;
    EXPECT_EQ(scaled.x, 3);
    EXPECT_EQ(scaled.y, 6);
    EXPECT_EQ(scaled.z, 9);

    int dot = a.dot_product(b);
    EXPECT_EQ(dot, 1*4 + 2*5 + 3*6); // 4 + 10 + 18 = 32

    EXPECT_EQ(a.length_squared(), 1 + 4 + 9); // 14
}

// TEST: Teilziel 3 - FixedRingBuffer NTTP
TEST(Cpp09Templates, FixedRingBufferNTTP) {
    cpp09::FixedRingBuffer<int, 3> ring;
    EXPECT_TRUE(ring.is_empty());
    EXPECT_FALSE(ring.is_full());
    EXPECT_EQ(ring.size(), 0);
    EXPECT_EQ(ring.capacity(), 3);

    EXPECT_TRUE(ring.push(10));
    EXPECT_TRUE(ring.push(20));
    EXPECT_TRUE(ring.push(30));
    EXPECT_FALSE(ring.push(40)); // Voll
    EXPECT_TRUE(ring.is_full());
    EXPECT_EQ(ring.size(), 3);

    EXPECT_EQ(ring.pop(), 10);
    EXPECT_EQ(ring.pop(), 20);
    EXPECT_EQ(ring.size(), 1);
    EXPECT_TRUE(ring.push(99));
    EXPECT_EQ(ring.pop(), 30);
    EXPECT_EQ(ring.pop(), 99);
    EXPECT_TRUE(ring.is_empty());

    EXPECT_THROW(ring.pop(), std::underflow_error);
}

// TEST: Teilziel 4 - Template Specialization
TEST(Cpp09Templates, SerializerSpecialization) {
    EXPECT_EQ(cpp09::Serializer<int>::serialize(42), "generic: 42");
    EXPECT_EQ(cpp09::Serializer<std::string>::serialize("Systems"), "string: \"Systems\"");
    EXPECT_EQ(cpp09::Serializer<bool>::serialize(true), "bool: true");
    EXPECT_EQ(cpp09::Serializer<bool>::serialize(false), "bool: false");
}

// TEST: Teilziel 5 - Generic Transformation Algorithm
TEST(Cpp09Templates, ApplyTransformAlgorithm) {
    std::vector<int> numbers = {1, 2, 3, 4, 5};
    auto squares = cpp09::apply_transform(numbers, [](int x) { return x * x; });
    std::vector<int> expected_squares = {1, 4, 9, 16, 25};
    EXPECT_EQ(squares, expected_squares);

    auto stringified = cpp09::apply_transform(numbers, [](int x) { return "Val: " + std::to_string(x); });
    EXPECT_EQ(stringified.size(), 5);
    EXPECT_EQ(stringified[0], "Val: 1");
    EXPECT_EQ(stringified[4], "Val: 5");
}

#ifndef RUN_AS_GTEST_MAIN
int main() {
    std::cout << "[ RUN      ] CppTestSuite.TestCase_1 (ClampValueFunctionTemplate)\n";
    Cpp09Templates_ClampValueFunctionTemplate();
    std::cout << "[       OK ] CppTestSuite.TestCase_1\n";

    std::cout << "[ RUN      ] CppTestSuite.TestCase_2 (Vector3DClassTemplate)\n";
    Cpp09Templates_Vector3DClassTemplate();
    std::cout << "[       OK ] CppTestSuite.TestCase_2\n";

    std::cout << "[ RUN      ] CppTestSuite.TestCase_3 (FixedRingBufferNTTP)\n";
    Cpp09Templates_FixedRingBufferNTTP();
    std::cout << "[       OK ] CppTestSuite.TestCase_3\n";

    std::cout << "[ RUN      ] CppTestSuite.TestCase_4 (SerializerSpecialization)\n";
    Cpp09Templates_SerializerSpecialization();
    std::cout << "[       OK ] CppTestSuite.TestCase_4\n";

    std::cout << "[ RUN      ] CppTestSuite.TestCase_5 (ApplyTransformAlgorithm)\n";
    Cpp09Templates_ApplyTransformAlgorithm();
    std::cout << "[       OK ] CppTestSuite.TestCase_5\n";

    std::cout << "\n[  PASSED  ] 5 tests passed successfully!\n";
    return 0;
}
#endif
