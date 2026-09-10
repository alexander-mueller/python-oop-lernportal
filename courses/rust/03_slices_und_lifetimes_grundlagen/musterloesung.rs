// 🦀 Rust 03: Musterlösung
// =========================

pub fn first_word(s: &str) -> &str {
    let bytes = s.as_bytes();
    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return &s[0..i];
        }
    }
    s
}

pub fn sum_slice(numbers: &[i32]) -> i32 {
    let mut sum = 0;
    for &num in numbers {
        sum += num;
    }
    sum
}

pub fn get_subslice(arr: &[u32], start: usize, len: usize) -> &[u32] {
    if start > arr.len() || start + len > arr.len() {
        return &[];
    }
    &arr[start..start + len]
}

pub fn longest_str<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() >= y.len() {
        x
    } else {
        y
    }
}

pub fn strip_prefix_slice<'a>(haystack: &'a str, prefix: &str) -> Option<&'a str> {
    if haystack.starts_with(prefix) {
        Some(&haystack[prefix.len()..])
    } else {
        None
    }
}

fn main() {
    let sentence = String::from("Rust ZeroCost Abstractions");
    println!("Erstes Wort: '{}'", first_word(&sentence));

    let numbers = [10, 20, 30, 40, 50];
    println!("Summe: {}", sum_slice(&numbers[1..4]));

    let slice = get_subslice(&numbers, 2, 2);
    println!("Sub-Slice: {:?}", slice);

    let str1 = "Concurrency";
    let str2 = "Async";
    println!("Längerer String: {}", longest_str(str1, str2));

    let path = "/api/v1/users";
    if let Some(rest) = strip_prefix_slice(path, "/api/v1") {
        println!("API Route: {}", rest);
    }
}
