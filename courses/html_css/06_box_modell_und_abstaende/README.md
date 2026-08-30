# CSS 06: Box-Modell, Padding, Margin & Border 📦

Willkommen in **Modul 06**!

In dieser Einheit meisterst du das Fundament jedes CSS-Layouts: Das Box-Modell, `box-sizing: border-box`, Innen- und Außenabstände sowie Margenkollaps.

---

## 💡 1. Das Wichtigste in Kürze

### Die Schichten des Box-Modells
1. **Content**: Der eigentliche Text- oder Bildinhalt (`width`, `height`).
2. **Padding**: Der Innenabstand zwischen Inhalt und Rahmen.
3. **Border**: Der sichtbare Rahmen um das Element herum.
4. **Margin**: Der Außenabstand zu benachbarten Elementen.

### Der moderne Border-Box Reset
```css
*, *::before, *::after {
  box-sizing: border-box;
}
```
Verhindert, dass `padding` und `border` die deklarierte Gesamtbreite vergrößern.

### Margin Auto & TRBL-Shorthands
- `margin: 0 auto;`: Zentriert einen Block-Container mit definierter `max-width` horizontal im Fenster.
- `padding: 10px 20px;`: Oben/Unten 10px, Links/Rechts 20px.
- `display: inline-block`: Ermöglicht Breiten-, Höhen- und Margin/Padding-Angaben auf Text-Elementen (wie Badges).

---

## 🎯 Teilziele in `aufgabe.html`

1. **Box-Sizing Reset**: Wende `box-sizing: border-box` auf `*, *::before, *::after` an.
2. **Container Zentrieren**: Style `.card-container` mit `max-width`, `margin: 0 auto` und `padding`.
3. **Card-Box**: Style `.profile-card` mit `padding`, `border`, `border-radius` und Hintergrund.
4. **Vertikaler Abstand**: Setze `margin-bottom` auf Überschriften und Absätze.
5. **Inline-Block Badges**: Style `.skill-badge` mit `display: inline-block`, `padding`, `margin-right` und `border-radius`.
