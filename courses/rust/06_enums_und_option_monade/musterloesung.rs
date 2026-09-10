#[derive(Debug, PartialEq)]
pub enum Status {
    Aktiv,
    Gesperrt(String),
}

pub fn sichere_division(a: f64, b: f64) -> Option<f64> {
    if b == 0.0 {
        None
    } else {
        Some(a / b)
    }
}