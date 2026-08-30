// 🧪 CSS 12: Testsuite für Transitions, Transforms & Keyframes

const styleContent = Array.from(document.querySelectorAll("style")).map(s => s.textContent).join("\n");

// TEST: 1. Transition auf .interactive-card
assert.ok(
  document.querySelector(".interactive-card"),
  ".interactive-card muss im HTML existieren"
);
assert.ok(
  /\.interactive-card\s*\{[^}]*transition\s*:\s*[^;]*(transform|box-shadow)/i.test(styleContent),
  ".interactive-card muss eine Transition für 'transform' oder 'box-shadow' besitzen"
);

// TEST: 2. Hover-Zustand mit Transform & Box-Shadow
assert.ok(
  /\.interactive-card:hover\s*\{[^}]*transform\s*:\s*translateY\(-8px\)/i.test(styleContent) &&
  /\.interactive-card:hover\s*\{[^}]*transform\s*:\s*[^;]*scale\(1\.02\)/i.test(styleContent),
  ".interactive-card:hover muss 'transform: translateY(-8px) scale(1.02)' besitzen"
);
assert.ok(
  /\.interactive-card:hover\s*\{[^}]*box-shadow\s*:/i.test(styleContent),
  ".interactive-card:hover muss einen erweiterten 'box-shadow' erhalten"
);

// TEST: 3. Keyframes Pulse & .live-dot Animation
assert.ok(
  /@keyframes\s+pulse\s*\{/i.test(styleContent),
  "@keyframes pulse muss im CSS definiert sein"
);
assert.ok(
  /\.live-dot\s*\{[^}]*animation\s*:\s*pulse\s+2s\s+infinite/i.test(styleContent),
  ".live-dot muss 'animation: pulse 2s infinite ease-in-out' besitzen"
);

// TEST: 4. Keyframes Float & .floating-badge Animation
assert.ok(
  /@keyframes\s+float\s*\{/i.test(styleContent),
  "@keyframes float muss im CSS definiert sein"
);
assert.ok(
  /\.floating-badge\s*\{[^}]*animation\s*:\s*float\s+4s\s+infinite/i.test(styleContent),
  ".floating-badge muss 'animation: float 4s infinite ease-in-out' besitzen"
);

// TEST: 5. Barrierefreiheit mit prefers-reduced-motion
assert.ok(
  /@media\s*\(\s*prefers-reduced-motion\s*:\s*reduce\s*\)/i.test(styleContent),
  "Media Query '@media (prefers-reduced-motion: reduce)' muss im Stylesheet definiert sein"
);

console.log("✅ Alle 5 Transitions & Keyframe Tests für Modul 12 erfolgreich bestanden!");
