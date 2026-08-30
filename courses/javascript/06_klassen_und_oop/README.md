# 🌐 JS 06: Klassen & Objektorientierung (OOP)

Willkommen zu **Modul 06** des JavaScript-Kurses! In diesem Modul lernst du, wie moderne objektorientierte Programmierung (OOP) in JavaScript mit ES6-Klassensyntax funktioniert.

---

## 🎯 Lernziele

Nach diesem Modul kannst du:
1. **ES6-Klassen** mit `class`, `constructor` und Instanzmethoden definieren.
2. Den **`this`**-Kontext innerhalb von Klasseninstanzen verstehen und sicher anwenden.
3. Daten mit **Gettern (`get`) und Settern (`set`)** kapseln und vor fehlerhaften Werten schützen.
4. **Vererbung (`extends`)** nutzen und den Elternkonstruktor mit **`super(...)`** aufrufen.
5. **Statische Methoden & Fabrikfunktionen (`static`)** definieren und anwenden.
6. Objekt-Typen zur Laufzeit mit **`instanceof`** überprüfen.

---

## 💡 Theoretische Grundlagen

### 1. Der Klassen-Bauplan (`class`, `constructor`, `this`)

Vor ECMAScript 2015 (ES6) basierte OOP in JavaScript rein auf Prototypen-Funktionen (`function Person() { ... } Person.prototype.sayHi = ...`). Die ES6-Klassensyntax bietet dafür eine moderne, lesbare und aus anderen Sprachen gewohnte Syntax:

```javascript
class Person {
  constructor(vorname, nachname) {
    this.vorname = vorname;
    this.nachname = nachname;
  }

  vollstaendigerName() {
    return `${this.vorname} ${this.nachname}`;
  }
}

const user = new Person("Max", "Mustermann");
console.log(user.vollstaendigerName()); // "Max Mustermann"
```

### 2. Kapselung & Getter/Setter

Kapselung (Encapsulation) ist eines der 4 Grundprinzipien der OOP. Interne Zustände sollten nicht ungeschützt direkt verändert werden.

```javascript
class Bankkonto {
  constructor(inhaber, startSaldo = 0) {
    this.inhaber = inhaber;
    this._saldo = startSaldo; // Konvention: _ kennzeichnet private/interne Felder
  }

  // Getter ermöglicht das Lesen wie ein Attribut: konto.saldo
  get saldo() {
    return this._saldo;
  }

  einzahlen(betrag) {
    if (typeof betrag !== "number" || betrag <= 0) {
      throw new Error("Einzahlungsbetrag muss positiv sein.");
    }
    this._saldo += betrag;
    return this._saldo;
  }
}
```

### 3. Vererbung mit `extends` und `super`

Kindklassen erben alle Methoden und Eigenschaften ihrer Basisklasse:

```javascript
class Fahrzeug {
  constructor(marke, modell, baujahr) {
    this.marke = marke;
    this.modell = modell;
    this.baujahr = baujahr;
  }

  beschreibung() {
    return `${this.marke} ${this.modell} (${this.baujahr})`;
  }
}

class ElektroAuto extends Fahrzeug {
  constructor(marke, modell, baujahr, batterieKapazitaet) {
    // ⚠️ WICHTIG: super() MUSS vor dem ersten Zugriff auf 'this' aufgerufen werden!
    super(marke, modell, baujahr);
    this.batterieKapazitaet = batterieKapazitaet;
  }

  // Überschreiben (Method Overriding):
  beschreibung() {
    return `${super.beschreibung()} [Elektro: ${this.batterieKapazitaet} kWh]`;
  }

  reichweiteBerechnen(verbrauchPro100km) {
    return (this.batterieKapazitaet / verbrauchPro100km) * 100;
  }
}
```

### 4. Statische Methoden (`static`)

Statische Methoden werden direkt an der Klasse aufgerufen, ohne eine Instanz mit `new` erstellen zu müssen. Sie eignen sich perfekt als Fabrikmethoden (Factory Pattern):

```javascript
class ElektroAuto extends Fahrzeug {
  // ...
  static erstelleStandardTesla() {
    return new ElektroAuto("Tesla", "Model 3", 2024, 75);
  }
}

const auto = ElektroAuto.erstelleStandardTesla();
```

---

## 🏭 Didaktische Analogie: Der Bauplan & die Fabrikstraße

- **Klasse (`class`)**: Der technische CAD-Bauplan in den Köpfen der Ingenieure.
- **Instanz (`new`)**: Das fertig montierte Auto, das die Fabrikhalle verlässt.
- **Konstruktor (`constructor`)**: Das Fließband, das Rohkarosserien mit Motor und Farbe ausstattet.
- **Methoden (`this.fahren()`)**: Die Pedale und Funktionen des Fahrzeugs.
- **Statische Methoden (`static`)**: Die Roboterwerkzeuge in der Werkshalle.

---

## 🎯 Aufgabenübersicht in `aufgabe.js`

1. **TODO 1: Bankkonto**:
   - `constructor(inhaber, startSaldo = 0)`
   - `get saldo`
   - `einzahlen(betrag)`
   - `abheben(betrag)`
2. **TODO 2: Fahrzeug**:
   - `constructor(marke, modell, baujahr)`
   - `beschreibung()`
3. **TODO 3: ElektroAuto extends Fahrzeug**:
   - `constructor(marke, modell, baujahr, batterieKapazitaet)`
   - `reichweiteBerechnen(verbrauchPro100km)`
   - `beschreibung()`
4. **TODO 4: ElektroAuto.erstelleStandardTesla()**:
   - Statische Fabrikmethode zur schnellen Erstellung eines Tesla Model 3.

---

## 🧪 Tests ausführen

Führe die Testsuite in der Web-IDE oder lokal aus:
```bash
# In der Web-IDE: Klicke auf 'Code ausführen & testen'
```
