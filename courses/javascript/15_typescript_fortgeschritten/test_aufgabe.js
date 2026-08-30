/**
 * 🧪 Testsuite für TS 15: Fortgeschrittenes TypeScript & Generics
 */

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
// 1. Tests für erstellePaginiertesErgebnis (Generics Container)
// ----------------------------------------------------
const datenSeite1 = [
  { id: 1, name: "Alpha" },
  { id: 2, name: "Beta" },
  { id: 3, name: "Gamma" }
];

const res1 = erstellePaginiertesErgebnis(datenSeite1, 25, 1, 10);
assert.strictEqual(res1.items.length, 3, "Items-Länge");
assert.strictEqual(res1.total, 25, "Gesamtanzahl");
assert.strictEqual(res1.page, 1, "Aktuelle Seite");
assert.strictEqual(res1.pageSize, 10, "Elemente pro Seite");
assert.strictEqual(res1.totalPages, 3, "25 Elemente bei pageSize 10 = 3 Seiten");
assert.strictEqual(res1.hasNextPage, true, "Seite 1 von 3 hat nächste Seite");
assert.strictEqual(res1.hasPrevPage, false, "Seite 1 hat keine vorherige Seite");

// Letzte Seite
const resLast = erstellePaginiertesErgebnis([{ id: 25, name: "Omega" }], 25, 3, 10);
assert.strictEqual(resLast.hasNextPage, false, "Letzte Seite hat hasNextPage=false");
assert.strictEqual(resLast.hasPrevPage, true, "Letzte Seite hat hasPrevPage=true");

// Leere Gesamtmenge
const resEmpty = erstellePaginiertesErgebnis([], 0, 1, 10);
assert.strictEqual(resEmpty.totalPages, 1, "0 Elemente ergeben 1 leere Seite");
assert.strictEqual(resEmpty.hasNextPage, false);
assert.strictEqual(resEmpty.hasPrevPage, false);

// Validierungstests
assertThrows(() => erstellePaginiertesErgebnis("kein-array", 10), "Items nicht als Array muss TypeError werfen");
assertThrows(() => erstellePaginiertesErgebnis([], -5), "Negatives Total muss RangeError werfen");
assertThrows(() => erstellePaginiertesErgebnis([], 10, 0), "Page 0 muss RangeError werfen");
assertThrows(() => erstellePaginiertesErgebnis([], 10, 1, 0), "PageSize 0 muss RangeError werfen");

// ----------------------------------------------------
// 2. Tests für istAdminBenutzer (Custom Type Guard)
// ----------------------------------------------------
const gueltigerAdmin = {
  id: "ADM-007",
  username: "superadmin",
  email: "admin@system.corp",
  rolle: "ADMIN",
  berechtigungen: ["MANAGE_USERS", "DELETE_RECORDS"]
};

assert.strictEqual(istAdminBenutzer(gueltigerAdmin), true, "Gültiges Admin-Objekt muss true liefern");

const normalerUser = {
  ...gueltigerAdmin,
  rolle: "USER"
};
assert.strictEqual(istAdminBenutzer(normalerUser), false, "User-Rolle darf kein Admin sein");

const adminOhneRechte = {
  ...gueltigerAdmin,
  berechtigungen: []
};
assert.strictEqual(istAdminBenutzer(adminOhneRechte), false, "Admin ohne Berechtigungen muss abgelehnt werden");

const adminFalscheEmail = {
  ...gueltigerAdmin,
  email: "kein-at-zeichen"
};
assert.strictEqual(istAdminBenutzer(adminFalscheEmail), false, "Ungültige E-Mail muss abgelehnt werden");

assert.strictEqual(istAdminBenutzer(null), false, "null muss false liefern");
assert.strictEqual(istAdminBenutzer(undefined), false, "undefined muss false liefern");
assert.strictEqual(istAdminBenutzer("admin"), false, "String muss false liefern");

// ----------------------------------------------------
// 3. Tests für aktualisiereBenutzerProfil (Partial<T> Semantik)
// ----------------------------------------------------
const originalProfil = {
  id: 101,
  username: "ada_lovelace",
  email: "ada@analytical.org",
  einstellungen: {
    darkMode: false,
    benachrichtigungen: true
  }
};

const updatePayload = {
  username: "  ada_the_first  ",
  einstellungen: {
    darkMode: true
  }
};

const aktualisiert = aktualisiereBenutzerProfil(originalProfil, updatePayload);

// Prüfung der Werte
assert.strictEqual(aktualisiert.id, 101, "ID bleibt unverändert");
assert.strictEqual(aktualisiert.username, "ada_the_first", "Username aktualisiert und getrimmt");
assert.strictEqual(aktualisiert.email, "ada@analytical.org", "Nicht im Update enthaltene Felder bleiben erhalten");
assert.strictEqual(aktualisiert.einstellungen.darkMode, true, "darkMode wurde aktualisiert");
assert.strictEqual(aktualisiert.einstellungen.benachrichtigungen, true, "Verschachtelte Eigenschaften bleiben erhalten");
assert.ok(typeof aktualisiert.aktualisiertAm === "string", "aktualisiertAm Timestamp muss gesetzt sein");

// Immutability Prüfung: Original darf nicht verändert werden!
assert.strictEqual(originalProfil.username, "ada_lovelace", "Original darf nicht mutiert werden");
assert.strictEqual(originalProfil.einstellungen.darkMode, false, "Original-Einstellungen dürfen nicht mutiert werden");

// Validierungstests
assertThrows(() => aktualisiereBenutzerProfil(null, {}), "Original=null muss TypeError werfen");
assertThrows(() => aktualisiereBenutzerProfil(originalProfil, { email: "ungueltig" }), "Ungültige E-Mail muss TypeError werfen");
assertThrows(() => aktualisiereBenutzerProfil(originalProfil, { username: "   " }), "Leerer Username muss TypeError werfen");

// ----------------------------------------------------
// 4. Tests für filtriereFelder (Pick<T, K> Semantik)
// ----------------------------------------------------
const komplexesObjekt = {
  id: 99,
  username: "linus",
  passwortHash: "secret_salt_hash",
  email: "linus@kernel.org",
  ipAdresse: "192.168.1.1",
  geheim: true
};

const oeffentlichesProfil = filtriereFelder(komplexesObjekt, ["id", "username", "email"]);
assert.deepStrictEqual(
  oeffentlichesProfil,
  { id: 99, username: "linus", email: "linus@kernel.org" },
  "filtriereFelder sollte exakt die angegebenen Schlüssel kopieren"
);
assert.strictEqual("passwortHash" in oeffentlichesProfil, false, "Sensible Felder dürfen nicht enthalten sein");

// Nicht existierende Schlüssel
const gefiltertMitZusatz = filtriereFelder(komplexesObjekt, ["id", "nichtExistierend"]);
assert.deepStrictEqual(
  gefiltertMitZusatz,
  { id: 99 },
  "Nicht im Original existierende Schlüssel werden ausgelassen"
);

assert.deepStrictEqual(filtriereFelder(null, ["id"]), {}, "null als Objekt liefert {}");

console.log("✅ Alle 22 Tests für TS 15 (Fortgeschrittenes TypeScript & Generics) erfolgreich bestanden!");
