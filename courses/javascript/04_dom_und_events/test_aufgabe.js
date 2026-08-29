// 🧪 JS 04: Testsuite für DOM-Manipulation & Events

// Mock-DOM Umgebung für Headless / Web-Worker Ausführung
if (typeof document === "undefined") {
  globalThis.document = {
    createElement(tagName) {
      const classes = new Set();
      const listeners = {};
      const el = {
        tagName: String(tagName).toUpperCase(),
        textContent: "",
        innerHTML: "",
        get className() {
          return Array.from(classes).join(" ");
        },
        set className(val) {
          classes.clear();
          if (val) String(val).trim().split(/\s+/).forEach(c => c && classes.add(c));
        },
        classList: {
          add(...tokens) {
            tokens.forEach(t => t && classes.add(String(t)));
          },
          remove(...tokens) {
            tokens.forEach(t => classes.delete(String(t)));
          },
          toggle(token) {
            if (classes.has(token)) {
              classes.delete(token);
              return false;
            } else {
              classes.add(token);
              return true;
            }
          },
          contains(token) {
            return classes.has(token);
          }
        },
        addEventListener(event, callback) {
          if (!listeners[event]) listeners[event] = [];
          listeners[event].push(callback);
        },
        dispatchEvent(eventObj) {
          const type = typeof eventObj === "string" ? eventObj : eventObj.type;
          const list = listeners[type] || [];
          const ev = typeof eventObj === "string" ? { type, target: this } : eventObj;
          list.forEach(cb => cb(ev));
        },
        click() {
          this.dispatchEvent({ type: "click", target: this });
        }
      };
      return el;
    }
  };
}

// Test 1: erzeugeButtonElement
let clicked = false;
const btn1 = erzeugeButtonElement("Speichern", "btn-primary", () => { clicked = true; });

assert.ok(btn1, "erzeugeButtonElement() sollte ein Element zurückgeben");
assert.strictEqual(btn1.textContent, "Speichern", "Button textContent sollte 'Speichern' sein");
assert.ok(btn1.classList.contains("btn-primary"), "Button sollte die Klasse 'btn-primary' besitzen");

if (typeof btn1.click === "function") {
  btn1.click();
} else if (typeof btn1.dispatchEvent === "function") {
  btn1.dispatchEvent({ type: "click" });
}
assert.strictEqual(clicked, true, "Button Click-Callback sollte beim Klick ausgelöst werden");

// Test 1b: erzeugeButtonElement ohne optionale Klasse/Callback
const btnSimple = erzeugeButtonElement("Abbrechen");
assert.strictEqual(btnSimple.textContent, "Abbrechen", "Einfacher Button ohne Parameter sollte funktionieren");

// Test 2: erstelleListenEintrag
const liOffen = erstelleListenEintrag("Milch kaufen", false);
assert.ok(liOffen, "erstelleListenEintrag() sollte ein <li> Element zurückgeben");
assert.strictEqual(liOffen.textContent, "Milch kaufen", "Listeneintrag-Text sollte 'Milch kaufen' sein");
assert.strictEqual(liOffen.classList.contains("erledigt"), false, "Unerledigter Eintrag darf nicht die Klasse 'erledigt' haben");

const liErledigt = erstelleListenEintrag("Post abholen", true);
assert.strictEqual(liErledigt.textContent, "Post abholen", "Erledigter Eintrag Text sollte stimmen");
assert.strictEqual(liErledigt.classList.contains("erledigt"), true, "Erledigter Eintrag muss die Klasse 'erledigt' besitzen");

// Test 3: filtereElementeNachKlasse
const el1 = document.createElement("div");
el1.classList.add("aktiv");
const el2 = document.createElement("div");
el2.classList.add("inaktiv");
const el3 = document.createElement("div");
el3.classList.add("aktiv");
el3.classList.add("hervorgehoben");

const gefiltertAktiv = filtereElementeNachKlasse([el1, el2, el3], "aktiv");
assert.strictEqual(gefiltertAktiv.length, 2, "filtereElementeNachKlasse() sollte 2 aktive Elemente finden");
assert.strictEqual(gefiltertAktiv[0], el1, "Erstes gefiltertes Element sollte el1 sein");
assert.strictEqual(gefiltertAktiv[1], el3, "Zweites gefiltertes Element sollte el3 sein");

const gefiltertHervorgehoben = filtereElementeNachKlasse([el1, el2, el3], "hervorgehoben");
assert.strictEqual(gefiltertHervorgehoben.length, 1, "Sollte 1 hervorgehobenes Element finden");

// Test 4: aktualisiereZaehlerAnzeige
const statusNormal = aktualisiereZaehlerAnzeige(5, 10);
assert.deepStrictEqual(
  statusNormal,
  { text: "Zähler: 5 / 10", wert: 5, istKritisch: false, statusKlasse: "status-normal" },
  "aktualisiereZaehlerAnzeige(5, 10) sollte Normalstatus liefern"
);

const statusKritisch = aktualisiereZaehlerAnzeige(10, 10);
assert.deepStrictEqual(
  statusKritisch,
  { text: "Zähler: 10 / 10", wert: 10, istKritisch: true, statusKlasse: "status-kritisch" },
  "aktualisiereZaehlerAnzeige(10, 10) bei Erreichen des Schwellenwerts sollte kritisch sein"
);

const statusUeberlimit = aktualisiereZaehlerAnzeige(15, 10);
assert.strictEqual(statusUeberlimit.istKritisch, true, "Überlimit sollte istKritisch=true haben");
assert.strictEqual(statusUeberlimit.statusKlasse, "status-kritisch", "Überlimit sollte 'status-kritisch' haben");

const statusDefault = aktualisiereZaehlerAnzeige(3);
assert.strictEqual(statusDefault.text, "Zähler: 3 / 10", "Standard-Schwellenwert sollte 10 sein");

console.log("✅ Alle 14 Tests in JS 04 erfolgreich bestanden!");
