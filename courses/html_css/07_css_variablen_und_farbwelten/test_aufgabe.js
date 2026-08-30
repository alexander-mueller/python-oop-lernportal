// 🧪 Testsuite: CSS 07 - Custom Properties & Farbräume

const styleTag = doc.querySelector("style");
assert.ok(styleTag && styleTag.textContent.trim().length > 0, "Ein <style>-Tag mit CSS-Regeln muss vorhanden sein.");
const cssText = styleTag.textContent;

// TEST: Teilziel 1 - :root Custom Properties Deklaration
assert.match(cssText, /:root\s*\{[^}]*--[a-zA-Z0-9_-]+\s*:/i, "Im ':root'-Selektor müssen CSS Custom Properties (z.B. --primary-color) definiert werden.");

// TEST: Teilziel 2 - Nutzung von var()
assert.match(cssText, /var\s*\(\s*--[a-zA-Z0-9_-]+/i, "CSS-Eigenschaften müssen Werte über die Funktion 'var(--name)' abrufen.");

// TEST: Teilziel 3 - Vielfalt an Farbmodellen (HEX, HSL/RGB, OKLCH)
assert.match(cssText, /#[0-9a-fA-F]{3,8}\b/, "Mindestens ein Farbwert im HEX-Format (z.B. #2563eb) muss vorkommen.");
assert.match(cssText, /(?:hsl|rgba?)\s*\(/i, "Mindestens ein Farbwert im HSL- oder RGB/RGBA-Format muss definiert sein.");
assert.match(cssText, /oklch\s*\(/i, "Mindestens ein moderner Farbwert im wahrnehmungsbasierten 'oklch(...)'-Farbraum muss genutzt werden.");

// TEST: Teilziel 4 - Linear Gradient Farbverlauf
assert.match(cssText, /linear-gradient\s*\(/i, "Ein Farbverlauf mit 'linear-gradient(...)' muss definiert sein (z.B. auf .gradient-header).");

// TEST: Teilziel 5 - Theme-Klasse mit Variablen-Überschreibung
assert.match(cssText, /\.dark-theme\s*\{[^}]*--[a-zA-Z0-9_-]+\s*:/i, "Die Klasse '.dark-theme' muss CSS-Variablen lokal überschreiben.");
