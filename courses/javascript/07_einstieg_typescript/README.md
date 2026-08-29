# 🛡️ Modul 07: TypeScript Type Safety & Interfaces

> **Leitgedanke:** *„TypeScript ist wie ein digitaler Sicherheitsgurt und ein unbestechlicher Bauplan-Wächter: Fehler werden bereits während der Entwicklung im Editor erkannt – und nicht erst nachts beim Kunden auf der Website!“*

---

## 📚 Übersicht & Lernziele

In diesem Modul machst du den entscheidenden Schritt von dynamischem JavaScript hin zur **statischen Typsicherheit mit TypeScript**:

1. **Warum TypeScript?** – Verstehe den Unterschied zwischen Laufzeit- und Compile-Time-Fehlern.
2. **Basis-Datentypen** – `string`, `number`, `boolean`, `string[]`, `any`, `unknown`, `void`.
3. **Type Aliases & Union Types** – Flexible Kombinationen wie `type ID = string | number;`.
4. **Interfaces & Optionale Eigenschaften** – Strukturverträge mit `interface` und `?`.
5. **Generics (`<T>`)** – Wiederverwendbare, typsichere Algorithmen und Hilfsfunktionen.
6. **Optional Chaining (`?.`) & Nullish Coalescing (`??`)** – Sichere Zugriffe ohne `Cannot read properties of undefined`.

---

## 💡 1. Die didaktische Analogie: Der Bauplan-Wächter

| Klassisches JavaScript ⚡ | TypeScript mit Interfaces 🛡️ |
| :--- | :--- |
| **Baustelle ohne Plan:** Man baut drauflos. Ob ein Stein passt oder eine tragende Wand fehlt, merkt man erst, wenn das Haus einstürzt (Laufzeit-Crash beim Kunden). | **Architekten-Bauplan mit TÜV-Prüfung:** Jede Schnittstelle, jeder Balken und jedes Kabel ist exakt typisiert. Passt ein Element nicht, schlägt der Compiler sofort Alarm. |

---

## 🔍 2. TypeScript Kernkonzepte im Detail

### A. Basis-Datentypen

```typescript
// Explizite Typ-Annotationen
const benutzername: string = "Anna_Dev";
const alter: number = 28;
const istAdmin: boolean = true;

// Arrays
const tags: string[] = ["typescript", "frontend", "web"];
const noten: Array<number> = [1, 2, 1, 3];

// Spezialtypen: any vs. unknown vs. void
let beliebig: any = "Kann alles sein (Typ-Check deaktiviert)";
let unsicher: unknown = JSON.parse('{"status": "ok"}'); // Erfordert Typprüfung vor Nutzung!

function loggeNachricht(msg: string): void {
  console.log(`[LOG]: ${msg}`);
  // Kein Return-Wert -> void
}
```

### B. Type Aliases & Union Types

Mit Union Types (`|`) können Variablen mehrere definierte Typen annehmen:

```typescript
// Type Alias für eindeutige Identifikatoren
type ID = string | number;

// Literal-Union-Type für feste Status-Werte
type AuftragsStatus = "offen" | "in_bearbeitung" | "abgeschlossen" | "storniert";

let meineId: ID = 42;
meineId = "USR-9921"; // ✅ Beides absolut gültig!
```

### C. Interfaces (Objekt-Verträge)

Ein Interface definiert die exakte Form eines JavaScript-Objekts. Mit dem Fragezeichen `?` werden Felder als optional markiert:

```typescript
interface User {
  id: ID;
  name: string;
  istAktiv: boolean;
  email?: string;       // ❓ Optional: Kann vorhanden sein oder undefined
  erstelltAm: string;
}

const kunde1: User = {
  id: 101,
  name: "Max Mustermann",
  istAktiv: true,
  erstelltAm: "2026-08-30T00:00:00.000Z"
};
```

### D. Generics (`<T>` – Typ-Parameter)

Generics erlauben es, Funktionen und Klassen zu schreiben, die mit beliebigen Datentypen arbeiten, dabei aber die volle Typsicherheit behalten:

```typescript
// Generische Umkehrfunktion für Arrays
function umkehren<T>(liste: T[]): T[] {
  return [...liste].reverse();
}

const zahlenUmgekehrt = umkehren<number>([1, 2, 3, 4]); // Typ: number[]
const worteUmgekehrt = umkehren<string>(["A", "B", "C"]); // Typ: string[]
```

### E. Optional Chaining (`?.`) & Nullish Coalescing (`??`)

```typescript
interface Profil {
  avatar?: {
    url?: string;
  };
}

const user: Profil = {};

// Sicherer Zugriff ohne Absturz:
const avatarUrl = user?.avatar?.url ?? "default_avatar.png";
console.log(avatarUrl); // -> "default_avatar.png"
```

---

## 🎯 3. Deine Aufgaben in `aufgabe.js`

Implementiere die folgenden 4 Kernfunktionen:

### 🎯 TODO 1: `erstelleKunde(id, name, istAktiv = true, email = null)`
- Erzeugt ein valides Kunden-Objekt `{ id, name, istAktiv, [email], erstelltAm }`.
- Wirft einen `TypeError`, wenn `id` weder `string` noch `number` ist, oder wenn `name` leer ist.
- Säubert den Namen mit `.trim()`.

### 🎯 TODO 2: `validiereAuftrag(auftragObjekt)`
- Validiert ein übergebenes Auftrag-Objekt gegen das `Auftrag`-Interface.
- Prüft `id`, `kundeId`, `positionen` (Array mit mind. 1 Element, validen Mengen > 0 & Einzelpreisen >= 0), `summe` (>= 0) und `status` ('offen', 'in_bearbeitung', 'abgeschlossen', 'storniert').
- Liefert `{ gueltig: boolean, fehler: string[] }`.

### 🎯 TODO 3: `filtereNachStatus(eintraege, zielStatus)`
- Generische Hilfsfunktion: Filtert ein Array von Objekten nach `item.status === zielStatus`.
- Liefert bei ungültigen Eingaben sicher ein leeres Array `[]`.

### 🎯 TODO 4: `formatierePreisangabe(betrag, waehrung = "EUR")`
- Formatiert Zahlen typsicher im deutschen Währungsformat (z.B. `49.99` -> `"49,99 EUR"`).
- Wirft bei ungültigen Beträgen (z.B. Strings, `NaN`) oder leeren Währungen einen `TypeError`.

---

## 🧪 4. Selbstüberprüfung

Führe die Unittests in der Web-IDE oder im Test-Runner aus:

- ✅ 1. Kunden-Erstellung mit Standardwerten & Fehlervalidierung.
- ✅ 2. Vollständige Auftragsvalidierung mit Fehler-Reporting.
- ✅ 3. Generischer Statusfilter.
- ✅ 4. Typsichere Preis- und Währungsformatierung.
