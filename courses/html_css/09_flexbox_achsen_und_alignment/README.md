# CSS 09: Flexbox Achsen, Justify & Align (1D-Layouts)

Willkommen im 3. Lehrpfad! In diesem Modul lernst du das **Flexible Box Layout (Flexbox)** kennen. Flexbox ist der moderne Standard für eindimensionale Layouts (Reihen oder Spalten) im Web.

---

## 🎯 Lernziele

1. **Flex-Container & Achsen verstehen**: Hauptachse (*Main Axis*) vs. Querachse (*Cross Axis*).
2. **Ausrichtung steuern**: `justify-content` (Hauptachse) und `align-items` / `align-self` (Querachse).
3. **Umbruch & Abstände**: `flex-wrap: wrap` und moderner `gap`-Abstand.
4. **Item-Verhalten berechnen**: `flex-grow`, `flex-shrink` und `flex-basis` (Kurzform `flex: 1 1 280px`).
5. **Praxisnahe UIs bauen**: Responsive Navigationsleisten und flexible Kartengitter.

---

## 🧠 Die Kernkonzepte im Detail

### 1. Das Achsensystem von Flexbox

Ein Element wird zum Flex-Container durch:
```css
.container {
  display: flex;
  flex-direction: row; /* Standard: von links nach rechts */
}
```

- **`flex-direction: row`**: Hauptachse ist horizontal (links nach rechts). Querachse ist vertikal (oben nach unten).
- **`flex-direction: column`**: Hauptachse ist vertikal (oben nach unten). Querachse ist horizontal (links nach rechts).

---

### 2. Ausrichtung auf der Hauptachse (`justify-content`)

`justify-content` steuert, wie überschüssiger Platz entlang der **Hauptachse** verteilt wird:

| Wert | Wirkung |
| :--- | :--- |
| `flex-start` | Elemente linksbündig / am Anfang der Achse |
| `center` | Elemente horizontal zentriert |
| `flex-end` | Elemente rechtsbündig / am Ende der Achse |
| `space-between` | Erstes Item ganz links, letztes ganz rechts, Zwischenräume gleichmäßig verteilt |
| `space-around` | Gleichmäßiger Abstand um jedes Element herum |
| `space-evenly` | Exakt gleicher Abstand zwischen allen Elementen und den Rändern |

```css
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
```

---

### 3. Ausrichtung auf der Querachse (`align-items` & `align-self`)

`align-items` bestimmt die Ausrichtung aller Kindelemente entlang der **Querachse**:

- `stretch` *(Standard)*: Elemente dehnen sich auf volle Containerhöhe aus.
- `center`: Elemente werden auf der Querachse mittig zentriert.
- `flex-start`: Am oberen Rand ausgerichtet.
- `flex-end`: Am unteren Rand ausgerichtet.
- `baseline`: An der Text-Grundlinie ausgerichtet.

Ein einzelnes Item kann diese Regel mit `align-self` überschreiben:
```css
.badge-special {
  align-self: flex-start;
}
```

---

### 4. Flex-Wrap und Gap

Standardmäßig quetscht Flexbox alle Elemente in eine einzige Zeile (`flex-wrap: nowrap`). Mit `flex-wrap: wrap` dürfen Elemente umbrechen:

```css
.card-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 24px; /* Gleichmäßiger Abstand zwischen Zeilen und Spalten */
}
```

---

### 5. Flex-Item Wachstumslogik (`flex: grow shrink basis`)

Jedes Kind-Element kann steuern, wie es bei Platzmangel schrumpft oder bei Platzüberschuss wächst:

- `flex-grow: 1`: Nimmt anteilig freien Platz ein.
- `flex-shrink: 1`: Darf bei Platzmangel schrumpfen.
- `flex-basis: 280px`: Ideale Startbreite vor dem Wachsen/Schrumpfen.

Kurzschreibweise:
```css
.card {
  flex: 1 1 280px; /* grow shrink basis */
}
```

---

## 🎯 Aufgabenstellung in `aufgabe.html`

Vervollständige die Stylesheet-Regeln in `aufgabe.html`:

- **TEILZIEL 1**: Stylinge `.navbar` als Flex-Container mit `justify-content: space-between` und `align-items: center`.
- **TEILZIEL 2**: Stylinge `.nav-links` als horizontale Flex-Liste mit `gap: 20px`, `align-items: center` und ohne Aufzählungszeichen.
- **TEILZIEL 3**: Stylinge `.card-container` mit `display: flex`, `flex-wrap: wrap` und `gap: 24px`.
- **TEILZIEL 4**: Setze für `.flex-card` die Kurzform `flex: 1 1 280px` und inneres Flex-Spaltenlayout (`flex-direction: column`, `justify-content: space-between`).
- **TEILZIEL 5**: Richte das Badge `.card__badge` mit `align-self: flex-start` oben links aus.

Teste deinen Code mit `test_aufgabe.js` oder direkt im Web-Workspace!
