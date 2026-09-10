#[derive(Debug, PartialEq)]
pub struct BankKonto {
    pub inhaber: String,
    saldo: f64,
}

impl BankKonto {
    // 🎯 TEILZIEL 1 (TODO 1): Konstruktor new()
    pub fn new(inhaber: String, start_saldo: f64) -> Self {
        // TODO: Implementieren
        Self { inhaber, saldo: 0.0 }
    }

    // 🎯 TEILZIEL 2 (TODO 2): Einzahlen & Abheben
    pub fn einzahlen(&mut self, betrag: f64) -> bool {
        // TODO: Implementieren
        false
    }

    pub fn get_saldo(&self) -> f64 {
        self.saldo
    }
}