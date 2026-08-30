# 🌐 JS 06: Async/Await & REST APIs (Fetch)

Willkommen zu **Modul 06** des JavaScript-Kurses! Hier lernst du die modernste und eleganteste Art kennen, um mit asynchronen Daten und Web-APIs in JavaScript zu arbeiten: **`async` und `await`**.

---

## 📖 1. Was ist `async` / `await`?

Mit ECMAScript 2017 (ES8) wurde `async/await` eingeführt. Es ist sogenannte *syntaktische Versüßung* (Syntactic Sugar) über JavaScript Promises:
- Asynchroner Code sieht plötzlich aus und verhält sich wie **linearer, synchroner Code**.
- Keine unübersichtlichen `.then()`-Ketten mehr.
- Fehler werden mit gewohntem `try { ... } catch (err) { ... }` abgefangen.

---

## 📚 2. Die Buch-Lese-Analogie

Stell dir vor, wie du ein Buch liest:

- **Mit Callbacks & Chaining (`.then()`):** Es ist wie ein Buch, bei dem jedes Kapitel auf Seite 80 verweist (*„Wenn du wissen willst, wie es weitergeht, lies Fußnote 4 auf Seite 80 und springe dann zu Kapitel 7“*). Du springst ständig hin und her.
- **Mit `async/await`:** Du liest die Geschichte ganz natürlich **Zeile für Zeile von oben nach unten**. Wenn an einer Stelle ein Briefbote eintrifft (asynchrones Laden via `await`), pausiert der Erzähler kurz, nimmt den Brief entgegen und liest nahtlos im Text weiter.

---

## ⚙️ 3. Die `async`-Funktion

Wird das Schlüsselwort `async` vor eine Funktion gesetzt:
1. Gibt die Funktion **immer** ein `Promise` zurück.
2. Jeder `return`-Wert wird automatisch in ein aufgelöstes Promise (`Promise.resolve(...)`) eingepackt.
3. Jeder nicht abgefangene Fehler (`throw new Error(...)`) wird zu einem abgewiesenen Promise (`Promise.reject(...)`).

```javascript
async function holeBegruessung(name) {
  return `Hallo ${name}!`; // Gibt Promise { <fulfilled>: "Hallo Anna!" } zurück
}

holeBegruessung("Anna").then(text => console.log(text));
```

---

## ⏳ 4. Der `await`-Operator

`await` kann nur innerhalb von `async`-Funktionen verwendet werden. Es pausiert die Ausführung der aktuellen Funktion, bis das Promise aufgelöst oder abgewiesen wurde:

```javascript
async function ladeBenutzer() {
  console.log("Starte Abruf...");
  
  // Pausiert die Funktion 'ladeBenutzer', aber blockiert NICHT den Browser-Thread!
  const benutzer = await apiCall("/user/1");
  
  console.log("Fertig:", benutzer.name);
  return benutzer;
}
```

---

## ⚖️ 5. Direktvergleich: Promises vs. Async/Await

### Vorher: Promise-Chaining (`.then()`)
```javascript
function holeDatenMitThen() {
  return fetch("https://api.beispiel.de/daten")
    .then(response => {
      if (!response.ok) throw new Error("Netzwerkfehler");
      return response.json();
    })
    .then(daten => {
      console.log("Ergebnis:", daten);
      return daten;
    })
    .catch(err => {
      console.error("Fehler:", err.message);
    });
}
```

### Jetzt: Modernes `async/await`
```javascript
async function holeDatenMitAsync() {
  try {
    const response = await fetch("https://api.beispiel.de/daten");
    if (!response.ok) throw new Error(`HTTP-Fehler: ${response.status}`);
    
    const daten = await response.json();
    console.log("Ergebnis:", daten);
    return daten;
  } catch (err) {
    console.error("Fehler:", err.message);
  }
}
```

---

## 🌐 6. REST-APIs abfragen mit `fetch()`

Beim Abfragen einer REST-API mit `fetch()` laufen in der Praxis zwei asynchrone Schritte ab:

1. **HTTP-Verbindung aufbauen & Statuscode prüfen:**
   ```javascript
   const response = await fetch(url);
   if (!response.ok) {
     // response.status enthält den HTTP-Code (z. B. 404 Not Found oder 500 Server Error)
     throw new Error(`Fehler: ${response.status}`);
   }
   ```
2. **JSON-Body asynchron parsen:**
   ```javascript
   const jsonData = await response.json();
   ```

---

## 🛡️ 7. Robuste Fehlerbehandlung mit `try ... catch`

Mit `try ... catch` können sowohl synchrone JavaScript-Laufzeitfehler als auch asynchrone Promise-Rejections an zentraler Stelle abgefangen werden:

```javascript
async function sichereAktion() {
  try {
    const erg = await riskanteOperation();
    return erg;
  } catch (err) {
    console.warn("Operation fehlgeschlagen, verwende Fallback:", err.message);
    return { status: "fallback_aktiv" };
  }
}
```

---

## 🎯 8. Deine Aufgaben in `aufgabe.js`

1. **`holeWetterDaten(stadtName, mockApiFetcher)`**:
   Rufe `await mockApiFetcher(stadtName)` auf. Prüfe `response.ok`. Wenn `false`, wirf einen Fehler. Wenn `true`, parse JSON (`await response.json()`) und gib `{ stadt, temperatur, wetterlage }` zurück.
2. **`aggregiereBenutzerPosts(userId, mockPostApiFetcher)`**:
   Rufe `await mockPostApiFetcher(userId)` auf. Aggregiere die Posts zu `{ userId, anzahlPosts, postTitel }`.
3. **`sichererApiAufruf(apiPromiseOderFn, standardFallback)`**:
   Führe ein Promise oder eine async Funktion im `try`-Block aus. Fange Fehler im `catch`-Block ab und gib `standardFallback` zurück.
