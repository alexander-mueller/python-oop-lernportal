// 🧪 JS 07: Testsuite für Reguläre Ausdrücke & Textverarbeitung

if (typeof assert === "undefined") {
  var assert = require("assert");
}

// ==========================================
// 1. Tests für istGueltigeEmail
// ==========================================
assert.strictEqual(istGueltigeEmail("max@mustermann.de"), true, "max@mustermann.de sollte gültig sein");
assert.strictEqual(istGueltigeEmail("user.name+tag@sub.domain.org"), true, "E-Mail mit Subdomain und Plus-Tag sollte gültig sein");
assert.strictEqual(istGueltigeEmail("dev123@code.io"), true, "dev123@code.io sollte gültig sein");

assert.strictEqual(istGueltigeEmail("max@domain"), false, "E-Mail ohne TLD (.de, .com) sollte ungültig sein");
assert.strictEqual(istGueltigeEmail("@domain.com"), false, "E-Mail ohne Benutzername sollte ungültig sein");
assert.strictEqual(istGueltigeEmail("keine-email"), false, "Reiner Text sollte ungültig sein");
assert.strictEqual(istGueltigeEmail(""), false, "Leerer String sollte ungültig sein");
assert.strictEqual(istGueltigeEmail(null), false, "null sollte ungültig sein");

// ==========================================
// 2. Tests für findeTelefonnummern
// ==========================================
const textMitNummern = "Kontakt: +49 170 1234567 oder per Festnetz 030 / 123456. Kein Datum 2024.";
const nummern = findeTelefonnummern(textMitNummern);
assert.deepStrictEqual(
  nummern,
  ["+49 170 1234567", "030 / 123456"],
  "Sollte Mobil- und Festnetznummern finden"
);

const mobilText = "Mobil: 0171-1234567 und 089 98765432.";
assert.deepStrictEqual(
  findeTelefonnummern(mobilText),
  ["0171-1234567", "089 98765432"],
  "Sollte Bindestrich- und Leerzeichen-Format erkennen"
);

assert.deepStrictEqual(findeTelefonnummern("Keine Telefonnummer hier im Jahr 2025!"), [], "Sollte leeres Array bei keinen Treffern liefern");
assert.deepStrictEqual(findeTelefonnummern(""), [], "Leerer Text sollte [] liefern");

// ==========================================
// 3. Tests für extrahiereHashtags
// ==========================================
const post = "Lerne #javascript und #webdev mit modernen #es6_features!";
const tags = extrahiereHashtags(post);
assert.deepStrictEqual(
  tags,
  ["#javascript", "#webdev", "#es6_features"],
  "Sollte alle Hashtags im Text finden"
);

assert.deepStrictEqual(extrahiereHashtags("Ein normaler Satz ohne Tags."), [], "Ohne Hashtags sollte [] zurückkommen");
assert.deepStrictEqual(extrahiereHashtags(""), [], "Leerer String sollte [] zurückgeben");

// ==========================================
// 4. Tests für maskiereKreditkarte
// ==========================================
const kkText = "Meine Karte ist 1234-5678-9012-3456.";
assert.strictEqual(
  maskiereKreditkarte(kkText),
  "Meine Karte ist ****-****-****-3456.",
  "16-stellige Karte mit Bindestrichen sollte maskiert werden"
);

const kkText2 = "Karten: 1111 2222 3333 4444 und 5555666677778888";
assert.strictEqual(
  maskiereKreditkarte(kkText2),
  "Karten: ****-****-****-4444 und ****-****-****-8888",
  "Mehrere Karten mit Leerzeichen und durchgehend sollten maskiert werden"
);

assert.strictEqual(
  maskiereKreditkarte("Keine Kreditkarte vorhanden."),
  "Keine Kreditkarte vorhanden.",
  "Text ohne Kreditkarten darf nicht verändert werden"
);

// ==========================================
// 5. Tests für istStarkesPasswort
// ==========================================
assert.strictEqual(istStarkesPasswort("Sicher123!"), true, "Sicher123! sollte stark sein");
assert.strictEqual(istStarkesPasswort("P@ssw0rd2024"), true, "P@ssw0rd2024 sollte stark sein");
assert.strictEqual(istStarkesPasswort("Mein#Geheimnis9"), true, "Mein#Geheimnis9 sollte stark sein");

assert.strictEqual(istStarkesPasswort("S1!a"), false, "Zu kurzes Passwort (< 8 Zeichen) sollte false liefern");
assert.strictEqual(istStarkesPasswort("sicher123!"), false, "Ohne Großbuchstaben sollte false liefern");
assert.strictEqual(istStarkesPasswort("SICHER123!"), false, "Ohne Kleinbuchstaben sollte false liefern");
assert.strictEqual(istStarkesPasswort("SicheresPasswort!"), false, "Ohne Zahl sollte false liefern");
assert.strictEqual(istStarkesPasswort("Sicher12345"), false, "Ohne Sonderzeichen sollte false liefern");
assert.strictEqual(istStarkesPasswort(""), false, "Leerer String sollte false liefern");
assert.strictEqual(istStarkesPasswort(null), false, "null sollte false liefern");

console.log("✅ Alle Tests in JS 07 (Regex & Textverarbeitung) erfolgreich bestanden!");
