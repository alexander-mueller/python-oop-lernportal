/**
 * 🌟 MUSTERLÖSUNG: TS 15 – FORTGESCHRITTENES TYPESCRIPT & GENERICS 🌟
 * ===================================================================
 */

const BenutzerRolle = {
  ADMIN: "ADMIN",
  USER: "USER",
  GAST: "GAST"
};

function erstellePaginiertesErgebnis(items, total, page = 1, pageSize = 10) {
  if (!Array.isArray(items)) {
    throw new TypeError("Items müssen als Array übergeben werden");
  }
  if (typeof total !== "number" || isNaN(total) || total < 0) {
    throw new RangeError("Total muss eine Zahl >= 0 sein");
  }
  if (typeof page !== "number" || isNaN(page) || page < 1) {
    throw new RangeError("Page muss eine Zahl >= 1 sein");
  }
  if (typeof pageSize !== "number" || isNaN(pageSize) || pageSize < 1) {
    throw new RangeError("PageSize muss eine Zahl >= 1 sein");
  }

  const totalPages = total === 0 ? 1 : Math.ceil(total / pageSize);
  const hasNextPage = page < totalPages;
  const hasPrevPage = page > 1;

  return {
    items: [...items],
    total,
    page,
    pageSize,
    totalPages,
    hasNextPage,
    hasPrevPage
  };
}

function istAdminBenutzer(benutzerObjekt) {
  if (!benutzerObjekt || typeof benutzerObjekt !== "object" || Array.isArray(benutzerObjekt)) {
    return false;
  }

  // 1. ID prüfen
  const hasId = (typeof benutzerObjekt.id === "string" && benutzerObjekt.id.trim().length > 0) ||
                (typeof benutzerObjekt.id === "number" && !isNaN(benutzerObjekt.id));
  if (!hasId) return false;

  // 2. Username prüfen
  if (typeof benutzerObjekt.username !== "string" || benutzerObjekt.username.trim().length === 0) {
    return false;
  }

  // 3. Email prüfen
  if (typeof benutzerObjekt.email !== "string" || !benutzerObjekt.email.includes("@")) {
    return false;
  }

  // 4. Rolle prüfen (muss ADMIN sein)
  const istRolleAdmin = benutzerObjekt.rolle === "ADMIN" ||
                        benutzerObjekt.role === "ADMIN" ||
                        benutzerObjekt.rolle === BenutzerRolle.ADMIN;
  if (!istRolleAdmin) return false;

  // 5. Berechtigungen prüfen (Array mit length > 0)
  if (!Array.isArray(benutzerObjekt.berechtigungen) || benutzerObjekt.berechtigungen.length === 0) {
    return false;
  }

  return true;
}

function aktualisiereBenutzerProfil(original, partiellesUpdate = {}) {
  if (!original || typeof original !== "object" || Array.isArray(original)) {
    throw new TypeError("Original muss ein gültiges Benutzer-Objekt sein");
  }

  const update = (partiellesUpdate && typeof partiellesUpdate === "object" && !Array.isArray(partiellesUpdate))
    ? partiellesUpdate
    : {};

  // Validierung der Update-Felder falls übergeben
  if (update.username !== undefined) {
    if (typeof update.username !== "string" || update.username.trim().length === 0) {
      throw new TypeError("Username muss ein nicht-leerer String sein");
    }
  }
  if (update.email !== undefined) {
    if (typeof update.email !== "string" || !update.email.includes("@")) {
      throw new TypeError("E-Mail muss ein gültiger E-Mail-String mit '@' sein");
    }
  }

  const bestehendeEinstellungen = (original.einstellungen && typeof original.einstellungen === "object")
    ? original.einstellungen
    : {};

  const neueEinstellungen = (update.einstellungen && typeof update.einstellungen === "object")
    ? update.einstellungen
    : {};

  return {
    ...original,
    ...update,
    username: update.username !== undefined ? update.username.trim() : original.username,
    einstellungen: {
      ...bestehendeEinstellungen,
      ...neueEinstellungen
    },
    aktualisiertAm: new Date().toISOString()
  };
}

function filtriereFelder(objekt, erlaubteSchluessel) {
  if (!objekt || typeof objekt !== "object" || !Array.isArray(erlaubteSchluessel)) {
    return {};
  }

  const ergebnis = {};
  for (const schluessel of erlaubteSchluessel) {
    if (typeof schluessel === "string" && Object.prototype.hasOwnProperty.call(objekt, schluessel)) {
      ergebnis[schluessel] = objekt[schluessel];
    }
  }
  return ergebnis;
}
