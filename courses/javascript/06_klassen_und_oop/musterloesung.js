/**
 * 🌟 MUSTERLÖSUNG: JS 06 – KLASSEN & OBJEKTORIENTIERUNG (OOP) 🌟
 * =============================================================
 */

class Bankkonto {
  constructor(inhaber, startSaldo = 0) {
    if (!inhaber || typeof inhaber !== "string") {
      throw new Error("Inhaber muss als gültiger Text angegeben werden.");
    }
    if (typeof startSaldo !== "number" || startSaldo < 0 || isNaN(startSaldo)) {
      throw new Error("Start-Saldo muss eine nicht-negative Zahl sein.");
    }
    this.inhaber = inhaber;
    this._saldo = startSaldo;
  }

  get saldo() {
    return this._saldo;
  }

  einzahlen(betrag) {
    if (typeof betrag !== "number" || betrag <= 0 || isNaN(betrag)) {
      throw new Error("Einzahlungsbetrag muss größer als 0 sein.");
    }
    this._saldo += betrag;
    return this._saldo;
  }

  abheben(betrag) {
    if (typeof betrag !== "number" || betrag <= 0 || isNaN(betrag)) {
      throw new Error("Abhebebetrag muss größer als 0 sein.");
    }
    if (betrag > this._saldo) {
      throw new Error("Nicht genügend Guthaben vorhanden.");
    }
    this._saldo -= betrag;
    return this._saldo;
  }
}

class Fahrzeug {
  constructor(marke, modell, baujahr) {
    this.marke = marke;
    this.modell = modell;
    this.baujahr = baujahr;
  }

  beschreibung() {
    return `${this.marke} ${this.modell} (${this.baujahr})`;
  }
}

class ElektroAuto extends Fahrzeug {
  constructor(marke, modell, baujahr, batterieKapazitaet) {
    super(marke, modell, baujahr);
    this.batterieKapazitaet = batterieKapazitaet;
  }

  beschreibung() {
    return `${super.beschreibung()} [Elektro: ${this.batterieKapazitaet} kWh]`;
  }

  reichweiteBerechnen(verbrauchPro100km) {
    if (typeof verbrauchPro100km !== "number" || verbrauchPro100km <= 0 || isNaN(verbrauchPro100km)) {
      throw new Error("Verbrauch pro 100 km muss größer als 0 sein.");
    }
    return (this.batterieKapazitaet / verbrauchPro100km) * 100;
  }

  static erstelleStandardTesla() {
    return new ElektroAuto("Tesla", "Model 3", 2024, 75);
  }
}
