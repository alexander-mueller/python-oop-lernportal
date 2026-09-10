# Rust 10: Generics & Dynamischer Dispatch

Lerne den fundamentalen Unterschied zwischen **statischem Dispatch (Monomorphisierung)** und **dynamischem Dispatch (Trait Objects mit `dyn Trait`)** kennen.

---

## 🎯 Lernziele
1. **Generische Structs & Methoden**: Typ-unabhängigen Code mit `struct Container<T>` und `impl<T> Container<T>` schreiben.
2. **Monomorphisierung**: Verstehen, wie der Rust-Compiler generischen Code zur Compile-Zeit dupliziert (Zero-Cost Abstractions).
3. **Trait Objects (`dyn Trait`)**: Trait-Objekte mit `Box<dyn Trait>` oder `&dyn Trait` für heterogene Collections erstellen.
4. **Vtable & Fat Pointer**: Aufbau von Trait Objects (Datenpointer + vtable-Pointer) nachvollziehen.

---

## 💡 Schlüsselkonzepte

### 1. Statischer Dispatch (Generics)
```rust
fn process_static<T: DataPlugin>(plugin: &T, input: &str) -> String {
    plugin.process(input) // Direkter Aufruf, vom Compiler inline-optimiert
}
```

### 2. Dynamischer Dispatch (`dyn Trait`)
```rust
fn process_dynamic(plugin: &dyn DataPlugin, input: &str) -> String {
    plugin.process(input) // vtable Lookup zur Laufzeit
}
```

---

## 🧪 Tests ausführen

```bash
rustc --test test_aufgabe.rs && ./test_aufgabe
```
