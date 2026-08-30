/**
 * 🧪 Testsuite für JS 10: Web Storage & JSON Serialisierung
 */

function createMockStorage() {
  const store = new Map();
  return {
    getItem(key) {
      return store.has(String(key)) ? store.get(String(key)) : null;
    },
    setItem(key, value) {
      store.set(String(key), String(value));
    },
    removeItem(key) {
      store.delete(String(key));
    },
    clear() {
      store.clear();
    },
    get length() {
      return store.size;
    }
  };
}

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
// 1. Tests für speichereDaten(schluessel, daten, storageMock)
// ----------------------------------------------------
const mock1 = createMockStorage();
const benutzerObjekt = { id: 42, name: "Ada Lovelace", isAdmin: true, rollen: ["dev", "admin"] };

const gespeichert = speichereDaten("user_ada", benutzerObjekt, mock1);
assert.strictEqual(gespeichert, true, "speichereDaten sollte bei Erfolg true zurückgeben");

const gespeicherterRawString = mock1.getItem("user_ada");
assert.ok(gespeicherterRawString !== null, "Der Wert muss im Storage vorhanden sein");
assert.strictEqual(
  gespeicherterRawString,
  JSON.stringify(benutzerObjekt),
  "Die Daten müssen als gültiger JSON-String serialisiert abgelegt werden"
);

// Zahl und Boolean speichern
speichereDaten("app_volume", 85, mock1);
assert.strictEqual(mock1.getItem("app_volume"), "85", "Zahlen müssen als JSON-String gespeichert werden");

speichereDaten("dark_mode", true, mock1);
assert.strictEqual(mock1.getItem("dark_mode"), "true", "Booleans müssen als JSON-String gespeichert werden");

// Validierung: Leerer Schlüssel muss TypeError werfen
assertThrows(() => speichereDaten("", { a: 1 }, mock1), "Leerer Schlüssel muss TypeError werfen");
assertThrows(() => speichereDaten(null, { a: 1 }, mock1), "null als Schlüssel muss TypeError werfen");

// ----------------------------------------------------
// 2. Tests für ladeDaten(schluessel, standardWert, storageMock)
// ----------------------------------------------------
const mock2 = createMockStorage();
mock2.setItem("einstellungen", JSON.stringify({ theme: "dark", fontSize: 16 }));

const geladeneEinstellungen = ladeDaten("einstellungen", {}, mock2);
assert.deepStrictEqual(
  geladeneEinstellungen,
  { theme: "dark", fontSize: 16 },
  "ladeDaten() sollte das JSON-Objekt korrekt rekonstruieren"
);

// Fallback bei nicht existierendem Schlüssel
const nichtVorhanden = ladeDaten("unbekannter_schluessel", "Standard-Wert", mock2);
assert.strictEqual(nichtVorhanden, "Standard-Wert", "Nicht existierender Schlüssel liefert standardWert");

const nichtVorhandenNull = ladeDaten("gibts_nicht", null, mock2);
assert.strictEqual(nichtVorhandenNull, null, "Default standardWert ist null");

// Fehlerbehandlung: Defektes JSON im Storage abfangen
mock2.setItem("defekter_eintrag", "{ name: 'Fehlerhaftes JSON ohne Anfuehrungszeichen'");
const geladenDefekt = ladeDaten("defekter_eintrag", { repariert: true }, mock2);
assert.deepStrictEqual(
  geladenDefekt,
  { repariert: true },
  "Bei SyntaxError in JSON.parse muss standardWert zurückgegeben werden"
);

// ----------------------------------------------------
// 3. Tests für loescheDaten(schluessel, storageMock)
// ----------------------------------------------------
const mock3 = createMockStorage();
mock3.setItem("session_token", "secret_12345");
assert.strictEqual(mock3.getItem("session_token"), "secret_12345");

const geloescht = loescheDaten("session_token", mock3);
assert.strictEqual(geloescht, true, "loescheDaten sollte true zurückgeben");
assert.strictEqual(mock3.getItem("session_token"), null, "Eintrag muss nach dem Löschen gelöscht sein");

const loescheUngueltig = loescheDaten("", mock3);
assert.strictEqual(loescheUngueltig, false, "Ungültiger Schlüssel liefert false");

// ----------------------------------------------------
// 4. Tests für aktualisiereHighscore(spielerName, punkte, storageMock)
// ----------------------------------------------------
const mock4 = createMockStorage();

// Erster Eintrag
const score1 = aktualisiereHighscore("Alice", 1500, mock4);
assert.strictEqual(score1.length, 1, "Erste Bestenliste hat 1 Eintrag");
assert.strictEqual(score1[0].name, "Alice");
assert.strictEqual(score1[0].punkte, 1500);
assert.ok(typeof score1[0].datum === "string", "Eintrag muss ein ISO-Datum haben");

// Zweiter Eintrag mit höherer Punktzahl -> Muss an Index 0 stehen
const score2 = aktualisiereHighscore("Bob", 2800, mock4);
assert.strictEqual(score2.length, 2, "Bestenliste hat nun 2 Einträge");
assert.strictEqual(score2[0].name, "Bob", "Höhere Punktzahl muss an erster Stelle stehen");
assert.strictEqual(score2[0].punkte, 2800);
assert.strictEqual(score2[1].name, "Alice");
assert.strictEqual(score2[1].punkte, 1500);

// Dritter Eintrag mit mittlerer Punktzahl
const score3 = aktualisiereHighscore("  Charlie  ", 2100, mock4);
assert.strictEqual(score3.length, 3);
assert.strictEqual(score3[0].name, "Bob");
assert.strictEqual(score3[1].name, "Charlie", "Name muss mit .trim() bereinigt werden");
assert.strictEqual(score3[1].punkte, 2100);
assert.strictEqual(score3[2].name, "Alice");

// Prüfung ob Bestenliste im Storage persistiert wurde
const persistierteScores = ladeDaten("highscores", [], mock4);
assert.strictEqual(persistierteScores.length, 3, "Highscores müssen im Storage gespeichert sein");
assert.strictEqual(persistierteScores[0].name, "Bob");

// Test Begrenzung auf Top 10
for (let i = 1; i <= 15; i++) {
  aktualisiereHighscore(`Player_${i}`, i * 100, mock4);
}
const topScores = ladeDaten("highscores", [], mock4);
assert.strictEqual(topScores.length, 10, "Highscore-Liste darf maximal 10 Einträge umfassen");
assert.ok(topScores[0].punkte >= topScores[1].punkte, "Bestenliste muss absteigend sortiert sein");

// Validierungstests
assertThrows(() => aktualisiereHighscore("", 500, mock4), "Leerer Spielername muss TypeError werfen");
assertThrows(() => aktualisiereHighscore("Dave", -10, mock4), "Negative Punkte müssen TypeError werfen");
assertThrows(() => aktualisiereHighscore("Dave", NaN, mock4), "NaN als Punktzahl muss TypeError werfen");

console.log("✅ Alle 16 Tests für JS 10 (Web Storage & JSON Serialisierung) erfolgreich bestanden!");
