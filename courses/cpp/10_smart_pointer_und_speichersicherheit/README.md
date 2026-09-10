# C++ 10: Smart Pointer & Modern Memory Safety

Modernes C++20 löst das historische Problem von C/C++ – manuelle Speicherverwaltung, Memory Leaks und Ungültige Zeiger (Dangling Pointers) – vollständig durch **Smart Pointer** und das **RAII-Prinzip** (Resource Acquisition Is Initialization).

---

## 🎯 Lernziele
1. **Exklusiver Besitz**: `std::unique_ptr<T>` mit `std::make_unique<T>` erzeugen und per `std::move` transferieren.
2. **Geteilter Besitz**: `std::shared_ptr<T>` und atomare Referenzzählung verstehen.
3. **Zyklenfreie Strukturen**: `std::weak_ptr<T>` zur Verhinderung von Speicherlecks in Graphen, Caches und Observern einsetzen (`.lock()`, `.expired()`).
4. **RAII Custom Deleters**: Nicht-speicherbasierte Handles (C-File-Pointers, Mutexes) sicher über RAII-Deleter verwalten.
5. **Memory Safety Verification**: Überwachung von Konstruktion und Destruktion in Unit Tests.

---

## 💡 Schlüsselkonzepte

### 1. `std::unique_ptr`
- Kann nicht kopiert werden (`copy constructor = delete`).
- Überträgt Besitz via `std::move`.
- Zerstört das Objekt automatisch beim Verlassen des Scopes.
```cpp
auto session = std::make_unique<Session>(42, "admin");
manager.register_session(std::move(session)); // session ist danach nullptr
```

### 2. `std::shared_ptr` & `std::weak_ptr`
- `std::shared_ptr` teilt den Besitz mit mehreren Instanzen.
- `std::weak_ptr` beobachtet ein Objekt, ohne den Referenzzähler zu erhöhen.
```cpp
std::shared_ptr<Document> doc = std::make_shared<Document>("MasterThesis");
std::weak_ptr<Document> observer = doc;

if (auto active_doc = observer.lock()) {
    std::cout << active_doc->get_title() << std::endl;
}
```

### 3. RAII Custom Deleter
```cpp
auto raw_buffer = std::unique_ptr<uint8_t[], void(*)(uint8_t*)>(
    new uint8_t[1024],
    [](uint8_t* ptr) { delete[] ptr; }
);
```

---

## 🚀 Aufgaben in `aufgabe.cpp`
- [ ] **TODO 1**: `create_unique_session(id, user)` mit `std::make_unique`
- [ ] **TODO 2**: `SessionManager` mit Move-Semantik (`std::move`)
- [ ] **TODO 3**: `SharedDocument` & `DocumentObserver` mit `std::weak_ptr`
- [ ] **TODO 4**: `ResourceTracker` mit RAII-Zähler
- [ ] **TODO 5**: Custom Deleter für `SafeBuffer`
