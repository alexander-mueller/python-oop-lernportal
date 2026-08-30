// 🧪 JS 06: Testsuite für Klassen, OOP, Vererbung & Methoden

if (typeof assert === "undefined") {
  var assert = require("assert");
}

function pruefeFehler(fn, beschreibung) {
  let threw = false;
  try {
    fn();
  } catch (e) {
    threw = true;
  }
  assert.ok(threw, `${beschreibung} sollte einen Fehler werfen!`);
}

// ==========================================
// 1. Tests für Bankkonto
// ==========================================
const konto1 = new Bankkonto("Alice Schmidt");
assert.strictEqual(konto1.inhaber, "Alice Schmidt", "Bankkonto sollte korrekten Inhaber besitzen");
assert.strictEqual(konto1.saldo, 0, "Standard-Startsaldo sollte 0 sein");

const konto2 = new Bankkonto("Bob Berger", 250);
assert.strictEqual(konto2.saldo, 250, "Bankkonto sollte initialen Saldo von 250 haben");

// Einzahlen
const nachEinzahlung = konto2.einzahlen(150);
assert.strictEqual(nachEinzahlung, 400, "einzahlen(150) sollte neuen Saldo 400 zurückgeben");
assert.strictEqual(konto2.saldo, 400, "konto.saldo sollte nach Einzahlung 400 betragen");

pruefeFehler(() => konto2.einzahlen(0), "einzahlen(0)");
pruefeFehler(() => konto2.einzahlen(-50), "einzahlen(-50)");

// Abheben
const nachAbhebung = konto2.abheben(100);
assert.strictEqual(nachAbhebung, 300, "abheben(100) sollte neuen Saldo 300 zurückgeben");
assert.strictEqual(konto2.saldo, 300, "konto.saldo sollte nach Abhebung 300 betragen");

pruefeFehler(() => konto2.abheben(0), "abheben(0)");
pruefeFehler(() => konto2.abheben(-20), "abheben(-20)");
pruefeFehler(() => konto2.abheben(999), "abheben(999) bei Saldo 300");

// ==========================================
// 2. Tests für Fahrzeug
// ==========================================
const fahrzeug = new Fahrzeug("Volkswagen", "Golf 8", 2021);
assert.strictEqual(fahrzeug.marke, "Volkswagen", "Fahrzeug sollte Marke 'Volkswagen' besitzen");
assert.strictEqual(fahrzeug.modell, "Golf 8", "Fahrzeug sollte Modell 'Golf 8' besitzen");
assert.strictEqual(fahrzeug.baujahr, 2021, "Fahrzeug sollte Baujahr 2021 besitzen");
assert.strictEqual(
  fahrzeug.beschreibung(),
  "Volkswagen Golf 8 (2021)",
  "Fahrzeug.beschreibung() sollte 'Marke Modell (Baujahr)' zurückgeben"
);

// ==========================================
// 3. Tests für ElektroAuto (Vererbung & Methoden)
// ==========================================
const eAuto = new ElektroAuto("Hyundai", "Ioniq 5", 2023, 77.4);

assert.ok(eAuto instanceof ElektroAuto, "eAuto sollte Instanz von ElektroAuto sein");
assert.ok(eAuto instanceof Fahrzeug, "eAuto sollte via Vererbung Instanz von Fahrzeug sein");

assert.strictEqual(eAuto.marke, "Hyundai", "ElektroAuto erbt marke");
assert.strictEqual(eAuto.modell, "Ioniq 5", "ElektroAuto erbt modell");
assert.strictEqual(eAuto.baujahr, 2023, "ElektroAuto erbt baujahr");
assert.strictEqual(eAuto.batterieKapazitaet, 77.4, "ElektroAuto besitzt batterieKapazitaet");

assert.strictEqual(
  eAuto.beschreibung(),
  "Hyundai Ioniq 5 (2023) [Elektro: 77.4 kWh]",
  "ElektroAuto.beschreibung() sollte erweiterte Beschreibung liefern"
);

// Reichweitenberechnung: (77.4 kWh / 15.48 kWh/100km) * 100 = 500 km
const reichweite = eAuto.reichweiteBerechnen(15.48);
assert.strictEqual(Math.round(reichweite), 500, "reichweiteBerechnen(15.48) sollte 500 km ergeben");

pruefeFehler(() => eAuto.reichweiteBerechnen(0), "reichweiteBerechnen(0)");
pruefeFehler(() => eAuto.reichweiteBerechnen(-10), "reichweiteBerechnen(-10)");

// ==========================================
// 4. Tests für Statische Fabrikmethode
// ==========================================
const standardTesla = ElektroAuto.erstelleStandardTesla();
assert.ok(standardTesla instanceof ElektroAuto, "erstelleStandardTesla() muss ein ElektroAuto zurückgeben");
assert.strictEqual(standardTesla.marke, "Tesla", "Tesla Marke sollte 'Tesla' sein");
assert.strictEqual(standardTesla.modell, "Model 3", "Tesla Modell sollte 'Model 3' sein");
assert.strictEqual(standardTesla.baujahr, 2024, "Tesla Baujahr sollte 2024 sein");
assert.strictEqual(standardTesla.batterieKapazitaet, 75, "Tesla Batteriekapazität sollte 75 sein");
assert.strictEqual(
  standardTesla.beschreibung(),
  "Tesla Model 3 (2024) [Elektro: 75 kWh]",
  "Tesla beschreibung() prüfen"
);
assert.strictEqual(
  standardTesla.reichweiteBerechnen(15),
  500,
  "Tesla Reichweite bei 15 kWh/100km sollte (75/15)*100 = 500 km sein"
);

console.log("✅ Alle Tests in JS 06 (Klassen & OOP) erfolgreich bestanden!");
