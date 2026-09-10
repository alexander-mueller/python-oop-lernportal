// 🦀 Rust 04: Musterlösung
// =========================

pub fn classify_temperature(temp_celsius: i32) -> &'static str {
    match temp_celsius {
        ..=0 => "Freezing",
        1..=15 => "Cold",
        16..=25 => "Comfortable",
        26..=35 => "Warm",
        _ => "Hot",
    }
}

pub fn compute_fibonacci(n: u32) -> u64 {
    if n == 0 {
        return 0;
    }
    if n == 1 {
        return 1;
    }
    let mut prev = 0u64;
    let mut curr = 1u64;
    for _ in 2..=n {
        let next = prev + curr;
        prev = curr;
        curr = next;
    }
    curr
}

pub fn retry_operation_loop(limit: u32, success_at: u32) -> u32 {
    let mut attempt = 1;
    loop {
        if attempt == success_at {
            break attempt;
        }
        if attempt > limit {
            break 0;
        }
        attempt += 1;
    }
}

pub fn evaluate_permission(role: &str, resource_level: u8, is_admin: bool) -> bool {
    match (role, resource_level, is_admin) {
        (_, _, true) => true,
        ("Editor", level, _) if level <= 3 => true,
        ("Viewer", level, _) if level <= 1 => true,
        _ => false,
    }
}

pub fn count_even_squares(max: u32) -> u64 {
    let mut sum = 0u64;
    for i in 1..=max {
        if i % 2 == 0 {
            let val = i as u64;
            sum += val * val;
        }
    }
    sum
}

fn main() {
    println!("Temp 21°C: {}", classify_temperature(21));
    println!("Fib(10): {}", compute_fibonacci(10));
    println!("Retry (success at 3, limit 5): {}", retry_operation_loop(5, 3));
    println!("Permission Editor Lvl 2: {}", evaluate_permission("Editor", 2, false));
    println!("Even Squares bis 10: {}", count_even_squares(10));
}
