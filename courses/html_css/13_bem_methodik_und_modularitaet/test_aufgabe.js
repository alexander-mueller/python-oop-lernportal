// 🧪 CSS 13: Testsuite für BEM-Methodik & Modulare CSS-Architektur

const styleContent = Array.from(document.querySelectorAll("style")).map(s => s.textContent).join("\n");

// TEST: 1. BEM Card Elements Styling
assert.ok(
  document.querySelector(".pricing-card__header") && document.querySelector(".pricing-card__title"),
  "BEM-Elemente .pricing-card__header und .pricing-card__title müssen im DOM existieren"
);
assert.ok(
  /\.pricing-card__header\s*\{[^}]*display\s*:\s*flex/i.test(styleContent) &&
  /\.pricing-card__header\s*\{[^}]*justify-content\s*:\s*space-between/i.test(styleContent),
  ".pricing-card__header muss 'display: flex' und 'justify-content: space-between' besitzen"
);
assert.ok(
  /\.pricing-card__title\s*\{[^}]*font-size\s*:/i.test(styleContent),
  ".pricing-card__title muss eine definierte Schriftgröße besitzen"
);
assert.ok(
  /\.pricing-card__price\s*\{[^}]*font-size\s*:/i.test(styleContent),
  ".pricing-card__price muss eine hervorgehobene Schriftgröße besitzen"
);

// TEST: 2. BEM Block-Modifier .pricing-card--popular
assert.ok(
  document.querySelector(".pricing-card--popular"),
  ".pricing-card--popular Modifier muss im HTML existieren"
);
assert.ok(
  /\.pricing-card--popular\s*\{[^}]*border-color\s*:/i.test(styleContent),
  ".pricing-card--popular muss 'border-color' überschreiben"
);
assert.ok(
  /\.pricing-card--popular\s*\{[^}]*transform\s*:\s*scale\(/i.test(styleContent),
  ".pricing-card--popular muss mit 'transform: scale(...)' optisch hervorgehoben werden"
);

// TEST: 3. BEM Button Modifiers (.btn--primary & .btn--outline)
assert.ok(
  document.querySelector(".btn--primary") && document.querySelector(".btn--outline"),
  "BEM Button-Varianten .btn--primary und .btn--outline müssen im HTML existieren"
);
assert.ok(
  /\.btn--primary\s*\{[^}]*background\s*:/i.test(styleContent),
  ".btn--primary muss eine eigene Hintergrundfarbe definieren"
);
assert.ok(
  /\.btn--outline\s*\{[^}]*(border|background\s*:\s*transparent)/i.test(styleContent),
  ".btn--outline muss 'background: transparent' oder einen 'border' besitzen"
);

// TEST: 4. BEM Badge Modifier (.pricing-card__badge--highlight)
assert.ok(
  document.querySelector(".pricing-card__badge--highlight"),
  ".pricing-card__badge--highlight muss im HTML existieren"
);
assert.ok(
  /\.pricing-card__badge--highlight\s*\{[^}]*background\s*:/i.test(styleContent),
  ".pricing-card__badge--highlight muss eine Highlight-Farbe besitzen"
);

console.log("✅ Alle 4 BEM-Architektur Tests für Modul 13 erfolgreich bestanden!");
