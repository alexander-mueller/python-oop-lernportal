/**
 * 🌐 MASTER 08: INTERAKTIVE TASK-APP (MUSTERLÖSUNG) 🌐
 * ====================================================
 */

/**
 * @typedef {'high' | 'medium' | 'low'} TaskPriority
 * @typedef {'all' | 'active' | 'completed'} FilterStatus
 * 
 * @typedef {Object} Task
 * @property {number} id
 * @property {string} title
 * @property {TaskPriority} priority
 * @property {boolean} completed
 * @property {string | null} dueDate
 * @property {string} createdAt
 * 
 * @typedef {Object} TaskStatistics
 * @property {number} total
 * @property {number} active
 * @property {number} completed
 * @property {number} highPriorityCount
 */

class TaskManager {
  constructor(initialTasks = []) {
    /** @type {Task[]} */
    this.tasks = [];
    this.nextId = 1;

    if (Array.isArray(initialTasks)) {
      for (const t of initialTasks) {
        if (t && typeof t === "object") {
          const task = {
            id: typeof t.id === "number" ? t.id : this.nextId++,
            title: typeof t.title === "string" ? t.title.trim() : "Ohne Titel",
            priority: ["high", "medium", "low"].includes(t.priority) ? t.priority : "medium",
            completed: Boolean(t.completed),
            dueDate: (typeof t.dueDate === "string" && t.dueDate.trim().length > 0) ? t.dueDate.trim() : null,
            createdAt: t.createdAt || new Date().toISOString()
          };
          if (task.id >= this.nextId) {
            this.nextId = task.id + 1;
          }
          this.tasks.push(task);
        }
      }
    }
  }

  /**
   * 🎯 TEILZIEL 1: addTask(title, priority = 'medium', dueDate = null)
   */
  addTask(title, priority = "medium", dueDate = null) {
    if (typeof title !== "string" || title.trim().length === 0) {
      throw new Error("Aufgabentitel darf nicht leer sein");
    }

    const validPriority = ["high", "medium", "low"].includes(priority) ? priority : "medium";
    const normalizedDueDate = (typeof dueDate === "string" && dueDate.trim().length > 0) ? dueDate.trim() : null;

    const task = {
      id: this.nextId++,
      title: title.trim(),
      priority: validPriority,
      completed: false,
      dueDate: normalizedDueDate,
      createdAt: new Date().toISOString()
    };

    this.tasks.push(task);
    return task;
  }

  /**
   * 🎯 TEILZIEL 2: toggleTask(id)
   */
  toggleTask(id) {
    const numId = Number(id);
    const task = this.tasks.find(t => t.id === numId);
    if (!task) {
      return null;
    }
    task.completed = !task.completed;
    return task;
  }

  /**
   * 🎯 TEILZIEL 3: deleteTask(id)
   */
  deleteTask(id) {
    const numId = Number(id);
    const index = this.tasks.findIndex(t => t.id === numId);
    if (index === -1) {
      return false;
    }
    this.tasks.splice(index, 1);
    return true;
  }

  /**
   * 🎯 TEILZIEL 4: getFilteredTasks(filterStatus = 'all', searchQuery = '')
   */
  getFilteredTasks(filterStatus = "all", searchQuery = "") {
    let result = [...this.tasks];

    if (filterStatus === "active") {
      result = result.filter(t => !t.completed);
    } else if (filterStatus === "completed") {
      result = result.filter(t => t.completed);
    }

    if (typeof searchQuery === "string" && searchQuery.trim().length > 0) {
      const query = searchQuery.trim().toLowerCase();
      result = result.filter(t => t.title.toLowerCase().includes(query));
    }

    return result;
  }

  /**
   * 🎯 TEILZIEL 5: getStatistics()
   */
  getStatistics() {
    const total = this.tasks.length;
    const completed = this.tasks.filter(t => t.completed).length;
    const active = total - completed;
    const highPriorityCount = this.tasks.filter(t => t.priority === "high").length;

    return {
      total,
      active,
      completed,
      highPriorityCount
    };
  }

  /**
   * Hilfsmethode: Task nach ID suchen
   */
  getTaskById(id) {
    const numId = Number(id);
    return this.tasks.find(t => t.id === numId) || null;
  }

  /**
   * Hilfsmethode: Alle erledigten Aufgaben auf einmal löschen
   */
  clearCompleted() {
    const initialCount = this.tasks.length;
    this.tasks = this.tasks.filter(t => !t.completed);
    return initialCount - this.tasks.length;
  }
}
