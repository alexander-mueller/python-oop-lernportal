# CSS 15: Moderne UI-Komponenten & Glassmorphism

Modernste Web-Interfaces setzen auf subtile Transparenzen, native HTML5-Dialoge und reaktive Komponenten ohne schwere JavaScript-Frameworks. In diesem Modul lernst du **Glassmorphism**, das native `<dialog>`-Element, CSS-Tooltips und Badge-Systeme kennen.

---

## 🎯 Lernziele

1. **Glassmorphism-Effekt**: `backdrop-filter: blur(16px)`, halbtransparente Hintergründe `rgba(255, 255, 255, 0.08)` und feine Glaskanten (`border: 1px solid rgba(255, 255, 255, 0.15)`).
2. **Natives HTML5 `<dialog>` Element**: Modale Fenster stylen mit `::backdrop` (Hintergrund-Abdunklung und Unschärfe).
3. **Pure-CSS Tooltips**: Infotexte mit `data-tooltip`, `::after` und `::before` ohne JavaScript.
4. **Moderne Status-Badges**: Pill-Badges mit sanftem Glow und Puls-Animation.
5. **Barrierefreie Dialog-Steuerung**: Öffnen mit `dialog.showModal()` und Schließen mit `dialog.close()`.

---

## 🧠 Die Kernkonzepte im Detail

### 1. Das Glassmorphism-Rezept

Glassmorphism simuliert mattes Milchglas mit optischer Lichtbrechung:

```css
.glass-card {
  /* 1. Halbtransparenter Hintergrund */
  background: rgba(255, 255, 255, 0.07);
  
  /* 2. Unschärfe des Hintergrundinhalts (Haupteffekt!) */
  backdrop-filter: blur(16px) saturate(180%);
  -webkit-backdrop-filter: blur(16px) saturate(180%);
  
  /* 3. Feine Glaskante & Reflexion */
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: 16px;
  
  /* 4. Tiefe durch weichen Schatten */
  box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
}
```

---

### 2. Natives `<dialog>` & `::backdrop`

Das HTML5-Element `<dialog>` ersetzt fehleranfällige Custom-Modals und bietet standardmäßig Tastaturbedienung (Escape-Taste) und Fokus-Falle:

```css
dialog.modal {
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 12px;
  background: #1e293b;
  color: white;
  padding: 24px;
  max-width: 500px;
}

/* Pseudo-Element für die Abdunklung hinter dem Modal */
dialog::backdrop {
  background: rgba(15, 23, 42, 0.75);
  backdrop-filter: blur(6px);
}
```

---

### 3. Pure-CSS Tooltip

```css
[data-tooltip] {
  position: relative;
  cursor: help;
}

[data-tooltip]::after {
  content: attr(data-tooltip);
  position: absolute;
  bottom: 125%;
  left: 50%;
  transform: translateX(-50%);
  background: #0f172a;
  color: white;
  padding: 6px 12px;
  border-radius: 4px;
  font-size: 0.8rem;
  white-space: nowrap;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.2s ease, transform 0.2s ease;
}

[data-tooltip]:hover::after {
  opacity: 1;
  transform: translateX(-50%) translateY(-4px);
}
```

---

## 🎯 Aufgabenstellung in `aufgabe.html`

- **TEILZIEL 1**: Stylinge `.glass-card` mit `backdrop-filter: blur(16px)`, `background: rgba(255, 255, 255, 0.08)` und Glaskante `border: 1px solid rgba(255, 255, 255, 0.15)`.
- **TEILZIEL 2**: Stylinge das native `<dialog id="demo-modal">` sowie das Pseudo-Element `dialog::backdrop` mit Unschärfe und Abdunklung.
- **TEILZIEL 3**: Implementiere den CSS-Tooltip für `[data-tooltip]::after` mit `content: attr(data-tooltip)`, absoluter Positionierung und Hover-Transition.
- **TEILZIEL 4**: Stylinge das Badge-System `.badge` und Varianten `.badge--success` und `.badge--purple`.

Teste dein Komponenten-Set mit `test_aufgabe.js`!
