/**
 * 🌐 JS 03: FUNKTIONEN, SCOPE & CLOSURES 🌐
 * ==========================================
 * Funktionsarten, Gültigkeitsbereiche, Rest-Parameter und Closures.
 */

// 🎯 TEILZIEL 1 (TODO 1): erstelleZaehler(startWert = 0)
// Erstelle eine Funktion, die einen internen Zähler kapselt (Closure).
// Die zurückgegebene Funktion soll bei jedem Aufruf den Zähler um 1 erhöhen
// und den neuen Wert zurückgeben.
// Standardwert für startWert ist 0.
// Beispiel:
//   const zaehler = erstelleZaehler(0);
//   zaehler(); // 1
//   zaehler(); // 2
function erstelleZaehler(startWert = 0) {
  // TODO: Innere Zählerfunktion (Closure) zurückgeben
  return function() {
    return 0;
  };
}

// 🎯 TEILZIEL 2 (TODO 2): multiplizierer(faktor)
// Erstelle eine Factory-Funktion (Closure), die eine Multiplikationsfunktion zurückgibt.
// Die zurückgegebene Funktion nimmt eine Zahl x entgegen und gibt (x * faktor) zurück.
// Beispiel:
//   const verdopple = multiplizierer(2);
//   verdopple(5); // 10
//   const verdreifache = multiplizierer(3);
//   verdreifache(4); // 12
function multiplizierer(faktor) {
  // TODO: Arrow-Funktion oder anonyme Funktion zurückgeben
  return (x) => 0;
}

// 🎯 TEILZIEL 3 (TODO 3): summiereAlles(...zahlen)
// Berechne die Summe beliebig vieler übergebener Zahlen unter Verwendung des
// Rest-Parameters (...zahlen).
// Werden keine Argumente übergeben, soll 0 zurückgegeben werden.
// Beispiel:
//   summiereAlles(1, 2, 3, 4); // 10
//   summiereAlles(5, -2);      // 3
//   summiereAlles();           // 0
function summiereAlles(...zahlen) {
  // TODO: Rest-Parameter aufsummieren
  return 0;
}

// 🎯 TEILZIEL 4 (TODO 4): erstellePraefixierer(praefix)
// Erstelle eine Funktion (Closure), die einen String als Präfix vor jeden
// übergebenen Text setzt.
// Beispiel:
//   const mitEuro = erstellePraefixierer("€ ");
//   mitEuro("100"); // "€ 100"
//   const https = erstellePraefixierer("https://");
//   https("google.com"); // "https://google.com"
function erstellePraefixierer(praefix) {
  // TODO: Closure-Funktion zurückgeben
  return (text) => "";
}
