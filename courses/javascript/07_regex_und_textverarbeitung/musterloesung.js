/**
 * 🌟 MUSTERLÖSUNG: JS 07 – REGEX & TEXTVERARBEITUNG 🌟
 * ====================================================
 */

function istGueltigeEmail(email) {
  if (!email || typeof email !== "string") return false;
  const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
  return emailRegex.test(email);
}

function findeTelefonnummern(text) {
  if (!text || typeof text !== "string") return [];
  const telefonRegex = /(?:\+49|\+?\d{1,3}|0)[\d\s\/\-\(\)]{6,}\d/g;
  const matches = text.match(telefonRegex);
  return matches ? matches.map((m) => m.trim()) : [];
}

function extrahiereHashtags(text) {
  if (!text || typeof text !== "string") return [];
  const hashtagRegex = /#[a-zA-Z0-9_äöüÄÖÜß]+/g;
  const matches = text.match(hashtagRegex);
  return matches || [];
}

function maskiereKreditkarte(text) {
  if (!text || typeof text !== "string") return "";
  const ccRegex = /\b\d{4}[ -]?\d{4}[ -]?\d{4}[ -]?(\d{4})\b/g;
  return text.replace(ccRegex, "****-****-****-$1");
}

function istStarkesPasswort(passwort) {
  if (!passwort || typeof passwort !== "string" || passwort.length < 8) {
    return false;
  }
  const hatKlein = /[a-z]/.test(passwort);
  const hatGross = /[A-Z]/.test(passwort);
  const hatZahl = /\d/.test(passwort);
  const hatSonderzeichen = /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?~`§]/.test(passwort);

  return hatKlein && hatGross && hatZahl && hatSonderzeichen;
}
