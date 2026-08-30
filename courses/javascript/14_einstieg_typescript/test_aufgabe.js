/**
 * 🧪 Testsuite für JS/TS 07: TypeScript Type Safety & Interfaces
 */

// Helper für Exception-Prüfung in Sandbox & Node
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
// 1. Tests für erstelleKunde(id, name, istAktiv, email)
// ----------------------------------------------------
const k1 = erstelleKunde(101, "Max Mustermann");
assert.strictEqual(k1.id, 101, "Kunden-ID sollte 101 sein");
assert.strictEqual(k1.name, "Max Mustermann", "Name sollte 'Max Mustermann' sein");
assert.strictEqual(k1.istAktiv, true, "Standardwert für istAktiv sollte true sein");
assert.ok(typeof k1.erstelltAm === "string" && k1.erstelltAm.length > 0, "erstelltAm muss ein Datums-String sein");

const k2 = erstelleKunde("C-42", "  Lisa Schmidt  ", false, "lisa@example.com");
assert.strictEqual(k2.id, "C-42", "Kunden-ID sollte 'C-42' sein");
assert.strictEqual(k2.name, "Lisa Schmidt", "Name sollte mit .trim() bereinigt werden");
assert.strictEqual(k2.istAktiv, false, "istAktiv sollte false sein");
assert.strictEqual(k2.email, "lisa@example.com", "E-Mail sollte übernommen werden");

assertThrows(() => erstelleKunde(null, "Test"), "erstelleKunde mit id=null muss Fehler werfen");
assertThrows(() => erstelleKunde(10, ""), "erstelleKunde mit leerem Namen muss Fehler werfen");
assertThrows(() => erstelleKunde(10, "   "), "erstelleKunde mit Leerzeichen-Name muss Fehler werfen");
assertThrows(() => erstelleKunde(10, 12345), "erstelleKunde mit Zahl als Name muss Fehler werfen");

// ----------------------------------------------------
// 2. Tests für validiereAuftrag(auftragObjekt)
// ----------------------------------------------------
const gueltigerAuftrag = {
  id: "A-1001",
  kundeId: 101,
  positionen: [
    { titel: "Webdesign & Frontend", menge: 1, einzelpreis: 1200.00 },
    { titel: "Hosting Setup", menge: 2, einzelpreis: 50.00 }
  ],
  summe: 1300.00,
  status: "offen"
};
const res1 = validiereAuftrag(gueltigerAuftrag);
assert.strictEqual(res1.gueltig, true, "Gültiger Auftrag sollte als gueltig: true erkannt werden");
assert.strictEqual(res1.fehler.length, 0, "Gültiger Auftrag darf keine Fehlermeldungen haben");

const ungueltigerStatus = { ...gueltigerAuftrag, status: "in_prüfung" };
const res2 = validiereAuftrag(ungueltigerStatus);
assert.strictEqual(res2.gueltig, false, "Unbekannter Status muss als ungültig erkannt werden");

const keinePositionen = { ...gueltigerAuftrag, positionen: [] };
const res3 = validiereAuftrag(keinePositionen);
assert.strictEqual(res3.gueltig, false, "Auftrag ohne Positionen muss ungültig sein");

const fehlerhaftePosition = {
  ...gueltigerAuftrag,
  positionen: [{ titel: "", menge: -1, einzelpreis: 10 }]
};
const res4 = validiereAuftrag(fehlerhaftePosition);
assert.strictEqual(res4.gueltig, false, "Ungültige Positionen müssen erkannt werden");

const resNull = validiereAuftrag(null);
assert.strictEqual(resNull.gueltig, false, "null als Auftrag muss abgefangen werden");

// ----------------------------------------------------
// 3. Tests für filtereNachStatus(eintraege, zielStatus)
// ----------------------------------------------------
const liste = [
  { id: 1, titel: "Design", status: "offen" },
  { id: 2, titel: "Backend", status: "in_bearbeitung" },
  { id: 3, titel: "Deployment", status: "offen" },
  { id: 4, titel: "Testing", status: "abgeschlossen" }
];
const offene = filtereNachStatus(liste, "offen");
assert.strictEqual(offene.length, 2, "Es sollte genau 2 offene Einträge geben");
assert.strictEqual(offene[0].id, 1, "Erster gefilterter Eintrag ID");
assert.strictEqual(offene[1].id, 3, "Zweiter gefilterter Eintrag ID");

const abgeschlossene = filtereNachStatus(liste, "abgeschlossen");
assert.strictEqual(abgeschlossene.length, 1, "Es sollte 1 abgeschlossenen Eintrag geben");

const stornierte = filtereNachStatus(liste, "storniert");
assert.strictEqual(stornierte.length, 0, "Nicht vorhandener Status liefert leeres Array");

assert.deepStrictEqual(filtereNachStatus(null, "offen"), [], "Ungültige Liste liefert []");

// ----------------------------------------------------
// 4. Tests für formatierePreisangabe(betrag, waehrung)
// ----------------------------------------------------
assert.strictEqual(formatierePreisangabe(49.99), "49,99 EUR", "formatierePreisangabe(49.99) mit Default EUR");
assert.strictEqual(formatierePreisangabe(1250, "USD"), "1250,00 USD", "formatierePreisangabe(1250, 'USD')");
assert.strictEqual(formatierePreisangabe(0, "chf"), "0,00 CHF", "Währung sollte in Großbuchstaben formatiert werden");
assert.strictEqual(formatierePreisangabe(9.5, "EUR"), "9,50 EUR", "Einstellige Nachkommastelle auf 2 Stellen auffüllen");

assertThrows(() => formatierePreisangabe("49.99"), "String als Betrag muss TypeError werfen");
assertThrows(() => formatierePreisangabe(NaN), "NaN als Betrag muss TypeError werfen");
assertThrows(() => formatierePreisangabe(10, ""), "Leere Währung muss TypeError werfen");

console.log("✅ Alle Tests für TS 07 (TypeScript Type Safety & Interfaces) erfolgreich bestanden!");
