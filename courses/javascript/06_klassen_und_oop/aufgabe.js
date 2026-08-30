/**
 * 🌐 JS 06: KLASSEN & OBJEKTORIENTIERUNG (OOP) 🌐
 * ==================================================
 * Moderne ES6-Klassen, Konstruktoren, Getter/Setter,
 * Vererbung mit extends/super und statische Methoden.
 */

// 🎯 TEILZIEL 1 (TODO 1): Klasse Bankkonto
// Erstelle eine Klasse Bankkonto mit Kapselung:
// - constructor(inhaber, startSaldo = 0):
//   - Weist this.inhaber zu
//   - Weist this._saldo das startSaldo zu (Default: 0)
// - Getter get saldo(): Gibt this._saldo zurück
// - Methode einzahlen(betrag):
//   - Wirft einen Fehler (throw new Error("...")), wenn betrag <= 0
//   - Erhöht this._saldo um betrag und gibt den neuen Saldo zurück
// - Methode abheben(betrag):
//   - Wirft einen Fehler, wenn betrag <= 0
//   - Wirft einen Fehler, wenn betrag > this._saldo ("Nicht genügend Guthaben")
//   - Verringert this._saldo um betrag und gibt den neuen Saldo zurück
class Bankkonto {
  constructor(inhaber, startSaldo = 0) {
    // TODO: Initialisiere inhaber und _saldo
    this.inhaber = inhaber;
    this._saldo = 0;
  }

  get saldo() {
    // TODO: Getter für _saldo implementieren
    return 0;
  }

  einzahlen(betrag) {
    // TODO: Validierung und Erhöhung von _saldo
    return 0;
  }

  abheben(betrag) {
    // TODO: Validierung, Guthabenprüfung und Reduzierung von _saldo
    return 0;
  }
}

// 🎯 TEILZIEL 2 (TODO 2): Basisklasse Fahrzeug
// Erstelle eine Basisklasse Fahrzeug:
// - constructor(marke, modell, baujahr):
//   - Weist this.marke, this.modell und this.baujahr zu
// - Methode beschreibung():
//   - Gibt einen String im Format "${marke} ${modell} (${baujahr})" zurück
class Fahrzeug {
  constructor(marke, modell, baujahr) {
    // TODO: Eigenschaften initialisieren
    this.marke = marke;
    this.modell = modell;
    this.baujahr = baujahr;
  }

  beschreibung() {
    // TODO: String-Repräsentation zurückgeben
    return "";
  }
}

// 🎯 TEILZIEL 3 (TODO 3): Kindklasse ElektroAuto extends Fahrzeug
// Erstelle eine Kindklasse ElektroAuto, die von Fahrzeug erbt:
// - constructor(marke, modell, baujahr, batterieKapazitaet):
//   - Ruft super(marke, modell, baujahr) auf
//   - Weist this.batterieKapazitaet (in kWh) zu
// - Methode reichweiteBerechnen(verbrauchPro100km):
//   - Wirft einen Fehler, wenn verbrauchPro100km <= 0
//   - Berechnet die Reichweite in km: (batterieKapazitaet / verbrauchPro100km) * 100
// - Überschreibe beschreibung():
//   - Gibt "${super.beschreibung()} [Elektro: ${batterieKapazitaet} kWh]" zurück
// 🎯 TEILZIEL 4 (TODO 4): Statische Fabrikmethode ElektroAuto.erstelleStandardTesla()
// - static erstelleStandardTesla():
//   - Gibt eine neue Instanz von ElektroAuto mit ("Tesla", "Model 3", 2024, 75) zurück
class ElektroAuto extends Fahrzeug {
  constructor(marke, modell, baujahr, batterieKapazitaet) {
    // TODO: super(...) aufrufen und batterieKapazitaet initialisieren
    super(marke, modell, baujahr);
    this.batterieKapazitaet = 0;
  }

  beschreibung() {
    // TODO: super.beschreibung() nutzen und um Batterie erweitern
    return "";
  }

  reichweiteBerechnen(verbrauchPro100km) {
    // TODO: Reichweite anhand von batterieKapazitaet und Verbrauch berechnen
    return 0;
  }

  static erstelleStandardTesla() {
    // TODO: Neues ElektroAuto-Objekt mit Standard-Parametern erzeugen und zurückgeben
    return null;
  }
}
