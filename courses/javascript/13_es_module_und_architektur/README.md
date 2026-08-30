# JS 13: ES Module & Clean Architecture 🧱

Willkommen zu **Modul 13** des JavaScript-Kurses!

Große Softwareprojekte scheitern selten an einzelnen Algorithmen – sie scheitern an unübersichtlichem "Spaghetti-Code", bei dem alles mit allem verknüpft ist. 

In diesem Modul lernst du das offizielle JavaScript-Modulsystem (**ES Modules**) sowie grundlegende Architekturprinzipien wie **Separation of Concerns (SoC)** und **Dependency Injection (DI)** kennen.

---

## 💡 1. Das Wichtigste in Kürze

### A. Named Exports vs. Default Exports
In ES6+ teilst du Code in eigenständige Dateien auf:

```javascript
// 📁 mathUtils.js (Named Exports)
export const PI = 3.1415926535;

export function addieren(a, b) {
  return a + b;
}

export function multiplizieren(a, b) {
  return a * b;
}
```

```javascript
// 📁 RechnungsEngine.js (Default Export)
export default class RechnungsEngine {
  constructor() {
    this.name = "Haupt-Engine";
  }
}
```

---

### B. Module importieren
Beim Importieren kannst du gezielte Teile oder das gesamte Modul einbinden:

```javascript
// 1. Gezielter Named Import:
import { addieren, PI } from "./mathUtils.js";

// 2. Default Import (freier Name wählbar):
import RechnungsEngine from "./RechnungsEngine.js";

// 3. Namespace Import (alles als Objekt bündeln):
import * as MathUtils from "./mathUtils.js";
console.log(MathUtils.addieren(5, 3));
```

---

### C. Separation of Concerns (Trennung von Verantwortlichkeiten)
Saubere Software trennt verschiedene Aufgabenbereiche strikt:

```
┌─────────────────────────────────────────────────────────┐
│              RechnungsEngine (Controller)               │
│  - Steuert den Ablauf                                   │
│  - Kennt keine direkten UI-/DOM-Details                 │
└──────────────┬───────────────────────────┬──────────────┘
               │ nutzt                     │ nutzt
               ▼                           ▼
┌──────────────────────────────┐ ┌────────────────────────┐
│  MathModule (Logik & Mathe)  │ │ FormatterModule (View) │
│  - Reines Rechnen            │ │ - Währung ("1.250 €")  │
│  - Keine Nebeneffekte        │ │ - Datum ("2026-08-30") │
└──────────────────────────────┘ └────────────────────────┘
```

1. **Logikschicht (`MathModule`):** Rechnet präzise und wirft bei unzulässigen Werten (z.B. Division durch 0) kontrollierte Fehler.
2. **Präsentationsschicht (`FormatterModule`):** Bereitet Zahlen und Datumsangaben für Menschen lesbar auf (z.B. deutsches Währungsformat mit Komma und Tausendertrennzeichen).
3. **Orchestrierungsschicht (`RechnungsEngine`):** Verbindet Datenmodell und Schichten via **Dependency Injection** im Konstruktor.

---

## 🏗️ Die didaktische Analogie: "Die modularen Legosteine & Container-Bauweise"

- **Monolithischer Code ist wie eine Statue aus einem einzigen Steinblock:**  
  Willst du einen Arm anpassen, bricht der ganze Steinblock auseinander.
- **Modulare Software ist wie moderne Frachtcontainer & Legosteine:**  
  - Jeder Container hat standardisierte Eckbeschläge (definierte Schnittstelle / Exports).
  - Was im Container transportiert wird (interne Implementierung), ist dem Kran (Controller) egal.
  - Du kannst den Motor (z.B. ein Mathe-Modul) jederzeit gegen einen Turbomotor (Mock-Objekt im Test) austauschen, solange die Stecker passen (**Dependency Injection**).

---

## 🎯 Aufgaben & Teilziele in `aufgabe.js`

1. **TODO 1:** `MathModule`  
   Implementiere `addieren`, `subtrahieren`, `multiplizieren`, `dividieren` (mit Schutz vor Division durch 0) und `runden`.
2. **TODO 2:** `FormatterModule`  
   Implementiere `formatiereWaehrung` (deutsches Format, z.B. `1.250,50 EUR`) und `formatiereDatumIso` (`YYYY-MM-DD`).
3. **TODO 3:** `RechnungsEngine.erstellePosition(bezeichnung, menge, einzelpreis)`  
   Validiere Eingaben, berechne den Gesamtpreis über `this.math` und gib die Position zurück.
4. **TODO 4:** `RechnungsEngine.berechneRechnung(positionen, steuersatzProzent)`  
   Summiere Netto, berechne Steuer und Brutto, und formatiere alle Ausgaben über `this.formatter`.

---

## 🧪 Tests ausführen

Öffne die Web-IDE oder führe die Unittests aus. Sobald alle 20 Tests grün sind, hast du Modul-Architektur und saubere Code-Strukturierung gemeistert!
