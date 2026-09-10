# Rust 03: Slices & Lifetimes Grundlagen 🦀

Willkommen zu **Modul 03**!

---

## 💡 1. Kerninhalte

### Slices (`&str` & `&[T]`)
- Ein Slice ist ein **Fat Pointer** (Start-Zeiger + Länge) ohne Eigentümerschaft (Ownership).
- String Slices: `&str` – Verweisen auf UTF-8 Bytefolgen in `String` oder Programmcode (`&'static str`).
- Slice Slices: `&[i32]` – Verweisen auf Teilstücke von Arrays oder Vektoren.

### Lifetimes & Borrow Checker
- Verhindern hängende Referenzen (*Dangling Pointers*).
- Funktionssignaturen mit mehreren Referenzen deklarieren Lifetimes mit `'a`.

```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() >= y.len() { x } else { y }
}
```

---

## 🎯 Teilziele in `aufgabe.rs`

- **TODO 1:** `first_word(s: &str) -> &str`
- **TODO 2:** `sum_slice(numbers: &[i32]) -> i32`
- **TODO 3:** `get_subslice(arr: &[u32], start: usize, len: usize) -> &[u32]`
- **TODO 4:** `longest_str<'a>(x: &'a str, y: &'a str) -> &'a str`
- **TODO 5:** `strip_prefix_slice<'a>(haystack: &'a str, prefix: &str) -> Option<&'a str>`
