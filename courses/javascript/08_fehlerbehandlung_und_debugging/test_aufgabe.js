// 🧪 JS 08: Testsuite für Fehlerbehandlung, Debugging & Error-Klassen

if (typeof assert === "undefined") {
  var assert = require("assert");
}

// ==========================================
// 1. Tests für die Error-Klassenhierarchie
// ==========================================
const appErr = new AnwendungsFehler("Basis Anwendungsfehler");
assert.ok(appErr instanceof Error, "AnwendungsFehler muss von Error erben");
assert.ok(appErr instanceof AnwendungsFehler, "appErr muss Instanz von AnwendungsFehler sein");
assert.strictEqual(appErr.name, "AnwendungsFehler", "appErr.name sollte 'AnwendungsFehler' sein");
assert.strictEqual(appErr.message, "Basis Anwendungsfehler", "appErr.message prüfen");

const valErr = new ValidierungsFehler("Ungültige E-Mail", "email");
assert.ok(valErr instanceof Error, "ValidierungsFehler erbt von Error");
assert.ok(valErr instanceof AnwendungsFehler, "ValidierungsFehler erbt von AnwendungsFehler");
assert.ok(valErr instanceof ValidierungsFehler, "valErr ist Instanz von ValidierungsFehler");
assert.strictEqual(valErr.name, "ValidierungsFehler", "valErr.name sollte 'ValidierungsFehler' sein");
assert.strictEqual(valErr.feld, "email", "valErr.feld sollte 'email' sein");

const gutErr = new GuthabenFehler("Zu wenig Geld", 50, 100);
assert.ok(gutErr instanceof Error, "GuthabenFehler erbt von Error");
assert.ok(gutErr instanceof AnwendungsFehler, "GuthabenFehler erbt von AnwendungsFehler");
assert.ok(gutErr instanceof GuthabenFehler, "gutErr ist Instanz von GuthabenFehler");
assert.strictEqual(gutErr.name, "GuthabenFehler", "gutErr.name sollte 'GuthabenFehler' sein");
assert.strictEqual(gutErr.saldo, 50, "gutErr.saldo sollte 50 sein");
assert.strictEqual(gutErr.betrag, 100, "gutErr.betrag sollte 100 sein");

// ==========================================
// 2. Tests für sichereDivision
// ==========================================
assert.strictEqual(sichereDivision(10, 2), 5, "sichereDivision(10, 2) sollte 5 ergeben");
assert.strictEqual(sichereDivision(-20, 4), -5, "sichereDivision(-20, 4) sollte -5 ergeben");

// Division durch Null
let divNullGefangen = false;
try {
  sichereDivision(10, 0);
} catch (err) {
  divNullGefangen = true;
  assert.ok(err instanceof AnwendungsFehler, "Division durch Null sollte AnwendungsFehler werfen");
}
assert.ok(divNullGefangen, "Division durch 0 muss einen Fehler werfen");

// Ungültige Typen
let invalidTypeGefangen = false;
try {
  sichereDivision("abc", 2);
} catch (err) {
  invalidTypeGefangen = true;
  assert.ok(err instanceof ValidierungsFehler, "Nicht-Zahlen sollten ValidierungsFehler werfen");
}
assert.ok(invalidTypeGefangen, "sichereDivision mit Strings muss ValidierungsFehler werfen");

// ==========================================
// 3. Tests für parseBenutzerJson
// ==========================================
const validJson = '{"name": "Lisa", "alter": 28}';
const userObj = parseBenutzerJson(validJson);
assert.deepStrictEqual(userObj, { name: "Lisa", alter: 28 }, "Gültiges JSON sollte geparst zurückgegeben werden");

// Syntaxfehler im JSON
let syntaxErrGefangen = false;
try {
  parseBenutzerJson('{ ungueltiges: json ]');
} catch (err) {
  syntaxErrGefangen = true;
  assert.ok(err instanceof ValidierungsFehler, "Syntaxfehler muss als ValidierungsFehler abgefangen werden");
  assert.strictEqual(err.feld, "jsonString", "Fehlerfeld bei SyntaxError sollte 'jsonString' sein");
}
assert.ok(syntaxErrGefangen, "Ungültiges JSON muss abgefangen werden");

// Fehlendes 'name' Feld
let nameErrGefangen = false;
try {
  parseBenutzerJson('{"alter": 30}');
} catch (err) {
  nameErrGefangen = true;
  assert.ok(err instanceof ValidierungsFehler, "Fehlendes 'name' muss ValidierungsFehler werfen");
  assert.strictEqual(err.feld, "name", "Fehlerfeld sollte 'name' sein");
}
assert.ok(nameErrGefangen, "Objekt ohne 'name' muss abgelehnt werden");

// ==========================================
// 4. Tests für pruefeTransaktion
// ==========================================
assert.strictEqual(pruefeTransaktion(500, 200), 300, "500 - 200 sollte Saldo 300 ergeben");
assert.strictEqual(pruefeTransaktion(100, 100), 0, "100 - 100 sollte Saldo 0 ergeben");

// Nicht genügend Guthaben
let guthabenErrGefangen = false;
try {
  pruefeTransaktion(50, 120);
} catch (err) {
  guthabenErrGefangen = true;
  assert.ok(err instanceof GuthabenFehler, "Überziehung muss GuthabenFehler werfen");
  assert.strictEqual(err.saldo, 50, "GuthabenFehler.saldo muss 50 sein");
  assert.strictEqual(err.betrag, 120, "GuthabenFehler.betrag muss 120 sein");
}
assert.ok(guthabenErrGefangen, "pruefeTransaktion bei Saldo < Betrag muss abbrechen");

// Negativer oder ungültiger Abhebebetrag
let ungueltigerBetragGefangen = false;
try {
  pruefeTransaktion(500, -20);
} catch (err) {
  ungueltigerBetragGefangen = true;
  assert.ok(err instanceof ValidierungsFehler, "Negativer Betrag muss ValidierungsFehler werfen");
  assert.strictEqual(err.feld, "abhebeBetrag", "Fehlerfeld sollte 'abhebeBetrag' sein");
}
assert.ok(ungueltigerBetragGefangen, "Negativer Betrag muss ValidierungsFehler werfen");

console.log("✅ Alle Tests in JS 08 (Fehlerbehandlung & Debugging) erfolgreich bestanden!");
