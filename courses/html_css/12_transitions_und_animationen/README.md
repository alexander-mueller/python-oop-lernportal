# CSS 12: Transitions, Transforms & Keyframes (Animationen)

Sanfte Bewegungen und visuelle Reaktionen machen Web-Oberflächen lebendig und intuitiv. In diesem Modul lernst du, wie du mit CSS Transitions, 2D/3D-Transformationen und `@keyframes`-Animationen hochwertige Interaktionen gestaltest.

---

## 🎯 Lernziele

1. **CSS Transitions**: Weiche Zustandswechsel mit `transition: transform 0.3s ease, box-shadow 0.3s ease`.
2. **Hardware-beschleunigte Transforms**: `transform: translateY(-8px) scale(1.02) rotate(2deg)`.
3. **Keyframe-Animationen**: Wiederholende Zyklen wie `pulse`, `float` und `spin` mit `@keyframes`.
4. **Animations-Parameter**: `animation: float 3s infinite ease-in-out`, `animation-fill-mode`.
5. **Barrierefreiheit (A11y)**: Nutzerpräferenzen mit `@media (prefers-reduced-motion: reduce)` respektieren.

---

## 🧠 Die Kernkonzepte im Detail

### 1. CSS Transitions

Transitions animieren den Übergang zwischen zwei Zuständen (z. B. `:hover`, `:focus`, `:active`):

```css
.card {
  /* Eigenschaft | Dauer | Easing-Funktion */
  transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.3s ease;
}

.card:hover {
  transform: translateY(-6px);
  box-shadow: 0 12px 24px -4px rgba(0, 0, 0, 0.3);
}
```

> **Performance-Tipp**: Animiere fast ausschließlich `transform` und `opacity`, da diese direkt auf der Grafikkarte (GPU) berechnet werden und keinen teuren Layout-Reflow auslösen.

---

### 2. 2D/3D Transformations (`transform`)

- `translate(x, y)` / `translateY(-10px)`: Verschiebung im Raum.
- `scale(1.05)`: Vergrößerung/Verkleinerung.
- `rotate(45deg)`: Rotation.
- `skew(10deg)`: Verzerrung.

Mehrere Werte können kombiniert werden: `transform: translateY(-5px) scale(1.02);`.

---

### 3. Komplexe Animationen mit `@keyframes`

Wenn eine Animation mehr als zwei Zustände hat oder dauerhaft in einer Schleife laufen soll:

```css
@keyframes pulse {
  0% {
    transform: scale(1);
    opacity: 1;
  }
  50% {
    transform: scale(1.15);
    opacity: 0.7;
  }
  100% {
    transform: scale(1);
    opacity: 1;
  }
}

.badge-live {
  animation: pulse 2s infinite ease-in-out;
}
```

---

### 4. Barrierefreiheit mit `prefers-reduced-motion`

Einige Nutzer leiden unter Schwindel oder vestibulären Störungen. Wir schalten Bewegungen für sie ab:

```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

---

## 🎯 Aufgabenstellung in `aufgabe.html`

- **TEILZIEL 1**: Versehe `.interactive-card` mit einer sanften Transition: `transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease`.
- **TEILZIEL 2**: Implementiere `.interactive-card:hover` mit `transform: translateY(-8px) scale(1.02)` und verstärktem `box-shadow`.
- **TEILZIEL 3**: Erstelle eine `@keyframes pulse` Animation und binde sie mit `animation: pulse 2s infinite ease-in-out` an `.live-indicator` an.
- **TEILZIEL 4**: Erstelle eine `@keyframes float` Animation und binde sie mit `animation: float 4s infinite ease-in-out` an `.floating-badge` an.
- **TEILZIEL 5**: Füge eine Barrierefreiheits-Regel `@media (prefers-reduced-motion: reduce)` hinzu.

Teste deine Animationen mit `test_aufgabe.js`!
