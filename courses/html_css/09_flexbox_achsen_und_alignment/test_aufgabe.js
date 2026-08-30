// 🧪 CSS 09: Testsuite für Flexbox Achsen, Justify & Align

// TEST: 1. Navbar Flex-Container & Alignment
assert.ok(
  document.querySelector(".navbar"),
  "Element mit Klasse '.navbar' muss im DOM existieren"
);
const styleContent = Array.from(document.querySelectorAll("style")).map(s => s.textContent).join("\n");
assert.ok(
  /\.navbar\s*\{[^}]*display\s*:\s*flex/i.test(styleContent),
  ".navbar muss 'display: flex' besitzen"
);
assert.ok(
  /\.navbar\s*\{[^}]*justify-content\s*:\s*space-between/i.test(styleContent),
  ".navbar muss 'justify-content: space-between' besitzen"
);
assert.ok(
  /\.navbar\s*\{[^}]*align-items\s*:\s*center/i.test(styleContent),
  ".navbar muss 'align-items: center' besitzen"
);

// TEST: 2. Nav-Links horizontale Flex-Liste
assert.ok(
  document.querySelector(".nav-links"),
  "Element mit Klasse '.nav-links' muss im DOM existieren"
);
assert.ok(
  /\.nav-links\s*\{[^}]*display\s*:\s*flex/i.test(styleContent),
  ".nav-links muss 'display: flex' besitzen"
);
assert.ok(
  /\.nav-links\s*\{[^}]*list-style\s*:\s*none/i.test(styleContent),
  ".nav-links muss 'list-style: none' besitzen"
);
assert.ok(
  /\.nav-links\s*\{[^}]*gap\s*:\s*(20px|1\.25rem)/i.test(styleContent),
  ".nav-links muss 'gap: 20px' besitzen"
);

// TEST: 3. Card-Container mit Flex-Wrap & Gap
assert.ok(
  document.querySelector(".card-container"),
  "Element mit Klasse '.card-container' muss im DOM existieren"
);
assert.ok(
  /\.card-container\s*\{[^}]*display\s*:\s*flex/i.test(styleContent),
  ".card-container muss 'display: flex' besitzen"
);
assert.ok(
  /\.card-container\s*\{[^}]*flex-wrap\s*:\s*wrap/i.test(styleContent),
  ".card-container muss 'flex-wrap: wrap' besitzen"
);
assert.ok(
  /\.card-container\s*\{[^}]*gap\s*:\s*(24px|1\.5rem)/i.test(styleContent),
  ".card-container muss 'gap: 24px' besitzen"
);

// TEST: 4. Flex-Card Sizing & Column-Layout
const cards = document.querySelectorAll(".flex-card");
assert.ok(cards.length >= 3, "Mindestens 3 .flex-card Elemente müssen im HTML existieren");
assert.ok(
  /\.flex-card\s*\{[^}]*flex\s*:\s*1\s+1\s+280px/i.test(styleContent) ||
  (/\.flex-card\s*\{[^}]*flex-grow\s*:\s*1/i.test(styleContent) && /\.flex-card\s*\{[^}]*flex-basis\s*:\s*280px/i.test(styleContent)),
  ".flex-card muss Flex-Sizing besitzen ('flex: 1 1 280px' oder entsprechende Einzelregeln)"
);
assert.ok(
  /\.flex-card\s*\{[^}]*display\s*:\s*flex/i.test(styleContent),
  ".flex-card muss als innerer Flex-Container ('display: flex') deklariert sein"
);
assert.ok(
  /\.flex-card\s*\{[^}]*flex-direction\s*:\s*column/i.test(styleContent),
  ".flex-card muss 'flex-direction: column' besitzen"
);

// TEST: 5. Badge Alignment mit align-self
assert.ok(
  document.querySelector(".card__badge"),
  "Element mit Klasse '.card__badge' muss im DOM existieren"
);
assert.ok(
  /\.card__badge\s*\{[^}]*align-self\s*:\s*flex-start/i.test(styleContent),
  ".card__badge muss 'align-self: flex-start' besitzen"
);

console.log("✅ Alle 5 Flexbox-Tests für Modul 09 erfolgreich bestanden!");
