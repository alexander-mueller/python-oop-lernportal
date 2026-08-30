/**
 * 🌐 TS 15: FORTGESCHRITTENES TYPESCRIPT & GENERICS 🌐
 * ====================================================
 * In diesem Modul lernst du Profi-Konzepte:
 * - Generics (<T>) für wiederverwendbare Datencontainer
 * - Custom Type Guards (is Type) für präzise Typ-Eingrenzung
 * - Enums für typisierte Konstanten
 * - Utility Types (Partial<T>, Pick<T, K>, Readonly<T>)
 */

/**
 * 🎯 ENUM: BenutzerRolle
 * Definiert alle gültigen Rollen im System.
 */
const BenutzerRolle = {
  ADMIN: "ADMIN",
  USER: "USER",
  GAST: "GAST"
};

/**
 * @template T
 * @typedef {Object} PaginiertesErgebnis
 * @property {T[]} items - Die Datensätze der aktuellen Seite
 * @property {number} total - Gesamtzahl aller Datensätze
 * @property {number} page - Aktuelle Seitennummer (1-basiert)
 * @property {number} pageSize - Anzahl Elemente pro Seite
 * @property {number} totalPages - Berechnete Gesamtseitenzahl
 * @property {boolean} hasNextPage - Ob eine Folgeseite existiert
 * @property {boolean} hasPrevPage - Ob eine vorherige Seite existiert
 */

/**
 * 🎯 TEILZIEL 1 (TODO 1): erstellePaginiertesErgebnis(items, total, page, pageSize)
 * Generische Hilfsfunktion für paginierte REST-API Antworten (Generic Container <T>).
 * 
 * Anforderungen:
 * - items: T[] (muss ein Array sein, sonst TypeError)
 * - total: number (Zahl >= 0, sonst RangeError)
 * - page: number (Zahl >= 1, Standard: 1, sonst RangeError)
 * - pageSize: number (Zahl >= 1, Standard: 10, sonst RangeError)
 * - totalPages berechnen: Math.max(1, Math.ceil(total / pageSize))
 * - hasNextPage: page < totalPages
 * - hasPrevPage: page > 1
 * - Rückgabe: Das fertige PaginiertesErgebnis-Objekt
 * 
 * @template T
 * @param {T[]} items
 * @param {number} total
 * @param {number} [page=1]
 * @param {number} [pageSize=10]
 * @returns {PaginiertesErgebnis<T>}
 */
function erstellePaginiertesErgebnis(items, total, page = 1, pageSize = 10) {
  // TODO: Parameter validieren, Metadaten berechnen und Objekt zurückgeben
  return null;
}

/**
 * @typedef {Object} AdminBenutzer
 * @property {string | number} id - Eindeutige ID
 * @property {string} username - Benutzername
 * @property {string} email - Gültige E-Mail-Adresse
 * @property {'ADMIN'} rolle - Rolle muss ADMIN sein
 * @property {string[]} berechtigungen - Array mit mindestens einer Berechtigung
 */

/**
 * 🎯 TEILZIEL 2 (TODO 2): istAdminBenutzer(benutzerObjekt)
 * Benutzerdefinierter Type Guard zur Laufzeitprüfung eines Objekts auf Admin-Konformität.
 * 
 * Anforderungen:
 * - Prüft, ob benutzerObjekt ein echtes Objekt ist (nicht null / undefined).
 * - id: Vorhanden (string oder number).
 * - username: string (nach .trim() nicht leer).
 * - email: string (muss "@" enthalten).
 * - rolle: exakt "ADMIN" (oder BenutzerRolle.ADMIN).
 * - berechtigungen: Array mit mindestens 1 Element (length > 0).
 * - Gibt true zurück wenn ALLE Kriterien erfüllt sind, sonst false (wirft KEINEN Fehler).
 * 
 * @param {any} benutzerObjekt
 * @returns {boolean}
 */
function istAdminBenutzer(benutzerObjekt) {
  // TODO: Alle Eigenschaften des Admin-Interfaces auf Gültigkeit prüfen
  return false;
}

/**
 * @typedef {Object} BenutzerProfil
 * @property {number} id
 * @property {string} username
 * @property {string} email
 * @property {Object} einstellungen
 * @property {boolean} einstellungen.darkMode
 * @property {boolean} einstellungen.benachrichtigungen
 * @property {string} [aktualisiertAm]
 */

/**
 * 🎯 TEILZIEL 3 (TODO 3): aktualisiereBenutzerProfil(original, partiellesUpdate)
 * Führt ein partielles Update eines Profils durch (Semantik von TypeScript Partial<T>).
 * 
 * Anforderungen:
 * - original: BenutzerProfil (muss ein gültiges Objekt sein, sonst TypeError)
 * - partiellesUpdate: Partial<BenutzerProfil> (optionale Teilmenge aller Felder)
 * - Validierung: Falls im Update Felder übergeben wurden, müssen die Typen stimmen:
 *     - email (falls vorhanden): muss string sein und "@" enthalten, sonst TypeError.
 *     - username (falls vorhanden): muss string sein und nicht leer, sonst TypeError.
 * - Immutability: Das `original`-Objekt darf NICHT verändert werden!
 * - Verschmilzt `original` mit `partiellesUpdate` (inklusive geschachtelter `einstellungen`).
 * - Setzt das Feld `aktualisiertAm` auf den aktuellen ISO-Datumsstring.
 * - Rückgabe: Das neue, aktualisierte BenutzerProfil-Objekt.
 * 
 * @param {BenutzerProfil} original
 * @param {Partial<BenutzerProfil>} partiellesUpdate
 * @returns {BenutzerProfil}
 */
function aktualisiereBenutzerProfil(original, partiellesUpdate = {}) {
  // TODO: Validierung, Immutable Merge und aktualisiertAm setzen
  return null;
}

/**
 * 🎯 TEILZIEL 4 (TODO 4): filtriereFelder(objekt, erlaubteSchluessel)
 * Erstellt ein neues Objekt mit einer Teilmenge der Eigenschaften (Semantik von Pick<T, K>).
 * 
 * Anforderungen:
 * - objekt: Beliebiges Objekt (falls kein Objekt oder null, leeres Objekt {} zurückgeben)
 * - erlaubteSchluessel: Array von Strings (z.B. ["id", "username"])
 * - Erstellt ein neues Objekt, das NUR die Eigenschaften aus `erlaubteSchluessel` enthält,
 *   die auch tatsächlich im Ausgangsobjekt existieren.
 * - Nicht vorhandene Schlüssel werden ignoriert (kein undefined als Wert einfügen).
 * - Gibt das neue gefilterte Objekt zurück.
 * 
 * @template T
 * @template {keyof T} K
 * @param {T} objekt
 * @param {K[]} erlaubteSchluessel
 * @returns {Pick<T, K>}
 */
function filtriereFelder(objekt, erlaubteSchluessel) {
  // TODO: Neues Objekt erstellen und nur erlaubte Schlüssel kopieren
  return {};
}
