# CSS 11: Media Queries & Mobile-First Design (Responsive Web Design)

Moderne Websites müssen auf jedem Endgerät – vom Smartphone (360px) über Tablets (768px) bis zum 4K-Desktop – perfekt aussehen und bedienbar sein. In diesem Modul lernst du die professionelle **Mobile-First-Architektur** und moderne Einheiten wie `clamp()` kennen.

---

## 🎯 Lernziele

1. **Mobile-First Philosophie**: Standard-CSS für mobile Screens schreiben und mit `min-width` schrittweise erweitern.
2. **Breakpoints definieren**: `@media (min-width: 768px)` (Tablet) und `@media (min-width: 1024px)` (Desktop).
3. **Flüssige Typografie**: `font-size: clamp(1.5rem, 3vw + 1rem, 2.75rem)`.
4. **Moderne Viewport-Einheiten**: `vw`, `vh`, `dvh` (Dynamic Viewport Height).
5. **Responsive Komponenten**: Layouts von 1-Spalten-Stapel auf Mehrspalten-Raster umbauen.

---

## 🧠 Die Kernkonzepte im Detail

### 1. Mobile-First vs. Desktop-Down

Früher schrieb man Desktop-CSS und überschrieb es mühsam mit `max-width`. Der moderne Goldstandard ist **Mobile-First**:

```css
/* 📱 1. Standard-Styles: Gelten für Mobile (Standard-Fluss) */
.hero {
  flex-direction: column;
  padding: 16px;
}

/* 💻 2. Erweiterung für Tablets & Desktops ab 768px */
@media (min-width: 768px) {
  .hero {
    flex-direction: row;
    padding: 40px;
  }
}
```

Vorteile:
- Schlanker Code für leistungsschwächere Mobilgeräte.
- Klare, progressive Aufwärts-Kaskade (`min-width`).

---

### 2. Typische Standard-Breakpoints

| Breakpoint | Gerätetyp | Typische Werte |
| :--- | :--- | :--- |
| Standard | Smartphones | `< 768px` |
| `@media (min-width: 768px)` | Tablets / iPads | `768px - 1023px` |
| `@media (min-width: 1024px)` | Laptops / Desktops | `1024px - 1279px` |
| `@media (min-width: 1280px)` | Große Bildschirme / Ultra-Wide | `≥ 1280px` |

---

### 3. Flüssige Typografie mit `clamp()`

Statt für jeden Breakpoint feste Schriftgrößen zu definieren, passt `clamp()` die Größe stufenlos an:

```css
/* clamp(MIN, IDEAL, MAX) */
h1.hero-title {
  font-size: clamp(1.75rem, 4vw + 1rem, 3.25rem);
}
```
- **MIN (1.75rem)**: Wird auf kleinen Bildschirmen nie unterschritten.
- **IDEAL (4vw + 1rem)**: Skaliert flüssig mit der Bildschirmbreite (`vw`).
- **MAX (3.25rem)**: Wird auf großen Displays nicht überschritten.

---

## 🎯 Aufgabenstellung in `aufgabe.html`

- **TEILZIEL 1**: Definiere flüssige Typografie für `.hero-title` mit `clamp(1.75rem, 4vw + 1rem, 3rem)`.
- **TEILZIEL 2**: Setze Mobile-First Basisstyles für `.responsive-layout` (`display: flex`, `flex-direction: column`, `gap: 16px`).
- **TEILZIEL 3**: Erstelle einen Media-Query `@media (min-width: 768px)` und schalte `.responsive-layout` auf `flex-direction: row` und 2 gleich breite Spalten (`flex: 1`).
- **TEILZIEL 4**: Erstelle einen Media-Query `@media (min-width: 1024px)` und erweitere das Grid `.features-grid` auf 3 Spalten (`grid-template-columns: repeat(3, 1fr)`).

Teste deine Responsive-Regeln mit `test_aufgabe.js`!
