# CSS 13: BEM-Methodik & Modulare CSS-Architektur

In großen Web-Projekten wird unstrukturiertes CSS schnell zu einem unkontrollierbaren Chaos aus Spezifitätskriegen und `!important`-Hacks. Die **BEM-Methodik (Block, Element, Modifier)** löst dieses Problem durch eine glasklare, modulare Namenskonvention.

---

## 🎯 Lernziele

1. **BEM-Syntax verstehen**: Block (`.card`), Element (`.card__header`), Modifier (`.card--featured`).
2. **Spezifitätskriege vermeiden**: Flache Selektor-Hierarchien mit nur 1 Klasse Spezifität `(0, 1, 0)`.
3. **Wiederverwendbarkeit maximieren**: Isolierte UI-Komponenten, die an jeder Stelle der Website funktionieren.
4. **Element- vs. Block-Modifier**: Wann nutzt man `.btn--primary` vs. `.card__title--large`?
5. **Praxisnahe Card-Komponenten**: Aufbau einer robusten Produktkarten-Bibliothek.

---

## 🧠 Die BEM-Formel im Detail

BEM steht für:
- **B (Block)**: Eine eigenständige, wiederverwendbare UI-Komponente (z. B. `.card`, `.btn`, `.navbar`).
- **E (Element)**: Ein zwingender Teil eines Blocks, der außerhalb keinen Sinn ergibt. Getrennt mit zwei Unterstrichen `__` (z. B. `.card__title`, `.card__body`, `.card__image`).
- **M (Modifier)**: Eine visuelle Variante oder ein Zustand eines Blocks oder Elements. Getrennt mit zwei Bindestrichen `--` (z. B. `.card--featured`, `.btn--primary`, `.card__badge--success`).

```html
<!-- BEM HTML Struktur -->
<article class="card card--featured">
  <div class="card__header">
    <h3 class="card__title">Pro Plan</h3>
    <span class="card__badge card__badge--popular">Bestseller</span>
  </div>
  <div class="card__body">
    <p class="card__text">Alle Premium-Features freigeschaltet.</p>
  </div>
  <div class="card__footer">
    <button class="btn btn--primary btn--large">Jetzt upgraden</button>
  </div>
</article>
```

```css
/* BEM CSS: Flache Selektoren ohne Verschachtelung! */
.card { ... }
.card--featured { border-color: #6366f1; }

.card__header { display: flex; justify-content: space-between; }
.card__title { font-size: 1.25rem; font-weight: 700; }
.card__badge { font-size: 0.75rem; padding: 4px 8px; border-radius: 9999px; }
.card__badge--popular { background: #f59e0b; color: white; }

.btn { display: inline-block; padding: 8px 16px; border-radius: 6px; }
.btn--primary { background: #4f46e5; color: white; }
.btn--large { padding: 12px 24px; font-size: 1.1rem; }
```

---

## 🎯 Aufgabenstellung in `aufgabe.html`

- **TEILZIEL 1**: Stylinge den Block `.pricing-card` und seine Elemente `.pricing-card__header`, `.pricing-card__title`, `.pricing-card__price`, `.pricing-card__features` und `.pricing-card__footer`.
- **TEILZIEL 2**: Implementiere den Block-Modifier `.pricing-card--popular` mit markanter Randfarbe (`border-color: #8b5cf6`), Glow-Schatten und Transform.
- **TEILZIEL 3**: Stylinge den Button-Block `.btn` sowie die Modifiers `.btn--primary` und `.btn--outline`.
- **TEILZIEL 4**: Stylinge das Badge-Element `.pricing-card__badge` und den Modifier `.pricing-card__badge--highlight`.

Teste deine BEM-Architektur mit `test_aufgabe.js`!
