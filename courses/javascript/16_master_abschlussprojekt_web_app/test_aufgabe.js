/**
 * 🧪 Testsuite für Master 08: Interaktive Task-App (TaskManager)
 */

function assertThrows(fn, msg) {
  let threw = false;
  try {
    fn();
  } catch (e) {
    threw = true;
  }
  assert.ok(threw, msg || "Erwarteter Fehler wurde nicht geworfen!");
}

// Instanz erzeugen
const manager = new TaskManager();

// ----------------------------------------------------
// 1. Tests für addTask(title, priority, dueDate)
// ----------------------------------------------------
const t1 = manager.addTask("TypeScript Typen & Interfaces lernen", "high", "2026-12-31");
assert.strictEqual(t1.id, 1, "Erste Aufgabe sollte ID 1 erhalten");
assert.strictEqual(t1.title, "TypeScript Typen & Interfaces lernen", "Titel korrekt");
assert.strictEqual(t1.priority, "high", "Priorität sollte 'high' sein");
assert.strictEqual(t1.completed, false, "Initialer Status muss completed: false sein");
assert.strictEqual(t1.dueDate, "2026-12-31", "Fälligkeitsdatum korrekt");
assert.ok(typeof t1.createdAt === "string", "createdAt muss gesetzt sein");

const t2 = manager.addTask("  CSS Design System verfeinern  ");
assert.strictEqual(t2.id, 2, "Zweite Aufgabe sollte ID 2 erhalten");
assert.strictEqual(t2.title, "CSS Design System verfeinern", "Titel muss getrimmt sein");
assert.strictEqual(t2.priority, "medium", "Standard-Priorität sollte 'medium' sein");
assert.strictEqual(t2.dueDate, null, "Ohne Fälligkeitsdatum sollte null gesetzt werden");

const t3 = manager.addTask("Unit Tests für State-Manager schreiben", "low");
assert.strictEqual(t3.id, 3, "Dritte Aufgabe sollte ID 3 erhalten");

const t4 = manager.addTask("Master Release v1.0 bereitstellen", "high", "2026-09-01");
assert.strictEqual(t4.id, 4, "Vierte Aufgabe sollte ID 4 erhalten");

// Validierung von fehlerhaftem Input
assertThrows(() => manager.addTask(""), "Leerer Titel muss Error werfen");
assertThrows(() => manager.addTask("   "), "Whitespace-Titel muss Error werfen");
assertThrows(() => manager.addTask(null), "null als Titel muss Error werfen");

// ----------------------------------------------------
// 2. Tests für toggleTask(id)
// ----------------------------------------------------
const toggled1 = manager.toggleTask(1);
assert.strictEqual(toggled1.completed, true, "Task 1 sollte nach erstem Toggle completed: true sein");

const toggledAgain = manager.toggleTask(1);
assert.strictEqual(toggledAgain.completed, false, "Task 1 sollte nach zweitem Toggle wieder completed: false sein");

const toggledNonExistent = manager.toggleTask(999);
assert.strictEqual(toggledNonExistent, null, "Toggle für unbekannte ID sollte null liefern");

// Für nachfolgende Tests Task 2 auf completed setzen
manager.toggleTask(2);

// ----------------------------------------------------
// 3. Tests für deleteTask(id)
// ----------------------------------------------------
const deleted = manager.deleteTask(3);
assert.strictEqual(deleted, true, "deleteTask(3) sollte true zurückgeben");
assert.strictEqual(manager.tasks.length, 3, "Nach Löschen sollten noch 3 Tasks vorhanden sein");

const deletedAgain = manager.deleteTask(3);
assert.strictEqual(deletedAgain, false, "Erneutes Löschen derselben ID sollte false liefern");

// ----------------------------------------------------
// 4. Tests für getFilteredTasks(filterStatus, searchQuery)
// ----------------------------------------------------
// Aktueller Zustand:
// - Task 1: "TypeScript ...", high, completed: false
// - Task 2: "CSS Design ...", medium, completed: true
// - Task 4: "Master Release ...", high, completed: false

const allTasks = manager.getFilteredTasks("all");
assert.strictEqual(allTasks.length, 3, "Filter 'all' sollte alle 3 Tasks liefern");

const activeTasks = manager.getFilteredTasks("active");
assert.strictEqual(activeTasks.length, 2, "Filter 'active' sollte 2 Tasks liefern");
assert.strictEqual(activeTasks[0].id, 1, "Erster aktiver Task");
assert.strictEqual(activeTasks[1].id, 4, "Zweiter aktiver Task");

const completedTasks = manager.getFilteredTasks("completed");
assert.strictEqual(completedTasks.length, 1, "Filter 'completed' sollte 1 Task liefern");
assert.strictEqual(completedTasks[0].id, 2, "Erledigter Task ID");

// Volltextsuche
const searchResult = manager.getFilteredTasks("all", "release");
assert.strictEqual(searchResult.length, 1, "Suche nach 'release' sollte Task 4 finden");
assert.strictEqual(searchResult[0].id, 4, "Gefundene Task-ID");

const searchCaseInsensitive = manager.getFilteredTasks("all", "TYPESCRIPT");
assert.strictEqual(searchCaseInsensitive.length, 1, "Suche sollte case-insensitive sein");

const searchEmpty = manager.getFilteredTasks("all", "NICHT_VORHANDEN_123");
assert.strictEqual(searchEmpty.length, 0, "Erfolglose Suche liefert leeres Array");

// ----------------------------------------------------
// 5. Tests für getStatistics()
// ----------------------------------------------------
const stats = manager.getStatistics();
assert.strictEqual(stats.total, 3, "Gesamtzahl Tasks");
assert.strictEqual(stats.active, 2, "Aktive Tasks");
assert.strictEqual(stats.completed, 1, "Erledigte Tasks");
assert.strictEqual(stats.highPriorityCount, 2, "Hohe Priorität Tasks (Task 1 & Task 4)");

console.log("✅ Alle Tests für Master 08 (Interaktive Task-App / TaskManager) erfolgreich bestanden!");
