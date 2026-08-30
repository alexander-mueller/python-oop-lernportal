// 🧪 CSS 10: Testsuite für CSS Grid 2D-Matrix & Template Areas

const styleContent = Array.from(document.querySelectorAll("style")).map(s => s.textContent).join("\n");

// TEST: 1. Dashboard Grid-Container & Spalten
assert.ok(
  document.querySelector(".dashboard-layout"),
  ".dashboard-layout muss im HTML existieren"
);
assert.ok(
  /\.dashboard-layout\s*\{[^}]*display\s*:\s*grid/i.test(styleContent),
  ".dashboard-layout muss 'display: grid' besitzen"
);
assert.ok(
  /\.dashboard-layout\s*\{[^}]*grid-template-columns\s*:\s*(240px|250px)\s+1fr/i.test(styleContent),
  ".dashboard-layout muss 'grid-template-columns: 240px 1fr' (oder 250px 1fr) besitzen"
);
assert.ok(
  /\.dashboard-layout\s*\{[^}]*gap\s*:\s*(20px|16px|1\.25rem|1rem)/i.test(styleContent),
  ".dashboard-layout muss ein gap definiert haben"
);

// TEST: 2. Grid-Template-Areas Definition
assert.ok(
  /grid-template-areas\s*:\s*["']header\s+header["']\s*["']sidebar\s+main["']\s*["']footer\s+footer["']/i.test(styleContent),
  ".dashboard-layout muss grid-template-areas mit 'header header', 'sidebar main', 'footer footer' definieren"
);

// TEST: 3. Zuweisung der Grid-Areas
assert.ok(
  /\.dash-header\s*\{[^}]*grid-area\s*:\s*header/i.test(styleContent),
  ".dash-header muss 'grid-area: header' zugewiesen bekommen"
);
assert.ok(
  /\.dash-sidebar\s*\{[^}]*grid-area\s*:\s*sidebar/i.test(styleContent),
  ".dash-sidebar muss 'grid-area: sidebar' zugewiesen bekommen"
);
assert.ok(
  /\.dash-main\s*\{[^}]*grid-area\s*:\s*main/i.test(styleContent),
  ".dash-main muss 'grid-area: main' zugewiesen bekommen"
);
assert.ok(
  /\.dash-footer\s*\{[^}]*grid-area\s*:\s*footer/i.test(styleContent),
  ".dash-footer muss 'grid-area: footer' zugewiesen bekommen"
);

// TEST: 4. Metrics-Grid mit auto-fit & minmax
assert.ok(
  document.querySelector(".metrics-grid"),
  ".metrics-grid muss im HTML existieren"
);
assert.ok(
  /\.metrics-grid\s*\{[^}]*display\s*:\s*grid/i.test(styleContent),
  ".metrics-grid muss 'display: grid' besitzen"
);
assert.ok(
  /\.metrics-grid\s*\{[^}]*grid-template-columns\s*:\s*repeat\(\s*auto-fit\s*,\s*minmax\(\s*200px\s*,\s*1fr\s*\)\s*\)/i.test(styleContent),
  ".metrics-grid muss 'grid-template-columns: repeat(auto-fit, minmax(200px, 1fr))' besitzen"
);

// TEST: 5. Featured Metric Card Spanning (grid-column: span 2)
assert.ok(
  document.querySelector(".metric-card--featured"),
  ".metric-card--featured muss im HTML existieren"
);
assert.ok(
  /\.metric-card--featured\s*\{[^}]*grid-column\s*:\s*span\s+2/i.test(styleContent),
  ".metric-card--featured muss 'grid-column: span 2' besitzen"
);

console.log("✅ Alle 5 CSS-Grid-Tests für Modul 10 erfolgreich bestanden!");
