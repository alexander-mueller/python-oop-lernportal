# 🌐 JS 05: Callbacks, Event Loop & Promises

Willkommen zu **Modul 05** des JavaScript-Kurses! In diesem Kapitel lernst du das Herzstück der modernen Web-Entwicklung kennen: **Asynchrone Programmierung mit Promises**.

---

## 📖 1. Synchron vs. Asynchron & Der Event Loop

JavaScript führt Code in einer einzigen Hauptausführungsschleife aus (**Single-Threaded**). 

- **Synchrone Ausführung (Blockierend):** Jede Codezeile wird nacheinander ausgeführt. Dauert eine Operation lange (z. B. ein schwerer Rechenschritt oder ein synchrones Warten), friert das gesamte Programm (und die Webseite!) ein.
- **Asynchrone Ausführung (Nicht-blockierend):** Zeitintensive Aufgaben (z. B. Netzwerk-Anfragen, Timer oder Dateizugriffe) werden im Hintergrund angestoßen. JavaScript läuft währenddessen sofort weiter. Sobald das Ergebnis vorliegt, wird ein Callback in die Warteschlange gelegt und vom **Event Loop** abgearbeitet.

```javascript
console.log("1. Bestellung aufgeben");

setTimeout(() => {
  console.log("3. Essen ist fertig!"); // Asynchroner Callback nach 1000ms
}, 1000);

console.log("2. An den Tisch setzen und plaudern");
// Ausgabe-Reihenfolge: 1 -> 2 -> 3
```

---

## 🍔 2. Die Restaurant-Pieper-Analogie

Stell dir vor, du bestellst Burger in einem Selbstbedienungs-Restaurant:

1. **Bestellung:** Du gehst an die Kasse und bestellst dein Menü.
2. **Der Pieper (`Promise` im Zustand `pending`):** Die Bedienung gibt dir sofort einen elektronischen Pieper in die Hand. Du musst *nicht* stur am Tresen stehen bleiben und die Schlange blockieren.
3. **Nicht-blockierendes Warten:** Du setzt dich an deinen Tisch, surfst am Smartphone oder unterhältst dich mit Freunden (JavaScript Event Loop verarbeitet andere Ereignisse).
4. **Erfolg (`resolve` -> `fulfilled`):** Der Pieper vibriert und leuchtet grün! Du holst dein frisches Essen ab (`.then(essen => ...)`).
5. **Fehler (`reject` -> `rejected`):** Der Pieper piept rot und die Bedienung ruft: *"Die Burger-Patties sind leider aus!"* (`.catch(fehler => ...)`).

---

## ⏳ 3. Was ist ein Promise?

Ein **Promise** (deutsch: *Versprechen*) ist ein Objekt, das einen Wert repräsentiert, der jetzt, in der Zukunft oder nie verfügbar ist.

### Die 3 Zustände eines Promise:
```
                ┌───> fulfilled (erfolgreich gelöst) ──> .then(wert)
  pending ──────┤
 (schwebend)    └───> rejected (fehlgeschlagen)      ──> .catch(fehler)
```

1. **`pending` (schwebend):** Die asynchrone Operation läuft noch. Weder Erfolg noch Fehler.
2. **`fulfilled` (erfüllt):** Die Operation war erfolgreich, `resolve(wert)` wurde aufgerufen.
3. **`rejected` (abgewiesen):** Ein Fehler ist aufgetreten, `reject(error)` wurde aufgerufen.

---

## 🛠️ 4. Eigene Promises erstellen

Ein Promise wird mit dem Konstruktor `new Promise(executor)` erzeugt. Die Executor-Funktion erhält zwei Parameter: `resolve` und `reject`.

```javascript
function simuliereDatenAbruf(erfolgreich) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (erfolgreich) {
        resolve({ id: 1, name: "Max Mustermann" });
      } else {
        reject(new Error("Netzwerk-Timeout beim Laden!"));
      }
    }, 500);
  });
}
```

---

## 🔗 5. Promise-Chaining: `.then()`, `.catch()`, `.finally()`

Promises ermöglichen sauberes Verketten ohne verschachtelte Callback-Pyramiden (*Callback Hell*):

```javascript
simuliereDatenAbruf(true)
  .then((daten) => {
    console.log("Erhaltene Daten:", daten.name);
    return daten.id; // Rückgabewert wird als nächstes Promise weitergegeben
  })
  .then((userId) => {
    console.log("Lade Details für ID:", userId);
  })
  .catch((err) => {
    console.error("Ein Fehler ist aufgetreten:", err.message);
  })
  .finally(() => {
    console.log("Lade-Indikator ausblenden (wird immer ausgeführt)");
  });
```

---

## ⚡ 6. Parallele Ausführung mit `Promise.all()` und `Promise.race()`

### `Promise.all([p1, p2, ...])`
Führt mehrere Promises parallel aus und wartet, bis **alle** erfolgreich aufgelöst wurden.
- Gibt ein Array mit allen Einzelergebnissen `[res1, res2, ...]` zurück.
- **Fail-Fast:** Bricht sofort ab, sobald *auch nur ein einzelnes* Promise rejected!

```javascript
const p1 = fetchUser();
const p2 = fetchPosts();

Promise.all([p1, p2])
  .then(([user, posts]) => {
    console.log("User & Posts gleichzeitig geladen:", user, posts);
  })
  .catch(err => console.error("Mindestens eine Quelle schlug fehl:", err));
```

### `Promise.race([p1, p2, ...])`
Liefert das Ergebnis des **allerschnellsten** Promise (egal ob `resolve` oder `reject`). Ideal z. B. für Timeouts.

---

## 🎯 7. Deine Aufgaben in `aufgabe.js`

1. **`verzoegereAusfuehrung(ms, rueckgabeWert)`**:
   Erzeuge ein Promise, das nach `ms` Millisekunden mittels `setTimeout` den `rueckgabeWert` auflöst.
2. **`pruefeZahlGroesserNull(zahl)`**:
   Prüfe die Zahl: Resolve bei `zahl > 0`, Reject mit `new Error("Zahl muss größer als 0 sein")` bei `<= 0`.
3. **`ladeBenutzerProfil(userId)`**:
   Asynchrones Profil-Laden: Resolve mit `{ id: userId, name: "Benutzer_" + userId, status: "aktiv" }` bei `userId > 0`, sonst Reject mit `new Error("Ungültige User-ID")`.
4. **`ladeAlleDatenQuellen(quelleA, quelleB)`**:
   Nutze `Promise.all([quelleA, quelleB])`, um zwei asynchrone Datenströme parallel zu aggregieren.
