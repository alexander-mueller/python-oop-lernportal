/**
 * 🌐 JS 07: REGULÄRE AUSDRÜCKE & TEXTVERARBEITUNG 🌐
 * ==================================================
 * RegExp-Muster, Flags, Metazeichen, Quantifizierer
 * und praktische Methoden (test, match, replace).
 */

// 🎯 TEILZIEL 1 (TODO 1): istGueltigeEmail(email)
// Prüfe, ob der gegebene String eine syntaktisch gültige E-Mail-Adresse ist.
// Kriterien:
// - Startet mit mind. 1 Zeichen (Buchstaben, Ziffern, ., _, %, +, -)
// - Enthält genau ein '@'
// - Domain-Teil mit mind. 1 Zeichen (Buchstaben, Ziffern, ., -)
// - Top-Level-Domain (TLD) mit mind. 2 Buchstaben am Ende (z. B. .de, .com, .info)
// Rückgabe: true wenn gültig, sonst false.
function istGueltigeEmail(email) {
  // TODO: Regex-Muster definieren und mit .test() prüfen
  return false;
}

// 🎯 TEILZIEL 2 (TODO 2): findeTelefonnummern(text)
// Finde alle Telefonnummern in einem beliebigen Fließtext.
// Unterstütze Formate wie "+49 170 1234567", "0171-1234567", "030 / 123456" oder "+49(0)30 123456".
// Rückgabe: Ein Array mit allen gefundenen Telefonnummern-Strings (oder [] wenn keine gefunden).
function findeTelefonnummern(text) {
  // TODO: Regex mit Global-Flag 'g' erstellen und text.match(regex) nutzen
  return [];
}

// 🎯 TEILZIEL 3 (TODO 3): extrahiereHashtags(text)
// Extrahiere alle Social-Media-Hashtags aus einem Text (z. B. "#javascript", "#webdev2024").
// Ein Hashtag beginnt mit '#' gefolgt von einem oder mehreren Wortzeichen (Buchstaben, Zahlen, Unterstrich).
// Rückgabe: Array aller Hashtag-Strings inklusive Raute '#' (oder [] wenn keine vorhanden).
function extrahiereHashtags(text) {
  // TODO: Hashtags mit Regex matchen und als Array zurückgeben
  return [];
}

// 🎯 TEILZIEL 4 (TODO 4): maskiereKreditkarte(text)
// Maskiere 16-stellige Kreditkartennummern aus Sicherheitsgründen im Text.
// Die Nummern können mit Bindestrichen ("1234-5678-9012-3456"), Leerzeichen ("1234 5678 9012 3456")
// oder durchgehend ("1234567890123456") geschrieben sein.
// Ersetze jede 16-stellige Kreditkarte durch das Format: "****-****-****-XXXX" (wobei XXXX die letzten 4 Ziffern sind).
// Rückgabe: Der bereinigte/maskierte Text-String.
function maskiereKreditkarte(text) {
  // TODO: Mit regex.replace() und Capturing Group $1 für die letzten 4 Ziffern maskieren
  return "";
}

// 🎯 TEILZIEL 5 (TODO 5): istStarkesPasswort(passwort)
// Validiere, ob ein Passwort den modernen Sicherheitsanforderungen entspricht:
// 1. Mindestens 8 Zeichen lang
// 2. Mindestens ein Kleinbuchstabe (a-z)
// 3. Mindestens ein Großbuchstabe (A-Z)
// 4. Mindestens eine Zahl (0-9)
// 5. Mindestens ein Sonderzeichen (z. B. ! @ # $ % ^ & * ( ) _ + - = [ ] { } ; ' : " \ | , . < > / ? ~)
// Rückgabe: true wenn stark, sonst false.
function istStarkesPasswort(passwort) {
  // TODO: Bedingungen mit Regex prüfen
  return false;
}
