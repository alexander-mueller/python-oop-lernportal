# JS 03: Objekte, Destructuring & Rest/Spread 📦

Willkommen zu **Modul 03** des JavaScript-Kurses!

Objekte sind der Herzschlag von JavaScript: Fast alles in JavaScript ist ein Objekt oder verhält sich wie eines. In diesem Modul lernst du, wie du strukturierte Daten erstellst, mit modernem **ES6-Destructuring** blitzschnell entpackst und Daten mit dem **Spread- & Rest-Operator (`...`)** elegant transformierst.

---

## 💡 1. Das Wichtigste in Kürze

### A. Object Literals & Property Shorthand
Ein Objekt speichert Daten als **Schlüssel-Wert-Paare** (*Key-Value Pairs*):

```javascript
// Klassische Deklaration
const person = {
  name: "Max",
  alter: 25,
  istEntwickler: true
};

// ES6 Property Shorthand (Wenn Variablenname und Key identisch sind)
const name = "Anna";
const email = "anna@example.com";
const user = { name, email }; 
// Entspricht: { name: name, email: email }
```

### B. Destructuring Assignment (Objekte & Arrays entpacken)
Mit Destructuring kannst du Werte direkt aus Objekten oder Arrays extrahieren, ohne wiederholt `objekt.eigenschaft` schreiben zu müssen:

```javascript
const dev = { name: "Sarah", sprache: "JavaScript", erfahrung: 5 };

// 🎯 Object Destructuring:
const { name, sprache } = dev;
console.log(name);    // "Sarah"
console.log(sprache); // "JavaScript"

// 🎯 Alias (Umbennen) & Standardwerte (Default Values):
const { alter = 18, name: vorname } = dev;
console.log(alter);   // 18 (Default-Wert, da 'alter' im Objekt fehlt)
console.log(vorname); // "Sarah" (unter neuem Namen verfügbar)

// 🎯 Array Destructuring:
const farben = ["#ff0000", "#00ff00", "#0000ff"];
const [rot, gruen] = farben;
console.log(rot); // "#ff0000"
```

### C. Spread- & Rest-Operator (`...`)
Die drei Punkte `...` haben je nach Kontext zwei mächtige Funktionen:

1. **Spread-Operator (Ausbreiten / Zusammenfügen):**
   Erzeugt eine flache Kopie (*Shallow Copy*) oder kombiniert mehrere Objekte/Arrays ohne Mutation:
   ```javascript
   const basisInfo = { name: "Tom", alter: 30 };
   const kontakt = { email: "tom@web.de", stadt: "Berlin" };

   // Neues Objekt mit allen Eigenschaften beider Objekte:
   const vollstaendig = { ...basisInfo, ...kontakt, premium: true };
   ```

2. **Rest-Operator (Einsammeln des Rests):**
   Sammelt verbleibende Eigenschaften in einem neuen Objekt/Array:
   ```javascript
   const { email, ...andereDaten } = vollstaendig;
   console.log(email);       // "tom@web.de"
   console.log(andereDaten); // { name: "Tom", alter: 30, stadt: "Berlin", premium: true }
   ```

### D. Hilfsmethoden: `Object.keys()`, `Object.values()`, `Object.entries()`
```javascript
const auto = { marke: "Tesla", modell: "Model 3", baujahr: 2024 };

console.log(Object.keys(auto));    // ["marke", "modell", "baujahr"]
console.log(Object.values(auto));  // ["Tesla", "Model 3", 2024]
console.log(Object.entries(auto)); // [["marke", "Tesla"], ["modell", "Model 3"], ["baujahr", 2024]]
console.log(Object.keys(auto).length); // 3 (Anzahl der Eigenschaften)
```

---

## 🧰 Die didaktische Analogie: "Die Werkzeugkiste & Auspack-Station"

- **Das Objekt als Werkzeugkiste:**  
  Ein Objekt `{ hammer: "500g", saege: "Holz", bohrer: "Akku" }` ist wie eine strukturierte Werkzeugkiste mit beschrifteten Fächern.
- **Destructuring als gezieltes Herausgreifen:**  
  Statt die ganze schwere Kiste an die Baustelle zu tragen (`werkzeugkiste.hammer`), greifst du mit `const { hammer, saege } = werkzeugkiste;` genau die Werkzeuge heraus, die du für die aktuelle Arbeit brauchst.
- **Spread (`...`) als Zusammenlegen in eine neue Kiste:**  
  Mit `{ ...kiste1, ...kiste2, multimeter: "digital" }` schüttest du zwei Werkzeugkisten in eine neue, größere Kiste um und packst noch ein neues Werkzeug dazu – die ursprünglichen Kisten bleiben unberührt (*Immutability*)!

---

## 🎯 Aufgaben & Teilziele in `aufgabe.js`

Öffne die Datei `aufgabe.js` und löse die 5 Teilziele:

1. **TODO 1:** `erstelleBenutzer(name, email, rolle = "user")`  
   Erstelle und gib ein Objekt mit `{ name, email, rolle }` unter Verwendung des Property Shorthands zurück.

2. **TODO 2:** `extrahiereDetails(benutzerObjekt)`  
   Extrahiere `name` und `email` mit Destructuring und gib den String `"${name} (${email})"` zurück.

3. **TODO 3:** `fuegeAdresseHinzu(benutzerObjekt, adresseObjekt)`  
   Erzeuge mit Spread (`...`) ein neues, zusammengeführtes Objekt `{ ...benutzerObjekt, ...adresseObjekt }`, ohne `benutzerObjekt` zu verändern.

4. **TODO 4:** `zaehleEigenschaften(objekt)`  
   Ermittle die Anzahl der Eigenschaften eines Objekts mit `Object.keys(objekt).length`.

5. **TODO 5:** `berechneWarenkorbGesamtwert(warenkorbItems)`  
   Berechne die Summe aus `preis * anzahl` für alle Items im Array. Nutze Destructuring (`const { preis, anzahl = 1 }`) im Schleifendurchlauf oder in `.reduce()`.

---

## 🧪 Tests ausführen

Führe den Test in der interaktiven Web-IDE oder im Runner aus. Deine Lösung ist perfekt, wenn alle Tests erfolgreich durchlaufen!
