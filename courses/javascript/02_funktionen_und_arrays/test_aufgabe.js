assert.deepStrictEqual(verdoppeln([1, 2, 3]), [2, 4, 6], "verdoppeln([1, 2, 3]) sollte [2, 4, 6] sein");
assert.deepStrictEqual(filterGeradeZahlen([1, 2, 3, 4, 5, 6]), [2, 4, 6], "filterGeradeZahlen() filtert unvollständig");
assert.strictEqual(arraySumme([10, 20, 30]), 60, "arraySumme([10, 20, 30]) sollte 60 sein");
assert.strictEqual(arraySumme([]), 0, "arraySumme([]) sollte 0 sein");
console.log("✅ Alle 4 JavaScript Tests in JS 02 erfolgreich bestanden!");
