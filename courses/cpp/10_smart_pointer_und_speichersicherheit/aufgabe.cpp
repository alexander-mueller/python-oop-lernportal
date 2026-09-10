#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <stdexcept>
#include <cstdint>

namespace cpp10 {

// Hilfsstruktur für Sessions
struct Session {
    int id;
    std::string username;

    Session(int session_id, std::string user)
        : id(session_id), username(std::move(user)) {}
};

// ============================================================================
// 🎯 TODO 1: create_unique_session
// Erzeuge mit std::make_unique einen neuen Session-Zeiger (std::unique_ptr<Session>)
// mit der übergebenen ID und dem Benutzernamen.
// ============================================================================
inline std::unique_ptr<Session> create_unique_session(int id, const std::string& username) {
    // TODO 1: std::make_unique aufrufen
    return nullptr;
}

// ============================================================================
// 🎯 TODO 2: SessionManager (Move-Semantik & Ownership)
// Verwaltet eine Liste von Sessions via std::vector<std::unique_ptr<Session>>.
// Methoden:
// - void add_session(std::unique_ptr<Session> session): Übernimmt den Besitz per std::move
// - std::size_t count() const: Gibt Anzahl der aktiven Sessions zurück
// - const Session* get_session(int id) const: Sucht Session mit id, gibt Rohzeiger (Observer)
//                                             oder nullptr zurück wenn nicht gefunden
// - std::unique_ptr<Session> extract_session(int id): Entfernt die Session aus dem Manager
//                                                     und gibt den Besitz an den Aufrufer zurück
// ============================================================================
class SessionManager {
private:
    std::vector<std::unique_ptr<Session>> sessions_;

public:
    void add_session(std::unique_ptr<Session> session) {
        // TODO 2a: Session in sessions_ per std::move einfügen
    }

    [[nodiscard]] std::size_t count() const {
        // TODO 2b: Anzahl zurückgeben
        return 0;
    }

    [[nodiscard]] const Session* get_session(int id) const {
        // TODO 2c: Observer-Zeiger suchen
        return nullptr;
    }

    std::unique_ptr<Session> extract_session(int id) {
        // TODO 2d: Session finden, aus Vector entfernen und ownership zurückgeben
        return nullptr;
    }
};

// ============================================================================
// 🎯 TODO 3: SharedDocument & DocumentObserver mit std::shared_ptr & std::weak_ptr
// - Document hält Titel und Text.
// - DocumentObserver hält eine schwache Referenz (std::weak_ptr<Document>).
// - bool is_valid() const: Prüft ob das Dokument noch existiert (!expired())
// - std::string read_title() const: Gibt den Titel zurück falls noch existent,
//                                   oder wirft std::runtime_error("Document destroyed")
// ============================================================================
class Document {
private:
    std::string title_;
    std::string content_;

public:
    Document(std::string title, std::string content)
        : title_(std::move(title)), content_(std::move(content)) {}

    [[nodiscard]] const std::string& get_title() const { return title_; }
    [[nodiscard]] const std::string& get_content() const { return content_; }
};

class DocumentObserver {
private:
    std::weak_ptr<Document> doc_ref_;

public:
    explicit DocumentObserver(std::shared_ptr<Document> doc) : doc_ref_(doc) {}

    [[nodiscard]] bool is_valid() const {
        // TODO 3a: Prüfen, ob das Zielobjekt noch existiert
        return false;
    }

    [[nodiscard]] std::string read_title() const {
        // TODO 3b: Mit lock() auflösen und Titel lesen
        if (auto doc = doc_ref_.lock()) {
            return doc->get_title();
        }
        throw std::runtime_error("Document destroyed");
    }
};

// ============================================================================
// 🎯 TODO 4: ResourceTracker (RAII Lifecycle & Leak Prevention)
// Zählt statisch alle aktiven Instanzen in 'active_count' und alle erzeugten Instanzen in 'total_created'.
// - Konstruktor: Inkrementiert active_count und total_created
// - Destruktor: Dekrementiert active_count
// ============================================================================
class ResourceTracker {
public:
    static inline int active_count = 0;
    static inline int total_created = 0;

    int resource_id;

    explicit ResourceTracker(int id) : resource_id(id) {
        // TODO 4a: Zähler inkrementieren
    }

    ~ResourceTracker() {
        // TODO 4b: active_count dekrementieren
    }
};

// ============================================================================
// 🎯 TODO 5: Custom Deleter für Heap Buffer (SafeBuffer)
// Erzeuge einen std::unique_ptr für ein uint8_t[]-Array der Größe 'size',
// dessen Custom Deleter ein boolean Flag 'freed_flag' auf true setzt, wenn er aufgerufen wird.
// ============================================================================
struct BufferDeleter {
    bool* freed_signal{nullptr};

    void operator()(uint8_t* ptr) const {
        if (freed_signal) *freed_signal = true;
        delete[] ptr;
    }
};

using SafeBuffer = std::unique_ptr<uint8_t[], BufferDeleter>;

inline SafeBuffer create_monitored_buffer(std::size_t size, bool* freed_flag) {
    // TODO 5: SafeBuffer mit neuem uint8_t[size] und BufferDeleter{freed_flag} zurückgeben
    return SafeBuffer(nullptr, BufferDeleter{freed_flag});
}

} // namespace cpp10

int main() {
    std::cout << "=== C++ 10: Smart Pointer & Speichersicherheit ===" << std::endl;
    auto s = cpp10::create_unique_session(1, "alice");
    if (s) {
        std::cout << "Session ID: " << s->id << ", User: " << s->username << std::endl;
    }
    return 0;
}
