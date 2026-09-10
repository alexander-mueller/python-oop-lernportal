# Rust 12: Smart Pointer & Speichersicherheit

Lerne die wichtigsten Smart Pointer der Rust-Standardbibliothek: `Box<T>`, `Rc<T>`, `RefCell<T>` und das RAII `Drop`-Trait.

---

## 🎯 Lernziele
1. **`Box<T>`**: Heap-Allokation für Daten mit bekannter Pointer-Größe und rekursive Typen.
2. **`Rc<T>`**: Referenzzählung für Multiple Ownership in Single-Thread-Szenarien.
3. **`RefCell<T>` & Interior Mutability**: Sichere Mutation unveränderlicher Variablen durch dynamische Laufzeitprüfung.
4. **`Rc<RefCell<T>>`**: Das Standard-Muster für geteilte veränderliche Datenstrukturen (z.B. Graphen, DOM).
5. **`Drop` Trait**: Deterministische Ressourcenfreigabe ohne Garbage Collector.

---

## 💡 Schlüsselkonzepte

### 1. Rekursiver Baum mit Box
```rust
pub enum TreeNode {
    Empty,
    Node {
        val: i32,
        left: Box<TreeNode>,
        right: Box<TreeNode>,
    },
}
```

### 2. Interior Mutability mit Rc und RefCell
```rust
use std::rc::Rc;
use std::cell::RefCell;

let counter = Rc::new(RefCell::new(0));
*counter.borrow_mut() += 1;
assert_eq!(*counter.borrow(), 1);
```

---

## 🧪 Tests ausführen

```bash
rustc --test test_aufgabe.rs && ./test_aufgabe
```
