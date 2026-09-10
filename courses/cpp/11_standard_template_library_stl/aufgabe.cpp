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

// ============================================================================
// 🎯 TODO 1: InventorySystem
// Verwaltet Artikel und deren Anzahl via std::unordered_map<std::string, int>.
// Methoden:
// - void add_item(const std::string& name, int amount): Erhöht den Bestand (oder fügt neu ein)
// - bool remove_item(const std::string& name, int amount):
//     Falls Artikel vorhanden und Bestand >= amount: reduziert um amount und gibt true zurück.
//     Falls Bestand danach 0 ist, bleibt der Eintrag oder wird 0.
//     Falls nicht genug vorhanden oder Artikel nicht existent: ändert nichts und gibt false zurück.
// - int get_stock(const std::string& name) const: Gibt Bestand zurück (0 wenn nicht existent)
// - std::size_t item_count() const: Anzahl der verschiedenen Artikelarten im Inventar
// ============================================================================
class InventorySystem {
private:
    std::unordered_map<std::string, int> stock_;

public:
    void add_item(const std::string& name, int amount) {
        // TODO 1a: Bestand erhöhen
    }

    bool remove_item(const std::string& name, int amount) {
        // TODO 1b: Bestand prüfen und reduzieren
        return false;
    }

    [[nodiscard]] int get_stock(const std::string& name) const {
        // TODO 1c: Bestand ermitteln
        return 0;
    }

    [[nodiscard]] std::size_t item_count() const {
        return stock_.size();
    }
};

// ============================================================================
// 🎯 TODO 2: filter_and_sort_leaderboard
// Struktur PlayerRecord mit name (std::string) und score (int).
// Filtere alle Spieler mit score >= min_score und sortiere sie absteigend nach score.
// Falls scores identisch sind, sortiere alphabetisch aufsteigend nach name.
// ============================================================================
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
    // TODO 2: Filtern mit std::copy_if und Sortieren mit std::sort
    return filtered;
}

// ============================================================================
// 🎯 TODO 3: calculate_telemetry_stats
// Struktur TelemetryStats mit min_val, max_val, average, total.
// Berechne aus einem std::vector<double> mit STL-Algorithmen:
// - std::min_element für min_val
// - std::max_element für max_val
// - std::accumulate für total und average
// Falls der Vektor leer ist, wirf std::invalid_argument("Vector is empty").
// ============================================================================
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
    // TODO 3: STL-Algorithmen zur Berechnung einsetzen
    return stats;
}

// ============================================================================
// 🎯 TODO 4: extract_unique_sorted_tags
// Gegeben ist eine Liste von Dokumenten, wobei jedes Dokument eine Liste von Tags enthält.
// Extrahiere alle eindeutigen Tags in ein sortiertes std::set<std::string>.
// ============================================================================
inline std::set<std::string> extract_unique_sorted_tags(
    const std::vector<std::vector<std::string>>& document_tags)
{
    std::set<std::string> unique_tags;
    // TODO 4: Alle Tags in unique_tags einfügen (Deduplizierung & Sortierung automatisch)
    return unique_tags;
}

// ============================================================================
// 🎯 TODO 5: normalize_sensor_data
// Normalisiere alle Werte in 'raw_data' auf den Bereich [0.0, 1.0]:
// normalized = (x - min) / (max - min)
// Verwende std::transform. Falls max == min (alle Werte gleich), setze alle Werte auf 0.0.
// ============================================================================
inline std::vector<double> normalize_sensor_data(const std::vector<double>& raw_data) {
    if (raw_data.empty()) return {};
    std::vector<double> result(raw_data.size());
    // TODO 5: Min/Max finden und mit std::transform normalisieren
    return result;
}

} // namespace cpp11

int main() {
    std::cout << "=== C++ 11: Standard Template Library (STL) ===" << std::endl;
    cpp11::InventorySystem inv;
    inv.add_item("IronSword", 2);
    std::cout << "IronSword count: " << inv.get_stock("IronSword") << std::endl;
    return 0;
}
