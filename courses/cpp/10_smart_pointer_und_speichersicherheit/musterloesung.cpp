#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <stdexcept>
#include <cstdint>
#include <algorithm>

namespace cpp10 {

struct Session {
    int id;
    std::string username;

    Session(int session_id, std::string user)
        : id(session_id), username(std::move(user)) {}
};

// 🎯 TODO 1: create_unique_session
inline std::unique_ptr<Session> create_unique_session(int id, const std::string& username) {
    return std::make_unique<Session>(id, username);
}

// 🎯 TODO 2: SessionManager (Move-Semantik & Ownership)
class SessionManager {
private:
    std::vector<std::unique_ptr<Session>> sessions_;

public:
    void add_session(std::unique_ptr<Session> session) {
        if (session) {
            sessions_.push_back(std::move(session));
        }
    }

    [[nodiscard]] std::size_t count() const {
        return sessions_.size();
    }

    [[nodiscard]] const Session* get_session(int id) const {
        for (const auto& s : sessions_) {
            if (s && s->id == id) {
                return s.get();
            }
        }
        return nullptr;
    }

    std::unique_ptr<Session> extract_session(int id) {
        for (auto it = sessions_.begin(); it != sessions_.end(); ++it) {
            if (*it && (*it)->id == id) {
                std::unique_ptr<Session> extracted = std::move(*it);
                sessions_.erase(it);
                return extracted;
            }
        }
        return nullptr;
    }
};

// 🎯 TODO 3: SharedDocument & DocumentObserver mit std::shared_ptr & std::weak_ptr
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
        return !doc_ref_.expired();
    }

    [[nodiscard]] std::string read_title() const {
        if (auto doc = doc_ref_.lock()) {
            return doc->get_title();
        }
        throw std::runtime_error("Document destroyed");
    }
};

// 🎯 TODO 4: ResourceTracker (RAII Lifecycle & Leak Prevention)
class ResourceTracker {
public:
    static inline int active_count = 0;
    static inline int total_created = 0;

    int resource_id;

    explicit ResourceTracker(int id) : resource_id(id) {
        ++active_count;
        ++total_created;
    }

    ~ResourceTracker() {
        --active_count;
    }
};

// 🎯 TODO 5: Custom Deleter für Heap Buffer (SafeBuffer)
struct BufferDeleter {
    bool* freed_signal{nullptr};

    void operator()(uint8_t* ptr) const {
        if (freed_signal) *freed_signal = true;
        delete[] ptr;
    }
};

using SafeBuffer = std::unique_ptr<uint8_t[], BufferDeleter>;

inline SafeBuffer create_monitored_buffer(std::size_t size, bool* freed_flag) {
    return SafeBuffer(new uint8_t[size], BufferDeleter{freed_flag});
}

} // namespace cpp10

int main() {
    std::cout << "=== C++ 10: Musterlösung ===" << std::endl;

    auto s1 = cpp10::create_unique_session(1, "alice");
    cpp10::SessionManager mgr;
    mgr.add_session(std::move(s1));
    std::cout << "Active sessions: " << mgr.count() << "\n";

    auto doc = std::make_shared<cpp10::Document>("Architektur", "Inhalt...");
    cpp10::DocumentObserver obs(doc);
    std::cout << "Doc title: " << obs.read_title() << "\n";

    bool freed = false;
    {
        auto buf = cpp10::create_monitored_buffer(1024, &freed);
        buf[0] = 0xAA;
    }
    std::cout << "Buffer freed automatically: " << (freed ? "true" : "false") << "\n";

    return 0;
}
