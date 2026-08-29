/**
 * 🌟 MUSTERLÖSUNG: JS 04 – DOM & EVENTS 🌟
 * ========================================
 */

function erzeugeButtonElement(text, cssKlasse, clickCallback) {
  const button = document.createElement("button");
  button.textContent = text;
  if (cssKlasse) {
    button.classList.add(cssKlasse);
  }
  if (typeof clickCallback === "function") {
    button.addEventListener("click", clickCallback);
  }
  return button;
}

function erstelleListenEintrag(titel, istErledigt = false) {
  const li = document.createElement("li");
  li.textContent = titel;
  if (istErledigt) {
    li.classList.add("erledigt");
  }
  return li;
}

function filtereElementeNachKlasse(elementListe, cssKlasse) {
  const arr = Array.isArray(elementListe) ? elementListe : Array.from(elementListe || []);
  return arr.filter(el => el && el.classList && el.classList.contains(cssKlasse));
}

function aktualisiereZaehlerAnzeige(aktuellerWert, schwellenwert = 10) {
  const istKritisch = aktuellerWert >= schwellenwert;
  return {
    text: `Zähler: ${aktuellerWert} / ${schwellenwert}`,
    wert: aktuellerWert,
    istKritisch,
    statusKlasse: istKritisch ? "status-kritisch" : "status-normal"
  };
}
