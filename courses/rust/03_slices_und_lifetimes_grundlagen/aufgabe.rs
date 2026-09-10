// 🦀 Rust 03: Slices & Lifetimes Grundlagen
// ==========================================

// 🎯 TEILZIEL 1 (TODO 1): Gib einen String-Slice auf das erste Wort zurück
// Suche das erste Leerzeichen ' ' im String.
// Wenn ein Leerzeichen gefunden wird, gib den Slice von Index 0 bis zum Leerzeichen zurück.
// Wenn kein Leerzeichen existiert, gib den gesamten String als Slice zurück.
pub fn first_word(s: &str) -> &str {
    // TODO: Ermittle das erste Wort und gib den Slice zurück
    ""
}

// 🎯 TEILZIEL 2 (TODO 2): Berechne die Summe aller Elemente in einem Array-Slice &[i32]
// Iteriere über den Slice oder nutze eine Schleife.
pub fn sum_slice(numbers: &[i32]) -> i32 {
    // TODO: Berechne und gib die Summe zurück
    0
}

// 🎯 TEILZIEL 3 (TODO 3): Erstelle einen sicheren Sub-Slice
// Parameter: arr (&[u32]), start (usize), len (usize)
// Falls `start + len > arr.len()` oder `start > arr.len()`, gib einen leeren Slice `&[]` zurück.
// Andernfalls gib `&arr[start..start + len]` zurück.
pub fn get_subslice(arr: &[u32], start: usize, len: usize) -> &[u32] {
    // TODO: Validiere Grenzen und gib den Sub-Slice zurück
    &[]
}

// 🎯 TEILZIEL 4 (TODO 4): Finde den längeren zweier String-Slices mit Lifetime-Annotation 'a
// Falls beide gleich lang sind, gib `x` zurück.
pub fn longest_str<'a>(x: &'a str, y: &'a str) -> &'a str {
    // TODO: Vergleiche Längen und gib den entsprechenden Slice mit Lifetime 'a zurück
    x
}

// 🎯 TEILZIEL 5 (TODO 5): Entferne ein Präfix und gib den Rest-Slice mit Lifetime 'a zurück
// Wenn `haystack` mit `prefix` beginnt, gib `Some(&haystack[prefix.len()..])` zurück.
// Andernfalls gib `None` zurück.
pub fn strip_prefix_slice<'a>(haystack: &'a str, prefix: &str) -> Option<&'a str> {
    // TODO: Prüfe mit starts_with und gib den Rest-Slice als Option zurück
    None
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
