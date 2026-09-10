#[derive(Debug, PartialEq)]
pub struct BankKonto {
    pub inhaber: String,
    saldo: f64,
}

impl BankKonto {
    pub fn new(inhaber: String, start_saldo: f64) -> Self {
        Self { inhaber, saldo: start_saldo }
    }

    pub fn einzahlen(&mut self, betrag: f64) -> bool {
        if betrag > 0.0 {
            self.saldo += betrag;
            true
        } else {
            false
        }
    }

    pub fn get_saldo(&self) -> f64 {
        self.saldo
    }
}