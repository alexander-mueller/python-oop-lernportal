// 🧪 Testsuite: HTML 02 - Texte, Listen, Bilder & Videos

// TEST: Teilziel 1 - Überschriften & Textformatierung
const h1 = doc.querySelector("h1");
assert.ok(h1 && h1.textContent.trim().length > 0, "Eine <h1>-Hauptüberschrift muss vorhanden sein.");
const h2 = doc.querySelector("h2");
assert.ok(h2 && h2.textContent.trim().length > 0, "Mindestens eine <h2>-Zwischenüberschrift ist erforderlich.");
const h3 = doc.querySelector("h3");
assert.ok(h3 && h3.textContent.trim().length > 0, "Eine <h3>-Unterüberschrift muss existieren.");
const strongTag = doc.querySelector("strong");
assert.ok(strongTag && strongTag.textContent.trim().length > 0, "Mindestens ein <strong>-Tag zur Betonung wichtiger Begriffe ist gefordert.");
const emTag = doc.querySelector("em");
assert.ok(emTag && emTag.textContent.trim().length > 0, "Mindestens ein <em>-Tag für akzentuierte Textstellen ist gefordert.");

// TEST: Teilziel 2 - Ungeordnete Liste (ul)
const ul = doc.querySelector("ul");
assert.ok(ul, "Eine ungeordnete Liste (<ul>) muss vorhanden sein.");
const ulItems = ul ? ul.querySelectorAll("li") : [];
assert.ok(ulItems.length >= 3, "Die ungeordnete Liste (<ul>) muss mindestens 3 <li>-Einträge besitzen.");

// TEST: Teilziel 3 - Geordnete Liste (ol)
const ol = doc.querySelector("ol");
assert.ok(ol, "Eine geordnete Liste (<ol>) muss vorhanden sein.");
const olItems = ol ? ol.querySelectorAll("li") : [];
assert.ok(olItems.length >= 3, "Die geordnete Liste (<ol>) muss mindestens 3 nummerierte <li>-Schritte besitzen.");

// TEST: Teilziel 4 - Bild mit Alternativtext
const img = doc.querySelector("img");
assert.ok(img, "Ein <img>-Element muss eingebunden sein.");
assert.ok(img.hasAttribute("src") && img.getAttribute("src").trim().length > 0, "Das <img>-Tag muss ein gültiges src-Attribut besitzen.");
assert.ok(img.hasAttribute("alt") && img.getAttribute("alt").trim().length > 0, "Das <img>-Tag verlangt zwingend ein nicht-leeres alt-Attribut für Barrierefreiheit.");

// TEST: Teilziel 5 - Video-Player mit Steuerelementen und Source
const video = doc.querySelector("video");
assert.ok(video, "Ein <video>-Element muss existieren.");
assert.ok(video.hasAttribute("controls"), "Das <video>-Tag muss das controls-Attribut für Benutzer-Steuerelemente besitzen.");
const videoSource = video.querySelector("source");
assert.ok(videoSource && videoSource.hasAttribute("src"), "Das <video> muss mindestens ein inneres <source src=\"...\" type=\"...\">-Tag enthalten.");
