# 🌐 JS 08: Fehlerbehandlung & Debugging

Willkommen zu **Modul 08** des JavaScript-Kurses! In diesem Modul lernst du defensive Programmiertechniken, strukturierte Ausnahmebehandlung mit `try...catch...finally` und den Aufbau professioneller Fehlerklassen-Hierarchien.

---

## 🎯 Lernziele

Nach diesem Modul kannst du:
1. Das **`try...catch...finally`** Kontrollmuster verstehen und für fehlertolerante Anwendungen einsetzen.
2. Gezielte Fehler mit **`throw new Error(...)`** auslösen.
3. Eigene Fehlerklassen von **`Error`** ableiten (`class ValidierungsFehler extends Error`).
4. Fehlerklassen hierarchisch strukturieren und mit **Zusatzattributen** (wie betroffenes Formularfeld oder Saldo) ausstatten.
5. Im `catch`-Block unterschiedliche Fehlerursachen mittels **`instanceof`** unterscheiden und behandeln.

---

## 💡 Theoretische Grundlagen

### 1. Das `try...catch...finally` Muster

```javascript
try {
  // Kritischer Code:
  const daten = JSON.parse(roheEingabe);
  verarbeite(daten);
} catch (error) {
  // Behandlung:
  console.error("Fehler abgefangen:", error.message);
} finally {
  // Läuft garantiert IMMER:
  cleanup();
}
```

### 2. Eigene Fehlerklassen definieren

Standard-Fehler (`new Error(...)`) enthalten oft nicht genügend Kontext für granulare UI-Reaktionen. Durch das Ableiten eigener Klassen schaffen wir Klarheit:

```javascript
// Basis für alle Fehler dieser Domäne:
class AnwendungsFehler extends Error {
  constructor(message) {
    super(message);
    this.name = "AnwendungsFehler";
  }
}

// Spezifischer Validierungsfehler mit Feldbezug:
class ValidierungsFehler extends AnwendungsFehler {
  constructor(message, feld = null) {
    super(message);
    this.name = "ValidierungsFehler";
    this.feld = feld;
  }
}
```

### 3. Fehler differenzieren mit `instanceof`

```javascript
try {
  fuehreOperationAus();
} catch (err) {
  if (err instanceof ValidierungsFehler) {
    console.warn(`Ungültige Eingabe im Feld ${err.feld}: ${err.message}`);
  } else if (err instanceof GuthabenFehler) {
    console.warn(`Guthaben (${err.saldo} €) reicht nicht für ${err.betrag} € aus.`);
  } else {
    // Unbekannter Fehler -> Neu werfen
    throw err;
  }
}
```

---

## 🪂 Didaktische Analogie: Die Notbremse & der Auffang-Fallschirm

- **`throw`**: Das Ziehen der Notbremse im Zug &ndash; der normale Ablauf wird sofort unterbrochen.
- **`catch`**: Der Fallschirm, der die Passagiere vor dem Absturz bewahrt und einen sicheren Ausstieg ermöglicht.
- **`finally`**: Der Flughafen-Boden, der am Ende des Flugs immer erreicht wird, egal wie turbulent die Reise war.

---

## 🎯 Aufgabenübersicht in `aufgabe.js`

1. **TODO 1: Error-Klassenhierarchie**:
   - `AnwendungsFehler extends Error`
   - `ValidierungsFehler extends AnwendungsFehler` (mit `feld`)
   - `GuthabenFehler extends AnwendungsFehler` (mit `saldo`, `betrag`)
2. **TODO 2: `sichereDivision(a, b)`**:
   - Prüft Zahlen und fängt Division durch 0 mit `AnwendungsFehler` ab.
3. **TODO 3: `parseBenutzerJson(jsonString)`**:
   - Fängt JSON-Syntaxfehler ab und validiert das Feld `name`.
4. **TODO 4: `pruefeTransaktion(kontoSaldo, abhebeBetrag)`**:
   - Prüft positive Beträge und ausreichendes Guthaben mit `GuthabenFehler`.

---

## 🧪 Tests ausführen

Führe die Testsuite in der Web-IDE oder lokal aus:
```bash
# In der Web-IDE: Klicke auf 'Code ausführen & testen'
```
