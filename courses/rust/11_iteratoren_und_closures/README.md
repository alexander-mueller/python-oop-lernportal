# Rust 11: Iteratoren & Closures

Tauche ein in die funktionale Welt von Rust: Closures, Environment Capturing und Zero-Cost Iterator-Pipelines.

---

## 🎯 Lernziele
1. **Closures**: Syntax `|args| body` und Environment-Capturing via `Fn`, `FnMut` und `FnOnce`.
2. **Move-Semantik**: Variablen-Besitz in Closures mit dem Schlüsselwort `move` übertragen.
3. **Eigene Iteratoren**: Den `Iterator`-Trait mit `type Item` und `fn next(&mut self)` implementieren.
4. **Adapter-Chaining**: `.map()`, `.filter()`, `.fold()`, `.filter_map()`, `.zip()`, `.take()` effizient verketten.
5. **Zero-Cost Abstraction**: Verstehen, warum funktionale Pipelines in Rust genauso schnell wie handgeschriebene for-Loops kompilieren.

---

## 💡 Schlüsselkonzepte

### 1. Custom Iterator
```rust
pub struct Fibonacci {
    curr: u64,
    next: u64,
}

impl Iterator for Fibonacci {
    type Item = u64;

    fn next(&mut self) -> Option<Self::Item> {
        let current = self.curr;
        self.curr = self.next;
        self.next = current + self.next;
        Some(current)
    }
}
```

---

## 🧪 Tests ausführen

```bash
rustc --test test_aufgabe.rs && ./test_aufgabe
```
