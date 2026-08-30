// 🧪 Testsuite: JS 04 - Arrays, Sets & Maps

// Test 1: verdoppeln
assert.deepStrictEqual(verdoppeln([1, 2, 3]), [2, 4, 6], "verdoppeln([1, 2, 3]) sollte [2, 4, 6] sein");
assert.deepStrictEqual(verdoppeln([]), [], "verdoppeln([]) sollte [] sein");
assert.deepStrictEqual(verdoppeln([-2, 0, 5]), [-4, 0, 10], "verdoppeln([-2, 0, 5]) sollte [-4, 0, 10] sein");

// Test 2: filterGeradeZahlen
assert.deepStrictEqual(filterGeradeZahlen([1, 2, 3, 4, 5, 6]), [2, 4, 6], "filterGeradeZahlen() filtert unvollständig");
assert.deepStrictEqual(filterGeradeZahlen([1, 3, 5]), [], "filterGeradeZahlen([1, 3, 5]) sollte [] sein");
assert.deepStrictEqual(filterGeradeZahlen([]), [], "filterGeradeZahlen([]) sollte [] sein");

// Test 3: arraySumme
assert.strictEqual(arraySumme([10, 20, 30]), 60, "arraySumme([10, 20, 30]) sollte 60 sein");
assert.strictEqual(arraySumme([]), 0, "arraySumme([]) sollte 0 sein");
assert.strictEqual(arraySumme([5]), 5, "arraySumme([5]) sollte 5 sein");

// Test 4: entferneDuplikate (Set)
assert.deepStrictEqual(entferneDuplikate([1, 2, 2, 3, 1, 4]), [1, 2, 3, 4], "entferneDuplikate([1, 2, 2, 3, 1, 4]) sollte [1, 2, 3, 4] sein");
assert.deepStrictEqual(entferneDuplikate(["a", "b", "a", "c", "b"]), ["a", "b", "c"], "entferneDuplikate mit Strings fehlerhaft");
assert.deepStrictEqual(entferneDuplikate([]), [], "entferneDuplikate([]) sollte [] sein");

// Test 5: erstelleWoerterbuch (Map)
const wb = erstelleWoerterbuch([["de", "Hallo"], ["en", "Hello"], ["es", "Hola"]]);
assert.ok(wb instanceof Map, "erstelleWoerterbuch() muss eine Instanz von Map zurückgeben");
assert.strictEqual(wb.size, 3, "Map sollte 3 Einträge enthalten");
assert.strictEqual(wb.get("de"), "Hallo", "Map.get('de') sollte 'Hallo' sein");
assert.strictEqual(wb.get("en"), "Hello", "Map.get('en') sollte 'Hello' sein");
assert.strictEqual(wb.get("es"), "Hola", "Map.get('es') sollte 'Hola' sein");
assert.strictEqual(wb.has("fr"), false, "Map.has('fr') sollte false sein");

// Test 6: zaehleHaeufigkeiten (Map)
const counts = zaehleHaeufigkeiten(["apfel", "banane", "apfel", "orange", "banane", "apfel"]);
assert.ok(counts instanceof Map, "zaehleHaeufigkeiten() muss eine Map zurückgeben");
assert.strictEqual(counts.size, 3, "Map sollte 3 unterschiedliche Früchte enthalten");
assert.strictEqual(counts.get("apfel"), 3, "Apfel sollte 3x gezählt werden");
assert.strictEqual(counts.get("banane"), 2, "Banane sollte 2x gezählt werden");
assert.strictEqual(counts.get("orange"), 1, "Orange sollte 1x gezählt werden");

const emptyCounts = zaehleHaeufigkeiten([]);
assert.ok(emptyCounts instanceof Map, "Leeres Array muss eine leere Map zurückgeben");
assert.strictEqual(emptyCounts.size, 0, "Leere Map sollte size 0 haben");

console.log("✅ Alle 21 JavaScript Tests in JS 04 erfolgreich bestanden!");
