/**
 * 🌟 MUSTERLÖSUNG: JS 13 – ES MODULE & ARCHITEKTUR 🌟
 * ===================================================
 */

function pruefeZahl(val, name = "Wert") {
  if (typeof val !== "number" || isNaN(val)) {
    throw new TypeError(`${name} muss eine gültige Zahl sein`);
  }
}

const MathModule = {
  addieren(a, b) {
    pruefeZahl(a, "Parameter a");
    pruefeZahl(b, "Parameter b");
    return Math.round((a + b) * 1e8) / 1e8;
  },

  subtrahieren(a, b) {
    pruefeZahl(a, "Parameter a");
    pruefeZahl(b, "Parameter b");
    return Math.round((a - b) * 1e8) / 1e8;
  },

  multiplizieren(a, b) {
    pruefeZahl(a, "Parameter a");
    pruefeZahl(b, "Parameter b");
    return Math.round((a * b) * 1e8) / 1e8;
  },

  dividieren(a, b) {
    pruefeZahl(a, "Parameter a");
    pruefeZahl(b, "Parameter b");
    if (b === 0) {
      throw new Error("Division durch 0 nicht erlaubt");
    }
    return Math.round((a / b) * 1e8) / 1e8;
  },

  runden(betrag, dezimalstellen = 2) {
    pruefeZahl(betrag, "Betrag");
    pruefeZahl(dezimalstellen, "Dezimalstellen");
    const faktor = Math.pow(10, dezimalstellen);
    return Math.round((betrag + Number.EPSILON) * faktor) / faktor;
  }
};

const FormatterModule = {
  formatiereWaehrung(betrag, waehrung = "EUR") {
    pruefeZahl(betrag, "Betrag");
    if (typeof waehrung !== "string" || waehrung.trim().length === 0) {
      throw new TypeError("Währung muss ein nicht-leerer String sein");
    }

    const gerundet = MathModule.runden(betrag, 2);
    const teile = (Math.abs(gerundet)).toFixed(2).split(".");
    const vz = gerundet < 0 ? "-" : "";
    const ganzzahlFormatiert = teile[0].replace(/\B(?=(\d{3})+(?!\d))/g, ".");
    return `${vz}${ganzzahlFormatiert},${teile[1]} ${waehrung.trim().toUpperCase()}`;
  },

  formatiereDatumIso(datum) {
    let d;
    if (datum instanceof Date) {
      d = datum;
    } else if (typeof datum === "string" || typeof datum === "number") {
      d = new Date(datum);
    } else {
      throw new TypeError("Ungültiges Datumsformat");
    }

    if (isNaN(d.getTime())) {
      throw new TypeError("Ungültiges Datum");
    }

    const jahr = d.getUTCFullYear();
    const monat = String(d.getUTCMonth() + 1).padStart(2, "0");
    const tag = String(d.getUTCDate()).padStart(2, "0");
    return `${jahr}-${monat}-${tag}`;
  }
};

class RechnungsEngine {
  constructor(mathMod = MathModule, formatMod = FormatterModule) {
    this.math = mathMod;
    this.formatter = formatMod;
  }

  erstellePosition(bezeichnung, menge, einzelpreis) {
    if (typeof bezeichnung !== "string" || bezeichnung.trim().length === 0) {
      throw new Error("Bezeichnung darf nicht leer sein");
    }
    if (typeof menge !== "number" || isNaN(menge) || menge <= 0) {
      throw new RangeError("Menge muss eine Zahl größer als 0 sein");
    }
    if (typeof einzelpreis !== "number" || isNaN(einzelpreis) || einzelpreis < 0) {
      throw new RangeError("Einzelpreis muss eine Zahl >= 0 sein");
    }

    const gesamtpreis = this.math.multiplizieren(menge, einzelpreis);
    return {
      bezeichnung: bezeichnung.trim(),
      menge,
      einzelpreis,
      gesamtpreis
    };
  }

  berechneRechnung(positionen, steuersatzProzent = 19) {
    if (!Array.isArray(positionen)) {
      throw new TypeError("Positionen müssen als Array übergeben werden");
    }
    if (typeof steuersatzProzent !== "number" || isNaN(steuersatzProzent) || steuersatzProzent < 0) {
      throw new RangeError("Steuersatz muss eine Zahl >= 0 sein");
    }

    let nettoSumme = 0;
    for (const p of positionen) {
      const gp = (p && typeof p.gesamtpreis === "number") ? p.gesamtpreis : 0;
      nettoSumme = this.math.addieren(nettoSumme, gp);
    }

    const steuerFaktor = this.math.dividieren(steuersatzProzent, 100);
    const steuerUnrund = this.math.multiplizieren(nettoSumme, steuerFaktor);
    const steuerBetrag = this.math.runden(steuerUnrund, 2);
    const bruttoSumme = this.math.addieren(nettoSumme, steuerBetrag);

    return {
      positionen: [...positionen],
      nettoSumme,
      steuersatzProzent,
      steuerBetrag,
      bruttoSumme,
      nettoFormatiert: this.formatter.formatiereWaehrung(nettoSumme),
      steuerFormatiert: this.formatter.formatiereWaehrung(steuerBetrag),
      bruttoFormatiert: this.formatter.formatiereWaehrung(bruttoSumme)
    };
  }
}
