/**
 * 🌐 MASTER 08: INTERAKTIVE TASK-APP (VIEW & CONTROLLER) 🌐
 * ==========================================================
 * Verbindet die TaskManager-Geschäftslogik mit einer modernen,
 * reaktiven Benutzeroberfläche im Browser.
 */

// Falls TaskManager noch nicht global vorhanden ist (z.B. Standalone):
if (typeof TaskManager === "undefined") {
  // Fallback Minimal-Implementation oder Import
  console.warn("TaskManager nicht gefunden. Lade Fallback-Definition.");
}

class TaskApp {
  constructor(rootElementId = "app") {
    this.root = document.getElementById(rootElementId) || document.body;
    this.manager = new TaskManager([
      { id: 1, title: "TypeScript Interfaces & Union Types verstehen", priority: "high", completed: true, dueDate: "2026-08-30", createdAt: new Date().toISOString() },
      { id: 2, title: "Model-View-Controller Architektur im Web umsetzen", priority: "high", completed: false, dueDate: "2026-09-01", createdAt: new Date().toISOString() },
      { id: 3, title: "Design System & Dark Mode Akzente optimieren", priority: "medium", completed: false, dueDate: "2026-09-05", createdAt: new Date().toISOString() },
      { id: 4, title: "Automatisierte Unittests mit 100% Abdeckung schreiben", priority: "low", completed: false, dueDate: null, createdAt: new Date().toISOString() }
    ]);

    this.currentFilter = "all";
    this.searchQuery = "";

    this.init();
  }

  init() {
    this.renderLayout();
    this.attachEventListeners();
    this.updateView();
  }

  renderLayout() {
    this.root.innerHTML = `
      <div class="task-app-wrapper" style="max-width: 820px; margin: 0 auto; font-family: var(--font-sans, system-ui, sans-serif);">
        <!-- App Header & Stats Bar -->
        <div style="background: linear-gradient(135deg, #1e1b4b 0%, #312e81 100%); color: white; padding: 24px; border-radius: 12px; margin-bottom: 24px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);">
          <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; margin-bottom: 16px;">
            <div>
              <h2 style="margin: 0; font-size: 1.5rem; font-weight: 800; display: flex; align-items: center; gap: 8px;">
                <span>🎯</span> Modern Task & Project Planner
              </h2>
              <p style="margin: 4px 0 0 0; font-size: 0.88rem; color: #c7d2fe;">Statussichere Aufgabenverwaltung mit TypeScript & Clean Architecture</p>
            </div>
            <button id="btn-clear-completed" class="btn" style="background: rgba(255,255,255,0.15); color: white; font-size: 0.82rem; padding: 6px 12px; border: 1px solid rgba(255,255,255,0.2); border-radius: 6px; cursor: pointer;">
              🧹 Erledigte aufräumen
            </button>
          </div>

          <!-- Statistik-Karten -->
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 10px;" id="stats-container">
            <div style="background: rgba(255,255,255,0.08); padding: 10px 14px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.1);">
              <div style="font-size: 0.72rem; text-transform: uppercase; color: #a5b4fc; font-weight: 700;">Gesamt</div>
              <div style="font-size: 1.4rem; font-weight: 800;" id="stat-total">0</div>
            </div>
            <div style="background: rgba(255,255,255,0.08); padding: 10px 14px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.1);">
              <div style="font-size: 0.72rem; text-transform: uppercase; color: #fde047; font-weight: 700;">Aktiv / Offen</div>
              <div style="font-size: 1.4rem; font-weight: 800; color: #fde047;" id="stat-active">0</div>
            </div>
            <div style="background: rgba(255,255,255,0.08); padding: 10px 14px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.1);">
              <div style="font-size: 0.72rem; text-transform: uppercase; color: #86efac; font-weight: 700;">Erledigt</div>
              <div style="font-size: 1.4rem; font-weight: 800; color: #86efac;" id="stat-completed">0</div>
            </div>
            <div style="background: rgba(255,255,255,0.08); padding: 10px 14px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.1);">
              <div style="font-size: 0.72rem; text-transform: uppercase; color: #fca5a5; font-weight: 700;">🔥 Hohe Prio</div>
              <div style="font-size: 1.4rem; font-weight: 800; color: #fca5a5;" id="stat-high">0</div>
            </div>
          </div>
        </div>

        <!-- Formular zum Hinzufügen -->
        <div style="background: white; border: 1px solid #e2e8f0; border-radius: 12px; padding: 18px; margin-bottom: 20px; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
          <form id="task-form" style="display: flex; flex-direction: column; gap: 12px;">
            <div style="display: flex; gap: 10px; flex-wrap: wrap;">
              <input type="text" id="task-input-title" placeholder="Was steht als Nächstes an? (z.B. API-Schnittstelle testen)" style="flex: 3; min-width: 220px; padding: 10px 14px; border: 1px solid #cbd5e1; border-radius: 8px; font-size: 0.95rem; outline: none;" required>
              <select id="task-select-priority" style="flex: 1; min-width: 130px; padding: 10px 12px; border: 1px solid #cbd5e1; border-radius: 8px; font-size: 0.9rem; background: white;">
                <option value="high">🔥 Hohe Priorität</option>
                <option value="medium" selected>⚡ Mittlere Priorität</option>
                <option value="low">🌱 Niedrige Priorität</option>
              </select>
              <input type="date" id="task-input-due" style="flex: 1; min-width: 140px; padding: 10px 12px; border: 1px solid #cbd5e1; border-radius: 8px; font-size: 0.9rem;">
              <button type="submit" class="btn" style="background: #4f46e5; color: white; border: none; padding: 10px 18px; border-radius: 8px; font-weight: 700; cursor: pointer; white-space: nowrap;">
                ➕ Hinzufügen
              </button>
            </div>
          </form>
        </div>

        <!-- Filter- & Suchleiste -->
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; margin-bottom: 16px;">
          <div style="display: flex; gap: 6px;" id="filter-buttons">
            <button data-filter="all" class="filter-btn active" style="padding: 6px 14px; border-radius: 20px; font-size: 0.85rem; font-weight: 600; cursor: pointer; border: 1px solid #4f46e5; background: #4f46e5; color: white;">Alle</button>
            <button data-filter="active" class="filter-btn" style="padding: 6px 14px; border-radius: 20px; font-size: 0.85rem; font-weight: 600; cursor: pointer; border: 1px solid #cbd5e1; background: white; color: #475569;">Aktiv</button>
            <button data-filter="completed" class="filter-btn" style="padding: 6px 14px; border-radius: 20px; font-size: 0.85rem; font-weight: 600; cursor: pointer; border: 1px solid #cbd5e1; background: white; color: #475569;">Erledigt</button>
          </div>

          <div style="position: relative; min-width: 220px;">
            <input type="text" id="search-input" placeholder="🔍 Aufgaben suchen..." style="width: 100%; padding: 6px 12px; border: 1px solid #cbd5e1; border-radius: 20px; font-size: 0.85rem; box-sizing: border-box; outline: none;">
          </div>
        </div>

        <!-- Task-Liste Container -->
        <div id="task-list" style="display: flex; flex-direction: column; gap: 8px;">
          <!-- Dynamisch gerenderte Aufgaben -->
        </div>
      </div>
    `;
  }

  attachEventListeners() {
    // Formular-Submit
    const form = document.getElementById("task-form");
    if (form) {
      form.addEventListener("submit", (e) => {
        e.preventDefault();
        const titleInput = document.getElementById("task-input-title");
        const prioritySelect = document.getElementById("task-select-priority");
        const dueInput = document.getElementById("task-input-due");

        const title = titleInput.value.trim();
        const priority = prioritySelect.value;
        const dueDate = dueInput.value || null;

        if (title) {
          try {
            this.manager.addTask(title, priority, dueDate);
            titleInput.value = "";
            dueInput.value = "";
            this.updateView();
          } catch (err) {
            alert(err.message);
          }
        }
      });
    }

    // Filter Buttons
    const filterContainer = document.getElementById("filter-buttons");
    if (filterContainer) {
      filterContainer.addEventListener("click", (e) => {
        const btn = e.target.closest("button[data-filter]");
        if (btn) {
          this.currentFilter = btn.getAttribute("data-filter");
          // Button-Stile aktualisieren
          filterContainer.querySelectorAll(".filter-btn").forEach((b) => {
            b.style.background = "white";
            b.style.color = "#475569";
            b.style.borderColor = "#cbd5e1";
          });
          btn.style.background = "#4f46e5";
          btn.style.color = "white";
          btn.style.borderColor = "#4f46e5";
          this.updateView();
        }
      });
    }

    // Live-Suche
    const searchInput = document.getElementById("search-input");
    if (searchInput) {
      searchInput.addEventListener("input", (e) => {
        this.searchQuery = e.target.value;
        this.updateView();
      });
    }

    // Erledigte aufräumen
    const clearBtn = document.getElementById("btn-clear-completed");
    if (clearBtn) {
      clearBtn.addEventListener("click", () => {
        if (confirm("Möchtest du alle erledigten Aufgaben wirklich entfernen?")) {
          this.manager.clearCompleted();
          this.updateView();
        }
      });
    }

    // Task-Liste Delegation (Toggle & Delete)
    const listContainer = document.getElementById("task-list");
    if (listContainer) {
      listContainer.addEventListener("click", (e) => {
        const target = e.target;
        const taskCard = target.closest("[data-task-id]");
        if (!taskCard) return;

        const id = Number(taskCard.getAttribute("data-task-id"));

        if (target.classList.contains("btn-delete") || target.closest(".btn-delete")) {
          this.manager.deleteTask(id);
          this.updateView();
        } else if (target.classList.contains("task-checkbox")) {
          this.manager.toggleTask(id);
          this.updateView();
        }
      });
    }
  }

  updateView() {
    this.renderStats();
    this.renderTasks();
  }

  renderStats() {
    const stats = this.manager.getStatistics();
    const elTotal = document.getElementById("stat-total");
    const elActive = document.getElementById("stat-active");
    const elCompleted = document.getElementById("stat-completed");
    const elHigh = document.getElementById("stat-high");

    if (elTotal) elTotal.textContent = stats.total;
    if (elActive) elActive.textContent = stats.active;
    if (elCompleted) elCompleted.textContent = stats.completed;
    if (elHigh) elHigh.textContent = stats.highPriorityCount;
  }

  renderTasks() {
    const container = document.getElementById("task-list");
    if (!container) return;

    const filtered = this.manager.getFilteredTasks(this.currentFilter, this.searchQuery);

    if (filtered.length === 0) {
      container.innerHTML = `
        <div style="background: white; border: 1px dashed #cbd5e1; border-radius: 10px; padding: 35px 20px; text-align: center; color: #64748b;">
          <div style="font-size: 2rem; margin-bottom: 8px;">✨</div>
          <div style="font-weight: 700; font-size: 1.05rem; color: #334155;">Keine Aufgaben gefunden</div>
          <div style="font-size: 0.85rem; margin-top: 4px;">Alle Aufgaben erledigt oder kein Treffer für den aktuellen Filter.</div>
        </div>
      `;
      return;
    }

    container.innerHTML = filtered
      .map((t) => {
        const priorityColors = {
          high: { bg: "#fee2e2", text: "#991b1b", label: "🔥 Hoch" },
          medium: { bg: "#fef3c7", text: "#92400e", label: "⚡ Mittel" },
          low: { bg: "#dcfce7", text: "#166534", label: "🌱 Niedrig" }
        };
        const p = priorityColors[t.priority] || priorityColors.medium;

        const dueHtml = t.dueDate
          ? `<span style="font-size: 0.75rem; color: #64748b; background: #f1f5f9; padding: 2px 8px; border-radius: 4px; display: inline-flex; align-items: center; gap: 4px;">
               📅 ${t.dueDate}
             </span>`
          : "";

        return `
          <div data-task-id="${t.id}" style="background: white; border: 1px solid ${t.completed ? "#e2e8f0" : "#cbd5e1"}; border-left: 5px solid ${t.priority === "high" ? "#ef4444" : t.priority === "medium" ? "#f59e0b" : "#10b981"}; border-radius: 8px; padding: 12px 16px; display: flex; align-items: center; justify-content: space-between; gap: 12px; transition: all 0.2s; ${t.completed ? "opacity: 0.65; background: #f8fafc;" : ""}">
            <div style="display: flex; align-items: center; gap: 12px; flex: 1;">
              <input type="checkbox" class="task-checkbox" ${t.completed ? "checked" : ""} style="width: 18px; height: 18px; cursor: pointer; accent-color: #4f46e5;">
              <div style="flex: 1;">
                <div style="font-weight: 600; font-size: 0.95rem; color: ${t.completed ? "#64748b" : "#0f172a"}; ${t.completed ? "text-decoration: line-through;" : ""}">
                  ${this.escapeHtml(t.title)}
                </div>
                <div style="display: flex; gap: 8px; align-items: center; margin-top: 4px; flex-wrap: wrap;">
                  <span style="font-size: 0.72rem; font-weight: 700; background: ${p.bg}; color: ${p.text}; padding: 2px 8px; border-radius: 99px;">
                    ${p.label}
                  </span>
                  ${dueHtml}
                </div>
              </div>
            </div>
            <button class="btn-delete" style="background: none; border: none; cursor: pointer; font-size: 1.1rem; padding: 4px 8px; border-radius: 4px; color: #94a3b8; transition: color 0.15s;" title="Aufgabe löschen">
              🗑️
            </button>
          </div>
        `;
      })
      .join("");
  }

  escapeHtml(str) {
    if (!str) return "";
    return str
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");
  }
}

// Bei DOMContentLoaded automatisch starten wenn im Browser
if (typeof document !== "undefined") {
  document.addEventListener("DOMContentLoaded", () => {
    if (document.getElementById("app") || document.getElementById("task-app-root")) {
      new TaskApp(document.getElementById("task-app-root") ? "task-app-root" : "app");
    }
  });
}
