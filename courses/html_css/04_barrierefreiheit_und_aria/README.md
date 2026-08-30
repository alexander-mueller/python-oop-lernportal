# HTML 04: Barrierefreiheit (A11y) & ARIA ♿

Willkommen in **Modul 04**!

In dieser Lerneinheit lernst du, wie Webseiten barrierefrei (WCAG 2.2 konform) gestaltet werden und wie WAI-ARIA Screenreadern und Tastatur-Nutzern Orientierung gibt.

---

## 💡 1. Das Wichtigste in Kürze

### Skip-Links & Tastatur-Fokus
- Ermöglichen Tastatur-Nutzern das direkte Überspringen langer Navigationsmenüs zum Hauptinhalt (`#main-content`).
- Interaktive Steuerelemente müssen echte `<button>`- oder `<a>`-Tags sein, niemals klickbare `<div>`s.

### Wichtige ARIA-Attribute
- `aria-label`: Eindeutiger Name für Icons oder Buttons ohne sichtbaren Text.
- `aria-expanded`: Zeigt an, ob ein Dropdown/Accordion ein- oder ausgeklappt ist (`"true"` / `"false"`).
- `aria-controls`: Verweist auf die `id` des gesteuerten Elements.
- `aria-hidden="true"`: Versteckt rein dekorative Elemente vor Screenreadern.
- `aria-describedby`: Verknüpft Eingabefelder mit Hilfetexten oder Fehlermeldungen.
- `role="status"` & `aria-live="polite"`: Kündigt dynamische Inhaltsänderungen für Screenreader an.

---

## 🎯 Teilziele in `aufgabe.html`

1. **Skip-Link**: Erstelle `<a href="#main-content">` ganz oben im `<body>` und `<main id="main-content">`.
2. **Icon-Button**: Erstelle `<button type="button" aria-label="Modal schließen">` mit einem Icon, das `aria-hidden="true"` hat.
3. **Accordion**: Baue einen Button mit `aria-expanded="false"` und `aria-controls="faq-answer"` mit zugehörigem Content-Container.
4. **Hilfetext-Verknüpfung**: Erstelle ein Input-Feld mit `aria-describedby="password-hint"` und den zugehörigen Hinweistext.
5. **Live Region**: Richte einen Benachrichtigungsbereich mit `role="status"` und `aria-live="polite"` ein.
