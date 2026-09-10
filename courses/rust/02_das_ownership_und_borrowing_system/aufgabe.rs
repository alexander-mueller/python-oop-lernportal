// 🦀 Rust 02: Das Ownership & Borrowing System
// ============================================

// 🎯 TEILZIEL 1 (TODO 1): Ermittle die Länge eines Strings via unveränderlicher Referenz (&String)
// Da nur eine Referenz übergeben wird, behält der Aufrufer die Ownership!
pub fn calculate_length_borrow(s: &String) -> usize {
    // TODO: Gib die Länge des Strings zurück
    0
}

// 🎯 TEILZIEL 2 (TODO 2): Hänge einen Sicherheitstag an einen String in-place an (&mut String)
// Nutze `.push_str()` auf der veränderbaren Referenz.
pub fn append_security_tag(s: &mut String, tag: &str) {
    // TODO: Hänge `tag` an `s` an
}

// 🎯 TEILZIEL 3 (TODO 3): Übernimm die volle Ownership des Strings und bette ihn ein
// Da `s` als Wert übergeben wird (ohne &), wandert die Ownership in diese Funktion.
// Gib einen neuen String zurück im Format: "{prefix}{s}{suffix}"
pub fn take_ownership_and_wrap(s: String, prefix: &str, suffix: &str) -> String {
    // TODO: Erstelle den formatierten String und gib ihn zurück
    String::new()
}

// 🎯 TEILZIEL 4 (TODO 4): Erstelle einen Klon via .clone(), konvertiere ihn zu Uppercase
// und gib ein Tupel (neuer_string, ursprüngliche_länge) zurück.
pub fn clone_and_transform(s: &String) -> (String, usize) {
    // TODO: Klone s, wandle ihn in Großbuchstaben (.to_uppercase()) und gib das Tupel zurück
    (String::new(), 0)
}

// 🎯 TEILZIEL 5 (TODO 5): Tausche die Werte zweier Integer-Referenzen in-place
// Nutze eine temporäre Variable oder std::mem::swap, um die Werte an den Zeigern zu tauschen.
pub fn swap_values(a: &mut i32, b: &mut i32) {
    // TODO: Tausche die Werte von a und b
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
