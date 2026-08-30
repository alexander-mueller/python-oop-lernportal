# JS 04: Arrays, Sets & Maps 📊

Willkommen zu **Modul 04** des JavaScript-Kurses!

In modernen Web-Anwendungen sind saubere Datenstrukturen das A und O. JavaScript stellt dir drei mächtige Sammlungen zur Verfügung:
1. **Arrays:** Geordnete, indexierte Listen mit funktionalen Methoden wie `.map()`, `.filter()`, `.reduce()`.
2. **Sets:** Sammlungen einzigartiger Werte – doppelte Einträge werden automatisch eliminiert.
3. **Maps:** Flexible Schlüssel-Wert-Speicher, die im Gegensatz zu normalen Objekten jeden Datentyp als Schlüssel erlauben.

---

## 💡 1. Das Wichtigste in Kürze

### A. Funktionale Array-Methoden (ES6+)

Statt schwerfälliger `for`-Schleifen transformieren wir Arrays deklarativ und ohne Seiteneffekte:

```javascript
const zahlen = [1, 2, 3, 4, 5];

// 🎯 1. .map(): Jedes Element eins-zu-eins transformieren
const verdoppelt = zahlen.map(x => x * 2); // [2, 4, 6, 8, 10]

// 🎯 2. .filter(): Elemente nach einer Bedingung filtern
const gerade = zahlen.filter(x => x % 2 === 0); // [2, 4]

// 🎯 3. .reduce(): Das gesamte Array zu einem Einzelwert aggregieren
const summe = zahlen.reduce((akkumulator, aktuellerWert) => akkumulator + aktuellerWert, 0); // 15
```

---

### B. Sets: Mengen ohne Duplikate

Ein `Set` speichert ausschließlich **eindeutige Werte**. Versuche, denselben Wert mehrfach hinzuzufügen, werden ignoriert:

```javascript
// Set erstellen:
const farben = new Set(["rot", "gruen", "rot", "blau"]);
console.log(farben.size); // 3 (da "rot" nur 1x gezählt wird)

// Werte hinzufügen & prüfen:
farben.add("gelb");
console.log(farben.has("rot")); // true (extrem schnelle O(1) Prüfung!)
farben.delete("blau");

// 🌟 Duplikate aus einem Array in 1 Zeile entfernen:
const mitDuplikaten = [1, 2, 2, 3, 3, 3, 4];
const ohneDuplikate = [...new Set(mitDuplikaten)]; // [1, 2, 3, 4]
```

---

### C. Maps: Schlüssel-Wert-Speicher (Key-Value)

Eine `Map` speichert Schlüssel-Wert-Paare in Einfügereihenfolge. Im Gegensatz zu einfachen `{}` Objekten darf ein Schlüssel in einer Map **jeder beliebige Typ** sein (auch Objekte, Zahlen oder Booleans):

```javascript
// Map instanziieren:
const benutzerStatus = new Map();

// Einträge setzen & abrufen:
benutzerStatus.set("user_101", { online: true, rolle: "Admin" });
benutzerStatus.set("user_102", { online: false, rolle: "Gast" });

console.log(benutzerStatus.get("user_101")); // { online: true, rolle: "Admin" }
console.log(benutzerStatus.has("user_999")); // false
console.log(benutzerStatus.size);            // 2

// Aus 2D-Array initialisieren:
const uebersetzung = new Map([
  ["de", "Guten Tag"],
  ["en", "Good day"],
  ["fr", "Bonjour"]
]);
console.log(uebersetzung.get("en")); // "Good day"
```

---

## 🎭 Die didaktische Analogie: "Fotogalerie, VIP-Club & Telefonbuch"

- 📸 **Das Array (Die Fotogalerie):**  
  Wie ein Fotoalbum: Jedes Foto liegt an einer festen Position (`index 0, 1, 2...`). Du kannst dasselbe Bild mehrfach einkleben. Mit Filtern legst du Schablonen über alle Bilder.

- 🎟️ **Das Set (Der VIP-Club):**  
  Der Türsteher führt eine Gästeliste. Niemand kommt doppelt auf die Liste. Wenn jemand bereits drin ist (`set.has("Max")`), wird ein zweiter Einlassversuch ignoriert.

- 📖 **Die Map (Das schlaue Telefonbuch):**  
  Zu jedem Namen (Schlüssel) gibt es den passenden Eintrag (Wert). Du schlägst blitzschnell den Namen nach (`map.get("Anna")`) und erhältst direkt die hinterlegte Information.

---

## 🎯 Aufgaben & Teilziele in `aufgabe.js`

1. **TODO 1: `verdoppeln(zahlen)`**  
   Gibt ein neues Array zurück, in dem alle Zahlen mit `.map()` verdoppelt wurden.

2. **TODO 2: `filterGeradeZahlen(zahlen)`**  
   Filtert mit `.filter()` nur die geraden Zahlen heraus.

3. **TODO 3: `arraySumme(zahlen)`**  
   Berechnet die Summe aller Array-Elemente mit `.reduce()` (Standardwert `0`).

4. **TODO 4: `entferneDuplikate(liste)`**  
   Eliminiert alle Duplikate aus dem übergebenen Array mithilfe von `new Set()` und gibt ein bereinigtes Array zurück.

5. **TODO 5: `erstelleWoerterbuch(paare)`**  
   Erzeugt eine neue JavaScript `Map` aus dem übergebenen 2D-Array von Schlüssel-Wert-Paaren (`[[k, v], ...]`).

6. **TODO 6: `zaehleHaeufigkeiten(woerter)`**  
   Zählt die Häufigkeit jedes Wortes im Array und gibt eine `Map` zurück, die jedes Wort auf seine Anzahl abbildet.

---

## 🧪 Tests ausführen

Öffne die Web-IDE oder führe die Tests aus:

```bash
# Im Browser:
workspace.html?course=javascript&track=track_1_grundlagen&chapter=04_arrays_sets_und_maps
```
