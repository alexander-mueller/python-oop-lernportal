# Rust 04: Kontrollfluss & Pattern Matching 🦀

Willkommen zu **Modul 04**!

---

## 💡 1. Kernkonzepte

### `if/else` Expressions
In Rust sind Verzweigungen Ausdrücke:
```rust
let val = if flag { 100 } else { 0 };
```

### Schleifen (`loop`, `while`, `for`)
- `loop` mit `break value;`
- `while condition { ... }`
- `for i in 1..=10 { ... }`

### `match` Pattern Matching & Guards
```rust
match (role, level) {
    ("Admin", _) => true,
    ("User", l) if l <= 2 => true,
    _ => false,
}
```

---

## 🎯 Teilziele in `aufgabe.rs`

- **TODO 1:** `classify_temperature(temp_celsius: i32) -> &'static str`
- **TODO 2:** `compute_fibonacci(n: u32) -> u64`
- **TODO 3:** `retry_operation_loop(limit: u32, success_at: u32) -> u32`
- **TODO 4:** `evaluate_permission(role: &str, resource_level: u8, is_admin: bool) -> bool`
- **TODO 5:** `count_even_squares(max: u32) -> u64`
