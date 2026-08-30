/**
 * 🌐 JS 04: DOM-MANIPULATION & EVENTS 🌐
 * ========================================
 * Interaktive Webseiten & Event-Driven Architecture in JavaScript.
 */

// 🎯 TEILZIEL 1 (TODO 1): erzeugeButtonElement(text, cssKlasse, clickCallback)
// Erzeuge ein Button-Element mit document.createElement("button").
// 1. Setze textContent auf 'text'.
// 2. Füge 'cssKlasse' über classList.add(cssKlasse) hinzu (falls cssKlasse übergeben wurde).
// 3. Registriere 'clickCallback' mit button.addEventListener("click", clickCallback) (falls clickCallback eine Funktion ist).
// Rückgabe: Das fertige Button-Element
function erzeugeButtonElement(text, cssKlasse, clickCallback) {
  // TODO: Button erstellen, Text setzen, Klasse hinzufügen, Event-Listener registrieren
  return null;
}

// 🎯 TEILZIEL 2 (TODO 2): erstelleListenEintrag(titel, istErledigt = false)
// Erzeuge ein <li>-Element mit document.createElement("li").
// 1. Setze textContent auf 'titel'.
// 2. Wenn istErledigt === true ist, füge die CSS-Klasse "erledigt" hinzu (classList.add("erledigt")).
// Rückgabe: Das erstellte <li>-Element
function erstelleListenEintrag(titel, istErledigt = false) {
  // TODO: <li> erzeugen, Text setzen, optional Klasse "erledigt" hinzufügen
  return null;
}

// 🎯 TEILZIEL 3 (TODO 3): filtereElementeNachKlasse(elementListe, cssKlasse)
// Filtert ein Array oder eine NodeList von Elementen.
// Rückgabe: Ein neues Array, das nur Elemente enthält, bei denen element.classList.contains(cssKlasse) true ist.
function filtereElementeNachKlasse(elementListe, cssKlasse) {
  // TODO: Array.from(elementListe).filter(...) mit classList.contains(cssKlasse)
  return [];
}

// 🎯 TEILZIEL 4 (TODO 4): aktualisiereZaehlerAnzeige(aktuellerWert, schwellenwert = 10)
// Berechnet den Status einer Zähleranzeige (Headless-UI State Pattern):
// Rückgabe-Objekt:
// {
//   text: `Zähler: ${aktuellerWert} / ${schwellenwert}`,
//   wert: aktuellerWert,
//   istKritisch: aktuellerWert >= schwellenwert,
//   statusKlasse: aktuellerWert >= schwellenwert ? "status-kritisch" : "status-normal"
// }
function aktualisiereZaehlerAnzeige(aktuellerWert, schwellenwert = 10) {
  // TODO: Zählerstatus berechnen und Objekt zurückgeben
  return null;
}
