/**
 * 🌐 JS/TS 07: TYPESCRIPT TYPE SAFETY & INTERFACES (MUSTERLÖSUNG) 🌐
 * ==================================================================
 */

/**
 * @typedef {Object} Kunde
 * @property {string | number} id - Eindeutige Kunden-ID
 * @property {string} name - Vollständiger Name des Kunden
 * @property {boolean} istAktiv - Status des Kunden
 * @property {string} [email] - Optionale E-Mail-Adresse
 * @property {string} erstelltAm - ISO-Datumsstring der Erstellung
 */

/**
 * 🎯 TEILZIEL 1: erstelleKunde(id, name, istAktiv = true, email = null)
 */
function erstelleKunde(id, name, istAktiv = true, email = null) {
  if (id === null || id === undefined || id === "" || (typeof id !== "string" && typeof id !== "number")) {
    throw new TypeError("Ungültige Kunden-ID: string oder number erwartet");
  }

  if (typeof name !== "string" || name.trim().length === 0) {
    throw new TypeError("Ungültiger Kunden-Name: nicht-leerer String erwartet");
  }

  if (typeof istAktiv !== "boolean") {
    istAktiv = Boolean(istAktiv);
  }

  if (email !== null && email !== undefined && (typeof email !== "string" || email.trim() === "")) {
    throw new TypeError("Ungültige E-Mail-Adresse");
  }

  const kunde = {
    id: id,
    name: name.trim(),
    istAktiv: istAktiv,
    erstelltAm: new Date().toISOString()
  };

  if (email && typeof email === "string" && email.trim().length > 0) {
    kunde.email = email.trim();
  }

  return kunde;
}

/**
 * 🎯 TEILZIEL 2: validiereAuftrag(auftragObjekt)
 */
function validiereAuftrag(auftragObjekt) {
  if (!auftragObjekt || typeof auftragObjekt !== "object" || Array.isArray(auftragObjekt)) {
    return { gueltig: false, fehler: ["Auftrag muss ein gültiges Objekt sein"] };
  }

  const fehler = [];

  // ID Validierung
  if (auftragObjekt.id === undefined || auftragObjekt.id === null || auftragObjekt.id === "" ||
      (typeof auftragObjekt.id !== "string" && typeof auftragObjekt.id !== "number")) {
    fehler.push("Ungültige Auftrags-ID");
  }

  // Kunde-ID Validierung
  if (auftragObjekt.kundeId === undefined || auftragObjekt.kundeId === null || auftragObjekt.kundeId === "" ||
      (typeof auftragObjekt.kundeId !== "string" && typeof auftragObjekt.kundeId !== "number")) {
    fehler.push("Ungültige Kunden-ID");
  }

  // Positionen Validierung
  if (!Array.isArray(auftragObjekt.positionen) || auftragObjekt.positionen.length === 0) {
    fehler.push("Mindestens eine Position erforderlich");
  } else {
    auftragObjekt.positionen.forEach((pos, idx) => {
      if (!pos || typeof pos !== "object") {
        fehler.push(`Position ${idx + 1} ist kein gültiges Objekt`);
      } else {
        if (typeof pos.titel !== "string" || pos.titel.trim() === "") {
          fehler.push(`Position ${idx + 1}: Titel fehlt oder ist leer`);
        }
        if (typeof pos.menge !== "number" || isNaN(pos.menge) || pos.menge <= 0) {
          fehler.push(`Position ${idx + 1}: Menge muss > 0 sein`);
        }
        if (typeof pos.einzelpreis !== "number" || isNaN(pos.einzelpreis) || pos.einzelpreis < 0) {
          fehler.push(`Position ${idx + 1}: Einzelpreis muss >= 0 sein`);
        }
      }
    });
  }

  // Summen-Validierung
  if (typeof auftragObjekt.summe !== "number" || isNaN(auftragObjekt.summe) || auftragObjekt.summe < 0) {
    fehler.push("Summe muss eine Zahl >= 0 sein");
  }

  // Status Validierung
  const erlaubteStatus = ["offen", "in_bearbeitung", "abgeschlossen", "storniert"];
  if (!erlaubteStatus.includes(auftragObjekt.status)) {
    fehler.push("Status ungültig (erlaubt: offen, in_bearbeitung, abgeschlossen, storniert)");
  }

  return {
    gueltig: fehler.length === 0,
    fehler: fehler
  };
}

/**
 * 🎯 TEILZIEL 3: filtereNachStatus(eintraege, zielStatus)
 */
function filtereNachStatus(eintraege, zielStatus) {
  if (!Array.isArray(eintraege)) {
    return [];
  }
  return eintraege.filter(item => item && typeof item === "object" && item.status === zielStatus);
}

/**
 * 🎯 TEILZIEL 4: formatierePreisangabe(betrag, waehrung = "EUR")
 */
function formatierePreisangabe(betrag, waehrung = "EUR") {
  if (typeof betrag !== "number" || isNaN(betrag)) {
    throw new TypeError("Ungültiger Betrag: Zahl erwartet");
  }
  if (typeof waehrung !== "string" || waehrung.trim().length === 0) {
    throw new TypeError("Ungültige Währung: nicht-leerer String erwartet");
  }

  const formatierteZahl = betrag.toFixed(2).replace(".", ",");
  return `${formatierteZahl} ${waehrung.trim().toUpperCase()}`;
}
