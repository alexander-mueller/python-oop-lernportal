# Rust 01: Variablen, Mutabilität & Typensystem 🦀

Willkommen zu **Modul 01** des modernen Rust-Kurses!

In diesem Kapitel lernst du die Kernbausteine der Sprache kennen:
- Warum Variablen in Rust standardmäßig unveränderlich (**immutable**) sind
- Wie du mit `let mut` kontrolliert Mutabilität aktivierst
- Skalare Datentypen (`i32`, `u64`, `f64`, `bool`, `char`) und zusammengesetzte Typen (Tupel und feste Arrays)
- Das Konzept des **Shadowing** (Wiederverwenden von Variablennamen mit neuem Typ)
- Explizite Typumwandlung mit dem Schlüsselwort `as`

---

## 💡 1. Theorie-Zusammenfassung

### Immutability by Default
```rust
let x = 5;
// x = 6; // ❌ Fehler: x ist unveränderlich

let mut y = 10;
y = 20; // ✅ Funktioniert!
```

### Skalare und zusammengesetzte Typen
- **Integers**: `i8` bis `i128`, `u8` bis `u128`, `usize` (plattformabhängige Pointerbreite)
- **Floats**: `f32`, `f64` (Standard)
- **Char**: 4-Byte Unicode Scalar (`'🦀'`, `'a'`)
- **Tupel**: `(String, u32, bool)` - Feste Länge, unterschiedliche Typen
- **Arrays**: `[i32; 4]` - Feste Länge, homogener Typ, Allokation direkt auf dem Stack!

### Shadowing
```rust
let data = "42";             // &str
let data: i32 = data.parse().unwrap(); // i32
```

---

## 🎯 Teilziele in `aufgabe.rs`

- **TODO 1:** `create_system_specs() -> (String, u32, f64, bool)`
- **TODO 2:** `calculate_average_load(cores: u32, total_ticks: u64) -> f64`
- **TODO 3:** `format_sensor_reading(sensor_id: u16, temp_celsius: f32, is_alert: bool) -> String`
- **TODO 4:** `demonstrate_shadowing_and_arrays(input_str: &str) -> [i32; 4]`
- **TODO 5:** `calculate_disk_utilization_percent(used_bytes: u64, total_bytes: u64) -> f64`
