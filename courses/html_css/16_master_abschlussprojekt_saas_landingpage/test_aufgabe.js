// 🧪 Master 16: Testsuite für Responsive SaaS Landingpage & Portfolio Master

const styleContent = Array.from(document.querySelectorAll("style")).map(s => s.textContent).join("\n");

// TEST: 1. Semantische HTML5 Dokumentenstruktur
assert.ok(
  document.querySelector("header") && document.querySelector("nav") && document.querySelector("main") && document.querySelector("footer"),
  "Das Dokument muss alle semantischen Tags besitzen (<header>, <nav>, <main>, <footer>)"
);
assert.ok(
  document.querySelectorAll("section").length >= 2,
  "Mindestens 2 <section> Abschnitte müssen im HTML definiert sein"
);
assert.ok(
  document.querySelectorAll("article").length >= 3,
  "Mindestens 3 <article> Komponenten (Features, Pricing) müssen existieren"
);

// TEST: 2. Design-Tokens & Theme-System
assert.ok(
  /:root\s*\{[\s\S]*?--bg-body\s*:/i.test(styleContent) &&
  /:root\s*\{[\s\S]*?--primary\s*:/i.test(styleContent),
  ":root muss die Design-Tokens '--bg-body' und '--primary' definieren"
);
assert.ok(
  /\[data-theme=["']dark["']\]\s*\{[\s\S]*?--bg-body\s*:/i.test(styleContent),
  "[data-theme='dark'] muss Farbvariablen für den Dark Mode überschreiben"
);

// TEST: 3. Sticky Flexbox Navbar
assert.ok(
  document.querySelector(".navbar"),
  ".navbar muss im HTML existieren"
);
assert.ok(
  /\.navbar\s*\{[\s\S]*?display\s*:\s*flex/i.test(styleContent) &&
  /\.navbar\s*\{[\s\S]*?justify-content\s*:\s*space-between/i.test(styleContent),
  ".navbar muss 'display: flex' und 'justify-content: space-between' besitzen"
);

// TEST: 4. Hero Section mit clamp() & Glassmorphism
assert.ok(
  document.querySelector(".hero-title"),
  ".hero-title muss im HTML existieren"
);
assert.ok(
  /\.hero-title\s*\{[\s\S]*?font-size\s*:\s*clamp\(/i.test(styleContent),
  ".hero-title muss eine flüssige Schriftgröße mit 'clamp(...)' besitzen"
);
assert.ok(
  document.querySelector(".glass-card"),
  ".glass-card muss im HTML existieren"
);
assert.ok(
  /\.glass-card\s*\{[\s\S]*?backdrop-filter\s*:\s*blur\(/i.test(styleContent),
  ".glass-card muss 'backdrop-filter: blur(...)' besitzen"
);
assert.ok(
  /@keyframes\s+float\s*\{/i.test(styleContent),
  "@keyframes float muss für schwebende UI-Elemente definiert sein"
);

// TEST: 5. Responsive Feature Grid Matrix
assert.ok(
  document.querySelector(".features-grid"),
  ".features-grid muss im HTML existieren"
);
assert.ok(
  /\.features-grid\s*\{[\s\S]*?display\s*:\s*grid/i.test(styleContent) &&
  /\.features-grid\s*\{[\s\S]*?grid-template-columns\s*:\s*repeat\(\s*auto-fit/i.test(styleContent),
  ".features-grid muss als CSS Grid mit 'repeat(auto-fit, minmax(...))' definiert sein"
);

// TEST: 6. BEM Pricing Cards & Modifiers
assert.ok(
  document.querySelector(".pricing-card") && document.querySelector(".pricing-card--popular"),
  ".pricing-card und der Modifier .pricing-card--popular müssen im HTML existieren"
);
assert.ok(
  /\.pricing-card--popular\s*\{[\s\S]*?border-color\s*:/i.test(styleContent) ||
  /\.pricing-card--popular\s*\{[\s\S]*?transform\s*:/i.test(styleContent),
  ".pricing-card--popular muss den BEM-Modifier mit Akzentfarben oder Transform stylen"
);

// TEST: 7. Responsive Media Queries (Mobile-First)
assert.ok(
  /@media\s*\(\s*min-width\s*:\s*768px\s*\)/i.test(styleContent),
  "@media (min-width: 768px) muss für Tablet/Desktop-Breakpoints definiert sein"
);

console.log("🎉 MASTER-ABSCHLUSS: Alle 7 Master-Tests für Modul 16 erfolgreich bestanden!");
