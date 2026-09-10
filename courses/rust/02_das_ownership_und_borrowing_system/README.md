# Rust 02: Das Ownership & Borrowing System 🦀

Willkommen zum wichtigsten Kernkonzept von Rust: **Ownership, Move-Semantik und Borrowing**!

---

## 💡 1. Kernkonzepte im Überblick

### Die drei Ownership-Regeln
1. Jeder Wert in Rust hat eine Variable als seinen **Besitzer** (Owner).
2. Es gibt immer nur **einen Besitzer zur Zeit**.
3. Verlässt der Besitzer den Gültigkeitsbereich (`}` Scope), wird der Speicher automatisch mit `drop` freigegeben.

### Move vs. Copy vs. Clone
- **Copy**: Automatische bitweise Stack-Kopie für skalare Typen (`i32`, `f64`, `bool`).
- **Move**: Zuweisung von Heap-Objekten (`String`, `Vec`) überträgt die Ownership. Die ursprüngliche Variable wird ungültig.
- **Clone**: Explizite, bewusste Tiefenkopie des Heap-Speichers via `.clone()`.

### Borrowing & Aliasing XOR Mutation
- **Unveränderliche Referenz (`&T`)**: Beliebig viele gleichzeitige Lesezugriffe erlaubt.
- **Veränderbare Referenz (`&mut T`)**: Maximal eine einzige veränderbare Referenz erlaubt, solange keine anderen Referenzen aktiv sind.

---

## 🎯 Teilziele in `aufgabe.rs`

- **TODO 1:** `calculate_length_borrow(s: &String) -> usize` (Unveränderliches Borrowing)
- **TODO 2:** `append_security_tag(s: &mut String, tag: &str)` (Veränderliches Borrowing)
- **TODO 3:** `take_ownership_and_wrap(s: String, prefix: &str, suffix: &str) -> String` (Move-Semantik & Ownership)
- **TODO 4:** `clone_and_transform(s: &String) -> (String, usize)` (Clone & Uppercase)
- **TODO 5:** `swap_values(a: &mut i32, b: &mut i32)` (In-Place Wertetausch via `&mut`)
