// 🧪 Testsuite: HTML 04 - Accessibility & ARIA

// TEST: Teilziel 1 - Skip-Link & Sprungziel
const skipLink = doc.querySelector('a[href="#main-content"]');
assert.ok(skipLink, "Ein Skip-Link mit href=\"#main-content\" muss als Navigationshilfe existieren.");
const mainTarget = doc.querySelector('main#main-content, #main-content');
assert.ok(mainTarget, "Das Sprungziel mit id=\"main-content\" (idealerweise das <main>-Element) muss vorhanden sein.");

// TEST: Teilziel 2 - Icon-Button mit aria-label & aria-hidden
const ariaLabelBtn = doc.querySelector('button[aria-label]');
assert.ok(ariaLabelBtn && ariaLabelBtn.getAttribute("aria-label").trim().length > 0, "Ein Button mit aussagekräftigem aria-label-Attribut ist erforderlich.");
const ariaHiddenIcon = ariaLabelBtn ? ariaLabelBtn.querySelector('[aria-hidden="true"]') : doc.querySelector('[aria-hidden="true"]');
assert.ok(ariaHiddenIcon, "Das rein dekorative Icon im Button muss aria-hidden=\"true\" besitzen.");

// TEST: Teilziel 3 - Aufklappbares Accordion mit aria-expanded & aria-controls
const expandedBtn = doc.querySelector('button[aria-expanded][aria-controls]');
assert.ok(expandedBtn, "Ein Accordion-Button mit aria-expanded und aria-controls-Attributen muss existieren.");
assert.ok(expandedBtn.getAttribute("aria-expanded") === "false" || expandedBtn.getAttribute("aria-expanded") === "true", "aria-expanded muss 'true' oder 'false' sein.");
const controlledId = expandedBtn.getAttribute("aria-controls");
const controlledElement = doc.getElementById(controlledId);
assert.ok(controlledElement, `Das durch aria-controls="${controlledId}" referenzierte Element muss im DOM existieren.`);

// TEST: Teilziel 4 - Hilfetext-Verknüpfung via aria-describedby
const describedInput = doc.querySelector('input[aria-describedby]');
assert.ok(describedInput, "Ein Eingabefeld mit aria-describedby-Attribut ist erforderlich.");
const descId = describedInput.getAttribute("aria-describedby");
const descElement = doc.getElementById(descId);
assert.ok(descElement && descElement.textContent.trim().length > 0, `Das durch aria-describedby="${descId}" verknüpfte Hinweistext-Element muss existieren.`);

// TEST: Teilziel 5 - Live Region mit role="status" & aria-live="polite"
const liveRegion = doc.querySelector('[role="status"], [aria-live]');
assert.ok(liveRegion, "Ein Live-Status-Bereich muss im Dokument definiert sein.");
assert.strictEqual(liveRegion.getAttribute("aria-live") || (liveRegion.getAttribute("role") === "status" ? "polite" : ""), "polite", "Der Statusbereich muss aria-live=\"polite\" oder role=\"status\" nutzen.");
