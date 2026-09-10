#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <set>
#include <algorithm>
#include <numeric>
#include <stdexcept>
#include <cmath>

namespace cpp11 {

// 🎯 TODO 1: InventorySystem
class InventorySystem {
private:
    std::unordered_map<std::string, int> stock_;

public:
    void add_item(const std::string& name, int amount) {
        if (amount > 0) {
            stock_[name] += amount;
        }
    }

    bool remove_item(const std::string& name, int amount) {
        auto it = stock_.find(name);
        if (it != stock_.end() && it->second >= amount && amount > 0) {
            it->second -= amount;
            return true;
        }
        return false;
    }

    [[nodiscard]] int get_stock(const std::string& name) const {
        auto it = stock_.find(name);
        if (it != stock_.end()) {
            return it->second;
        }
        return 0;
    }

    [[nodiscard]] std::size_t item_count() const {
        return stock_.size();
    }
};

// 🎯 TODO 2: filter_and_sort_leaderboard
struct PlayerRecord {
    std::string name;
    int score;

    bool operator==(const PlayerRecord& other) const {
        return name == other.name && score == other.score;
    }
};

inline std::vector<PlayerRecord> filter_and_sort_leaderboard(
    const std::vector<PlayerRecord>& records,
    int min_score)
{
    std::vector<PlayerRecord> filtered;
    std::copy_if(records.begin(), records.end(), std::back_inserter(filtered),
        [min_score](const PlayerRecord& p) {
            return p.score >= min_score;
        });

    std::sort(filtered.begin(), filtered.end(),
        [](const PlayerRecord& a, const PlayerRecord& b) {
            if (a.score != b.score) {
                return a.score > b.score; // Absteigend nach Score
            }
            return a.name < b.name;       // Alphabetisch bei Gleichstand
        });

    return filtered;
}

// 🎯 TODO 3: calculate_telemetry_stats
struct TelemetryStats {
    double min_val{0.0};
    double max_val{0.0};
    double average{0.0};
    double total{0.0};
};

inline TelemetryStats calculate_telemetry_stats(const std::vector<double>& readings) {
    if (readings.empty()) {
        throw std::invalid_argument("Vector is empty");
    }

    TelemetryStats stats;
    auto [min_it, max_it] = std::minmax_element(readings.begin(), readings.end());
    stats.min_val = *min_it;
    stats.max_val = *max_it;
    stats.total = std::accumulate(readings.begin(), readings.end(), 0.0);
    stats.average = stats.total / static_cast<double>(readings.size());

    return stats;
}

// 🎯 TODO 4: extract_unique_sorted_tags
inline std::set<std::string> extract_unique_sorted_tags(
    const std::vector<std::vector<std::string>>& document_tags)
{
    std::set<std::string> unique_tags;
    for (const auto& tags : document_tags) {
        unique_tags.insert(tags.begin(), tags.end());
    }
    return unique_tags;
}

// 🎯 TODO 5: normalize_sensor_data
inline std::vector<double> normalize_sensor_data(const std::vector<double>& raw_data) {
    if (raw_data.empty()) return {};

    double min_val = *std::min_element(raw_data.begin(), raw_data.end());
    double max_val = *std::max_element(raw_data.begin(), raw_data.end());
    double range = max_val - min_val;

    std::vector<double> result(raw_data.size());

    if (std::fabs(range) < 1e-9) {
        std::fill(result.begin(), result.end(), 0.0);
        return result;
    }

    std::transform(raw_data.begin(), raw_data.end(), result.begin(),
        [min_val, range](double val) {
            return (val - min_val) / range;
        });

    return result;
}

} // namespace cpp11

int main() {
    std::cout << "=== C++ 11: Musterlösung ===" << std::endl;
    cpp11::InventorySystem inv;
    inv.add_item("Diamond", 10);
    std::cout << "Diamond count: " << inv.get_stock("Diamond") << "\n";

    std::vector<cpp11::PlayerRecord> players = {
        {"Alice", 80}, {"Bob", 120}, {"Charlie", 120}, {"Dave", 40}
    };
    auto ranked = cpp11::filter_and_sort_leaderboard(players, 50);
    for (const auto& p : ranked) {
        std::cout << p.name << ": " << p.score << "\n";
    }

    return 0;
}
