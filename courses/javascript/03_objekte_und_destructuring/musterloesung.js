/**
 * 🌟 MUSTERLÖSUNG: JS 03 – OBJEKTE & DESTRUCTURING 🌟
 * ==================================================
 */

function erstelleBenutzer(name, email, rolle = "user") {
  return { name, email, rolle };
}

function extrahiereDetails(benutzerObjekt) {
  const { name, email } = benutzerObjekt;
  return `${name} (${email})`;
}

function fuegeAdresseHinzu(benutzerObjekt, adresseObjekt) {
  return { ...benutzerObjekt, ...adresseObjekt };
}

function zaehleEigenschaften(objekt) {
  if (!objekt || typeof objekt !== "object") return 0;
  return Object.keys(objekt).length;
}

function berechneWarenkorbGesamtwert(warenkorbItems) {
  if (!Array.isArray(warenkorbItems) || warenkorbItems.length === 0) return 0;
  return warenkorbItems.reduce((gesamt, { preis = 0, anzahl = 1 }) => gesamt + preis * anzahl, 0);
}
