// 🦀 Rust 02: Musterlösung
// =========================

pub fn calculate_length_borrow(s: &String) -> usize {
    s.len()
}

pub fn append_security_tag(s: &mut String, tag: &str) {
    s.push_str(tag);
}

pub fn take_ownership_and_wrap(s: String, prefix: &str, suffix: &str) -> String {
    format!("{}{}{}", prefix, s, suffix)
}

pub fn clone_and_transform(s: &String) -> (String, usize) {
    let original_len = s.len();
    let cloned_upper = s.clone().to_uppercase();
    (cloned_upper, original_len)
}

pub fn swap_values(a: &mut i32, b: &mut i32) {
    let temp = *a;
    *a = *b;
    *b = temp;
}

fn main() {
    let mut greeting = String::from("Hallo Rust");
    println!("Länge (borrow): {}", calculate_length_borrow(&greeting));

    append_security_tag(&mut greeting, " [SECURE]");
    println!("Nach Tag: {}", greeting);

    let wrapped = take_ownership_and_wrap(greeting, ">>> ", " <<<");
    println!("Wrapped: {}", wrapped);

    let sample = String::from("concurrency");
    let (upper, len) = clone_and_transform(&sample);
    println!("Clone & Upper: {} (Orig-Länge: {})", upper, len);

    let mut x = 10;
    let mut y = 99;
    swap_values(&mut x, &mut y);
    println!("Swapped: x={}, y={}", x, y);
}
