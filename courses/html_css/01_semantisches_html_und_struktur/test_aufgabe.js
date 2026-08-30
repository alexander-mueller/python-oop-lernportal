// 🧪 Testsuite: HTML 01 - Semantik & Dokumentenstruktur

// TEST: Teilziel 1 - Dokumenten-Kopf & Metadaten
assert.ok(userCode.includes("<!DOCTYPE html>") || userCode.includes("<!doctype html>"), "Dokument muss mit <!DOCTYPE html> beginnen.");
assert.strictEqual(doc.documentElement.getAttribute("lang"), "de", "Das <html>-Tag muss das Attribut lang=\"de\" besitzen.");
const metaCharset = doc.querySelector('meta[charset="UTF-8"], meta[charset="utf-8"]');
assert.ok(metaCharset, "Im <head> muss ein <meta charset=\"UTF-8\"> vorhanden sein.");
const metaViewport = doc.querySelector('meta[name="viewport"]');
assert.ok(metaViewport && metaViewport.getAttribute("content").includes("width=device-width"), "Ein valider <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"> ist erforderlich.");
assert.ok(doc.title && doc.title.trim().length > 0, "Das Dokument muss einen nicht-leeren <title> im <head> haben.");

// TEST: Teilziel 2 - Header & Navigation
const header = doc.querySelector("header");
assert.ok(header, "Ein <header>-Element muss im Dokument vorhanden sein.");
const h1 = doc.querySelector("header h1") || doc.querySelector("h1");
assert.ok(h1 && h1.textContent.trim().length > 0, "Im Header muss eine <h1>-Hauptüberschrift definiert sein.");
const nav = doc.querySelector("nav");
assert.ok(nav, "Ein semantisches <nav>-Element muss existieren.");
const navLinks = nav.querySelectorAll("ul li a, ol li a, a");
assert.ok(navLinks.length >= 3, "Die Navigation muss mindestens 3 Links (<a>) enthalten.");

// TEST: Teilziel 3 - Main & Article
const mains = doc.querySelectorAll("main");
assert.strictEqual(mains.length, 1, "Es darf genau ein einziges <main>-Element auf der Seite existieren.");
const main = mains[0];
const article = doc.querySelector("main article") || doc.querySelector("article");
assert.ok(article, "Es muss ein semantischer <article> vorhanden sein.");
const h2 = article.querySelector("h2");
assert.ok(h2 && h2.textContent.trim().length > 0, "Der <article> muss eine <h2>-Überschrift enthalten.");
const articleP = article.querySelector("p");
assert.ok(articleP && articleP.textContent.trim().length > 0, "Der <article> muss mindestens einen Fließtext-Absatz (<p>) enthalten.");

// TEST: Teilziel 4 - Section & Aside
const section = doc.querySelector("section");
assert.ok(section, "Eine <section> für thematische Abschnitte muss vorhanden sein.");
const h3 = section.querySelector("h3") || doc.querySelector("h3");
assert.ok(h3 && h3.textContent.trim().length > 0, "Die <section> sollte eine <h3>-Überschrift enthalten.");
const aside = doc.querySelector("aside");
assert.ok(aside, "Ein semantisches <aside>-Element für Randinformationen/Sidebar muss existieren.");

// TEST: Teilziel 5 - Footer & Copyright
const footer = doc.querySelector("footer");
assert.ok(footer, "Ein <footer>-Element am Dokumentenende muss existieren.");
assert.ok(footer.textContent.includes("©") || userCode.includes("&copy;") || footer.textContent.toLowerCase().includes("copyright") || footer.textContent.toLowerCase().includes("alle rechte"), "Der Footer muss einen Copyright-Vermerk (&copy;) enthalten.");
