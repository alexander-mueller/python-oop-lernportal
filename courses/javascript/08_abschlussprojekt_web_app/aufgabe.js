/**
 * 🌐 MASTER 08: INTERAKTIVE TASK-APP (STATE & BUSINESS LOGIC) 🌐
 * ===============================================================
 * In diesem Master-Abschlussprojekt erstellst du die vollständige
 * Geschäftslogik (Model & State Manager) für eine interaktive
 * Aufgabenverwaltungs-Web-App mit sauberer Model-View Trennung.
 */

/**
 * @typedef {'high' | 'medium' | 'low'} TaskPriority
 * @typedef {'all' | 'active' | 'completed'} FilterStatus
 * 
 * @typedef {Object} Task
 * @property {number} id - Eindeutige numerische ID
 * @property {string} title - Titel der Aufgabe
 * @property {TaskPriority} priority - Priorität ('high', 'medium', 'low')
 * @property {boolean} completed - Erledigungsstatus
 * @property {string | null} dueDate - Optionales Fälligkeitsdatum (z.B. '2026-12-31')
 * @property {string} createdAt - ISO-Datumsstring
 * 
 * @typedef {Object} TaskStatistics
 * @property {number} total - Gesamtzahl aller Aufgaben
 * @property {number} active - Anzahl aktiver (unerledigter) Aufgaben
 * @property {number} completed - Anzahl erledigter Aufgaben
 * @property {number} highPriorityCount - Anzahl Aufgaben mit Priorität 'high'
 */

class TaskManager {
  constructor(initialTasks = []) {
    /** @type {Task[]} */
    this.tasks = [];
    this.nextId = 1;

    // TODO: Initialisiere das Array und lade eventuelle initialTasks
  }

  /**
   * 🎯 TEILZIEL 1 (TODO 1): addTask(title, priority = 'medium', dueDate = null)
   * Fügt eine neue Aufgabe hinzu.
   * 
   * Anforderungen:
   * - title: string (nach .trim() nicht leer, sonst Error werfen)
   * - priority: 'high' | 'medium' | 'low' (Standard: 'medium')
   * - dueDate: string | null (Standard: null)
   * - completed: initial false
   * - createdAt: new Date().toISOString()
   * - Vergibt eine eindeutige, inkrementierte ID (1, 2, 3, ...)
   * - Gibt das erstellte Task-Objekt zurück.
   * 
   * @param {string} title
   * @param {TaskPriority} [priority='medium']
   * @param {string | null} [dueDate=null]
   * @returns {Task}
   */
  addTask(title, priority = "medium", dueDate = null) {
    // TODO: Neue Aufgabe erstellen und im tasks-Array speichern
    return null;
  }

  /**
   * 🎯 TEILZIEL 2 (TODO 2): toggleTask(id)
   * Schaltet den completed-Status der Aufgabe mit der übergebenen ID um (true <-> false).
   * 
   * Anforderungen:
   * - Findet die Aufgabe anhand der ID.
   * - Schaltet task.completed um.
   * - Gibt den aktualisierten Task zurück, oder null falls ID nicht existiert.
   * 
   * @param {number} id
   * @returns {Task | null}
   */
  toggleTask(id) {
    // TODO: Status umschalten
    return null;
  }

  /**
   * 🎯 TEILZIEL 3 (TODO 3): deleteTask(id)
   * Entfernt eine Aufgabe anhand ihrer ID.
   * 
   * Anforderungen:
   * - Entfernt die Aufgabe aus this.tasks.
   * - Gibt true zurück wenn gelöscht wurde, sonst false wenn ID nicht vorhanden war.
   * 
   * @param {number} id
   * @returns {boolean}
   */
  deleteTask(id) {
    // TODO: Aufgabe löschen
    return false;
  }

  /**
   * 🎯 TEILZIEL 4 (TODO 4): getFilteredTasks(filterStatus = 'all', searchQuery = '')
   * Liefert gefilterte Aufgaben basierend auf Status und optionalem Suchbegriff.
   * 
   * Anforderungen:
   * - filterStatus:
   *     - 'all': Alle Aufgaben
   *     - 'active': Nur Aufgaben mit completed === false
   *     - 'completed': Nur Aufgaben mit completed === true
   * - searchQuery: Filtert zusätzlich case-insensitive nach Teilübereinstimmung im title (wenn nicht leer)
   * - Liefert eine neue Array-Kopie der gefilterten Aufgaben zurück.
   * 
   * @param {FilterStatus} [filterStatus='all']
   * @param {string} [searchQuery='']
   * @returns {Task[]}
   */
  getFilteredTasks(filterStatus = "all", searchQuery = "") {
    // TODO: Filtern nach Status und Volltextsuche
    return [];
  }

  /**
   * 🎯 TEILZIEL 5 (TODO 5): getStatistics()
   * Berechnet Aggregat-Statistiken über alle Aufgaben.
   * 
   * Anforderungen:
   * - total: Gesamtzahl aller Aufgaben
   * - active: Anzahl noch nicht erledigter Aufgaben
   * - completed: Anzahl erledigter Aufgaben
   * - highPriorityCount: Anzahl aller Aufgaben mit priority === 'high'
   * 
   * @returns {TaskStatistics}
   */
  getStatistics() {
    // TODO: Statistiken berechnen
    return {
      total: 0,
      active: 0,
      completed: 0,
      highPriorityCount: 0
    };
  }

  /**
   * Hilfsmethode: Findet eine Aufgabe nach ID
   * @param {number} id
   * @returns {Task | null}
   */
  getTaskById(id) {
    const numId = Number(id);
    return this.tasks.find(t => t.id === numId) || null;
  }
}
