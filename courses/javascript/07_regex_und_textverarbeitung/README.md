# 🌐 JS 07: Reguläre Ausdrücke & Textverarbeitung

Willkommen zu **Modul 07** des JavaScript-Kurses! In diesem Modul lernst du die Kunst des **Pattern Matchings** und der **Textanalyse** mit Regulären Ausdrücken (RegExp).

---

## 🎯 Lernziele

Nach diesem Modul kannst du:
1. **Reguläre Ausdrücke (RegExp)** in JavaScript sowohl als Literal (`/muster/flags`) als auch über den Konstruktor (`new RegExp(...)`) erstellen.
2. **Flags** wie `g` (global), `i` (case-insensitive) und `m` (multiline) gezielt steuern.
3. **Metazeichen** (`\d`, `\w`, `\s`, `.`, `^`, `$`) und **Quantifizierer** (`+`, `*`, `?`, `{min,max}`) souverän kombinieren.
4. Strings mit **`regex.test()`** validieren und mit **`str.match()`** Fundstellen extrahieren.
5. Texte mit **`str.replace()`** und **Capturing Groups (`$1`, `$2`)** formatieren und sensible Daten maskieren.
6. Komplexe Validierungsregeln wie **Passwort- und E-Mail-Prüfungen** sauber umsetzen.

---

## 💡 Theoretische Grundlagen

### 1. Die zwei Wege zur RegExp-Erstellung

```javascript
// 1. Literal (schnell, statisch kompiliert, Standardfall):
const regexLiteral = /^[A-Z][a-z]+$/;

// 2. RegExp-Objekt (dynamisch, erlaubt Variablen im Suchmuster):
const userKeyword = "admin";
const regexDynamic = new RegExp(`^${userKeyword}$`, "i");
```

### 2. Metazeichen-Übersicht

| Metazeichen | Bedeutung | Beispiel-Treffer |
| :--- | :--- | :--- |
| `\d` | Ziffer (0-9) | `"5"`, `"9"` |
| `\D` | Keine Ziffer | `"a"`, `"!"` |
| `\w` | Wortzeichen (`[a-zA-Z0-9_]`) | `"x"`, `"7"`, `"_"` |
| `\W` | Kein Wortzeichen | `" "`, `"@"`, `"-"` |
| `\s` | Whitespace (Leerzeichen, Tab, Umbruch) | `" "`, `"\t"`, `"\n"` |
| `.` | Beliebiges Zeichen (außer Umbruch) | `"a"`, `"8"`, `"%"` |
| `^` | Textanfang | `/^Start/` |
| `$` | Textende | `/Ende$/` |

### 3. Quantifizierer (Häufigkeiten)

| Quantifizierer | Bedeutung | Beispiel |
| :--- | :--- | :--- |
| `+` | Mindestens 1 Mal (1 bis unendlich) | `\d+` matcht `"1234"` |
| `*` | 0 bis unendlich (optional) | `a*` matcht `""` oder `"aaa"` |
| `?` | 0 oder 1 Mal (optional) | `https?` matcht `"http"` & `"https"` |
| `{n}` | Exakt `n` Mal | `\d{4}` matcht `"2024"` |
| `{min,max}` | Zwischen `min` und `max` Mal | `\d{2,4}` |
| `{min,}` | Mindestens `min` Mal | `.{8,}` (mind. 8 Zeichen) |

### 4. Capturing Groups & Maskierung mit `replace`

Runde Klammern `( ... )` bilden Gruppen. Im Ersetzungs-String kann mit `$1`, `$2` usw. darauf zugegriffen werden:

```javascript
// Telefonnummer formatieren:
const nummer = "01711234567";
const formatiert = nummer.replace(/(\d{4})(\d+)/, "$1-$2");
console.log(formatiert); // "0171-1234567"
```

---

## 🕵️ Didaktische Analogie: Der Muster-Detektiv & Schablonen-Scanner

Ein Regulärer Ausdruck ist wie ein **Röntgengerät mit Lochmaske**:
- Du legst das Dokument (den Fließtext) auf den Scanner.
- Die Lochmaske blendet alle irrelevanten Wörter aus.
- Nur Abschnitte, die exakt in die Aussparungen passen (z. B. 4er-Zahlenblöcke für Kreditkarten oder das `@`-Zeichen mit Domain), leuchten grün auf.

---

## 🎯 Aufgabenübersicht in `aufgabe.js`

1. **TODO 1: `istGueltigeEmail(email)`**:
   - Prüft E-Mails auf das Format `name@domain.tld` (mind. 2-stellige TLD).
2. **TODO 2: `findeTelefonnummern(text)`**:
   - Findet Telefonnummern wie `+49 170 1234567`, `0171-1234567` etc.
3. **TODO 3: `extrahiereHashtags(text)`**:
   - Findet alle Social-Media-Tags (`#hashtag`).
4. **TODO 4: `maskiereKreditkarte(text)`**:
   - Anonymisiert 16-stellige Kreditkartennummern zu `****-****-****-1234`.
5. **TODO 5: `istStarkesPasswort(passwort)`**:
   - Prüft Passwortstärke (mind. 8 Zeichen, Klein-, Großbuchstaben, Ziffer, Sonderzeichen).

---

## 🧪 Tests ausführen

Führe die Testsuite in der Web-IDE oder lokal aus:
```bash
# In der Web-IDE: Klicke auf 'Code ausführen & testen'
```
