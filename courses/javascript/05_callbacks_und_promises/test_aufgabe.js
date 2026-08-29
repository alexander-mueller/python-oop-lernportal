// Hilfsfunktion zur Rejection-Prüfung
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
    throw new Error(`${beschreibung}: Promise sollte abgewiesen werden (reject), wurde aber erfolgreich aufgelöst.`);
  }
}

// 1. Test: verzoegereAusfuehrung
const erg1 = await verzoegereAusfuehrung(20, "Erfolg 20ms");
assert.strictEqual(erg1, "Erfolg 20ms", "verzoegereAusfuehrung liefert falschen Wert nach Ablauf des Timers");

// 2. Test: pruefeZahlGroesserNull bei positiver Zahl
const erg2 = await pruefeZahlGroesserNull(42);
assert.strictEqual(erg2, 42, "pruefeZahlGroesserNull(42) sollte mit 42 resolven");

// 3. Test: pruefeZahlGroesserNull bei 0 und negativer Zahl
await pruefeReject(
  pruefeZahlGroesserNull(-5),
  "Zahl muss größer als 0 sein",
  "pruefeZahlGroesserNull(-5)"
);
await pruefeReject(
  pruefeZahlGroesserNull(0),
  "Zahl muss größer als 0 sein",
  "pruefeZahlGroesserNull(0)"
);

// 4. Test: ladeBenutzerProfil mit gültiger ID
const profil = await ladeBenutzerProfil(101);
assert.deepStrictEqual(
  profil,
  { id: 101, name: "Benutzer_101", status: "aktiv" },
  "ladeBenutzerProfil(101) liefert falsches Profil-Objekt"
);

// 5. Test: ladeBenutzerProfil mit ungültiger ID
await pruefeReject(
  ladeBenutzerProfil(0),
  "Ungültige User-ID",
  "ladeBenutzerProfil(0)"
);
await pruefeReject(
  ladeBenutzerProfil(-10),
  "Ungültige User-ID",
  "ladeBenutzerProfil(-10)"
);

// 6. Test: ladeAlleDatenQuellen mit zwei erfolgreichen Promises (Promise.all)
const pA = verzoegereAusfuehrung(15, "Sensordaten Alpha");
const pB = verzoegereAusfuehrung(10, "Sensordaten Beta");
const alleQuellen = await ladeAlleDatenQuellen(pA, pB);
assert.deepStrictEqual(
  alleQuellen,
  ["Sensordaten Alpha", "Sensordaten Beta"],
  "ladeAlleDatenQuellen sollte alle Ergebnisse im Array zusammenfassen"
);

// 7. Test: ladeAlleDatenQuellen mit einem abgewiesenen Promise
const pGut = verzoegereAusfuehrung(10, "Gute Daten");
const pSchlecht = pruefeZahlGroesserNull(-100);
await pruefeReject(
  ladeAlleDatenQuellen(pGut, pSchlecht),
  "Zahl muss größer als 0 sein",
  "ladeAlleDatenQuellen mit abgewiesenem Promise"
);

console.log("✅ Alle 7 Asynchronitäts- und Promise-Tests in JS 05 erfolgreich bestanden!");
