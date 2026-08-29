/**
 * 🌐 JS 06: ASYNC / AWAIT & REST-APIS (FETCH) 🌐
 * ===============================================
 * Lerne modernes asynchrones JavaScript mit async/await,
 * robuster try-catch-Fehlerbehandlung und dem Konsumieren von REST-APIs.
 */

// 🎯 TEILZIEL 1 (TODO 1): Schreibe holeWetterDaten(stadtName, mockApiFetcher)
// - Ruft mockApiFetcher(stadtName) mit await auf.
// - Das Response-Objekt enthält { ok: boolean, status: number, json: async () => data }.
// - Wenn response.ok === false ist: wirf einen Fehler (throw new Error(`Stadt ${stadtName} nicht gefunden`)).
// - Wenn response.ok === true ist: parse das JSON mit await response.json()
// - Gib ein formatiertes Objekt zurück:
//   { stadt: data.stadt, temperatur: data.temperatur, wetterlage: data.wetterlage }
async function holeWetterDaten(stadtName, mockApiFetcher) {
  // TODO: Nutze await, prüfe response.ok, parse JSON und gib das formatierte Objekt zurück
  return null;
}

// 🎯 TEILZIEL 2 (TODO 2): Schreibe aggregiereBenutzerPosts(userId, mockPostApiFetcher)
// - Ruft mockPostApiFetcher(userId) mit await auf.
// - Wenn der Fetcher eine Response liefert (response.ok), parse das JSON; wenn direkt ein Array geliefert wird, nutze dieses.
// - Extrahiere alle Posts des Nutzers.
// - Gib ein Aggregat-Objekt zurück mit folgendem Aufbau:
//   {
//     userId: userId,
//     anzahlPosts: posts.length,
//     postTitel: posts.map(p => p.titel)
//   }
async function aggregiereBenutzerPosts(userId, mockPostApiFetcher) {
  // TODO: Asynchron abrufen und aggregieren
  return null;
}

// 🎯 TEILZIEL 3 (TODO 3): Schreibe sichererApiAufruf(apiPromiseOderFn, standardFallback)
// - Führt das übergebene Promise oder die asynchrone Funktion in einem try-Block mit await aus.
// - Wenn die Ausführung erfolgreich ist: gib das Ergebnis zurück.
// - Wenn ein Fehler auftritt (catch): fange den Fehler ab und gib standardFallback zurück.
async function sichererApiAufruf(apiPromiseOderFn, standardFallback) {
  // TODO: try-catch Block für sicheren Aufruf mit Fallback-Wert
  return null;
}
