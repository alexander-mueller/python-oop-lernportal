// 🧪 Testsuite: JS 02 - Kontrollfluss, Verzweigungen & Schleifen

// Test 1: kategorisiereAlter
assert.strictEqual(kategorisiereAlter(5), "Kind", "Alter 5 sollte 'Kind' sein");
assert.strictEqual(kategorisiereAlter(12), "Kind", "Alter 12 sollte 'Kind' sein");
assert.strictEqual(kategorisiereAlter(13), "Jugendlicher", "Alter 13 sollte 'Jugendlicher' sein");
assert.strictEqual(kategorisiereAlter(17), "Jugendlicher", "Alter 17 sollte 'Jugendlicher' sein");
assert.strictEqual(kategorisiereAlter(18), "Erwachsener", "Alter 18 sollte 'Erwachsener' sein");
assert.strictEqual(kategorisiereAlter(64), "Erwachsener", "Alter 64 sollte 'Erwachsener' sein");
assert.strictEqual(kategorisiereAlter(65), "Senior", "Alter 65 sollte 'Senior' sein");
assert.strictEqual(kategorisiereAlter(80), "Senior", "Alter 80 sollte 'Senior' sein");

// Test 2: wochentagName
assert.strictEqual(wochentagName(1), "Montag", "Tag 1 sollte 'Montag' sein");
assert.strictEqual(wochentagName(3), "Mittwoch", "Tag 3 sollte 'Mittwoch' sein");
assert.strictEqual(wochentagName(7), "Sonntag", "Tag 7 sollte 'Sonntag' sein");
assert.strictEqual(wochentagName(0), "Ungültig", "Tag 0 sollte 'Ungültig' sein");
assert.strictEqual(wochentagName(8), "Ungültig", "Tag 8 sollte 'Ungültig' sein");
assert.strictEqual(wochentagName(-2), "Ungültig", "Tag -2 sollte 'Ungültig' sein");

// Test 3: berechneRabattpreis
assert.strictEqual(berechneRabattpreis(100, true, true), 70, "100€ mit Premium & Gutschein (30%) sollte 70€ ergeben");
assert.strictEqual(berechneRabattpreis(100, true, false), 80, "100€ nur Premium (20%) sollte 80€ ergeben");
assert.strictEqual(berechneRabattpreis(100, false, true), 90, "100€ nur Gutschein (10%) sollte 90€ ergeben");
assert.strictEqual(berechneRabattpreis(100, false, false), 100, "100€ ohne Rabatte sollte 100€ ergeben");
assert.strictEqual(berechneRabattpreis(50, true, true), 35, "50€ mit 30% Rabatt sollte 35€ ergeben");

// Test 4: summeGeraderZahlen
assert.strictEqual(summeGeraderZahlen(1, 10), 30, "Summe gerader Zahlen 1 bis 10 (2+4+6+8+10) sollte 30 sein");
assert.strictEqual(summeGeraderZahlen(1, 1), 0, "Summe gerader Zahlen von 1 bis 1 sollte 0 sein");
assert.strictEqual(summeGeraderZahlen(2, 2), 2, "Summe gerader Zahlen von 2 bis 2 sollte 2 sein");
assert.strictEqual(summeGeraderZahlen(4, 8), 18, "Summe gerader Zahlen 4 bis 8 (4+6+8) sollte 18 sein");
assert.strictEqual(summeGeraderZahlen(5, 5), 0, "Summe gerader Zahlen 5 bis 5 sollte 0 sein");

// Test 5: findeErstesVielfaches
assert.strictEqual(findeErstesVielfaches([7, 14, 21], 7), 7, "Erstes Vielfaches von 7 in [7, 14, 21] sollte 7 sein");
assert.strictEqual(findeErstesVielfaches([5, 11, 18, 25], 6), 18, "Erstes Vielfaches von 6 in [5, 11, 18, 25] sollte 18 sein");
assert.strictEqual(findeErstesVielfaches([1, 3, 5, 7], 2), null, "Kein Vielfaches von 2 vorhanden, sollte null sein");
assert.strictEqual(findeErstesVielfaches([], 5), null, "Leeres Array sollte null liefern");
assert.strictEqual(findeErstesVielfaches([10, 20, 30], 5), 10, "Erstes Vielfaches von 5 in [10, 20, 30] sollte 10 sein");

console.log("✅ Alle 28 JavaScript Tests in JS 02 erfolgreich bestanden!");
