// 🦀 Rust 04: Kontrollfluss & Pattern Matching
// ============================================

// 🎯 TEILZIEL 1 (TODO 1): Klassifiziere eine Temperatur mittels `match`
// - ..=0    -> "Freezing"
// - 1..=15  -> "Cold"
// - 16..=25 -> "Comfortable"
// - 26..=35 -> "Warm"
// - _       -> "Hot"
pub fn classify_temperature(temp_celsius: i32) -> &'static str {
    // TODO: Verwende match mit Range-Patterns
    ""
}

// 🎯 TEILZIEL 2 (TODO 2): Berechne die n-te Fibonacci-Zahl iterativ
// n=0 -> 0, n=1 -> 1, n=2 -> 1, n=3 -> 2, n=4 -> 3, n=5 -> 5, n=6 -> 8 ...
pub fn compute_fibonacci(n: u32) -> u64 {
    // TODO: Berechne Fibonacci iterativ mit einer for- oder while-Schleife
    0
}

// 🎯 TEILZIEL 3 (TODO 3): Simuliere eine Retry-Schleife mit `loop` und `break value`
// Starte bei attempt = 1.
// In jedem Durchlauf:
// - Wenn attempt == success_at: beende mit `break attempt;`
// - Wenn attempt > limit: beende mit `break 0;` (Limit überschritten)
// - Sonst attempt += 1
pub fn retry_operation_loop(limit: u32, success_at: u32) -> u32 {
    // TODO: Verwende `loop` mit `break value`
    0
}

// 🎯 TEILZIEL 4 (TODO 4): Berechtigungsprüfung mit `match` und Guards
// - Wenn is_admin == true: immer `true`
// - Wenn role == "Editor" und resource_level <= 3: `true`
// - Wenn role == "Viewer" und resource_level <= 1: `true`
// - In allen anderen Fällen: `false`
pub fn evaluate_permission(role: &str, resource_level: u8, is_admin: bool) -> bool {
    // TODO: Verwende match (role, resource_level, is_admin)
    false
}

// 🎯 TEILZIEL 5 (TODO 5): Summiere die Quadrate aller geraden Zahlen von 1 bis max
// Iteriere mit `for i in 1..=max`.
// Wenn i gerade ist (i % 2 == 0), addiere (i as u64) * (i as u64) zur Summe.
pub fn count_even_squares(max: u32) -> u64 {
    // TODO: Iteriere und summiere die Quadrate der geraden Zahlen
    0
}

fn main() {
    println!("Temp 21°C: {}", classify_temperature(21));
    println!("Fib(10): {}", compute_fibonacci(10));
    println!("Retry (success at 3, limit 5): {}", retry_operation_loop(5, 3));
    println!("Permission Editor Lvl 2: {}", evaluate_permission("Editor", 2, false));
    println!("Even Squares bis 10: {}", count_even_squares(10));
}
