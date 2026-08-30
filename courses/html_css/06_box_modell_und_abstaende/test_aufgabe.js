// 🧪 Testsuite: CSS 06 - Box-Modell & Abstände

const styleTag = doc.querySelector("style");
assert.ok(styleTag && styleTag.textContent.trim().length > 0, "Ein <style>-Tag mit CSS-Regeln muss definiert sein.");
const cssText = styleTag.textContent;

// TEST: Teilziel 1 - Universeller Box-Sizing Reset
assert.match(cssText, /\*[^}]*box-sizing\s*:\s*border-box/i, "Ein universeller Reset mit 'box-sizing: border-box' muss auf '*' angewendet werden.");

// TEST: Teilziel 2 - Container mit max-width & horizontalem Auto-Margin
assert.match(cssText, /\.card-container\s*\{[^}]*max-width/i, ".card-container muss eine 'max-width' definieren.");
assert.match(cssText, /\.card-container\s*\{[^}]*margin\s*:[^;]*auto/i, ".card-container muss durch 'margin: ... auto' horizontal zentriert werden.");

// TEST: Teilziel 3 - Card-Box mit Padding, Border & Border-Radius
assert.match(cssText, /\.profile-card\s*\{[^}]*padding\s*:/i, ".profile-card muss einen Innenabstand mit 'padding' erhalten.");
assert.match(cssText, /\.profile-card\s*\{[^}]*border\s*:/i, ".profile-card muss einen sichtbaren Rahmen ('border') definieren.");
assert.match(cssText, /\.profile-card\s*\{[^}]*border-radius\s*:/i, ".profile-card muss abgerundete Ecken mit 'border-radius' besitzen.");

// TEST: Teilziel 4 - Vertikaler Abstand mit margin-bottom
assert.match(cssText, /margin-bottom\s*:/i, "Überschrift oder Absätze müssen mit 'margin-bottom' formatiert sein.");

// TEST: Teilziel 5 - Badges mit display: inline-block, padding & margin
assert.match(cssText, /\.skill-badge\s*\{[^}]*display\s*:\s*inline-block/i, ".skill-badge muss 'display: inline-block' nutzen.");
assert.match(cssText, /\.skill-badge\s*\{[^}]*padding\s*:/i, ".skill-badge benötigt ein Innenabstand-Styling ('padding').");
assert.match(cssText, /\.skill-badge\s*\{[^}]*margin/i, ".skill-badge muss Außenabstände ('margin') definieren.");
