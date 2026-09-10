// ============================================================================
// 🦀 RUST 11: ITERATOREN & CLOSURES (MUSTERLÖSUNG)
// ============================================================================

#[derive(Debug, Clone, PartialEq)]
pub struct LogRecord {
    pub id: u64,
    pub service: String,
    pub level: String,
    pub response_time_ms: u64,
}

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
        let current = self.curr;
        self.curr = self.next;
        self.next = current.saturating_add(self.next);
        Some(current)
    }
}

pub fn filter_and_extract_slow_requests(
    logs: &[LogRecord],
    service_name: &str,
    min_latency: u64,
) -> Vec<u64> {
    logs.iter()
        .filter(|log| log.service == service_name && log.response_time_ms >= min_latency)
        .map(|log| log.id)
        .collect()
}

pub fn compute_service_stats(logs: &[LogRecord], service_name: &str) -> Option<(usize, f64, u64)> {
    let matching: Vec<&LogRecord> = logs
        .iter()
        .filter(|log| log.service == service_name)
        .collect();

    if matching.is_empty() {
        return None;
    }

    let count = matching.len();
    let (total_lat, max_lat) = matching.iter().fold((0u64, 0u64), |(sum, max_val), log| {
        (sum + log.response_time_ms, max_val.max(log.response_time_ms))
    });

    let avg = total_lat as f64 / count as f64;
    Some((count, avg, max_lat))
}

pub fn create_multiplier_closure(factor: u64) -> impl Fn(u64) -> u64 {
    move |x: u64| x * factor
}

pub fn fold_metrics<I: IntoIterator<Item = u64>>(iter: I) -> (u64, u64, u64) {
    let mut it = iter.into_iter();
    let first = match it.next() {
        Some(val) => val,
        None => return (0, 0, 0),
    };

    it.fold((first, first, first), |(min_val, max_val, sum_val), x| {
        (min_val.min(x), max_val.max(x), sum_val + x)
    })
}

fn main() {
    println!("=== Rust 11: Iteratoren & Closures ===");
    let fib_8: Vec<u64> = Fibonacci::new().take(8).collect();
    println!("Erste 8 Fibonacci-Zahlen: {:?}", fib_8);

    let logs = vec![
        LogRecord { id: 1, service: "auth".to_string(), level: "INFO".to_string(), response_time_ms: 12 },
        LogRecord { id: 2, service: "auth".to_string(), level: "WARN".to_string(), response_time_ms: 250 },
        LogRecord { id: 3, service: "billing".to_string(), level: "ERROR".to_string(), response_time_ms: 450 },
        LogRecord { id: 4, service: "auth".to_string(), level: "ERROR".to_string(), response_time_ms: 300 },
    ];

    let slow_auth = filter_and_extract_slow_requests(&logs, "auth", 100);
    println!("Slow Auth Logs: {:?}", slow_auth);

    if let Some((count, avg, max)) = compute_service_stats(&logs, "auth") {
        println!("Auth Stats: Count={}, Avg={:.1}ms, Max={}ms", count, avg, max);
    }
}
