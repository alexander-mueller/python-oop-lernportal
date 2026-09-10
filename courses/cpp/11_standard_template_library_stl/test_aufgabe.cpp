#include <iostream>
#include <vector>
#include <string>
#include <cassert>
#include <cmath>
#include "aufgabe.cpp"

// ============================================================================
// 🧪 GOOGLETEST SUITE: C++ 11 - STANDARD TEMPLATE LIBRARY (STL)
// ============================================================================

#ifndef TEST
#define TEST(Suite, Name) void Suite##_##Name()
#define EXPECT_EQ(a, b) assert((a) == (b))
#define EXPECT_NE(a, b) assert((a) != (b))
#define EXPECT_TRUE(a) assert(a)
#define EXPECT_FALSE(a) assert(!(a))
#define EXPECT_NEAR(a, b, eps) assert(std::fabs((a) - (b)) <= (eps))
#define EXPECT_THROW(stmt, ex_type) \
    try { stmt; assert(false && "Expected exception not thrown"); } \
    catch (const ex_type&) {} \
    catch (...) { assert(false && "Wrong exception type thrown"); }
#endif

// TEST: Teilziel 1 - InventorySystem with unordered_map
TEST(Cpp11STL, InventorySystemMap) {
    cpp11::InventorySystem inv;
    EXPECT_EQ(inv.item_count(), 0);
    EXPECT_EQ(inv.get_stock("HealthPotion"), 0);

    inv.add_item("HealthPotion", 5);
    inv.add_item("HealthPotion", 3);
    inv.add_item("ManaPotion", 10);

    EXPECT_EQ(inv.item_count(), 2);
    EXPECT_EQ(inv.get_stock("HealthPotion"), 8);
    EXPECT_EQ(inv.get_stock("ManaPotion"), 10);

    EXPECT_TRUE(inv.remove_item("HealthPotion", 4));
    EXPECT_EQ(inv.get_stock("HealthPotion"), 4);

    EXPECT_FALSE(inv.remove_item("HealthPotion", 10)); // Nicht genug
    EXPECT_EQ(inv.get_stock("HealthPotion"), 4);

    EXPECT_FALSE(inv.remove_item("NonExistent", 1));
}

// TEST: Teilziel 2 - Leaderboard Filtering and Sorting
TEST(Cpp11STL, FilterAndSortLeaderboard) {
    std::vector<cpp11::PlayerRecord> records = {
        {"Alice", 250},
        {"Bob", 400},
        {"Charlie", 150},
        {"Dave", 400},
        {"Eve", 300}
    };

    auto top_players = cpp11::filter_and_sort_leaderboard(records, 250);
    EXPECT_EQ(top_players.size(), 4); // Bob, Dave, Eve, Alice

    EXPECT_EQ(top_players[0].name, "Bob");     // 400, 'B' < 'D'
    EXPECT_EQ(top_players[0].score, 400);
    EXPECT_EQ(top_players[1].name, "Dave");    // 400
    EXPECT_EQ(top_players[1].score, 400);
    EXPECT_EQ(top_players[2].name, "Eve");     // 300
    EXPECT_EQ(top_players[2].score, 300);
    EXPECT_EQ(top_players[3].name, "Alice");   // 250
    EXPECT_EQ(top_players[3].score, 250);
}

// TEST: Teilziel 3 - Telemetry Stats Calculation
TEST(Cpp11STL, CalculateTelemetryStats) {
    std::vector<double> readings = {10.0, 20.0, 5.0, 35.0, 30.0};
    auto stats = cpp11::calculate_telemetry_stats(readings);

    EXPECT_NEAR(stats.min_val, 5.0, 0.001);
    EXPECT_NEAR(stats.max_val, 35.0, 0.001);
    EXPECT_NEAR(stats.total, 100.0, 0.001);
    EXPECT_NEAR(stats.average, 20.0, 0.001);

    std::vector<double> empty;
    EXPECT_THROW(cpp11::calculate_telemetry_stats(empty), std::invalid_argument);
}

// TEST: Teilziel 4 - Unique Tag Extraction
TEST(Cpp11STL, ExtractUniqueSortedTags) {
    std::vector<std::vector<std::string>> doc_tags = {
        {"cpp", "systems", "memory"},
        {"c", "systems", "lowlevel"},
        {"cpp", "stl", "algorithms"}
    };

    auto tags = cpp11::extract_unique_sorted_tags(doc_tags);
    EXPECT_EQ(tags.size(), 6); // algorithms, c, cpp, lowlevel, memory, systems
    EXPECT_TRUE(tags.count("cpp") > 0);
    EXPECT_TRUE(tags.count("systems") > 0);
    EXPECT_TRUE(tags.count("unknown") == 0);

    // Erste alphabetische Position prüfen
    EXPECT_EQ(*tags.begin(), "algorithms");
}

// TEST: Teilziel 5 - Normalizing Sensor Data
TEST(Cpp11STL, NormalizeSensorData) {
    std::vector<double> raw = {10.0, 20.0, 30.0, 40.0, 50.0};
    auto norm = cpp11::normalize_sensor_data(raw);

    EXPECT_EQ(norm.size(), 5);
    EXPECT_NEAR(norm[0], 0.0, 0.001);
    EXPECT_NEAR(norm[2], 0.5, 0.001);
    EXPECT_NEAR(norm[4], 1.0, 0.001);

    std::vector<double> flat = {5.0, 5.0, 5.0};
    auto flat_norm = cpp11::normalize_sensor_data(flat);
    EXPECT_NEAR(flat_norm[0], 0.0, 0.001);
}

#ifndef RUN_AS_GTEST_MAIN
int main() {
    std::cout << "[ RUN      ] CppTestSuite.TestCase_1 (InventorySystemMap)\n";
    Cpp11STL_InventorySystemMap();
    std::cout << "[       OK ] CppTestSuite.TestCase_1\n";

    std::cout << "[ RUN      ] CppTestSuite.TestCase_2 (FilterAndSortLeaderboard)\n";
    Cpp11STL_FilterAndSortLeaderboard();
    std::cout << "[       OK ] CppTestSuite.TestCase_2\n";

    std::cout << "[ RUN      ] CppTestSuite.TestCase_3 (CalculateTelemetryStats)\n";
    Cpp11STL_CalculateTelemetryStats();
    std::cout << "[       OK ] CppTestSuite.TestCase_3\n";

    std::cout << "[ RUN      ] CppTestSuite.TestCase_4 (ExtractUniqueSortedTags)\n";
    Cpp11STL_ExtractUniqueSortedTags();
    std::cout << "[       OK ] CppTestSuite.TestCase_4\n";

    std::cout << "[ RUN      ] CppTestSuite.TestCase_5 (NormalizeSensorData)\n";
    Cpp11STL_NormalizeSensorData();
    std::cout << "[       OK ] CppTestSuite.TestCase_5\n";

    std::cout << "\n[  PASSED  ] 5 tests passed successfully!\n";
    return 0;
}
#endif
