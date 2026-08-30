// 🧪 Testsuite: HTML 03 - Formulare & Validierung

// TEST: Teilziel 1 - Form-Container & Fieldset
const form = doc.querySelector("form");
assert.ok(form, "Ein <form>-Tag muss existieren.");
assert.ok(form.hasAttribute("action"), "Das <form> muss ein action-Attribut besitzen.");
assert.strictEqual((form.getAttribute("method") || "").toUpperCase(), "POST", "Das Formular muss method=\"POST\" verwenden.");
const fieldset = form.querySelector("fieldset");
assert.ok(fieldset, "Das Formular muss mindestens ein <fieldset> zur semantischen Gruppierung enthalten.");
const legend = fieldset ? fieldset.querySelector("legend") : null;
assert.ok(legend && legend.textContent.trim().length > 0, "Das <fieldset> muss ein <legend>-Element mit Beschreibung enthalten.");

// TEST: Teilziel 2 - Text & E-Mail Inputs mit Labels
const nameInput = doc.querySelector('input[name="name"], input#name, input[type="text"]');
assert.ok(nameInput, "Ein Text-Eingabefeld für den Namen muss vorhanden sein.");
assert.ok(nameInput.hasAttribute("required"), "Das Namensfeld muss das Attribut required besitzen.");
assert.ok(nameInput.id, "Das Namensfeld muss eine eindeutige id besitzen.");
const nameLabel = doc.querySelector(`label[for="${nameInput.id}"]`);
assert.ok(nameLabel, `Es muss ein <label for="${nameInput.id}"> für das Namensfeld existieren.`);

const emailInput = doc.querySelector('input[type="email"]');
assert.ok(emailInput, "Ein Eingabefeld mit type=\"email\" ist erforderlich.");
assert.ok(emailInput.hasAttribute("required"), "Das E-Mail-Feld muss als Pflichtfeld mit required markiert sein.");
assert.ok(emailInput.id, "Das E-Mail-Feld muss eine id besitzen.");
const emailLabel = doc.querySelector(`label[for="${emailInput.id}"]`);
assert.ok(emailLabel, `Ein verknüpftes <label for="${emailInput.id}"> für das E-Mail-Feld ist erforderlich.`);

// TEST: Teilziel 3 - Passwort & Number Inputs
const passwordInput = doc.querySelector('input[type="password"]');
assert.ok(passwordInput, "Ein Passwort-Feld (type=\"password\") muss existieren.");
assert.ok(passwordInput.hasAttribute("minlength") && parseInt(passwordInput.getAttribute("minlength")) >= 8, "Das Passwort-Feld muss minlength=\"8\" oder höher verlangen.");

const numberInput = doc.querySelector('input[type="number"]');
assert.ok(numberInput, "Ein Zahlen-Eingabefeld (type=\"number\") muss existieren.");
assert.ok(numberInput.hasAttribute("min") && numberInput.hasAttribute("max"), "Das Zahlenfeld muss die Attribute min und max zur Wertebereichsbeschränkung nutzen.");

// TEST: Teilziel 4 - Select & Textarea
const select = doc.querySelector("select");
assert.ok(select, "Ein <select>-Dropdown-Menü muss eingebunden sein.");
const options = select ? select.querySelectorAll("option") : [];
assert.ok(options.length >= 3, "Das <select>-Menü muss mindestens 3 <option>-Einträge anbieten.");

const textarea = doc.querySelector("textarea");
assert.ok(textarea, "Ein mehrzeiliges <textarea>-Feld für Motivation/Nachrichten muss existieren.");
assert.ok(textarea.id, "Das <textarea>-Feld muss eine id besitzen.");
const textareaLabel = doc.querySelector(`label[for="${textarea.id}"]`);
assert.ok(textareaLabel, "Ein zugehöriges <label> für die Textarea muss vorhanden sein.");

// TEST: Teilziel 5 - Checkbox & Submit-Button
const checkbox = doc.querySelector('input[type="checkbox"]');
assert.ok(checkbox, "Eine Checkbox (type=\"checkbox\") für die AGB-Zustimmung ist gefordert.");
assert.ok(checkbox.hasAttribute("required"), "Die AGB-Checkbox muss als Pflichtfeld mit required definiert sein.");

const submitBtn = doc.querySelector('button[type="submit"], input[type="submit"]');
assert.ok(submitBtn, "Ein Absende-Button mit type=\"submit\" muss im Formular vorhanden sein.");
