// Hilfsfunktion für Fehler-Prüfung
async function pruefeReject(promise, expectedMsg, beschreibung) {
  let threw = false;
  let caughtErr = null;
  try {
    await promise;
  } catch (err) {
    threw = true;
    caughtErr = err;
    if (expectedMsg && !String(err && (err.message || err)).includes(expectedMsg)) {
      throw new Error(`${beschreibung}: Erwartete Fehlermeldung "${expectedMsg}", aber erhalten: "${err ? err.message : err}"`);
    }
  }
  if (!threw) {
    throw new Error(`${beschreibung}: Funktion sollte Fehler werfen / rejecten, war aber erfolgreich.`);
  }
}

// ----------------------------------------------------
// Mock-APIs definieren
// ----------------------------------------------------
const mockWetterApi = async (stadt) => {
  if (stadt === "Berlin") {
    return {
      ok: true,
      status: 200,
      json: async () => ({ stadt: "Berlin", temperatur: 21, wetterlage: "Sonnig", feuchtigkeit: "55%" })
    };
  } else if (stadt === "München") {
    return {
      ok: true,
      status: 200,
      json: async () => ({ stadt: "München", temperatur: 18, wetterlage: "Regnerisch" })
    };
  } else {
    return {
      ok: false,
      status: 404,
      json: async () => ({ fehler: "Stadt nicht gefunden" })
    };
  }
};

const mockPostApi = async (userId) => {
  if (userId === 10) {
    return {
      ok: true,
      status: 200,
      json: async () => [
        { id: 1, titel: "Einführung in JS" },
        { id: 2, titel: "Async Await Guide" },
        { id: 3, titel: "REST-APIs verstehen" }
      ]
    };
  } else if (userId === 99) {
    return [
      { id: 4, titel: "Einzelbeitrag" }
    ];
  } else {
    return {
      ok: true,
      status: 200,
      json: async () => []
    };
  }
};

// ----------------------------------------------------
// 1. Test: holeWetterDaten (Erfolg)
// ----------------------------------------------------
const wetterBerlin = await holeWetterDaten("Berlin", mockWetterApi);
assert.deepStrictEqual(
  wetterBerlin,
  { stadt: "Berlin", temperatur: 21, wetterlage: "Sonnig" },
  "holeWetterDaten('Berlin') liefert unerwartetes Wetter-Objekt"
);

const wetterMuenchen = await holeWetterDaten("München", mockWetterApi);
assert.strictEqual(wetterMuenchen.temperatur, 18, "Temperatur für München sollte 18 sein");
assert.strictEqual(wetterMuenchen.wetterlage, "Regnerisch", "Wetterlage für München sollte Regnerisch sein");

// ----------------------------------------------------
// 2. Test: holeWetterDaten (404 Fehler)
// ----------------------------------------------------
await pruefeReject(
  holeWetterDaten("Atlantis", mockWetterApi),
  "Atlantis",
  "holeWetterDaten für unbekannte Stadt muss Fehler werfen"
);

// ----------------------------------------------------
// 3. Test: aggregiereBenutzerPosts
// ----------------------------------------------------
const posts10 = await aggregiereBenutzerPosts(10, mockPostApi);
assert.deepStrictEqual(
  posts10,
  {
    userId: 10,
    anzahlPosts: 3,
    postTitel: ["Einführung in JS", "Async Await Guide", "REST-APIs verstehen"]
  },
  "aggregiereBenutzerPosts(10) liefert falsches Aggregat"
);

const posts99 = await aggregiereBenutzerPosts(99, mockPostApi);
assert.strictEqual(posts99.anzahlPosts, 1, "User 99 sollte genau 1 Post haben");
assert.deepStrictEqual(posts99.postTitel, ["Einzelbeitrag"], "Post-Titel für User 99 fehlerhaft");

const postsLeer = await aggregiereBenutzerPosts(999, mockPostApi);
assert.strictEqual(postsLeer.anzahlPosts, 0, "User 999 sollte 0 Posts haben");
assert.deepStrictEqual(postsLeer.postTitel, [], "Leere Post-Titel-Liste erwartet");

// ----------------------------------------------------
// 4. Test: sichererApiAufruf
// ----------------------------------------------------
// 4a: Erfolgreiches Promise
const ergErfolg = await sichererApiAufruf(Promise.resolve("Daten geladen!"), "Standard");
assert.strictEqual(ergErfolg, "Daten geladen!", "sichererApiAufruf sollte den aufgelösten Wert zurückgeben");

// 4b: Fehlgeschlagenes Promise (muss abgefangen werden)
const ergFehler = await sichererApiAufruf(
  Promise.reject(new Error("Netzwerk-Timeout")),
  "Standard-Fallback"
);
assert.strictEqual(ergFehler, "Standard-Fallback", "sichererApiAufruf sollte Fallback zurückgeben bei Rejection");

// 4c: Async Funktion, die eine Exception wirft
const ergFnFehler = await sichererApiAufruf(
  async () => { throw new Error("Kritischer API Crash"); },
  { status: "offline", data: [] }
);
assert.deepStrictEqual(
  ergFnFehler,
  { status: "offline", data: [] },
  "sichererApiAufruf sollte Fallback-Objekt bei geworfenem Fehler liefern"
);

console.log("✅ Alle Tests in JS 06 (Async/Await & REST-APIs) erfolgreich bestanden!");
