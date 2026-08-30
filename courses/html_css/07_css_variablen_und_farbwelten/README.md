# CSS 07: CSS Custom Properties & Farbsysteme 🌈

Willkommen in **Modul 07**!

In diesem Modul erstellst du ein dynamisches Design-Token-System mit CSS Custom Properties (`--variable`), nutzt moderne Farbmodelle (HEX, RGB, HSL, OKLCH) und implementierst ein variables Dark/Light Theme.

---

## 💡 1. Das Wichtigste in Kürze

### Deklaration & Zugriff
```css
:root {
  --primary: #3b82f6;
  --bg-surface: oklch(0.98 0.01 240);
  --radius-sm: 6px;
}

.button {
  background-color: var(--primary);
  border-radius: var(--radius-sm);
}
```

### Farbmodelle im Überblick
- `HEX`: `#3b82f6`
- `RGB / RGBA`: `rgba(59, 130, 246, 0.8)` oder `rgb(59 130 246 / 80%)`
- `HSL`: `hsl(217, 91%, 60%)`
- `OKLCH`: `oklch(0.65 0.22 255)` (Sehr große Dynamik auf modernen Displays)

---

## 🎯 Teilziele in `aufgabe.html`

1. **:root Tokens**: Definiere Design-Token (`--primary-color`, `--bg-page`, `--bg-card`, `--text-color`, `--radius`).
2. **var() Verknüpfung**: Formatiere `body` und `.card` mit `var(...)`.
3. **Farbwelten**: Nutze HEX, HSL/RGBA und `oklch(...)`.
4. **Farbverlauf**: Wende `linear-gradient(...)` auf `.gradient-header` an.
5. **Theme-Klasse**: Überschreibe Variablen in `.dark-theme`.
