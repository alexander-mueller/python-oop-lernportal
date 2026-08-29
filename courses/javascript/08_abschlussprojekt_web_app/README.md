# 🏆 Modul 08: Master-Abschlussprojekt – Interaktive Task-App (MVC)

> **Leitgedanke:** *„Ein wahrer Software-Engineer zeichnet sich nicht nur dadurch aus, einzelne Funktionen zu schreiben, sondern komplexe Systeme mit klarer Model-View-Architektur, State-Management und 100% testgetriebener Logik zu strukturieren.“*

---

## 📚 Übersicht & Projektziel

Herzlichen Glückwunsch zum Erreichen des **Master-Abschlussprojekts** des JavaScript & TypeScript Kurses! In diesem Abschlussprojekt entwickelst du eine vollständige, professionelle Aufgaben- und Projektmanagement-Web-Applikation.

### Kernanforderungen:
1. **Saubere Model-View-Trennung (MVC / Clean Architecture)**:
   - Die Geschäftslogik (`TaskManager`) ist zu 100% unabhängig vom DOM und läuft headless in jedem Test-Runner.
   - Die View (`TaskApp`) reagiert reaktiv auf State-Änderungen und visualisiert Tasks mit Prioritäts-Badges und Fälligkeitsdaten.
2. **Umfassende Aufgabenverwaltung**:
   - Aufgaben hinzufügen mit Titel, Priorität (`high`, `medium`, `low`) und Fälligkeitsdatum (`dueDate`).
   - Status umschalten (Toggle: Offen <-> Erledigt).
   - Aufgaben löschen und abgeschlossene Aufgaben gesammelt aufräumen.
   - Dynamische Filterung (`all`, `active`, `completed`) und Volltextsuche (Live Search).
   - Aggregat-Statistiken in Echtzeit (Gesamtzahl, Offen, Erledigt, Hohe Priorität).
3. **100% Unittest-Abdeckung** mit automatisierter Testsuite.

---

## 🏛️ 1. Architektur: Model-View-Controller (MVC)

```
┌─────────────────────────────────────────────────────────────┐
│                    BENUTZER / BROWSER UI                    │
└──────────────────────────────┬──────────────────────────────┘
                               │ Klick / Formular-Eingabe
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                   VIEW / CONTROLLER (app.js)                │
│  - Reagiert auf DOM-Events (submit, click, input)           │
│  - Aktualisiert das DOM bei State-Änderungen                │
│  - Formatiert UI-Elemente (Badges, Datumsanzeige)           │
└──────────────────────────────┬──────────────────────────────┘
                               │ Ruft Methoden auf
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                 MODEL / STATE (TaskManager)                 │
│  - addTask(title, priority, dueDate)                        │
│  - toggleTask(id)                                           │
│  - deleteTask(id)                                           │
│  - getFilteredTasks(status, query)                          │
│  - getStatistics()                                          │
└─────────────────────────────────────────────────────────────┘
```

---

## 📐 2. TypeScript Datenmodell & Interfaces

```typescript
type TaskPriority = "high" | "medium" | "low";
type FilterStatus = "all" | "active" | "completed";

interface Task {
  id: number;
  title: string;
  priority: TaskPriority;
  completed: boolean;
  dueDate: string | null;
  createdAt: string;
}

interface TaskStatistics {
  total: number;
  active: number;
  completed: number;
  highPriorityCount: number;
}
```

---

## 🎯 3. Deine Aufgaben in `aufgabe.js`

Implementiere die Klasse `TaskManager`:

### 🎯 TODO 1: `constructor(initialTasks = [])` & `addTask(title, priority = 'medium', dueDate = null)`
- Erzeugt eine neue Aufgabe mit fortlaufender ID (1, 2, 3, ...).
- Validiert den Titel (muss ein nicht-leerer String sein; wirft sonst einen `Error`).
- Setzt Standardwerte für `priority` ('medium') und `dueDate` (null).
- Gibt das neu erstellte `Task`-Objekt zurück.

### 🎯 TODO 2: `toggleTask(id)`
- Schaltet `completed` für die Aufgabe mit der angegebenen ID um (`true` <-> `false`).
- Liefert den aktualisierten Task zurück, oder `null` falls die ID nicht gefunden wurde.

### 🎯 TODO 3: `deleteTask(id)`
- Entfernt die Aufgabe mit der ID aus der internen Liste.
- Gibt `true` bei erfolgreichem Löschen zurück, sonst `false`.

### 🎯 TODO 4: `getFilteredTasks(filterStatus = 'all', searchQuery = '')`
- Filtert nach Status: `'all'` (alle), `'active'` (nur unerledigte), `'completed'` (nur erledigte).
- Filtert optional case-insensitive nach Teilübereinstimmung im Titel (`searchQuery`).
- Gibt eine Kopie des gefilterten Arrays zurück.

### 🎯 TODO 5: `getStatistics()`
- Liefert ein Objekt mit `{ total, active, completed, highPriorityCount }`.

---

## 🧪 4. Verifikation & Ausführung

### Unittests ausführen:
Öffne das Modul in der integrierten Web-IDE oder führe `test_aufgabe.js` aus.

### Interaktive Browser-App testen:
Öffne `index.html` direkt im Browser, um die live gerenderte Task-App auszuprobieren!
