/**
 * ✨ INTERAKTIVE UX-ERWEITERUNGEN FÜR PYTHON LERNPORTAL ✨
 * ========================================================
 * - Live-Suche & Filter über alle 27 Kapitel
 * - 1-Klick Code-Kopier-Buttons mit Checkmark-Animation
 * - Persistente Aufgaben-Checklisten (Checkboxen im Browser speichern)
 * - Sanftes Scrollen & Tastatur-Shortcuts
 */

(function () {
  document.addEventListener("DOMContentLoaded", () => {
    // 1. Code-Kopier-Buttons für alle Code-Blöcke
    document.querySelectorAll(".code-container").forEach((container) => {
      const header = container.querySelector(".code-header");
      const pre = container.querySelector("pre");
      if (!pre) return;

      const copyBtn = document.createElement("button");
      copyBtn.type = "button";
      copyBtn.className = "btn-copy-code";
      copyBtn.innerHTML = "<span>📋 Kopieren</span>";
      copyBtn.title = "Code in Zwischenablage kopieren";

      copyBtn.addEventListener("click", async () => {
        const codeText = pre.innerText;
        try {
          await navigator.clipboard.writeText(codeText);
          copyBtn.innerHTML = "<span>✅ Kopiert!</span>";
          copyBtn.classList.add("copied");
          setTimeout(() => {
            copyBtn.innerHTML = "<span>📋 Kopieren</span>";
            copyBtn.classList.remove("copied");
          }, 2000);
        } catch (err) {
          copyBtn.innerHTML = "<span>❌ Fehler</span>";
        }
      });

      if (header) {
        header.appendChild(copyBtn);
      } else {
        container.style.position = "relative";
        copyBtn.classList.add("btn-copy-floating");
        container.appendChild(copyBtn);
      }
    });

    // 2. Persistente Checkboxen in Aufgabenlisten
    const pageId = window.location.pathname;
    try {
      const savedChecks = JSON.parse(localStorage.getItem("task_checks_" + pageId) || "{}");
      document.querySelectorAll(".task-checkbox").forEach((cb, idx) => {
        const key = cb.id || "cb_" + idx;
        if (savedChecks[key]) {
          cb.checked = true;
          cb.closest(".task-item")?.classList.add("task-completed");
        }

        cb.addEventListener("change", () => {
          savedChecks[key] = cb.checked;
          localStorage.setItem("task_checks_" + pageId, JSON.stringify(savedChecks));
          if (cb.checked) {
            cb.closest(".task-item")?.classList.add("task-completed");
          } else {
            cb.closest(".task-item")?.classList.remove("task-completed");
          }
        });
      });
    } catch (e) {}

    // 3. Live-Suche & Filter für das Hauptportal
    const searchInput = document.getElementById("portal-search-input");
    if (searchInput) {
      const cards = document.querySelectorAll(".roadmap-card");
      searchInput.addEventListener("input", (e) => {
        const query = e.target.value.toLowerCase().trim();
        let matchCount = 0;

        cards.forEach((card) => {
          const text = card.innerText.toLowerCase();
          if (!query || text.includes(query)) {
            card.style.display = "flex";
            matchCount++;
          } else {
            card.style.display = "none";
          }
        });

        const countBadge = document.getElementById("search-results-count");
        if (countBadge) {
          if (query) {
            countBadge.innerText = `${matchCount} Kapitel gefunden`;
            countBadge.style.display = "inline-block";
          } else {
            countBadge.style.display = "none";
          }
        }
      });
    }
  });
})();
