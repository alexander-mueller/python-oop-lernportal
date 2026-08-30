# JS 01: Variablen, Typen & Template-Strings 🌱

Willkommen zu **Modul 01** des JavaScript-Kurses!

In diesem Modul lernst du die Grundlagen von modernen JavaScript-Variablen (`let`, `const`), Basis-Datentypen und Template-Strings (`${...}`) kennen.

---

## 💡 1. Das Wichtigste in Kürze

### `let` vs. `const`
- `const`: Für Werte, deren Bindung sich nicht ändert. Immer die Standard-Wahl!
- `let`: Für Variablen, deren Wert später neu zugewiesen wird (z.B. Zähler in Schleifen).
- `var`: Veraltet (ES5), bitte in modernem Code nicht mehr verwenden.

### Template-Strings
Mit Backticks (`` ` ``) kannst du Ausdrücke und Variablen direkt in Strings einbetten:
```javascript
const name = "Max";
const alter = 25;
const nachricht = `Hallo ${name}, du bist ${alter} Jahre alt.`;
```

---

## 🎯 Aufgaben in `aufgabe.js`

1. Deklariere die Konstante `KURS_NAME = "JavaScript Masterclass"`.
2. Erstelle Variablen für Name und Alter.
3. Formatiere einen Begrüßungssatz mit einem Template-String.
