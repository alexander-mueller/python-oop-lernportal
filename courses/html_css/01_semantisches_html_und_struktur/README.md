# HTML 01: Semantisches HTML & Dokumentenstruktur 🌱

Willkommen im **Modul 01** des HTML5 & CSS3 Meisterkurses!

In diesem Modul lernst du, wie ein sauberes, valides HTML5-Dokument strukturiert wird und warum semantische Tags das Fundament moderner Webentwicklung, Barrierefreiheit (Accessibility) und Suchmaschinenoptimierung (SEO) bilden.

---

## 💡 1. Das Wichtigste in Kürze

### Grundgerüst eines HTML5-Dokuments
```html
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mein Portal</title>
</head>
<body>
  <!-- Sichtbarer Inhalt -->
</body>
</html>
```

### Semantische Landmark-Tags im Überblick
- `<header>`: Einleitender Bereich der Webseite (Logo, Webseitentitel, Slogan) oder eines Artikels.
- `<nav>`: Navigationsbereich mit Links (meist als `<ul>` mit `<li>` und `<a>`).
- `<main>`: Repräsentiert den zentralen Hauptinhalt. **Darf genau einmal pro HTML-Dokument vorkommen.**
- `<article>`: Eigenständiger, thematisch abgeschlossener Beitrag (z.B. Blogpost, News-Meldung, Produktkarte).
- `<section>`: Thematisch zusammenhängender Abschnitt, typischerweise mit einer eigenen Überschrift (`<h2>` bis `<h6>`).
- `<aside>`: Beistell-Inhalte, Sidebar, Autoren-Biografie, thematisch verwandte Linklisten.
- `<footer>`: Fußzeile mit Copyright-Vermerk, rechtlichen Hinweisen, Kontaktlinks.

---

## 🎯 Teilziele in `aufgabe.html`

1. **Doctype & Head**: Richte `<!DOCTYPE html>`, `<html lang="de">`, `<meta charset="UTF-8">`, `<meta name="viewport">` und `<title>` ein.
2. **Kopfbereich & Navigation**: Baue einen `<header>` mit `<h1>` und ein `<nav>`-Menü mit mindestens 3 Navigationslinks.
3. **Hauptinhalt & Artikel**: Erstelle ein `<main>`-Element mit einem `<article>`, der eine `<h2>`-Überschrift und Fließtext enthält.
4. **Sektion & Sidebar**: Ergänze innerhalb des Hauptbereichs eine `<section>` mit `<h3>` und eine `<aside>` für Zusatzinformationen.
5. **Fußzeile**: Erstelle ein `<footer>`-Element mit Copyright-Angabe (`&copy;`).
