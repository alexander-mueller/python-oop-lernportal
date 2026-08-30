// 🧪 Testsuite: CSS 05 - Selektoren, Kaskade & Spezifität

const styleTag = doc.querySelector("style");
assert.ok(styleTag && styleTag.textContent.trim().length > 0, "Ein <style>-Tag mit CSS-Regeln muss im <head> definiert sein.");
const cssText = styleTag.textContent;

// TEST: Teilziel 1 - Typ-Selektoren (body & h1)
assert.match(cssText, /body\s*\{[^}]*(?:background|color|font)/i, "CSS muss eine Typ-Regel für 'body' definieren (z.B. background-color oder font-family).");
assert.match(cssText, /h1\s*\{[^}]*color/i, "CSS muss eine Typ-Regel für 'h1' (z.B. color) enthalten.");

// TEST: Teilziel 2 - Klassen- (.card) & ID-Selektor (#featured-card)
assert.match(cssText, /\.card\s*\{[^}]*(?:border|padding|border-radius)/i, "Ein Klassen-Selektor '.card' muss definiert sein (mit border, border-radius oder padding).");
assert.match(cssText, /#featured-card\s*\{[^}]*(?:background|border|color)/i, "Ein ID-Selektor '#featured-card' muss spezifische Styles überschreiben.");

// TEST: Teilziel 3 - Kombinatoren (ul > li & h2 + p)
assert.match(cssText, /ul\s*>\s*li/i, "Der direkte Kind-Kombinator 'ul > li' muss verwendet werden.");
assert.match(cssText, /h2\s*\+\s*p/i, "Der direkt benachbarte Geschwister-Selektor 'h2 + p' muss verwendet werden.");

// TEST: Teilziel 4 - Attribut-Selektor a[target="_blank"]
assert.match(cssText, /a\[target\s*=\s*["']?_blank["']?\]/i, "Ein Attribut-Selektor für externe Links 'a[target=\"_blank\"]' muss definiert sein.");

// TEST: Teilziel 5 - Pseudo-Klassen (:hover & :nth-child)
assert.match(cssText, /:hover\b/i, "Mindestens eine interaktive ':hover'-Pseudo-Klasse (z.B. .btn:hover) muss definiert sein.");
assert.match(cssText, /:nth-child\s*\(\s*(?:even|odd|\d+n?[+-]?\d*)\s*\)/i, "Eine strukturelle ':nth-child(...)'-Pseudo-Klasse muss definiert sein (z.B. li:nth-child(even)).");
