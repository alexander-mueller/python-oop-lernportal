# JS 02: Kontrollfluss, Verzweigungen & Schleifen 🚦

Willkommen zu **Modul 02** des JavaScript-Kurses!

In realen Programmen läuft Code selten nur starr von oben nach unten ab. Ein Programm muss Entscheidungen treffen ("Ist der Benutzer eingeloggt?", "Hat der Kunde einen Rabatt?") und Aktionen wiederholen ("Durchsuche 1000 Produkte", "Summiere Zahlen").

In diesem Modul lernst du alle Werkzeuge kennen, mit denen du den Kontrollfluss deines JavaScript-Codes präzise und elegant steuerst.

---

## 💡 1. Das Wichtigste in Kürze

### A. Verzweigungen: `if`, `else if`, `else`
Mit Verzweigungen führst du Codeblöcke nur dann aus, wenn bestimmte Bedingungen erfüllt (`true`) sind:

```javascript
const punkte = 85;

if (punkte >= 90) {
  console.log("Note: Sehr gut");
} else if (punkte >= 75) {
  console.log("Note: Gut");
} else if (punkte >= 50) {
  console.log("Note: Bestanden");
} else {
  console.log("Note: Nicht bestanden");
}
```

#### ⚠️ Strikter Vergleich: `===` vs. `==`
Verwende in modernem JavaScript **immer den strikten Gleichheitsoperator `===`** (und Ungleichheit `!==`):
- `===` prüft Wert **und Datentyp** (ohne implizite Typkonvertierung).
- `==` führt vorher eine automatische Typumwandlung (*Type Coercion*) durch, was zu tückischen Bugs führt (`0 == ""` ist `true`, aber `0 === ""` ist `false`).

```javascript
console.log(5 === "5");  // false (Zahl vs. String)
console.log(5 == "5");   // true  (Achtung: Gefährlich!)
console.log(null === undefined); // false
```

---

### B. Die `switch-case`-Anweisung
Wenn eine einzelne Variable gegen viele diskrete Werte geprüft werden soll, ist `switch` oft übersichtlicher als endlose Ketten von `else if`:

```javascript
const status = "geliefert";

switch (status) {
  case "bestellt":
    console.log("Paket wird verpackt.");
    break; // Verhindert 'Fall-Through' zum nächsten Case!
  case "unterwegs":
    console.log("Paket ist im Zustellfahrzeug.");
    break;
  case "geliefert":
    console.log("Paket erfolgreich zugestellt!");
    break;
  default:
    console.log("Unbekannter Status.");
}
```

> **Wichtig:** Vergiss niemals das `break;` am Ende jedes Case-Blocks, außer du möchtest bewusst mehrere Cases zusammenfassen (*Fall-Through*).

---

### C. Der Ternäre Operator (`? :`)
Für einfache Entweder-Oder-Zuweisungen bietet der ternäre Operator eine kompakte Einzeiler-Syntax:

$$\text{Bedingung} \ ? \ \text{Wert wenn wahr} \ : \ \text{Wert wenn falsch}$$

```javascript
const alter = 20;
const status = alter >= 18 ? "Erwachsen" : "Minderjährig";
console.log(status); // "Erwachsen"

// Auch kombinierbar für Rabatte:
const istPremium = true;
const rabatt = istPremium ? 0.2 : 0.0;
```

---

### D. Schleifen in JavaScript

#### 1. Die klassische Zählschleife: `for (let i = 0; i < n; i++)`
Ideal, wenn du die genaue Anzahl der Durchläufe kennst oder den Index benötigst:

```javascript
for (let i = 1; i <= 5; i++) {
  console.log(`Durchlauf Nummer: ${i}`);
}
```

#### 2. Die moderne Iterationsschleife: `for (const element of array)`
Perfekt zum Durchlaufen von Arrays und iterierbaren Datenstrukturen:

```javascript
const fruechte = ["Apfel", "Banane", "Mango"];
for (const frucht of fruechte) {
  console.log(`Lecker: ${frucht}`);
}
```

#### 3. Die Objekt-Schlüsselschleife: `for (const key in object)`
Durchläuft alle Schlüssel (*Keys*) eines Objekts:

```javascript
const auto = { marke: "BMW", baujahr: 2023, ps: 190 };
for (const eigenschaft in auto) {
  console.log(`${eigenschaft}: ${auto[eigenschaft]}`);
}
```

#### 4. Bedingungsgesteuerte Schleifen: `while` & `do...while`
- `while (bedingung)`: Prüft die Bedingung **vor** dem ersten Durchlauf.
- `do { ... } while (bedingung)`: Führt den Codeblock **mindestens einmal** aus, bevor geprüft wird.

```javascript
let energie = 100;
while (energie > 0) {
  console.log(`Akku bei ${energie}%`);
  energie -= 25;
}
```

---

### E. Schleifensteuerung: `break` und `continue`

- **`break`**: Bricht die gesamte Schleife sofort ab und springt hinter die Schleife.
- **`continue`**: Bricht nur den *aktuellen Durchlauf* ab und springt direkt zur nächsten Iteration.

```javascript
// Beispiel: Nur ungerade Zahlen überspringen (continue) und bei 8 stoppen (break)
for (let i = 1; i <= 10; i++) {
  if (i % 2 !== 0) {
    continue; // Ungerade Zahl -> Weiter zur nächsten Zahl
  }
  if (i > 8) {
    break; // Beende Schleife vorzeitig
  }
  console.log(i); // Gibt 2, 4, 6, 8 aus
}
```

---

## 🚦 Die didaktische Analogie: "Die Verkehrsampeln & Kreisverkehre im Code"

Stelle dir den Programmablauf wie eine Autofahrt durch eine moderne Stadt vor:

- 🟢 **Die Ampelkreuzung (`if` / `else` / `switch`):**  
  Dein Auto rollt auf eine Kreuzung zu. Steht die Ampel auf Grün (`true`), fährst du geradeaus weiter. Zeigt sie Rot (`false`), biegst du in die Ausweichroute (`else`) ab. Eine `switch`-Kreuzung ist ein mehrspuriger Verteiler: Jede Spur führt zu einem anderen Ziel (`case`), und wenn keine passt, nimmst du die Notspur (`default`).

- 🔄 **Der Kreisverkehr (`while` / `for`):**  
  Schleifen sind wie ein Kreisverkehr. Du drehst solange deine Runden, bis eine bestimmte Bedingung nicht mehr erfüllt ist oder du deine gewünschte Ausfahrt entdeckst.
  - Mit **`continue`** bleibst du auf der Innenbahn und fährst ohne Anhalten direkt in die nächste Runde.
  - Mit **`break`** nimmst du sofort die Ausfahrt und verlässt den Kreisverkehr endgültig.

---

## 🎯 Aufgaben & Teilziele in `aufgabe.js`

Öffne die Datei `aufgabe.js` und implementiere folgende 5 Funktionen:

1. **TODO 1: `kategorisiereAlter(alter)`**  
   Kategorisiert ein Alter in String-Gruppen:
   - `< 13` $\rightarrow$ `"Kind"`
   - `13` bis `17` $\rightarrow$ `"Jugendlicher"`
   - `18` bis `64` $\rightarrow$ `"Erwachsener"`
   - $\ge 65$ $\rightarrow$ `"Senior"`

2. **TODO 2: `wochentagName(tagNummer)`**  
   Wandelt eine Zahl `1` bis `7` in den Wochentag `"Montag"` bis `"Sonntag"` um. Alle anderen Eingaben liefern `"Ungültig"`. Verwende `switch(tagNummer)`.

3. **TODO 3: `berechneRabattpreis(preis, istPremium, hatGutschein)`**  
   Berechnet den rabattierten Endpreis:
   - Premium + Gutschein $\rightarrow$ 30% Rabatt (`preis * 0.7`)
   - Nur Premium $\rightarrow$ 20% Rabatt (`preis * 0.8`)
   - Nur Gutschein $\rightarrow$ 10% Rabatt (`preis * 0.9`)
   - Weder noch $\rightarrow$ kein Rabatt (`preis`)

4. **TODO 4: `summeGeraderZahlen(start, ende)`**  
   Summiert alle geraden Zahlen im Intervall $[start, ende]$. Verwende eine `for`-Schleife und `continue` für ungerade Zahlen.

5. **TODO 5: `findeErstesVielfaches(zahlen, teiler)`**  
   Durchsucht das Array `zahlen` mit `for...of` nach der ersten Zahl, für die `zahl % teiler === 0` gilt. Beende die Schleife mit `break` und gib die gefundene Zahl zurück (oder `null`, wenn kein Vielfaches existiert).

---

## 🧪 Tests ausführen

Öffne die Web-IDE im Browser oder starte den Testrunner:

```bash
# Im Browser:
workspace.html?course=javascript&track=track_1_grundlagen&chapter=02_kontrollfluss_und_schleifen
```
