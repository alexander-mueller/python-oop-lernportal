# JS 04: DOM-Manipulation & Events 🎭

Willkommen zu **Modul 04** des JavaScript-Kurses!

Das **Document Object Model (DOM)** ist die Schnittstelle zwischen JavaScript und der sichtbaren HTML-Struktur im Webbrowser. Durch die Kombination aus DOM-Selektoren, Manipulation und Event-Listenern hauchst du statischen Webseiten echtes Leben ein und machst sie interaktiv.

---

## 💡 1. Das Wichtigste in Kürze

### A. Was ist das DOM?
Der Browser parst HTML-Code und baut daraus einen hierarchischen Baum aus JavaScript-Objekten (*DOM Tree*):

```
         document
            │
         <html>
        ┌───┴───┐
     <head>   <body>
        │       ┌───┴────────┐
     <title>  <h1>          <div> (Container)
                             ┌───┴───┐
                          <button>  <ul>
                                     │
                                    <li>
```

Jeder HTML-Tag wird zu einem **DOM-Element (Node)** mit Eigenschaften und Methoden, die du in JavaScript zur Laufzeit auslesen und verändern kannst.

---

### B. Elemente selektieren
Moderne Selektoren nutzen dieselbe Syntax wie CSS:

```javascript
// Einzelnes Element selektieren (erstes Vorkommen):
const ueberschrift = document.querySelector("h1");
const speicherBtn = document.querySelector("#save-btn");
const erstesItem = document.querySelector(".liste-item");

// Mehrere Elemente selektieren (NodeList / Collection):
const alleButtons = document.querySelectorAll(".btn");
alleButtons.forEach(btn => console.log(btn.textContent));
```

---

### C. Element-Inhalte & Klassen manipulieren
```javascript
const box = document.querySelector("#info-box");

// 1. Textinhalt sicher ändern (schützt vor XSS-Sicherheitslücken):
box.textContent = "Neuer sicherer Text";

// 2. CSS-Klassen verwalten mit classList:
box.classList.add("aktiv");       // Klasse hinzufügen
box.classList.remove("inaktiv");  // Klasse entfernen
box.classList.toggle("sichtbar"); // Hinzufügen falls fehlt, sonst entfernen
console.log(box.classList.contains("aktiv")); // true oder false
```

---

### D. Event-Listener (Ereignis-Steuerung)
Mit `addEventListener()` reagiert deine Webanwendung auf Benutzerinteraktionen wie Klicks, Tastatureingaben oder Formulare:

```javascript
const button = document.querySelector("#klick-mich");

button.addEventListener("click", (event) => {
  console.log("Button wurde angeklickt!", event.target);
  button.textContent = "Erfolgreich geklickt! 🎉";
});
```

---

### E. Dynamische Elemente erstellen
Du kannst neue HTML-Elemente dynamisch zur Laufzeit erzeugen und in den DOM-Baum einhängen:

```javascript
// 1. Element im Speicher erzeugen:
const neuesLi = document.createElement("li");
neuesLi.textContent = "Neuer dynamischer Eintrag";
neuesLi.classList.add("eintrag");

// 2. In den DOM-Baum an ein Elternelement anfügen:
const liste = document.querySelector("#aufgaben-liste");
liste.appendChild(neuesLi);
```

---

## 🎼 Die didaktische Analogie: "Der Dirigent des Web-Orchesters"

- **Das HTML-Dokument als Partitur:**  
  HTML liefert den statischen Notentext und die Struktur des Musikstücks.
- **Der Browser als Orchester:**  
  Die Musiker (DOM-Nodes) sitzen bereit, um Töne und Farben darzustellen.
- **JavaScript als Dirigent:**  
  - **Selektoren (`querySelector`):** Der Dirigent schaut gezielt zu den Streichern oder Bläsern.
  - **Manipulation (`textContent`, `classList`):** Mit dem Taktstock gibt der Dirigent Anweisungen für Lautstärke, Helligkeit oder Text.
  - **Events (`addEventListener`):** Der Dirigent wartet auf den Einsatz oder den Applaus des Publikums und reagiert dynamisch.

---

## 🏗️ Headless- & Isolierte Logik (Testbare Architektur)

In moderner Web-Entwicklung (wie React, Vue oder Node.js) trennen professionelle Entwickler reine **Berechnungs- und Zustandslogik** von direkten DOM-Zugriffen. 

Dadurch können Funktionen wie `aktualisiereZaehlerAnzeige` oder `filtereElementeNachKlasse` sowohl im echten Browser als auch in **Headless-Umgebungen (z.B. Unittests im Web-Worker / CI-Runner)** blitzschnell und ohne echten Monitor getestet werden!

---

## 🎯 Aufgaben & Teilziele in `aufgabe.js`

Öffne `aufgabe.js` und löse die 4 Aufgaben:

1. **TODO 1:** `erzeugeButtonElement(text, cssKlasse, clickCallback)`  
   Erstelle einen Button (`document.createElement("button")`), setze den Text, füge optional die CSS-Klasse hinzu und binde den Click-Callback per `addEventListener` an.

2. **TODO 2:** `erstelleListenEintrag(titel, istErledigt = false)`  
   Erstelle ein `<li>`-Element mit dem Titel und füge die Klasse `"erledigt"` hinzu, falls `istErledigt === true` ist.

3. **TODO 3:** `filtereElementeNachKlasse(elementListe, cssKlasse)`  
   Filtere ein Array von DOM-Elementen nach `element.classList.contains(cssKlasse)`.

4. **TODO 4:** `aktualisiereZaehlerAnzeige(aktuellerWert, schwellenwert = 10)`  
   Berechne das Zustands-Objekt für eine Zähler-Komponente:
   ```javascript
   {
     text: `Zähler: ${aktuellerWert} / ${schwellenwert}`,
     wert: aktuellerWert,
     istKritisch: aktuellerWert >= schwellenwert,
     statusKlasse: aktuellerWert >= schwellenwert ? "status-kritisch" : "status-normal"
   }
   ```

---

## 🧪 Tests ausführen

Starte die Tests im Test-Runner oder in der Web-IDE. Sobald alle Tests grün sind, hast du DOM-Manipulation & Events gemeistert!
