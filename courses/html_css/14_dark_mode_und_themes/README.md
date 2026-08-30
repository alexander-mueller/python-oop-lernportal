# CSS 14: Dark/Light Mode & System-Themes (CSS Custom Properties)

Ein nativer Dark Mode gehört heute zur Pflichtausstattung moderner Webanwendungen. In diesem Modul lernst du, wie du Themes mit **CSS Custom Properties (Variablen)**, der Media Query `@media (prefers-color-scheme)` und einem flexiblen HTML-Attribut-Umschalter (`data-theme`) aufbaust.

---

## 🎯 Lernziele

1. **CSS Custom Properties als Design-Token**: Globale Farbvariablen in `:root` definieren (`--bg-body`, `--bg-card`, `--text-main`, `--accent`).
2. **Systempräferenz abfragen**: `@media (prefers-color-scheme: dark)` für automatischen System-Sync.
3. **Explizites Theme-Override**: Selektor `[data-theme="dark"]` und `[data-theme="light"]`.
4. **Sanfte Theme-Transitions**: `transition: background-color 0.3s ease, color 0.3s ease`.
5. **Theme-Toggle-Interaktion**: Schalter mit JavaScript und `localStorage`-Persistenz.

---

## 🧠 Die Theme-Architektur im Detail

### 1. Variablen auf `:root` definieren (Light Theme als Standard)

```css
:root {
  --bg-body: #f8fafc;
  --bg-surface: #ffffff;
  --text-main: #0f172a;
  --text-muted: #64748b;
  --border-color: #e2e8f0;
  --primary: #4f46e5;
}
```

---

### 2. Dark Theme über `[data-theme="dark"]` überschreiben

Wir überschreiben **nur die Werte der Variablen**, nicht die Selektoren der Elemente!

```css
[data-theme="dark"] {
  --bg-body: #090d16;
  --bg-surface: #131b2e;
  --text-main: #f8fafc;
  --text-muted: #94a3b8;
  --border-color: #1e293b;
  --primary: #6366f1;
}
```

---

### 3. Automatische Anpassung an Betriebssysteme

```css
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --bg-body: #090d16;
    --bg-surface: #131b2e;
    --text-main: #f8fafc;
    --text-muted: #94a3b8;
    --border-color: #1e293b;
  }
}
```

---

### 4. Sanfter Farbwechsel mit CSS Transitions

```css
body, .theme-card, button {
  transition: background-color 0.3s ease, color 0.3s ease, border-color 0.3s ease;
}
```

---

## 🎯 Aufgabenstellung in `aufgabe.html`

- **TEILZIEL 1**: Definiere in `:root` die Standard-Variablen für das Light Theme (`--bg-body: #f8fafc`, `--bg-surface: #ffffff`, `--text-main: #0f172a`, `--border-color: #e2e8f0`).
- **TEILZIEL 2**: Überschreibe in `[data-theme="dark"]` die Variablen für das Dark Theme (`--bg-body: #0f172a`, `--bg-surface: #1e293b`, `--text-main: #f8fafc`, `--border-color: #334155`).
- **TEILZIEL 3**: Unterstütze `@media (prefers-color-scheme: dark)` für automatischen System-Sync.
- **TEILZIEL 4**: Wende die Variablen auf `body` und `.theme-card` an (`background: var(--bg-surface)`, `color: var(--text-main)`).
- **TEILZIEL 5**: Implementiere die Toggle-Funktion in JavaScript mit `document.documentElement.setAttribute('data-theme', ...)`.

Teste deine Theme-Logik mit `test_aufgabe.js`!
