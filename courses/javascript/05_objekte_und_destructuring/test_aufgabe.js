// 🧪 JS 03: Testsuite für Objekte, Destructuring & Rest/Spread

// Test 1: erstelleBenutzer
const user1 = erstelleBenutzer("Max Mustermann", "max@beispiel.de");
assert.deepStrictEqual(
  user1,
  { name: "Max Mustermann", email: "max@beispiel.de", rolle: "user" },
  "erstelleBenutzer() sollte Standard-Rolle 'user' und korrekte Attribute besitzen"
);

const adminUser = erstelleBenutzer("Alice Admin", "alice@corp.de", "admin");
assert.deepStrictEqual(
  adminUser,
  { name: "Alice Admin", email: "alice@corp.de", rolle: "admin" },
  "erstelleBenutzer() sollte benutzerdefinierte Rolle 'admin' unterstützen"
);

// Test 2: extrahiereDetails
const details1 = extrahiereDetails({ name: "Anna Schmidt", email: "anna@web.de", rolle: "user" });
assert.strictEqual(
  details1,
  "Anna Schmidt (anna@web.de)",
  "extrahiereDetails() sollte 'Name (Email)' zurückgeben"
);

const details2 = extrahiereDetails({ name: "Bob", email: "bob@dev.io", alter: 30 });
assert.strictEqual(
  details2,
  "Bob (bob@dev.io)",
  "extrahiereDetails() sollte auch mit zusätzlichen Objekt-Eigenschaften funktionieren"
);

// Test 3: fuegeAdresseHinzu & Immutability Check
const basisBenutzer = { name: "Sarah", email: "sarah@mail.de" };
const adresse = { stadt: "Hamburg", plz: "20095" };
const kombiniert = fuegeAdresseHinzu(basisBenutzer, adresse);

assert.deepStrictEqual(
  kombiniert,
  { name: "Sarah", email: "sarah@mail.de", stadt: "Hamburg", plz: "20095" },
  "fuegeAdresseHinzu() sollte Benutzer und Adresse zu einem neuen Objekt verschmelzen"
);
assert.strictEqual(
  basisBenutzer.stadt,
  undefined,
  "fuegeAdresseHinzu() darf das Originalobjekt nicht mutieren (Immutability)"
);

// Test 4: zaehleEigenschaften
assert.strictEqual(zaehleEigenschaften({ a: 1, b: 2, c: 3 }), 3, "zaehleEigenschaften({a:1, b:2, c:3}) sollte 3 ergeben");
assert.strictEqual(zaehleEigenschaften({}), 0, "zaehleEigenschaften({}) für leeres Objekt sollte 0 sein");
assert.strictEqual(
  zaehleEigenschaften({ id: 101, title: "Laptop", preis: 999, verfuegbar: true }),
  4,
  "zaehleEigenschaften() sollte 4 Eigenschaften korrekt zählen"
);

// Test 5: berechneWarenkorbGesamtwert
const warenkorb = [
  { titel: "Buch", preis: 20, anzahl: 2 },
  { titel: "Maus", preis: 15, anzahl: 3 },
  { titel: "Kabel", preis: 5, anzahl: 1 }
];
assert.strictEqual(
  berechneWarenkorbGesamtwert(warenkorb),
  90,
  "berechneWarenkorbGesamtwert() sollte 20*2 + 15*3 + 5*1 = 90 berechnen"
);

const warenkorbMitDefault = [{ titel: "Monitor", preis: 199 }];
assert.strictEqual(
  berechneWarenkorbGesamtwert(warenkorbMitDefault),
  199,
  "berechneWarenkorbGesamtwert() sollte anzahl = 1 als Fallback nutzen"
);

assert.strictEqual(
  berechneWarenkorbGesamtwert([]),
  0,
  "berechneWarenkorbGesamtwert([]) für leeren Warenkorb sollte 0 sein"
);

console.log("✅ Alle 10 Tests in JS 03 erfolgreich bestanden!");
