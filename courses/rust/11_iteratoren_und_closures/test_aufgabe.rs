// ============================================================================
// 🧪 TESTSUITE: RUST 11 ITERATOREN & CLOSURES
// ============================================================================

#[allow(dead_code)]
#[path = "aufgabe.rs"]
mod aufgabe;

#[allow(unused_imports)]
use aufgabe::*;

// TEST: test_fibonacci_iterator
#[test]
fn test_fibonacci_iterator() {
    let fib: Vec<u64> = Fibonacci::new().take(8).collect();
    assert_eq!(fib, vec![0, 1, 1, 2, 3, 5, 8, 13]);

    let sum_first_5: u64 = Fibonacci::new().take(5).sum();
    // 0 + 1 + 1 + 2 + 3 = 7
    assert_eq!(sum_first_5, 7);
}

// TEST: test_filter_slow_requests
#[test]
fn test_filter_slow_requests() {
    let logs = vec![
        LogRecord { id: 101, service: "gateway".to_string(), level: "INFO".to_string(), response_time_ms: 10 },
        LogRecord { id: 102, service: "gateway".to_string(), level: "WARN".to_string(), response_time_ms: 150 },
        LogRecord { id: 103, service: "db".to_string(), level: "ERROR".to_string(), response_time_ms: 500 },
        LogRecord { id: 104, service: "gateway".to_string(), level: "ERROR".to_string(), response_time_ms: 220 },
    ];

    let slow_gateway = filter_and_extract_slow_requests(&logs, "gateway", 100);
    assert_eq!(slow_gateway, vec![102, 104]);

    let slow_db = filter_and_extract_slow_requests(&logs, "db", 600);
    assert_eq!(slow_db, Vec::<u64>::new());
}

// TEST: test_service_stats
#[test]
fn test_service_stats() {
    let logs = vec![
        LogRecord { id: 1, service: "auth".to_string(), level: "INFO".to_string(), response_time_ms: 100 },
        LogRecord { id: 2, service: "auth".to_string(), level: "WARN".to_string(), response_time_ms: 200 },
        LogRecord { id: 3, service: "auth".to_string(), level: "ERROR".to_string(), response_time_ms: 300 },
    ];

    let stats = compute_service_stats(&logs, "auth");
    assert!(stats.is_some());
    let (count, avg, max) = stats.unwrap();
    assert_eq!(count, 3);
    assert!((avg - 200.0).abs() < 1e-5);
    assert_eq!(max, 300);

    let not_found = compute_service_stats(&logs, "non_existent");
    assert_eq!(not_found, None);
}

// TEST: test_closures_and_fold_metrics
#[test]
fn test_closures_and_fold_metrics() {
    let times_ten = create_multiplier_closure(10);
    assert_eq!(times_ten(5), 50);
    assert_eq!(times_ten(0), 0);

    let numbers = vec![15, 3, 42, 8, 23];
    let (min, max, sum) = fold_metrics(numbers);
    assert_eq!(min, 3);
    assert_eq!(max, 42);
    assert_eq!(sum, 91);

    let empty: Vec<u64> = vec![];
    assert_eq!(fold_metrics(empty), (0, 0, 0));
}

fn main() {
    println!("🧪 Führe Rust 11 Testsuite aus...");
    test_fibonacci_iterator();
    println!("  ✓ test_fibonacci_iterator bestanden");
    test_filter_slow_requests();
    println!("  ✓ test_filter_slow_requests bestanden");
    test_service_stats();
    println!("  ✓ test_service_stats bestanden");
    test_closures_and_fold_metrics();
    println!("  ✓ test_closures_and_fold_metrics bestanden");
    println!("\n✅ Alle Tests für Rust 11 erfolgreich bestanden!");
}
