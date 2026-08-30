/**
 * 🌐 JS 02: KONTROLLFLUSS, VERZWEIGUNGEN & SCHLEIFEN 🌐
 * ====================================================
 * Entscheidungen treffen und Wiederholungen steuern in JavaScript.
 */

// 🎯 TEILZIEL 1 (TODO 1): kategorisiereAlter(alter)
// Bestimme die Altersgruppe anhand folgender Kriterien:
// - kleiner als 13: "Kind"
// - 13 bis 17 (inklusive): "Jugendlicher"
// - 18 bis 64 (inklusive): "Erwachsener"
// - ab 65 (inklusive): "Senior"
// Verwende if, else if und else mit striktem Vergleich.
function kategorisiereAlter(alter) {
  // TODO: Implementiere die Alterskategorisierung
  return "";
}

// 🎯 TEILZIEL 2 (TODO 2): wochentagName(tagNummer)
// Wandle eine Zahl von 1 bis 7 in den passenden Wochentag um:
// 1 -> "Montag", 2 -> "Dienstag", 3 -> "Mittwoch", 4 -> "Donnerstag",
// 5 -> "Freitag", 6 -> "Samstag", 7 -> "Sonntag"
// Für alle anderen Zahlen/Eingaben soll "Ungültig" zurückgegeben werden.
// Verwende dafür eine switch-case Anweisung mit break und default.
function wochentagName(tagNummer) {
  // TODO: Nutze switch(tagNummer) { case ...: return ...; default: ... }
  return "";
}

// 🎯 TEILZIEL 3 (TODO 3): berechneRabattpreis(preis, istPremium, hatGutschein)
// Berechne den rabattierten Endpreis:
// - Wenn istPremium UND hatGutschein: 30% Rabatt (zahlt 70%, also preis * 0.7)
// - Wenn nur istPremium: 20% Rabatt (zahlt 80%, also preis * 0.8)
// - Wenn nur hatGutschein: 10% Rabatt (zahlt 90%, also preis * 0.9)
// - Sonst: kein Rabatt (zahlt 100%, also preis)
// Tipp: Nutze if/else oder den ternären Operator.
function berechneRabattpreis(preis, istPremium, hatGutschein) {
  // TODO: Berechne den reduzierten Preis
  return 0;
}

// 🎯 TEILZIEL 4 (TODO 4): summeGeraderZahlen(start, ende)
// Berechne die Summe aller GERADEN Zahlen im Bereich von start bis einschließlich ende.
// Nutze eine for-Schleife (for (let i = start; i <= ende; i++)) und
// überspringe ungerade Zahlen mit 'continue'.
function summeGeraderZahlen(start, ende) {
  // TODO: for-Schleife mit continue für ungerade Zahlen
  return 0;
}

// 🎯 TEILZIEL 5 (TODO 5): findeErstesVielfaches(zahlen, teiler)
// Durchsuche das Array 'zahlen' nach der ersten Zahl, die ohne Rest durch 'teiler'
// teilbar ist (zahl % teiler === 0).
// Verwende eine for...of Schleife und beende die Schleife vorzeitig mit 'break' (oder direktem return).
// Wird kein Vielfaches gefunden oder ist das Array leer, gib null zurück.
function findeErstesVielfaches(zahlen, teiler) {
  // TODO: for (const zahl of zahlen) mit Prüfung und break
  return null;
}
