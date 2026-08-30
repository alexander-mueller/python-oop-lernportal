# CSS 08: Web-Typografie, Schriftarten & Text-Effekte 🔤

Willkommen in **Modul 08**!

In dieser Lerneinheit lernst du, wie Webfonts via `@import` eingebunden werden, wie Font-Stacks aufgebaut sind, wie relative Schriftgrößen (`rem`) funktionieren und wie du Text-Transformationen gezielt einsetzt.

---

## 💡 1. Das Wichtigste in Kürze

### Webfont-Einbindung & Fallback
```css
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700&display=swap');

body {
  font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
}
```

### Type-Scales & Zeilenabstände
- `h1`: `2.25rem` bis `2.5rem`, `line-height: 1.2`
- `h2`: `1.5rem` bis `1.75rem`, `line-height: 1.3`
- `p`: `1rem` bis `1.125rem`, `line-height: 1.6` (optimale Zeilenhöhe für ermüdungsfreies Lesen)
- `letter-spacing`: `0.05em` bis `0.1em` in Kombination mit `text-transform: uppercase`

---

## 🎯 Teilziele in `aufgabe.html`

1. **Webfont @import**: Binde Google Fonts mit `@import` ein.
2. **Font-Family Stack**: Wende `font-family` mit Fallbacks auf den `body` an.
3. **Type-Scale**: Definiere Schriftgrößen mit relativen `rem`-Einheiten für `h1`, `h2` und `p`.
4. **Lesbarkeit**: Setze `line-height: 1.6` (oder höher) auf Absätze.
5. **Text-Transformation**: Formatiere `.category-tag` mit `text-transform: uppercase`, `letter-spacing` und `font-weight`.
