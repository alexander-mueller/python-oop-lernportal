#include <iostream>
#include <memory>
#include <string>
#include <cassert>
#include "aufgabe.cpp"

// ============================================================================
// 🧪 GOOGLETEST SUITE: C++ 10 - SMART POINTER & SPEICHERSICHERHEIT
// ============================================================================

#ifndef TEST
#define TEST(Suite, Name) void Suite##_##Name()
#define EXPECT_EQ(a, b) assert((a) == (b))
#define EXPECT_NE(a, b) assert((a) != (b))
#define EXPECT_TRUE(a) assert(a)
#define EXPECT_FALSE(a) assert(!(a))
#define EXPECT_THROW(stmt, ex_type) \
    try { stmt; assert(false && "Expected exception not thrown"); } \
    catch (const ex_type&) {} \
    catch (...) { assert(false && "Wrong exception type thrown"); }
#endif

// TEST: Teilziel 1 - create_unique_session
TEST(Cpp10SmartPointers, CreateUniqueSession) {
    auto session = cpp10::create_unique_session(101, "bob");
    EXPECT_NE(session, nullptr);
    EXPECT_EQ(session->id, 101);
    EXPECT_EQ(session->username, "bob");
}

// TEST: Teilziel 2 - SessionManager Ownership & Move
TEST(Cpp10SmartPointers, SessionManagerMoveOwnership) {
    cpp10::SessionManager mgr;
    EXPECT_EQ(mgr.count(), 0);

    auto s1 = cpp10::create_unique_session(1, "alice");
    auto s2 = cpp10::create_unique_session(2, "charlie");

    mgr.add_session(std::move(s1));
    EXPECT_EQ(s1, nullptr); // s1 wurde gemovt!
    EXPECT_EQ(mgr.count(), 1);

    mgr.add_session(std::move(s2));
    EXPECT_EQ(mgr.count(), 2);

    const auto* found = mgr.get_session(1);
    EXPECT_NE(found, nullptr);
    EXPECT_EQ(found->username, "alice");

    EXPECT_EQ(mgr.get_session(999), nullptr);

    auto extracted = mgr.extract_session(1);
    EXPECT_NE(extracted, nullptr);
    EXPECT_EQ(extracted->id, 1);
    EXPECT_EQ(mgr.count(), 1);
    EXPECT_EQ(mgr.get_session(1), nullptr);
}

// TEST: Teilziel 3 - SharedDocument and WeakObserver
TEST(Cpp10SmartPointers, SharedDocumentAndWeakObserver) {
    std::unique_ptr<cpp10::DocumentObserver> obs;
    {
        auto doc = std::make_shared<cpp10::Document>("SecurityWhitepaper", "Confidential text...");
        obs = std::make_unique<cpp10::DocumentObserver>(doc);
        EXPECT_TRUE(obs->is_valid());
        EXPECT_EQ(obs->read_title(), "SecurityWhitepaper");
    } // doc out of scope here!

    EXPECT_FALSE(obs->is_valid());
    EXPECT_THROW(obs->read_title(), std::runtime_error);
}

// TEST: Teilziel 4 - ResourceTracker RAII
TEST(Cpp10SmartPointers, ResourceTrackerRAII) {
    cpp10::ResourceTracker::active_count = 0;
    cpp10::ResourceTracker::total_created = 0;

    {
        auto r1 = std::make_unique<cpp10::ResourceTracker>(1);
        auto r2 = std::make_shared<cpp10::ResourceTracker>(2);
        auto r3 = r2; // Shared copy
        EXPECT_EQ(cpp10::ResourceTracker::active_count, 2);
        EXPECT_EQ(cpp10::ResourceTracker::total_created, 2);
    } // Alle Ressourcen zerstört

    EXPECT_EQ(cpp10::ResourceTracker::active_count, 0);
    EXPECT_EQ(cpp10::ResourceTracker::total_created, 2);
}

// TEST: Teilziel 5 - Custom Deleter SafeBuffer
TEST(Cpp10SmartPointers, SafeBufferCustomDeleter) {
    bool was_freed = false;
    {
        auto buf = cpp10::create_monitored_buffer(512, &was_freed);
        EXPECT_FALSE(was_freed);
        buf[0] = 0x42;
        EXPECT_EQ(buf[0], 0x42);
    } // buf leaves scope here
    EXPECT_TRUE(was_freed);
}

#ifndef RUN_AS_GTEST_MAIN
int main() {
    std::cout << "[ RUN      ] CppTestSuite.TestCase_1 (CreateUniqueSession)\n";
    Cpp10SmartPointers_CreateUniqueSession();
    std::cout << "[       OK ] CppTestSuite.TestCase_1\n";

    std::cout << "[ RUN      ] CppTestSuite.TestCase_2 (SessionManagerMoveOwnership)\n";
    Cpp10SmartPointers_SessionManagerMoveOwnership();
    std::cout << "[       OK ] CppTestSuite.TestCase_2\n";

    std::cout << "[ RUN      ] CppTestSuite.TestCase_3 (SharedDocumentAndWeakObserver)\n";
    Cpp10SmartPointers_SharedDocumentAndWeakObserver();
    std::cout << "[       OK ] CppTestSuite.TestCase_3\n";

    std::cout << "[ RUN      ] CppTestSuite.TestCase_4 (ResourceTrackerRAII)\n";
    Cpp10SmartPointers_ResourceTrackerRAII();
    std::cout << "[       OK ] CppTestSuite.TestCase_4\n";

    std::cout << "[ RUN      ] CppTestSuite.TestCase_5 (SafeBufferCustomDeleter)\n";
    Cpp10SmartPointers_SafeBufferCustomDeleter();
    std::cout << "[       OK ] CppTestSuite.TestCase_5\n";

    std::cout << "\n[  PASSED  ] 5 tests passed successfully!\n";
    return 0;
}
#endif
