// 🧪 CSS 11: Testsuite für Media Queries & Mobile-First Design

const styleContent = Array.from(document.querySelectorAll("style")).map(s => s.textContent).join("\n");

// TEST: 1. Flüssige Typografie mit clamp()
assert.ok(
  document.querySelector(".hero-title"),
  ".hero-title muss im HTML existieren"
);
assert.ok(
  /\.hero-title\s*\{[^}]*font-size\s*:\s*clamp\(\s*1\.75rem\s*,\s*4vw\s*\+\s*1rem\s*,\s*3rem\s*\)/i.test(styleContent),
  ".hero-title muss 'font-size: clamp(1.75rem, 4vw + 1rem, 3rem)' besitzen"
);

// TEST: 2. Mobile-First Basis-Layout
assert.ok(
  document.querySelector(".responsive-layout"),
  ".responsive-layout muss im HTML existieren"
);
assert.ok(
  /\.responsive-layout\s*\{[^}]*display\s*:\s*flex/i.test(styleContent),
  ".responsive-layout muss als Flex-Container ('display: flex') deklariert sein"
);
assert.ok(
  /\.responsive-layout\s*\{[^}]*flex-direction\s*:\s*column/i.test(styleContent),
  ".responsive-layout muss in den Basis-Styles 'flex-direction: column' besitzen (Mobile First)"
);

// TEST: 3. Media Query für Tablet (min-width: 768px)
assert.ok(
  /@media\s*\(\s*min-width\s*:\s*768px\s*\)/i.test(styleContent),
  "Media Query '@media (min-width: 768px)' muss im Stylesheet vorhanden sein"
);
assert.ok(
  /@media[^{]*\(\s*min-width\s*:\s*768px\s*\)\s*\{[\s\S]*?\.responsive-layout\s*\{[\s\S]*?flex-direction\s*:\s*row/i.test(styleContent),
  "Unter @media (min-width: 768px) muss .responsive-layout auf 'flex-direction: row' umgeschaltet werden"
);

// TEST: 4. Media Query für Desktop (min-width: 1024px)
assert.ok(
  /@media\s*\(\s*min-width\s*:\s*1024px\s*\)/i.test(styleContent),
  "Media Query '@media (min-width: 1024px)' muss im Stylesheet vorhanden sein"
);
assert.ok(
  /@media[^{]*\(\s*min-width\s*:\s*1024px\s*\)\s*\{[\s\S]*?\.features-grid\s*\{[\s\S]*?grid-template-columns\s*:\s*repeat\(\s*3\s*,\s*1fr\s*\)/i.test(styleContent),
  "Unter @media (min-width: 1024px) muss .features-grid auf 'grid-template-columns: repeat(3, 1fr)' geschaltet werden"
);

console.log("✅ Alle 4 Responsive-Tests für Modul 11 erfolgreich bestanden!");
