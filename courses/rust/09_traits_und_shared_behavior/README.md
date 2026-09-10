# Rust 09: Traits & Shared Behavior

In diesem Modul lernst du, wie Rust Polymorphie und gemeinsame Schnittstellen ohne klassische Vererbung abbildet: **Traits**.

---

## 🎯 Lernziele
1. **Traits definieren**: Methodensignaturen mit `pub trait MyTrait` festlegen.
2. **Default-Implementierungen**: Standardverhalten in Traits bereitstellen und selektiv überschreiben.
3. **`impl Trait for Type`**: Traits für benutzerdefinierte Structs implementieren.
4. **Trait Bounds (`T: Trait1 + Trait2`)**: Typsichere Einschränkungen für generische Funktionen und `where`-Klauseln.
5. **`impl Trait` als Rückgabetyp**: Kapselung konkreter Typen bei statischem Dispatch.

---

## 💡 Schlüsselkonzepte

### 1. Trait-Definition & Default-Methoden
```rust
pub trait TelemetryReport {
    fn summary(&self) -> String;

    // Default-Implementierung
    fn severity_level(&self) -> u8 {
        1
    }

    fn is_critical(&self) -> bool {
        self.severity_level() >= 8
    }
}
```

### 2. Trait Bounds & Where-Klauseln
```rust
// Kompakte Syntax
fn print_report<T: TelemetryReport + std::fmt::Display>(item: &T) {
    println!("{}: {}", item, item.summary());
}

// Lesbar bei vielen Typen mit where-Klausel
fn process<T, U>(t: &T, u: &U)
where
    T: TelemetryReport + Clone,
    U: std::fmt::Debug,
{
    println!("{:?} => {}", u, t.summary());
}
```

---

## 🧪 Tests ausführen

```bash
# Mit rustc direkt kompilieren und ausführen
rustc --test test_aufgabe.rs && ./test_aufgabe

# Oder im Kurs-Workspace ausführen
```
