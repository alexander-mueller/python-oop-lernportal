assert.strictEqual(addieren(10, 20), 30, "addieren(10, 20) sollte 30 ergeben");
assert.strictEqual(addieren(-5, 5), 0, "addieren(-5, 5) sollte 0 ergeben");
assert.strictEqual(begruessung("Anna"), "Hallo Anna, willkommen zu JavaScript!", "begruessung() liefert falschen Text");
assert.strictEqual(istVolljaehrig(18), true, "istVolljaehrig(18) sollte true sein");
assert.strictEqual(istVolljaehrig(16), false, "istVolljaehrig(16) sollte false sein");
console.log("✅ Alle 5 JavaScript Tests erfolgreich bestanden!");
