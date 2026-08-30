// 🧪 CSS 15: Testsuite für Moderne UI-Komponenten & Glassmorphism

const styleContent = Array.from(document.querySelectorAll("style")).map(s => s.textContent).join("\n");

// TEST: 1. Glassmorphism Card Styling
assert.ok(
  document.querySelector(".glass-card"),
  ".glass-card muss im DOM existieren"
);
assert.ok(
  /\.glass-card\s*\{[\s\S]*?backdrop-filter\s*:\s*blur\(/i.test(styleContent),
  ".glass-card muss 'backdrop-filter: blur(...)' besitzen"
);
assert.ok(
  /\.glass-card\s*\{[\s\S]*?background\s*:\s*rgba\(/i.test(styleContent),
  ".glass-card muss einen halbtransparenten 'background: rgba(...)' besitzen"
);

// TEST: 2. Natives HTML5 <dialog> und ::backdrop
assert.ok(
  document.querySelector("dialog"),
  "<dialog> Element muss im HTML existieren"
);
assert.ok(
  /dialog::backdrop\s*\{[\s\S]*?backdrop-filter\s*:/i.test(styleContent) ||
  /dialog::backdrop\s*\{[\s\S]*?background\s*:\s*rgba/i.test(styleContent),
  "dialog::backdrop muss gestylt sein (Hintergrund-Abdunklung oder Unschärfe)"
);

// TEST: 3. Pure CSS Tooltip
assert.ok(
  document.querySelector("[data-tooltip]"),
  "Element mit 'data-tooltip' Attribut muss existieren"
);
assert.ok(
  /\[data-tooltip\]::after\s*\{[\s\S]*?content\s*:\s*attr\(data-tooltip\)/i.test(styleContent),
  "[data-tooltip]::after muss 'content: attr(data-tooltip)' besitzen"
);

// TEST: 4. Badge-System
assert.ok(
  document.querySelector(".badge") && document.querySelector(".badge--success"),
  "Elemente mit .badge und .badge--success müssen im DOM existieren"
);
assert.ok(
  /\.badge--success\s*\{[^}]*background\s*:/i.test(styleContent),
  ".badge--success muss eine definierte Hintergrundfarbe besitzen"
);
assert.ok(
  /\.badge--purple\s*\{[^}]*background\s*:/i.test(styleContent),
  ".badge--purple muss eine definierte Hintergrundfarbe besitzen"
);

console.log("✅ Alle 4 Modern-UI-Tests für Modul 15 erfolgreich bestanden!");
