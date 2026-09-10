// 🦀 Testsuite für Rust 03: Slices & Lifetimes Grundlagen

#[test]
fn test_first_word() {
    let s1 = "Hello Rustacean!";
    assert_eq!(first_word(s1), "Hello");

    let s2 = "SingleWord";
    assert_eq!(first_word(s2), "SingleWord");

    let s3 = " leading space";
    assert_eq!(first_word(s3), "");
}

#[test]
fn test_sum_slice() {
    let arr = [10, 20, 30, 40, 50];
    assert_eq!(sum_slice(&arr), 150);
    assert_eq!(sum_slice(&arr[1..4]), 90);
    assert_eq!(sum_slice(&[]), 0);
}

#[test]
fn test_get_subslice() {
    let data = [1, 2, 3, 4, 5, 6, 7, 8];
    assert_eq!(get_subslice(&data, 2, 3), &[3, 4, 5]);
    assert_eq!(get_subslice(&data, 0, 2), &[1, 2]);
    assert_eq!(get_subslice(&data, 6, 5), &[]); // Out of bounds -> leerer Slice
    assert_eq!(get_subslice(&data, 10, 2), &[]);
}

#[test]
fn test_longest_str() {
    let word1 = "Microservice";
    let word2 = "API";
    assert_eq!(longest_str(word1, word2), "Microservice");

    let equal1 = "Rust";
    let equal2 = "GoLang";
    assert_eq!(longest_str(equal1, equal2), "GoLang");

    let tie1 = "Alpha";
    let tie2 = "Beta1";
    assert_eq!(longest_str(tie1, tie2), "Alpha"); // tie returns x
}

#[test]
fn test_strip_prefix_slice() {
    let uri = "/v1/auth/login";
    assert_eq!(strip_prefix_slice(uri, "/v1"), Some("/auth/login"));
    assert_eq!(strip_prefix_slice(uri, "/v2"), None);
    assert_eq!(strip_prefix_slice("Bearer eyJhbGciOi", "Bearer "), Some("eyJhbGciOi"));
}
