/**
 * 🌟 MUSTERLÖSUNG: JS 08 – FEHLERBEHANDLUNG & DEBUGGING 🌟
 * =======================================================
 */

class AnwendungsFehler extends Error {
  constructor(message) {
    super(message);
    this.name = "AnwendungsFehler";
  }
}

class ValidierungsFehler extends AnwendungsFehler {
  constructor(message, feld = null) {
    super(message);
    this.name = "ValidierungsFehler";
    this.feld = feld;
  }
}

class GuthabenFehler extends AnwendungsFehler {
  constructor(message, saldo = 0, betrag = 0) {
    super(message);
    this.name = "GuthabenFehler";
    this.saldo = saldo;
    this.betrag = betrag;
  }
}

function sichereDivision(a, b) {
  if (typeof a !== "number" || typeof b !== "number" || isNaN(a) || isNaN(b)) {
    throw new ValidierungsFehler("Ungültige Zahlenwerte für Division.", "parameter");
  }
  if (b === 0) {
    throw new AnwendungsFehler("Division durch Null ist nicht erlaubt.");
  }
  return a / b;
}

function parseBenutzerJson(jsonString) {
  if (!jsonString || typeof jsonString !== "string") {
    throw new ValidierungsFehler("JSON-String darf nicht leer sein.", "jsonString");
  }

  let parsed;
  try {
    parsed = JSON.parse(jsonString);
  } catch (err) {
    throw new ValidierungsFehler("Ungültiges JSON-Format: " + err.message, "jsonString");
  }

  if (!parsed || typeof parsed !== "object" || Array.isArray(parsed)) {
    throw new ValidierungsFehler("JSON muss ein Objekt darstellen.", "root");
  }

  if (!parsed.name || typeof parsed.name !== "string" || parsed.name.trim() === "") {
    throw new ValidierungsFehler("Pflichtfeld 'name' fehlt oder ist ungültig.", "name");
  }

  return parsed;
}

function pruefeTransaktion(kontoSaldo, abhebeBetrag) {
  if (
    typeof kontoSaldo !== "number" ||
    typeof abhebeBetrag !== "number" ||
    isNaN(kontoSaldo) ||
    isNaN(abhebeBetrag) ||
    abhebeBetrag <= 0
  ) {
    throw new ValidierungsFehler("Ungültiger Abhebebetrag.", "abhebeBetrag");
  }

  if (kontoSaldo < abhebeBetrag) {
    throw new GuthabenFehler("Nicht genügend Guthaben vorhanden.", kontoSaldo, abhebeBetrag);
  }

  return kontoSaldo - abhebeBetrag;
}
