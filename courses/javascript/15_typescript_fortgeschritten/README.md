# TS 15: Fortgeschrittenes TypeScript & Generics 🛡️

Willkommen zu **Modul 15** des JavaScript- & TypeScript-Kurses!

Einfache Typen wie `string` oder `number` reichen für elementare Skripte aus. In professionellen Enterprise-Anwendungen benötigst du jedoch **generische Container**, **Typ-Wächter (Type Guards)**, **Enums** und **Utility Types**, um hochflexible und dennoch zu 100 % typsichere Architekturen zu bauen.

---

## 💡 1. Das Wichtigste in Kürze

### A. Generics (`<T>`): Wiederverwendbare Typen
Statt Code für jeden Datentyp zu duplizieren oder `any` zu verwenden, nutzt du **Generics** als Typ-Platzhalter:

```typescript
// Generisches Interface für paginierte REST-API Antworten:
interface PaginiertesErgebnis<T> {
  items: T[];
  total: number;
  page: number;
  pageSize: number;
  totalPages: number;
  hasNextPage: boolean;
  hasPrevPage: boolean;
}

// Verwendung:
const benutzerSeite: PaginiertesErgebnis<Benutzer> = erstellePaginiertesErgebnis(users, 100, 1, 10);
const produktSeite: PaginiertesErgebnis<Produkt> = erstellePaginiertesErgebnis(products, 50, 2, 20);
```

---

### B. Custom Type Guards (`obj is Type`)
Mit einem Type Guard teilst du dem TypeScript-Compiler mit, dass ein Objekt nach einer erfolgreichen Laufzeitprüfung einem bestimmten Typ entspricht:

```typescript
function istAdminBenutzer(obj: any): obj is AdminBenutzer {
  return (
    obj !== null &&
    typeof obj === "object" &&
    typeof obj.username === "string" &&
    obj.rolle === "ADMIN" &&
    Array.isArray(obj.berechtigungen) &&
    obj.berechtigungen.length > 0
  );
}

// In der Anwendung (TypeScript narrowed den Typ automatisch):
if (istAdminBenutzer(aktuellerUser)) {
  console.log(aktuellerUser.berechtigungen.join(", ")); // ✅ Sicher, kein any!
}
```

---

### C. Enums: Typisierte Konstanten
Enums bündeln eine feste Menge zusammengehöriger Werte und verhindern Tippfehler:

```typescript
enum BenutzerRolle {
  ADMIN = "ADMIN",
  USER = "USER",
  GAST = "GAST"
}

enum TaskStatus {
  TODO = "TODO",
  IN_PROGRESS = "IN_PROGRESS",
  DONE = "DONE"
}
```

---

### D. TypeScript Utility Types
TypeScript bietet eingebaute Werkzeuge zur Transformation bestehender Typen:

| Utility Type | Syntax | Bedeutung |
| :--- | :--- | :--- |
| **`Partial<T>`** | `Partial<Benutzer>` | Macht alle Eigenschaften von `T` optional (ideal für Updates/PATCH-Requests). |
| **`Readonly<T>`** | `Readonly<Konfiguration>` | Verhindert nachträgliche Veränderungen von Eigenschaften. |
| **`Pick<T, K>`** | `Pick<Benutzer, "id" \| "email">` | Wählt eine Teilmenge bestimmter Eigenschaften aus `T` aus. |
| **`Omit<T, K>`** | `Omit<Benutzer, "passwortHash">` | Entfernt sensible Eigenschaften aus `T`. |
| **`Record<K, T>`** | `Record<string, number>` | Erstellt ein Dictionary/Map mit Schlüsseln vom Typ `K` und Werten vom Typ `T`. |

---

## 🩻 Die didaktische Analogie: "Der Hightech-Röntgenapparat & der Präzisions-Maßanzug"

- **`any` ist die Augenbinde:**  
  Man ignoriert alle Gefahren und hofft, dass auf der Baustelle nichts schiefgeht.
- **Generics (`<T>`) sind wie maßgeschneiderte Transportbehälter:**  
  Ein Behälter mit Schutzpolsterung für Gläser transportiert Gläser bruchsicher. Dasselbe Design transportiert Goldbarren. Der Inhalt bleibt exakt typisiert, ohne dass der Behälter den Inhalt beschädigt.
- **Type Guards sind der Hightech-Röntgenapparat am Flughafen:**  
  Jedes Gepäckstück (unbekannte Daten) wird an der Schleuse durchleuchtet. Nur wenn alle Kriterien (ID, Admin-Rolle, Berechtigungen) einwandfrei erkannt werden, öffnet die Schranke in den VIP-Bereich.
- **Utility Types (`Partial`, `Pick`) sind die Schneiderwerkzeuge:**  
  Du hast einen kompletten Maßanzug (Großes Interface) und schneidest daraus für den Sommer präzise eine Weste (`Pick`) oder machst die Knöpfe flexibel verstellbar (`Partial`).

---

## 🎯 Aufgaben & Teilziele in `aufgabe.js`

1. **TODO 1:** `erstellePaginiertesErgebnis(items, total, page = 1, pageSize = 10)`  
   Erstelle einen generischen Container `<T>` mit Berechnung von `totalPages`, `hasNextPage` und `hasPrevPage`.
2. **TODO 2:** `istAdminBenutzer(benutzerObjekt)`  
   Implementiere einen Custom Type Guard, der ID, Username, Email, Admin-Rolle und Berechtigungs-Array prüft.
3. **TODO 3:** `aktualisiereBenutzerProfil(original, partiellesUpdate)`  
   Führe ein partielles Update (`Partial<T>`) mit Validierung durch, ohne das Original zu mutieren (Immutability).
4. **TODO 4:** `filtriereFelder(objekt, erlaubteSchluessel)`  
   Filtere die Eigenschaften eines Objekts (`Pick<T, K>`) und ignoriere nicht vorhandene Schlüssel.

---

## 🧪 Tests ausführen

Öffne die Web-IDE oder führe die Unittests aus. Sobald alle 22 Tests grün sind, beherrschst du TypeScript auf Profi-Niveau!
