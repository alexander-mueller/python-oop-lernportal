# JS 03: Funktionen, Gültigkeitsbereiche (Scope) & Closures 🔐

Willkommen zu **Modul 03** des JavaScript-Kurses!

In JavaScript sind Funktionen sogenannte **First-Class Citizens**: Sie können wie gewöhnliche Variablen gespeichert, als Argumente übergeben und von anderen Funktionen zurückgegeben werden (*Higher-Order Functions*). 

In diesem Modul meisterst du moderne Funktionsarten, Gültigkeitsbereiche (*Scopes*) und eines der faszinierendsten Kernkonzepte von JavaScript: **Closures**!

---

## 💡 1. Das Wichtigste in Kürze

### A. Funktionsarten im Vergleich

#### 1. Function Declaration (Klassische Funktionsdeklaration)
Wird vollständig gehoistet (kann bereits vor ihrer Definition im Code aufgerufen werden):

```javascript
console.log(quadriere(4)); // 16 (funktioniert dank Hoisting!)

function quadriere(x) {
  return x * x;
}
```

#### 2. Function Expression (Funktionsausdruck)
Wird einer Variablen zugewiesen und ist erst ab der Zuweisungszeile verfügbar:

```javascript
const verdopple = function(x) {
  return x * 2;
};
```

#### 3. Arrow Function (Pfeilfunktion / ES6)
Kompakte Syntax, kein eigenes `this` oder `arguments`-Objekt:

```javascript
// Ausführliche Arrow Function:
const addiere = (a, b) => {
  return a + b;
};

// Einzeilige Arrow Function mit implizitem Return:
const multipliziere = (a, b) => a * b;
```

---

### B. Moderne Parameter: Default- & Rest-Parameter

#### 1. Default-Parameter (Standardwerte)
Verhindert `undefined`, wenn kein Wert übergeben wird:

```javascript
function begruesse(name = "Gast", sprache = "de") {
  return sprache === "de" ? `Hallo, ${name}!` : `Hello, ${name}!`;
}

console.log(begruesse()); // "Hallo, Gast!"
console.log(begruesse("Anna", "en")); // "Hello, Anna!"
```

#### 2. Rest-Parameter (`...rest`)
Sammelt eine beliebige Anzahl von Argumenten in einem echten JavaScript-Array:

```javascript
function maxZahl(...zahlen) {
  // 'zahlen' ist ein echtes Array!
  return Math.max(...zahlen);
}

console.log(maxZahl(3, 9, 21, 4)); // 21
```

---

### C. Gültigkeitsbereiche (Scopes) & Hoisting

JavaScript kennt drei Ebenen von Scopes:

```
┌─────────────────────────────────────────────────────────┐
│ 🌍 GLOBAL SCOPE (Überall im Programm sichtbar)           │
│   const globalVar = "Welt";                             │
│                                                         │
│   ┌─────────────────────────────────────────────────┐   │
│   │ 📦 FUNCTION SCOPE (Nur innerhalb der Funktion)  │   │
│   │   function meineFunktion() {                    │   │
│   │     const funcVar = "Funktion";                 │   │
│   │                                                 │   │
│   │     ┌───────────────────────────────────────┐   │   │
│   │     │ 🔒 BLOCK SCOPE (if, for, { let/const})│   │   │
│   │     │   if (true) {                         │   │   │
│   │     │     const blockVar = "Block";         │   │   │
│   │     │   }                                   │   │   │
│   │     └───────────────────────────────────────┘   │   │
│   │   }                                             │   │
│   └─────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

- **`let` und `const`** besitzen **Block-Scope** (gelten nur innerhalb der `{ ... }` geschweiften Klammern).
- **`var`** besitzt nur **Function-Scope** (ignoriert `if`- und `for`-Blöcke) und sollte in modernem JS vermieden werden.
- **Lexical Scope (Statische Bindung):** Innere Funktionen können auf Variablen ihrer äußeren Eltern-Scopes zugreifen, aber nicht umgekehrt!

---

### D. Closures: Das Super-Feature

> **Definition Closure:** Eine Closure entsteht, wenn eine innere Funktion Zugriff auf Variablen ihres äußeren Gültigkeitsbereichs behält – **selbst nachdem die äußere Funktion ihre Ausführung längst beendet hat**.

```javascript
function erstelleSparschwein() {
  let guthaben = 0; // Private Variable, von außen nicht direkt änderbar!

  return function(einzahlung) {
    guthaben += einzahlung;
    return `Aktuelles Guthaben: ${guthaben} €`;
  };
}

const meinKonto = erstelleSparschwein();
console.log(meinKonto(50));  // "Aktuelles Guthaben: 50 €"
console.log(meinKonto(100)); // "Aktuelles Guthaben: 150 €"

// Wichtig: 'guthaben' kann von außen nicht manipuliert werden (z.B. kein meinKonto.guthaben = 0)!
```

---

## 🔐 Die didaktische Analogie: "Der Tresor mit Geheimzahl"

Stelle dir eine Closure wie einen **verschlossenen Tresor mit einem Einwurf-Schlitz und Zahlenrad** vor:

- **Der Erbauer (Die äußere Factory-Funktion):**  
  Die äußere Funktion baut den Tresor und legt die interne Mechanik (die geschützten Variablen `let zaehler`) im Inneren des Gehäuses an.
- **Der Schlüsselanhänger (Die zurückgegebene innere Funktion):**  
  Du erhältst von der Funktion lediglich den Schlüssel (die Referenz auf die innere Funktion). 
- **Geschützte Kapselung (Data Encapsulation):**  
  Niemand von außen kann die Tresorwand aufbrechen oder direkt an die internen Zahnräder fassen. Nur wenn du den Schlüssel drehst (`zaehler()`), verändert sich der interne Zählerstand kontrolliert.
- **Unabhängige Instanzen:**  
  Jeder neue Aufruf der äußeren Funktion baut einen komplett eigenständigen Tresor. Tresor A und Tresor B beeinflussen sich gegenseitig zu keinem Zeitpunkt!

---

## 🎯 Aufgaben & Teilziele in `aufgabe.js`

Öffne die Datei `aufgabe.js` und implementiere folgende 4 Funktionen:

1. **TODO 1: `erstelleZaehler(startWert = 0)`**  
   Gibt eine Zählerfunktion (Closure) zurück. Jeder Aufruf erhöht den internen Zähler um 1 und gibt den neuen Stand zurück.

2. **TODO 2: `multiplizierer(faktor)`**  
   Erzeugt eine Multiplikator-Funktion (Closure): `(x) => x * faktor`.  
   *Beispiel:* `const verdopple = multiplizierer(2); verdopple(5); // 10`

3. **TODO 3: `summiereAlles(...zahlen)`**  
   Nimmt beliebig viele Zahlen per Rest-Parameter entgegen und gibt deren Gesamtsumme zurück. Bei leerem Aufruf wird `0` zurückgegeben.

4. **TODO 4: `erstellePraefixierer(praefix)`**  
   Gibt eine Funktion (Closure) zurück, die vor jeden übergebenen String das vorgegebene `praefix` anhängt: `(text) => `${praefix}${text}``.

---

## 🧪 Tests ausführen

Öffne die Web-IDE oder führe die Testsuite aus:

```bash
# Im Browser:
workspace.html?course=javascript&track=track_1_grundlagen&chapter=03_funktionen_und_scope
```
