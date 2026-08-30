// 🧪 Testsuite: JS 03 - Funktionen, Scope & Closures

// Test 1: erstelleZaehler (Standardwert 0)
const z1 = erstelleZaehler();
assert.strictEqual(z1(), 1, "Erster Aufruf von erstelleZaehler() sollte 1 zurückgeben");
assert.strictEqual(z1(), 2, "Zweiter Aufruf von erstelleZaehler() sollte 2 zurückgeben");
assert.strictEqual(z1(), 3, "Dritter Aufruf von erstelleZaehler() sollte 3 zurückgeben");

// Test 1b: erstelleZaehler mit Startwert 10
const z2 = erstelleZaehler(10);
assert.strictEqual(z2(), 11, "Erster Aufruf von erstelleZaehler(10) sollte 11 zurückgeben");
assert.strictEqual(z2(), 12, "Zweiter Aufruf von erstelleZaehler(10) sollte 12 zurückgeben");

// Test 1c: Closure-Isolation (z1 und z2 dürfen sich nicht gegenseitig beeinflussen)
assert.strictEqual(z1(), 4, "z1 sollte unabhängig von z2 weiterzählen (erwartet: 4)");

// Test 2: multiplizierer
const verdopple = multiplizierer(2);
assert.strictEqual(verdopple(5), 10, "verdopple(5) sollte 10 sein");
assert.strictEqual(verdopple(0), 0, "verdopple(0) sollte 0 sein");
assert.strictEqual(verdopple(-4), -8, "verdopple(-4) sollte -8 sein");

const verdreifache = multiplizierer(3);
assert.strictEqual(verdreifache(4), 12, "verdreifache(4) sollte 12 sein");

const halbiere = multiplizierer(0.5);
assert.strictEqual(halbiere(20), 10, "halbiere(20) sollte 10 sein");

// Test 3: summiereAlles (Rest-Parameter)
assert.strictEqual(summiereAlles(), 0, "summiereAlles() ohne Argumente sollte 0 sein");
assert.strictEqual(summiereAlles(42), 42, "summiereAlles(42) sollte 42 sein");
assert.strictEqual(summiereAlles(1, 2, 3, 4, 5), 15, "summiereAlles(1, 2, 3, 4, 5) sollte 15 sein");
assert.strictEqual(summiereAlles(10, -5, 3), 8, "summiereAlles(10, -5, 3) sollte 8 sein");

// Test 4: erstellePraefixierer
const mitEuro = erstellePraefixierer("€ ");
assert.strictEqual(mitEuro("100"), "€ 100", "mitEuro('100') sollte '€ 100' sein");
assert.strictEqual(mitEuro("0"), "€ 0", "mitEuro('0') sollte '€ 0' sein");

const mitHttps = erstellePraefixierer("https://");
assert.strictEqual(mitHttps("github.com"), "https://github.com", "mitHttps('github.com') sollte 'https://github.com' sein");
assert.strictEqual(mitHttps("developer.mozilla.org"), "https://developer.mozilla.org", "mitHttps('developer.mozilla.org') sollte 'https://developer.mozilla.org' sein");

console.log("✅ Alle 18 JavaScript Tests in JS 03 erfolgreich bestanden!");
