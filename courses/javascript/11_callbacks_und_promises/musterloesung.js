/**
 * 🌐 JS 05: MUSTERLÖSUNG – CALLBACKS & PROMISES 🌐
 * ===============================================
 */

function verzoegereAusfuehrung(ms, rueckgabeWert) {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve(rueckgabeWert);
    }, ms);
  });
}

function pruefeZahlGroesserNull(zahl) {
  return new Promise((resolve, reject) => {
    if (typeof zahl === "number" && zahl > 0) {
      resolve(zahl);
    } else {
      reject(new Error("Zahl muss größer als 0 sein"));
    }
  });
}

function ladeBenutzerProfil(userId) {
  return new Promise((resolve, reject) => {
    if (typeof userId === "number" && userId > 0) {
      setTimeout(() => {
        resolve({
          id: userId,
          name: `Benutzer_${userId}`,
          status: "aktiv"
        });
      }, 10);
    } else {
      reject(new Error("Ungültige User-ID"));
    }
  });
}

function ladeAlleDatenQuellen(quelleA, quelleB) {
  return Promise.all([quelleA, quelleB]);
}
