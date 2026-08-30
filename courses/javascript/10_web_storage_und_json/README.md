# JS 10: Web Storage & JSON-Serialisierung 💾

Willkommen zu **Modul 10** des JavaScript-Kurses!

In modernen Web-Anwendungen müssen Einstellungen, Warenkörbe, Spielstände oder Formulardaten clientseitig im Browser gespeichert werden – auch wenn der Benutzer die Seite neu lädt oder den Browser schließt.

Die **Web Storage API** (`localStorage` und `sessionStorage`) in Kombination mit **JSON-Serialisierung** (`JSON.stringify` & `JSON.parse`) bildet das Fundament für clientseitige Datenpersistenz.

---

## 💡 1. Das Wichtigste in Kürze

### A. localStorage vs. sessionStorage
Der Browser stellt zwei getrennte Key-Value-Speicher zur Verfügung:

| Eigenschaft | `localStorage` | `sessionStorage` |
| :--- | :--- | :--- |
| **Lebensdauer** | Dauerhaft (bleibt nach Browser-Neustart erhalten) | Bis der Browser-Tab geschlossen wird |
| **Gültigkeitsbereich** | Same-Origin (gleiches Protokoll, Domain, Port) | Nur im aktuellen Browser-Tab / Fenster |
| **Speicherkapazität** | Typisch ca. 5 – 10 MB pro Origin | Typisch ca. 5 MB pro Tab |
| **Typischer Nutzen** | Theme-Wahl, Highscores, Offline-Caches | Schrittweises Formular, temporärer Session-State |

---

### B. Die Standard-Methoden der Storage API
Beide Speicher bieten dieselbe intuitive Schnittstelle:

```javascript
// 1. Wert speichern (Key und Value sind immer Strings!):
localStorage.setItem("benutzerName", "Ada Lovelace");

// 2. Wert abrufen (liefert null, wenn der Key nicht existiert):
const name = localStorage.getItem("benutzerName"); // "Ada Lovelace"
const fehlt = localStorage.getItem("unbekannt");    // null

// 3. Einzelnen Eintrag löschen:
localStorage.removeItem("benutzerName");

// 4. Gesamten Speicher der Domain leeren:
localStorage.clear();
```

---

### C. Komplexe Datentypen speichern mit JSON
Da die Web Storage API **ausschließlich Strings** speichert, führen Objekte und Arrays ohne Serialisierung zu dem gefürchteten `"[object Object]"`-Fehler!

```javascript
const spieler = { name: "Mario", punkte: 1200, items: ["Pilz", "Stern"] };

// ❌ FALSCH: Speichert nur den String "[object Object]"
localStorage.setItem("player", spieler);

// ✅ RICHTIG: In JSON-String serialisieren
const jsonString = JSON.stringify(spieler);
localStorage.setItem("player", jsonString);

// 📥 Beim Laden: Von JSON zurück in ein JavaScript-Objekt parsen
const geladenerString = localStorage.getItem("player");
if (geladenerString) {
  const parsedPlayer = JSON.parse(geladenerString);
  console.log(parsedPlayer.punkte); // 1200
}
```

---

### D. Robuste Fehlerbehandlung (Defektes JSON & Quota Exceeded)
In Produktionscode können zwei Fehler auftreten:
1. **Defektes JSON im Storage:** Ein anderer Scriptteil oder eine Drittanbieter-Erweiterung hat ungültigen Text hinterlegt.
2. **QuotaExceededError:** Der Speicherplatz (5 MB) ist voll.

```javascript
function sicheresLaden(key, fallback) {
  try {
    const raw = localStorage.getItem(key);
    return raw !== null ? JSON.parse(raw) : fallback;
  } catch (err) {
    console.warn(`Warnung: JSON für ${key} beschädigt, nutze Fallback:`, err);
    return fallback;
  }
}
```

---

## 🔐 Die didaktische Analogie: "Das Schließfach & das Reisetagebuch"

- **`localStorage` ist das Bankschließfach:**  
  Du legst deinen Reisepass (Benutzerprofil) oder deine Trophäen (Highscore) hinein. Selbst wenn du nach einem Jahr wiederkommst (Browser-Neustart), liegt alles genau so im Schließfach wie du es hinterlassen hast.
- **`sessionStorage` ist das Reisetagebuch der aktuellen Tour:**  
  Du schreibst deine Tagesnotizen hinein, solange du im Zug sitzt (aktueller Tab). Sobald du aussteigst und nach Hause gehst (Tab schließen), beginnt die nächste Reise mit einem frischen, leeren Notizblock.
- **`JSON.stringify` & `JSON.parse` sind Vakuumierer & Entpacker:**  
  Du kannst keinen dreidimensionalen Koffer (JavaScript-Objekt mit Methoden & Referenzen) durch den flachen Schließfachschlitz schieben. Du packst ihn flach zusammen (`stringify`), schiebst den Umschlag hinein und packst ihn beim Herausholen wieder vollständig aus (`parse`).

---

## 🎯 Aufgaben & Teilziele in `aufgabe.js`

1. **TODO 1:** `speichereDaten(schluessel, daten, storageMock)`  
   Validiere den Schlüssel, serialisiere beliebige Werte mit `JSON.stringify` und fange Speicherfehler ab.
2. **TODO 2:** `ladeDaten(schluessel, standardWert = null, storageMock)`  
   Lade Daten mit `getItem`, behandle fehlende Einträge sowie `SyntaxError` bei defektem JSON mit `try/catch` und liefere den `standardWert` zurück.
3. **TODO 3:** `loescheDaten(schluessel, storageMock)`  
   Entferne den Schlüssel sauber aus dem Storage mit `removeItem`.
4. **TODO 4:** `aktualisiereHighscore(spielerName, punkte, storageMock)`  
   Verwalte eine Bestenliste unter dem Key `"highscores"`. Füge den neuen Spieler ein, sortiere absteigend nach Punkten, kürze auf die Top 10 und speichere die Liste persistent ab.

---

## 🧪 Tests ausführen

Öffne die Web-IDE oder führe die Unittests aus. Sobald alle 16 Tests grün sind, hast du clientseitige Persistenz und JSON-Verarbeitung gemeistert!
