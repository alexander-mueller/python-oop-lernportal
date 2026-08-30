# CSS 05: Selektoren, Kaskade & Spezifität 🎨

Willkommen in **Modul 05** und dem Einstieg in **Lehrpfad 2: Modern CSS3 Styling**!

In dieser Lerneinheit meisterst du CSS-Selektoren, Kombinatoren, Pseudo-Klassen und verstehst das Spezifitätsmodell der Kaskade.

---

## 💡 1. Das Wichtigste in Kürze

### Selektoren & Spezifitäts-Wertung
1. **Typ-Selektoren** (`h1`, `p`, `div`): Wert `0-0-1`.
2. **Klassen-, Attribut- und Pseudo-Klassen-Selektoren** (`.card`, `[type="text"]`, `:hover`, `:nth-child`): Wert `0-1-0`.
3. **ID-Selektoren** (`#header`, `#main`): Wert `1-0-0`.
4. **Inline-Styles** (`style="..."`): Wert `1-0-0-0`.

### Kombinatoren
- `A B` (Nachfahre): Alle `B` innerhalb von `A`.
- `A > B` (Kind): Nur direkte Kinder `B` von `A`.
- `A + B` (Direkter Nachbar): `B` direkt nach `A`.
- `A ~ B` (Allgemeiner Nachbar): Alle `B` nach `A` auf gleicher Ebene.

---

## 🎯 Teilziele in `aufgabe.html`

1. **Typ-Selektoren**: Style `body` und `h1`.
2. **Klasse & ID**: Style `.card` und die spezielle `#featured-card`.
3. **Kombinatoren**: Wende `ul > li` und `h2 + p` an.
4. **Attribut-Selektor**: Style Links mit `a[target="_blank"]`.
5. **Pseudo-Klassen**: Ergänze `.btn:hover` und `li:nth-child(even)`.
