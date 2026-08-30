# CSS 10: CSS Grid 2D-Matrix & Template Areas (2D-Layouts)

CSS Grid Layout ist das mächtigste zweidimensionale Layout-System im Web. Während Flexbox für 1D-Reihen oder Spalten gedacht ist, erlaubt Grid die gleichzeitige Ausrichtung von Elementen in Zeilen **und** Spalten.

---

## 🎯 Lernziele

1. **2D-Matrix verstehen**: `display: grid`, Spaltendefinition mit `fr` (Fractional Unit) und `repeat()`.
2. **Responsive Grids ohne Media Queries**: `grid-template-columns: repeat(auto-fit, minmax(250px, 1fr))`.
3. **Benannte Bereiche (*Template Areas*)**: Visuelle Layout-Skizzen mit `grid-template-areas` und `grid-area`.
4. **Zellen überspannen**: `grid-column: span 2` und `grid-row: span 2`.
5. **Dashboard-Layouts**: Professionelle Anwendungs-Interfaces mit Sidebar, Header, Main und Widgets bauen.

---

## 🧠 Die Kernkonzepte im Detail

### 1. Der Grid-Container & Fractional Units (`fr`)

```css
.grid-container {
  display: grid;
  grid-template-columns: 200px 1fr 2fr; /* Feste Spalte, 1/3 Restplatz, 2/3 Restplatz */
  gap: 20px;                            /* Zeilen- und Spaltenabstand */
}
```

Die Einheit `fr` teilt den verfügbaren Platz nach Abzug aller festen Einheiten proportional auf.

---

### 2. Die magische Responsive-Formel: `repeat(auto-fit, minmax(...))`

Die wohl mächtigste Zeile in modernem CSS:
```css
.auto-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
}
```
- **`minmax(250px, 1fr)`**: Jedes Element ist mindestens 250px breit, darf aber gleichmäßig bis zu 1fr wachsen.
- **`auto-fit`**: Platziert so viele Spalten nebeneinander wie Platz vorhanden ist. Passt keine Spalte mehr hinein, bricht Grid automatisch um – **ganz ohne Media Queries**!

---

### 3. Benannte Template Areas (`grid-template-areas`)

Du kannst dein Layout wie eine ASCII-Grafik direkt in CSS skizzieren:

```css
.dashboard {
  display: grid;
  grid-template-columns: 240px 1fr;
  grid-template-rows: 60px 1fr 50px;
  grid-template-areas:
    "header  header"
    "sidebar main"
    "footer  footer";
  min-height: 100vh;
  gap: 16px;
}

.dash-header  { grid-area: header; }
.dash-sidebar { grid-area: sidebar; }
.dash-main    { grid-area: main; }
.dash-footer  { grid-area: footer; }
```

---

### 4. Zellen überspannen mit `grid-column` & `grid-row`

Ein Element kann mehrere Spalten oder Zeilen einnehmen:
```css
.widget-wide {
  grid-column: span 2; /* 2 Spalten breit */
}

.widget-tall {
  grid-row: span 2;    /* 2 Zeilen hoch */
}
```

---

## 🎯 Aufgabenstellung in `aufgabe.html`

- **TEILZIEL 1**: Stylinge `.dashboard-layout` mit `display: grid`, 2 Spalten (`250px 1fr`), 3 Zeilen (`auto 1fr auto`) und `gap: 20px`.
- **TEILZIEL 2**: Definiere `grid-template-areas` für Header, Sidebar, Main und Footer und weise den Elementen (`.dash-header`, `.dash-sidebar`, `.dash-main`, `.dash-footer`) ihr jeweiliges `grid-area` zu.
- **TEILZIEL 3**: Stylinge `.metrics-grid` mit `display: grid`, `repeat(auto-fit, minmax(200px, 1fr))` und `gap: 16px`.
- **TEILZIEL 4**: Lasse `.metric-card--featured` zwei Spalten überspannen (`grid-column: span 2`).
- **TEILZIEL 5**: Zentriere Inhalte in `.metric-card` mit `place-items: center` oder `align-items: center`.

Teste deine Lösung mit `test_aufgabe.js`!
