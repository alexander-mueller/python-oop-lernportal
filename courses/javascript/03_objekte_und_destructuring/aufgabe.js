/**
 * 🌐 JS 03: OBJEKTE, DESTRUCTURING & REST/SPREAD 🌐
 * ==================================================
 * Strukturierte Daten & moderne ES6-Operatoren in JavaScript.
 */

// 🎯 TEILZIEL 1 (TODO 1): erstelleBenutzer(name, email, rolle = "user")
// Erstelle ein Benutzerobjekt mit Property Shorthand und Default-Parameter.
// Rückgabe: Ein Objekt mit { name, email, rolle }
function erstelleBenutzer(name, email, rolle = "user") {
  // TODO: Nutze ES6 Property Shorthand { name, email, rolle }
  return null;
}

// 🎯 TEILZIEL 2 (TODO 2): extrahiereDetails(benutzerObjekt)
// Extrahiere 'name' und 'email' mittels Object Destructuring: const { name, email } = benutzerObjekt;
// Rückgabe: Formatierter String im Format: `${name} (${email})`
function extrahiereDetails(benutzerObjekt) {
  // TODO: Destructuring anwenden und String im Format "Name (email@domain.de)" zurückgeben
  return "";
}

// 🎯 TEILZIEL 3 (TODO 3): fuegeAdresseHinzu(benutzerObjekt, adresseObjekt)
// Kombiniere Benutzer und Adresse zu einem NEUEN Objekt mittels Spread-Operator: { ...benutzerObjekt, ...adresseObjekt }
// Wichtig: Das Originalobjekt benutzerObjekt darf NICHT verändert werden (Immutability).
function fuegeAdresseHinzu(benutzerObjekt, adresseObjekt) {
  // TODO: Neues Objekt mit Object Spread { ...benutzerObjekt, ...adresseObjekt } erstellen
  return null;
}

// 🎯 TEILZIEL 4 (TODO 4): zaehleEigenschaften(objekt)
// Zähle die Anzahl der eigenen Schlüssel/Eigenschaften eines Objekts mit Object.keys(objekt).length.
// Bei leeren oder ungültigen Objekten soll 0 zurückgegeben werden.
function zaehleEigenschaften(objekt) {
  // TODO: Object.keys() nutzen und Anzahl der Keys zurückgeben
  return 0;
}

// 🎯 TEILZIEL 5 (TODO 5): berechneWarenkorbGesamtwert(warenkorbItems)
// Berechne die Summe aller (preis * anzahl) im Array warenkorbItems.
// Nutze Destructuring im Loop oder in reduce: for (const { preis, anzahl = 1 } of warenkorbItems)
// Bei leerem Warenkorb [] soll 0 zurückgegeben werden.
function berechneWarenkorbGesamtwert(warenkorbItems) {
  // TODO: Destructuring im Schleifendurchlauf oder reduce nutzen
  return 0;
}
