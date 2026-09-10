// ============================================================================
// 🦀 RUST 11: ITERATOREN & CLOSURES
// ============================================================================

#[derive(Debug, Clone, PartialEq)]
pub struct LogRecord {
    pub id: u64,
    pub service: String,
    pub level: String,
    pub response_time_ms: u64,
}

// 🎯 TODO 1: Implementiere den Custom Iterator 'Fibonacci'
// Erzeugt eine endlose Folge von Fibonacci-Zahlen (0, 1, 1, 2, 3, 5, 8, 13, ...)
pub struct Fibonacci {
    pub curr: u64,
    pub next: u64,
}

impl Fibonacci {
    pub fn new() -> Self {
        Self { curr: 0, next: 1 }
    }
}

impl Iterator for Fibonacci {
    type Item = u64;

    fn next(&mut self) -> Option<Self::Item> {
        // TODO: Aktuellen Wert sichern, next aktualisieren und Some(current) zurückgeben
        None
    }
}

// 🎯 TODO 2: Implementiere 'filter_and_extract_slow_requests'
// Filtert alle Logs, bei denen 'service == service_name' und 'response_time_ms >= min_latency' gilt,
// und gibt einen Vec<u64> der Log-IDs zurück.
// Verwende eine funktionale Iterator-Pipeline (.iter(), .filter(), .map(), .collect())!
pub fn filter_and_extract_slow_requests(logs: &[LogRecord], service_name: &str, min_latency: u64) -> Vec<u64> {
    // TODO: Iterator-Pipeline aufbauen
    Vec::new()
}

// 🎯 TODO 3: Implementiere 'compute_service_stats'
// Berechnet für einen gegebenen Service: (Anzahl Logs, Durchschnittliche Latenz in ms f64, Maximale Latenz u64)
// Falls keine Logs für den Service existieren, gib 'None' zurück.
pub fn compute_service_stats(logs: &[LogRecord], service_name: &str) -> Option<(usize, f64, u64)> {
    // TODO: Filtern und mit .fold() oder .map() aggregieren
    None
}

// 🎯 TODO 4: Implementiere 'create_multiplier_closure'
// Liefert ein Closure mit 'impl Fn(u64) -> u64', welches den Eingabewert mit 'factor' multipliziert.
pub fn create_multiplier_closure(factor: u64) -> impl Fn(u64) -> u64 {
    // TODO: move Closure zurückgeben
    move |x: u64| x
}

// 🎯 TODO 5: Implementiere 'fold_metrics'
// Berechnet für ein beliebiges Iterable von u64 in einem einzigen .fold() Durchlauf:
// (Minimum, Maximum, Summe)
// Bei leerem Iterator: (0, 0, 0)
pub fn fold_metrics<I: IntoIterator<Item = u64>>(iter: I) -> (u64, u64, u64) {
    // TODO: In ein Iterator wandeln und mit .fold() aggregieren
    (0, 0, 0)
}

fn main() {
    println!("=== Rust 11: Iteratoren & Closures ===");
    let fib_5: Vec<u64> = Fibonacci::new().take(8).collect();
    println!("Erste 8 Fibonacci-Zahlen: {:?}", fib_5);

    let logs = vec![
        LogRecord { id: 1, service: "auth".to_string(), level: "INFO".to_string(), response_time_ms: 12 },
        LogRecord { id: 2, service: "auth".to_string(), level: "WARN".to_string(), response_time_ms: 250 },
        LogRecord { id: 3, service: "billing".to_string(), level: "ERROR".to_string(), response_time_ms: 450 },
    ];

    let slow_auth = filter_and_extract_slow_requests(&logs, "auth", 100);
    println!("Slow Auth Logs: {:?}", slow_auth);
}
