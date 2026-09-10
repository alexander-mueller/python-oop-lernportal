// 🦀 Testsuite für Rust 02: Das Ownership & Borrowing System

#[test]
fn test_calculate_length_borrow() {
    let text = String::from("WebAssembly");
    let len = calculate_length_borrow(&text);
    assert_eq!(len, 11);
    // Beweis, dass `text` immer noch gültig ist (nicht moved):
    assert_eq!(text, "WebAssembly");
}

#[test]
fn test_append_security_tag() {
    let mut buffer = String::from("Payload");
    append_security_tag(&mut buffer, "::v2");
    assert_eq!(buffer, "Payload::v2");

    append_security_tag(&mut buffer, "::auth");
    assert_eq!(buffer, "Payload::v2::auth");
}

#[test]
fn test_take_ownership_and_wrap() {
    let original = String::from("TOKEN_XYZ");
    let result = take_ownership_and_wrap(original, "Bearer [", "]");
    assert_eq!(result, "Bearer [TOKEN_XYZ]");
}

#[test]
fn test_clone_and_transform() {
    let original = String::from("async await");
    let (upper, len) = clone_and_transform(&original);
    assert_eq!(upper, "ASYNC AWAIT");
    assert_eq!(len, 11);
    assert_eq!(original, "async await", "Original String darf nicht verändert werden");
}

#[test]
fn test_swap_values() {
    let mut num1 = 42;
    let mut num2 = 999;
    swap_values(&mut num1, &mut num2);
    assert_eq!(num1, 999);
    assert_eq!(num2, 42);
}
