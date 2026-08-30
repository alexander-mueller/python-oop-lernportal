# Master 16: Responsive SaaS Landingpage & Portfolio Master (Abschlussprojekt)

Herzlichen Glückwunsch zum Erreichen des großen Meister-Abschlussprojekts! In diesem Modul führst du alle erlernten Fertigkeiten aus den 4 Lehrpfaden zusammen und erstellst eine vollständige, produktionsreife, barrierefreie und responsive **SaaS Landingpage & Portfolio**-Website.

---

## 🎯 Lernziele & Synthese

1. **Semantisches HTML5 & A11y**: Klare Dokumentenstruktur (`header`, `nav`, `main`, `section`, `article`, `footer`, ARIA-Labels).
2. **Modern CSS Layouts**:
   - **Flexbox**: Sticky Navigation Bar, Pill-Badges und Button-Gruppen.
   - **CSS Grid**: 2D-Feature Matrix mit `repeat(auto-fit, minmax(280px, 1fr))` und responsive Pricing-Cards.
3. **Design-Tokens & Dark Mode**: CSS Custom Properties für Theme-Switching (`:root`, `[data-theme="dark"]`).
4. **Moderne UI-Effekte**: Glassmorphism Hero-Preview mit `backdrop-filter`, Hover-Lift Cards und `@keyframes float`-Animation.
5. **Mobile-First Responsivität**: Flüssige Typografie mit `clamp()` und Media Queries für Tablets (≥768px) und Desktops (≥1024px).
6. **BEM-Architektur**: Modulare Klassennamen (`.pricing-card`, `.pricing-card__header`, `.pricing-card--popular`).

---

## 🏛️ Aufbau der SaaS Landingpage

```text
┌────────────────────────────────────────────────────────┐
│ ⚡ Sticky Header: Logo, Nav-Links, Theme-Toggle, CTA   │
├────────────────────────────────────────────────────────┤
│ 🚀 Hero Section: Fluid Title, CTA-Group, Glassmorphism │
├────────────────────────────────────────────────────────┤
│ ⚡ Feature Matrix: CSS Grid (auto-fit, minmax)          │
├────────────────────────────────────────────────────────┤
│ 💎 Pricing Plans: BEM Cards mit --popular Highlight    │
├────────────────────────────────────────────────────────┤
│ 💬 Testimonials / Stats: Metric Counters               │
├────────────────────────────────────────────────────────┤
│ 📄 Footer: Links, Copyright, Accessibility Status      │
└────────────────────────────────────────────────────────┘
```

---

## 🎯 Aufgabenstellung in `aufgabe.html`

- **TEILZIEL 1**: Konfiguriere das Theme-System mit CSS Custom Properties für Light und Dark Mode (`:root` und `[data-theme="dark"]`).
- **TEILZIEL 2**: Stylinge die Sticky `.navbar` mit Flexbox (`justify-content: space-between`, `align-items: center`).
- **TEILZIEL 3**: Gestalte die `.hero-section` mit flüssiger `clamp()`-Überschrift und schwebender `.glass-card` (`backdrop-filter`, `@keyframes float`).
- **TEILZIEL 4**: Baue die `.features-grid` Matrix mit `display: grid` und `repeat(auto-fit, minmax(280px, 1fr))`.
- **TEILZIEL 5**: Implementiere die `.pricing-card` Komponenten nach BEM mit dem `.pricing-card--popular` Modifier.
- **TEILZIEL 6**: Stelle die 100% Responsivität mit Media Queries `@media (min-width: 768px)` sicher.

Teste dein Master-Projekt mit `test_aufgabe.js` und starte deine Web-Karriere! 🚀
