/**
 * 🧪 Testsuite für JS 13: ES Module & Architektur
 */

function assertThrows(fn, msg) {
  let threw = false;
  try {
    fn();
  } catch (e) {
    threw = true;
  }
  assert.ok(threw, msg || "Erwartete Exception wurde nicht geworfen!");
}

// ----------------------------------------------------
// 1. Tests für MathModule
// ----------------------------------------------------
assert.strictEqual(MathModule.addieren(12.5, 7.5), 20, "MathModule.addieren(12.5, 7.5) sollte 20 sein");
assert.strictEqual(MathModule.subtrahieren(100, 35), 65, "MathModule.subtrahieren(100, 35) sollte 65 sein");
assert.strictEqual(MathModule.multiplizieren(6, 7), 42, "MathModule.multiplizieren(6, 7) sollte 42 sein");
assert.strictEqual(MathModule.dividieren(100, 4), 25, "MathModule.dividieren(100, 4) sollte 25 sein");
assert.strictEqual(MathModule.runden(49.994, 2), 49.99, "MathModule.runden(49.994, 2)");
assert.strictEqual(MathModule.runden(49.996, 2), 50.00, "MathModule.runden(49.996, 2)");

// Validierung & Schutz vor Division durch 0
assertThrows(() => MathModule.dividieren(10, 0), "Division durch 0 muss Error werfen");
assertThrows(() => MathModule.addieren("10", 5), "String statt Zahl muss TypeError werfen");
assertThrows(() => MathModule.multiplizieren(5, NaN), "NaN muss TypeError werfen");

// ----------------------------------------------------
// 2. Tests für FormatterModule
// ----------------------------------------------------
assert.strictEqual(
  FormatterModule.formatiereWaehrung(1250.5),
  "1.250,50 EUR",
  "formatiereWaehrung(1250.5) mit Standard EUR und Tausender-Punkt"
);
assert.strictEqual(
  FormatterModule.formatiereWaehrung(49.99, "USD"),
  "49,99 USD",
  "formatiereWaehrung(49.99, 'USD')"
);
assert.strictEqual(
  FormatterModule.formatiereWaehrung(0, "chf"),
  "0,00 CHF",
  "formatiereWaehrung(0, 'chf') sollte Währung großschreiben"
);

const testDatum = new Date(Date.UTC(2026, 7, 30));
assert.strictEqual(
  FormatterModule.formatiereDatumIso(testDatum),
  "2026-08-30",
  "formatiereDatumIso(testDatum) sollte '2026-08-30' liefern"
);

assertThrows(() => FormatterModule.formatiereWaehrung("ungültig"), "Ungültiger Betrag muss TypeError werfen");
assertThrows(() => FormatterModule.formatiereDatumIso("kein-datum"), "Ungültiges Datum muss TypeError werfen");

// ----------------------------------------------------
// 3. Tests für RechnungsEngine (Positionen)
// ----------------------------------------------------
const engine = new RechnungsEngine();

const pos1 = engine.erstellePosition("Webdesign & UI", 10, 95);
assert.strictEqual(pos1.bezeichnung, "Webdesign & UI");
assert.strictEqual(pos1.menge, 10);
assert.strictEqual(pos1.einzelpreis, 95);
assert.strictEqual(pos1.gesamtpreis, 950, "gesamtpreis sollte 10 * 95 = 950 sein");

const pos2 = engine.erstellePosition("  Hosting Setup  ", 2, 25);
assert.strictEqual(pos2.bezeichnung, "Hosting Setup", "Bezeichnung muss mit .trim() bereinigt werden");
assert.strictEqual(pos2.gesamtpreis, 50);

assertThrows(() => engine.erstellePosition("", 1, 50), "Leere Bezeichnung muss Error werfen");
assertThrows(() => engine.erstellePosition("Server", 0, 50), "Menge <= 0 muss RangeError werfen");
assertThrows(() => engine.erstellePosition("Server", 2, -10), "Negativer Preis muss RangeError werfen");

// ----------------------------------------------------
// 4. Tests für RechnungsEngine.berechneRechnung
// ----------------------------------------------------
const rechnung = engine.berechneRechnung([pos1, pos2], 19);

assert.strictEqual(rechnung.positionen.length, 2);
assert.strictEqual(rechnung.nettoSumme, 1000, "Netto-Summe 950 + 50 = 1000");
assert.strictEqual(rechnung.steuersatzProzent, 19);
assert.strictEqual(rechnung.steuerBetrag, 190, "19% Steuer auf 1000 = 190");
assert.strictEqual(rechnung.bruttoSumme, 1190, "Brutto-Summe 1000 + 190 = 1190");
assert.strictEqual(rechnung.nettoFormatiert, "1.000,00 EUR");
assert.strictEqual(rechnung.steuerFormatiert, "190,00 EUR");
assert.strictEqual(rechnung.bruttoFormatiert, "1.190,00 EUR");

// Test Leere Rechnung
const leereRechnung = engine.berechneRechnung([]);
assert.strictEqual(leereRechnung.nettoSumme, 0);
assert.strictEqual(leereRechnung.bruttoSumme, 0);
assert.strictEqual(leereRechnung.nettoFormatiert, "0,00 EUR");

// Test Dependency Injection mit Custom Mock
let mockCalcUsed = false;
const customMathMock = {
  ...MathModule,
  multiplizieren(a, b) {
    mockCalcUsed = true;
    return a * b;
  }
};
const customEngine = new RechnungsEngine(customMathMock, FormatterModule);
customEngine.erstellePosition("Test Mock", 5, 20);
assert.strictEqual(mockCalcUsed, true, "Dependency Injection sollte das übergebene Math-Modul nutzen");

console.log("✅ Alle 20 Tests für JS 13 (ES Module & Architektur) erfolgreich bestanden!");
