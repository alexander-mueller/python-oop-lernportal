// 🧪 Testsuite: CSS 08 - Web-Typografie, Schriftarten & Text-Effekte

const styleTag = doc.querySelector("style");
assert.ok(styleTag && styleTag.textContent.trim().length > 0, "Ein <style>-Tag mit CSS-Regeln muss vorhanden sein.");
const cssText = styleTag.textContent;

// TEST: Teilziel 1 - Webfont @import
assert.match(cssText, /@import\s+url\s*\([^)]+fonts\.(?:googleapis|bunny|google)\.com[^)]+\)/i, "Eine externe Webfont von Google Fonts muss mit '@import url(...)' eingebunden werden.");

// TEST: Teilziel 2 - Font-Family auf body
assert.match(cssText, /body\s*\{[^}]*font-family\s*:/i, "Der 'body' muss eine 'font-family' zugewiesen bekommen.");

// TEST: Teilziel 3 - Type-Scale in rem
assert.match(cssText, /h1\s*\{[^}]*font-size\s*:\s*[0-9.]+(?:rem|em|px)/i, "h1 muss eine spezifische 'font-size' besitzen.");
assert.match(cssText, /h2\s*\{[^}]*font-size\s*:\s*[0-9.]+(?:rem|em|px)/i, "h2 muss eine spezifische 'font-size' besitzen.");

// TEST: Teilziel 4 - Lesefreundliche line-height auf Absätzen
assert.match(cssText, /p\s*\{[^}]*line-height\s*:\s*(?:1\.[5-9]|[2-9]|normal|[0-9.]+(?:rem|em|px|%))/i, "Absätze (p) müssen eine lesefreundliche 'line-height' (z.B. 1.6) aufweisen.");

// TEST: Teilziel 5 - .category-tag mit text-transform: uppercase & letter-spacing
assert.match(cssText, /\.category-tag\s*\{[^}]*text-transform\s*:\s*uppercase/i, ".category-tag muss 'text-transform: uppercase' verwenden.");
assert.match(cssText, /\.category-tag\s*\{[^}]*letter-spacing\s*:/i, ".category-tag muss eine Laufweite mit 'letter-spacing' definieren.");
