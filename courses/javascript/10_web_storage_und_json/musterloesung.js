/**
 * 🌟 MUSTERLÖSUNG: JS 10 – WEB STORAGE & JSON SERIALISIERUNG 🌟
 * =============================================================
 */

function ermittleStorage(storageMock = null) {
  if (storageMock) return storageMock;
  if (typeof localStorage !== "undefined") return localStorage;
  return null;
}

function speichereDaten(schluessel, daten, storageMock = null) {
  if (typeof schluessel !== "string" || schluessel.trim().length === 0) {
    throw new TypeError("Schlüssel muss ein nicht-leerer String sein");
  }
  const storage = ermittleStorage(storageMock);
  if (!storage) return false;

  try {
    const jsonString = JSON.stringify(daten);
    storage.setItem(schluessel, jsonString);
    return true;
  } catch (error) {
    return false;
  }
}

function ladeDaten(schluessel, standardWert = null, storageMock = null) {
  if (typeof schluessel !== "string") {
    return standardWert;
  }
  const storage = ermittleStorage(storageMock);
  if (!storage) return standardWert;

  try {
    const raw = storage.getItem(schluessel);
    if (raw === null || raw === undefined) {
      return standardWert;
    }
    return JSON.parse(raw);
  } catch (error) {
    return standardWert;
  }
}

function loescheDaten(schluessel, storageMock = null) {
  if (typeof schluessel !== "string" || schluessel.trim().length === 0) {
    return false;
  }
  const storage = ermittleStorage(storageMock);
  if (!storage) return false;

  try {
    storage.removeItem(schluessel);
    return true;
  } catch (error) {
    return false;
  }
}

function aktualisiereHighscore(spielerName, punkte, storageMock = null) {
  if (typeof spielerName !== "string" || spielerName.trim().length === 0) {
    throw new TypeError("Spielername muss ein nicht-leerer String sein");
  }
  if (typeof punkte !== "number" || isNaN(punkte) || punkte < 0) {
    throw new TypeError("Punkte müssen eine gültige Zahl >= 0 sein");
  }

  const bestehendeHighscores = ladeDaten("highscores", [], storageMock);
  const liste = Array.isArray(bestehendeHighscores) ? [...bestehendeHighscores] : [];

  const neuerEintrag = {
    name: spielerName.trim(),
    punkte: punkte,
    datum: new Date().toISOString()
  };

  liste.push(neuerEintrag);
  liste.sort((a, b) => b.punkte - a.punkte);

  const top10 = liste.slice(0, 10);
  speichereDaten("highscores", top10, storageMock);

  return top10;
}
