# HTML 03: Formulare & HTML5-Validierung 📋

Willkommen in **Modul 03**!

In dieser Einheit baust du interaktive Eingabeformulare, verknüpfst barrierefreie Labels und nutzt native HTML5-Validierungsregeln.

---

## 💡 1. Das Wichtigste in Kürze

### Formular & Labels
- Jedes Eingabefeld benötigt ein `id`-Attribut und ein passendes `<label for="...">`.
- `<fieldset>` gruppiert logisch zusammenhängende Felder, `<legend>` liefert den Titel.

### Input-Typen
- `<input type="text">`: Einzeiliger Text.
- `<input type="email">`: E-Mail-Validierung.
- `<input type="password">`: Versteckte Passworteingabe.
- `<input type="number">`: Numerische Eingabe mit `min`, `max`, `step`.
- `<select>` & `<option>`: Dropdown-Auswahl.
- `<textarea>`: Mehrzeiliger Fließtext.

### Validierung ohne JavaScript
- `required`: Feld darf nicht leer sein.
- `minlength` / `maxlength`: Minimale / maximale Textlänge.
- `min` / `max`: Zahlen- und Datumslimits.
- `pattern`: Regex-Prüfung direkt im Browser.

---

## 🎯 Teilziele in `aufgabe.html`

1. **Form-Container**: Erstelle `<form action="/submit" method="POST">` mit `<fieldset>` und `<legend>`.
2. **Text & E-Mail**: Lege Input-Felder für Name und E-Mail mit verknüpften `<label for="...">` und `required` an.
3. **Passwort & Zahl**: Füge ein Passwort-Feld (`minlength="8"`) und ein Number-Feld (`min="1"`, `max="50"`) hinzu.
4. **Auswahl & Textarea**: Integriere `<select>` mit `<option>`-Einträgen und eine `<textarea>`.
5. **AGB & Submit**: Füge eine AGB-Checkbox (`required`) und `<button type="submit">` ein.
