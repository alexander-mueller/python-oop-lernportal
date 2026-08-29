/**
 * 🌐 JS 05: CALLBACKS, EVENT LOOP & PROMISES 🌐
 * =============================================
 * Lerne die Grundlagen der asynchronen Programmierung in JavaScript:
 * Callbacks, der Event Loop und Promises für nicht-blockierenden Code.
 */

// 🎯 TEILZIEL 1 (TODO 1): Schreibe verzoegereAusfuehrung(ms, rueckgabeWert)
// Gibt ein neues Promise zurück, das nach `ms` Millisekunden mit `rueckgabeWert` aufgelöst (resolved) wird.
// Nutze dafür setTimeout(callback, ms).
function verzoegereAusfuehrung(ms, rueckgabeWert) {
  // TODO: Gib ein new Promise((resolve) => ...) zurück
  return null;
}

// 🎯 TEILZIEL 2 (TODO 2): Schreibe pruefeZahlGroesserNull(zahl)
// Gibt ein Promise zurück:
// - Wenn zahl > 0: resolve mit zahl
// - Wenn zahl <= 0 oder keine Zahl: reject mit einem Error("Zahl muss größer als 0 sein")
function pruefeZahlGroesserNull(zahl) {
  // TODO: Gib ein Promise zurück, das resolve() oder reject() aufruft
  return null;
}

// 🎯 TEILZIEL 3 (TODO 3): Schreibe ladeBenutzerProfil(userId)
// Simuliert das asynchrone Laden eines Benutzerprofils:
// - Wenn userId ein positiver Wert (> 0) ist:
//   Gibt ein Promise zurück, das nach kurzer Zeit (z.B. 10ms) ein Objekt auflöst:
//   { id: userId, name: `Benutzer_${userId}`, status: "aktiv" }
// - Wenn userId <= 0 oder ungültig:
//   Gibt ein abgewiesenes Promise (reject) mit Error("Ungültige User-ID") zurück.
function ladeBenutzerProfil(userId) {
  // TODO: Implementiere ladeBenutzerProfil mit Promise
  return null;
}

// 🎯 TEILZIEL 4 (TODO 4): Schreibe ladeAlleDatenQuellen(quelleA, quelleB)
// Nimmt zwei Promises quelleA und quelleB entgegen und nutzt Promise.all([...]),
// um beide Datenquellen parallel abzuwarten.
// Gibt das Promise von Promise.all zurück, das ein Array [ergebnisA, ergebnisB] liefert.
function ladeAlleDatenQuellen(quelleA, quelleB) {
  // TODO: Nutze Promise.all([quelleA, quelleB])
  return null;
}
