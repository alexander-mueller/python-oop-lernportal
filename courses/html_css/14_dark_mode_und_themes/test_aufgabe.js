// 🧪 CSS 14: Testsuite für Dark/Light Mode & System-Themes

const styleContent = Array.from(document.querySelectorAll("style")).map(s => s.textContent).join("\n");

// TEST: 1. :root Variablen für Light Theme
assert.ok(
  /:root\s*\{[\s\S]*?--bg-body\s*:\s*#f8fafc/i.test(styleContent) &&
  /:root\s*\{[\s\S]*?--bg-surface\s*:\s*#ffffff/i.test(styleContent),
  ":root muss die Variablen '--bg-body' und '--bg-surface' definieren"
);
assert.ok(
  /:root\s*\{[\s\S]*?--text-main\s*:\s*#0f172a/i.test(styleContent),
  ":root muss '--text-main' definieren"
);

// TEST: 2. [data-theme="dark"] Overrides
assert.ok(
  /\[data-theme=["']dark["']\]\s*\{[\s\S]*?--bg-body\s*:\s*#0f172a/i.test(styleContent) &&
  /\[data-theme=["']dark["']\]\s*\{[\s\S]*?--bg-surface\s*:\s*#1e293b/i.test(styleContent),
  "[data-theme='dark'] muss '--bg-body' (#0f172a) und '--bg-surface' (#1e293b) überschreiben"
);

// TEST: 3. prefers-color-scheme Media Query
assert.ok(
  /@media\s*\(\s*prefers-color-scheme\s*:\s*dark\s*\)/i.test(styleContent),
  "@media (prefers-color-scheme: dark) muss im CSS deklariert sein"
);

// TEST: 4. Variablen-Anwendung in Body & Theme-Card
assert.ok(
  /body\s*\{[^}]*background-color\s*:\s*var\(--bg-body\)/i.test(styleContent),
  "body muss 'background-color: var(--bg-body)' verwenden"
);
assert.ok(
  /\.theme-card\s*\{[^}]*background-color\s*:\s*var\(--bg-surface\)/i.test(styleContent),
  ".theme-card muss 'background-color: var(--bg-surface)' verwenden"
);

// TEST: 5. JavaScript Theme-Toggle-Button
const btn = document.getElementById("theme-toggle");
assert.ok(btn, "Button mit ID #theme-toggle muss im HTML existieren");
if (typeof btn.click === "function") {
  document.documentElement.removeAttribute("data-theme");
  btn.click();
  assert.strictEqual(document.documentElement.getAttribute("data-theme"), "dark", "Nach dem 1. Klick muss data-theme='dark' aktiv sein");
  btn.click();
  assert.strictEqual(document.documentElement.getAttribute("data-theme"), "light", "Nach dem 2. Klick muss data-theme='light' aktiv sein");
}

console.log("✅ Alle 5 Theme- und Dark-Mode-Tests für Modul 14 erfolgreich bestanden!");
